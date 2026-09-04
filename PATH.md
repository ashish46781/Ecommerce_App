# Backend E-Commerce Learning Path

## Goal

Build and understand a production-style FastAPI e-commerce and order-management
backend suitable for a strong fresher portfolio and backend interviews.

## Current Stage

Stage 1 - Foundation.

## Current Lesson

Lesson 1: Run a minimal FastAPI application and trace an HTTP request.
Implementation reviewed and verified. Understanding is pending discussion of
server versus application and HTTP method/path routing.
Next implementation lesson: application configuration and environment variables.

## Completed

- [x] Inspect the workspace: no existing files, code, tests, or Git history.
- [x] Establish permanent teaching rules and the staged learning roadmap.
- [x] Lesson 1 implementation: Python 3.13 virtual environment, minimal FastAPI app,
  GET / JSON response, pinned direct dependencies, and Git initialized on main.
- [x] Lesson 1 verification: real HTTP checks for root JSON (200), documentation
  HTML (200), OpenAPI route definition, unknown route (404), and wrong method (405).
  Dependency compatibility and Python compilation checks passed.

## Next

- [ ] Discuss Lesson 1 understanding before marking the learning milestone complete.
- [ ] Lesson 2: Application configuration and environment variables.
- [ ] Select PostgreSQL or MySQL and configure a local database connection.
- [ ] Understand SQLAlchemy engine, session lifecycle, and request-scoped sessions.
- [ ] Understand and implement the Product database model.
- [ ] Define Product request/response schemas with Pydantic.
- [ ] Implement POST /products and understand commit and refresh.
- [ ] Implement product list/detail endpoints, then update/delete in small lessons.
- [ ] Introduce Category, then its relationship with Product in Stage 2.

## Stage Roadmap

1. Foundation: application setup, configuration, database, SQLAlchemy, schemas, CRUD.
2. Database design: keys, constraints, Category-to-Product relationship, useful indexes.
3. Users and authentication: User, password hashing, registration, login, JWT verification.
4. Authorization: customer/seller/admin roles, permissions, and ownership checks.
5. Cart: Cart/CartItem, quantities, related data, validation, ownership.
6. Orders and inventory: checkout, order history/status, transactions, race conditions.
7. Migrations: Alembic revisions and schema evolution when manual changes become painful.
8. Testing: pytest, fixtures, isolated databases, authentication and business behavior.
9. Redis: a justified product/category cache, TTL, stale data, and invalidation.
10. Background work: confirmation/notification work using the simplest suitable approach.
11. Docker: images, containers, ports, volumes, networks, and Compose for multiple services.
12. Production improvements: errors, logging, pagination, query performance, documentation.
13. CI/CD and deployment: automated checks, secrets, production configuration, public hosting.

Move a topic earlier only when a real project need justifies it; record the reason.
Split large stages into focused lessons and review the project after each stage.

## Concepts Learned

No new concepts confirmed yet. Lesson 1 introduces or revisits virtual environments,
server versus application, import targets, method/path routing, JSON serialization,
and the distinction between 404 and 405 responses.

## Technologies Introduced

- Python 3.13.2 and a local `.venv`.
- FastAPI 0.141.1 and Uvicorn 0.52.4.
- pip, `requirements.txt`, Git, and `.gitignore`.
- Pydantic is installed as a FastAPI dependency; schema design has not been taught.

## Postponed Until Needed

- Database vendor choice and installation: at the database connection lesson.
- SQLAlchemy and Pydantic schema design: at the relevant foundation lessons.
- Authentication/JWT and RBAC: after product/database foundations.
- Alembic: when evolving an existing schema makes migrations useful.
- pytest and test database architecture: when meaningful behavior needs protection.
- Redis: after identifying a worthwhile caching use case.
- BackgroundTasks or a task queue: when concrete background work exists.
- Docker/Compose: when coordinating multiple services becomes useful.
- CI/CD, deployment, and the full professional README: as the application matures.
- Refresh tokens: after access-token authentication is understood and a need appears.
- Service/repository layers: only if actual code complexity warrants them.

## Important Decisions

### Start with one application module

Keep the FastAPI application and first route in `app/main.py`.
Reason: one route does not yet justify routers or additional architectural layers.

### Use an isolated Python 3.13 environment

Use `.venv` and invoke its Python explicitly in local commands.
Reason: the machine's default `python` points to 3.10; an explicit interpreter avoids
installing dependencies into or starting the server from the wrong environment.

## Technical Debt to Revisit

- Direct dependencies are pinned; full transitive dependency locking is deferred
  until reproducible CI/deployment setup. No pytest suite yet; first behavior was
  verified with temporary standard-library HTTP checks.

## Local Commands

Run from the repository root in PowerShell; activation is optional when using the
virtual environment's interpreter explicitly.

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

API: http://127.0.0.1:8000/ - interactive documentation: http://127.0.0.1:8000/docs.
Use `--reload` for local development; it restarts the server after Python edits.
