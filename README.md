# repo_baby

This main dir is function & unittest pairs composed via:
- commits directly to main
- commits to main via pull request
- commits to main via squashed pull request

See `docker` dir to build a container that downloads the repo, installs requirements, and runs unittests.

See `gh_data` dir for json of this repo's events and PR commits scraped via `gh` api.