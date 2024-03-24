from templates.space_object_template import SpaceObjectTemplate


class PortRoyal(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'omicron1_01'
    TEMPLATE = '''[Object]
nickname = omicron1_01
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_police01
{dock_props}

[Object]
nickname = omicron1_01_ind01
pos = 0, -584, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = omicron1_01

[Object]
nickname = omicron1_01_ind02
pos = 72.5, -434, 460
rotate = 0, 0, 0
archetype = space_industrial02a
parent = omicron1_01

[Object]
nickname = omicron1_01_ind03
pos = -72.5, -434, 460
rotate = 0, 0, 0
archetype = space_industrial02a
parent = omicron1_01

[Object]
nickname = omicron1_01_ind04
pos = 217.5, -434, 460
rotate = 0, 0, 0
archetype = space_industrial02a
parent = omicron1_01

[Object]
nickname = omicron1_01_ind05
pos = -217.5, -434, 460
rotate = 0, 0, 0
archetype = space_industrial02a
parent = omicron1_01

[Object]
nickname = omicron1_01_ind06
pos = 217.5, -224, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = omicron1_01

[Object]
nickname = omicron1_01_ind07
pos = -217.5, -224, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = omicron1_01

[Object]
nickname = omicron1_01_ind08
pos = 72.5, -434, -460
rotate = 0, 0, 0
archetype = space_industrial02a
parent = omicron1_01

[Object]
nickname = omicron1_01_ind09
pos = -72.5, -434, -460
rotate = 0, 0, 0
archetype = space_industrial02a
parent = omicron1_01

[Object]
nickname = omicron1_01_ind10
pos = -217.5, -434, -460
rotate = 0, 0, 0
archetype = space_industrial02a
parent = omicron1_01

[Object]
nickname = omicron1_01_ind11
pos = 217.5, -434, -460
rotate = 0, 0, 0
archetype = space_industrial02a
parent = omicron1_01

[Object]
nickname = omicron1_01_ind12
pos = 0, -354, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = omicron1_01

[Object]
nickname = omicron1_01_girder01
pos = 72.5, -434, 330
rotate = 45, 180, 0
archetype = space_girdera
parent = omicron1_01

[Object]
nickname = omicron1_01_girder02
pos = -72.5, -434, 330
rotate = 45, 180, 0
archetype = space_girdera
parent = omicron1_01

[Object]
nickname = omicron1_01_girder03
pos = 217.5, -434, 330
rotate = -45, 180, 0
archetype = space_girdera
parent = omicron1_01

[Object]
nickname = omicron1_01_girder04
pos = -217.5, -434, 330
rotate = -45, 180, 0
archetype = space_girdera
parent = omicron1_01

[Object]
nickname = omicron1_01_girder05
pos = 72.5, -434, -330
rotate = 45, 0, 0
archetype = space_girdera
parent = omicron1_01

[Object]
nickname = omicron1_01_girder06
pos = -72.5, -434, -330
rotate = 45, 0, 0
archetype = space_girdera
parent = omicron1_01

[Object]
nickname = omicron1_01_girder07
pos = 217.5, -434, -330
rotate = -45, 0, 0
archetype = space_girdera
parent = omicron1_01

[Object]
nickname = omicron1_01_girder08
pos = -217.5, -434, -330
rotate = -45, 0, 0
archetype = space_girdera
parent = omicron1_01

[Object]
nickname = omicron1_01_girder09
pos = 127.5, -744, 0
rotate = -30, -90, 0
archetype = space_girderc
parent = omicron1_01

[Object]
nickname = omicron1_01_girder10
pos = -127.5, -744, 0
rotate = -30, 90, 0
archetype = space_girderc
parent = omicron1_01

[Object]
nickname = omicron1_01_dome01
pos = 249.5, -484, 0
rotate = 0, -90, -90
archetype = space_dome
parent = omicron1_01

[Object]
nickname = omicron1_01_dome02
pos = 249.5, -784, 0
rotate = 0, -90, -90
archetype = space_dome
parent = omicron1_01

[Object]
nickname = omicron1_01_dome03
pos = -248.5, -484, 0
rotate = 0, 90, 90
archetype = space_dome
parent = omicron1_01

[Object]
nickname = omicron1_01_dome04
pos = -248.5, -784, 0
rotate = 0, 90, 90
archetype = space_dome
parent = omicron1_01

[Object]
nickname = omicron1_01_ctrl_twr01
pos = 0, -224, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = omicron1_01

[Object]
nickname = omicron1_01_ctrl_twr02
pos = 0, -684, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = omicron1_01

[Object]
nickname = omicron1_01_ctrl_twr03
pos = 0, -484, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = omicron1_01

[Object]
nickname = omicron1_01_ctrl_twr04
pos = 0, -914, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = omicron1_01

[Object]
nickname = omicron1_01_ctrl_twr05
pos = 0, -849, 0
rotate = 180, 0, 0
archetype = space_small_control_tower
parent = omicron1_01

[Object]
nickname = omicron1_01_ctrl_twr06
pos = 0, -119, 0
rotate = 180, 90, 0
archetype = space_small_control_tower
parent = omicron1_01

[Object]
nickname = omicron1_01_habitat01
pos = 0, -284, 110
rotate = 45, 0, 0
archetype = space_habitat_wide
parent = omicron1_01

[Object]
nickname = omicron1_01_habitat02
pos = 0, -284, -110
rotate = -45, 0, 0
archetype = space_habitat_wide
parent = omicron1_01

[Object]
nickname = omicron1_01_habitat03
pos = -110, -284, 0
rotate = 0, 0, 45
archetype = space_habitat_wide
parent = omicron1_01

[Object]
nickname = omicron1_01_habitat04
pos = 110, -284, 0
rotate = 0, 0, -45
archetype = space_habitat_wide
parent = omicron1_01

[Object]
nickname = omicron1_01_habitat05
pos = 0, -424, 110
rotate = -45, 0, 0
archetype = space_habitat_wide
parent = omicron1_01

[Object]
nickname = omicron1_01_habitat06
pos = 0, -424, -110
rotate = 45, 0, 0
archetype = space_habitat_wide
parent = omicron1_01

[Object]
nickname = omicron1_01_habitat07
pos = -110, -424, 0
rotate = 0, 0, -45
archetype = space_habitat_wide
parent = omicron1_01

[Object]
nickname = omicron1_01_habitat08
pos = 110, -424, 0
rotate = 0, 0, 45
archetype = space_habitat_wide
parent = omicron1_01

[Object]
nickname = omicron1_01_habitat09
pos = 0, -754, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = omicron1_01

[Object]
nickname = omicron1_01_habitat10
pos = 0, -119, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = omicron1_01
'''


class ChurchAlive(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'omicron1_01'
    TEMPLATE = '''[Object]
nickname = omicron1_02
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_shipping01
{dock_props}

[Object]
nickname = omicron1_02_ind01
pos = 1530, 0, 0
rotate = 0, 0, 0
archetype = space_industrial01a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind02
pos = 1480, 0, -200
rotate = 0, 30, 0
archetype = space_industrial01a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind03
pos = 1330, 0, -350
rotate = 0, 60, 0
archetype = space_industrial01a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind04
pos = 1130, 0, -400
rotate = 0, 90, 0
archetype = space_industrial01a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind05
pos = 930, 0, -350
rotate = 0, -60, 0
archetype = space_industrial01a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind06
pos = 780, 0, -200
rotate = 0, -30, 0
archetype = space_industrial01a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind07
pos = 730, 0, 0
rotate = 0, 0, 0
archetype = space_industrial01a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind08
pos = 1480, 0, 200
rotate = 0, -30, 0
archetype = space_industrial01a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind09
pos = 1330, 0, 350
rotate = 0, -60, 0
archetype = space_industrial01a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind10
pos = 1130, 0, 400
rotate = 0, 90, 0
archetype = space_industrial01a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind11
pos = 930, 0, 350
rotate = 0, 60, 0
archetype = space_industrial01a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind12
pos = 780, 0, 200
rotate = 0, 30, 0
archetype = space_industrial01a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind13
pos = 1380, 0, -58
rotate = 0, 90, 0
archetype = space_industrial02a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind14
pos = 1380, 0, 58
rotate = 0, 90, 0
archetype = space_industrial02a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind15
pos = 880, 0, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = omicron1_02

[Object]
nickname = omicron1_02_ind16
pos = 1130, 0, -250
rotate = 0, 0, 0
archetype = space_industriala
parent = omicron1_02

[Object]
nickname = omicron1_02_ind17
pos = 1130, 0, 250
rotate = 0, 0, 0
archetype = space_industriala
parent = omicron1_02

[Object]
nickname = omicron1_02_tanks04
pos = 1130, 0, 600
rotate = 0, 0, 90
archetype = space_tankl4x4
parent = omicron1_02

[Object]
nickname = omicron1_02_tanks05
pos = 1130, 0, -600
rotate = 0, 0, 90
archetype = space_tankl4x4
parent = omicron1_02

[Object]
nickname = omicron1_02_tanks06
pos = 1730, 0, 0
rotate = 90, 0, 90
archetype = space_tankl4x4
parent = omicron1_02

[Object]
nickname = omicron1_02_habitat01
pos = 1130, 0, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = omicron1_02

[Object]
nickname = omicron1_02_habitat02
pos = 1230, 0, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = omicron1_02

[Object]
nickname = omicron1_02_habitat03
pos = 1030, 0, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = omicron1_02

[Object]
nickname = omicron1_02_habitat04
pos = 1130, 0, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = omicron1_02

[Object]
nickname = omicron1_02_habitat05
pos = 1130, 0, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = omicron1_02

[Object]
nickname = omicron1_02_habitat06
pos = 1060, 0, 70
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = omicron1_02

[Object]
nickname = omicron1_02_habitat07
pos = 1200, 0, 70
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = omicron1_02

[Object]
nickname = omicron1_02_habitat08
pos = 1060, 0, -70
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = omicron1_02

[Object]
nickname = omicron1_02_habitat09
pos = 1200, 0, -70
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = omicron1_02

[Object]
nickname = omicron1_02_control01
pos = 1500, 40, 0
rotate = 0, 90, 0
archetype = space_control_block

[Object]
nickname = omicron1_02_control02
pos = 1130, 0, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = omicron1_02

[Object]
nickname = omicron1_02_control03
pos = 1130, 85, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = omicron1_02

[Object]
nickname = omicron1_02_control04
pos = 1130, -85, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = omicron1_02
'''


class ChurchDestroyed(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'omicron1_02'
    TEMPLATE = '''[Object]
nickname = omicron1_02
pos = 0, 0, 0
rotate = -2, 0, 0
archetype = space_control_tower_root
{dock_props}

[Object]
nickname = omicron1_02_ind01
pos = 400, 110, -20
rotate = -10, 0, 0
archetype = space_industrial01a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind02
pos = 350, 20, -180
rotate = -40, 40, 0
archetype = space_industrial01a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind06
pos = -360, -50, -200
rotate = -15, -20, 0
archetype = space_industrial01a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind07
pos = -400, 0, 0
rotate = -10, 0, 0
archetype = space_industrial01a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind08
pos = 350, 100, 200
rotate = 10, -30, 0
archetype = space_industrial01a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind09
pos = 200, 60, 350
rotate = 10, -60, 0
archetype = space_industrial01a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind10
pos = 0, 70, 400
rotate = 10, 90, 0
archetype = space_industrial01a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind11
pos = -200, 40, 350
rotate = -30, 60, 0
archetype = space_industrial01a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind12
pos = -350, 0, 200
rotate = 10, 30, 0
archetype = space_industrial01a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind13
pos = 250, 50, -38
rotate = 110, 5, 110
archetype = space_industrial02a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind14
pos = 250, 50, 58
rotate = -20, 90, 5
archetype = space_industrial02a
parent = omicron1_02

[Object]
nickname = omicron1_02_ind15
pos = -250, 0, 10
rotate = 2,86, 0
archetype = space_industriala
parent = omicron1_02

[Object]
nickname = omicron1_02_ind16
pos = -50, -20, -250
rotate = -8, 20, 0
archetype = space_industrial_dmg
parent = omicron1_02

[Object]
nickname = omicron1_02_ind17
pos = 0, 40, 250
rotate = -15, 0, 0
archetype = space_industriala
parent = omicron1_02

[Object]
nickname = omicron1_02_tanks01
pos = -600, 0, 0
rotate = 90, 10, 90
archetype = space_tankl4x4
parent = omicron1_02

[Object]
nickname = omicron1_02_tanks02
pos = -865, 0, -15
rotate = 90, 5, 90
archetype = space_tankl4x4_dmg
parent = omicron1_02

[Object]
nickname = omicron1_02_tanks03
pos = -1127, -4, -29
rotate = 90, 15, -90
archetype = space_tankl4_dmg
parent = omicron1_02

[Object]
nickname = omicron1_02_tanks04
pos = 0, 180, 650
rotate = 0, 20, 90
archetype = space_tankl4x4_dmg
parent = omicron1_02

[Object]
nickname = omicron1_02_tanks05
pos = 0, 0, -750
rotate = 90, -45, 0
archetype = space_tankl_2dmg
parent = omicron1_02

[Object]
nickname = omicron1_02_tanks06
pos = 600, 80, 0
rotate = 90, 0, 70
archetype = space_tankl4_dmg
parent = omicron1_02

[Object]
nickname = omicron1_02_habitat01
pos = 0, 0, 0
rotate = 3, 3, 3
archetype = space_habitat_dmg
parent = omicron1_02

[Object]
nickname = omicron1_02_habitat02
pos = 100, 0, 0
rotate = 20, 0, 0
archetype = space_habitat_dmg
parent = omicron1_02

[Object]
nickname = omicron1_02_habitat03
pos = -100, 0, 0
rotate = 10, 0, 0
archetype = space_habitat_dmg
parent = omicron1_02

[Object]
nickname = omicron1_02_habitat04
pos = 0, 0, 100
rotate = 10, 0, -10
archetype = space_habitat_dmg
parent = omicron1_02

[Object]
nickname = omicron1_02_habitat05
pos = 0, 0, -100
rotate = 5, 0, 10
archetype = space_habitat_dmg
parent = omicron1_02

[Object]
nickname = omicron1_02_habitat06
pos = -70, 0, 70
rotate = 0, 0, 10
archetype = space_habitat_dmg
parent = omicron1_02

[Object]
nickname = omicron1_02_habitat07
pos = 70, 0, 70
rotate = -5, 0, 0
archetype = space_habitat_dmg
parent = omicron1_02

[Object]
nickname = omicron1_02_habitat08
pos = -70, 0, -70
rotate = 5, 0, 0
archetype = space_habitat_dmg
parent = omicron1_02

[Object]
nickname = omicron1_02_habitat09
pos = 70, 0, -70
rotate = 0, 50, 0
archetype = space_habitat_dmg
parent = omicron1_02

[Object]
nickname = omicron1_02_control01
pos = 280, 40, 0
rotate = 70, 85, 90
archetype = space_control_block
parent = omicron1_02

[Object]
nickname = omicron1_02_control03
pos = 0, 85, 15
rotate = -5, 0, 0
archetype = space_medium_control_tower
parent = omicron1_02

[Object]
nickname = omicron1_02_control04
pos = 0, -130, 0
rotate = 10, 0, 0
archetype = space_medium_control_tower
parent = omicron1_02
'''


class TauFreeport(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'tau31_04'
    TEMPLATE = '''[Object]
nickname = tau31_04
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_police01
{dock_props}

[Object]
nickname = tau31_04_indA01
pos = 0, -530, 200
rotate = 0, -90, 0
archetype = space_industriala
loadout = space_ind_girder_one_side1
parent = tau31_04

[Object]
nickname = tau31_04_indA02
pos = -250, -530, 200
rotate = 0, -90, 0
archetype = space_industriala
loadout = space_ind_girder_one_side1
parent = tau31_04

[Object]
nickname = tau31_04_indA03
pos = 250, -530, 200
rotate = 0, -90, 0
archetype = space_industriala
loadout = space_ind_girder_one_side1
parent = tau31_04

[Object]
nickname = tau31_04_indA04
pos = 0, -530, -200
rotate = 0, 90, 0
archetype = space_industriala
loadout = space_ind_girder_one_side1
parent = tau31_04

[Object]
nickname = tau31_04_indA05
pos = -250, -530, -200
rotate = 0, 90, 0
archetype = space_industriala
loadout = space_ind_girder_one_side1
parent = tau31_04

[Object]
nickname = tau31_04_indA06
pos = 250, -530, -200
rotate = 0, 90, 0
archetype = space_industriala
loadout = space_ind_girder_one_side1
parent = tau31_04

[Object]
nickname = tau31_04_indB01
pos = 0, -530, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = tau31_04

[Object]
nickname = tau31_04_dome01
pos = -650, -498, 200
rotate = 0, 90, 0
archetype = space_dome
loadout = space_ind_girder_one_side1
parent = tau31_04

[Object]
nickname = tau31_04_dome02
pos = -650, -498, -200
rotate = 0, 90, 0
archetype = space_dome
loadout = space_ind_girder_one_side1
parent = tau31_04

[Object]
nickname = tau31_04_dome03
pos = 650, -498, 200
rotate = 0, -90, 0
archetype = space_dome
loadout = space_ind_girder_one_side1
parent = tau31_04

[Object]
nickname = tau31_04_dome04
pos = 650, -498, -200
rotate = 0, -90, 0
archetype = space_dome
loadout = space_ind_girder_one_side1
parent = tau31_04

[Object]
nickname = tau31_04_control_tower01
pos = 0, -482, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = tau31_04

[Object]
nickname = tau31_04_control_tower02
pos = 0, -578, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = tau31_04

[Object]
nickname = tau31_04_control_tower03
pos = 0, -820, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = tau31_04

[Object]
nickname = tau31_04_control_tower04
pos = 0, -240, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = tau31_04

[Object]
nickname = tau31_04_gider01
pos = -60, -530, -7
rotate = 0, -52, 0
archetype = space_girdera
parent = tau31_04

[Object]
nickname = tau31_04_gider02
pos = 60, -530, -7
rotate = 0, 52, 0
archetype = space_girdera
parent = tau31_04

[Object]
nickname = tau31_04_gider03
pos = -60, -530, 7
rotate = 0, -128, 0
archetype = space_girdera
parent = tau31_04

[Object]
nickname = tau31_04_gider04
pos = 60, -530, 7
rotate = 0, 128, 0
archetype = space_girdera
parent = tau31_04

[Object]
nickname = tau31_04_gider05
pos = 0, -120, 0
rotate = -90, 0, 0
archetype = space_girderc
parent = tau31_04

[Object]
nickname = tau31_04_habitat01
pos = 0, -428, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau31_04

[Object]
nickname = tau31_04_habitat02
pos = 0, -290, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau31_04

[Object]
nickname = tau31_04_habitat03
pos = 0, -395, 40
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = tau31_04

[Object]
nickname = tau31_04_habitat04
pos = 0, -395, -40
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = tau31_04

[Object]
nickname = tau31_04_habitat05
pos = 0, -632, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau31_04

[Object]
nickname = tau31_04_habitat06
pos = 0, -770, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau31_04

[Object]
nickname = tau31_04_habitat07
pos = 0, -665, 40
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = tau31_04

[Object]
nickname = tau31_04_habitat08
pos = 0, -665, -40
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = tau31_04

[Object]
nickname = tau31_04_tank01
pos = 0, -982, 0
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = tau31_04

[Object]
nickname = tau31_04_tank02
pos = -1, -1170, 1
rotate = 0, 0, 0
archetype = space_tanklx4
parent = tau31_04
'''
