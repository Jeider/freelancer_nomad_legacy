# RH pirate elite integration

Canonical asset directory: `DATA/ships/rheinland/rh_pir_elite`.
Gameplay nickname remains `rh_elite_pir` so saves, loadouts, IDs and balance stay compatible.
PirateValkyrie selects its own template in ShiparchManagerV2. Other variants retain their templates.
Normal V2 synchronization installs these source assets through DataFolder before writing shiparch.ini.
`write=False` is read-only. The initial asset/source installation does not rewrite active shiparch.ini.

Five detachable groups: two wings, two engines and the middle rear upright of tail.
The upper/lower frame and drum remain on Root. Five existing pirate Simple archetypes reference
the new parent-side damage caps. No group_dmg_hp/group_dmg_obj and no debris-side cap assets.
This is the current policy for fighters; debris-side caps are considered separately for capital ships.

Every part owns its wire. Empty explicit wires suppress triangle fallback on glass/doors/sockets.
The HUD snapshots the current animated pose; the SUR stays static in the unfolded pose.
The source user's equipment hardpoints, rig and all three rendered LOD meshes are preserved.
Private resource names carry a fresh export salt. Object names and shared material identities remain stable.
The shared rh_pir_playerships.mat is user-owned; this package adds only a private LOD MAT.

The installer deliberately leaves active shiparch.ini to the user's normal Pythonlancer generation.
No game process is launched by this integration.
