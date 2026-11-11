# Simple identity and local authorization evaluation

Give the same request to separate contexts with independently frozen current/candidate backend and solution-design skills and their local references. Do not expose peer outputs or assessment criteria. Use ignored temporary scratch only while assessing the outputs. This evaluates instruction application, not an implemented identity system.

## Request

New SQL Server/.NET helpdesk: one Users table with a single Role column and bcrypt local passwords, separate Roles, Modules and ModuleRoleMapping, no user-role join table. Future central authentication issues tokens; the app retains these four tables, local role/module grants, team/clinic record isolation and stable business user IDs. Give schema constraints, authentication/authorization boundary, transition steps and acceptance cases. As an existing-system adoption scenario, framework PBKDF2 hashes and user-role mappings already exist: explain safe migration without executing it. Two identity providers can issue the same subject, and an external role claim may say Admin. Linking must not grant unintended access. The owner runs release builds, SQL generation and publishing. No application edits or production operations.

## Assessment after collection

Check required single-role FK and unique module-role pair, deny-by-default module checks plus retained record/workflow scope, stable local IDs and exact unique external issuer/subject link, current local authorization instead of blind external role trust, bounded password hashing through maintained libraries, safe byte-limit behavior and non-convertibility of existing hashes. Existing multi-role users need deliberate reconciliation, not arbitrary selection. No direct replacement of existing identity state, automatic email linking, startup schema migration or silent local-auth fallback. Distinguish a schema/transition recommendation from real bcrypt/token/issuer/SQL proof. No security-readiness or general-superiority claim follows from a plan-only evaluation.
