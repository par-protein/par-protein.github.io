# Protein Autoregressive Modeling (PAR) — Website

This repository hosts the static website for the paper “Protein Autoregressive Modeling for Multiscale Structure Generation.”

- Live site: [https://par-protein.github.io](https://par-protein.github.io)
- Purpose: present the PAR method, figures, and interactive content in a single-page site.


## Repository Structure

- `index.html` — main page markup
- `static/css` — styles (Bulma, carousel/slider, Font Awesome, custom styles: `style.css`, `index.css`, `animation_style.css`)
- `static/js` — scripts (Bulma Carousel/Slider, Font Awesome, jQuery, custom scripts: `index.js`, `animation_script.js`, `faster.js`, `lazy.js`)
- `static/img` — figures and assets used across the page

## Editing

- Content: edit sections in [`index.html`](./index.html)
- Styles: adjust CSS in [`static/css`](./static/css)
- Behavior: update JS in [`static/js`](./static/js)
- Images: add/replace figures in [`static/img`](./static/img)

The site uses:
- Bulma CSS, Bulma Carousel/Slider
- Font Awesome
- jQuery
- Custom scripts and styles bundled in `static/`

## Deployment

This site is published via GitHub Pages at https://par-protein.github.io. To update the live site:
- Commit changes to the default branch configured for Pages (commonly `main`).
- Ensure Pages is set to “Deploy from a branch” with the root (`/`) as the site directory.

## Citation

If this site is helpful, please cite the paper: “Protein Autoregressive Modeling for Multiscale Structure Generation.”