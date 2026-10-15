---
name: web-accessibility
description: Review or fix accessibility barriers in web pages, components, and user journeys using WCAG 2.2 and observed behavior. Use for accessibility audits, keyboard or screen-reader issues, accessible forms, dialogs, navigation, and reviews of changed UI. Distinguishes tested outcomes from assumptions; does not certify compliance.
---

# Web accessibility

Help people complete the task. Find the barrier, prove it, and make the smallest correction that preserves the intended interaction.

## 1. Bound the review

Use the requested mode: review reports findings; implementation changes the authorized surface. Do not turn a component fix into a whole-site audit.

Identify the pages or diff, affected journeys and states, available source/browser access, and required standard. Use WCAG 2.2 A and AA as the engineering target when none is supplied; state this assumption. Do not infer legal obligations. Native apps, PDFs, and procurement conformance reports need their own evaluation context.

Inspect the existing components and test setup first. Reuse native HTML or a working accessible component before adding ARIA, custom keyboard handlers, dependencies, or scanners. ARIA communicates semantics; it does not supply interaction behavior.

## 2. Match evidence to the question

Read the relevant sections of [CHECKS.md](CHECKS.md) for the actual controls and content. Consult [SOURCES.md](SOURCES.md) when interpreting a criterion, checking an exception, or planning a full audit. These checks are a starting point, not the complete standard.

- Trace source to the rendered behavior, including loading, empty, error, success, disabled, and open states that exist in the affected journey.
- Use the project's available scanner for leads, then verify applicable findings. A clean axe/Lighthouse result covers only the rules and states exercised.
- Exercise keyboard behavior and inspect computed names, roles, states, and reading order. An accessibility-tree snapshot is not evidence of what a real screen reader announced.
- Test the relevant adaptation: text enlargement, reflow, spacing, pointer alternatives, contrast, or motion preferences. A screenshot cannot prove keyboard behavior.
- Use real assistive technology when the outcome depends on its behavior and access permits. Record the browser, OS, and AT versions actually used. When unavailable, keep investigating other checks and name the exact untested interaction.

For a full audit, apply WCAG-EM: define the product boundary, inventory views/technologies/states, select representative and random samples when needed, include complete processes, and evaluate every applicable criterion at the target level. Record omissions. A successful sample does not prove the whole product conforms. Involving people with disabilities can reveal barriers that standards checks miss.

## 3. Decide without inventing certainty

For each in-scope check, distinguish:

- **Pass:** the method established the expected outcome for the named surface and state.
- **Fail:** reproducible evidence establishes an unmet requirement; check its applicability and exceptions first.
- **Not tested:** unavailable, inconclusive, or insufficient evidence; say what would decide it.
- **Not applicable:** the triggering content or condition is absent; give the reason.

These are report labels, not a certification scheme. Mark an unconfirmed suspicion as such. A scanner's incomplete result is not a pass. One passing aspect, such as a nonempty name, does not pass an entire WCAG criterion. Separate WCAG failures from advisory improvements and design preferences.

## 4. Fix and recheck when requested

Correct the underlying interaction or shared component rather than hiding it from assistive technology. Preserve visible labels, functionality, and sensible focus. Do not duplicate behavior already provided by HTML or a component library.

Repeat the failing journey and affected states after the change. Add a focused regression check using existing tooling when it can actually detect the defect; do not add a new test stack or assert that an ARIA attribute exists as proof of usability.

## Output

Lead with findings ordered by blocked tasks and user impact, not criterion level or scanner score. For each: location/state, reproduction and observed barrier, applicable criterion and source, smallest correction, and verification status. Group repeated defects by shared cause.

State scope, methods/environments used, and material untested areas once. For a component review, group findings with the same correction; omit routine passes and inapplicable checks unless coverage was requested. Avoid repeating evidence limits in every paragraph. Include a coverage matrix only when the audit warrants it. Never turn a score, source review, simulated AT, or sampled review into a claim of WCAG or legal compliance.
