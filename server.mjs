import { createHash, randomBytes, randomUUID, timingSafeEqual } from "node:crypto";
import { createServer } from "node:http";
import { mkdir, readFile, rename, writeFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import { dirname } from "node:path";

const port = Number(process.env.PAYMENT_PORT ?? 3001);
const host = process.env.PAYMENT_HOST ?? "127.0.0.1";
const adminPassword = process.env.PAYMENT_ADMIN_PASSWORD;
const cookieSecure = process.env.PAYMENT_COOKIE_SECURE === "true";
const sessionLifetimeMs = 8 * 60 * 60 * 1000;
const dataFile = fileURLToPath(new URL("./.data/payments.json", import.meta.url));
const projectRoutes = Object.freeze({
    all: { name: "All projects", redirectTo: "/" },
    chess: { name: "Chess & Arcade", redirectTo: "/chess-arcade/" },
    apikart: { name: "APIKart", redirectTo: "/apikart/" },
    eco: { name: "Eco / Everyday", redirectTo: "/eco/" },
    calculator: { name: "Orbit Calculator", redirectTo: "/calculator/" },
    python: { name: "Python Field Notes", redirectTo: "/main/roadmap.html" }
});
const adminSessions = new Map();
const loginAttempts = new Map();
const submissionAttempts = new Map();
const hash = (value) => createHash("sha256").update(value, "utf8").digest("hex");
let payments = [];
let persistQueue = Promise.resolve();

class HttpError extends Error {
    constructor(status, message) {
        super(message);
        this.status = status;
    }
}

function sendJson(response, status, value, headers = {}) {
    response.writeHead(status, {
        "Cache-Control": "no-store",
        "Content-Type": "application/json; charset=utf-8",
        "Referrer-Policy": "no-referrer",
        "X-Content-Type-Options": "nosniff",
        ...headers
    });
    response.end(JSON.stringify(value));
}

function isRateLimited(limits, key, maxAttempts, windowMs) {
    const now = Date.now();
    let entry = limits.get(key);
    if (!entry || now - entry.startedAt >= windowMs) {
        entry = { startedAt: now, count: 0 };
        limits.set(key, entry);
    }
    entry.count++;
    return entry.count > maxAttempts;
}

async function readJson(request) {
    if (!request.headers["content-type"]?.toLowerCase().startsWith("application/json")) {
        throw new HttpError(415, "Send the request as JSON.");
    }

    const chunks = [];
    let length = 0;
    let tooLarge = false;
    for await (const chunk of request) {
        length += chunk.length;
        if (length > 16_384) {
            tooLarge = true;
            continue;
        }
        chunks.push(chunk);
    }
    if (tooLarge) throw new HttpError(413, "The request is too large.");

    try {
        const body = JSON.parse(Buffer.concat(chunks).toString("utf8"));
        if (!body || typeof body !== "object" || Array.isArray(body)) {
            throw new HttpError(400, "The request body must be a JSON object.");
        }
        return body;
    } catch {
        throw new HttpError(400, "The request body must be a JSON object.");
    }
}

async function savePayments() {
    const serialized = JSON.stringify(payments, null, 2);
    const operation = persistQueue.then(async () => {
        await mkdir(dirname(dataFile), { recursive: true, mode: 0o700 });
        const temporaryFile = `${dataFile}.tmp`;
        await writeFile(temporaryFile, serialized, { encoding: "utf8", mode: 0o600 });
        await rename(temporaryFile, dataFile);
    });
    persistQueue = operation.catch((error) => {
        console.error("Could not save payment review data.", error.message);
    });
    await operation;
}

function getAdminSession(request) {
    const cookieHeader = request.headers.cookie ?? "";
    const token = cookieHeader.split(";").map((part) => part.trim())
        .find((part) => part.startsWith("payment_admin="))
        ?.slice("payment_admin=".length);
    if (!token) return null;
    const expiresAt = adminSessions.get(token);
    if (!expiresAt || expiresAt <= Date.now()) {
        adminSessions.delete(token);
        return null;
    }
    return token;
}

function requireAdmin(request) {
    if (!getAdminSession(request)) throw new HttpError(401, "Please sign in as an admin.");
}

function cleanPayment(payment) {
    const project = projectRoutes[payment.project];
    return {
        id: payment.id,
        project: payment.project,
        projectName: project.name,
        amount: payment.amount,
        utr: payment.utr,
        status: payment.status,
        createdAt: payment.createdAt,
        reviewedAt: payment.reviewedAt ?? null
    };
}

async function handleRequest(request, response) {
    const url = new URL(request.url ?? "/", `http://${request.headers.host ?? "localhost"}`);
    const ip = request.socket.remoteAddress ?? "unknown";

    if (request.method === "GET" && url.pathname === "/api/health") {
        sendJson(response, 200, { ready: true });
        return;
    }

    if (request.method === "POST" && url.pathname === "/api/payments") {
        if (isRateLimited(submissionAttempts, ip, 10, 60 * 60 * 1000)) {
            throw new HttpError(429, "Too many submissions. Wait before trying again.");
        }
        const body = await readJson(request);
        const project = projectRoutes[body.project];
        const amount = body.amount;
        const utr = typeof body.utr === "string" ? body.utr.trim().toUpperCase() : "";
        if (!project || !Number.isInteger(amount) || amount < 1 || amount > 100_000) {
            throw new HttpError(400, "Select a valid project and enter an amount from ₹1 to ₹1,00,000.");
        }
        if (!/^[A-Z0-9]{6,32}$/.test(utr)) {
            throw new HttpError(400, "Enter a valid UTR or transaction reference using 6–32 letters or numbers.");
        }
        if (payments.some((payment) => payment.utr === utr)) {
            throw new HttpError(409, "This UTR was already submitted. Contact the project owner if you need help.");
        }

        const statusToken = randomBytes(32).toString("base64url");
        const payment = {
            id: randomUUID(),
            project: body.project,
            amount,
            utr,
            status: "pending",
            statusTokenHash: hash(statusToken),
            createdAt: new Date().toISOString()
        };
        payments.push(payment);
        await savePayments();
        sendJson(response, 201, { id: payment.id, statusToken, status: payment.status });
        return;
    }

    const statusMatch = url.pathname.match(/^\/api\/payments\/([0-9a-f-]{36})$/i);
    if (request.method === "GET" && statusMatch) {
        const payment = payments.find((entry) => entry.id === statusMatch[1]);
        const statusToken = request.headers.authorization?.match(/^Bearer ([A-Za-z0-9_-]{32,64})$/)?.[1];
        const suppliedTokenHash = statusToken ? Buffer.from(hash(statusToken), "hex") : Buffer.alloc(0);
        const savedTokenHash = payment ? Buffer.from(payment.statusTokenHash, "hex") : Buffer.alloc(0);
        const tokenMatches = suppliedTokenHash.length === savedTokenHash.length
            && suppliedTokenHash.length > 0
            && timingSafeEqual(suppliedTokenHash, savedTokenHash);
        if (!payment || !tokenMatches) {
            throw new HttpError(404, "Payment review not found.");
        }
        const project = projectRoutes[payment.project];
        sendJson(response, 200, {
            status: payment.status,
            project: payment.project,
            projectName: project.name,
            ...(payment.status === "approved" ? { redirectTo: project.redirectTo } : {}),
            ...(payment.status === "rejected" ? { reviewedAt: payment.reviewedAt } : {})
        });
        return;
    }

    if (request.method === "POST" && url.pathname === "/api/admin/login") {
        if (isRateLimited(loginAttempts, ip, 5, 15 * 60 * 1000)) {
            throw new HttpError(429, "Too many login attempts. Try again later.");
        }
        const body = await readJson(request);
        const suppliedDigest = hash(typeof body.password === "string" ? body.password : "");
        const expectedDigest = hash(adminPassword);
        if (!timingSafeEqual(Buffer.from(suppliedDigest), Buffer.from(expectedDigest))) {
            throw new HttpError(401, "The admin password is incorrect.");
        }
        const sessionToken = randomBytes(32).toString("base64url");
        adminSessions.set(sessionToken, Date.now() + sessionLifetimeMs);
        const cookie = [
            `payment_admin=${sessionToken}`,
            "HttpOnly",
            "SameSite=Strict",
            "Path=/api/admin",
            `Max-Age=${sessionLifetimeMs / 1000}`,
            ...(cookieSecure ? ["Secure"] : [])
        ].join("; ");
        sendJson(response, 200, { authenticated: true }, { "Set-Cookie": cookie });
        return;
    }

    if (request.method === "POST" && url.pathname === "/api/admin/logout") {
        const session = getAdminSession(request);
        if (session) adminSessions.delete(session);
        sendJson(response, 200, { authenticated: false }, {
            "Set-Cookie": `payment_admin=; HttpOnly; SameSite=Strict; Path=/api/admin; Max-Age=0${cookieSecure ? "; Secure" : ""}`
        });
        return;
    }

    if (request.method === "GET" && url.pathname === "/api/admin/payments") {
        requireAdmin(request);
        const pending = payments
            .filter((payment) => payment.status === "pending")
            .sort((left, right) => left.createdAt.localeCompare(right.createdAt))
            .map(cleanPayment);
        sendJson(response, 200, { payments: pending });
        return;
    }

    const reviewMatch = url.pathname.match(/^\/api\/admin\/payments\/([0-9a-f-]{36})\/review$/i);
    if (request.method === "POST" && reviewMatch) {
        requireAdmin(request);
        const body = await readJson(request);
        if (body.decision !== "approved" && body.decision !== "rejected") {
            throw new HttpError(400, "Choose approve or reject.");
        }
        const payment = payments.find((entry) => entry.id === reviewMatch[1]);
        if (!payment) throw new HttpError(404, "Payment review not found.");
        if (payment.status !== "pending") throw new HttpError(409, "This payment has already been reviewed.");

        payment.status = body.decision;
        payment.reviewedAt = new Date().toISOString();
        await savePayments();
        sendJson(response, 200, { payment: cleanPayment(payment) });
        return;
    }

    throw new HttpError(404, "API endpoint not found.");
}

async function start() {
    if (!adminPassword || adminPassword.length < 16) {
        throw new Error("Set PAYMENT_ADMIN_PASSWORD to a private password with at least 16 characters before starting the payment server.");
    }
    if (!Number.isInteger(port) || port < 1 || port > 65535) throw new Error("PAYMENT_PORT must be a valid TCP port.");

    await mkdir(dirname(dataFile), { recursive: true, mode: 0o700 });
    try {
        const existing = JSON.parse(await readFile(dataFile, "utf8"));
        if (!Array.isArray(existing)) throw new Error("Payment review data must be a JSON array.");
        payments = existing;
    } catch (error) {
        if (error.code !== "ENOENT") throw error;
    }

    const server = createServer((request, response) => {
        handleRequest(request, response).catch((error) => {
            if (response.headersSent) {
                response.destroy(error);
                return;
            }
            if (error instanceof HttpError) {
                sendJson(response, error.status, { error: error.message });
                return;
            }
            console.error("Payment API request failed.", error.message);
            sendJson(response, 500, { error: "The payment service could not complete the request." });
        });
    });

    server.requestTimeout = 15_000;
    server.headersTimeout = 17_000;
    server.listen(port, host, () => {
        console.log(`Payment review API listening at http://${host}:${port}`);
        console.log("Admin review page: /payment.hub/admin.html");
        console.log("Payment records are stored privately in payment.hub/.data/.");
    });
}

start().catch((error) => {
    console.error("Payment API startup failed.", error.message);
    process.exitCode = 1;
});
