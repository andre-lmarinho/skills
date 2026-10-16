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
| [Open Graph protocol](https://ogp.me/) | Protocol definition. Basic object properties, image property grouping/order, image descriptions, article/profile types. Does not prescribe one image canvas or universal consumer format support. |
| [llms.txt proposal](https://llmstxt.org/) | Community proposal, v2 dated 2026-08-10. Curated/scoped indexes, Markdown alternatives, and alternate/describedby discovery; not a Google requirement or proof of consumer adoption. |

For another engine, use its own current documentation instead of extrapolating these controls. For social metadata, consult the consuming platform's documentation; Google Search guidance does not specify social cards.

When updating: change the rule and this ledger together, retain the source's scope, and record the new check date. Source dates describe the source, not the reviewed site's editorial freshness.

## Agent formats and transport

| Primary source | Status and decision supported |
| --- | --- |
| [Mintlify: llms.txt](https://www.mintlify.com/docs/ai/llmstxt) | Platform documentation. Generated index and combined full-text export; verifies a working convention, not universal search-engine ingestion. |
| [Mintlify: agent-friendly documentation](https://www.mintlify.com/library/how-to-make-your-documentation-agent-friendly) | Platform guidance. Broad context versus selective reading, tool/context limits, and authorization boundaries. Product behavior is not a requirement for other sites. |
| [AI Hero sitemap.md](https://www.aihero.dev/sitemap.md) and [public discovery API](https://www.aihero.dev/api) | Observed implementation, HTTP 200 on 2026-10-15. Markdown catalogue covers route families, text twins, and JSON discovery; `/api` exposes structured formats/resources. Its llms.txt uses a local hint format rather than the proposal's required H1. Naming and coverage are site conventions, not universal standards. |
| [RFC 7763](https://www.rfc-editor.org/info/rfc7763/) | Informational RFC registering `text/markdown`; not a GEO discovery specification. |
| [RFC 9110, Vary](https://httpwg.org/specs/rfc9110.html#field.vary) | HTTP semantics. Representation selection and caches; a CDN's actual key/configuration still needs testing. |
| [RFC 9727](https://www.rfc-editor.org/info/rfc9727/) | Standards-track API catalogue discovery. Relevant when publishing/discovering APIs; does not require a website to build an API. |
| [Cloudflare: Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) | Vendor documentation, updated 2026-10-09 when checked. Negotiated conversion, response-header changes, and default Content-Signal behavior. Applies to that feature, not arbitrary origin negotiation. |
| [Cloudflare: origin cache control](https://developers.cloudflare.com/cache/concepts/cache-control/) | Vendor documentation. General Vary behavior has configuration exceptions; emitting the header alone does not establish separate cache variants. |

## Images and social implementation

| Primary source | Status and decision supported |
| --- | --- |
| [Google: image SEO](https://developers.google.com/search/docs/appearance/google-images) | Search provider guidance. AVIF/WebP support, crawlable image references, picture/img fallback, responsive images, descriptive context, and conditional image sitemaps. Does not establish another consumer's codec support. |
| [web.dev: AVIF](https://web.dev/learn/images/avif) | Browser-engineering guidance, dated 2023-02-01. Encoding/quality tradeoffs and resilient delivery. Recheck current client support; historical browser-version statements are not today's support matrix. |
| [web.dev: optimize LCP](https://web.dev/articles/optimize-lcp) | Browser performance guidance. Resource discovery, prioritization, loading phases, and field/lab distinctions; compression alone does not fix every LCP delay. |
| [Next.js: generateMetadata](https://nextjs.org/docs/app/api-reference/functions/generate-metadata) | Framework documentation. Metadata inheritance, file conventions, and streamed metadata handling for HTML-limited bots. Use only for a matching installed framework/version. |

Access notes for this review: the [legacy X large-image-card documentation](https://developer.x.com/en/docs/x-for-websites/cards/overview/summary-card-with-large-image) redirected to a general overview; the corresponding `docs.x.com/x-for-websites/cards/overview/summary-card-with-large-image` URL was inaccessible. No current X-specific byte/format limit was verified, so the skill does not freeze one. Obtain the target platform's current requirements and actual preview before claiming compatibility. Some raw HTTP fetches of Mintlify/Cloudflare returned 403 while their official documentation was readable through browsing; those failed requests do not establish general agent access.

## Decision-rule update — 2026-10-15

Added conditional references because the initial workflow named agent formats and media without enough selection or verification criteria. The revision now distinguishes per-page coverage, full-context export, broader discovery, and API use; requires body/cache/publication checks; and separates browser images from consumer-tested social previews. The full-export acceptance checks, portfolio candidates, common image canvas, and cost/benefit decisions are engineering heuristics informed by these sources, not provider ranking rules. Sources were checked for the scope recorded in each row; examples demonstrate implementation, not a visibility uplift.
