# Engineering Skills

Agent skills for writing documentation that matches the code, reviewing search visibility, improving technical content, and finding barriers in web interfaces.

A README can lose a required default when shortened. A public article can send `noindex`. A control can have a label and still lack keyboard operation. These skills guide the agent through the evidence needed to find and correct those problems.

Each skill works independently, with a short workflow and detailed references loaded when needed. They use your existing tools and project conventions.

## Install

Use the Skills CLI to select individual skills, or install the collection as a native plugin. Choose one method per agent to avoid loading duplicate copies.

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

Update with `claude plugin update andre-marinho-skills@andre-lmarinho`. Automatic updates can be enabled for this marketplace in Claude's plugin settings; they are off by default for a marketplace you add.

### Codex plugin

```sh
codex plugin marketplace add andre-lmarinho/skills
codex plugin add andre-marinho-skills@andre-lmarinho
```

Use a client with plugin support. The Skills CLI route also works when the installed client does not provide plugin commands.

## Choose a skill

| You need to… | Skill | What it checks |
| --- | --- | --- |
| Write, shorten, or review engineering documentation | [engineering-docs](skills/engineering-docs/SKILL.md) | Reader needs, implementation accuracy, procedures, interface contracts, and scope. |
| Audit or fix how a site is discovered and interpreted | [technical-seo](skills/technical-seo/SKILL.md) | Crawling, rendering, indexing, canonical URLs, metadata, structured data, and AI-search access. |
| Review search-facing text and drafts for useful, supported information | [search-content-review](skills/search-content-review/SKILL.md) | Information value, evidence, entity clarity, unsupported claims, repetition, and context lost in excerpts. |
| Review or fix barriers in a web interface | [web-accessibility](skills/web-accessibility/SKILL.md) | Complete interactions, semantics, keyboard and assistive technology behavior, and applicable WCAG criteria. |

## Use the skills

Ask your agent in plain language, or invoke the installed skill explicitly. For a Skills CLI installation, use `$engineering-docs` in Codex or `/engineering-docs` in Claude Code. The plugin namespaces its skills: `$andre-marinho-skills:engineering-docs` or `/andre-marinho-skills:engineering-docs`. Substitute any skill from the table.

### Write documentation an engineer can act on

```text
Use engineering-docs to shorten content/README.md. Check its commands
and defaults against the implementation. Keep what a contributor needs
to publish content; remove details that belong elsewhere.
```

The skill starts with the reader's task, then checks the facts behind the prose. It preserves details that change behavior: required inputs, defaults, precedence, limits, error cases, and side effects.

Use it for root or folder READMEs, API and configuration reference, ADRs, RFCs, runbooks, and migration guides. It selects the structure the task needs instead of filling a universal template.

### Find technical barriers to search and retrieval

```text
Use technical-seo to audit the article routes and their public output.
Trace canonical URLs, metadata, sitemap entries, and Markdown alternatives.
Report the smallest useful fixes before changing files.
```

The skill follows representative content from source to response and rendered output. It distinguishes repository intent, local behavior, production access, and actual indexing evidence.

AI access is reviewed by provider and purpose. Search retrieval, user-triggered fetching, and model training have different controls. Optional formats such as llms.txt are assessed for a concrete consumer or workflow.

### Review what the text actually contributes

```text
Use search-content-review on this project case study. Identify sections
to keep, cut, merge, clarify, or substantiate. Test whether the main claims
remain accurate when read as excerpts. Preserve measurement conditions
and shared authorship.
```

The skill evaluates what a section helps the reader understand or decide, whether its claims are supported, and whether its subject and qualifications remain clear outside the surrounding page.

The excerpt check catches plausible misreadings. It does not simulate a private ranking system or predict citation probability. SEO/GEO recommendations distinguish provider guidance, observed results, and editorial judgment.

### Review complete interactions

```text
Use web-accessibility to review the checkout dialog and its error states.
Check keyboard and focus behavior, accessible names, and announcements.
Separate observed failures from interactions you cannot test here.
```

The skill uses WCAG 2.2 A and AA when another target is not specified. It combines source inspection, available automated checks, and manual interaction checks suited to the affected journey.

Findings identify the barrier, affected interaction, evidence, applicable criterion, and smallest correction. Browser and screen-reader results are reported only when those checks were actually performed.

## Sources

Each skill keeps a source ledger with primary references, their authority and scope, the date checked, and reasons to revisit them:

- [Documentation sources](skills/engineering-docs/SOURCES.md): Google Technical Writing, Microsoft Writing Style Guide, and Diátaxis.
- [Technical SEO sources](skills/technical-seo/SOURCES.md): search-provider documentation, crawler controls, protocols, and discovery proposals.
- [Content review sources](skills/search-content-review/SOURCES.md): Google and Microsoft guidance, with provider-specific boundaries.
- [Accessibility sources](skills/web-accessibility/SOURCES.md): W3C standards, WAI evaluation guidance, and implementation patterns.

Normative requirements, provider guidance, community proposals, and local review heuristics remain distinct. When guidance changes, the affected instruction and source record should change together.

## Contribute and release

[AGENTS.md](AGENTS.md) records the repository conventions and checks. [Releasing](docs/releasing.md) explains the automated GitHub release, ZIP packaging, and directory submission steps.

## License

[MIT](LICENSE).
