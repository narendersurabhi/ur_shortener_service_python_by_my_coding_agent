# Contributing

Thanks for wanting to contribute! This document explains the minimal workflow we expect for issues, branches, commits, and pull requests so contributions can be reviewed and merged quickly.

Principles
- Keep changes small and focused.
- Write or update tests for bug fixes or new features.
- Make sure the project builds and lints locally before opening a PR.

Getting started
1. Fork the repository (or clone if you have push access).
2. Create a branch from main: feature/<short-description> or fix/<short-description>.
3. Make changes in that branch. Rebase or merge main regularly to keep your branch up to date.

Issue workflow
- Create a clear issue with steps to reproduce, expected and actual behavior, and any relevant logs or screenshots.
- If you plan to implement the issue, add a comment that you are working on it and link your branch/PR.

Branching & commits
- Branch names: feature/<summary>, fix/<summary>, docs/<summary>, chore/<summary>.
- Commit messages should be short and descriptive. Prefer conventional-style: type(scope): short summary
  - type: feat, fix, docs, style, refactor, test, chore
  - Example: feat(api): add pagination to /users
- Keep commits atomic and focused. Squash or rebase before merging if appropriate.

Pull request checklist
- Link the PR to the issue (e.g. fixes #123) if applicable.
- Describe what you changed and why.
- Include steps to test the change, and list platform/OS specifics if relevant.
- Run and pass all tests and linters locally.
- Add or update documentation where appropriate.

Review process
- A PR needs at least one approving review and CI passing to merge.
- Reviewers may request changes. Address them in follow-up commits.
- Maintainers may squash/merge and adjust commit messages to keep history tidy.

Tests & CI
- Add unit/integration tests for new logic or to prevent regressions.
- Keep tests deterministic and reasonably fast.

Code of conduct
- Be respectful and constructive. Treat others as you would want to be treated.
- If you have concerns about interactions in the project, contact maintainers privately.

Thank you for contributing. Small improvements and clear fixes are always welcome!