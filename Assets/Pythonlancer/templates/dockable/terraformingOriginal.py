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


class TerraformingRotate(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'alt_cur_02'
    TEMPLATE = '''[Object]
nickname = alt_cur_02
pos = -379, 500, 11
rotate = 0, 0, 0
archetype = space_police01
{dock_props}

[Object]
nickname = alt_cur_02_tankdmg1
pos = 869, -288, -31
rotate = 90, 39, 100
archetype = space_tanks_1dmg
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tankdmg2
pos = 609, -290, -31
rotate = 90, -2, 179
archetype = space_tanks_3dmg
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tankdmg3
pos = 469, -300, -31
rotate = 90, -2, 179
archetype = space_tanks_1dmg
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tankdmg4
pos = 269, -296, -31
rotate = 0, 30, 0
archetype = space_tanks_3dmg
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tankdmg5
pos = 369, -303, -131
rotate = 90, -2, 179
archetype = space_tanks_2dmg
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SPHERE
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = sw_center_250
parent = alt_cur_02

[Object]
nickname = alt_cur_02_xgird01
pos = -379, 300, 11
rotate = -90, 0, 0
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube01
pos = 1024, 75, 93
rotate = 85, 59, -93
archetype = space_tube_fix
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube02
pos = 1014, 76, -170
rotate = 16, 87, -163
archetype = space_tube_fix
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube03
pos = 900, -200, -35
rotate = 16, 87, -170
archetype = space_short_tube
parent = alt_cur_02

[;Object]
nickname = alt_cur_02_tube01_tanks
pos = 928, 140, 205
rotate = 85, 59, -93
archetype = space_tube_hidden_connect
loadout = space_tube_tanks
parent = alt_cur_02

[;Object]
nickname = alt_cur_02_tube02_tanks
pos = 910, 135, -274
rotate = 85, -60, -86
archetype = space_tube_hidden_connect
loadout = space_tube_tanks
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube02_girder01
pos = 850, 135, -272
rotate = 85, -60, -86
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube02_girder02
pos = 411, 135, -256
rotate = 85, -60, -86
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube01_girder03
pos = 877, 131, 189
rotate = 177, -30, -88
archetype = space_girderc
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube02_girder03
pos = 861, 126, -255
rotate = 2, -29, 88
archetype = space_girderc
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube01_girder04
pos = 222, 48, 75
rotate = 177, -30, -88
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_tube02_girder04
pos = 216, 47, -92
rotate = 2, -29, 88
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_cntrl_twr01
pos = 219, -0, -7
rotate = 106, 87, -163
archetype = space_control_tower
parent = alt_cur_02

[Object]
nickname = alt_cur_02_cntrl_twr02
pos = -229, 0, 8
rotate = -73, 87, -163
archetype = space_control_tower
parent = alt_cur_02

[Object]
nickname = alt_cur_02_cntrl_twr03
pos = -529, 0, 19
rotate = -73, 87, -163
archetype = space_control_tower
parent = alt_cur_02

[Object]
nickname = alt_cur_02_cntrl_twr04
pos = -699, 0, 25
rotate = -73, 87, -163
archetype = space_medium_control_tower
parent = alt_cur_02

[Object]
nickname = alt_cur_02_large_ring01
pos = 969, -0, -35
rotate = 90, -2, 179
archetype = large_ring
parent = alt_cur_02

[Object]
nickname = alt_cur_02_large_ring02
pos = 869, -0, -31
rotate = 90, -2, 179
archetype = large_ring
parent = alt_cur_02

[Object]
nickname = alt_cur_02_large_ring04
pos = 669, -0, -24
rotate = 90, -2, 179
archetype = large_ring
parent = alt_cur_02

[Object]
nickname = alt_cur_02_large_ring06
pos = 469, -0, -17
rotate = 190, -2, 169
archetype = large_ring
parent = alt_cur_02

[Object]
nickname = alt_cur_02_large_ring07
pos = 369, -0, -13
rotate = 90, -2, 174
archetype = large_ring
parent = alt_cur_02

[Object]
nickname = alt_cur_02_industrial01
pos = -385, -88, -135
rotate = -94, 59, -93
archetype = space_industrial01a
parent = alt_cur_02

[Object]
nickname = alt_cur_02_industrial02
pos = -374, -84, 164
rotate = -92, 29, -91
archetype = space_industrial01a
parent = alt_cur_02

[Object]
nickname = alt_cur_02_industrial03
pos = -379, 170, 11
rotate = -163, 87, -163
archetype = space_industrial01a
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_controlA01
pos = -874, 0, 31
rotate = 106, 87, -163
archetype = space_small_control_tower
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatA01
pos = -627, 0, 72
rotate = 106, 87, -163
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatA02
pos = -631, -0, -27
rotate = 106, 87, -163
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatA03
pos = -629, -49, 23
rotate = 106, 87, -163
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatA04
pos = -629, 50, 22
rotate = 106, 87, -163
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatA05
pos = -787, 0, 78
rotate = 106, 87, -163
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatA06
pos = -791, -0, -21
rotate = 106, 87, -163
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatA07
pos = -789, -49, 29
rotate = 106, 87, -163
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatA08
pos = -789, 50, 28
rotate = 106, 87, -163
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_controlB01
pos = -1204, 0, 43
rotate = 106, 87, -163
archetype = space_small_control_tower
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatB02
pos = -961, -0, -15
rotate = 106, 87, -163
archetype = space_habitat_dmg
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatB03
pos = -959, -49, 35
rotate = 106, 87, -163
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatB04
pos = -959, 50, 34
rotate = 106, 87, -163
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatB05
pos = -1112, 0, 90
rotate = 106, 87, -163
archetype = space_habitat_dmg
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatB07
pos = -1114, -49, 40
rotate = 106, 87, -163
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatB08
pos = -1114, 50, 39
rotate = 106, 87, -163
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatC01
pos = -1299, 0, 47
rotate = 106, 87, -163
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatC02
pos = -1444, 0, 52
rotate = 106, 87, -163
archetype = space_habitat_wide
parent = alt_cur_02

[Object]
nickname = alt_cur_02_TOWER_habitatC03
pos = -1618, 0, 58
rotate = 106, 87, -163
archetype = space_habitat_dmg
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND01_ind01
pos = -599, -149, 23
rotate = -28, 87, -163
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND01_ind02
pos = -799, -219, 31
rotate = -163, 87, -163
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND01_ind03
pos = -1029, -219, 39
rotate = -163, 87, -163
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND01_ind04
pos = -1259, -219, 48
rotate = -163, 87, -163
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND01_ind05
pos = -1489, -219, 56
rotate = -163, 87, -163
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND01_dome01
pos = -899, -259, 35
rotate = 16, 87, -163
archetype = space_domea
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND01_dome02
pos = -1149, -259, 44
rotate = 16, 87, -163
archetype = space_domea
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND02_ind03
pos = -1022, 112, 226
rotate = -82, -30, -88
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND02_ind04
pos = -1252, 112, 235
rotate = -102, -30, -88
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND02_ind05
pos = -1482, 132, 303
rotate = -112, -30, -88
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND02_dome02
pos = -1141, 132, 265
rotate = 127, 0, -178
archetype = space_dome_dmg2
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND03_ind01
pos = -604, 74, -108
rotate = -132, -29, 88
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND03_ind02
pos = -806, 109, -161
rotate = 92, -29, 88
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND03_ind03
pos = -1036, 109, -153
rotate = 92, -29, 88
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND03_ind04
pos = -1266, 109, -145
rotate = 92, -29, 88
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND03_ind05
pos = -1495, 109, -136
rotate = 92, -29, 88
archetype = space_industrial02d
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND03_dome01
pos = -907, 129, -192
rotate = -87, -29, 88
archetype = space_domea
parent = alt_cur_02

[Object]
nickname = alt_cur_02_HAND03_dome02
pos = -1157, 129, -183
rotate = -87, -29, 88
archetype = space_domea
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_slr04
pos = 239, 399, -12
rotate = -163, 87, -163
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_slr05
pos = 459, 399, -20
rotate = -163, 87, -163
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_slr06
pos = 679, 399, -28
rotate = -163, 87, -163
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_slrB04
pos = 349, 579, -19
rotate = -163, 87, -163
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_slrB05
pos = 569, 579, -27
rotate = -163, 87, -163
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_gird05
pos = 429, 679, -22
rotate = -163, 87, -163
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_gird06
pos = 791, 379, -32
rotate = 76, 87, -163
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_gird07
pos = 849, 281, -34
rotate = -103, 87, -163
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_gird09
pos = 149, 299, -8
rotate = -163, 87, -163
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_gird10
pos = 29, 269, -1
rotate = 16, 87, -150
archetype = space_beaml_dmg
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD01_gird11
pos = 649, 299, -25
rotate = -163, 87, -163
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slr01
pos = -212, -202, -337
rotate = -92, -30, -88
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slr02
pos = -432, -202, -329
rotate = -92, -30, -88
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slr03
pos = 7, -203, -345
rotate = -92, -30, -88
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slr04
pos = 227, -203, -353
rotate = -92, -30, -88
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slr05
pos = 447, -203, -361
rotate = -92, -30, -88
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slr06
pos = 666, -203, -369
rotate = -92, -30, -88
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slrB01
pos = -328, -295, -487
rotate = -92, -30, -88
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slrB02
pos = -108, -295, -495
rotate = -92, -30, -88
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slrB03
pos = 111, -295, -503
rotate = -92, -30, -88
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slrB04
pos = 331, -295, -511
rotate = -92, -30, -88
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_slrB05
pos = 551, -295, -519
rotate = -92, -30, -88
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird01
pos = -543, -195, -308
rotate = 27, -30, -88
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird02
pos = -543, -192, -307
rotate = -152, -30, -88
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird03
pos = -191, -345, -579
rotate = -92, -30, -88
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird04
pos = -21, -345, -585
rotate = -92, -30, -88
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird05
pos = 408, -345, -601
rotate = -92, -30, -88
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird06
pos = 779, -193, -355
rotate = 147, -30, -88
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird07
pos = 840, -144, -273
rotate = -32, -30, -88
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird08
pos = -234, -152, -250
rotate = 87, -30, -88
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird09
pos = 140, -152, -263
rotate = -92, -30, -88
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird10
pos = -49, -152, -256
rotate = 87, -30, -88
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD02_gird11
pos = 640, -151, -282
rotate = -92, -30, -88
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_slr01
pos = -187, -194, 356
rotate = 92, -29, 85
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_slr02
pos = -407, -194, 364
rotate = 92, -29, 88
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_slr05
pos = 472, -194, 332
rotate = 90, -29, 88
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_slr06
pos = 692, -194, 324
rotate = 92, -29, 88
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_slrB01
pos = -291, -281, 518
rotate = 92, -26, 88
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_slrB04
pos = 368, -261, 494
rotate = 90, -29, 80
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_slrB05
pos = 587, -281, 486
rotate = 92, -29, 88
archetype = space_panel
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_gird01
pos = -519, -183, 353
rotate = -147, -29, 88
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_gird02
pos = -519, -184, 351
rotate = 32, -29, 88
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_gird03
pos = -218, -330, 599
rotate = -72, -29, 88
archetype = space_beaml_dmg
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_gird05
pos = 451, -320, 578
rotate = 92, -29, 85
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_gird06
pos = 803, -185, 303
rotate = -27, -29, 88
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_gird07
pos = 858, -136, 215
rotate = 152, -29, 88
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_gird08
pos = -215, -145, 270
rotate = -87, -29, 88
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_gird09
pos = 159, -145, 256
rotate = 92, -29, 88
archetype = space_girdera
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_gird10
pos = -30, -145, 263
rotate = -87, -29, 88
archetype = space_girder
parent = alt_cur_02

[Object]
nickname = alt_cur_02_SHIELD03_gird11
pos = 659, -147, 237
rotate = 92, -29, 88
archetype = space_girder
parent = alt_cur_02
'''


class Track(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'Br05'
    TEMPLATE = '''[Object]
nickname = Br05_telescope_1
ids_name = 216606
pos = 2329.9330075939, 120, 1663.32906827743
rotate = 0, -75, 0
archetype = telescope_no_target

[Object]
nickname = Br05_track_ring_2
ids_name = 216617
pos = 2325.9330075939, 0, 1665.32906827743
rotate = 0, 120, 0
archetype = track_ring
ids_info = 66614

[Object]
nickname = Br05_track_ring_4
ids_name = 216617
pos = 1025.93300759389, 0, 2330.32906827743
rotate = 0, 120, 0
archetype = track_ring
ids_info = 66614

[Object]
nickname = Br05_track_ring_5
ids_name = 216617
pos = -1500.06699240611, 100, 3368.32906827743
rotate = 0, 80, 0
archetype = track_ring
ids_info = 66614

[Object]
nickname = Br05_track_ring_6
ids_name = 216617
pos = -2357.06699240611, 125, 2706.32906827743
rotate = 0, 50, 0
archetype = track_ring
ids_info = 66614

[Object]
nickname = Br05_track_ring_7
ids_name = 216617
pos = -2914.0669924061, 150, 2054.32906827742
rotate = 10, 10, 2
archetype = track_ring
ids_info = 66614

[Object]
nickname = Br05_track_ring_8
ids_name = 216617
pos = -2755.0669924061, 100, 1126.32906827743
rotate = 0, -5, 0
archetype = track_ring
ids_info = 66614

[Object]
nickname = Br05_track_ring_9
ids_name = 216617
pos = -3127.0669924061, 75, 309.329068277425
rotate = 0, 30, 0
archetype = track_ring
ids_info = 66614

[Object]
nickname = Br05_track_ring_10
ids_name = 216617
pos = -2895.0669924061, 0, -862.670931722566
rotate = 0, -40, 0
archetype = track_ring
ids_info = 66614

[Object]
nickname = Br05_track_ring_11
ids_name = 216617
pos = -2190.0669924061, -25, -1281.67093172256
rotate = 0, -50, 0
archetype = track_ring
ids_info = 66614

[Object]
nickname = Br05_track_ring_12
ids_name = 216617
pos = -1495.06699240611, -50, -2779.67093172257
rotate = 0, -65, 0
archetype = track_ring
ids_info = 66614

[Object]
nickname = Br05_track_ring_13
ids_name = 216617
pos = -580.066992406121, -200, -3112.67093172257
rotate = 0, -70, 0
archetype = track_ring
ids_info = 66614

[Object]
nickname = Br05_track_ring_14
ids_name = 216617
pos = 226.933007593883, -25, -3026.67093172257
rotate = 0, -110, 0
archetype = track_ring
ids_info = 66614

[Object]
nickname = Br05_track_ring_15
ids_name = 216617
pos = 1041.93300759389, -25, -1952.67093172256
rotate = 0, -100, 0
archetype = track_ring
ids_info = 66614

[Object]
nickname = Br05_track_ring_16
ids_name = 216617
pos = 2351.9330075939, 50, -1714.67093172256
rotate = 0, -115, 0
archetype = track_ring
ids_info = 66614

[Object]
nickname = Br05_track_ring_17
ids_name = 216617
pos = 2975.93300759389, 200, -689.670931722566
rotate = 0, -175, 0
archetype = track_ring
ids_info = 66614

[Object]
nickname = Br05_track_ring_18
ids_name = 216617
pos = 3121.93300759389, -50, 446.329068277436
rotate = -173, 50, -176
archetype = track_ring
ids_info = 66614

[Object]
nickname = Br05_track_ring_19
ids_name = 216617
pos = -195.066992406107, 50, 3147.32906827743
rotate = 0, 120, 0
archetype = track_ring
ids_info = 66614

[Object]
nickname = Br05_track_ring_20
ids_name = 216617
pos = -1720.06699240611, 0, -1962.67093172256
rotate = 0, -25, 0
archetype = track_ring
ids_info = 66614

[Object]
nickname = Br05_track_ring_21
ids_name = 216617
pos = 603.933007593892, -75, -2465.67093172256
rotate = 0, -150, 0
archetype = track_ring
ids_info = 66614

[Object]
nickname = Br05_track_ring_22
ids_name = 216617
pos = 1781.93300759389, 0, -2088.67093172256
rotate = 0, -90, 0
archetype = track_ring
ids_info = 66614

[Object]
nickname = Br05_track_ring_23
ids_name = 216617
pos = 2924.93300759389, 100, -1473.67093172256
rotate = 0, -155, 0
archetype = track_ring
ids_info = 66614

[Object]
nickname = Br05_nav_buoy_2
ids_name = 261162
pos = 2180.93300759389, 200, 1378.32906827743
archetype = nav_buoy_non_targetable
ids_info = 66147

[Object]
nickname = Br05_nav_buoy_4
ids_name = 261162
pos = 2283.9330075939, -200, 1573.32906827743
archetype = nav_buoy_non_targetable
ids_info = 66147

[Object]
nickname = Br05_nav_buoy_6
ids_name = 261162
pos = 2389.9330075939, 200, 1779.32906827742
archetype = nav_buoy_non_targetable
ids_info = 66147

[Object]
nickname = Br05_nav_buoy_8
ids_name = 261162
pos = 2481.93300759389, -200, 1960.32906827742
archetype = nav_buoy_non_targetable
ids_info = 66147

[Object]
nickname = Br05_nav_buoy_9
ids_name = 261162
pos = 2202.93300759389, -200, 1398.32906827743
archetype = nav_buoy_non_targetable
ids_info = 66147

[Object]
nickname = Br05_nav_buoy_12
ids_name = 261162
pos = 2281.9330075939, 200, 1573.32906827743
archetype = nav_buoy_non_targetable
ids_info = 66147

[Object]
nickname = Br05_nav_buoy_14
ids_name = 261162
pos = 2389.9330075939, -200, 1778.32906827742
archetype = nav_buoy_non_targetable
ids_info = 66147

[Object]
nickname = Br05_nav_buoy_16
ids_name = 261162
pos = 2485.93300759389, 200, 1965.32906827742
archetype = nav_buoy_non_targetable
ids_info = 66147
'''