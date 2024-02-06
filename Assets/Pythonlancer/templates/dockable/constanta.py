from templates.space_object_template import SpaceObjectTemplate


class Constanta(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'sig22_02'
    TEMPLATE = '''[Object]
nickname = sig22_02_dock
ids_name = 196722
ids_info = 065739
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_police01
dock_with = sig22_02_Base
base = sig22_02_Base
reputation = edv_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = pl_male4_head, sh_male2_body, prop_neuralnet_b_right
difficulty_level = 16
;loadout = space_freeport01_li
pilot = pilot_solar_hardest

[Object]
nickname = sig22_02
ids_name = 203662
pos = 0, 0, 950
rotate = 0, -90, 0
archetype = constanta_core
ids_info = 065580
dock_with = sig22_02_Base
base = sig22_02_Base
reputation = edv_grp
behavior = NOTHING

;ROOT

[Object]
nickname = sig22_02_ROOT_cntrl_block01
pos = 0, -89, 0
rotate = 180, 90, 0
archetype = space_small_control_block
parent = sig22_02

[Object]
nickname = sig22_02_ROOT_cntrl_twr01
pos = 0, 150, 950
rotate = 180, 0, 0
archetype = space_control_tower
parent = sig22_02

[Object]
nickname = sig22_02_ROOT_cntrl_twr02
pos = 0, -150, 950
rotate = 0, 0, 0
archetype = space_control_tower
parent = sig22_02

[Object]
nickname = sig22_02_ROOT_industrial01
pos = 0, 0, 950
rotate = 90, 0, 0
archetype = space_industriala
parent = sig22_02

[Object]
nickname = sig22_02_ROOT_industrial02
pos = 0, 0, 950
rotate = 90, 30, 0
archetype = space_industriala
parent = sig22_02

[Object]
nickname = sig22_02_ROOT_industrial03
pos = 0, 0, 950
rotate = 90, 60, 0
archetype = space_industriala
parent = sig22_02

[Object]
nickname = sig22_02_ROOT_industrial04
pos = 150, 0, 863
rotate = 90, 30, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = sig22_02

[Object]
nickname = sig22_02_ROOT_industrial05
pos = -150, 0, 864
rotate = 90, 60, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = sig22_02

[Object]
nickname = sig22_02_ROOT_industrial06
pos = 0, 0, 1120
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = sig22_02

[Object]
nickname = sig22_02_ROOT_girder01
pos = 223, 0, 1079
rotate = 0, 240, 0
archetype = space_girder
parent = sig22_02

[Object]
nickname = sig22_02_ROOT_girder02
pos = 0, 0, 693
rotate = 0, 0, 0
archetype = space_girder
parent = sig22_02

[Object]
nickname = sig22_02_ROOT_girder03
pos = -223, 0, 1079
rotate = 0, 120, 0
archetype = space_girder
parent = sig22_02

;TOP BLOCK (HILL)

[Object]
nickname = sig22_02_TOP_cntrl_twr01
pos = 0, 195, 950
rotate = 180, 0, 0
archetype = space_control_tower
parent = sig22_02

[Object]
nickname = sig22_02_TOP_cntrl_twr02
pos = 0, 380, 950
rotate = 180, 0, 0
archetype = space_control_tower
parent = sig22_02

[Object]
nickname = sig22_02_TOP_habitat01
pos = 150, 288, 863
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_TOP_habitat02
pos = -150, 288, 864
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_TOP_habitat03
pos = 0, 288, 1120
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_TOP_habitat04
pos = -150, 288, 1037
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_TOP_habitat05
pos = 150, 288, 1036
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_TOP_habitat06
pos = 0, 288, 780
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_TOP_habitat07
pos = 0, 265, 1013
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = sig22_02

[Object]
nickname = sig22_02_TOP_habitat08
pos = 0, 265, 887
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = sig22_02

[Object]
nickname = sig22_02_TOP_habitat09
pos = 63, 265, 950
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = sig22_02

[Object]
nickname = sig22_02_TOP_habitat10
pos = -63, 265, 950
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = sig22_02

[Object]
nickname = sig22_02_TOP_habitat11
pos = 0, 288, 950
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_TOP_habitat12
pos = 0, 476, 950
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_TOP_habitat13
pos = 0, 450, 1015
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_TOP_habitat14
pos = 65, 450, 950
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_TOP_habitat15
pos = -65, 450, 950
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_TOP_habitat16
pos = 0, 508, 890
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = sig22_02

[Object]
nickname = sig22_02_TOP_habitat17
pos = 0, 600, 1015
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = sig22_02

[Object]
nickname = sig22_02_TOP_habitat18
pos = 65, 540, 950
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = sig22_02

[Object]
nickname = sig22_02_TOP_habitat19
pos = 0, 650, 950
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = sig22_02


;BOTTOM BLOCK (HILL)

[Object]
nickname = sig22_02_BOTTOM_cntrl_twr01
pos = 0, -195, 950
rotate = 0, 0, 0
archetype = space_control_tower
parent = sig22_02

[Object]
nickname = sig22_02_BOTTOM_cntrl_twr02
pos = 0, -380, 950
rotate = 0, 0, 0
archetype = space_control_tower
parent = sig22_02

[Object]
nickname = sig22_02_BOTTOM_habitat01
pos = 150, -288, 863
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_BOTTOM_habitat02
pos = -150, -288, 864
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_BOTTOM_habitat03
pos = 0, -288, 1120
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_BOTTOM_habitat04
pos = -150, -288, 1037
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_BOTTOM_habitat05
pos = 150, -288, 1036
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_BOTTOM_habitat06
pos = 0, -288, 780
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_BOTTOM_habitat07
pos = 0, -265, 1013
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = sig22_02

[Object]
nickname = sig22_02_BOTTOM_habitat08
pos = 0, -265, 887
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = sig22_02

[Object]
nickname = sig22_02_BOTTOM_habitat09
pos = 63, -265, 950
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = sig22_02

[Object]
nickname = sig22_02_BOTTOM_habitat10
pos = -63, -265, 950
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = sig22_02

[Object]
nickname = sig22_02_BOTTOM_habitat11
pos = 0, -288, 950
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_BOTTOM_habitat12
pos = 0, -476, 950
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_BOTTOM_habitat13
pos = 0, -450, 1015
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_BOTTOM_habitat14
pos = 65, -450, 950
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_BOTTOM_habitat15
pos = -65, -450, 950
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_BOTTOM_habitat16
pos = 0, -508, 890
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = sig22_02

[Object]
nickname = sig22_02_BOTTOM_habitat17
pos = 0, -600, 1015
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = sig22_02

[Object]
nickname = sig22_02_BOTTOM_habitat18
pos = 65, -540, 950
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = sig22_02

[Object]
nickname = sig22_02_BOTTOM_habitat19
pos = 0, -650, 950
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = sig22_02

;DOCK BLOCK


[Object]
nickname = sig22_02_DOCK_cntrl_twr01
pos = 0, 150, 435
rotate = 180, 45, 0
archetype = space_control_tower
parent = sig22_02

[Object]
nickname = sig22_02_DOCK_cntrl_twr02
pos = 0, -150, 435
rotate = 0, 0, 0
archetype = space_control_tower
parent = sig22_02

[Object]
nickname = sig22_02_DOCK_industrial01
pos = 0, 0, 435
rotate = 90, 0, 0
archetype = space_industriala
parent = sig22_02

[Object]
nickname = sig22_02_DOCK_industrial02
pos = 150, 0, 348
rotate = 90, 30, 0
archetype = space_industrial02a
parent = sig22_02

[Object]
nickname = sig22_02_DOCK_industrial03
pos = -150, 0, 349
rotate = 90, 60, 0
archetype = space_industrial02a
parent = sig22_02

[Object]
nickname = sig22_02_DOCK_industrial04
pos = -150, 0, 522
rotate = 90, 30, 0
archetype = space_industrial02a
parent = sig22_02

[Object]
nickname = sig22_02_DOCK_industrial05
pos = 150, 0, 521
rotate = 90, 60, 0
archetype = space_industrial02a
parent = sig22_02

[Object]
nickname = sig22_02_DOCK_girder01
pos = 0, 0, 230
rotate = 0, 0, 0
archetype = space_girder
parent = sig22_02

;DOME AND HILL BLOCK


[Object]
nickname = sig22_02_DOME_cntrl_twr01
pos = -446, 150, 1207
rotate = 180, 45, 0
archetype = space_control_tower
parent = sig22_02

[Object]
nickname = sig22_02_DOME_cntrl_twr02
pos = -446, -150, 1207
rotate = 0, 0, 0
archetype = space_control_tower
parent = sig22_02

[Object]
nickname = sig22_02_DOME_cntrl_twr03
pos = -446, 0, 1207
rotate = 0, 0, 0
archetype = space_control_tower
parent = sig22_02

[Object]
nickname = sig22_02_DOME_industrial01
pos = -446, 0, 1207
rotate = 90, 0, 0
archetype = space_industriala
parent = sig22_02

[Object]
nickname = sig22_02_DOME_habitat01
pos = -296, 75, 1120
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_DOME_habitat02
pos = -596, 75, 1121
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_DOME_habitat03
pos = -446, 75, 1377
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_DOME_habitat04
pos = -596, 75, 1297
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_DOME_habitat05
pos = -296, 75, 1293
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_DOME_habitat06
pos = -446, 75, 1037
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_DOME_habitat07
pos = -296, -75, 1120
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_DOME_habitat08
pos = -596, -75, 1121
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_DOME_habitat09
pos = -446, -75, 1377
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_DOME_habitat10
pos = -596, -75, 1297
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_DOME_habitat11
pos = -296, -75, 1293
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_DOME_habitat12
pos = -446, -75, 1037
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig22_02

[Object]
nickname = sig22_02_DOME_dome01
pos = -127, 180, 1392
rotate = 0, 240, 0
archetype = space_dome
parent = sig22_02

[Object]
nickname = sig22_02_DOME_dome02
pos = -446, 30, 837
rotate = 0, 0, 0
archetype = space_dome
parent = sig22_02

[Object]
nickname = sig22_02_DOME_dome03
pos = -765, 30, 1392
rotate = 0, 120, 0
archetype = space_dome
parent = sig22_02

[Object]
nickname = sig22_02_DOME_dome04
pos = -767, -120, 1023
rotate = 0, 60, 0
archetype = space_dome
parent = sig22_02

[Object]
nickname = sig22_02_DOME_dome05
pos = -446, -120, 1576
rotate = 0, 180, 0
archetype = space_dome
parent = sig22_02

;STORE AND SHIPYARD BLOCK

[Object]
nickname = sig22_02_STORE_cntrl_twr01
pos = 446, 150, 1207
rotate = 180, 45, 0
archetype = space_control_tower
parent = sig22_02

[Object]
nickname = sig22_02_STORE_cntrl_twr02
pos = 446, 0, 1207
rotate = 0, 0, 0
archetype = space_control_tower
parent = sig22_02

[Object]
nickname = sig22_02_STORE_cntrl_twr03
pos = 446, -150, 1207
rotate = 0, 0, 0
archetype = space_control_tower
parent = sig22_02

[Object]
nickname = sig22_02_STORE_industrial01
pos = 446, 0, 1207
rotate = 90, 60, 0
archetype = space_industriala
parent = sig22_02

[Object]
nickname = sig22_02_STORE_tanks01
pos = 596, 75, 1120
rotate = 90, 30, 0
archetype = space_tanks4x4
parent = sig22_02

[Object]
nickname = sig22_02_STORE_tanks02
pos = 296, 75, 1121
rotate = 90, -30, 0
archetype = space_tanks4x4
parent = sig22_02

[Object]
nickname = sig22_02_STORE_tanks03
pos = 446, 75, 1377
rotate = 90, 90, 0
archetype = space_tanks4x4
parent = sig22_02

[Object]
nickname = sig22_02_STORE_tanks04
pos = 296, 75, 1297
rotate = 90, 30, 0
archetype = space_tanks4x4
parent = sig22_02

[Object]
nickname = sig22_02_STORE_tanks05
pos = 596, 75, 1293
rotate = 90, -30, 0
archetype = space_tanks4x4
parent = sig22_02

[Object]
nickname = sig22_02_STORE_tanks06
pos = 446, 75, 1037
rotate = 90, 90, 0
archetype = space_tanks4x4
parent = sig22_02

[Object]
nickname = sig22_02_STORE_tanks07
pos = 596, -75, 1120
rotate = 90, 30, 0
archetype = space_tanks4x4
parent = sig22_02

[Object]
nickname = sig22_02_STORE_tanks08
pos = 296, -75, 1121
rotate = 90, -30, 0
archetype = space_tanks4x4
parent = sig22_02

[Object]
nickname = sig22_02_STORE_tanks09
pos = 446, -75, 1377
rotate = 90, 90, 0
archetype = space_tanks4x4
parent = sig22_02

[Object]
nickname = sig22_02_STORE_tanks10
pos = 296, -75, 1297
rotate = 90, 30, 0
archetype = space_tanks4x4
parent = sig22_02

[Object]
nickname = sig22_02_STORE_tanks11
pos = 596, -75, 1293
rotate = 90, -30, 0
archetype = space_tanks4x4
parent = sig22_02

[Object]
nickname = sig22_02_STORE_tanks12
pos = 446, -75, 1037
rotate = 90, 90, 0
archetype = space_tanks4x4
parent = sig22_02

[Object]
nickname = sig22_02_STORE_shipyard01
pos = 742, 0, 1036
rotate = 90, 300, 0
archetype = shipyard
parent = sig22_02

[Object]
nickname = sig22_02_STORE_shipyard02
pos = 446, 0, 1546
rotate = 90, 180, 0
archetype = shipyard
parent = sig22_02
'''
