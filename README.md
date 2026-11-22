# Web discovery and accessibility skills

Three skills help review public site behavior, search-facing content, and web interactions. Use the examples below to choose the right skill.

## Choose a skill

| Skill                                                          | Use it for                                                                                                                             | Verified case                                                                                                                                      |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| [technical-seo](skills/technical-seo/SKILL.md)                 | Crawl access, public responses, URLs, metadata, social cards, and discovery formats. Use this when the issue is in the delivered site. | On Nov 22, 2026, `andremarinho.me/projects/turistar/index.md` returned HTTP 200 as Markdown and included a canonical `Link` header.                |
| [search-content-review](skills/search-content-review/SKILL.md) | Whether search-facing claims are useful, clear, and supported by evidence. Use technical-seo for routes and rendered output.           | The `typed-svg-sprite` README reports 6.45% less gzip JavaScript but 1.73% more first-visit bytes, and warns against a general loading-time claim. |
| [web-accessibility](skills/web-accessibility/SKILL.md)         | Whether people can complete web interactions with keyboard and assistive technology.                                                   | In `ui-components-library/feature-carousel`, cards are `div` elements and dots are `span` elements. The source binds click handlers to both.       |

## Real cases

### Check the published response

The Turistar project Markdown route on `andremarinho.me` returned `200` with
`Content-Type: text/markdown`. Its `Link` header named the HTML project page as
canonical and linked `llms.txt` with `rel="describedby"`. The response body
contained the project text. This check confirms one live route. It does not
confirm search indexing or the rest of the site.

- [Live Markdown response](https://andremarinho.me/projects/turistar/index.md)
- [Route headers in `vercel.json`](https://github.com/andre-lmarinho/andremarinho.me/blob/main/vercel.json)

Use `technical-seo` to compare source configuration with the actual response.
Keep response checks, crawler access, and indexing evidence separate.

```text
Use technical-seo to compare this route's live response with vercel.json.
Report the status, content type, body, and canonical header for this route.
Do not infer indexing from a successful response.
```

### Review a measured claim

The `typed-svg-sprite` benchmark reports lower gzip JavaScript and higher
first-visit bytes for its tested workload. Its README keeps both results beside
the limitation that they do not prove a general loading-time improvement.
This is a real example of preserving measurement scope when editing a claim.

- [Benchmark summary and limits](https://github.com/andre-lmarinho/typed-svg-sprite/blob/main/README.md#performance-measurements)
- [Reproducible benchmark report](https://github.com/andre-lmarinho/typed-svg-sprite/blob/main/docs/performance-analysis.md)

Use `search-content-review` to check the claim, conditions, baseline, and nearby
caveats against the report.

```text
Use search-content-review to check the README benchmark summary against its report.
Keep the 6.45% gzip decrease and 1.73% first-visit increase in context.
Do not turn these results into a general loading-time claim.
```

### Inspect an interaction

The feature carousel in `ui-components-library` uses `div` cards and `span`
dots. Its script attaches click handlers to both sets. Source inspection shows
no keyboard handler for those controls. Source review does not establish what a browser or
screen reader announces.

- [Carousel markup](https://github.com/andre-lmarinho/ui-components-library/blob/main/feature-carousel/index.html)
- [Carousel interaction code](https://github.com/andre-lmarinho/ui-components-library/blob/main/feature-carousel/script.js)

Use `web-accessibility` to test keyboard operation and the rendered names,
roles, and states. Report those results only after testing them.

```text
Use web-accessibility to test keyboard access to the carousel cards and dots.
Start with the div and span controls that only have click handlers in the source.
Report browser results separately from untested screen-reader behavior.
```

## Install

Use the Skills CLI to select individual skills, or install the collection as a native plugin. Choose one method for each agent. This avoids duplicate copies.

### Skills CLI

From your project directory:

```sh
npx skills@latest add andre-lmarinho/skills
```

Choose your agent and the skills you want. To install one skill:

```sh
npx skills@latest add andre-lmarinho/skills --skill technical-seo
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

Ask your agent in plain language, or invoke a skill explicitly. For a Skills CLI installation, use `$technical-seo` in Codex or `/technical-seo` in Claude Code. The plugin namespaces its skills: `$andre-marinho-skills:technical-seo` or `/andre-marinho-skills:technical-seo`. Replace `technical-seo` with `search-content-review` or `web-accessibility` when needed.

## Sources

Each skill keeps a source ledger. It lists primary references, their authority and scope, review dates, and reasons to revisit them:

- [Technical SEO sources](skills/technical-seo/SOURCES.md): search-provider documentation, crawler controls, protocols, and discovery proposals.
- [Content review sources](skills/search-content-review/SOURCES.md): Google and Microsoft guidance, with provider-specific boundaries.
- [Accessibility sources](skills/web-accessibility/SOURCES.md): W3C standards, WAI evaluation guidance, and implementation patterns.

Normative requirements, provider guidance, community proposals, and local review heuristics remain distinct. Update the affected instruction and source record when guidance changes.

## Contribute and release

[AGENTS.md](AGENTS.md) records the repository conventions and checks. [Releasing](docs/releasing.md) explains the automated GitHub release, ZIP packaging, and directory submission steps.

## License

[MIT](LICENSE).
