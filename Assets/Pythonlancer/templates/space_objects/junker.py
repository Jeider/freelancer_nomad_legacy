from templates.space_object_template import SpaceObjectTemplate


class HonshuJunker(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_hns_04'
    TEMPLATE = '''[Object]
nickname = ku_hns_04
ids_name = 203769
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = space_police01
ids_info = 065684
base = ku_hns_04_base
dock_with = ku_hns_04_base
visit = 16
reputation = kx_grp
behavior = NOTHING
voice = atc_leg_f01
space_costume = ku_kym_head_gen, pl_female2_journeyman_body, prop_neuralnet_f
difficulty_level = 10
loadout = depot_ku
pilot = pilot_solar_hardest

[Object]
nickname = ku_hns_04_industrial01
pos = 0, 210, 0
rotate = 90, 0, 0
archetype = space_industrial02a
parent = ku_hns_04

[Object]
nickname = ku_hns_04_industrial02
pos = 0, 210, 190
rotate = 0, 0, 45
archetype = space_industriala
parent = ku_hns_04

[Object]
nickname = ku_hns_04_industrial03
pos = 0, 210, -190
rotate = 0, 0, 45
archetype = space_industriala
parent = ku_hns_04

[Object]
nickname = ku_hns_04_industrial04
pos = -140, 200, 0
rotate = 0, 90, 30
archetype = space_industriala
parent = ku_hns_04

[Object]
nickname = ku_hns_04_industrial05
pos = 140, 200, 0
rotate = 0, 90, -30
archetype = space_industrial_dmg
parent = ku_hns_04

[Object]
nickname = ku_hns_04_tanks01
pos = -50, 160, -180
rotate = 0, 0, -90
archetype = space_tankl4
parent = ku_hns_04

[Object]
nickname = ku_hns_04_tanks02
pos = 50, 160, -180
rotate = 0, 0, 90
archetype = space_tankl4
parent = ku_hns_04

[Object]
nickname = ku_hns_04_tanks03
pos = -50, 160, 190
rotate = 0, 0, -90
archetype = space_tankl4
parent = ku_hns_04

[Object]
nickname = ku_hns_04_tanks04
pos = 50, 160, 190
rotate = 0, 0, 90
archetype = space_tankl4
parent = ku_hns_04

[Object]
nickname = ku_hns_04_panel01
pos = 110, 225, -180
rotate = 0, 180, 15
archetype = space_debris_panel
parent = ku_hns_04

[Object]
nickname = ku_hns_04_panel02
pos = -110, 225, -180
rotate = 0, 0, -15
archetype = space_debris_panel
parent = ku_hns_04

[Object]
nickname = ku_hns_04_panel03
pos = 110, 225, 180
rotate = 0, 180, 15
archetype = space_debris_panel
parent = ku_hns_04

[Object]
nickname = ku_hns_04_panel04
pos = -110, 225, 180
rotate = 0, 0, -15
archetype = space_debris_panel
parent = ku_hns_04

[Object]
nickname = ku_hns_04_tower01
pos = 0, 360, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = ku_hns_04

[Object]
nickname = ku_hns_04_control01
pos = 0, 425, 0
rotate = 0, 0, 0
archetype = space_pirate_control_block
parent = ku_hns_04
'''