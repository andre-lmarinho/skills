# Sources and maintenance

Checked: 2026-10-15. The skill targets web engineering. It does not determine legal applicability or replace specialist evaluation of native software, documents, or a conformance claim.

## Authority

| Source | Status checked | What it supports |
| --- | --- | --- |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | W3C Recommendation, 2024-12-12 | Success criteria, levels, definitions, exceptions, and full-page/complete-process conformance requirements. Normative requirements take precedence over this skill's summaries. |
| [WCAG 2.2 Understanding](https://www.w3.org/WAI/WCAG22/Understanding/) and [Techniques](https://www.w3.org/WAI/WCAG22/Techniques/) | Informative implementation material | Interpret criteria and choose suitable techniques; listed techniques are not the only valid implementations. Individual criterion links are beside the checks in CHECKS.md. |
| [ARIA in HTML](https://www.w3.org/TR/html-aria/) | W3C Recommendation, 2026-08-11 | Allowed ARIA usage, native semantics, naming restrictions, and redundant/conflicting attributes. |
| [WCAG-EM 2.0](https://www.w3.org/TR/WCAG-EM/) | W3C Group Note, 2026-07-23 | Scoping, sampling, complete processes, evidence, and evaluation reporting. Does not add WCAG requirements or convert a sample into a whole-product conformance claim. |
| [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) | Informative patterns and practices | Widget keyboard/focus behavior. Implement the matching pattern and test support; an APG example is not a production support guarantee. |
| [APG: Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/) and [Keyboard Interface](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/) | Informative guidance | Native-first semantics, responsibility for custom interaction, browser/AT limitations, and composite focus navigation. |
| [Selecting Evaluation Tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/) | WAI evaluation guidance | Tool-assisted testing and the need for human judgment; no automated tool determines full accessibility. |
| [Involving Users in Evaluation](https://www.w3.org/WAI/test-evaluate/involving-users/) | WAI evaluation guidance | User participation complements standards evaluation and can expose overlooked barriers. It does not substitute for systematic criteria checks. |
| [Image Decision Tree](https://www.w3.org/WAI/tutorials/images/decision-tree/) | WAI tutorial | Choose alternatives from the image's contextual purpose. |
| [Form Notifications](https://www.w3.org/WAI/tutorials/forms/notifications/) | WAI tutorial | Error identification, correction paths, associations, and notification choices. |
| [Making Audio and Video Accessible](https://www.w3.org/WAI/media/av/) | WAI practical guidance | Media-type distinctions, alternatives, captions, descriptions, and player accessibility. |
| [COGA: Making Content Usable](https://www.w3.org/TR/coga-usable/) | W3C Working Group Note, 2021-04-29 | Supplemental cognitive and learning accessibility guidance beyond WCAG conformance. |

## Drafts and interpretation boundaries

- [WCAG 3.0](https://www.w3.org/TR/wcag3/) is a Working Draft, dated 2026-09-10 when checked. Do not substitute its provisional model for a WCAG 2.2 evaluation.
- [Accessible Name and Description Computation 1.2](https://www.w3.org/TR/accname-1.2/) is a Working Draft, dated 2026-10-12 when checked. Use it to investigate algorithm details and implementation differences, with its status explicit; inspect actual browser exposure instead of assuming support.
- WCAG 2.2 removed 4.1.1 Parsing. If a contract names WCAG 2.0/2.1, evaluate and report that version explicitly rather than silently dropping its requirements.
- A/AA/AAA are requirement levels, not severity rankings. A recommendation beyond the target can still materially improve usability; identify it honestly.

## Updating

Recheck the affected source when a criterion interpretation changes, a W3C Recommendation or methodology is revised, a relevant browser/AT interaction changes, or an evaluation exposes a wrong finding. Check the source's current status, linked errata, and changed definitions before updating a summary; do not promote drafts silently.

Update the date and affected checks together, then rerun a focused case demonstrating the distinction. Use URLs and short paraphrases rather than importing specifications into the skill. Add a reference only when it resolves a recurring decision.
