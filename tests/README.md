Tests — how to run them

Purpose
This document explains how to run the project's test suite locally and what we expect from test-related contributions.

Prerequisites
- Ensure language tooling for the project is installed (examples below).
- Install dependencies from the project root before running tests.

Quick commands (pick the one matching this repo)
- Node (npm): npm install && npm test
- Node (yarn): yarn install && yarn test
- Python (pytest): python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && python -m pytest
- Go: go test ./...
- Rust: cargo test
- Java (Maven): mvn test
- Java (Gradle): ./gradlew test

Running specific tests
- Jest: npx jest path/to/file.test.js or npx jest -t "test name"
- Pytest: python -m pytest tests/test_file.py::test_name
- Go: go test ./pkg/path -run TestName

Coverage and snapshots
- Coverage (if configured): use the project's coverage command, e.g. npm run coverage or python -m pytest --cov
- Update snapshots intentionally (Jest): npm test -- -u

CI
CI runs the same commands as above; if a pipeline fails locally, reproduce with the matching command and fix tests before opening a PR.

Contribution checklist for tests
- Run the full test suite locally before pushing.
- Add tests for new features and bug fixes; place them under the tests/ (or language-idiomatic) folder.
- Keep tests deterministic, fast, and isolated (mock external services).
- When updating snapshots, double-check changes are expected and document why.
- Include a brief note in your PR describing what tests were added/changed and how to run them.

If something fails
- Re-run tests with verbose output, check logs, and isolate the failing test.
- If unsure, include failing test output and minimal repro steps in your PR or an issue.