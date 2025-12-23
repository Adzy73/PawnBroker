# Contributing

Thanks for helping! This document explains how we collaborate via GitHub.

Branch naming
- Use `main` as the protected base branch.
- Create topic branches from `main` using these prefixes:
  - `feature/short-descriptive-name`
  - `bugfix/short-description`
  - `hotfix/short-description`

Workflow
- Create a branch locally: `git checkout -b feature/your-feature`
- Commit small, focused changes with clear messages (use `type: subject` style, e.g. `feat: add login`).
- Push the branch: `git push -u origin feature/your-feature`
- Open a Pull Request (PR) on GitHub targeting `main`.
- Request one or more reviewers, wait for review, and ensure CI checks pass.
- After approval and passing CI, merge using the repository's configured merge strategy.

Pull request checklist (use the template when creating PRs):
- Describe the change and why it's needed.
- Link any related issue or ticket.
- Ensure code is formatted and passes tests.

Running checks locally
- Syntax check: `python -m compileall .`
- Tests: `pytest` (if tests exist)

Code style
- Keep changes small and focused.
- Ask maintainers before large refactors.

If you're new to Git or GitHub and want hands-on help, ask here and a maintainer will guide you.
