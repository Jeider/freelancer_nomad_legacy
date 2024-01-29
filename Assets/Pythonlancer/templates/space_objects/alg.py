from templates.space_object_template import SpaceObjectTemplate


class AlgBaseHokkaido(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_hkd_07'
    TEMPLATE = '''[Object]
nickname = ku_hkd_07
ids_name = 208625
pos = 0, 0, 0
rotate = 90, 0, -90
archetype = space_shipping01
ids_info = 067025
base = ku_hkd_07_base
dock_with = ku_hkd_07_base
visit = 16
reputation = ku_grp
behavior = NOTHING
voice = atc_leg_f01
space_costume = ku_tashi_head, pl_female1_peasant_body, prop_neuralnet_a

[Object]
nickname = ku_hkd_07_tube01
pos = 0, -500, -100
rotate = -90, 0, 0
archetype = space_short_tube
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_tube02
pos = 0, -500, 100
rotate = -90, 0, 0
archetype = space_short_tube
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_girder01
pos = 0, 264, -102
rotate = -78.8, 0, 0
archetype = space_girdera
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_girder02
pos = 0, 264, 102
rotate = -78.8, 180, 0
archetype = space_girdera
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_girder03
pos = 0, 273, 0
rotate = 0, 0, 0
archetype = space_girderc
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_girder04
pos = 0, -55, 0
rotate = 0, 0, 0
archetype = space_girderc
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_girder05
pos = 0, -382, 0
rotate = 0, 0, 0
archetype = space_girderc
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_girder06
pos = 175, -725, 0
rotate = 90, 0, 0
archetype = space_girderc
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_girder07
pos = -175, -725, 0
rotate = 90, 0, 0
archetype = space_girderc
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_girder08
pos = 0, -725, -175
rotate = 90, 0, 0
archetype = space_girderc
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_girder09
pos = 0, -725, 175
rotate = 90, 0, 0
archetype = space_girderc
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_girder10
pos = 0, -725, 0
rotate = 0, 0, 0
archetype = space_girder
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_girder11
pos = 0, -725, 0
rotate = 0, 90, 0
archetype = space_girder
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_girder12
pos = 0, -975, 0
rotate = 0, 0, 0
archetype = space_girderc
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_girder13
pos = 0, -1110, 0
rotate = 0, 0, 0
archetype = space_girderc
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_girder14
pos = 0, -1440, 0
rotate = 0, 0, 0
archetype = space_girderc
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_ind01
pos = 0, -625, -100
rotate = -90, 0, 0
archetype = space_industrialc
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_ind02
pos = 0, -625, 100
rotate = -90, 0, 0
archetype = space_industrialc
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_ind03
pos = 0, -725, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_ind04
pos = 175, -725, 0
rotate = 0, 0, 90
archetype = space_industrial02d
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_ind05
pos = -175, -725, 0
rotate = 0, 0, 90
archetype = space_industrial02d
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_ind06
pos = 0, -725, -175
rotate = 90, 0, 90
archetype = space_industrial02d
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_ind07
pos = 0, -725, 175
rotate = 90, 0, 90
archetype = space_industrial02d
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_ctrl_twr01
pos = 0, -625, 0
rotate = 180, 45, 0
archetype = space_control_tower
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_ctrl_twr02
pos = 0, -825, 0
rotate = 0, 45, 0
archetype = space_control_tower
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_indA01
pos = -200, -725, -80
rotate = 0, 90, 0
archetype = space_industrial01c
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_indA02
pos = -200, -725, 80
rotate = 0, 90, 0
archetype = space_industrial01c
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_indA03
pos = 200, -725, -80
rotate = 0, -90, 0
archetype = space_industrial01c
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_indA04
pos = 200, -725, 80
rotate = 0, -90, 0
archetype = space_industrial01c
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_indA05
pos = 80, -725, -200
rotate = 0, 0, 0
archetype = space_industrial01c
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_indA06
pos = -80, -725, -200
rotate = 0, 0, 0
archetype = space_industrial01c
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_indA07
pos = 80, -725, 200
rotate = 0, 180, 0
archetype = space_industrial01c
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_indA08
pos = -80, -725, 200
rotate = 0, 180, 0
archetype = space_industrial01c
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_production01
pos = -310, -725, -80
rotate = 0, 90, 0
archetype = space_production
loadout = mplatform_module_black
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_production02
pos = -310, -725, 80
rotate = 0, 90, 0
archetype = space_production
loadout = mplatform_module_black
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_production03
pos = 310, -725, -80
rotate = 0, -90, 0
archetype = space_production
loadout = mplatform_module_black
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_production04
pos = 310, -725, 80
rotate = 0, -90, 0
archetype = space_production
loadout = mplatform_module_black
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_production05
pos = 80, -725, 310
rotate = 0, 180, 0
archetype = space_production
loadout = mplatform_module_black
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_production06
pos = -80, -725, 310
rotate = 0, 0, 0
archetype = space_production
loadout = mplatform_module_black
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_production07
pos = 80, -725, -310
rotate = 0, 0, 0
archetype = space_production
loadout = mplatform_module_black
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_production08
pos = -80, -725, -310
rotate = 0, 0, 0
archetype = space_production
loadout = mplatform_module_black
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_tanks01
pos = 0, -975, -104
rotate = 0, 90, 90
archetype = space_tankl4x4
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_tanks02
pos = 0, -1240, -104
rotate = 0, 90, 90
archetype = space_tankl4x4
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_tanks03
pos = 0, -975, 104
rotate = 0, 90, 90
archetype = space_tankl4x4
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_tanks04
pos = 0, -1240, 104
rotate = 0, 90, 90
archetype = space_tankl4x4
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_tanks05
pos = 0, -1440, -104
rotate = 0, 90, 90
archetype = space_tankl2x2
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_tanks06
pos = 0, -1440, 104
rotate = 0, 90, 90
archetype = space_tankl2x2
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_ctrl_twr03
pos = 0, -865, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_ctrl_twr04
pos = 0, -975, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_ctrl_twr05
pos = 0, -1110, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_ctrl_twr06
pos = 0, -1440, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_ctrl_block01
pos = 0, -1500, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_ctrl_block02
pos = 0, 720, 0
rotate = 0, 0, 0
archetype = space_small_control_block
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_habitat01
pos = 0, -920, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_habitat02
pos = 0, -1040, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_habitat03
pos = 0, -1190, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_hkd_07

[Object]
nickname = ku_hkd_07_habitat04
pos = 0, -1360, 0
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = ku_hkd_07
'''
