# Choose the document's job

Use the branch that matches the reader's need. Combine small sections when useful; do not scaffold a documentation taxonomy or require these headings.

## README

A root README helps a prospective user or contributor decide what the project does and reach a first useful result. Include prerequisites and a working path when needed, then link to maintained references.

A folder README explains what belongs there and the local editing or usage contract. Prefer the facts that prevent mistakes: naming, publication rules, required metadata, relationships, and local checks. Link to root setup instructions instead of repeating them. Renderer internals belong only when they affect the author's choices.

## API or configuration reference

Organize around the interface engineers consult: operation, parameter, field, event, or setting. Describe types, accepted values, defaults, units, optionality, constraints, precedence, return values, and errors when they are part of that contract.

For example, `timeoutMs: 0` might disable a deadline while an omitted value selects a default. Replacing both with “optional timeout” loses behavior. Do not infer missing semantics from an option's name.

Use examples to resolve ambiguity. Keep procedures and rationale as links or brief context when they are not the reference's main purpose. Generated reference can reduce drift but does not replace undocumented semantics.

## How-to, runbook, or migration

Document the actual start state, relevant version/environment, commands in execution order, meaningful side effects, and a result the reader can check. Explain placeholders and required working directories.

For operational changes, include stop conditions, recovery, or rollback when the operation warrants them. State irreversible consequences before the action. Do not manufacture a rollback for an operation that cannot be reversed.

A migration also identifies compatibility boundaries and what changes for existing callers or data. Avoid documenting every possible failure; cover failures the available evidence shows are relevant to this task.

## Tutorial

Choose a complete learning path with a predictable result. Provide the context and prerequisites a newcomer lacks. Separate optional detours from the path. A tutorial needs more guidance than a reference for experienced users; shortening both identically is a mistake.

## ADR, RFC, or design explanation

An ADR records a decision in its historical context. Preserve status, constraints, alternatives considered, consequences, and the evidence available at that time. A later implementation change may warrant a superseding decision; it does not prove the old rationale was false.

An RFC distinguishes proposed behavior from accepted behavior and identifies the decision still needed. A design explanation connects mechanisms to constraints, tradeoffs, and consequences. Include diagrams only when they clarify a relationship that prose obscures.
