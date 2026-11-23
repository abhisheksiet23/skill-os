# Keep identity and permissions simple and consistent

Use the same small permission structure for new account-based applications, including SSO-first apps. Simplicity means clear responsibilities and few policy mechanisms, not a fixed table count. Authentication proves identity; permission grants, resource scope and workflow rules decide access. Preserve an adequate existing system or accepted central policy through an explicit mapping to these responsibilities; this guidance does not authorize replacing deployed identity or adding login where none is required. Use maintained bcrypt when new local passwords are offered; SSO-only apps need no local credentials or password fallback.

## Schema and responsibilities

Settle the access structure before dependent implementation and keep design, database, backend, UI capability contracts and QA aligned. Use these logical relations in new applications; map equivalent framework entities rather than adding duplicate stores:

| Table | Responsibility and constraints |
| --- | --- |
| Users | Stable application `Id`, display/login fields as needed and `Active` state. Business records and audit actors reference this ID. Local password storage is optional and follows the selected identity library. No scalar role field competes with assignments. |
| Roles | Stable `Id`, unique stable `Code` and human name. A role groups business responsibilities; it is not a hard-coded branch in each handler. Seed only agreed roles. |
| Permissions | Stable `Id`, unique stable `Code` for a resource/action such as `expenses.read` or `expenses.approve`, plus a description. UI modules can group permissions but module visibility grants no action by itself. |
| UserRoles | Foreign keys `UserId`, `RoleId`, with a composite primary key or unique pair. Start with one assigned role when sufficient; multiple responsibilities use additional rows in the same structure. |
| RolePermissions | Foreign keys `RoleId`, `PermissionId`, with a composite primary key or unique pair. A row grants that action; no matching grant means deny. |

Use one permission catalog and one authoritative assignment/grant path per application. Distinct roles combine their explicit grants; a missing grant on one role does not cancel another role's grant. Do not add direct user grants, explicit deny rows, role hierarchies, wildcards or a generic policy engine without a concrete requirement and defined conflict semantics. Administrator roles receive explicit permissions; a role name or new permission must not silently grant privilege.

Add supporting relations for real behavior using the same responsibilities: `UserIdentities(UserId, Issuer, Subject)` when external authentication is used, with foreign key and unique exact issuer/subject pair; typed department/team/tenant memberships for resource scope; and the identity library's sessions/recovery state where needed. These are not permission-table-count violations. Default roles are application-wide capabilities, not cross-tenant authority. When a role differs by tenant, use a tenant-bound assignment with foreign keys to the user membership and role, and resolve grants only for the resource's tenant; do not mix global and scoped assignments without an explicit rule. No speculative tenancy, hierarchy or central identity service is required.

### Enforce current application permissions

For each operation require a trusted active user, an explicit permission through current role assignments, allowed resource/tenant scope and valid workflow state. With scoped assignments, select only assignments applicable to the target scope before combining grants; an approval role in tenant A cannot combine with read membership in tenant B to approve there. All applicable conditions must hold. Deny unknown actions, missing assignments, unavailable policy decisions and failed scope checks. An approval permission does not waive a no-self-approval rule; a read permission does not imply write or approve. Enforce at server boundaries including direct API, exports, downloads and background work, and scope list queries as well as individual records. Recheck mutable ownership/scope/workflow conditions at the guarded write using the appropriate transaction or concurrency mechanism; define source/destination authority for supported ownership or tenant transfers.

Use one ordinary authorization boundary, such as `Can(user, permission, resource)`, backed by the application's accepted policy implementation. The UI consumes current-user capabilities from that same authority for presentation; it cannot grant access or reconstruct permissions from role names. Define when user disablement, role removal and grant changes take effect, including cache/token invalidation. Keep simple live lookup when adequate. Audit permission, assignment and identity-link changes. Check an administrator's delegated authority over affected users, resulting privileges and scopes, including indirect effects of editing a shared role; administration authority need not equal the actor's own business permissions. Prevent unintended self-escalation or unrecoverable loss of administrators without inventing an approval ceremony for routine authorized maintenance.

### Preserve identity during schema changes

Define local login normalization and uniqueness separately from password/subject comparison. Existing scalar roles can map to one UserRoles row per user; existing multiple roles retain all authorized assignments. Inventory current effective actions, resource restrictions and privileged administration before mapping Modules/ModuleRoleMapping or another model to action permissions. Do not expand a module grant into every action by assumption, pick a most privileged role, or drop policy to fit the new structure. Resolve ambiguous mappings, compare effective access before/after, preserve stable user IDs/history and keep compatible readers/verifiers until an authorized data-preserving cutover. New instructions do not authorize migrating an existing application.

