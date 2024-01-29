from templates.space_object_template import SpaceObjectTemplate


class KyushuAsteroidBase(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_ksu_05'
    TEMPLATE = '''[Object]
nickname = ku_ksu_05
ids_name = 203746
pos = 0, 0, 0
rotate = 180, 90, 0
archetype = miningbase_small_ice
ids_info = 065661
dock_with = ku_ksu_05_base
base = ku_ksu_05_base
reputation = kx_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = pl_male8_head, pi_pirate7_body, prop_neuralnet_c_right, prop_neuralnet_f_up
difficulty_level = 10
;loadout = solar_plant_ku
pilot = pilot_solar_hardest
visit = 16

[Object]
nickname = ku_ksu_05_ind01
pos = 0, -100, 0
rotate = 90, 0, 0
archetype = space_industrial01b
loadout = space_ind01_reactor
parent = ku_ksu_05

[Object]
nickname = ku_ksu_05_twr01
pos = 0, -150, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = ku_ksu_05

[Object]
nickname = ku_ksu_05_ctrl01
pos = 0, -150, 0
rotate = 180, 0, 0
archetype = space_pirate_control_block
parent = ku_ksu_05

[Object]
nickname = ku_ksu_05_twr02
pos = 0, 30, -90
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = ku_ksu_05

[Object]
nickname = ku_ksu_05_ctrl02
pos = 0, 60, -90
rotate = 0, 0, 0
archetype = space_pirate_control_block
parent = ku_ksu_05

[Object]
nickname = ku_ksu_05_girder01
pos = 0, -100, -85
rotate = 60, 0, 0
archetype = space_girderb
parent = ku_ksu_05

[Object]
nickname = ku_ksu_05_girder02
pos = 80, -95, 0
rotate = 70, -90, 0
archetype = space_girderb
parent = ku_ksu_05

[Object]
nickname = ku_ksu_05_girder03
pos = -80, -95, 0
rotate = 70, 90, 0
archetype = space_girderb
parent = ku_ksu_05

[Object]
nickname = ku_ksu_05_girder04
pos = 0, -90, 75
rotate = -70, 0, 0
archetype = space_girderb
parent = ku_ksu_05

[Object]
nickname = ku_ksu_05_girder05
pos = 30, -20, -95
rotate = 45, 0, 0
archetype = space_girderb
parent = ku_ksu_05

[Object]
nickname = ku_ksu_05_girder06
pos = -30, -20, -95
rotate = 45, 0, 0
archetype = space_girderb
parent = ku_ksu_05
'''
