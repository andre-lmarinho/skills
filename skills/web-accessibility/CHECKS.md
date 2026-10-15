# Checks by surface

Read only the sections relevant to the task. Criterion numbers refer to WCAG 2.2. For a full audit, use the complete target-level criteria from [the standard](https://www.w3.org/TR/WCAG22/), not just this selection. A test must cover the actual outcome and applicable exceptions before it supports a pass.

## Keyboard and navigation

Complete the relevant task with Tab/Shift+Tab and the controls' expected activation/navigation keys. Include opening, operating, dismissing, and returning from overlays. Check meaningful focus order, visible focus, and bypassing repeated blocks. A skip link is one bypass technique, not the only valid solution.

Keyboard access applies to functionality, not necessarily a one-to-one keyboard equivalent for every visible pointer control. Prefer familiar platform behavior; assess any path-dependent-input exception against the underlying function. For composite widgets, use the matching [APG pattern](https://www.w3.org/WAI/ARIA/apg/patterns/) rather than putting every item in the page tab sequence.

Criteria: [2.1.1 Keyboard](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html), 2.1.2 No Keyboard Trap, 2.4.1 Bypass Blocks, 2.4.3 Focus Order, 2.4.7 Focus Visible. Check 2.1.4 when single-character shortcuts exist.

## Names, structure, and non-text content

Inspect computed names, roles, values, relationships, and states in the rendered accessibility tree, including changes after interaction. Meaningful visible labels should be represented in accessible names; `aria-label` can override useful visible text. Prefer existing visible text over a second, drifting label.

Check headings, reading sequence, lists, landmarks, tables when present, link purpose in context, page titles, and language. Do not invent a WCAG rule requiring exactly one H1 or an ARIA label on every element. For images, decide their purpose: decorative images may have empty alternatives; informative images need equivalent information; functional images need the action/destination. Complex charts may need a nearby explanation or data, not an enormous alt string.

Criteria: [1.1.1 Non-text Content](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html), [1.3.1 Info and Relationships](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html), 1.3.2 Meaningful Sequence, 2.4.2 Page Titled, 2.4.4 Link Purpose (In Context), 2.4.6 Headings and Labels, [2.5.3 Label in Name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html), 3.1.1/3.1.2 Language, 4.1.2 Name, Role, Value.

## Focus and overlays

Open the actual dialog/popover and inspect initial focus, navigation, background interactivity, dismissal, and the logical focus destination afterward. Use native modal dialog behavior or the existing library where it meets the interaction; do not add a second focus trap. Follow the [modal dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) as implementation guidance, not as a separate WCAG conformance rule.

At AA, author-created content must not entirely hide the component receiving keyboard focus (2.4.11). Full visibility is the enhanced AAA criterion (2.4.12). Test sticky headers, banners, and overlays at enlarged/narrow layouts. If hover/focus reveals content, check dismissal, pointer access to that content, and persistence under 1.4.13, including its exceptions.

Criteria: 2.1.2, 2.4.3, 2.4.7, [2.4.11 Focus Not Obscured (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html), 4.1.2; [1.4.13 Content on Hover or Focus](https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html) when applicable.

## Enlargement, reflow, and spacing

Test text enlargement to 200% without lost content/functionality. Separately test vertically scrolling content at 320 CSS px width, or horizontally scrolling content at 256 CSS px height. For example, a 1280 CSS px viewport at 400% zoom approximates the width condition. Device emulation alone does not demonstrate text enlargement.

Check text spacing overrides together: line height 1.5 times font size, paragraph spacing 2 times, letter spacing 0.12em, and word spacing 0.16em. These are user-override tolerances, not mandatory default typography. Apply language/script provisions.

Inspect clipped labels, fixed-height controls, sticky UI, and orientation restrictions. Essential two-dimensional content has a reflow exception; that does not exempt surrounding prose. Do not build support for absent tables or hypothetical widgets.

Criteria: 1.3.4 Orientation, 1.4.4 Resize Text, [1.4.10 Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html), [1.4.12 Text Spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html).

## Color and visual states

Measure rendered foreground/background pairs, including transparency, images/gradients, themes, and affected control/focus states. Normal text needs 4.5:1; large text needs 3:1. Large means at least 18pt (24 CSS px), or 14pt bold (about 18.67 CSS px), not 18px/14px. Apply the criterion's exceptions, including incidental text and logos.

Necessary visual information identifying controls/states and meaningful graphics generally needs 3:1 against adjacent colors under 1.4.11; assess its scope and exceptions. Do not assume an inherited text color proves focus contrast. Information must not depend on color alone. Check forced-colors behavior where custom styling could hide controls or state; do not disable adaptation globally to preserve branding.

Criteria: 1.4.1 Use of Color, [1.4.3 Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [1.4.11 Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).

## Pointer targets, gestures, and dragging

Measure targets in CSS pixels. AA 2.5.8 uses 24 by 24 CSS px with spacing, equivalent-control, inline, user-agent, and essential exceptions. Test the exact spacing exception; a 44px minimum everywhere is not the AA rule.

Check alternatives to multipoint/path gestures and dragging. Keyboard support does not by itself satisfy 2.5.7's single-pointer alternative to dragging; use clicks/taps or equivalent controls where applicable. Also examine accidental activation/cancellation and device-motion actions when present.

Criteria: 2.5.1 Pointer Gestures, 2.5.2 Pointer Cancellation, 2.5.4 Motion Actuation, [2.5.7 Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html), [2.5.8 Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html).

## Forms, errors, and authentication

Complete the flow with missing, malformed, valid, and rejected input. Check persistent visible labels/instructions, programmatic relationships, input purpose where applicable, error identification and correction, and preservation of entered data. An alert on every field or automatic focus movement is not a universal solution. For consequential submissions, evaluate review, correction, or reversal under 3.3.4.

Inspect all authentication steps, including OTP and recovery. Permit password-manager/autofill and copy-paste assistance; check whether a cognitive test has a qualifying mechanism, alternative, or exception before declaring failure. Split OTP inputs must accept assisted entry effectively, not just the first character. Avoid redundant entry within the same process unless an exception applies. Check changes of context on focus/input and repeated help placement.

Criteria: 1.3.5 Identify Input Purpose, 3.2.1/3.2.2, 3.2.6 Consistent Help, 3.3.1/3.3.2/3.3.3, 3.3.4, 3.3.7 Redundant Entry, [3.3.8 Accessible Authentication (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html), 4.1.2. See [WAI form notifications](https://www.w3.org/WAI/tutorials/forms/notifications/).

## Dynamic feedback and assistive technology

Trigger updates, validation, loading, empty/success states, and navigation. Determine which changes are status messages and whether users can discover them without unnecessary focus moves. Use polite status announcements for routine feedback; reserve assertive alerts for appropriate urgency. Do not announce every DOM change or duplicate the same message.

The accessibility tree helps inspect programmatic exposure; it cannot prove timing, interruption, duplication, or actual speech. When those outcomes matter, test a real browser/AT combination with the relevant navigation mode. Record unavailable AT checks as not tested, even if a virtual reader or role assertion passes.

Criteria: [4.1.3 Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html), 4.1.2, and 2.4.3 when focus changes.

## Time, motion, and media

Inspect timeouts, autoplay, moving/updating content, flashing, and embedded media only when present. Check timing-adjustment and pause/stop/hide requirements with their duration and essential-function exceptions. Do not trigger potentially unsafe flashing to prove a failure.

For media, distinguish captions, transcripts, and audio description; a transcript alone does not replace synchronized captions or required audio description. Test availability, accuracy, and player operation. Check 1.4.2 when audio starts automatically.

Reduced-motion support is useful; animation from interactions is 2.3.3 at AAA, not an automatic AA failure. Other applicable A/AA motion, timing, or flash requirements still apply. Do not use a global near-zero-duration override that breaks state changes or events without testing the behavior.

Criteria: applicable 1.2.1–1.2.5, 1.4.2 Audio Control, 2.2.1 Timing Adjustable, [2.2.2 Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html), 2.3.1 Three Flashes or Below Threshold. [2.3.3 Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html) is advisory when the target is AA.

For barriers involving confusing language, memory load, or unfamiliar interactions beyond a specific criterion, consult [COGA guidance](https://www.w3.org/TR/coga-usable/). Label these as usability/accessibility recommendations rather than inventing a WCAG failure.