## Local authentication now

This section applies only when local passwords are offered, regardless of where authorization is enforced. An authorization-model exception does not waive credential security; an SSO-only app skips local password implementation and its checks.

Keep credential verification behind a small coherent boundary that returns the stable local user identity. Use established session/authentication middleware and a maintained bcrypt implementation; simplifying tables does not justify implementing cryptography, token validation or session security from scratch. Persist the library's full encoded bcrypt hash, which carries its salt and cost. Never store plaintext, reversible passwords or a shared default password; never return hashes in API responses.

### Verify password-library behavior

Calibrate the work factor for the actual server and login load, respecting current security guidance (OWASP specifies at least 10 for bcrypt). Enforce the selected implementation's byte limit before hashing and verification; conventional bcrypt accepts at most 72 bytes. Unicode characters may occupy multiple bytes. Do not silently truncate, silently normalize passwords or invent a prehash scheme. Test the boundary with multibyte input using the real selected library. Rehash after successful verification when cost policy changes. An existing PBKDF2/other hash cannot be converted to bcrypt without a password: use verified-on-login rehash or a controlled reset, preserving existing login until the agreed cutover.

## Keep the surrounding security controls

Preserve session expiry/revocation and CSRF protection for cookie-authenticated mutations with either local login or SSO. Retain applicable rate limiting, account recovery and one-time setup under the selected identity mechanism; an SSO-only app does not need local password recovery. Use the identity library's compatible extension points and required supporting state instead of discarding security controls to reduce table count or adding competing user/role stores.

## External authentication at launch or later

Keep business foreign keys and audit actors bound to `Users.Id`. When external identity is used, map its issuer/subject to that stable user through UserIdentities or an equivalent established identity relation. Require both values and a unique pair, matching provider-defined values exactly including case; configure database collation/index behavior accordingly. Add another linked identity only for a supported provider/provisioning need. Do not use mutable email/usernames or a bare subject without its issuer as the permanent identity key.

### Validate identity, then resolve local access

Use standard OIDC/OAuth integration and maintained token-validation middleware. Validate signature/key trust, allowed algorithm, issuer, audience, token type and time claims for the appropriate token profile. An ID token is not a general-purpose API access token. Never accept one application's token at another merely because the signature is valid. Do not build the central authentication service speculatively now.

After successful validation, resolve the trusted issuer/subject to the active user and run the same accepted authorization path as local login. Unknown/unlinked identities are denied or follow an agreed provisioning process; do not auto-link on email or grant a default privileged role. External role/group claims do not silently create UserRoles rows or RolePermissions grants. Where an accepted central policy is authoritative, adapt its decision through the same enforcement contract rather than maintain a competing local grant store.

### Cut over without losing users or history

Changing authentication does not require replacing the permission structure. Link existing accounts through a verified, audited process, preserve Id values, then disable local login/reset for centrally managed users. Missing local credentials must deny local login. Invalid external tokens or provider outages must not trigger automatic local-auth fallback. Plan session invalidation, staged coexistence, rollback eligibility and eventual local-hash removal deliberately. Provider/subject changes need controlled relinking. A change in authorization authority is a separate accepted policy/migration decision, not an incidental consequence of SSO.

## Proof before calling it ready

When local login is offered, test the real selected password library, wrong passwords, multibyte limits and cost rehash; use bcrypt-specific byte checks for bcrypt, and prove credential-hash migration before replacing storage. For permissions, test unique codes and assignment/grant pairs, multiple-role union without unintended grants, read-versus-approve separation, unknown/missing grants, cross-scope grant composition, record/tenant boundaries, workflow restrictions, role removal, disablement and delegated administration/shared-role changes. Include actual list/export and direct mutation paths plus relevant concurrent scope/state changes. For an accepted existing/central policy, prove equivalent decisions rather than demand new table names; local credential checks still apply when offered.

For external identity, prove valid linking, same subject under another issuer, wrong audience/signature, expiry, unknown/disabled users, rejected external-role escalation and disabled local fallback. Prove stable business/audit references and unchanged effective permissions across linking or model migration. A schema, synthetic policy example or token stub does not establish real issuer, cryptographic, database or application integration behavior. Prepare migrations, required SQL and operator instructions where applicable; authoring does not authorize release compilation, packaging or applying schema.

Primary guidance: [NIST core RBAC](https://csrc.nist.gov/projects/role-based-access-control/faqs), [OWASP authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html), [password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html), [OpenID Connect stable identity](https://openid.net/specs/openid-connect-core-1_0.html), and [OWASP REST security](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html). The chosen schema is an owner convention, not a universal standard; verify current guidance and selected libraries when implementing.
