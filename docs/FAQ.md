# FAQ

This FAQ covers common questions for working with this codebase.

Q: What is this repository?
A: This repo contains the code and docs for the project. Check the root README.md for an overview and basic commands.

Q: How do I run the project locally?
A: See README.md for the canonical commands. Typical steps:
- Install dependencies: npm install / pip install -r requirements.txt (depending on language)
- Run tests: npm test / pytest
- Start locally: npm start / python -m <module>

Q: How do I run tests and linters?
A: Run the test command in the README. Common commands:
- npm test or yarn test
- pytest
- npm run lint or flake8

Q: Where are the coding standards and style rules?
A: Look for .eslintrc, .prettierrc, pyproject.toml or CONTRIBUTING.md. If not present, follow the main language community style (PEP8 for Python, Airbnb style for JavaScript).

Q: How should I add a new feature?
A: 1) Create a feature branch. 2) Add tests first. 3) Implement code and run tests locally. 4) Run linters and formatters. 5) Open a PR with a clear description and link to any issue.

Q: How do I report a bug or request a feature?
A: Open an issue in the repository with steps to reproduce, expected vs actual behavior, environment, and logs or stack traces when available.

Q: Who can I contact for help?
A: Use the repository maintainers listed in the README or the project's issue tracker.

Q: Where are environment or secret variables configured?
A: Check README and sample env files (e.g., .env.example). Never commit secrets to the repo.

Q: How are releases and versioning handled?
A: Check the CHANGELOG.md or release workflow in the .github/workflows folder. If absent, use semantic versioning and document releases in the changelog.