# Social previews and image delivery

Read for metadata, images, preview failures, and whole-site audits. Apply the relevant checks even when the framework generates the tags or image variants. Consult [SOURCES.md](SOURCES.md) for the protocol, search guidance, framework behavior, and consumer-specific limits.

## Validate the social object

Fetch representative home, profile, index, article/case, and other relevant templates from production. Include a missing page and any relevant redirect, locale, or preview environment. Inspect the raw response received by the sharing crawler as well as the browser DOM; hydrated tag presence does not prove a client can read it. If metadata streams, check the framework's handling of HTML-limited bots before changing it.

Check Open Graph's basic properties: `og:title`, `og:type`, `og:image`, and `og:url`. Validate description and site identity where useful. Values must describe this page: look for inherited homepage titles/descriptions, the wrong object type, staging origins, relative asset URLs, conflicting duplicates, and redirect/canonical disagreement. Sharing URLs should be stable public HTTPS destinations. Do not remove supported multiple images/authors as if all repetition were invalid.

For each image, associate `og:image:type`, width, height, and alt with the correct preceding root image tag. The Open Graph protocol gives the first value preference in conflicts; order matters. Metadata dimensions must match decoded pixels, MIME must match bytes, and alt should describe the image rather than repeat a caption. Keep article authors as profile URLs and timestamps as supported real dates when using those typed properties.

Inspect the actual `twitter:card`, title, description, image, and alt or their supported fallbacks. Some clients consume Open Graph, some card-specific tags; sharing behavior is not specified by Google Search. Verify the target consumer's current accepted formats, file size, dimensions/aspect ratio, cropping, and fallback behavior. A common 1200 × 630 design canvas is a starting convention, not an Open Graph eligibility rule.

Prefer an existing page image for Open Graph and Twitter when it represents the page and meets the intended consumer's requirements. This applies to posts, articles, projects, and other pages. Add a dedicated asset or generator only when no suitable image exists, an observed limitation requires it, or the user explicitly chooses a different presentation. Fix missing metadata without replacing a suitable image.

## Fetch and inspect the actual asset

Follow the declared image URL with GET as a logged-out client. Check final status, redirect target, content type, decoded dimensions, byte size, and visual content. Detect an HTML challenge/error at an image URL, expiring signed URLs, hotlink protection, authentication, or crawler-specific denial. Requesting a spoofed user-agent cannot prove the platform's servers can fetch it.

Compare the declared image with the delivered negotiated variant; filenames and tags alone cannot establish format. Open the image to check title legibility, clipping, contrast, and safe cropping on the intended card. Check generated route assets, screenshots, and default/fallback images, not just files under a public directory. A large browser screenshot is not automatically a useful social card.

Browser support for AVIF/WebP does not establish support in LinkedIn, Facebook, X, or another sharing client. Test WebP/AVIF for a named consumer before claiming compatibility. When a fallback is needed, prefer an existing or minimally converted PNG/JPEG version of the same visual before a new design or generator. Unverified compatibility is a verification gap, not evidence of a broken preview.

When available, inspect the actual preview using the target platform's official debugger/inspector or a supplied preview. Record date, consumer, and URL. A local tag parser is not a platform preview. If a stale preview persists, distinguish cached HTML/metadata, cached image bytes, and application inheritance before adding cache-busting URLs. Do not publish a post or submit private/signed preview URLs to a public debugger merely to validate metadata. When platform access is unavailable, report exactly which layers passed and which remain untested.

## Choose image formats by delivery and content

Google Image Search supports AVIF and WebP; using one is not itself a ranking improvement. Inspect the bytes users and crawlers receive before proposing source-file conversions. A framework/CDN may already convert a PNG/JPEG source into efficient variants.

- Compare AVIF and WebP at acceptable visual quality and rendered size. AVIF can reduce transfer size but encoding cost, first-request latency, decode behavior, and cache reuse may outweigh savings. Measure relevant assets rather than promising a fixed percentage.
- Preserve fine text, UI screenshots, diagrams, transparency, and color accuracy. PNG, lossless WebP, or SVG may suit a particular asset better than aggressive photographic compression. Retain appropriate SVG/vector assets instead of rasterizing every image.
- Use native `picture`/`source` or existing framework negotiation when multiple formats are warranted. Keep a valid `img src` fallback; check `srcset` and `sizes` against actual layout and device pixel ratios. Do not force every legacy format into the pipeline if supported clients already have a working fallback.
- For URL-based variants, verify the selected width/quality/format. For negotiation, verify forwarded `Accept`, response `Content-Type`, cache keys, `Vary`, and fallback bytes through the deployed CDN. Test both supported and unsupported-format requests after cache warming.

Google's support for AVIF does not make every agent or image-analysis tool an AVIF decoder. Important explanations should remain available as text rather than only inside screenshots. Preserve image context and suitable alt text; accessibility requirements depend on the image's purpose.

## Discoverability and loading

Use crawlable image URLs in meaningful HTML image elements; CSS backgrounds are not a substitute for informative image discovery. Ensure page and asset access policies agree. If using `picture`, retain its `img src` fallback. Examine lazy loading when a crawler cannot discover an image; use an image sitemap only when a real discovery gap warrants it, not as another compulsory file.

For performance, identify the actual LCP element and inspect its request waterfall. Avoid lazy-loading an LCP image; make it discoverable early and apply preload/fetch priority only where it addresses the observed delay. Avoid preloading every image or downloading competing fallback/preload candidates. Reserve layout space with correct intrinsic dimensions or aspect ratio and size below-fold images appropriately. Field experience and a repeatable lab trace answer different questions.

## Completion evidence

For affected templates, record the page URL, metadata source/response, image URL, decoded type/dimensions/bytes, negotiated request variant, and consumer-preview result or limitation. State the actual optimization opportunity: oversized source delivery, wrong responsive candidate, delayed LCP discovery, cache mix-up, unreadable crop, or unsupported card format. Do not create conversion work solely because an asset ends in `.png`, or mark a preview correct because `og:image` exists.
