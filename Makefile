SHELL := /bin/sh
VENV ?= .venv

.PHONY: help setup install test run lint fmt clean ci

help:
	@printf "Usage:\n  make setup   Install dependencies\n  make run     Run the app\n  make test    Run tests\n  make lint    Lint project\n  make fmt     Format code\n  make clean   Clean artifacts\n  make ci      setup + test + lint\n"

# Install project dependencies (Python or Node if present)
setup:
	@if [ -f requirements.txt ]; then \
		python3 -m venv $(VENV) && . $(VENV)/bin/activate && pip install -r requirements.txt; \
	elif [ -f package.json ]; then \
		npm install; \
	else \
		echo "No requirements.txt or package.json found; nothing to install."; exit 0; \
	fi

install: setup

# Run the project using common entrypoints
run:
	@if [ -f app.py ]; then \
		python3 app.py; \
	elif [ -f server.js ]; then \
		node server.js; \
	elif [ -f package.json ] && grep -q "\"start\"" package.json 2>/dev/null; then \
		npm start; \
	else \
		echo "No runnable entrypoint found (app.py, server.js, or package.json start)."; exit 1; \
	fi

# Run tests via npm or pytest (if tests/ exists)
test:
	@if [ -f package.json ] && grep -q "\"test\"" package.json 2>/dev/null; then \
		npm test; \
	elif [ -d tests ] || ls tests 2>/dev/null >/dev/null; then \
		pytest -q; \
	else \
		echo "No tests found."; exit 0; \
	fi

# Lint using ESLint or Flake8 if available/configured
lint:
	@if command -v eslint >/dev/null 2>&1 && [ -f .eslintrc ] || [ -f package.json ] && grep -q "eslintConfig" package.json 2>/dev/null; then \
		eslint . || true; \
	elif command -v flake8 >/dev/null 2>&1; then \
		flake8 . || true; \
	else \
		echo "No linter configured or installed (eslint/flake8)."; exit 0; \
	fi

# Format code using Black or Prettier if available
fmt:
	@if command -v black >/dev/null 2>&1; then \
		black . || true; \
	elif command -v prettier >/dev/null 2>&1; then \
		prettier --write . || true; \
	else \
		echo "No formatter configured or installed (black/prettier)."; exit 0; \
	fi

clean:
	rm -rf $(VENV) .pytest_cache build dist node_modules *.egg-info

ci: setup test lint
