# Backend E-Commerce Learning Path

## Goal

Build and understand a production-style FastAPI e-commerce and order-management
backend suitable for a strong fresher portfolio and backend interviews.

Repository: https://github.com/ashish46781/Ecommerce_App

## Current Stage

Stage 2 - Database design.
Stage 1 - Foundation is complete.

## Current Lesson

Stage 2 - Lesson 2: adopt Alembic and baseline the existing Product and Category schema.
Implemented and verified. Teaching covers migration history, revisions, upgrade and
downgrade functions, head and base, the version table, schema comparison, and stamping
an audited existing database without recreating its tables.
Next lesson: Stage 2 - Lesson 3: add the Category-to-Product relationship with an
Alembic migration.

## Completed

- [x] Inspect the workspace: no existing files, code, tests, or Git history.
- [x] Establish permanent teaching rules and the staged learning roadmap.
- [x] Stage 1 - Lesson 1 implementation: Python 3.13 virtual environment, minimal FastAPI app,
  GET / JSON response, pinned direct dependencies, and Git initialized on main.
- [x] Stage 1 - Lesson 1 verification: real HTTP checks for root JSON (200), documentation
  HTML (200), OpenAPI route definition, unknown route (404), and wrong method (405).
  Dependency compatibility and Python compilation checks passed.
- [x] Stage 1 - Lesson 1 explanation: server/application responsibilities and HTTP routing.
- [x] Stage 1 - Lesson 2 implementation: typed application name and debug flag in
  `app/config.py`, FastAPI integration, `.env.example`, and an ignored local `.env`.
- [x] Stage 1 - Lesson 2 verification: defaults, dotenv loading, environment overrides,
  boolean conversion, missing dotenv fallback, and invalid-value startup rejection.
  Real HTTP checks confirmed the configured name in JSON and documentation;
  existing route behavior, dependency compatibility, and compilation also passed.
- [x] Stage 1 - Lesson 3 implementation: PostgreSQL `ecommerce` database, limited
  `ecommerce_app` owner role, typed connection settings, Psycopg driver, and a
  reusable synchronous SQLAlchemy engine in `app/database.py`.
- [x] Stage 1 - Lesson 3 verification: live `SELECT 1`, server/database/user identity,
  database ownership, restricted role privileges, password authentication,
  redacted URL rendering, dependency compatibility, compilation, and API behavior.
- [x] Stage 1 - Lesson 4 implementation: module-level `SessionFactory` and a `get_db()` yield
  dependency that creates and closes one SQLAlchemy Session per FastAPI request.
- [x] Stage 1 - Lesson 4 verification: distinct sessions share the engine, execute real queries,
  and return connections to the pool after successful and failed HTTP requests.
- [x] Stage 1 - Lesson 5 implementation: shared declarative `Base`, a focused `Product` model,
  and a temporary, repeatable command for creating the `products` table.
- [x] Stage 1 - Lesson 5 verification: PostgreSQL column types, nullability, identity primary
  key, repeatable table creation, and an ORM insert/load/rollback cycle.
- [x] Stage 1 - Lesson 6 implementation: shared Product fields, a creation-input schema without
  `id`, and a response schema that can read SQLAlchemy object attributes.
- [x] Stage 1 - Lesson 6 verification: valid parsing and serialization, generated JSON Schema,
  ORM-to-response conversion, and rejection of invalid, extra, or misleading values.
- [x] Stage 1 - Lesson 7 implementation: POST /products validates input, creates and commits a
  Product through the request-scoped Session, refreshes it, and returns a filtered
  201 response.
- [x] Stage 1 - Lesson 7 verification: live HTTP success and validation failures, OpenAPI request
  and response contracts, PostgreSQL persistence, route semantics, and session cleanup.
- [x] Stage 1 - Lesson 8 implementation: GET /products executes an ordered ORM select and returns
  every Product through a list of `ProductResponse` objects.
- [x] Stage 1 - Lesson 8 verification: live empty and populated responses, ascending ID order,
  exact response fields, existing POST behavior, OpenAPI, and connection cleanup.
- [x] Stage 1 - Lesson 9 implementation: a validated product-ID path parameter, primary-key
  lookup with `Session.get()`, a safe 404 response, and a creation `Location` header.
- [x] Stage 1 - Lesson 9 verification: live 200, 404, and 422 responses, OpenAPI parameter and
  error contracts, a resolvable `Location` header, unchanged data, and session cleanup.
- [x] Stage 1 - Lesson 10 implementation: a complete Product update schema and PUT
  /products/{product_id}, with primary-key lookup, explicit field assignment,
  transaction commit, refreshed state, and a safe 404 response.
