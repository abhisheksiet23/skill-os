# Access and data standards

Read the section that applies. Each states the owner's standing choices for its area.

## Permission structure
Settle this before dependent account or access implementation.
- Entities: Users, Roles, Permissions with stable resource and action codes, UserRoles assignments, RolePermissions grants.
- One role per user is enough when it fits. Multiple roles use the same assignment relation and combine the explicit grants that apply to the target scope.
- Access also requires an active trusted user, resource scope and workflow eligibility. Recheck them at the guarded write where state is mutable.
- Roles and module visibility never grant every action or record.
- Use equivalent framework entities instead of duplicate stores.
- Use one authorization boundary for APIs, services and UI capability projection.
- Add external identity links, typed memberships, scoped assignments or session state only for an actual requirement. Set no table-count limit and build no speculative policy engine.
- Local passwords use maintained bcrypt. SSO needs no local fallback.
- Preserve stable business IDs, adequate existing systems and accepted central policy.
- Migration needs an explicit data-preserving scope and an effective-access comparison.

## Relational backends
- Existing adequate native migration workflow: keep it, with versioned artifacts, repeatable install and upgrade steps and recovery. Add SQL files only when the owner or project requires them.
- Otherwise: plan repository-owned initial DDL and master-data SQL, plus ordered later changes.
- Require safe rerun and partial-failure handling through the chosen mechanism.
- Include guarded database creation where the operator owns provisioning. Managed or provider creation is a separate prerequisite. Do not require privileges that are unavailable.
- Script authoring and safe local generation do not authorize database execution or release compilation.
- New .NET relational projects keep EF migrations as schema authority, with SQL Server and SSMS manual application. Other stacks keep their own native mechanisms.
- Administrator bootstrap is separate. Production startup verifies compatibility and never mutates schema or seeds data.
- Design app and schema compatibility, and persistent data and configuration locations, so upgrades and recovery are concrete.
