# Leave Management App (Demo)

This workspace contains two interfaces for a Leave Management app:

- `Main.py` — A terminal/CLI application that persists data to `leave_data.json`.
- `leave.html` — A single-file browser demo (full CSS included) that stores data in browser `localStorage`.

Files added by this update:
- `leave.html` — Browser UI with all CSS inlined. Open in any modern browser.
- `test_app.py` — Non-interactive smoke test for `Main.py` (creates a temporary test data file).

Quick start
-----------

Run CLI app (Python 3.8+ recommended):

```powershell
python Main.py
```

Open the browser demo:

- Double-click `leave.html` or open it in your browser. Data is saved to `localStorage` under the key `leave_demo_data`.

Run the smoke test (automated):

```powershell
python test_app.py
```

The test script uses a temporary file `test_leave_data.json` and removes it when finished.

Notes
-----
- The CLI and browser demo are independent: the browser version uses `localStorage`, the CLI uses a JSON file.
- If you want a unified server-backed app, I can scaffold a Flask/Django backend and connect the HTML UI to it.

Next steps
----------
If you'd like, I can:
- Add an HTML frontend that talks to the `Main.py` backend via a small HTTP API.
- Convert the CLI app into a Flask API + SPA using the existing `leave.html` UI.
- Add user authentication and role-based approvals.

