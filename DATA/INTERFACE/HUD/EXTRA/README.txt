Cloak icon: HUD_DefCloak.3db (the existing client filename is retained).
Its contents are a standalone copy of the Health opening button, HUD_targetedobject.
It no longer uses the Beta DefCloak atlas.

Unique texture: HUD_health_cloak_icon.tga, initially 32x32 with alpha.
Unique material: UI_HUD_health_cloak_icon_mat.
Unique mesh: HUD_health_cloak_icon.lod0.vms.

In a UTF editor replace:
  Texture library / HUD_health_cloak_icon.tga / MIP0
with your complete 32-bit TGA icon. The quad covers the whole texture with
the original Health edge insets; there are no other icons in this texture.
Keep the UI_ material prefix for HUD button tinting.

The adjacent TGA is an editable source; the game reads the texture embedded
in the 3db, not the loose TGA. To rebuild from an edited TGA in this repository:
  python -B tools/health_equipment/stage_icon.py --texture assets/hud/extra/HUD_health_cloak_icon.tga

Install the rebuilt 3db to FL_MOD/DATA/INTERFACE/HUD/EXTRA and restart the game.
