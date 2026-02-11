# UR Shortener Service (Python) — by my coding agent

Small URL shortening service (backend + frontend). This README focuses on common developer tasks and includes runnable commands in fenced code blocks.

## Requirements

- Docker & docker-compose (for stack deployment)
- Python 3.9+ (for local development)
- pip / virtualenv

## Quickstart (docker-compose)

Start the frontend and backend as a stack:

```bash
docker-compose -f docker-compose.yml up --build -d
```

View logs:

```bash
docker-compose -f docker-compose.yml logs -f
```

Stop and remove the stack:

```bash
docker-compose -f docker-compose.yml down
```

## Local development (backend)

Create a virtual environment and install deps:

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

Run the backend (example using Flask):

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=8000
```

Example request (create short URL):

```bash
curl -s -X POST http://localhost:8000/shorten \
  -H "Content-Type: application/json" \
  -d '{"url":"https://example.com"}' | jq
```

## Tests / CI

Run the test suite locally with pytest:

```bash
pytest -q
```

The repository includes a GitHub Actions workflow to run these tests on push and pull requests (see .github/workflows). The workflow invokes the same pytest command above.

## Contributing

- Open an issue or a PR
- Keep changes small and add/maintain tests

## Notes

This README was updated to include fenced command and code blocks for clarity during development and CI. For deployment and CI specifics, inspect the repository's docker-compose.yml and .github/workflows/*.yml files.