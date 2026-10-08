# Civic button artwork

The 25 icons are generated with the built-in image generation tool. The original
RFC civic atlas is the style reference. `generation.json` records the common
prompt, each subject, and its civic type.

Game assets are in `RFC MP Plus/Assets/Art/Interface/Buttons/Civics/RFCMP`:
64 x 64 pixels, DXT3 DDS, with the original atlas's rounded corner alpha mask.
The civic XML uses direct DDS paths for both the civic screen and Civilopedia.
`preview.png` shows the final icons by civic column at an enlarged pixel scale.

To convert a replacement generation, install Pillow in a local environment and
use `prepare_icons.py`. It reads an ignored `sources.local.json` mapping civic
types to generated PNG paths, writes the game textures and preview, and updates
the XML paths. Full-size generated originals remain in the tool's local output
folder; they are not part of the mod download.

For future generations, request the smallest available source size. The current
built-in tool exposes no explicit size parameter, so the final 64 x 64 resolution
is enforced during conversion.
