# Expense access change

These are fictional project facts for an isolated offline exercise. They do not describe an implemented or deployed application. No external service, credential, framework installation or production operation is authorized.

## A. New small application

A six-person travel-expense application has a Python service and a relational database. Authentication already provides a stable application user ID. Local passwords are outside this increment. The operator maintains staff assignments. The UI has separate list and approve actions.

| Role label | Business capability |
| --- | --- |
| Reader | Read expenses |
| Approver | Approve expenses |

Staff can hold both responsibilities. Every operation is limited to the person's current department memberships. Approval is available only for Pending expenses belonging to someone else. Deactivating a user stops access. Assignment changes must apply to the next call in this exercise; caching is not required. Role names arriving in an identity token are not maintained staff assignments.

| User ID | Active | Assigned responsibilities | Department membership |
| --- | --- | --- | --- |
| kim | Yes | Reader, Approver | north |
| lou | Yes | Approver | north |
| mina | Yes | Reader | north |
| noah | No | Reader, Approver | north |

| Expense ID | Owner | Department | State |
| --- | --- | --- | --- |
| 1 | mina | north | Pending |
| 2 | sam | south | Pending |
| 3 | kim | north | Pending |
| 4 | mina | north | Approved |

Design the smallest coherent account/access structure and implement a thin executable policy example using Python's standard-library SQLite. Deliver `policy.py` with `create_demo()` returning an initialized in-memory connection, `can(db, user_id, permission_code, expense_id)` returning a boolean, and `revoke_role(db, user_id, role_code)` for the operator's assignment change. Use permission codes `expenses.read` and `expenses.approve`; use the listed role labels as role codes. Unknown users, actions or records receive no implicit access. Database and application exceptions must not become grants. Include meaningful executable tests and a short schema/enforcement explanation. The demonstration is not an authentication provider or production-ready policy service.

## B. Existing application's next endpoint

An existing claims application has stable user IDs, a company-operated policy service and users with multiple responsibilities. Its database contains `Staff`, `ResponsibilityAssignments` and claim history. Every current handler calls `policy.authorize(actor, action, claim)`; the policy service also owns the department rule. Current token verification and administration are unchanged. The next request is to add a CSV export to the existing claim search. Search already applies policy to its results, and export must use the same authorized result set.

Give the bounded design/backend/frontend/QA handoff for that request. State what evidence you need and what you would actually change. No application source beyond this excerpt or live policy target is supplied; do not invent checks you executed.