- [x] Stage 1 - Lesson 10 verification: live 200, 404, and 422 responses, repeated identical PUT
  behavior, GET-visible and PostgreSQL-visible persistence, OpenAPI contracts, and
  temporary-data cleanup.
- [x] Stage 1 - Lesson 11 implementation: DELETE /products/{product_id} validates the ID, loads
  the Product, schedules its row for deletion, commits, returns an empty HTTP 204,
  and safely reports a missing Product with 404.
- [x] Stage 1 - Lesson 11 verification: live 204, 404, and 422 responses, an empty success body,
  GET/list/database confirmation of removal, repeated DELETE behavior, OpenAPI
  contracts, and restoration of the original database row count.
- [x] Stage 1 review: application setup, typed configuration, PostgreSQL integration,
  request-scoped sessions, Product mapping and schemas, and complete CRUD all work.
  The single-module design remains proportionate; planned debt stays on the roadmap.
- [x] Stage 2 - Lesson 1 implementation: standalone `categories` table with an identity primary
  key, required `VARCHAR(100)` name, optional description, named nonblank-name check,
  and named unique-name constraint.
- [x] Stage 2 - Lesson 1 verification: repeatable table creation, live PostgreSQL column and
  constraint inspection, generated identity values, ORM insert/load/rollback, rejection
  of blank and duplicate names, unique-index creation, and unchanged Product data.
- [x] Stage 2 - Lesson 2 implementation: Alembic configuration loads the application's typed
  database URL and model metadata, an initial revision represents both existing tables,
  and the temporary `create_all()` bootstrap command has been removed.
- [x] Stage 2 - Lesson 2 verification: the live schema matched SQLAlchemy metadata before the
  one-time stamp, offline upgrade SQL recreated the complete baseline, the database is
  at migration head with no detected drift, Product data remained unchanged, repeated
  upgrade is a no-op, dependencies are healthy, and live API reads still return 200.

## Next

- [ ] Stage 2 - Lesson 3: add the Category-to-Product relationship with a foreign key
  and useful indexes.

## Stage Roadmap

1. Foundation: application setup, configuration, database, SQLAlchemy, schemas, CRUD.
   **Complete.**
2. Database design: keys, constraints, Category-to-Product relationship, useful indexes.
3. Users and authentication: User, password hashing, registration, login, JWT verification.
4. Authorization: customer/seller/admin roles, permissions, and ownership checks.
5. Cart: Cart/CartItem, quantities, related data, validation, ownership.
6. Orders and inventory: checkout, order history/status, transactions, race conditions.
7. Migration discipline: continue using and reviewing Alembic revisions as the schema
   evolves. Alembic was introduced in Stage 2 when the first table alteration became due.
8. Testing: pytest, fixtures, isolated databases, authentication and business behavior.
9. Redis: a justified product/category cache, TTL, stale data, and invalidation.
10. Background work: confirmation/notification work using the simplest suitable approach.
11. Docker: images, containers, ports, volumes, networks, and Compose for multiple services.
12. Production improvements: errors, logging, pagination, query performance, documentation.
13. CI/CD and deployment: automated checks, secrets, production configuration, public hosting.

Move a topic earlier only when a real project need justifies it; record the reason.
Split large stages into focused lessons and review the project after each stage.

## Concepts Learned

- Stage 1 - Lesson 1: virtual environments, server versus application, import targets,
  method/path routing, JSON serialization, and 404 versus 405 responses.
- Stage 1 - Lesson 2: configuration versus application logic, process environments, `.env`
  loading, type conversion/validation, source priority, startup settings lifetime,
  debug versus reload, and keeping local configuration outside Git.
- Stage 1 - Lesson 3: database server versus client, connection components, PostgreSQL roles
  and ownership, least privilege, SQLAlchemy dialect/driver selection, lazy engine
  connections, connection context management, and secret redaction versus encryption.
- Stage 1 - Lesson 4: engine versus connection versus session, `sessionmaker`, unit of work,
  identity map, automatic transaction start, request-scoped dependency injection,
  session concurrency boundaries, explicit commit ownership, and guaranteed cleanup.
- Stage 1 - Lesson 5: declarative ORM mapping, `Base` and metadata, tables versus model classes,
  rows versus objects, columns versus attributes, primary keys, identity generation,
  nullability inferred from `Mapped` annotations, `Numeric`/`Decimal` for money,
  `create_all()` limitations, and ORM models versus API schemas.
