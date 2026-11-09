# TravelHub Architecture Overview

TravelHub is a small REST API for managing travel bookings, destinations, and users. It is organized as a classic layered application: HTTP routes form the presentation boundary, services hold the business use cases, and the database layer contains persistence models and repositories. Shared schemas mediate data validation and serialization, while `core/` keeps configuration, security, and common exceptions separate from the main flow. Supporting utilities, maintenance scripts, and tests sit outside the request path but help keep the system maintainable.

The architecture is intentionally simple but clearly separated:

- `api/` exposes the HTTP interface and delegates to the business layer.
- `services/` coordinates booking-related workflows and other use-case logic.
- `database/` implements the persistence side, including the Repository pattern.
- `schemas/` defines the data contracts used at the boundaries.
- `core/` groups cross-cutting concerns such as config, security, and exceptions.
- `utils/`, `scripts/`, and `tests/` support the application without becoming part of the core request flow.

## Sections

- [Layered Architecture and Request Flow](Layered-Architecture-and-Request-Flow.md) — the end-to-end path from HTTP entrypoint to business logic and persistence, and the boundaries that keep those layers separated.
- [API Boundary and HTTP Routing](API-Boundary-and-HTTP-Routing.md) — how the route layer shapes the public API and adapts requests into service calls.
- [Business Services and Use-Case Orchestration](Business-Services-and-Use-Case-Orchestration.md) — the coordination layer that centralizes booking logic and supporting workflows.
- [Domain Models, Schemas, and Data Contracts](Domain-Models,-Schemas,-and-Data-Contracts.md) — the domain vocabulary and the types that validate, serialize, and persist it.
- [Persistence Layer and Repository Pattern](Persistence-Layer-and-Repository-Pattern.md) — how data access is isolated behind repositories and session/model infrastructure.
- [Cross-Cutting Concerns: Configuration, Security, and Exceptions](Cross-Cutting-Concerns_-Configuration,-Security,-and-Exceptions.md) — the shared infrastructure that cuts across layers without polluting business logic.
- [Supporting Utilities, Scripts, and Test Support](Supporting-Utilities,-Scripts,-and-Test-Support.md) — helpers, maintenance scripts, and tests that reinforce the architecture from the edges.
- [Application Entry Point and Assembly](Application-Entry-Point-and-Assembly.md) — the startup composition root where the application is wired together for runtime.