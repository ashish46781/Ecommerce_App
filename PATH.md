# Backend E-Commerce Learning Path

## Goal

Build and understand a production-style FastAPI e-commerce and order-management
backend suitable for a strong fresher portfolio and backend interviews.

Repository: https://github.com/ashish46781/Ecommerce_App

## Current Stage

Stage 1 - Foundation.

## Current Lesson

Lesson 5: Product SQLAlchemy model and first application table.
Implemented and verified. Teaching covers declarative mapping, metadata, columns,
database-generated primary keys, nullability, exact numeric money, and the boundary
between ORM models and API schemas. No assessment gate.
Next lesson: define Product request and response schemas with Pydantic.

## Completed

- [x] Inspect the workspace: no existing files, code, tests, or Git history.
- [x] Establish permanent teaching rules and the staged learning roadmap.
- [x] Lesson 1 implementation: Python 3.13 virtual environment, minimal FastAPI app,
  GET / JSON response, pinned direct dependencies, and Git initialized on main.
- [x] Lesson 1 verification: real HTTP checks for root JSON (200), documentation
  HTML (200), OpenAPI route definition, unknown route (404), and wrong method (405).
  Dependency compatibility and Python compilation checks passed.
- [x] Lesson 1 explanation: server/application responsibilities and HTTP routing.
- [x] Lesson 2 implementation: typed application name and debug flag in
  `app/config.py`, FastAPI integration, `.env.example`, and an ignored local `.env`.
- [x] Lesson 2 verification: defaults, dotenv loading, environment overrides,
  boolean conversion, missing dotenv fallback, and invalid-value startup rejection.
  Real HTTP checks confirmed the configured name in JSON and documentation;
  existing route behavior, dependency compatibility, and compilation also passed.
- [x] Lesson 3 implementation: PostgreSQL `ecommerce` database, limited
  `ecommerce_app` owner role, typed connection settings, Psycopg driver, and a
  reusable synchronous SQLAlchemy engine in `app/database.py`.
- [x] Lesson 3 verification: live `SELECT 1`, server/database/user identity,
  database ownership, restricted role privileges, password authentication,
  redacted URL rendering, dependency compatibility, compilation, and API behavior.
- [x] Lesson 4 implementation: module-level `SessionFactory` and a `get_db()` yield
  dependency that creates and closes one SQLAlchemy Session per FastAPI request.
- [x] Lesson 4 verification: distinct sessions share the engine, execute real queries,
  and return connections to the pool after successful and failed HTTP requests.
- [x] Lesson 5 implementation: shared declarative `Base`, a focused `Product` model,
  and a temporary, repeatable command for creating the `products` table.
- [x] Lesson 5 verification: PostgreSQL column types, nullability, identity primary
  key, repeatable table creation, and an ORM insert/load/rollback cycle.

## Next

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

- Lesson 1: virtual environments, server versus application, import targets,
  method/path routing, JSON serialization, and 404 versus 405 responses.
- Lesson 2: configuration versus application logic, process environments, `.env`
  loading, type conversion/validation, source priority, startup settings lifetime,
  debug versus reload, and keeping local configuration outside Git.
- Lesson 3: database server versus client, connection components, PostgreSQL roles
  and ownership, least privilege, SQLAlchemy dialect/driver selection, lazy engine
  connections, connection context management, and secret redaction versus encryption.
- Lesson 4: engine versus connection versus session, `sessionmaker`, unit of work,
  identity map, automatic transaction start, request-scoped dependency injection,
  session concurrency boundaries, explicit commit ownership, and guaranteed cleanup.
- Lesson 5: declarative ORM mapping, `Base` and metadata, tables versus model classes,
  rows versus objects, columns versus attributes, primary keys, identity generation,
  nullability inferred from `Mapped` annotations, `Numeric`/`Decimal` for money,
  `create_all()` limitations, and ORM models versus API schemas.

These record teaching coverage, not assessed mastery.

## Technologies Introduced

