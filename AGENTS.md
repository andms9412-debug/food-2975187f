# ig-food-template Project SSOT

## Purpose

This repo is the SSOT for the food-note style IG post template/generator.

- Public app: https://andms9412-debug.github.io/food-2975187f/
- GitHub repo: https://github.com/andms9412-debug/food-2975187f
- GitHub Pages source: `master` branch, repo root `/`
- Main files: `index.html` and `ig-food-post.html`

## File Invariants

- Keep `index.html` and `ig-food-post.html` identical unless there is an explicit reason to split them.
- The app is a static single-page HTML tool; do not add a build system or dependency for small fixes.
- Canvas output target is IG portrait 4:5, `1080x1350`.

## Known Font Pitfall

Canvas can draw CJK text before Google Fonts finishes loading all subset glyphs. This causes mixed fallback fonts, for example `艋舺中原鹹酥雞` showing uneven title weights.

Current fix:

- Collect all current canvas text with `getCanvasText()`.
- Load the actual text against `LXGW WenKai TC` via `document.fonts.load()`.
- Route text edits through `scheduleDraw()`.
- Route export through `drawForExport()` before `toDataURL()`.
- Keep title Chinese-first: `ctx.font='700 72px '+HAND`; do not put `Caveat` before Chinese title text.

Regression check:

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/index.html`, set store name to `艋舺中原鹹酥雞`, then confirm title glyphs look consistent and PNG export matches the preview.

## Deploy Checklist

1. Run:

```bash
git diff --check
diff -u index.html ig-food-post.html
```

2. When Codex creates the commit, follow the global Codex commit-attribution rule; do not duplicate a model- or version-specific trailer here.

3. Push:

```bash
git push origin master
```

4. Wait for GitHub Pages status to become `built`:

```bash
gh api repos/andms9412-debug/food-2975187f/pages
```

5. Verify the public HTML contains the expected change:

```bash
curl -sL https://andms9412-debug.github.io/food-2975187f/index.html | rg -n "EXPECTED_SYMBOL_OR_TEXT"
```

## Skillization Candidates

Do not create a project skill just for one-off fixes. Create one after the same workflow repeats or becomes error-prone.

Good candidates:

- Release/deploy helper: run `git diff --check`, confirm `index.html` and `ig-food-post.html` are identical, push `master`, poll GitHub Pages until `built`, then verify the public URL.
- Font regression helper: serve locally, open with Playwright, set store name to `艋舺中原鹹酥雞`, check `document.fonts.check('700 72px "LXGW WenKai TC"', text)`, trigger download, and confirm no console errors except optional favicon 404.
- Template sync helper: fail fast if only one of the two HTML files changed or if their contents diverge.

If skillized, prefer a small repo-local script first, then a Codex skill wrapper only if the workflow becomes useful outside this repo.
