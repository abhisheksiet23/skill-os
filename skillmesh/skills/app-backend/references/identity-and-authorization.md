# Simple identity and application-owned authorization

Use this default for new applications that need user accounts. It is not a reason to add login to a public marketing site or replace an existing adequate identity system without an agreed migration. The owner prefers a single role per application user and bcrypt for local password hashing; this is a chosen convention, not a claim that bcrypt is universally preferred over other maintained password hashers.

## Schema and responsibilities

Keep four application-owned tables:

| Table | Responsibility and constraints |
| --- | --- |
| Users | Stable local `Id`, login/display fields as needed, nullable `PasswordHash`, application `Active` state and required `Role` foreign key to `Roles.Id`. Exactly one role per user; no duplicate role-name field or user-role join table. |
| Roles | Stable `Id`, unique stable code and human name. Seed only agreed roles, without implicit privileged defaults. |
| Modules | Stable `Id`, unique stable code and human name. Module codes identify server-enforced application capabilities, not browser URLs alone. |
| ModuleRoleMapping | `ModuleId` and `RoleId` foreign keys with a composite primary key or unique constraint. A row grants module access; no matching row means deny. |

Users, Roles, Modules and ModuleRoleMapping remain in each consuming application when authentication becomes central. Authentication establishes a trusted identity; authorization resolves the current active local user, role, module grant, record/tenant scope and workflow rules. Module access alone must not grant every action or access to every record. Do not replace clinic/team/ownership rules with role checks. Enforce at server boundaries including direct API, downloads and background work, not just navigation visibility. Audit role/grant/identity-link changes and prevent unintended self-escalation or loss of all administrators.

Define local login normalization and uniqueness separately from password/subject comparison. Existing multi-role adoption needs an inventory and explicit target mapping for zero/multiple-role users; do not pick the first or most privileged role. Compare effective permissions before removing old mappings, preserve stable user IDs and keep compatible readers/verifiers until the reviewed cutover. A true multi-role requirement is an exception to resolve with the owner, not data to discard.

## Local authentication now

Keep credential verification behind a small coherent boundary that returns the stable local user identity. Use established session/authentication middleware and a maintained bcrypt implementation; simplifying tables does not justify implementing cryptography, token validation or session security from scratch. Persist the library's full encoded bcrypt hash, which carries its salt and cost. Never store plaintext, reversible passwords or a shared default password; never return hashes in API responses.

Calibrate the work factor for the actual server and login load, respecting current security guidance (OWASP specifies at least 10 for bcrypt). Enforce the selected implementation's byte limit before hashing and verification; conventional bcrypt accepts at most 72 bytes. Unicode characters may occupy multiple bytes. Do not silently truncate, silently normalize passwords or invent a prehash scheme. Test the boundary with multibyte input using the real selected library. Rehash after successful verification when cost policy changes. An existing PBKDF2/other hash cannot be converted to bcrypt without a password: use verified-on-login rehash or a controlled reset, preserving existing login until the agreed cutover.

Preserve rate limiting, safe account-recovery and one-time setup, session expiry/revocation and CSRF protection for cookie-authenticated mutations. Supporting state should be justified by those behaviors, not by an arbitrary four-table limit. Session/recovery state is distinct from forbidden redundant user-role mapping. Use the identity library's compatible extension points or a purposeful thin boundary, rather than retaining unused framework role/claim tables or discarding security controls just to reduce table count.

## External authentication later

Keep business foreign keys and audit actors bound to `Users.Id`. For the planned single external identity per local account, reserve nullable `ExternalIssuer` and `ExternalSubject` on Users now, or add them with one additive migration later. Require both values together and a unique non-null pair. Match their provider-defined values exactly, including case; configure database collation/index behavior accordingly. Do not use mutable email/usernames or a bare subject without its issuer as the permanent identity key.

Use standard OIDC/OAuth integration and maintained token-validation middleware. Validate signature/key trust, allowed algorithm, issuer, audience, token type and time claims for the appropriate token profile. An ID token is not a general-purpose API access token. Never accept one application's token at another merely because the signature is valid. Do not build the central authentication service speculatively now.

After successful validation, map the trusted issuer/subject to the active local Users row and run the same local authorization path as local login. Unknown/unlinked identities are denied or go through a separately agreed provisioning process; do not auto-link on email or grant a default privileged role. External role claims do not silently overwrite Users.Role or module grants. Define role/grant caching and invalidation so local disablement/permission changes take effect within an explicit bound.

Central cutover replaces credential verification and session integration, not the four authorization tables. Link existing accounts through a verified, audited process, preserve Id values, then disable local login/reset for centrally managed users. Nullable PasswordHash supports external-only users; missing credentials must deny local login. Invalid external tokens or provider outages must not trigger automatic local-auth fallback. Plan session invalidation, staged coexistence, rollback eligibility and eventual local-hash removal deliberately. Migration of a provider or subject scheme needs controlled relinking; multiple providers per local user are a different requirement to assess when real.

## Proof before calling it ready

Test local login with the real bcrypt library, wrong passwords, multibyte byte limits and cost rehash; foreign keys and duplicate grants; missing module grants; cross-record/tenant attempts; role/disablement changes; and privileged administration. Test credential-hash migration on representative existing accounts before replacing authentication storage.

For the external transition, prove valid linked identity, same subject under another issuer, wrong audience/signature, expired token, unknown/disabled user, rejected external-role escalation and disabled local fallback. Prove business/audit foreign keys and local permissions remain unchanged across account linking. A synthetic token stub or schema proposal does not establish real issuer, cryptographic or SQL behavior. Prepare EF migrations and owner-run SQL/SSMS instructions where applicable; do not run release generation or apply schema without explicit direction.

Primary guidance: [OWASP password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html), [OpenID Connect stable identity](https://openid.net/specs/openid-connect-core-1_0.html), and [OWASP REST security](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html). Verify the current guidance and selected library's actual behavior when implementing.
