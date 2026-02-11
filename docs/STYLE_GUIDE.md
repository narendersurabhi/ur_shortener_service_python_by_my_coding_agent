# Style Guide

This guide is intentionally minimal and language-agnostic. Follow existing patterns in the codebase when in doubt.

Formatting
- Use an automatic formatter where available (Prettier, Black, gofmt, rustfmt, etc.).
- Keep line length reasonable (80–100 chars preferred).

Naming
- Use clear, descriptive names for functions, variables, types, and modules.
- Prefer nouns for types/classes and verbs for functions.
- Use consistent casing across the repo (camelCase, snake_case, or kebab-case) based on the language ecosystem.

Structure & modularity
- Keep functions small and single-purpose. If a function exceeds ~50 lines, consider splitting it.
- Group related code into modules or packages with clear public APIs.
- Avoid deep nesting; prefer early returns/guards.

Error handling
- Handle errors explicitly and surface useful messages for debugging.
- Avoid swallowing errors silently; log or propagate them with context.

Documentation & comments
- Document public APIs with concise descriptions and examples when non-obvious.
- Prefer self-documenting code; use comments to explain why, not what.

Tests
- Tests should be deterministic and cover edge cases.
- Use descriptive test names and group related tests together.

Logging
- Use structured logging where possible. Avoid printing raw debug messages to stdout in libraries.
- Do not log secrets or sensitive data.

Security & dependencies
- Validate external input and sanitize where appropriate.
- Keep dependencies up to date and prefer well-maintained, lightweight libraries.

Performance
- Optimize only when necessary. Start with clear, correct implementations and measure bottlenecks before micro-optimizing.

Commit & PR etiquette
- Link commits/PRs to issues when applicable.
- Keep PRs focused. Large architectural changes may be split across multiple PRs with descriptive plans.

When in doubt
- Follow existing patterns used across the repository.
- Ask maintainers or open an issue discussing alternatives if a change will affect APIs or public behavior.

This guide should be a living document — please propose improvements via PRs.