- Stage 1 - Lesson 6: schemas as API boundaries, untrusted input, validation versus parsing,
  serialization, required versus nullable fields, `Field` constraints, strict versus
  coercive parsing, rejecting extra fields, input/output schema separation, JSON Schema,
  and `from_attributes` for converting SQLAlchemy objects to responses.
- Stage 1 - Lesson 7: FastAPI path operations, request-body recognition, dependency injection with
  `Annotated` and `Depends`, Pydantic-to-ORM conversion, transient and pending objects,
  automatic flush before commit, transaction durability, expiration and refresh,
  response-model filtering, 201 Created, and identity values that may contain gaps.
- Stage 1 - Lesson 8: collection endpoints, SQL `SELECT`, SQLAlchemy statement objects,
  `Session.scalars()`, scalar values versus result rows, materializing results with
  `all()`, list response models, empty-list semantics, explicit `ORDER BY`, and read-only
  request transactions that require no commit.
- Stage 1 - Lesson 9: collection versus member resources, dynamic path segments, path parsing,
  numeric range validation, 422 versus 404, primary-key lookup with `Session.get()`,
  identity-map lookup behavior, `None` as a missing result, raising `HTTPException`,
  documenting error responses, and `Location` headers for newly created resources.
- Stage 1 - Lesson 10: PUT as complete replacement of editable resource state, operation-specific
  input schemas, required update fields, resource identity versus mutable state,
  SQLAlchemy attribute change tracking, UPDATE on commit, refresh after a write,
  idempotent intended state, and PUT versus PATCH semantics.
- Stage 1 - Lesson 11: DELETE resource semantics, hard deletion, SQLAlchemy's deleted state,
  transaction commit for durable removal, 204 No Content, empty response bodies,
  repeated DELETE behavior, and future foreign-key and historical-record concerns.
- Stage 2 - Lesson 1: entity boundaries, table-level constraints, application validation versus
  database enforcement, named `CHECK` and `UNIQUE` constraints, whitespace checks,
  unique-constraint indexes, case-sensitive text uniqueness, and adding a new table
  versus altering an existing table with `create_all()`.
- Stage 2 - Lesson 2: schema migration versus ORM metadata, migration repositories, revisions,
  `upgrade()` and `downgrade()`, base and head, the `alembic_version` table, online versus
  offline migration mode, autogenerate as a review aid, schema drift, baselining an
  existing database, and the difference between `stamp` and `upgrade`.

These record teaching coverage, not assessed mastery.

## Technologies Introduced

- Python 3.13.2 and a local `.venv`.
- FastAPI 0.141.1 and Uvicorn 0.52.4.
- Pydantic Settings 2.15.0; python-dotenv is its dependency for reading `.env` files.
- PostgreSQL 17.4, SQLAlchemy 2.0.52, and Psycopg 3.2.10.
- Alembic 1.20.0 for versioned database schema migrations.
- pip, `requirements.txt`, Git, and `.gitignore`.
- Pydantic 2.13.5 now directly defines the Product API schemas.

## Postponed Until Needed

- Authentication/JWT and RBAC: after product/database foundations.
- pytest and test database architecture: when meaningful behavior needs protection.
- Redis: after identifying a worthwhile caching use case.
- BackgroundTasks or a task queue: when concrete background work exists.
- Docker/Compose: when coordinating multiple services becomes useful.
- CI/CD, deployment, and the full professional README: as the application matures.
- Refresh tokens: after access-token authentication is understood and a need appears.
- PATCH and partial-update schemas: after a real need for partial product updates.
- Product archival or soft deletion: when relationships or history-retention rules
  make permanent row removal inappropriate.
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

### Manage the database schema with Alembic

Keep ordered migration revisions under `migrations/` and use `alembic upgrade head`
to bring a database to the latest schema. The initial revision can create Product and
Category on an empty database. The existing local database was inspected, compared with
SQLAlchemy metadata, and stamped at that revision because its tables already matched;
stamping recorded the version without running their `CREATE TABLE` operations. The old
`create_all()` script was removed so fresh setup and later schema changes use one clear
workflow. Future autogenerated revisions must be reviewed before they are applied.

### Use separate Product input and output schemas

Keep shared public fields in `ProductBase`. Accept creation data through
`ProductCreate`, which has no server-generated `id`, and serialize ORM objects through
`ProductResponse`, which includes `id` and enables `from_attributes`. Strip surrounding
string whitespace, reject unexpected fields, require a positive price that fits the
database decimal, and require non-negative stock as a strict JSON integer.
Reason: clients should receive clear validation errors before database work begins,
and response fields should be an explicit public contract rather than every ORM field.

