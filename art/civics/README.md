# Civic button artwork

All 25 current icons are symbolic pixel illustrations drawn directly at
64 x 64 pixels with Pillow. No image generation service is used for this set.
The original RFC civic atlas supplies the rounded corner alpha mask.

The five Government icons are drawn directly at 64 x 64 pixels by
`draw_government.py`, without an image generation service:

- Tribal System: a community hearth and crossed flint spears.
- Monarchy: a gold throne with burgundy upholstery and crown crest.
- Republic: a senate portico framed by olive branches.
- Dictatorship: an iron gauntlet in front of a crimson standard.
- Democracy: a marked ballot and wooden ballot box.

Run `.venv-art/Scripts/python.exe art/civics/draw_government.py` from the
workspace root to recreate their DXT3 textures, PNG sources, and
`government-pixel-preview.png`. The preview shows the compressed game assets.
Monarchy's drawing is defined in `draw_monarchy.py`. All five buttons use the
original atlas's rounded corner alpha, with no added gold frame.
The other 20 icons are defined in `draw_symbolic_civics.py`:

| Category | Civic symbols, in row order |
| --- | --- |
| Legitimacy | Jeweled scepter; ceremonial mitre and book; gold coin stacks; abstract flag; scales of justice and law document |
| Labor | Harvest basket; shackles; grain and sickle; hammer and sickle; market stall |
| Military | Wooden shield and spear; town wall and bow; horseshoe and lance; military helmet and swords; muster list and helmets |
| Religion | Ancestral memorial and candles; radiant sacred book; crowned sanctuary; three equal interlinked rings; atom and reference book |

To rebuild the complete set, run from the workspace root:

```powershell
.\.venv-art\Scripts\python.exe art/civics/draw_government.py
.\.venv-art\Scripts\python.exe art/civics/draw_symbolic_civics.py
```

This writes the native-size `*-pixel.png` sources, the game DDS files,
`symbolic-civics-preview.png`, and the compact `preview.png` contact sheet.
Both contact sheets show the actual compressed game assets. Copy changed DDS
files to the installed mod after rebuilding the artwork.

Game assets are in `RFC MP Plus/Assets/Art/Interface/Buttons/Civics/RFCMP`:
64 x 64 pixels, DXT3 DDS, with the original atlas's rounded corner alpha mask.
The civic XML uses direct DDS paths for both the civic screen and Civilopedia.
`preview.png` shows the final icons by civic column at an enlarged pixel scale.

`prepare_icons.py` and `generation.json` describe the earlier image-generation
workflow. Running that converter overwrites the symbolic buttons with its input
images. Run both drawing scripts afterward to restore the current set.
