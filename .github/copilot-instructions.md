# Copilot Instructions for Adamus KPI Codebase

## Architecture & Big Picture
- **Single-File Monolith**: The entire application lives in `KPI.html`. This includes the HTML structure, CSS styling (embedded `<style>`), and business logic (embedded `<script>`).
- **Client-Side Persistence**: Data is stored exclusively in `localStorage` under the key `leave_demo_data`. There is no active backend connection in the HTML version.
- **State Management**: A global `state` object holds `employees`, `leave_requests`, and departmental `kpi_records`. All modules read/write to this central state.

## Core Developer Workflows
- **Running the App**: Open `KPI.html` directly in a browser or serve via `python -m http.server`. No build step (Design/Compile) is required.
- **Debugging**: 
  - Logic functions (e.g., `doLogin`, `addKPIRecord`) are exposed globally. Call them from the browser console to test.
  - Data inspection: check `JSON.parse(localStorage.getItem('leave_demo_data'))` in console.
- **Testing**:
  - `test_app.py` references a `Main.py` (CLI version) which may not be present. Focus testing on browser interactions for `KPI.html`.
  - Validate logic changes by verifying the "Calculation Chains" (see below).

## Project-Specific Patterns
- **Departmental Prefixes**: DOM IDs and variable names are strictly prefixed by department:
  - `geo` (Geology)
  - `crush` (Crushing)
  - `mill` (Milling/CIL)
  - `ohs` (Health & Safety)
- **Calculation Chains**: KPI logic uses specific event listeners to trigger cascading updates. 
  - Example Pattern: `Daily Input` -> `update...DailyForecast` -> `compute...Var` -> `compute...MTD`.
  - When modifying a calculation, trace the entire chain of dependencies to ensure downstream variances (`Var1`, `Var2`, `Var3`) update correctly.
- **Vanilla JS & DOM**:
  - Use `document.getElementById` extensively.
  - Avoid adding external libraries; maintain the "zero-dependency" nature of the file.
- **Styling**:
  - Use CSS Variables defined in `:root` (e.g., `--primary`, `--bg-secondary`) for all colors.
  - Follow the card/shadow design system: `class="card"`, `var(--shadow)`.

## Critical Files
- `KPI.html`: The application. Contains ~8000 lines. Use Search/Find to navigate between "Logic Layout" (bottom scripts) and "UI Layout" (HTML body).
- `DESIGN_SYSTEM.md`: Source of truth for color palette and typography.
- `README.md` & `QUICK_START.md`: Operational guides (though note that strictly backend instructions might apply to the CLI version).
