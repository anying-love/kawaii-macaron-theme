# Kawaii Macaron Theme

[简体中文](README.md) | English

A soft macaron-pastel theme for VS Code, with a cute, sweet "kawaii" vibe: low-saturation warm-pink borders and accents, warm-yellow or cream-milk code areas. Soft colors that stay easy on the eyes.

## Features

- **Pink borders**: all dividing lines (editor groups, sidebar, tabs, panels, status bar) use the same low-saturation warm pink — sweet but not cloying.
- **Eye-friendly warm code areas**: two base colors — warm yellow / cream milk — comfortable for long coding sessions.
- **Macaron palette**: pink, white, milky-white, and warm yellow; comments, keywords, strings, etc. use low-saturation pastels for clear hierarchy.
- **Code-friendly**: syntax highlighting is contrast-tuned to stay readable on light backgrounds.

## Two theme variants

| Variant | Code area background | Best for |
| --- | --- | --- |
| `Kawaii Macaron · Warm Yellow 暖黄` | warm yellow `#FFF7E5` | a creamy sunny feel, softer for long reading |
| `Kawaii Macaron · Cream Milk 奶油白` | cream milk `#FDF5F0` | a fresh pink-white feel, a cleaner look |

Both variants share the same pink borders, sidebar, tabs and status bar; they differ only in the code area and a few backgrounds.

## Palette

| Purpose | Color | Value |
| --- | --- | --- |
| Border pink | low-saturation warm pink | `#F2B4C4` |
| Accent pink (cursor / active) | sakura pink | `#E58AA8` |
| Activity bar | sakura pink bg | `#F7DAE2` |
| Sidebar | milky white | `#FAF3E7` |
| Code area (warm) | warm yellow | `#FFF7E5` |
| Code area (cream) | cream milk | `#FDF5F0` |
| Keywords | raspberry pink | `#C2587F` |
| Strings | caramel brown | `#A8763F` |
| Numbers | peach orange | `#C0784F` |
| Comments | milk-tea gray | `#A79380` |

## Installation

### Option 1: VSIX package (recommended)

1. In VS Code press `Ctrl+Shift+P`, type `Extensions: Install from VSIX...` and press Enter.
2. Select `kawaii-macaron-theme-1.0.0.vsix`.
3. Restart VS Code, then press `Ctrl+K Ctrl+T` to pick the theme.

### Option 2: Install from source (for development)

Copy the whole `vscode-kawaii-macaron-theme` folder into the VS Code extensions directory:

- Windows: `%USERPROFILE%\.vscode\extensions\`
- macOS: `~/.vscode/extensions/`
- Linux: `~/.vscode/extensions/`

Restart VS Code and the two themes will appear in the theme picker.

### Option 3: Rebuild from source

No `vsce` needed — just run the bundled script (requires Python 3 + standard library):

```bash
python scripts/build_vsix.py
```

This generates `kawaii-macaron-theme-<version>.vsix` in the project root, then install it via Option 1.

### Option 4: Developer debugging

Open this folder in VS Code and press `F5` to launch the Extension Development Host and preview the theme live.

## Customization

The themes are plain JSON — edit `themes/kawaii-macaron-warm.json` or `themes/kawaii-macaron-cream.json`:

- Change the code-area background: edit `"editor.background"` and `"editorGutter.background"` under `colors`.
- Change the border pink: find-and-replace `#F2B4C4` with your favorite pink.
- Tweak syntax colors: edit the `foreground` of the corresponding entry under `tokenColors`.

Save, then re-select the theme in VS Code to apply.

## Project structure

```
vscode-kawaii-macaron-theme/
├── package.json           # extension manifest (declares two themes)
├── themes/                # theme color definitions (core)
│   ├── kawaii-macaron-warm.json     # warm-yellow variant
│   └── kawaii-macaron-cream.json    # cream-milk variant
├── images/icon.png        # extension icon (128×128 macaron)
├── scripts/
│   ├── make_icon.py       # generate the icon (relative paths, reproducible)
│   └── build_vsix.py      # offline .vsix packaging (no vsce needed)
├── preview/preview.html   # effect preview page
├── docs/REBUILD_GUIDE.md  # complete blueprint to recreate from scratch (Chinese)
├── README.md / README_EN.md / CHANGELOG.md / LICENSE
```

## Recreate from scratch

Want to build an identical theme? The full workflow — palette, directory structure, how to write each file, icon drawing and packaging steps — is documented in [docs/REBUILD_GUIDE.md](docs/REBUILD_GUIDE.md) (written in Chinese).

## License

MIT License
