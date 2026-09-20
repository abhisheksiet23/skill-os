# Delivery efficiency cases

Run each case independently. Use only the supplied evidence and the indicated variant's skills. No browsing, production changes, installs, external access or fabricated test execution. Produce a useful response of at most 350 words per case; record skills read and limitations. No private reasoning requested.

## 1. Modernize an existing portal

User: Analyze Login, Home and Menu for a technology upgrade. Preserve credentials and shared database schema; improve UX. Do not implement. We have not decided whether Home should retain its widgets. A shallow inspection finds 11 configurable widgets, legacy sessions used by 100 retained pages, and a menu that links to those pages. The product owner can answer consequential questions. Source and local database are available; the deployed database is one month newer. Provide the next analysis actions, the immediate owner questions and the conditions for completing analysis. Do not invent answers or perform a whole-app audit.

## 2. Contained correction

User: Fix a typo in the existing recovery dialog: “Contcat your administrator” should be “Contact your administrator.” Layout, behavior and approved design are unchanged. Existing component tests cover opening and closing the dialog. Give the implementation and verification approach, without editing code in this exercise.

## 3. Repeat QA after an auth change

User: Verify a fix for stale CSRF tokens after another browser tab signs in. There are 28 backend tests, 11 frontend tests and reusable browser journey functions, but those functions only run through interactive agent calls. We expect ten more auth/menu changes. Local test accounts and a production build are available. CI can execute Node commands. A previous screenshot check found CSS blocked by production CSP. Provide the verification and reusable automation approach. Distinguish proposed tests from executed proof. Consider whether an MCP service is needed.

## 4. First real integration

User: Implement an API using an unchanged legacy identity store. Transport roles are Admin/Executive; actual stored names have not been checked. Mock tests pass. A read-only local database connection and designated test account are available. The frontend has an approved design and a contract-faithful mock. Give the order of work and completion evidence. Do not execute code in this exercise.
