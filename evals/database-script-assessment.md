# Database script deliverables assessment — 2026-10-20

## Decision and scope

Adopt the owner's requirement as a backend default: actual idempotent initial database SQL covering database creation, required DDL and applicable master-data inserts, with separate ordered scripts for later schema/master-data changes. Keep migration authority, manual database application, customer data and separate credential bootstrap intact. This corrects a concrete handoff obligation; it does not justify a new framework or guarantee runtime correctness.

## Evaluation before maintained skill edits

The existing backend skill and its references were copied unchanged into ignored `.eval-runs/database-scripts/baseline/app-backend/`. A candidate was developed only in `.eval-runs/database-scripts/candidate/app-backend/`. Two fresh-context agents independently applied the respective instructions to the same four requests in [the task pack](database-script-tasks.md), without seeing the peer variant, outputs or assessment rubric. Actual answers are retained in `.eval-runs/database-scripts/baseline-output.md` and `candidate-output.md`. Only after reading both outputs were maintained skills changed. The coordinating assessor knew the proposed changes; this is a small qualitative instruction evaluation, not a blind causal benchmark or a live database pass.

| Case | Baseline observed response | Candidate observed response |
| --- | --- | --- |
| Empty-server setup | Described provisioning, preflight, schema, reference-data and verification files; deferred schema SQL generation to the owner and used a non-idempotent generation command. | Explicit `database/initial.sql` entry point including guarded creation, migration-derived DDL/history and stable-key master inserts; explicitly marked missing migration sources and SQL generation pending. |
| V1-to-V2 and rerun | Already preserved renamed labels/customer data, described delta and fresh-install paths, and separated schema success from seed completion. | Made ordered change-file names, frozen baseline composition, prerequisite checks and second-run no-op behavior explicit; preserved operator labels. |
| Drift and interrupted install | Already rejected history-only proof and proposed a data-preserving corrective path. | Also rejected history-only proof, retained partial database state and required explicit correction/recovery; no substantive demonstrated advantage on this case. |
| HTTP-only change in Alembic project | No database churn or migration-system replacement. | Same restraint and preservation. |

Neither evaluator generated application SQL: no concrete migration sources or application database were supplied, and the requests were handoff specifications. Both disclosed missing live proof. The evidence supports making the script-delivery obligation explicit; it does not establish that the candidate produces correct executable SQL or outperforms the baseline generally. No numerical behavioral score, token saving or runtime improvement is claimed.

## Resulting instruction changes

- Backend implementation owns SQL file authoring and safe local generation, rather than providing only owner-run commands. If generation needs unavailable tooling or a separately unauthorized build, identify the incomplete portions instead of supplying a fake completed script.
- Default source paths are `database/initial.sql` and `database/changes/<sequence>-<purpose>.sql`; preserve adequate established paths. During authorized release packaging, reviewed copies go in `releases/<version>/database/`.
- Initial setup includes all required objects and master data, directly or through supplied, ordered SQL composed by an explicit supported runner. Database creation remains a separate nontransactional stage where the engine requires it, even within one setup entry point.
- Keep one migration authority; derive EF schema SQL from committed migrations. Deliver required master inserts in SQL because application seeding callbacks are not executed by SQL scripts.
- Reruns must avoid duplicate objects/rows, preserve operator-managed values, reject unsupported drift and recover deliberately from partial failure. Freeze shipped scripts and add corrections as new changes. Keep fresh install and upgrade consistent without resetting customer data.
- No database script churn for unrelated changes. No production startup migration/seeding, default password, implicit database execution or release binary publication.
- Reconciled contradictory SQL-generation wording in solution design, delivery, QA and identity-transition guidance. Their unrelated boundaries remain intact.

## Evidence and limits

Checked current primary documentation: [EF SQL deployment and seeding behavior](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/applying), [SQL Server database creation transaction restrictions](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-database-transact-sql), and [SQLCMD fail-stop commands](https://learn.microsoft.com/en-us/sql/tools/sqlcmd/sqlcmd-commands). These support design constraints, not an execution pass.

After promotion, an independent agent reviewed the backend and companion guidance for consequential contradictions and found no blockers. The library validator passed all 19 skills with zero packaging errors; official validators passed the four changed entrypoints, and whitespace checks passed. These checks establish packaging/frontmatter/reference integrity only. The first official-validator attempt lacked PyYAML; rerunning with the repository's existing `.validation-deps/` succeeded without installation.

No application code, installed plugin or live database was changed. SQL Server/SSMS fresh install, repeat run, supported upgrade, seed failure, drift detection, concurrent execution and recovery remain unverified until the actual application scripts are tested. Performance, token use and owner usability remain unknown.
