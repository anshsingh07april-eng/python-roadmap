# Four Small Web Projects

A collection of five independent, browser-based projects, built with TypeScript, Three.js, chess.js, HTML, CSS, and Vite. The root page summarizes and links to each project; the Payment Hub provides UPI checkout and an admin-reviewed UTR verification flow.

## Project summary

| Folder | Page | What it does |
| --- | --- | --- |
| `main/roadmap.html` | Python Field Notes | Day-by-day roadmap checklist, focus timer, streak, notes, and local progress export. |
| `chess-arcade/` | Astra Chess & Arcade | 3D chess against a local AI plus Checkers, Connect Four, Tic-Tac-Toe, Snake, and 2048. |
| `calculator/` | Orbit Calculator | Arithmetic with keyboard input, a rotatable 3D case, and floating-key animation. |
| `eco/` | Eco / Everyday | Everyday sustainability ideas and an illustrative annual-impact estimator. |
| `apikart/` | APIKart Store | E-commerce storefront demo with product search, category filters, a local cart, and simulated checkout. |
| `payment.hub/payment.html` | Project Payment Hub | Send a UPI payment, submit its UTR for manual admin verification, and open the chosen project once approved. |
| `payment.hub/admin.html` | Payment Reviews | Password-protected admin queue for matching submitted UTRs and amounts against the recipient's own UPI or bank transaction history. |

Each page is in its own directory with its own `index.html`. Shared project navigation connects the four experiences.

## Run locally

1. Install Node.js 20.19+ or 22.12+.
2. From the project folder, run `npm install`.
3. Configure and run the private payment review API in its own PowerShell window:
   ```powershell
   $env:PAYMENT_ADMIN_PASSWORD = "replace-with-a-private-password-of-at-least-16-characters"
   npm run payment:api
   ```
4. In a second window, run `npm run dev` and open the local URL printed by Vite. Use `/` for the overview, `/main/roadmap.html` for Python Field Notes, or append `/chess-arcade/` for the games.
5. Run `npm run build` to type-check and create the production site in `dist/`.
   - Alternatively on Windows, double-click `start-games.bat` to start Vite and open the game page.
   - The 3D chess/arcade page needs a local web server; opening its HTML file directly will display a launch instruction because browsers block its module imports under `file://`.

## Play

### Astra Chess & Arcade

- Select a white piece to show its legal moves, then click a highlighted square.
- Drag the board to rotate the camera, scroll to zoom, or use **Reset view**.
- Choose Thoughtful, Challenging, or Grandmaster for Astra's local minimax chess engine.
- Use **Undo** to rewind your last move and Astra's reply; **New game** resets the match.
- Castling, en passant, check, checkmate, stalemate, draws, and pawn promotion follow standard chess rules.
- Choose **More games** for Checkers, Connect Four, Tic-Tac-Toe, Snake, or 2048.
- Checkers, Connect Four, and Tic-Tac-Toe include computer opponents. Snake supports keyboard and touch direction controls; 2048 supports arrow/WASD keys and touch swipes. Their best scores are saved in this browser.

Astra's chess opponent and all arcade games run locally in the browser; they do not use an online AI service.

### Orbit Calculator

Use the on-screen keypad or keyboard for basic arithmetic. Drag the calculator body to rotate it; **Reset view** returns the front. **Shake the keys** plays the floating animation.

### Eco / Everyday

Select habits to see an illustrative annual estimate. It is not a formal emissions calculation.

### APIKart Store

Browse sample products, search and filter the collection, change quantities in the cart, and preview checkout. The cart is saved in browser local storage. Checkout does not process payments or save submitted contact details.

### Project Payment Hub

Open `/payment.hub/payment.html` to choose a project, set a suggested or custom rupee amount, then open a UPI app or scan a locally generated payment QR code. After paying, submit the UTR from the payment app's transaction details. The admin signs in at `/payment.hub/admin.html`, compares the submitted UTR and exact amount against the recipient's own UPI or bank transaction history, and approves or rejects the claim. Only an approved payment is shown as verified and redirected to its chosen project.

The server does not connect to a bank or verify UPI transactions automatically. A submitted UTR or screenshot is not proof of settlement: the recipient must independently check their account before approving. The API requires a private `PAYMENT_ADMIN_PASSWORD` of at least 16 characters, rate-limits submissions and sign-in attempts, stores review records in the git-ignored `payment.hub/.data/` directory, and binds to `127.0.0.1` by default. Keep the data directory private and backed up. For a public deployment, use HTTPS, set `PAYMENT_COOKIE_SECURE=true`, put the API behind a same-origin reverse proxy, and provide persistent private storage. The JSON file store is for a single API instance; use a transactional database before running multiple instances or accepting high payment volume. Static hosting without the API cannot accept UTRs or verify payments.

### Python Field Notes

Open `/main/roadmap.html` to follow the Python Mastery Roadmap from November 3, 2026 through February 28, 2027. The weekly calendar includes the roadmap's daily learning routine, weekly lighter review days, and dated learning checkpoints. Check off work as you complete it, log notes, and use the focus timer to add completed study blocks to your daily total. Progress is saved in this browser's local storage; use **Export progress** to download a JSON backup.

To open the tracker automatically when you sign in to Windows, double-click `install-python-roadmap-startup.bat` once. It adds a shortcut to your personal Startup folder; remove that shortcut to disable automatic launch. The shortcut opens the standalone page in your default browser, so it does not need a server or an internet connection. You can also use `npm run dev` to open it at `/main/roadmap.html`. The site encourages practice but cannot lock or control other apps.
