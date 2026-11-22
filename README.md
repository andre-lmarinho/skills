# Engineering Skills

Four focused skills cover engineering documentation, site discovery, search-facing content, and web accessibility. Each uses a short workflow and loads detailed references when needed.

## Choose a skill

| Skill | Use it for | Example request |
| --- | --- | --- |
| [engineering-docs](skills/engineering-docs/SKILL.md) | Technical documents that help engineers operate software or understand a contract. It checks details against the implementation. | Check this runbook's commands and defaults against the code. |
| [technical-seo](skills/technical-seo/SKILL.md) | Site behavior that affects crawling, URLs, metadata, structured data, previews, or retrieval. | Trace an article from source through its public response, canonical URL, metadata, and social card. |
| [search-content-review](skills/search-content-review/SKILL.md) | Search-facing text: its value to readers, support for its claims, and context in excerpts. Use technical-seo for site implementation. | Review this case study's claims and excerpts. Flag what to clarify or substantiate. |
| [web-accessibility](skills/web-accessibility/SKILL.md) | Barriers in web interactions, including semantics, keyboard behavior, assistive technology, and complete user journeys. | Check the checkout dialog's error states, focus, and keyboard behavior. |

## Install

Use the Skills CLI to select individual skills, or install the collection as a native plugin. Choose one method for each agent. This avoids duplicate copies.

### Skills CLI

From your project directory:

```sh
npx skills@latest add andre-lmarinho/skills
```

Choose your agent and the skills you want. To install a specific skill:

```sh
npx skills@latest add andre-lmarinho/skills --skill engineering-docs
```

Add `--global` to make the selected skills available across projects. The installer lists supported agents and installation destinations. Check for existing skills with the same names before replacing them.

Update installed skills with:

```sh
npx skills@latest update
```

### Claude Code plugin

```sh
claude plugin marketplace add andre-lmarinho/skills
claude plugin install andre-marinho-skills@andre-lmarinho
```

Update with `claude plugin update andre-marinho-skills@andre-lmarinho`. Claude turns off automatic updates for added marketplaces by default. Enable updates in Claude's plugin settings.

### Codex plugin

```sh
codex plugin marketplace add andre-lmarinho/skills
codex plugin add andre-marinho-skills@andre-lmarinho
```

Use a client with plugin support. The Skills CLI route also works when the installed client does not provide plugin commands.

## Use a skill

Ask your agent in plain language, or invoke the installed skill explicitly. For a Skills CLI installation, use `$engineering-docs` in Codex or `/engineering-docs` in Claude Code. The plugin namespaces its skills: `$andre-marinho-skills:engineering-docs` or `/andre-marinho-skills:engineering-docs`. Substitute any skill from the table.

## Sources

Each skill keeps a source ledger. It lists primary references, their authority and scope, review dates, and reasons to revisit them:

- [Documentation sources](skills/engineering-docs/SOURCES.md): Google Technical Writing, Microsoft Writing Style Guide, and Diátaxis.
- [Technical SEO sources](skills/technical-seo/SOURCES.md): search-provider documentation, crawler controls, protocols, and discovery proposals.
- [Content review sources](skills/search-content-review/SOURCES.md): Google and Microsoft guidance, with provider-specific boundaries.
- [Accessibility sources](skills/web-accessibility/SOURCES.md): W3C standards, WAI evaluation guidance, and implementation patterns.

Normative requirements, provider guidance, community proposals, and local review heuristics remain distinct. Update the affected instruction and source record when guidance changes.

## Contribute and release

[AGENTS.md](AGENTS.md) records the repository conventions and checks. [Releasing](docs/releasing.md) explains the automated GitHub release, ZIP packaging, and directory submission steps.

## License

[MIT](LICENSE).
