# Semisolve Website

This repository contains the source code for the official landing page of **Semisolve**: [https://semisolve.org/](https://semisolve.org/).

## About the Project
Semisolve is a Python-first simulation framework for III-V Nitride heterostructures. It prioritizes physical transparency and research flexibility. The framework is currently private during a major refactor; an open-source release is planned, with no release date set.

- **Planned Core Repository**: [github.com/semisolve/semisolve](https://github.com/semisolve/semisolve)
- **Planned PyPI Package**: [pypi.org/project/semisolve/](https://pypi.org/project/semisolve/)

## Development
The website is built with vanilla HTML/CSS/JS for maximum performance and compatibility. No build step is required—simply serve the files using any static web server (e.g., Cloudflare Pages, GitHub Pages, or `python -m http.server`).

Shared styles live in `styles/shared.css`, with page-specific styles in `styles/landing.css` and `styles/demo.css`. The demo displays precomputed JSON data; its reference code is collapsed by default because the APIs are being revised.

The landing-page SVG figures are generated from `data/hemt_data.json`. After changing that dataset, regenerate both themes with `python3 scripts/render_preview.py`. This is an asset maintenance command, not a required site build step.

## License
This website is licensed under the [Apache License 2.0](LICENSE).
Copyright &copy; 2026 Takeru Kumabe
