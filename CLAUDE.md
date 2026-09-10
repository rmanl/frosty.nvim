# CLAUDE.md

## Project

frosty.nvim — a neovim colorscheme. `extra/base16/<theme>.yaml` is the source of
truth for a theme's name and palette; every other file for that theme is keyed
off `<theme>` from the yaml filename.

## Keeping themes and extras in sync

Themes (`extra/base16/<theme>.yaml`, one per theme) and extras (the tool subdirs
below, plus nvim) form a matrix: every theme should have a file in every extra.
Whenever that matrix gets a new row or column, fill in the rest of it:

- **New theme** (a new `extra/base16/<theme>.yaml` appears): create a matching
  `<theme>` file in every extra listed below, for that new theme, and add
  `<theme>` to the `-- Can be one of: ...` list documenting the `theme` option
  in `README.md`, keeping that list alphabetically sorted.
- **New extra** (a file for a new tool appears under only one theme, e.g.
  `extra/<tool>/<theme>.ext` shows up but `extra/<tool>/` didn't exist before):
  create the matching `<tool>` file for every *other* existing theme, derived
  from each of those themes' palettes.

Nvim:

- `lua/frosty/palette/<theme>.lua` (the `frosty.Theme` table), `colors/<theme>.lua`
  and `colors/<theme>-alt.lua` (the `:colorscheme` entry points, alt = `alt_bg = true`),
  and register `<theme>` in `lua/frosty/palette/init.lua`'s `M.themes`

Extras:

- `extra/bat/<theme>.tmTheme`
- `extra/btop/<theme>.theme`
- `extra/claude/<theme>.json`
- `extra/foot/<theme>.ini`
- `extra/fuzzel/<theme>.ini`
- `extra/fzf/<theme>.zsh`
- `extra/gtk/<theme>.css`
- `extra/mako/<theme>.ini`
- `extra/spotify/<theme>.ini`
- `extra/zathura/<theme>.zathurarc`

In either case, use the other themes' existing files in that same location as
the template — same keys/structure, colors swapped for the relevant theme's
palette (`extra/base16/<theme>.yaml` is the palette to pull from).

Finally, regenerate the palette image:

```
nix shell nixpkgs#librsvg --command python3 palette/gen_palette.py
```

This reads every `extra/base16/*.yaml` and rewrites `palette/palette.png`, which
is embedded in `README.md` under `## Palette`. Regenerate it any time an
`extra/base16/*.yaml` file is added or edited, and commit the updated PNG
alongside the rest of the theme's files.

## Committing changes

After filling in the matrix for a new theme or extra, or updating an
existing theme's palette, show the `git status` / `git diff --stat` of
what will be committed, then commit automatically (no need to ask first).
Do not push — always confirm with the user before pushing.

If a single request adds multiple new extras/tools (or multiple new themes),
make **one commit covering all of them**, not one commit per tool/theme.
Only split into separate commits when the user asks for unrelated changes
in the same session.

Commit message conventions:

- New theme: `theme: add <theme>` (multiple themes in one request: `theme: add <theme1>, <theme2>`)
- New extra/tool (rolled out to all themes): `feat: add <tool>` (multiple tools in one request: `feat: add <tool1>, <tool2>`)
- Palette edit to an existing theme: `fix: update colors for <theme>`
  - For small, targeted tweaks, add a body listing the changed keys, e.g.:
    ```
    fix: update colors for nord

    - bg: #2e3440 -> #242933
    - accent: #88c0d0 -> #8fbcbb
    ```
  - For sweeping palette rewrites, skip the itemized body — `git diff`
    already documents it.
