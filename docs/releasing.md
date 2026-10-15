# Releasing

The GitHub repository serves the skill files and the plugin marketplace. A release also produces a ZIP for versioned downloads and directory submissions. Both use the same `skills/` source tree.

## Publish a GitHub release

1. Merge the reviewed changes into `main`.
2. Open **Actions → Release → Run workflow**, select `main`, and enter a stable version such as `0.1.0`.
3. The workflow validates the package, synchronizes both plugin manifests, builds the ZIP, commits a version change when needed, pushes the commit and tag atomically, and creates the GitHub Release with the ZIP attached.

The portable `plugin.json` is the version source. A lower version or an existing release tag is rejected. Repository rules must allow this workflow's release commit and tag; it does not bypass branch protection. No npm account or third-party registry token is required.

If the tag was pushed but creating the Release failed, use the tagged revision to rebuild the ZIP and finish the Release with `gh release create --verify-tag`. Re-running the version workflow with an existing tag intentionally stops; do not bump again just to repair the missing Release.

## Build locally

Run these commands from the repository checkout. Build the current version without changing files:

```sh
python3 scripts/package.py build --output /tmp/andre-marinho-skills.zip
```

To prepare a version change locally:

```sh
python3 scripts/package.py version 0.2.0
```

Review both manifest changes before committing. The full checks need the tools listed in `scripts/requirements.txt` and Claude Code; the build and operational smoke check use Python's standard library:

```sh
curl --fail --silent --show-error --location \
  https://agent-plugins.org/schemas/1.0.0/plugin.schema.json \
  --output /tmp/agent-plugin.schema.json
python3 scripts/check.py --schema /tmp/agent-plugin.schema.json
python3 scripts/test_package.py
```

The CI workflow installs the validation tools and runs the same checks. A ZIP validates packaging; it does not establish that every skill makes the right decision on every task.

## How updates reach users

| Channel | Distribution and updates |
| --- | --- |
| Skills CLI | Installs directly from GitHub. Users run `npx skills@latest update` to update installed skills. |
| Own plugin marketplace | Users add `andre-lmarinho/skills` and install `andre-marinho-skills@andre-lmarinho`. Claude checks the plugin version for updates; auto-update for an added marketplace is opt-in. Other clients manage refresh according to their own behavior. |
| skills.sh directory | The Skills CLI reports genuine public-repository installs through its telemetry. A compatible repository does not guarantee directory indexing or a particular listing date. Do not generate fake installs in CI. |
| Public ChatGPT/Codex directory | Upload the release ZIP using a verified developer identity, resolve the portal checks, submit for review, and publish the approved version. Changes to skills or package metadata require a new ZIP. |
| Anthropic directory | Submit through Anthropic's developer portal with an eligible account and complete its review. This is separate from adding a GitHub marketplace and from `claude-plugins-official`. |

The GitHub workflow automates the repository release and ZIP. It does not claim an official-directory listing or automate account verification and review decisions.

## Primary references

Checked 2026-10-15. Recheck the relevant source when changing a manifest, installation route, update behavior, or submission process.

- [Agent Plugins specification](https://agent-plugins.org/) and [manifest schema 1.0.0](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json): portable package format.
- [OpenAI packaging](https://developers.openai.com/plugins/build/plugins): portable manifests, skill discovery, compatible marketplaces, and client-specific behavior.
- [OpenAI submission](https://developers.openai.com/plugins/deploy/submission): identity, ZIP upload, checks, review, and package updates.
- [Claude plugin reference](https://code.claude.com/docs/en/plugins-reference) and [marketplace reference](https://code.claude.com/docs/en/plugins/marketplace-reference): compatibility manifests and source paths.
- [Claude publishing](https://code.claude.com/docs/en/plugins/publish): marketplace distribution, versioned updates, auto-update settings, and directory submission.
- [Skills CLI](https://github.com/vercel-labs/skills) and [skills.sh documentation](https://skills.sh/docs): discovery, installation, updates, and directory behavior.
