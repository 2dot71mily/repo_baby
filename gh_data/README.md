### gh data

This repo's metadata scraped via `gh` api.

Investigating what can scrape commit hash for squashed pr4's sub-commit:
https://github.com/2dot71mily/repo_baby/pull/4/commits/5bdb9b155e27193208056f293e29788c3bb3a163

#### Events
`repo_baby_events.jsonl` obtained via:
```
gh api \
   -H "Accept: application/vnd.github+json" \
   -H "X-GitHub-Api-Version: 2022-11-28" \
   /repos/2dot71mily/repo_baby/events  > repo_baby_events.json
```
Ctrl-f of `repo_baby_events.json` does not find above hash in question: `5bdb9b155e27193208056f293e29788c3bb3a163`.
But does find many `commit`, `head`, `sha` metadata for other commits.


#### PR Commits
`repo_baby_pr4_commits.json` obtained via:
```
gh pr view https://github.com/2dot71mily/repo_baby/pull/4/ --json commits > repo_baby_pr4_commits.json
```
In this data we **do** see the commit hash for the squashed commit: `5bdb9b155e27193208056f293e29788c3bb3a163`