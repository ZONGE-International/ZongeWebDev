# Zonge Website

This repository contains the Hugo source for the Zonge International website.

The site is built with:

- [Hugo Extended](https://gohugo.io/)
- the [`hugo-universal-theme`](https://github.com/devcows/hugo-universal-theme) theme
- repository-managed content, data files, layouts, and static assets

The production site is deployed through GitHub Pages from the workflow in [.github/workflows/hugo.yml](/Users/admin/Documents/PRO/GEOPHYZ/ZONGE/ENGINEER/DEV/ZONGE_WEBSITE/ZongeWebDev/.github/workflows/hugo.yml).

## Project structure

- [`content/`](/Users/admin/Documents/PRO/GEOPHYZ/ZONGE/ENGINEER/DEV/ZONGE_WEBSITE/ZongeWebDev/content) contains site pages and section content in Markdown.
- [`layouts/`](/Users/admin/Documents/PRO/GEOPHYZ/ZONGE/ENGINEER/DEV/ZONGE_WEBSITE/ZongeWebDev/layouts) contains template overrides, partials, and shortcodes.
- [`data/`](/Users/admin/Documents/PRO/GEOPHYZ/ZONGE/ENGINEER/DEV/ZONGE_WEBSITE/ZongeWebDev/data) contains structured YAML data used by carousels, testimonials, target tables, and other reusable content.
- [`static/`](/Users/admin/Documents/PRO/GEOPHYZ/ZONGE/ENGINEER/DEV/ZONGE_WEBSITE/ZongeWebDev/static) contains images, downloadable documents, CSS, and other public assets.
- [`themes/hugo-universal-theme/`](/Users/admin/Documents/PRO/GEOPHYZ/ZONGE/ENGINEER/DEV/ZONGE_WEBSITE/ZongeWebDev/themes/hugo-universal-theme) is the ignored local theme checkout. CI fetches the pinned revision declared in the deployment workflow.
- [`hugo.toml`](/Users/admin/Documents/PRO/GEOPHYZ/ZONGE/ENGINEER/DEV/ZONGE_WEBSITE/ZongeWebDev/hugo.toml) contains site configuration, menus, params, and base URL settings.
- [`public/`](/Users/admin/Documents/PRO/GEOPHYZ/ZONGE/ENGINEER/DEV/ZONGE_WEBSITE/ZongeWebDev/public) is the generated output directory.

## Prerequisites

Install:

- Hugo Extended `0.168.0` (the version pinned in CI)
- Dart Sass
- Git

If you clone the repository fresh, create the local theme checkout at the same pinned revision used by CI:

```bash
git clone https://github.com/devcows/hugo-universal-theme.git themes/hugo-universal-theme
git -C themes/hugo-universal-theme checkout d3000904ec2dfe7cae2a2d09320444cfccd3f5fc
```

## Local development

Run the site locally with:

```bash
hugo server --disableFastRender
```

By default Hugo serves the site at `http://localhost:1313/`.

Useful commands:

```bash
hugo
```

Builds the production output into `public/`.

```bash
hugo server -D
```

Serves draft content locally if drafts are added in the future.

## Content editing notes

- Add or update pages in `content/`.
- Update menus, global settings, and site metadata in `hugo.toml`.
- Update reusable homepage and target-table content in `data/`.
- Update custom UI behavior and styling in `layouts/` and `static/css/custom.css`.
- Keep downloadable PDFs and packaged files in `static/documents/`.

The target comparison popups are implemented as shortcode templates:

- [`layouts/shortcodes/mining.html`](/Users/admin/Documents/PRO/GEOPHYZ/ZONGE/ENGINEER/DEV/ZONGE_WEBSITE/ZongeWebDev/layouts/shortcodes/mining.html)
- [`layouts/shortcodes/geothermal.html`](/Users/admin/Documents/PRO/GEOPHYZ/ZONGE/ENGINEER/DEV/ZONGE_WEBSITE/ZongeWebDev/layouts/shortcodes/geothermal.html)
- [`layouts/shortcodes/groundwater.html`](/Users/admin/Documents/PRO/GEOPHYZ/ZONGE/ENGINEER/DEV/ZONGE_WEBSITE/ZongeWebDev/layouts/shortcodes/groundwater.html)

Their supporting explanation text lives in:

- [`data/mining/messageMINING.yaml`](/Users/admin/Documents/PRO/GEOPHYZ/ZONGE/ENGINEER/DEV/ZONGE_WEBSITE/ZongeWebDev/data/mining/messageMINING.yaml)
- [`data/mining/messageGEOTHERMAL.yaml`](/Users/admin/Documents/PRO/GEOPHYZ/ZONGE/ENGINEER/DEV/ZONGE_WEBSITE/ZongeWebDev/data/mining/messageGEOTHERMAL.yaml)
- [`data/mining/messageGROUNDWATER.yaml`](/Users/admin/Documents/PRO/GEOPHYZ/ZONGE/ENGINEER/DEV/ZONGE_WEBSITE/ZongeWebDev/data/mining/messageGROUNDWATER.yaml)

## Deployment

Deployment is handled by GitHub Actions on pushes to `main`.

The workflow:

1. Installs Hugo Extended and Dart Sass
2. Checks out the repository
3. Ensures the theme is pinned to the expected commit
4. Builds the site with Hugo
5. Uploads `public/` to GitHub Pages

If you need to trigger a deployment manually, use the `workflow_dispatch` option in the GitHub Actions UI.

## Notes

- Preserve the legacy `/gdp3224/` and `/legacy/Contacts.html` aliases when editing their destination pages. Hugo emits HTML redirects with canonical tags; these are not server-side HTTP 301 responses on GitHub Pages.

## 404 responses and legacy redirects

The generated `404.html` keeps `noindex,follow`. GitHub Pages serves it with a real HTTP 404 for unmapped paths. The main GA4 property (`G-B7SVCQZ8GK`) is omitted from that page entirely; valid pages retain the normal Hugo analytics tag. Global Hugo links use root-relative paths so assets and navigation work when the 404 HTML is served at any URL depth.

404 diagnostics are off by default. To use them, set `params.analytics404ID` in `hugo.toml` to a **different, dedicated GA4 measurement ID**. The template rejects the main property's ID. The dedicated tag sends a custom `404_view` event with the requested path; GA4 may also generate its usual session events in that separate property. Do not configure the main property as the diagnostics property.

`redirects/legacy.csv` is the source-of-truth map of individually identified old URLs. It covers all 59 URLs in the two affected families in the legacy site's page sitemap as of 18 October 2026. A current page is used where it covers the same method or section; otherwise the destination is the identical path on `legacy.zonge.com`. Unknown paths are deliberately absent from the map and remain HTTP 404. All 59 configured destinations returned direct HTTP 200 responses in the live verifier. Recheck before activation because legacy content can change; unsitemapped paths need separate review before adding.

This repository deploys directly to GitHub Pages. Live DNS on 18 October 2026 showed PairNIC nameservers and `www.zonge.com` pointing to `zonge-international.github.io`; an unknown URL returned `server: GitHub.com` and HTTP 404. No HTTP redirect edge is evident or configured in this repository. **The CSV is not deployed as HTTP 301s by GitHub Pages.** An operator must put an HTTP edge redirect service in front of `www.zonge.com`, then import the mapped paths. The exporter generates a headerless [Cloudflare Bulk Redirects CSV](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/csv-file-format/) or a [Netlify `_redirects` file](https://docs.netlify.com/manage/routing/redirects/overview/). Preserve exact path matching and status 301; activate the rules before the GitHub Pages origin. Do not create a catch-all prefix rule. The existing Hugo aliases are HTML pages and are not 301s. No country-based traffic block is involved.

Validation from a network-enabled machine:

```sh
hugo --environment production --minify --baseURL https://www.zonge.com/
python3 -m unittest discover -s tests -v
python3 scripts/export_edge_redirects.py cloudflare > /tmp/zonge-cloudflare.csv
python3 scripts/export_edge_redirects.py netlify > /tmp/zonge-_redirects
python3 scripts/verify_redirects_live.py              # before edge activation: destinations return direct 200
python3 scripts/verify_redirects_live.py --sources    # after edge activation: one 301, then direct 200
dig +short NS zonge.com
dig +short www.zonge.com CNAME
curl -sSI https://www.zonge.com/
curl -sSI https://www.zonge.com/contact/
curl -sSI https://www.zonge.com/missing/a/b/random-no-such-page/
curl -sS https://www.zonge.com/missing/a/b/random-no-such-page/ | grep -E 'noindex,follow|G-B7SVCQZ8GK|href="/contact/"|href="/"'
curl -sSI https://www.zonge.com/geophysical-methods/electrical-em/tem/
curl -sSI https://www.zonge.com/robots.txt
curl -sSI https://www.zonge.com/sitemap.xml
```

For the missing URL, expect HTTP 404, `noindex,follow`, root-relative links, and **no** `G-B7SVCQZ8GK` match. The old TEM URL should produce one HTTP 301 to `/methods/groundmethods/tem/` only after edge rules are installed. The live verifier checks every mapped URL and fails on a chain or loop. Review the DNS/edge account before importing rules; nameservers alone do not prove that HTTP traffic is proxied through an edge service.
- `static/documents/zmg30.pdf` and `static/documents/ZMG-9.pdf` preserve previously crawled download URLs. Both are copies of `power.pdf`, which includes specifications for ZMG-30DLE and ZMG-9A. Keep these compatibility copies synchronized if that document changes; current page links should use `/documents/power.pdf`.
- This repository does not currently use a Node.js build pipeline.
- The GitHub Pages base URL is configured in `hugo.toml` and overridden in CI during the Pages build step.
- `public/` is generated output and can be rebuilt at any time from source.
