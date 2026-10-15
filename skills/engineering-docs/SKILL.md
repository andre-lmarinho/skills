---
name: engineering-docs
description: Write, shorten, or review engineering documentation and technical READMEs, including folder guides, API/configuration reference, ADRs, RFCs, runbooks, and migration guides. Use when the reader needs to operate software, consult a contract, or understand a technical decision. Applies to engineering documentation rather than marketing, personal profiles, or stylistic humanization.
---

# Engineering docs

Optimize for the engineer's next action or decision. Brevity is useful only when the reader still has the information needed to act correctly.

## Establish the job

Read the requested document, nearby conventions, and the relevant implementation or specification. Infer the reader and purpose from this context; ask only when missing information would materially change the result.

Decide what the reader needs to do, look up, learn, or understand. Keep sections that serve that need. When the purpose or structure is unclear, consult [DOCUMENT-TYPES.md](DOCUMENT-TYPES.md); its branches are choices, not a template to fill.

Stay within the requested files and audience. A folder README does not automatically need the root project's installation guide, deployment internals, or every renderer detail.

## Ground the content

- Verify names, paths, commands, options, defaults, and behavior against available code, configuration, tests, or versioned specifications. Existing prose is a claim to check, not independent proof.
- If the intended contract and implementation disagree, surface the discrepancy. Do not silently document a suspected bug as the intended behavior or change code to make the prose true.
- Preserve the distinction between observed, specified, proposed, and unknown behavior. Current code cannot establish the historical motivation for a decision.
- Private context can guide editorial decisions; it does not authorize new public claims about the author, product, or team.

## Write or revise

Lead with the information the reader came for. State a condition before the action it changes. Use the project's exact terms and the document's language; explain unfamiliar concepts only when this audience needs them.

Cut scope before polishing sentences. Remove repeated explanations, announced intentions, ornamental claims, and sections with no useful content. Reference a maintained source instead of copying it. Do not create a new document merely to retain everything removed from this one.

Preserve contracts while shortening: required inputs, defaults, units, precedence, limits, compatibility, error behavior, and side effects where relevant. Distinctions such as omitted versus zero, asynchronous acceptance versus completion, or optional versus required must survive.

Use headings for navigation, steps for ordered work, and tables for actual comparisons or reference data. Do not impose a word count, section checklist, sentence rhythm, or punctuation quota. Leave text that already works alone.

For examples, use the smallest valid case that teaches the behavior. Label placeholders and omissions, follow the repository's code conventions, and distinguish illustrative output from observed output. Never invent commands, results, benchmarks, or guarantees to complete a narrative.

## Verify the result

Check the revised document against its sources and the requested scope. Check links, paths, snippets, and rendered Markdown when relevant. For a procedure, confirm the reader can identify where to start and how to recognize success.

Run the smallest safe, relevant check available within the task's authorization. A documentation request does not authorize destructive commands, production changes, paid operations, or contacting others merely to validate an example. Report what could not be verified instead of claiming it passed.

Accuracy, required warnings, and essential limitations take precedence over a shorter diff. Do not broaden this into an unrelated code refactor or rewrite historical records to match today's implementation.

## Deliver

For a writing task, deliver the requested artifact and a brief note only for material changes or unresolved facts. For an audit, give concrete findings with location, evidence, reader consequence, and the smallest correction; distinguish errors from editorial preferences.

For disputed recommendations or source updates, consult [SOURCES.md](SOURCES.md). Project conventions and the reader's task take precedence over a publisher's house style.
