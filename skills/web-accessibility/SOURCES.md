# Sources and maintenance

Baseline checked: 2026-10-15; affected references rechecked: 2026-10-17. The skill targets web engineering. It does not determine legal applicability or replace specialist evaluation of native software, documents, or a conformance claim.

## Authority

| Source | Status checked | What it supports |
| --- | --- | --- |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | W3C Recommendation, 2024-12-12 | Success criteria, levels, definitions, exceptions, and full-page/complete-process conformance requirements. Normative requirements take precedence over this skill's summaries. |
| [WCAG 2.2 Understanding](https://www.w3.org/WAI/WCAG22/Understanding/) and [Techniques](https://www.w3.org/WAI/WCAG22/Techniques/) | Informative implementation material | Interpret criteria and choose suitable techniques; listed techniques are not the only valid implementations. Individual criterion links are beside the checks in CHECKS.md. |
| [ARIA in HTML](https://www.w3.org/TR/html-aria/) | W3C Recommendation, 2026-08-11 | Allowed ARIA usage, native semantics, naming restrictions, and redundant/conflicting attributes. |
| [WAI Page Structure: Page Regions](https://www.w3.org/WAI/tutorials/page-structure/regions/) | Informative tutorial | Choosing and naming regions, nested header/footer context, and navigation landmarks. These techniques are not standalone WCAG requirements. |
| [Accessible Name and Description Computation 1.1](https://www.w3.org/TR/accname-1.1/) | W3C Recommendation, 2018-12-18 | Published naming baseline; distinguish it from the provisional 1.2 algorithm below. |
| [WCAG-EM 2.0](https://www.w3.org/TR/wcag-em-2/) | W3C Group Note, 2026-07-23 | Scoping, sampling, complete processes, evidence, and evaluation reporting. Does not add WCAG requirements or convert a sample into a whole-product conformance claim. |
| [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) | Informative patterns and practices | Widget keyboard/focus behavior. Implement the matching pattern and test support; an APG example is not a production support guarantee. |
| [APG: Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/) and [Keyboard Interface](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/) | Informative guidance | Native-first semantics, responsibility for custom interaction, browser/AT limitations, and composite focus navigation. |
| [Selecting Evaluation Tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/) | WAI evaluation guidance | Tool-assisted testing and the need for human judgment; no automated tool determines full accessibility. |
| [Involving Users in Evaluation](https://www.w3.org/WAI/test-evaluate/involving-users/) | WAI evaluation guidance | User participation complements standards evaluation and can expose overlooked barriers. It does not substitute for systematic criteria checks. |
| [Image Decision Tree](https://www.w3.org/WAI/tutorials/images/decision-tree/) | WAI tutorial | Choose alternatives from the image's contextual purpose. |
| [WAI Tables](https://www.w3.org/WAI/tutorials/tables/) and [Grouping Controls](https://www.w3.org/WAI/tutorials/forms/grouping/) | Informative tutorials | Header/data-cell relationships and shared form questions; choose techniques for the actual structure, not a universal attribute recipe. |
| [ACT: aria-hidden and sequential focus](https://www.w3.org/WAI/standards-guidelines/act/rules/6cfa84/) | Atomic test rule, with applicability and support assumptions | Investigate hidden content retaining keyboard focus; passing this rule does not pass all of 4.1.2. |
| [ACT: Scrollable content and sequential focus](https://www.w3.org/WAI/standards-guidelines/act/rules/0ssw9k/) | Atomic test rule, updated 2023-08-30; rechecked 2026-10-17 | Scroller/descendant focus access under 2.1.1, with decorative-content and equivalent-keyboard-control assumptions. Browser focus support varies; actual keyboard scrolling needs a separate behavioral check. |
| [MDN: overflow accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow#accessibility) | Informative implementation guidance, modified 2026-08-27; rechecked 2026-10-17 | Explains scroll-container focus limitations and a `tabindex` technique. Suggested roles/names require contextual judgment; they are not blanket WCAG requirements. |
| [Shiki: codeToHast API](https://shiki.style/api#codetohast) | Library implementation example; checked 2026-10-17 | Documents generated `pre` markup with `tabindex="0"`. Supports considering a simple focus fallback for code that may overflow; framework output is not a WCAG requirement or a browser-support guarantee. |
| [Form Notifications](https://www.w3.org/WAI/tutorials/forms/notifications/) | WAI tutorial | Error identification, correction paths, associations, and notification choices. |
| [Making Audio and Video Accessible](https://www.w3.org/WAI/media/av/) | WAI practical guidance | Media-type distinctions, alternatives, captions, descriptions, and player accessibility. |
| [COGA: Making Content Usable](https://www.w3.org/TR/coga-usable/) | W3C Working Group Note, 2021-04-29 | Supplemental cognitive and learning accessibility guidance beyond WCAG conformance. |

## Drafts and interpretation boundaries

- [WCAG 3.0](https://www.w3.org/TR/wcag-3.0/) is a Working Draft, dated 2026-09-10 when checked. Do not substitute its provisional model for a WCAG 2.2 evaluation.
- [Accessible Name and Description Computation 1.2](https://www.w3.org/TR/accname-1.2/) is a Working Draft, dated 2026-10-12 when checked. Use it to investigate algorithm details and implementation differences, with its status explicit; inspect actual browser exposure instead of assuming support.
- [HTML Accessibility API Mappings 1.0](https://www.w3.org/TR/html-aam-1.0/) is a Working Draft, dated 2026-10-12 when checked. Use contextual element mappings to investigate browser exposure, not to assert universal implementation or new WCAG requirements.
- WCAG 2.2 removed 4.1.1 Parsing. If a contract names WCAG 2.0/2.1, evaluate and report that version explicitly rather than silently dropping its requirements.
- A/AA/AAA are requirement levels, not severity rankings. A recommendation beyond the target can still materially improve usability; identify it honestly.

## Complementary checklists

[The A11Y Project checklist](https://www.a11yproject.com/checklist/), checked 2026-10-16, supplies practical review prompts, not a complete WCAG 2.2 conformance matrix. It still cites removed 4.1.1 and includes AAA guidance and preferred techniques. Verify the current criterion, level, applicability, and exceptions in W3C sources before adopting a prescription; a single H1, an error summary above every form, and a particular bypass technique are not universal A/AA requirements.

## Updating

Recheck the affected source when a criterion interpretation changes, a W3C Recommendation or methodology is revised, a relevant browser/AT interaction changes, or an evaluation exposes a wrong finding. Check the source's current status, linked errata, and changed definitions before updating a summary; do not promote drafts silently.

Update the date and affected checks together, then rerun a focused case demonstrating the distinction. Use URLs and short paraphrases rather than importing specifications into the skill. Add a reference only when it resolves a recurring decision.

## Review update — 2026-10-16

Rechecked the affected WCAG 2.2 criteria and Understanding guidance for sensory instructions, images of text, page discovery, navigation consistency, language, input purposes, and media alternatives. CHECKS.md now makes their applicability and key exceptions explicit. This improves practical selection; criterion-number coverage does not establish test coverage or conformance.

WCAG-EM 2.0, WCAG 3.0, and AccName 1.2 publication statuses/dates were confirmed. Canonical WCAG-EM and WCAG 3.0 links were normalized; the older aliases still returned the expected documents when checked. ARIA in HTML, the Page Regions tutorial, and HTML-AAM were checked to distinguish authoring rules, informative techniques, and draft mappings. The interface description now names audit work explicitly; it is a display label, not the skill-dispatch description.

A complementary A11Y Project review prompted explicit checks for hidden focus stops, table-header associations, and shared form questions. These were verified against W3C ACT and WAI guidance; the checklist remains a secondary discovery aid rather than the authority for a WCAG failure.

## Review update — 2026-10-17

A site audit's scanner flagged an overflowing code block without an explicit focus target. Chromium 149 supplied native focus; other browsers were not tested, so no browser-specific keyboard failure was established. Rechecked ACT 0ssw9k's applicability, focus expectation, exceptions, and support notes, MDN's overflow guidance, and Shiki's documented focusable `pre` output. CHECKS.md now calls for Tab and arrow-key testing and visible focus, separates observed behavior from untested support, and allows a simple focus fallback for code that may overflow. That tradeoff does not require dynamic overflow tracking or justify tab stops and roles on arbitrary content.
