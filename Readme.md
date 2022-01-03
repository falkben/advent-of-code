# Advent of Code

## 2021

<https://adventofcode.com/2021/>

## Website

### Pages

Index.html located in [site-dist](site-dist/).

Pages for each day are generated

```cmd
python scripts/gen_pages.py
```

### Styles

Get tailwind:

```cmd
npm install
```

Build css and keep updated:

```cmd
npx tailwindcss -i ./site-src/input.css -o ./site-dist/output.css --watch
```

or for publishing:

```cmd
npm run build-css
```

### Local dev

```cmd
python -m http.server -d site-dist
```
