# Zonge 2027 design review

This branch proposes a new visual direction for the existing Hugo website. It keeps the current website available while the president and team review the redesign.

## Review the experience

- Homepage: a fixed opening message, the existing night-sky hero image, service and instrument paths, a ZT-100B spotlight, applications, company background, and the next event.
- Instruments: a visual catalog with all 15 existing product destinations, specification links, and clear legacy labeling.
- Technical pages: clear instrument photography, compact page introductions, readable text, and navigation within longer pages.
- Shared design: restrained navy and blue, IBM Plex typography, lighter content surfaces, simpler figures and tables, and a consistent navigation and footer.
- Application matrices: a consistent suitability scale and keyboard-operable explanations. Underlying ratings and technical explanations are unchanged.

The homepage uses a lossless WebP of the earliest available night-sky PNG, recovered from `2848272:static/img/carousel/pete-night-sky.png` (1366 × 768). It preserves the photograph's wider original frame and avoids the previous 1170 × 673 image's lossy compression. This is the largest source found in repository history; a larger photographic master would still improve sharpness on high-density desktop displays. The earlier compressed asset remains available for existing references.

Existing routes, downloadable documents, company history, audio, contact destinations, and technical content remain available. Heading levels and a spelling error were corrected as part of presentation cleanup.

## Approval questions

1. Does the design communicate Zonge's engineering quality and field experience?
2. Is the balance between geophysical services and instrumentation right?
3. Is the lighter reading layout preferable for the technical pages?
4. Are the photographs and homepage wording appropriate for the brand?

## Preview configuration

Run `hugo server --environment review` for the review environment. It excludes the preview from search indexing, disables analytics, and disables contact-form submission. The pages display without a review banner. `bash scripts/build-review.sh` builds the separate GitHub Pages preview into `dist/`.

The normal production configuration keeps the contact form and analytics behavior. The production GitHub Pages workflow is restricted to `main`, including manual runs. This branch has not been merged into `main` or deployed to zonge.com.

The shareable review is hosted separately at https://zonge-international.github.io/zonge-design-review-2027/. The generated preview repository is separate from the production repository. The review branch and draft pull request remain the source of truth for approval.
