# Executable Postman upkeep evaluation

Use separate contexts with the same requests and independently frozen current/candidate backend skills and local references. Do not provide peer outputs or assessment criteria. Keep answers and generated samples in ignored temporary scratch only while assessing them. This is an isolated skill evaluation, not a live application change.

1. A new local HTTP helpdesk increment is implemented: POST /session returns accessToken, POST /tickets returns 201 with id/status/version, and POST /tickets/{id}/approve requires reviewer token plus version and returns assigned state. Requesters can create but cannot approve; stale version returns 409. Prepare reusable human/API verification deliverables, assertions and execution steps. No actual server is supplied.
2. Existing repository collection expects GET /tickets to return an array. The changed endpoint returns `{items,total,page}` and accepts page/size. Explain targeted collection upkeep and checks while retaining unrelated tests.
3. An internal helper refactor changes no HTTP contract and an existing collection is green. Explain necessary collection edits and which execution evidence remains valid.

Both contexts know Postman CLI/Newman are unavailable. No runner installation, network calls, application/release build, production operation or SQL generation is authorized. Sample collection creation is optional; file existence or syntax validation must not be called a real API pass.

After collection, assess whether Postman is a default repository-owned executable asset, meaningful auth/error/state assertions and repeatable test setup are present, no nonexistent cleanup endpoint is invented, API changes update affected requests/assertions, non-API changes avoid churn, and missing runner/target stays pending. Prefer compact reports/failure inspection; token savings remain unknown without measurement. Preserve owner-controlled release/production boundaries and compatible existing runners/formats rather than forcing migration or cloud upload.
