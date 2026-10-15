# Sources

Checked **2026-10-15**. These are provider-specific requirements or guidance, not a universal GEO standard. Reopen the relevant primary source before changing crawler policy, claiming feature eligibility, or relying on a provider behavior that may have changed. If it is inaccessible, report that limit and preserve existing policy.

## Google Search documentation

| Source | Use |
| --- | --- |
| [Technical requirements](https://developers.google.com/search/docs/essentials/technical) | Public access, successful responses, indexable content; eligibility does not guarantee indexing. |
| [Robots meta and snippet controls](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag) | `noindex`, `nosnippet`, `max-snippet`, `data-nosnippet`, and `X-Robots-Tag`; directives require crawl access. |
| [Canonicalization methods](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) | Consistent canonical signals and HTTP canonical headers for supported non-HTML documents. |
| [JavaScript SEO](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) | Crawling/rendering/indexing distinctions; inspect output rather than banning client rendering. |
| [Crawlable links](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) | Real destinations and useful anchor context; no universal link-count quota. |
| [Sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) | Canonical public URLs and truthful significant-change dates. A sitemap is a hint. |
| [Title links](https://developers.google.com/search/docs/appearance/title-link) and [snippets](https://developers.google.com/search/docs/appearance/snippet) | Descriptive page-specific metadata; presentation can be rewritten or truncated. |
| [Structured data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) | Markup must match visible content; validation and rich-result eligibility are distinct. Check the current specific feature guide before adding a type. |
| [Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals) | User experience and field metrics, without treating scores as ranking guarantees. |
| [Generative AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | Search foundations apply; no special AI file, wording, chunk size, or schema is required. Google does not use llms.txt for ranking. |
| [Common crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) | Googlebot versus the Google-Extended product-control token; training/grounding controls differ from Search. |

## Other providers and optional discovery

| Source | Status and use |
| --- | --- |
| [OpenAI crawler documentation](https://developers.openai.com/api/docs/bots) | Provider documentation. OAI-SearchBot, GPTBot, and ChatGPT-User have different purposes and control semantics; consult current IP verification instructions when needed. |
| [Anthropic crawler documentation](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) | Provider documentation. Claude-SearchBot, ClaudeBot, and Claude-User have distinct roles. User-triggered access behavior differs across providers. |
| [Bing AI Performance](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/) | Provider product guidance. Citation reporting is scoped to supported surfaces; counts do not establish ranking or recommendation. Recheck current report coverage and availability. |
| [Open Graph protocol](https://ogp.me/) | Protocol specification for social graph metadata, not a Google ranking requirement. Check typed properties and consumer behavior when debugging previews. |
| [llms.txt proposal](https://llmstxt.org/) | Community proposal, v2 when checked. Curated index, Markdown alternatives, `rel="alternate"`, and `rel="describedby"`; not access control or proof of consumer adoption. |

For another engine, use its own current documentation instead of extrapolating these controls. For social metadata, consult the consuming platform's documentation; Google Search guidance does not specify social cards.

When updating: change the rule and this ledger together, retain the source's scope, and record the new check date. Source dates describe the source, not the reviewed site's editorial freshness.
