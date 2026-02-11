URL Shortener Service

A minimal URL shortener implemented with FastAPI. Features:
- REST API to shorten URLs and redirect to originals
- In-memory storage for mappings
- Basic URL validation
- Structured logging to stdout
- /health endpoint
- Tests with pytest
- Dockerfile for containerization

Quickstart (local)

1. Clone the repository

2. Create a virtual environment and install dependencies

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

3. Run the app (development)

# from project root
uvicorn app.main:app --host 0.0.0.0 --port 8000 --log-config log_config.yml

4. Endpoints

POST /shorten
- Request JSON: {"url": "https://example.com/path"}
- Response: {"short_id": "abc123", "short_url": "http://localhost:8000/abc123"}
- Validates scheme (http/https) and basic form

GET /{short_id}
- Redirects (307) to the original URL if found
- Returns 404 if not found

GET /health
- Returns 200 JSON {"status": "ok"}

Examples

Shorten a URL

curl -s -X POST -H "Content-Type: application/json" \
  -d '{"url":"https://www.example.com"}' \
  http://localhost:8000/shorten | jq

Follow redirect

curl -v http://localhost:8000/<short_id>

Run tests

pytest -q

Docker

Build

docker build -t url-shortener:latest .

Run

docker run -p 8000:8000 --env PORT=8000 url-shortener:latest

Configuration

- PORT: port to listen on (default 8000)
- BASE_URL: base host used when returning short_url (default http://localhost:8000)

Notes

- Storage is in-memory and ephemeral; for production replace with persistent store (Redis, PostgreSQL).
- Short IDs are compact and checked for collisions.
- Logging is structured (JSON) and goes to stdout for easy collection by log aggregators.

Contact

For details or improvements, see IMPLEMENTATION_PLAN.md for design choices and extension ideas.
