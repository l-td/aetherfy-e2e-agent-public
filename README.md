# aetherfy-e2e-agent-public

Test fixture for the Aetherfy E2E test suite. **Do not delete.**

This repo is the public-repo target referenced by the GitHub-integration tests in
[`aetherfy-e2e-tests`](https://github.com/aetherfy/aetherfy-e2e-tests) — specifically:

- `tests/test_github.py::TestAgentGithubLinkage::test_link_and_unlink_public_repo`
- `tests/test_github.py::TestWebhookReceiver::test_valid_push_triggers_deployment`
- `tests/test_github.py::TestCLIFromGithub::test_from_github_public_repo_deploys`

Setup expectation: this repo's full path (`<owner>/aetherfy-e2e-agent-public`) must be set as
`GITHUB_TEST_REPO` in the e2e-tests `.env`, and the Aetherfy GitHub App must be installed on it.

A private mirror lives at `aetherfy-e2e-agent-private` and is exercised by a parallel test class.
