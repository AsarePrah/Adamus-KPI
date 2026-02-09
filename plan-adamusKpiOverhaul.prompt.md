## Plan: Adamus KPI Overhaul & Separation

This plan transitions the project from a monolithic HTML file to a separated architecture with a **Python/FastAPI backend** and a **Vanilla HTML/CSS/JS frontend**.

### Steps
1. **Initialize Project Structure**
   - Create `backend/` and `frontend/` directories.
   - **Backend**: Set up Python virtual environment, install FastAPI, SQLModel, Uvicorn.
   - **Frontend**: Create basic structure: `index.html`, `css/style.css`, `js/app.js`.

2. **Design Database & Models (Backend)**
   - Create `backend/models.py` using **SQLModel** (combining SQLAlchemy & Pydantic).
   - Define entities: `Employee` (with role/dept), `LeaveRequest`, and `KPIRecord` (using a JSON field for flexible metric storage per dept).
   - Implement `backend/database.py` to handle SQLite connection and initialization.

3. **Implement Core API Endpoints**
   - Create `backend/main.py` entry point.
   - **Auth**: `/login` (Simple token-based or session).
   - **Employees**: `/employees` (List/Add).
   - **Leaves**: `/leaves` (Apply/Approve).
   - **KPIs**: `/kpi/{department}` (Get/Post). Implement the "Previous MTD" lookup logic here to support calculation chains.
   - **Serving Frontend**: Configure FastAPI to serve the `frontend/` directory as static files.

4. **Frontend Architecture & Design System**
   - **CSS**: Create `frontend/css/style.css`. Manually implement the color palette (Indigo/Green/Red) and shadow utilities from `DESIGN_SYSTEM.md` using CSS Variables (`:root`).
   - **JS Architecture**: Split logic into simple files:
     - `js/api.js`: Wrapper functions for `fetch` calls to the backend.
     - `js/dom.js`: Helper functions for manipulating the DOM (showing/hiding sections, creating elements).
     - `js/calculations.js`: The "Calculation Chain" logic ported from the original monolith.

5. **Migrate Logic & Build UI**
   - **Dashboard**: Recreate the Department inputs using standard HTML Forms. Attach `input` event listeners to trigger the vanilla JS calculation chains (Daily $\to$ Variance $\to$ MTD) provides immediate feedback.
   - **Admin Panel**: Build simple forms for adding Employees and approving Leave.
   - **Navigation**: Use simple element visibility toggling (e.g., `document.getElementById('section').style.display = 'block'`) to switch between views.

### Further Considerations
1. **Calculation Logic Location**: Interactive logic (Daily $\to$ MTD) remains in `frontend/js/calculations.js` for responsiveness. The Backend will validate data upon submission.
2. **Migration**: We will start with a fresh database structure (SQLite).
3. **Libraries**:
   - **Charts**: Use **Chart.js** via CDN for simple, beginner-friendly charts (easier than raw Canvas).
   - **Icons**: Use a CDN link for **FontAwesome** or **Google Material Icons**.
   - No build tools (Webpack/Vite) required; run directly via the Python backend.
