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
- [`themes/hugo-universal-theme/`](/Users/admin/Documents/PRO/GEOPHYZ/ZONGE/ENGINEER/DEV/ZONGE_WEBSITE/ZongeWebDev/themes/hugo-universal-theme) is the theme dependency tracked as a git submodule.
- [`hugo.toml`](/Users/admin/Documents/PRO/GEOPHYZ/ZONGE/ENGINEER/DEV/ZONGE_WEBSITE/ZongeWebDev/hugo.toml) contains site configuration, menus, params, and base URL settings.
- [`public/`](/Users/admin/Documents/PRO/GEOPHYZ/ZONGE/ENGINEER/DEV/ZONGE_WEBSITE/ZongeWebDev/public) is the generated output directory.

## Prerequisites

Install:

- Hugo Extended `0.160.0` or newer
- Dart Sass
- Git

If you clone the repository fresh, initialize the theme submodule:

```bash
git submodule update --init --recursive
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
2. Checks out the repository and theme submodule
3. Ensures the theme is pinned to the expected commit
4. Builds the site with Hugo
5. Uploads `public/` to GitHub Pages

If you need to trigger a deployment manually, use the `workflow_dispatch` option in the GitHub Actions UI.

## Notes

- This repository does not currently use a Node.js build pipeline.
- The GitHub Pages base URL is configured in `hugo.toml` and overridden in CI during the Pages build step.
- `public/` is generated output and can be rebuilt at any time from source.
