# Troubleshooting Guide

This file lists common problems and quick fixes when working with the project.

1) Dependency installation fails
- Symptom: package manager errors during install.
- Fixes:
  - Delete lockfile (package-lock.json / yarn.lock) and node_modules, then reinstall.
  - Ensure your runtime version matches project requirements (node, python). Use nvm/pyenv.
  - If a native dependency fails to build, install system packages (build-essential, python-dev) or use prebuilt binaries.

2) Tests fail locally but passed in CI
- Symptom: flaky tests, environment-dependent failures.
- Fixes:
  - Run tests with verbose output to capture the failing test and stack trace.
  - Ensure you use the same test database, fixtures, and environment variables as CI.
  - Re-run tests in a clean environment (docker or CI image) to isolate local state.

3) Linter / formatter errors
- Symptom: CI rejects PR due to style/lint failures.
- Fixes:
  - Run the project's formatter and linter locally (npm run lint / black . / isort .).
  - Configure your editor to use the project's configuration files.

4) Port already in use / server won't start
- Symptom: EADDRINUSE or bind error.
- Fixes:
  - Find the process using the port: lsof -i :<port> or ss -ltnp | grep <port> and stop it.
  - Change the default port via an env var or config.

5) Permission denied errors
- Symptom: EACCES when writing files or installing global packages.
- Fixes:
  - Avoid installing global packages; use npx or virtual environments.
  - Fix file permissions or run commands with correct user privileges.

6) Database migrations / schema mismatch
- Symptom: Missing column or migration errors after deploy.
- Fixes:
  - Run the migration tool (e.g., alembic upgrade head / prisma migrate deploy).
  - Check migration history and ensure deploy order is correct.

7) Secrets / env vars missing
- Symptom: Runtime errors referencing missing configuration.
- Fixes:
  - Create a .env from .env.example and populate required values.
  - On CI, ensure required secrets are set in project settings.

8) Performance problems in dev
- Symptom: Slow tests, hot reload not working.
- Fixes:
  - Use test subset or run tests in parallel (if supported).
  - Disable source maps or heavy tooling when not needed.

9) Build or bundling errors
- Symptom: Webpack/rollup/build failures.
- Fixes:
  - Clear the build cache and reinstall deps.
  - Check config files for breaking changes after dependency upgrades.

10) How to collect useful debug information for issues
- Steps to gather data:
  - Reproduce the issue and capture stdout/stderr and stack traces.
  - Note exact commands run, platform, runtime versions, and branch/commit.
  - If applicable, include database snapshots, logs, and minimal reproduction steps.

If none of the above solves the problem, open an issue with the collected debug information and link to relevant commits, logs, and reproductions.