- Python 3.13.2 and a local `.venv`.
- FastAPI 0.141.1 and Uvicorn 0.52.4.
- Pydantic Settings 2.15.0; python-dotenv is its dependency for reading `.env` files.
- PostgreSQL 17.4, SQLAlchemy 2.0.52, and Psycopg 3.2.10.
- pip, `requirements.txt`, Git, and `.gitignore`.
- Pydantic is installed as a FastAPI dependency; schema design has not been taught.

## Postponed Until Needed

- Pydantic request and response schema design: in the next foundation lesson.
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

### Load typed settings once at startup

Use one `Settings` class and one module-level instance in `app/config.py`.
For the sources we use, process variables override `.env`, which overrides defaults.
Reason: validate configuration before serving requests and reuse it without per-request
file reads. Add more settings only when used. Debug defaults to false.

### Keep local configuration outside Git

Track `.env.example` with public defaults; ignore the actual `.env`.
The `.env` path is relative to the working directory, so run from the repository root.
Restart the server after changing configuration; Python reload need not watch `.env`.
Reason: share setup instructions without committing machine-specific values or secrets.

### Use PostgreSQL with a dedicated application role

Use the installed PostgreSQL 17 server. The `ecommerce_app` role owns the `ecommerce`
database but cannot create databases or roles and is not a superuser.
Reason: PostgreSQL supports the relational, transactional, and concurrency lessons
ahead, and separating administration from application access limits accidental damage.

### Build the SQLAlchemy URL from typed components

Store database host, port, name, user, and password as settings. Build a
`postgresql+psycopg` URL with `URL.create()` and configure one synchronous engine.
Reason: programmatic URL construction handles special characters in passwords safely,
the explicit dialect/driver is unambiguous, and sync access matches our current routes.
The engine connects lazily; creating it alone does not prove the server is reachable.

### Use one SQLAlchemy Session per request

Keep the engine and `SessionFactory` at module scope. `get_db()` creates a new Session,
yields it to one request, and closes it through a context manager after the request.
Reason: a Session contains mutable ORM and transaction state and is unsafe to share
across concurrent requests. The dependency does not commit automatically; each write
operation owns its commit decision, while cleanup rolls back unfinished work.

### Start Product with its essential persistence fields

Map `Product` to `products` with an identity integer primary key, required name,
optional description, exact `NUMERIC(10, 2)` price, and integer stock. Use Python
`Decimal` for prices to avoid binary floating-point rounding. Category relationships,
timestamps, and business constraints will be introduced when their lessons can explain
the problems they solve.

### Bootstrap the first table before introducing migrations

Use `Base.metadata.create_all()` through `python -m app.create_tables` for the first
table. It can create a missing table and can be rerun, but it does not modify an
existing table to match later model changes. Replace this bootstrap workflow with
Alembic when the schema begins evolving.

## Technical Debt to Revisit

- Direct dependencies are pinned; full transitive dependency locking is deferred
  until reproducible CI/deployment setup. No pytest suite yet; first behavior was
  verified with temporary standard-library HTTP checks.
- `create_all()` can create missing tables but cannot migrate an existing schema.
  Introduce Alembic when the Product schema or relationships begin evolving.
- Product price and stock do not yet have database `CHECK` constraints; add and teach
  those with database constraints in Stage 2. Category and timestamps are also deferred.

## Local Commands

Run from the repository root in PowerShell; activation is optional when using the
virtual environment's interpreter explicitly.

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m app.create_tables
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

On a fresh clone, optionally copy `.env.example` to `.env` before starting the API:
`Copy-Item .env.example .env`. Do not overwrite an existing local `.env`.
`APP_NAME` controls the API title and root message. `DEBUG` controls error tracebacks;
keep it false for public use. A local `.env` with example defaults already exists.
Database settings default to the local `ecommerce` database and `ecommerce_app` role;
`DATABASE_PASSWORD` is required and belongs only in `.env` or the process environment.

API: http://127.0.0.1:8000/ - interactive documentation: http://127.0.0.1:8000/docs.
Use `--reload` for local development; it restarts the server after Python edits.