### Keep product creation and its transaction explicit

POST /products converts validated `ProductCreate` data into a `Product`, adds it to the
request-scoped Session, commits the transaction, refreshes database-generated state,
and returns the ORM object through `ProductResponse` with HTTP 201 Created.
Reason: the endpoint is currently short enough to show the full write flow clearly.
The write operation owns its commit; the session dependency owns resource cleanup.

### Return product collections in deterministic ID order

GET /products executes `select(Product).order_by(Product.id)` through
`Session.scalars()` and returns a `list[ProductResponse]`. Return HTTP 200 with `[]`
when no rows match. Reason: clients receive one predictable response shape, and explicit
ordering avoids relying on PostgreSQL's unspecified natural row order.

### Use primary-key lookup and a clear not-found response

GET /products/{product_id} accepts only positive PostgreSQL `INTEGER` values, uses
`Session.get(Product, product_id)`, and raises a generic 404 when no row exists.
Reason: `Session.get()` states the primary-key intent directly and can reuse an object
already in the Session identity map. Invalid ID syntax or range receives 422, while a
valid but absent ID receives 404. POST /products now links to this route with `Location`.

### Use PUT for complete Product updates

PUT /products/{product_id} accepts a `ProductUpdate` containing the complete editable
Product state, loads the existing row, assigns each allowed field explicitly, commits,
refreshes, and returns the same resource ID with HTTP 200. Omitted description becomes
null, while name, price, and stock remain required. Reason: complete replacement gives
PUT clear semantics, explicit assignment limits changes to approved fields, and sending
the same valid request repeatedly leaves the resource in the same intended state.
Partial PATCH behavior is deferred until it solves a concrete client need.

### Return 204 after a successful hard delete

DELETE /products/{product_id} loads the existing Product, passes it to
`Session.delete()`, commits the transaction, and returns HTTP 204 with no body. A valid
but missing ID returns 404. Reason: the resource representation no longer exists after
successful deletion, and an empty response communicates that the requested removal is
complete. Hard deletion is sufficient while Product has no relationships; deletion,
restriction, and archival rules must be revisited before orders depend on Product rows.

### Give Category its own constrained table before relating it to Product

Map `Category` to `categories` with an identity integer primary key, required unique
`VARCHAR(100)` name, optional text description, and a named check that rejects blank or
space-only names. PostgreSQL backs the unique constraint with a unique index. Reason:
Category is an independent entity with its own identity and data rules, while named
constraints produce clearer database errors and future migrations. Name uniqueness is
currently case-sensitive. Add the relationship only after Alembic can safely alter the
existing `products` table.

## Technical Debt to Revisit

- Direct dependencies are pinned; full transitive dependency locking is deferred
  until reproducible CI/deployment setup. No pytest suite yet; first behavior was
  verified with temporary standard-library HTTP checks.
- The baseline downgrade removes both application tables and therefore their data.
  Migration downgrade testing against an isolated database is deferred until the test
  database setup exists; the generated downgrade SQL should always be reviewed first.
- Product price and stock do not yet have database `CHECK` constraints; add and teach
  those with database constraints in Stage 2. Timestamps are also deferred.
- Category is not exposed through the API or related to Product yet. Its unique name is
  case-sensitive; decide normalization behavior when adding the Category API.
- Product write operations are intentionally unauthenticated until users,
  authentication, and seller/admin authorization are introduced.
- Product deletion currently removes the row permanently. Revisit foreign-key policies,
  order-history preservation, and archival before orders reference Product rows.
- GET /products currently loads every matching row into memory. Add limit/offset or
  cursor pagination before the product collection can grow large.

## Local Commands

Run from the repository root in PowerShell.

First-time setup:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
alembic upgrade head
```

Normal development after opening a new terminal:

```powershell
.\.venv\Scripts\Activate.ps1
alembic upgrade head
uvicorn app.main:app --reload
```

On a fresh clone, optionally copy `.env.example` to `.env` before starting the API:
`Copy-Item .env.example .env`. Do not overwrite an existing local `.env`.
`APP_NAME` controls the API title and root message. `DEBUG` controls error tracebacks;
keep it false for public use. A local `.env` with example defaults already exists.
Database settings default to the local `ecommerce` database and `ecommerce_app` role;
`DATABASE_PASSWORD` is required and belongs only in `.env` or the process environment.

API: http://127.0.0.1:8000/ - interactive documentation: http://127.0.0.1:8000/docs.
Use `--reload` for local development; it restarts the server after Python edits.
