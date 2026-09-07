# Zonge 2027 design review

This branch proposes a new visual direction for the existing Hugo website. It keeps the current website available while the president and team review the redesign.

## Review the experience

- Homepage: a cinematic night-sky opening, oversized “Clarity runs deep” typography, full-width field photography, a documented Newberry Volcano interpretation, a ZT-100B product feature, photographic application links, company history, and the next event.
- Instruments: all 15 existing product destinations, a compact introduction, sticky category filters with shareable links and browser-history support, compact phone product rows, stronger photo framing, specification links, and clear legacy labeling. Product chapters expand on demand and remain fully available without JavaScript.
- Technical pages: a software page organized into four task groups containing all 12 existing programs; a genuine MT model image; a geothermal introduction with the full published Newberry gravity map; concise ZT-100B introductory copy and power options; and navigation within longer pages.
- Shared design: deep navy, a restrained cyan accent, IBM Plex typography, varied photographic and reading surfaces, a grouped instrument menu, current-page indicators, and a consistent footer.
- Application matrices: a consistent suitability scale and keyboard-operable explanations. Underlying ratings and technical explanations are unchanged.
- Visitor paths: direct method shortcuts, concise method introductions and survey inquiry links, plus receiver, sensor, and catalog links alongside the ZT-100B spotlight. These refinements preserve the broader product and application choices while making technical destinations easier to reach.

The homepage uses a lossless WebP of the earliest available night-sky PNG, recovered from `2848272:static/img/carousel/pete-night-sky.png` (1366 × 768). It preserves the image's wider original frame and avoids the previous 1170 × 673 image's lossy compression. The revised desktop composition confines the image to the right portion of the opening, reducing enlargement while retaining the surveyor and landscape. This is the largest source found in repository history; a larger photographic master would still improve sharpness on high-density desktop displays. The earlier compressed asset remains available for existing references.

## Asset and specification sources

- Field panorama: existing `img/methods/ip/ip-transmitter-tent-banner.jpg`, 2560 × 1250. Its general mountain-terrain caption does not identify it as Newberry.
- Newberry: the homepage uses the user-supplied illustrative Line D redraw (1511 × 1041), received on 7 September 2026 and copied unchanged to `img/review/newberry-line-d-supplied.png`. Its caption identifies it as an illustrative redraw, rather than the original published figure. The viewer compares this illustration with original Figure 9 on page 5 of `documents/newberry-volcano-mt-geothermal-exploration.pdf`, Waibel, Beard and Oppliger (2013). The original extracted Figure 9 (772 × 642) remains available as `img/review/newberry-mt-line-d.jpg`. The accompanying interpretation of shallow conductive zones and clay-altered volcanic deposits is supported by the Discussion on page 7. The copy preserves the paper’s uncertainty and does not claim a productive reservoir. The illustration differs from the published figure in scales and contour labels; measurements are explicitly referred to the original. The mountain field photograph is not presented as Newberry.
- NT-20: native product photograph (973 × 750) from `documents/nt20.pdf`, page 1. Page 2 supports size 22 × 32 × 18 cm and weight 5 kg without batteries; no width/height/depth axes are inferred.
- Instrument highlights: existing product technical pages and linked specification sheets. GGT-10B maximum current is intentionally omitted from highlights because its brochure conflicts between 25 A on page 1 and 20 A on page 2. Other detailed technical content remains available for engineering review.
- Product imagery: GGT-10B uses the native 1097 × 823 JPEG extracted unchanged from `documents/ggt10b.pdf`; XMT-R uses the existing 1600 × 1200 original controls photo. TEM-4 uses its genuine individual image, `img/banners/tem-4.jpg`. ANT-4, ANT-6, ANT-7, and ANT-9 use technical profile panels instead of presenting a sensor-family photo as the individual product. The family photo remains in the catalog overview. Uniform studio photography is still unavailable.
- Geothermal: the complete original Figure 3 gravity map (577 × 506), including legend and footer, is retained as `img/review/newberry-gravity-published.jpg`. The 2006 MT survey is attributed to Geosystems and the 2011 MT survey to Zonge.
- Software: existing `img/mt-model-e13664090974923_m.png` (1024 × 657), captioned as an MT resistivity model from the Zonge image library. No project or producing software is inferred. Program descriptions are retained in `data/software_catalog.json`, with file extensions correctly rendered as code.
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

Review and production Hugo builds pass. All 76 generated HTML files were checked for preview indexing settings, duplicate IDs, and internal link/asset references. All 15 product pages retain key facts, an appropriate photograph or technical profile, and current-page navigation. Inline and external enhancement JavaScript syntax checks pass. Review form submission and analytics remain disabled; the production configuration retains the Formspree/Turnstile flow.

### Browser validation — September 7, 2026

- Full phone regression: 332 checks, zero failures, across Chromium widths 320, 375, 390, 412, and 430 px and WebKit widths 375, 390, and 430 px, plus WebKit 844 × 390 landscape. All 50 content pages passed the 320 px overflow and broken-image scan.
- New interactions: 145 checks, zero failures, in Chromium and WebKit at 320, 390, and 1440 px. Covered the image viewer, supplied/published figure switching, Escape and close buttons, focus restoration, category selection, direct category links, browser back, visibility below the sticky bar, product chapter deep links, keyboard disclosures, sensor profiles, individual TEM-4 photo, all 12 software programs, file-extension formatting, and software task links.
- Progressive enhancement: complete catalogs and product documents remain readable with JavaScript disabled in both engines.
- Visual inspection covered the homepage sequence and Newberry figure, catalog, software, geothermal, ZT-100B, ANT-9, TEM-4, and the figure viewer on desktop and phone. The original broader pass also checked application-matrix dialogs and inquiry forms; the full phone regression rechecked navigation, inquiry fields, and review submission safeguards.

This is browser emulation and visual testing; physical-device keyboards, screen-reader behavior, and real cellular performance were not measured.
