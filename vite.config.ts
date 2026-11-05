import { defineConfig } from "vite";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const workspace = fileURLToPath(new URL(".", import.meta.url));
const paymentApiProxy = {
    "/api": {
        target: process.env.PAYMENT_API_TARGET ?? "http://127.0.0.1:3001",
        changeOrigin: true,
    },
};

export default defineConfig({
    base: "./",
    server: { proxy: paymentApiProxy },
    preview: { proxy: paymentApiProxy },
    build: {
        rollupOptions: {
            input: {
                home: resolve(workspace, "index.html"),
                paymentHub: resolve(workspace, "payment.hub/payment.html"),
                paymentAdmin: resolve(workspace, "payment.hub/admin.html"),
                pythonRoadmap: resolve(workspace, "main/roadmap.html"),
                chessArcade: resolve(workspace, "chess-arcade/index.html"),
                calculator: resolve(workspace, "calculator/index.html"),
                eco: resolve(workspace, "eco/index.html"),
                apikart: resolve(workspace, "apikart/index.html"),
            },
            output: {
                manualChunks: {
                    "chess-engine": ["chess.js"],
                    "three-core": ["three"],
                },
            },
        },
    },
});
