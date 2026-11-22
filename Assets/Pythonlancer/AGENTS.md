# Pythonlancer agent instructions

## Standing authorization: rh_pir_freighter

On 2026-11-18 the user declared rh_pir_freighter ready and transferred its
ongoing management to the agent. Validated model/SUR/damage updates and its
Pythonlancer source integration may be deployed without asking for ship
installation permission again. This is a scoped exception for this ship only.
Use tools.data_folder for every DATA write and rollback. Check current manual
HP edits before rebuilding. Keep the user's shared MAT and other ships intact.
Never launch Freelancer or FLServer. Normal generation and deployment remain
separate steps; authorization is not a request to regenerate unrelated DATA.

## DATA writes

Pythonlancer may write to the game's DATA directory only through
`tools.data_folder`. Extend `DataFolder` with the necessary methods for new
content. Generators and installers must not write, copy, move or delete DATA
files directly. Use the same entry point for staged DATA output and rollback.
Direct reads are allowed.

## Cutscene blends

A story cutscene needs `Assets/SCENES/<dump>.blend`. The dump is taken from that file. Old scenes do not share a dump: offer, accept, decision and the main cutscene each get their own file.

A marker a character moves to (`MoveFastEvent` / `MoveEvent` on `Char_*`, such as `trent_init_pos` or `trent_pos`) is drawn as that character: the same mesh as `Char_trent` (`trent_stand.obj`), not an empty. The object name stays the point name. Look-at markers, cameras and ship paths stay empties.

An event type the generator cannot emit is an error. Do not drop it. A spatial engine sound is `SpatialSound` plus `AttachEvent` onto the ship hardpoint, then `start`.

Action cutscenes (flyby, launch, cityscape) use absolute seconds from the source thn. The group clock does not move. Dialogue cutscenes are cut relatively: `facial()` and `append_time` own the clock, and `t` is only a cursor inside the current line.

Do not build or sync final cutscene `.thn` files. The user runs `single.py` for that. Prepare the Python scene only.

When analysing an old cutscene, the lipsync is the facial clips written next to the sound in the thn, such as `Sc_dx_s038x_4202_kress`. That window is the time allocated to the line. Replace those clips with `facial()`; do not keep the old clip. Build the following scene against that allocated window, not against the wav and not against the generic facial Pythonlancer substitutes later. A pause past that window is intentional and is there for a body animation. Do not drop it.
