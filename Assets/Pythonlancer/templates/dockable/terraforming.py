from templates.space_object_template import SpaceObjectTemplate


# CHANGE TO SINGLE DOCK ?
class Terraforming(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'co_cur_02'
    TEMPLATE = '''[Object]
nickname = co_cur_02_ROOT
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = terraforming_core
{root_props}

[Object]
nickname = co_cur_02_SPHERE
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = sw_center_250
parent = co_cur_02_ROOT

[Object]
nickname = co_cur_02_HAND_dock01
pos = 0, 1150, 1400
rotate = -90, 0, 90
archetype = space_arch_dockable
{dock_props}

[Object]
nickname = co_cur_02_HAND_dock02
pos = 1205, 1150, -695
rotate = 30, 0, 90
archetype = space_arch_dockable
{dock_props}

[Object]
nickname = co_cur_02_HAND_dock03
pos = -1205, 1150, -695
rotate = 150, 0, 90
archetype = space_arch_dockable
{dock_props}

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

class TerraformingTwo(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'alt_cur_02'
    TEMPLATE = '''[Object]
nickname = alt_cur_02
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = terraforming_core

[Object]
nickname = alt_cur_02_SPHERE
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = sw_center_250
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube01
pos = -131, -1020, 75
rotate = -90, 30, 0
archetype = space_tube_fix
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube02
pos = 133, -1020, 78
rotate = -90, 0, 0
archetype = space_tube_fix
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube03
pos = 0, -1020, -150
rotate = -90, 0, 0
archetype = space_tube_fix
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube01_tanks
pos = -240, -920, 138
rotate = -90, 30, 0
archetype = space_tube_hidden_connect
loadout = space_tube_tanks
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube02_tanks
pos = 240, -920, 138
rotate = -90, 150, 0
archetype = space_tube_hidden_connect
loadout = space_tube_tanks
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube03_tanks
pos = 0, -920, -280
rotate = -90, -90, 0
archetype = space_tube_hidden_connect
loadout = space_tube_tanks
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube01_girder01
pos = -240, -860, 138
rotate = -90, 30, 0
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube02_girder01
pos = 240, -860, 138
rotate = -90, 150, 0
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube03_girder01
pos = 0, -860, -280
rotate = -90, -90, 0
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube01_girder02
pos = -240, -420, 138
rotate = -90, 30, 0
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube02_girder02
pos = 240, -420, 138
rotate = -90, 150, 0
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube03_girder02
pos = 0, -420, -280
rotate = -90, -90, 0
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube01_girder03
pos = -223, -870, 129
rotate = 0, 120, 0
archetype = space_girderc
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube02_girder03
pos = 223, -870, 129
rotate = 0, 240, 0
archetype = space_girderc
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube03_girder03
pos = 0, -870, -257
rotate = 0, 0, 0
archetype = space_girderc
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube01_girder04
pos = -84, -220, 48
rotate = 0, 120, 0
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube02_girder04
pos = 84, -220, 48
rotate = 0, 240, 0
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube03_girder04
pos = 0, -220, -100
rotate = 0, 0, 0
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_cntrl_twr01
pos = 0, -220, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = alt_cur_02

[Object]
nickname = alt_cur_02_cntrl_twr02
pos = 0, 230, 0
rotate = 180, 0, 0
archetype = space_control_tower
parent = alt_cur_02

[Object]
nickname = alt_cur_02_cntrl_twr03
pos = 0, 530, 0
rotate = 180, 0, 0
archetype = space_control_tower
parent = alt_cur_02

[Object]
nickname = alt_cur_02_cntrl_twr04
pos = 0, 700, 0
rotate = 180, 0, 0
archetype = space_medium_control_tower
parent = alt_cur_02

[Object]
nickname = alt_cur_02_LIGHTGUN_root01
pos = 0, -210, 0
rotate = -90, 0, 0
archetype = space_industrial01a
parent = alt_cur_02

[Object]
nickname = alt_cur_02_LIGHTGUN_girder01
pos = 0, -320, 0
rotate = 180, 0, 0
archetype = space_cloakgen_laser
loadout = terraform_effect2
parent = alt_cur_02

[Object]
nickname = alt_cur_02_LIGHTGUN_girder02
pos = -40, -320, 0
rotate = 90, 0, 0
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_LIGHTGUN_girder03
pos = 40, -320, 0
rotate = 90, 0, 0
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_LIGHTGUN_girder04
pos = 0, -320, -40
rotate = 90, 0, 0
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_LIGHTGUN_girder05
pos = 0, -320, 40
rotate = 90, 0, 0
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_large_ring01
pos = 0, -970, 0
rotate = 0, 0, 90
archetype = large_ring
parent = alt_cur_02

[Object]
nickname = alt_cur_02_large_ring02
pos = 0, -870, 0
rotate = 0, 0, 90
archetype = large_ring
parent = alt_cur_02

[Object]
nickname = alt_cur_02_large_ring03
pos = 0, -770, 0
rotate = 0, 0, 90
archetype = large_ring
parent = alt_cur_02

[Object]
nickname = alt_cur_02_large_ring04
pos = 0, -670, 0
rotate = 0, 0, 90
archetype = large_ring
parent = alt_cur_02

[Object]
nickname = alt_cur_02_large_ring05
pos = 0, -570, 0
rotate = 0, 0, 90
archetype = large_ring
parent = alt_cur_02

[Object]
nickname = alt_cur_02_large_ring06
pos = 0, -470, 0
rotate = 0, 0, 90
archetype = large_ring
parent = alt_cur_02

[Object]
nickname = alt_cur_02_large_ring07
pos = 0, -370, 0
rotate = 0, 0, 90
archetype = large_ring
parent = alt_cur_02

[Object]
nickname = alt_cur_02_industrial01
pos = 150, 380, -87
rotate = 90, 30, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = alt_cur_02

[Object]
nickname = alt_cur_02_industrial02
pos = -150, 380, -86
rotate = 90, 60, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = alt_cur_02

[Object]
nickname = alt_cur_02_industrial03
pos = 0, 380, 170
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_controlA01
pos = 0, 875, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatA01
pos = -50, 630, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatA02
pos = 50, 630, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatA03
pos = 0, 630, -50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatA04
pos = 0, 630, 50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatA05
pos = -50, 790, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatA06
pos = 50, 790, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatA07
pos = 0, 790, -50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatA08
pos = 0, 790, 50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_controlB01
pos = 0, 1205, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatB01
pos = -50, 960, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatB02
pos = 50, 960, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatB03
pos = 0, 960, -50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatB04
pos = 0, 960, 50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatB05
pos = -50, 1115, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatB06
pos = 50, 1115, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatB07
pos = 0, 1115, -50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatB08
pos = 0, 1115, 50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatC01
pos = 0, 1300, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatC02
pos = 0, 1445, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatC03
pos = 0, 1620, 0
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = alt_cur_02

[Object]
nickname = alt_cur_02_rings_root01
pos = 0, -920, 0
rotate = 90, 0, 0
archetype = hidden_connect
loadout = planetform_rings
parent = alt_cur_02

[Object]
nickname = alt_cur_02_rings_root02
pos = 0, -420, 0
rotate = -90, 0, 0
archetype = hidden_connect
loadout = planetform_rings
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND01_ind01
pos = 0, 600, -150
rotate = 945, 0, 0
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND01_ind02
pos = 0, 800, -220
rotate = 90, 0, 0
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND01_ind03
pos = 0, 1030, -220
rotate = 90, 0, 0
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND01_ind04
pos = 0, 1260, -220
rotate = 90, 0, 0
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND01_ind05
pos = 0, 1490, -220
rotate = 90, 0, 0
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND01_dome01
pos = 0, 900, -260
rotate = -90, 0, 0
archetype = space_domea
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND01_dome02
pos = 0, 1150, -260
rotate = -90, 0, 0
archetype = space_domea
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND02_ind01
pos = -130.029054230132, 600, 74.7826521060806
rotate = 44.999999999993, 60.0958179265229, -180
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND02_ind02
pos = -190.709279537526, 800, 109.681223088918
rotate = -90, 60.0958179265229, -180
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND02_ind03
pos = -190.709279537526, 1030, 109.681223088918
rotate = -90, 60.0958179265229, -180
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND02_ind04
pos = -190.709279537526, 1260, 109.681223088918
rotate = -90, 60.0958179265229, -180
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND02_ind05
pos = -190.709279537526, 1490, 109.681223088918
rotate = -90, 60.0958179265229, -180
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND02_dome01
pos = -225.383693998895, 900, 129.62326365054
rotate = 90, 60.0958179265229, -180
archetype = space_domea
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND02_dome02
pos = -225.383693998895, 1150, 129.62326365054
rotate = 90, 60.0958179265229, -180
archetype = space_domea
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND03_ind01
pos = 129.392881221804, 600, 75.8780751542951
rotate = 45.0000000000003, -59.6119517932883, -180
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND03_ind02
pos = 189.776225791979, 800, 111.287843559633
rotate = -89.9999999999997, -59.6119517932883, -180
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND03_ind03
pos = 189.776225791979, 1030, 111.287843559633
rotate = -89.9999999999997, -59.6119517932883, -180
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND03_ind04
pos = 189.776225791979, 1260, 111.287843559633
rotate = -89.9999999999997, -59.6119517932883, -180
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND03_ind05
pos = 189.776225791979, 1490, 111.287843559633
rotate = -89.9999999999997, -59.6119517932883, -180
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND03_dome01
pos = 224.280994117794, 900, 131.521996934112
rotate = 90.0000000000003, -59.6119517932883, -180
archetype = space_domea
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND03_dome02
pos = 224.280994117794, 1150, 131.521996934112
rotate = 90.0000000000003, -59.6119517932883, -180
archetype = space_domea
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_slr01
pos = 0, 200, 400
rotate = 90, 0, 0
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_slr02
pos = 0, 420, 400
rotate = 90, 0, 0
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_slr03
pos = 0, -20, 400
rotate = 90, 0, 0
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_slr04
pos = 0, -240, 400
rotate = 90, 0, 0
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_slr05
pos = 0, -460, 400
rotate = 90, 0, 0
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_slr06
pos = 0, -680, 400
rotate = 90, 0, 0
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_slrB01
pos = 1, 310, 580
rotate = 90, 0, 0
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_slrB02
pos = 1, 90, 580
rotate = 90, 0, 0
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_slrB03
pos = 1, -130, 580
rotate = 90, 0, 0
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_slrB04
pos = 1, -350, 580
rotate = 90, 0, 0
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_slrB05
pos = 1, -570, 580
rotate = 90, 0, 0
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_gird01
pos = 2, 532, 382
rotate = -150, 0, 0
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_gird02
pos = 0, 532, 380
rotate = 30, 0, 0
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_gird03
pos = 0, 170, 680
rotate = 90, 0, 0
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_gird04
pos = 0, 0, 680
rotate = 90, 0, 0
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_gird05
pos = 0, -430, 680
rotate = 90, 0, 0
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_gird06
pos = 0, -792, 380
rotate = -30, 0, 0
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_gird07
pos = 1, -850, 282
rotate = 150, 0, 0
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_gird08
pos = 0, 225, 300
rotate = -90, 0, 0
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_gird09
pos = 0, -150, 300
rotate = 90, 0, 0
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_gird10
pos = 0, 40, 300
rotate = -90, 0, 0
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_gird11
pos = -1, -650, 300
rotate = 90, 0, 0
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slr01
pos = 346.776146558912, 200, -199.364751593063
rotate = -90.0000000000001, 60.1050137374333, -180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slr02
pos = 346.776146558912, 420, -199.364751593063
rotate = -90.0000000000001, 60.1050137374333, -180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slr03
pos = 346.776146558912, -20, -199.364751593063
rotate = -90.0000000000001, 60.1050137374333, -180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slr04
pos = 346.776146558912, -240, -199.364751593063
rotate = -90.0000000000001, 60.1050137374333, -180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slr05
pos = 346.776146558912, -460, -199.364751593063
rotate = -90.0000000000001, 60.1050137374333, -180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slr06
pos = 346.776146558912, -680, -199.364751593063
rotate = -90.0000000000001, 60.1050137374333, -180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slrB01
pos = 502.327000631437, 310, -289.945830176336
rotate = -90.0000000000001, 60.1050137374333, -180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slrB02
pos = 502.327000631437, 90, -289.945830176336
rotate = -90.0000000000001, 60.1050137374333, -180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slrB03
pos = 502.327000631437, -130, -289.945830176336
rotate = -90.0000000000001, 60.1050137374333, -180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slrB04
pos = 502.327000631437, -350, -289.945830176336
rotate = -90.0000000000001, 60.1050137374333, -180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slrB05
pos = 502.327000631437, -570, -289.945830176336
rotate = -90.0000000000001, 60.1050137374333, -180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird01
pos = 330.174396205794, 532, -192.127218504169
rotate = 29.9999999999999, 60.1050137374333, -180
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird02
pos = 329.437339230965, 532, -189.396514013409
rotate = -150, 60.1050137374333, -180
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird03
pos = 589.51944915015, 170, -338.920077708207
rotate = -90.0000000000001, 60.1050137374333, -180
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird04
pos = 589.51944915015, -8.70406600118298E-15, -338.920077708207
rotate = -90.0000000000001, 60.1050137374333, -180
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird05
pos = 589.51944915015, -430, -338.920077708207
rotate = -90.0000000000001, 60.1050137374333, -180
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird06
pos = 329.437339230965, -792, -189.396514013409
rotate = 150, 60.1050137374333, -180
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird07
pos = 243.978771445049, -850, -141.419090239505
rotate = -29.9999999999999, 60.1050137374333, -180
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird08
pos = 260.082109919183, 225, -149.523563694797
rotate = 90, 60.1050137374333, -180
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird09
pos = 260.082109919183, -150, -149.523563694797
rotate = -90.0000000000001, 60.1050137374333, -180
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird10
pos = 260.082109919183, 40, -149.523563694797
rotate = 90, 60.1050137374333, -180
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird11
pos = 260.580521798165, -650, -148.656623328399
rotate = -90.0000000000001, 60.1050137374333, -180
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_slr01
pos = -347.429802364986, 200, -198.223440663897
rotate = -90, -60.2934080908103, 180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_slr02
pos = -347.429802364986, 420, -198.223440663897
rotate = -90, -60.2934080908103, 180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_slr03
pos = -347.429802364986, -20, -198.223440663897
rotate = -90, -60.2934080908103, 180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_slr04
pos = -347.429802364986, -240, -198.223440663897
rotate = -90, -60.2934080908103, 180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_slr05
pos = -347.429802364986, -460, -198.223440663897
rotate = -90, -60.2934080908103, 180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_slr06
pos = -347.429802364986, -680, -198.223440663897
rotate = -90, -60.2934080908103, 180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_slrB01
pos = -504.268772030887, 310, -286.555414456736
rotate = -90, -60.2934080908103, 180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_slrB02
pos = -504.268772030887, 90, -286.555414456736
rotate = -90, -60.2934080908103, 180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_slrB03
pos = -504.268772030887, -130, -286.555414456736
rotate = -90, -60.2934080908103, 180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_slrB04
pos = -504.268772030887, -350, -286.555414456736
rotate = -90, -60.2934080908103, 180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_slrB05
pos = -504.268772030887, -570, -286.555414456736
rotate = -90, -60.2934080908103, 180
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_gird01
pos = -332.786578461881, 532, -187.566236822196
rotate = 30.0000000000001, -60.2934080908103, 180
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_gird02
pos = -330.058312246737, 532, -188.312268630702
rotate = -150, -60.2934080908103, 180
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_gird03
pos = -590.630664020476, 170, -336.979849128625
rotate = -90, -60.2934080908103, 180
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_gird04
pos = -590.630664020476, -9.74103888545392E-15, -336.979849128625
rotate = -90, -60.2934080908103, 180
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_gird05
pos = -590.630664020476, -430, -336.979849128625
rotate = -90, -60.2934080908103, 180
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_gird06
pos = -330.058312246737, -792, -188.312268630702
rotate = 150, -60.2934080908103, 180
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_gird07
pos = -245.433569268974, -850, -138.878951162134
rotate = -29.9999999999999, -60.2934080908103, 180
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_gird08
pos = -260.572351773738, 225, -148.667580497922
rotate = 90, -60.2934080908103, 180
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_gird09
pos = -260.572351773738, -150, -148.667580497922
rotate = -90, -60.2934080908103, 180
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_gird10
pos = -260.572351773738, 40, -148.667580497922
rotate = 90, -60.2934080908103, 180
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_gird11
pos = -260.076793172078, -650, -149.536155003834
rotate = -90, -60.2934080908103, 180
archetype = space_girder
parent = alt_cur_02
'''
