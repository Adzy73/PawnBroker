# PawnBroker

Quick collaboration guide for contributors.

How to contribute
- See [CONTRIBUTING.md](CONTRIBUTING.md) for branch naming, PR workflow, and local checks.

Basic git commands for collaborators

```bash
# configure your name/email if needed
git config --global user.name "Your Name"
git config --global user.email you@example.com

# create a feature branch
git checkout -b feature/your-feature

# work, stage, commit
git add .
git commit -m "feat: short description of change"

# push branch and create PR
git push -u origin feature/your-feature
# then open a PR on GitHub and request reviews
```

Setting Branch Protection (recommended)
- On GitHub: go to `Settings` → `Branches` → `Add rule` for `main`.
- Require pull request reviews before merging.
- Require status checks to pass (select `CI` checks after they run once).
- Optionally require signed commits.

If you'd like, I can help run the initial `git` commands and push these files for you — tell me if you want that.
