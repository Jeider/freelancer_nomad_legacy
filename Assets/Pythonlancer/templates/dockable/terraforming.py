from templates.space_object_template import SpaceObjectTemplate


class Terraforming(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'co_cur_02'
    TEMPLATE = '''[Object]
nickname = co_cur_02_SPHERE
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = sw_center_250
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_ROOT
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = terraforming_core
ids_name = 203830
ids_info = 067022
base = co_cur_02_base
;dock_with = co_cur_02_base
burn_color = 255, 222, 160
behavior = NOTHING
reputation = co_grp

[Object]
nickname = co_cur_02_HAND_dock01
pos = 0, 1150, 1400
rotate = -90, 0, 90
archetype = space_arch_dockable
base = co_cur_02_base
dock_with = co_cur_02_base
ids_name = 203831
ids_info = 065739
behavior = NOTHING
reputation = co_grp
voice = atc_leg_f01
space_costume = br_karina_head_gen, pl_female1_journeyman_body, prop_neuralnet_a_right
loadout = station_null

[Object]
nickname = co_cur_02_HAND_dock02
pos = 1205, 1150, -695
rotate = 30, 0, 90
archetype = space_arch_dockable
base = co_cur_02_base
dock_with = co_cur_02_base
ids_name = 203831
ids_info = 065739
behavior = NOTHING
reputation = co_grp
voice = atc_leg_f01
space_costume = br_karina_head_gen, pl_female1_journeyman_body, prop_neuralnet_a_right
loadout = station_null

[Object]
nickname = co_cur_02_HAND_dock03
pos = -1205, 1150, -695
rotate = 150, 0, 90
archetype = space_arch_dockable
base = co_cur_02_base
dock_with = co_cur_02_base
ids_name = 203831
ids_info = 065739
behavior = NOTHING
reputation = co_grp
voice = atc_leg_f01
space_costume = br_karina_head_gen, pl_female1_journeyman_body, prop_neuralnet_a_right
loadout = station_null


[Object]
nickname = co_cur_02_tube01
pos = -131, -1020, 75
rotate = -90, 30, 0
archetype = space_tube
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube02
pos = 133, -1020, 78
rotate = -90, 0, 0
archetype = space_tube
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube03
pos = 0, -1020, -150
rotate = -90, 0, 0
archetype = space_tube
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube01_tanks
pos = -240, -920, 138
rotate = -90, 30, 0
archetype = space_tube_hidden_connect
loadout = space_tube_tanks
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube02_tanks
pos = 240, -920, 138
rotate = -90, 150, 0
archetype = space_tube_hidden_connect
loadout = space_tube_tanks
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube03_tanks
pos = 0, -920, -280
rotate = -90, -90, 0
archetype = space_tube_hidden_connect
loadout = space_tube_tanks
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube01_girder01
pos = -240, -800, 138
rotate = -90, 30, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube02_girder01
pos = 240, -800, 138
rotate = -90, 150, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube03_girder01
pos = 0, -800, -280
rotate = -90, -90, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube01_girder02
pos = -240, -420, 138
rotate = -90, 30, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube02_girder02
pos = 240, -420, 138
rotate = -90, 150, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube03_girder02
pos = 0, -420, -280
rotate = -90, -90, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube01_girder03
pos = -223, -870, 129
rotate = 0, 120, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube02_girder03
pos = 223, -870, 129
rotate = 0, 240, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube03_girder03
pos = 0, -870, -257
rotate = 0, 0, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube01_girder04
pos = -84, -220, 48
rotate = 0, 120, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube02_girder04
pos = 84, -220, 48
rotate = 0, 240, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube03_girder04
pos = 0, -220, -100
rotate = 0, 0, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube01_girder05
pos = -131, 520, 75
rotate = -90, 30, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube02_girder05
pos = 133, 520, 78
rotate = -90, 0, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube03_girder05
pos = 0, 520, -150
rotate = -90, 0, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube04
pos = 451, -920, -260
rotate = -90, 0, 0
archetype = space_tube
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube05
pos = -451, -920, -260
rotate = -90, 0, 0
archetype = space_tube
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube06
pos = 0, -920, 520
rotate = -90, 0, 0
archetype = space_tube
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube04_girder01
pos = 451, 630, -260
rotate = 90, 0, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube05_girder01
pos = -451, 630, -260
rotate = 90, 0, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_tube06_girder01
pos = 0, 630, 520
rotate = 90, 0, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_shield01
pos = 0, -150, 830
rotate = 90, 0, 0
archetype = space_shield_cut
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_shield02
pos = -705, -150, -405
rotate = 90, 60, 0
archetype = space_shield_cut
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_shield03
pos = 705, -150, -405
rotate = 90, -60, 0
archetype = space_shield_cut
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_cntrl_twr01
pos = 0, -220, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_cntrl_twr02
pos = 0, 230, 0
rotate = 180, 0, 0
archetype = space_control_tower
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_cntrl_twr03
pos = 0, 530, 0
rotate = 180, 0, 0
archetype = space_control_tower
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_LIGHTGUN_root01
pos = 0, -210, 0
rotate = -90, 0, 0
archetype = space_industrial01a
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_LIGHTGUN_girder01
pos = 0, -320, 0
rotate = 180, 0, 0
archetype = space_cloakgen_laser ;space_girder
parent = co_cur_02_ROOT
loadout = terraform_effect

[Object]
nickname = co_cur_02_LIGHTGUN_girder02
pos = -40, -320, 0
rotate = 90, 0, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_LIGHTGUN_girder03
pos = 40, -320, 0
rotate = 90, 0, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_LIGHTGUN_girder04
pos = 0, -320, -40
rotate = 90, 0, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_LIGHTGUN_girder05
pos = 0, -320, 40
rotate = 90, 0, 0
archetype = space_girder
parent = co_cur_02_ROOT



[Object]
nickname = co_cur_02_large_ring01
pos = 0, -970, 0
rotate = 0, 0, 90
archetype = large_ring
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_large_ring02
pos = 0, -870, 0
rotate = 0, 0, 90
archetype = large_ring
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_large_ring03
pos = 0, -770, 0
rotate = 0, 0, 90
archetype = large_ring
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_large_ring04
pos = 0, -670, 0
rotate = 0, 0, 90
archetype = large_ring
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_large_ring05
pos = 0, -570, 0
rotate = 0, 0, 90
archetype = large_ring
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_large_ring06
pos = 0, -470, 0
rotate = 0, 0, 90
archetype = large_ring
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_large_ring07
pos = 0, -370, 0
rotate = 0, 0, 90
archetype = large_ring
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_SHIELD_girder01
pos = 0, -220, 340
rotate = 0, 0, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_SHIELD_girder02
pos = 0, 230, 340
rotate = 0, 0, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_SHIELD_girder03
pos = -282, -220, -163
rotate = 0, 60, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_SHIELD_girder04
pos = -282, 230, -163
rotate = 0, 60, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_SHIELD_girder05
pos = 282, -220, -163
rotate = 0, 120, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_SHIELD_girder06
pos = 282, 230, -163
rotate = 0, 120, 0
archetype = space_girder
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_industrial01
pos = 150, 380, -87
rotate = 90, 30, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_industrial02
pos = -150, 380, -86
rotate = 90, 60, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_industrial03
pos = 0, 380, 170
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_TOWER_controlA01
pos = 0, 875, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_TOWER_habitatA01
pos = -50, 630, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_TOWER_habitatA02
pos = 50, 630, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_TOWER_habitatA03
pos = 0, 630, -50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_TOWER_habitatA04
pos = 0, 630, 50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_TOWER_habitatA05
pos = -50, 785, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_TOWER_habitatA06
pos = 50, 785, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_TOWER_habitatA07
pos = 0, 785, -50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_TOWER_habitatA08
pos = 0, 785, 50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_TOWER_controlB01
pos = 0, 1205, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_TOWER_habitatB01
pos = -50, 960, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_TOWER_habitatB02
pos = 50, 960, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_TOWER_habitatB03
pos = 0, 960, -50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_TOWER_habitatB04
pos = 0, 960, 50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_TOWER_habitatB05
pos = -50, 1115, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_TOWER_habitatB06
pos = 50, 1115, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_TOWER_habitatB07
pos = 0, 1115, -50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_TOWER_habitatB08
pos = 0, 1115, 50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_TOWER_habitatC01
pos = 0, 1300, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_TOWER_habitatC02
pos = 0, 1445, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_TOWER_habitatC03
pos = 0, 1620, 0
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = co_cur_02_ROOT


[Object]
nickname = co_cur_02_HAND_hidden_connect01
pos = 0, 530, 0
rotate = 0, 0, 0
archetype = hidden_connect
loadout = hidden_planetform_part
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_HAND_hidden_connect02
pos = 0, 529.5, 0
rotate = 0, 120, 0
archetype = hidden_connect
loadout = hidden_planetform_part
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_HAND_hidden_connect03
pos = 0, 530.5, 0
rotate = 0, 240, 0
archetype = hidden_connect
loadout = hidden_planetform_part
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_rings_root01
pos = 0, -920, 0
rotate = 90, 0, 0
archetype = hidden_connect
loadout = planetform_rings
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_rings_root02
pos = 0, -420, 0
rotate = -90, 0, 0
archetype = hidden_connect
loadout = planetform_rings
parent = co_cur_02_ROOT
'''
