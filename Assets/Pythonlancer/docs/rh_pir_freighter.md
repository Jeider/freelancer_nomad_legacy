# RH pirate freighter Q13

The user explicitly authorized this ship installation on 18 November 2026,
including continuing while the game is running; the user restarts it themselves.
This exception does not authorize future ship installations implicitly.

PirateHumpback uses the rh_pir_freighter template; nickname remains rh_freighter_pir.
The four CollisionGroups use unique DpRPF_* receiving points and existing pirate
Simple archetypes for the new damaged engines and torn panels. No flying debris caps.
The source assets are under assets/ships/rheinland/rh_pir_freighter with SHA256 manifest.
ShiparchManagerV2 publishes them through DataFolder.sync_rh_pir_freighter during
normal write=True builds, before writing shiparch.ini. write=False stays read-only.
The initial installation does not generate or overwrite active shiparch.ini.

LOD material handoff: rh_pir_freighter_projection_lod, texture
rh_pir_freighter_projection_lod.tga, DXT1 2048x2048 with 12 mips.
The user merges these into rh_pir_playerships.mat. Preserve these external names.
Do not ship, copy, overwrite or offer another LOD MAT in subsequent revisions.
The one-time authoring handoff is in the workspace ship's assets/rh_pir_freighter_lods.mat.
The merge is user-owned and is not claimed complete by this integration.
The template now uses the shared MAT only, plus envmapbasic.

## Latest source revision: narrow hold and deep panel wounds

Canonical source assets now use hold_damage: 26961 / 1776 / 494 triangles.
The cargo walls are inside the retracted btn paths; floor Y=0.355 is unchanged.
Both panel caps have recessed internal structure; ten light hardpoints moved.
The 398-edge HUD wire, other hardpoints and native animations are preserved.
Only five binary source assets and the hash manifest were updated. Existing
shiparch bindings, main SUR, engine wounds and the user's shared MAT remain.
That earlier step updated source assets only; the subsequent standing authorization below supersedes the deployment restriction.

## Standing authorization: rh_pir_freighter

On 2026-11-18 the user declared rh_pir_freighter ready and transferred its
ongoing management to the agent. Validated model/SUR/damage updates and its
Pythonlancer source integration may be deployed without asking for ship
installation permission again. This is a scoped exception for this ship only.
Use tools.data_folder for every DATA write and rollback. Check current manual
HP edits before rebuilding. Keep the user's shared MAT and other ships intact.
Never launch Freelancer or FLServer. Normal generation and deployment remain
separate steps; authorization is not a request to regenerate unrelated DATA.
