# Agent access and discovery

Read for agent-access work, machine-readable formats, and whole-site audits. Source categories and maintenance notes are in [SOURCES.md](SOURCES.md). The selection rules below are engineering judgments, not universal GEO eligibility requirements.

## Access before formats

Identify the intended consumer and task: search inclusion, user-requested page reading, or bulk context for a coding/research assistant. Preserve the site's existing training policy.

- OpenAI documents separate controls for OAI-SearchBot, ChatGPT-User, and GPTBot. User-triggered retrieval does not have identical robots semantics to automatic search crawling.
- Anthropic distinguishes Claude-SearchBot, Claude-User, and ClaudeBot. Do not copy OpenAI's retrieval-policy assumptions to Anthropic.
- Googlebot and Google-Extended serve different purposes; Google-Extended is not the Google Search indexing control.

Reopen the provider's documentation before changing rules or IP allowlists. Inspect robots, meta/HTTP directives, redirects, assets, CDN challenges, and rate limits together. A request carrying a bot's user-agent tests routing only; verify actual bot access through the provider's published verification method or trusted logs. Do not broadly disable WAF rules or allow training merely to enable search.

## Select page families for Markdown

Choose by the information an agent needs, not by file count or whether a route is called marketing. Assess these candidates against the actual site:

| Page family | Decision criterion |
| --- | --- |
| Articles, cases, reference docs, tutorials | Usually strong candidates: substantial reusable explanations, examples, or evidence. |
| About, professional profile, résumé | Useful when agents need identity, role, qualifications, availability, or hiring context. Preserve public facts and links; offer a maintained text representation of a public PDF only if its extraction is a real obstacle. |
| Home, product/service, pricing, policy pages | Useful when they contain authoritative positioning, capabilities, terms, or current public facts absent from detail pages. Preserve scope and conditions; do not exclude them categorically. |
| Indexes, categories, catalogues | Export when summaries or navigation help locate resources. An existing generated discovery index may already serve the task. |
| Forms, applications, maps, interactive tools | Text can explain inputs, outputs, limits, and links, but cannot replace the interaction. Preserve meaningful diagrams/data through descriptions where needed. |
| Private, paid, draft, removed, duplicate, session-specific pages | Match authorization and publication boundaries in every format. Do not publish a public text twin of restricted content or generate endless URL variants. |

For each selected family, identify its maintained source, canonical human URL, Markdown URL, and discovery path. Reuse the source/publishing filter rather than hand-maintaining a parallel article. Carry title, entity/author, qualifications, relevant dates, examples, and evidence needed to understand the page. Do not remove essential caveats while removing navigation. Resolve relative links against the correct source URL; aggregates need rewritten links/anchors so references still reach their intended page.

## Choose the discovery surface

| Surface | Job and adoption decision |
| --- | --- |
| `sitemap.xml` | Search discovery of intended canonical URLs. Keep the search contract and truthful dates; other indexes do not replace it. |
| `llms.txt` | Concise curated starting point with context and links. Check the community proposal's format and scope; root and section-scoped files can coexist. Prefer detailed agent-readable destinations where available. |
| Per-page Markdown | Selective reading and precise source attribution. Follow the site's established route convention; the proposal describes `.md` alternatives and directory `index.md` forms. Advertise them with `alternate`/`text/markdown`, and the covering index with `describedby`, in HTML or HTTP links. |
| `llms-full.txt` | Complete text export for a task requiring broad context in one fetch. This is an implemented convention, not a required companion or a cure for indexing. Apply the acceptance checks below. |
| `sitemap.md` | Generated, broader Markdown catalogue when a small curated index cannot expose useful route families, resource descriptions, or format choices. Use the site's naming convention; no general SEO requirement mandates this filename. |
| JSON search/discovery, OpenAPI, API catalogue | Prefer an existing interface when agents need exact lookup, filters, pagination, or an API contract. RFC 9727 standardizes API catalogue discovery, not a mandatory website endpoint. Consider this only for an actual API/workflow; a portfolio does not need a new MCP server to expose its articles. |

If a catalogue outgrows the reader's fetch budget, consider grouped indexes linked from a small entry point; verify every group remains reachable through the deployed proxy. Existing platforms may already generate this hierarchy. A second flat index that duplicates the first adds little.

The llms.txt proposal specifies its own format; a site's file with that name may implement a different local contract. Check both syntax and usefulness instead of copying an example uncritically. AI Hero's public `sitemap.md` demonstrates a route-family catalogue, Markdown twins, and JSON discovery; its implementation is an example, not a standard to require elsewhere.

## Decide when to add llms-full.txt

Recommend it when a concrete task benefits from reading several pages together, the selected corpus fits the target tool's fetch and context limits, and generation can share the public-content pipeline. Examples include evaluating a public professional profile with its cases, onboarding to a bounded library, or comparing related policies. A small site can meet these conditions now; there is no minimum number of posts to wait for.

Before recommending an export:

- Define its public scope. Keep separate product versions, languages, or conflicting editions identifiable; avoid silently merging mutually exclusive instructions.
- Measure bytes and, when useful, tokens with the intended consumer. Verify representative facts near both the beginning and end survive retrieval. A downloadable file may still be truncated or too large to use.
- Retain source URLs and clear document boundaries. Preserve authorship, scenario limits, and supported dates; make internal links usable from the aggregate.
- Generate, invalidate, and remove content alongside the source, including deleted, unpublished, or restricted entries. An automatically generated file can still use the wrong publication filter.
- Link the export from the existing discovery surface so a user or agent can choose it; keep per-page retrieval for focused questions and precise attribution.

Defer when no broad-context task exists, the target client truncates it, or maintaining a faithful public export would introduce disproportionate work. State the trigger for revisiting: an identified cross-page workflow, observed fetch-limit problem, or an existing generator that makes the export inexpensive. Large corpora can use scoped exports or existing search rather than an unbounded full-site dump. Do not use arbitrary KB/token quotas or observed fetches elsewhere as a forecast of citations here.

## Verify the representations

Use GET, not HEAD alone, for every introduced format and representative existing family. Confirm status, MIME/encoding, actual body, discoverable links, working examples, and source fidelity. Markdown should be served as Markdown, not a 200 HTML wrapper. Treat canonical relationships as signals whose search-engine support must be checked for that format.

For `Accept: text/markdown` negotiation, test HTML, Markdown, and the default request through the deployed CDN in alternating order after cache warming. Check `Vary: Accept`, actual cache-key separation, validators, and preservation of other varying headers. The header alone does not establish correct CDN behavior. Separate URLs may be simpler when cache variants cannot be controlled. Verify the same issue for negotiated image formats.

Exercise missing, unpublished, restricted, redirected, and removed URLs across formats and indexes. Confirm sensitive content is neither exported nor shared-cached. If using an edge converter, inspect losses in code, links, images, and late-rendered content; check any added content-use policy headers before enabling it. Cloudflare documents its converter's behavior separately from its general cache rules. Its converter can add `Content-Signal` with `ai-train=yes` when the origin supplies no policy; preserve the intended policy before enabling conversion. Do not extrapolate this behavior to every CDN.

Test discovery with a realistic question starting only from the published entry point. Record the fetch path, pages used, missing facts, and client limits. Separately track verified machine fetches, human referrals, citations, and the business outcome. A parsed index or a high tool score is not proof that an assistant discovers or recommends the site.
