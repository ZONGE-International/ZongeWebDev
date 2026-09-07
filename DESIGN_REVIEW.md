# Zonge 2027 design review

This branch proposes a new visual direction for the existing Hugo website. It keeps the current website available while the president and team review the redesign.

## Review the experience

- Homepage: a cinematic night-sky opening, oversized “Clarity runs deep” typography, full-width field photography, a documented Newberry Volcano interpretation, a ZT-100B product feature, photographic application links, company history, and the next event.
- Instruments: all 15 existing product destinations, key specifications on catalog cards and product introductions, distinct sensor descriptions, recovered NT-20 photography and mechanical specifications, specification links, and clear legacy labeling.
- Technical pages: clear instrument photography, compact page introductions, readable text, and navigation within longer pages.
- Shared design: deep navy, a restrained cyan accent, IBM Plex typography, varied photographic and reading surfaces, a grouped instrument menu, current-page indicators, and a consistent footer.
- Application matrices: a consistent suitability scale and keyboard-operable explanations. Underlying ratings and technical explanations are unchanged.
- Visitor paths: direct method shortcuts, concise method introductions and survey inquiry links, plus receiver, sensor, and catalog links alongside the ZT-100B spotlight. These refinements preserve the broader product and application choices while making technical destinations easier to reach.

The homepage uses a lossless WebP of the earliest available night-sky PNG, recovered from `2848272:static/img/carousel/pete-night-sky.png` (1366 × 768). It preserves the image's wider original frame and avoids the previous 1170 × 673 image's lossy compression. The revised desktop composition confines the image to the right portion of the opening, reducing enlargement while retaining the surveyor and landscape. This is the largest source found in repository history; a larger photographic master would still improve sharpness on high-density desktop displays. The earlier compressed asset remains available for existing references.

## Asset and specification sources

- Field panorama: existing `img/methods/ip/ip-transmitter-tent-banner.jpg`, 2560 × 1250. Its general mountain-terrain caption does not identify it as Newberry.
- Newberry: the homepage uses the user-supplied illustrative Line D redraw (1511 × 1041), received on 7 September 2026 and copied unchanged to `img/review/newberry-line-d-supplied.png`. Its caption identifies it as an illustrative redraw, rather than the original published figure. The source-study link remains: page 5 of `documents/newberry-volcano-mt-geothermal-exploration.pdf`, Waibel, Beard and Oppliger (2013). The original extracted Figure 9 (772 × 642) remains available as `img/review/newberry-mt-line-d.jpg`. The copy describes integrated interpretation without claiming a discovery or drilling outcome.
- NT-20: native product photograph (973 × 750) from `documents/nt20.pdf`, page 1. Page 2 supports size 22 × 32 × 18 cm and weight 5 kg without batteries; no width/height/depth axes are inferred.
- Instrument highlights: existing product technical pages and linked specification sheets. GGT-10B maximum current is intentionally omitted from highlights because its brochure conflicts between 25 A on page 1 and 20 A on page 2. Other detailed technical content remains available for engineering review.
- Sensor photographs remain a clearly labelled family image; the available individual brochure composites contain old backgrounds and logos, and no individual ANT-9 photograph was found.
- The original flat Zonge logo is retained at a smaller display size. Neither repository history nor the inspected brochures yielded a verified vector or sharper master. A genuine vector logo and larger night-sky master remain useful future source assets; no artificial upscaling is presented as recovered detail.

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

## Validation of this refinement

Review and production builds pass. All 76 generated HTML files were checked for preview indexing settings, duplicate IDs, and 3,696 internal link/asset references; all 15 product pages have images, key facts, and current-page navigation. Inline JavaScript syntax checks pass. Review form submission and analytics remain disabled; the production configuration retains the Formspree/Turnstile flow. Desktop Chrome inspection covered the homepage sequence, NT-20 page, grouped instrument menu, and Escape-to-close behavior.

### Phone validation — completed September 7, 2026

An isolated Playwright run completed 317 checks with no failures after fixes. Browser-based device emulation covered:

| Engine | Portrait widths | Additional coverage |
| --- | --- | --- |
| Chromium 153 | 320, 375, 390, 412, 430 px | All 50 content pages checked at 320 px for page-level overflow and broken images |
| WebKit 26.6 | 375, 390, 430 px | 844 × 390 landscape, including navigation through the long instrument menu |

Tested menu opening, grouped navigation, same-page category links, automatic menu dismissal, Escape behavior, product navigation, inquiry-context prefill, form entry, readable touch controls, and preview submission safeguards. All three application-matrix explanations were checked in both engines for touch opening, viewport containment, keyboard opening, Escape, tap dismissal, and focus restoration. The CSAMT diagram was verified after scrolling and image decode. Screenshots were inspected for homepage composition, catalog/product facts, sensor labeling, tables, and dialogs.

The phone pass corrected oversized menu rows, small method-link touch areas, unnecessary software-table horizontal scrolling, inconsistent catalog fact widths, and joined words in a responsive heading. It also added a visible sensor-family caption and a mobile scroll hint on intentionally wide comparison matrices.

This is browser emulation and visual testing; physical-device keyboards, screen-reader behavior, and real cellular performance were not measured.
