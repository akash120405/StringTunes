# StringTunes

A static replica of the StringTune showcase, hosted from this repository on GitHub Pages.

**Original design, artwork, animations, fonts, and branding: [Fiddle.Digital](https://fiddle.digital).** Reference: https://string-tune.fiddle.digital/. This is an unofficial replica and retains the original credits. No new ownership or license over the original assets is claimed.

## Hosting

In repository **Settings → Pages**, choose **GitHub Actions** as the build source. The `Deploy StringTunes to GitHub Pages` workflow publishes on pushes to `main` and can be run manually.

Expected URL: https://akash120405.github.io/StringTunes/

## Contents

The published HTML, CSS, JavaScript modules, fonts, graphics, 3D models, and most videos are stored in the repository. Three large tutorial videos are fetched during deployment and checked against pinned SHA-256 hashes in `deployment-assets.json`; the deployed site serves them locally. No package installation is required. Asset URLs and Nuxt's application base are adapted to `/StringTunes/`.

Original third-party analytics configuration is disabled. Search indexing is disabled for this unofficial replica. External community, package, and studio links retain their original destinations. Some documentation features may depend on the original service.

The source is the site's compiled public build, rather than its private editable Vue components. Original third-party assets remain subject to their respective terms.
