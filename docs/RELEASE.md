# Release Guide

This document describes a concise, repeatable release process for the repository. Keep releases small and atomic.

Prerequisites
- CI green and all tests passing.
- Local workspace up-to-date: git fetch && git checkout main && git pull
- Have appropriate permissions to push and create releases.

Versioning
- Use Semantic Versioning: MAJOR.MINOR.PATCH
- Bump only the component that changed: incompatible API -> MAJOR, new features -> MINOR, bugfixes -> PATCH.

Quick checklist
- [ ] Update CHANGELOG.md (move Unreleased entries to the new version section with date)
- [ ] Bump version in relevant files (package.json, pyproject.toml, etc.)
- [ ] Run tests and lint
- [ ] Commit and tag the release
- [ ] Push and create a release on the remote (GitHub/GitLab)
- [ ] Publish artifacts (registry, container, etc.)

Recommended step-by-step
1. Prepare
   - git checkout main
   - git pull origin main
   - ensure all changes to include are merged into main

2. Update changelog
   - Edit CHANGELOG.md: copy Unreleased content under a new heading for the release version and add the release date.
   - Example heading: ## [1.2.3] - 2026-02-11

3. Bump version
   - Update project version in the appropriate files. Common examples:
     - npm: npm version patch|minor|major -m "chore(release): %s"
     - Python (manual): update pyproject.toml / __version__ and commit

4. Run checks
   - Run the test suite and linters locally or via CI.

5. Commit
   - git add -A
   - git commit -m "chore(release): vX.Y.Z"

6. Tag and push
   - git tag -a vX.Y.Z -m "Release vX.Y.Z"
   - git push origin main --follow-tags

7. Create release on remote
   - GitHub CLI: gh release create vX.Y.Z --title "vX.Y.Z" --notes-file CHANGELOG.md
   - Or create release via web UI and paste the changelog section for the version.

8. Publish artifacts
   - Publish to package registries or container registries as needed (npm publish, twine upload, docker push, etc.).

9. Post-release
   - Verify package availability and CI status.
   - Update docs/site if the release introduces user-visible changes.

Rollback
- If release must be reverted:
  - Create a new patch release that reverts the offending change, or
  - Delete the tag and release (if still safe) and push corrective commits.

Examples
- Bump patch and tag (npm example):
  - npm version patch -m "chore(release): %s"
  - git push origin main --follow-tags
  - gh release create vX.Y.Z --notes-file CHANGELOG.md

Tips
- Keep CHANGELOG.md concise: short bullets grouped by Added/Changed/Fixed.
- Automate where possible (CI checks, changelog generation, release creation via CLI).

If you follow this checklist and record the changes in CHANGELOG.md, releases will remain reproducible and traceable.
