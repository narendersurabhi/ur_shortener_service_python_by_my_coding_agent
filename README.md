URL Shortener — Docker Quickstart

A compact, decoupled URL shortener with a beautiful frontend and a simple backend. This repository contains two services: a frontend (static UI) and a backend (API). Run them with Docker for a fast local demo.

Quick notes
- Frontend serves the UI (default port 8080) and talks to the backend via an env var BACKEND_URL.
- Backend serves the API (default port 8000).
- We recommend running both containers on a user-defined Docker network so the frontend can call the backend by name.

1) Build images (optional)
If you have the source locally, build images named url-shortener-backend and url-shortener-frontend:

docker build -t url-shortener-backend ./backend
docker build -t url-shortener-frontend ./frontend

2) Run with a dedicated Docker network (recommended)
Create a network so containers can talk by name:

docker network create url-net

Run the backend (exposes port 8000 on the host):

docker run -d --name url-backend --network url-net -p 8000:8000 \
  -e PORT=8000 \
  url-shortener-backend:latest

Run the frontend (serves UI on host port 8080). The container will use the backend by its container name via BACKEND_URL:

docker run -d --name url-frontend --network url-net -p 8080:80 \
  -e BACKEND_URL=http://url-backend:8000 \
  url-shortener-frontend:latest

Open the UI: http://localhost:8080

3) Alternative: Host mapping (no custom network)
If you prefer not to create a Docker network, run the backend and tell the frontend to call the host address. On macOS/Windows use host.docker.internal:

docker run -d --name url-backend -p 8000:8000 url-shortener-backend:latest

docker run -d --name url-frontend -p 8080:80 -e BACKEND_URL=http://host.docker.internal:8000 url-shortener-frontend:latest

On Linux, replace host.docker.internal with your host gateway (e.g. http://172.17.0.1:8000) or use the recommended user-defined network above.

4) Stop & cleanup

docker stop url-frontend url-backend && docker rm url-frontend url-backend
docker network rm url-net  # if you created it

5) Environment variables
- Backend
  - PORT (default 8000)
- Frontend
  - BACKEND_URL (full URL to backend, e.g. http://url-backend:8000)

6) Quick test (example)
If your backend exposes a JSON POST endpoint /api/shorten that accepts {"url":"..."}, you can test with:

curl -X POST -H "Content-Type: application/json" \
  -d '{"url":"https://example.com"}' \
  http://localhost:8000/api/shorten

Adjust the endpoint path to match your backend implementation.

Need help?
If something doesn't start, check container logs:

docker logs url-backend

docker logs url-frontend

Enjoy the pretty, decoupled URL shortener!