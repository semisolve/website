# Repository Instructions

## Communication

* Respond concisely in the user's language. For long procedures, give the overview before the steps.
* Write artifacts in English, except localized site content.

## Site

* Keep the vanilla HTML/CSS/JavaScript architecture; no build step is required. `index.html` is the landing page; `demo.html` uses Plotly and JSON files in `data/`.
* Keep English/Japanese content, light/dark themes, and shared controls consistent across both pages. Preserve the `ss-lang` and `ss-theme` preference keys.
* Preserve responsive layouts, accessibility, and scientific accuracy, including data, formulas, and units.
* For design work, consult `DESIGN.md` if present as a reference within the requested scope.

## Validation

* Verify behavior affected by the change; documentation-only edits need only content review.
* Report what was verified and any checks that could not be completed.

## Git

* Check status and relevant diffs before editing; preserve unrelated changes. Stage only task-related changes and review the staged diff before committing.
* Keep commits atomic. Use Conventional Commits `<type>(<scope>): <why>` with a lowercase type, optional scope, and a reason-focused subject, ideally at most 72 characters. Add a body only when needed to explain why.
* Do not rewrite history unless requested, or commit secrets, machine-specific identifiers, or temporary generated files.
