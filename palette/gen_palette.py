#!/usr/bin/env python3
"""Regenerates palette/palette.png from the base16 yaml files in extra/base16/.

Usage:
    python3 palette/gen_palette.py

Requires rsvg-convert (e.g. `nix shell nixpkgs#librsvg`) on PATH.
"""
import os
import re
import subprocess
import tempfile

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE16_DIR = os.path.join(REPO_ROOT, "extra", "base16")
OUT_PNG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "palette.png")

SLOT_ORDER = [
    "base00", "base01", "base02", "base03",
    "base04", "base05", "base06", "base07",
    "base08", "base09", "base0A", "base0B",
    "base0C", "base0D", "base0E", "base0F",
    "diffRed", "diffGreen",
]

SLOT_ROLE = {
    "base00": "bg", "base01": "bg1", "base02": "sel", "base03": "cmnt",
    "base04": "fg1", "base05": "fg", "base06": "fg2", "base07": "bg2",
    "base08": "var", "base09": "int", "base0A": "cls", "base0B": "str",
    "base0C": "sup", "base0D": "fn", "base0E": "kw", "base0F": "dep",
    "diffRed": "diff-", "diffGreen": "diff+",
}

SWATCH_W = 90
SWATCH_H = 90
LABEL_H = 36
ROW_TITLE_H = 40
PADDING = 24
GAP = 6
SWATCHES_PER_ROW = 9


def parse_yaml(path):
    data = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            m = re.match(r'^([A-Za-z0-9]+):\s*"?([^"]*)"?$', line)
            if not m:
                continue
            key, val = m.group(1), m.group(2)
            data[key] = val
    return data


def luminance(hexcolor):
    hexcolor = hexcolor.lstrip("#")
    r, g, b = (int(hexcolor[i:i + 2], 16) / 255.0 for i in (0, 2, 4))

    def lin(c):
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = lin(r), lin(g), lin(b)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def text_color(bg_hex):
    return "#111111" if luminance(bg_hex) > 0.35 else "#eeeeee"


def load_themes():
    themes = []
    for fname in sorted(os.listdir(BASE16_DIR)):
        if not fname.endswith(".yaml"):
            continue
        data = parse_yaml(os.path.join(BASE16_DIR, fname))
        name = data.get("scheme", fname[:-5])
        themes.append((name, data))
    return themes


def build_svg(themes):
    n_sub_rows = (len(SLOT_ORDER) + SWATCHES_PER_ROW - 1) // SWATCHES_PER_ROW
    row_w = SWATCHES_PER_ROW * (SWATCH_W + GAP) - GAP
    width = PADDING * 2 + row_w
    sub_row_h = SWATCH_H + LABEL_H
    theme_block_h = ROW_TITLE_H + n_sub_rows * sub_row_h + (n_sub_rows - 1) * GAP
    height = PADDING * 2 + len(themes) * (theme_block_h + GAP) - GAP

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" font-family="monospace">',
        f'<rect x="0" y="0" width="{width}" height="{height}" fill="#0d0d0f"/>',
    ]

    y = PADDING
    for name, data in themes:
        parts.append(
            f'<text x="{PADDING}" y="{y + 22}" font-size="20" font-weight="bold" fill="#e8e8e8">{name}</text>'
        )
        swatch_y = y + ROW_TITLE_H
        for i, slot in enumerate(SLOT_ORDER):
            sub_row = i // SWATCHES_PER_ROW
            col = i % SWATCHES_PER_ROW
            x = PADDING + col * (SWATCH_W + GAP)
            row_y = swatch_y + sub_row * (sub_row_h + GAP)
            hexval = data.get(slot, "000000")
            hexval = hexval if hexval.startswith("#") else "#" + hexval
            tcol = text_color(hexval)
            parts.append(
                f'<rect x="{x}" y="{row_y}" width="{SWATCH_W}" height="{SWATCH_H}" '
                f'fill="{hexval}" stroke="#000" stroke-width="1"/>'
            )
            parts.append(
                f'<text x="{x + SWATCH_W / 2}" y="{row_y + SWATCH_H / 2 - 4}" font-size="11" '
                f'fill="{tcol}" text-anchor="middle">{slot}</text>'
            )
            parts.append(
                f'<text x="{x + SWATCH_W / 2}" y="{row_y + SWATCH_H / 2 + 12}" font-size="10" '
                f'fill="{tcol}" text-anchor="middle">{hexval}</text>'
            )
            role = SLOT_ROLE.get(slot, "")
            parts.append(
                f'<text x="{x + SWATCH_W / 2}" y="{row_y + SWATCH_H + 16}" font-size="11" '
                f'fill="#999" text-anchor="middle">{role}</text>'
            )
        y += theme_block_h + GAP

    parts.append("</svg>")
    return "\n".join(parts)


def main():
    themes = load_themes()
    svg = build_svg(themes)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".svg", delete=False) as f:
        f.write(svg)
        svg_path = f.name

    try:
        subprocess.run(
            ["rsvg-convert", "-o", OUT_PNG, svg_path, "--background-color=#0d0d0f", "-z", "2"],
            check=True,
        )
    finally:
        os.remove(svg_path)

    print(f"wrote {OUT_PNG} ({', '.join(name for name, _ in themes)})")


if __name__ == "__main__":
    main()
