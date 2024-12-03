# Advent of Code

<https://adventofcode.com/>

## Website

### Pages

Index.html located in [site-dist](site-dist/).

Pages for each day are generated

```sh
python scripts/gen_pages.py
```

### Styles

Get tailwind:

```sh
npm install
```

Build css and keep updated:

```sh
npx tailwindcss -i ./site-src/input.css -o ./site-dist/output.css --watch
```

or for publishing:

```sh
npm run build-css
```

### Local dev

```sh
python -m http.server -d site-dist
```
