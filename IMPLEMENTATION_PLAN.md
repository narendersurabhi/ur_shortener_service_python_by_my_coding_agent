# Implementation Plan

Objective

Create a compact deployment and CI setup for the ur_shortener_service_python_by_my_coding_agent repository:
- Add a docker-compose stack to run frontend and backend
- Add a GitHub Actions CI workflow that runs repository tests
- Improve README.md to include fenced code blocks for commands and snippets

Deliverables

- docker-compose.yml (root)
- .github/workflows/ci.yml (CI workflow)
- README.md improvements (use fenced code blocks)
- Tests run via pytest (backend) and npm (frontend) if present

Plan (compact steps)

1) Inspect repository layout
- Ensure there are backend/ and frontend/ folders (or adapt paths)
- Ensure backend has requirements.txt and tests/ using pytest
- Ensure frontend has package.json and tests if applicable

2) Add docker-compose.yml (root)
- Purpose: build and run both services for local development and quick deploy
- Minimal recommended content (create file with this template):

```yaml
version: '3.8'
services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - PORT=8000
    restart: unless-stopped
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend
    restart: unless-stopped
networks:
  default: {}
```

Notes: adapt backend port, Dockerfiles should exist in backend/ and frontend/ directories. Use lightweight base images in Dockerfiles.

3) Add GitHub Actions CI workflow
- Path: .github/workflows/ci.yml
- Trigger: push and pull_request
- Jobs: test (runs both backend and frontend tests if present)
- Minimal workflow template to create:

```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install backend deps & run tests
        if: exists('backend/requirements.txt')
        run: |
          python -m pip install -U pip
          pip install -r backend/requirements.txt
          pytest -q

      - name: Set up Node and run frontend tests
        if: exists('frontend/package.json')
        uses: actions/setup-node@v4
        with:
          node-version: '18'
      - name: Install frontend deps & run tests
        if: exists('frontend/package.json')
        run: |
          cd frontend
          npm ci
          npm test --if-present
```

This workflow is compact and skips steps if folders or manifest files do not exist.

4) Improve README.md
- Add a short "Local development" section with fenced code blocks for common commands:

Examples to add to README.md:

```bash
# Build and run stack
docker compose up --build -d

# Stop
docker compose down

# Run backend tests
cd backend && pytest

# Run frontend tests
cd frontend && npm ci && npm test
```

- Add a small "CI" note that points to .github/workflows/ci.yml

5) Tests and verification
- Ensure backend has tests/ and pytest configured. If tests missing, add at least one smoke test (e.g., tests/test_smoke.py) that imports the app and asserts response.
- Run locally to verify:
  - pip install -r backend/requirements.txt
  - pytest
  - cd frontend && npm ci && npm test (if applicable)
  - docker compose up --build -d
  - curl -f http://localhost:8000/ (or appropriate endpoint)

6) Commit flow
- Create branch, add files, run tests, push, open PR

Commands:

```bash
git checkout -b ci-compose-setup
git add docker-compose.yml .github/workflows/ci.yml README.md
git commit -m "Add docker-compose, CI workflow, and README improvements"
git push -u origin ci-compose-setup
```

7) Minimal validation checklist
- [ ] docker-compose up builds both services
- [ ] pytest runs and passes on CI and locally
- [ ] README contains fenced code blocks for commands
- [ ] GitHub Actions shows green on push/PR

Notes and constraints
- Compose file is intentionally minimal; tune images, healthchecks, volumes, and env files as needed
- CI job uses conditional steps based on existence of files to keep it robust across repo shapes
- Keep Dockerfiles small and secure (multi-stage builds if needed)

Estimated time
- ~30–90 minutes depending on existing repo state (Dockerfiles/tests present or not)

Next step
- Implement the files listed above (docker-compose.yml, .github/workflows/ci.yml) and update README.md. Run local tests and push.
