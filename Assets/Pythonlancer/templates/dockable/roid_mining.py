from templates.space_object_template import SpaceObjectTemplate


class BretoniaRoidMining(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'tau37_01'
    TEMPLATE = '''[Object]
nickname = tau37_01
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = space_shipping01
{dock_props}

[Object]
nickname = tau37_01_research01
pos = -926, -323, 0
rotate = 0, 0, 0
archetype = space_research
parent = tau37_01

[Object]
nickname = tau37_01_industrial01
pos = -926, -323, 350
rotate = 0, -90, 0
archetype = space_industrial
parent = tau37_01

[Object]
nickname = tau37_01_industrial02
pos = -926, -323, 900
rotate = 0, -90, 0
archetype = space_industrial
parent = tau37_01

[Object]
nickname = tau37_01_industrial03
pos = -926, -323, 1450
rotate = 0, -90, 0
archetype = space_industrial
parent = tau37_01

[Object]
nickname = tau37_01_industrial04
pos = -576, -323, 350
rotate = 90, 0, 0
archetype = space_industrial02a
parent = tau37_01

[Object]
nickname = tau37_01_industrial05
pos = -596, -323, 900
rotate = 90, 0, 0
archetype = space_industrial02a
parent = tau37_01

[Object]
nickname = tau37_01_industrial06
pos = -616, -323, 1450
rotate = 90, 0, 0
archetype = space_industrial02a
parent = tau37_01

[Object]
nickname = tau37_01_girder01
pos = -776, -323, 350
rotate = 0, 90, 0
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder02
pos = -776, -323, 900
rotate = 0, 90, 0
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder03
pos = -776, -323, 1450
rotate = 0, 90, 0
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder04
pos = -798, -133, 0
rotate = -45, 90, 0
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder05
pos = -641, -73, 0
rotate = 90, 0, 0
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder06
pos = -786, -503, 0
rotate = 40, 90, 0
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder07
pos = -841, -323, 0
rotate = 0, 90, 0
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder08
pos = -641, -443, 0
rotate = 90, 0, 0
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder09
pos = 561, -473, 0
rotate = 90, 0, 0
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder10
pos = -276, -323, 0
rotate = 90, 45, 90
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder11
pos = -276, -625, 0
rotate = 90, 45, 90
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder12
pos = 174, -323, 0
rotate = 90, 45, 90
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder13
pos = 174, -625, 0
rotate = 90, 45, 90
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_shipyard01
pos = -436, -323, 350
rotate = 90, 90, 0
archetype = shipyard
parent = tau37_01

[Object]
nickname = tau37_01_shipyard02
pos = -456, -323, 900
rotate = 90, 90, 0
archetype = shipyard
parent = tau37_01

[Object]
nickname = tau37_01_shipyard03
pos = -476, -323, 1450
rotate = 90, 90, 0
archetype = shipyard
parent = tau37_01

[Object]
nickname = tau37_01_solar_plant01
pos = -1376, -323, 350
rotate = 0, 0, 0
archetype = space_solar_plant
parent = tau37_01
spin = 0.1, 0, 0

[Object]
nickname = tau37_01_solar_plant02
pos = -1396, -323, 900
rotate = 0, 0, 0
archetype = space_solar_plant
parent = tau37_01
spin = 0.1, 0, 0

[Object]
nickname = tau37_01_solar_plant03
pos = -1416, -323, 1450
rotate = 0, 0, 0
archetype = space_solar_plant
parent = tau37_01
spin = 0.1, 0, 0

[Object]
nickname = tau37_01_tanks01
pos = -561, -625, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks02
pos = -430, -625, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks03
pos = 26, -625, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks04
pos = 350, -625, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks05
pos = 481, -625, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks06
pos = -561, -323, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks07
pos = -430, -323, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks08
pos = 26, -323, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks09
pos = 350, -323, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks10
pos = 481, -323, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks11
pos = -106, -323, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks12
pos = -106, -625, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA01
pos = -561, -625, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA02
pos = -430, -625, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA03
pos = 26, -625, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA04
pos = 350, -625, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA05
pos = 481, -625, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA06
pos = -561, -323, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA07
pos = -430, -323, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA08
pos = 26, -323, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA09
pos = 350, -323, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA10
pos = 481, -323, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA11
pos = -106, -323, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA12
pos = -106, -625, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_habitat01
pos = -926, -93, 350
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = tau37_01

[Object]
nickname = tau37_01_habitat02
pos = -926, -3, 900
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = tau37_01

[Object]
nickname = tau37_01_habitat03
pos = -926, -118, 1450
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = tau37_01

[Object]
nickname = tau37_01_habitat04
pos = -926, -181, 350
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau37_01

[Object]
nickname = tau37_01_habitat05
pos = -926, -181, 900
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau37_01

[Object]
nickname = tau37_01_habitat06
pos = -926, -553, 350
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = tau37_01

[Object]
nickname = tau37_01_habitat07
pos = -926, -643, 900
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = tau37_01

[Object]
nickname = tau37_01_habitat08
pos = -926, -528, 1450
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = tau37_01

[Object]
nickname = tau37_01_habitat09
pos = -926, -465, 350
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = tau37_01

[Object]
nickname = tau37_01_habitat10
pos = -926, -465, 900
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = tau37_01
'''


class RheinlandRoidMining(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'om15_01'
    TEMPLATE = '''[Object]
nickname = om15_01
pos = 0, 0, 0
rotate = 0,180, 0
archetype = space_shipping01
{dock_props}

[Object]
nickname = om15_01_research01
pos = -1035, -300, 0
rotate = 0, 0, 0
archetype = space_research
parent = om15_01

[Object]
nickname = om15_01_research02
pos = -735, -300, 0
rotate = 0, 0, 0
archetype = space_research
parent = om15_01

[Object]
nickname = om15_01_research03
pos = -735, 0, 0
rotate = 0, 0, 0
archetype = space_research
parent = om15_01

[Object]
nickname = om15_01_girder01
pos = -885, -300, 0
rotate = 0, 90, 0
archetype = space_girder
parent = om15_01

[Object]
nickname = om15_01_girder02
pos = -735, -150, 0
rotate = 90, 0, 0
archetype = space_girder
parent = om15_01

[Object]
nickname = om15_01_girder03
pos = -915, -120, 0
rotate = 90, 0, -45
archetype = space_girder
parent = om15_01

[Object]
nickname = om15_01_girder04
pos = -885, -300, 1800
rotate = 0, 90, 0
archetype = space_girder
parent = om15_01

[Object]
nickname = om15_01_girder05
pos = -735, -150, 1800
rotate = 90, 0, 0
archetype = space_girder
parent = om15_01

[Object]
nickname = om15_01_girder06
pos = -915, -120, 1800
rotate = 90, 0, -45
archetype = space_girder
parent = om15_01

[Object]
nickname = om15_01_industrial01
pos = -315, -300, 0
rotate = 0, -90, 0
archetype = space_industrial
parent = om15_01

[Object]
nickname = om15_01_industrial02
pos = 35, -300, 0
rotate = 0, -90, 0
archetype = space_industrial
parent = om15_01

[Object]
nickname = om15_01_industrial03
pos = 385, -300, 0
rotate = 0, -90, 0
archetype = space_industrial
parent = om15_01

[Object]
nickname = om15_01_tankl_01
pos = -315, -300, 200
rotate = 0, 0, 0
archetype = space_tankl4
parent = om15_01

[Object]
nickname = om15_01_tankl_02
pos = -315, -300, -200
rotate = 0, 0, 0
archetype = space_tankl4
parent = om15_01

[Object]
nickname = om15_01_tankl_03
pos = 385, -300, 200
rotate = 0, 0, 0
archetype = space_tankl4
parent = om15_01

[Object]
nickname = om15_01_tankl_04
pos = 35, -300, -200
rotate = 0, 0, 0
archetype = space_tankl4
parent = om15_01

[Object]
nickname = om15_01_tankl_05
pos = 35, -300, 200
rotate = 0, 0, 0
archetype = space_tankl4
parent = om15_01

[Object]
nickname = om15_01_tankl_06
pos = 385, -300, -200
rotate = 0, 0, 0
archetype = space_tankl4
parent = om15_01

[Object]
nickname = om15_01_industrial04
pos = -1155, 0, 0
rotate = 0, 90, 0
archetype = space_industrial02
parent = om15_01

[Object]
nickname = om15_01_industrial05
pos = -1155, 0, 1800
rotate = 0, 90, 0
archetype = space_industrial02
parent = om15_01

[Object]
nickname = om15_01_space_dome01
pos = -1155, 30, 350
rotate = 0, 180, 0
archetype = space_dome
parent = om15_01

[Object]
nickname = om15_01_space_dome02
pos = -1155, 30, 1450
rotate = 0, 0, 0
archetype = space_dome
parent = om15_01

[Object]
nickname = om15_01_habitat01
pos = -1155, 350, 0
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = om15_01

[Object]
nickname = om15_01_habitat02
pos = -1155, 230, 1800
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = om15_01

[Object]
nickname = om15_01_habitat03
pos = -1155, 140, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = om15_01

[Object]
nickname = om15_01_habitat04
pos = -1155, -140, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = om15_01

[Object]
nickname = om15_01_habitat05
pos = -1155, 140, 1800
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = om15_01

[Object]
nickname = om15_01_habitat06
pos = -1155, -140, 1800
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = om15_01

[Object]
nickname = om15_01_habitat07
pos = -1155, -1, 1250
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = om15_01

[Object]
nickname = om15_01_habitat08
pos = -1155, -0.5, 555
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = om15_01

[Object]
nickname = om15_01_habitat09
pos = -1155, -0.5, 900
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = om15_01

[Object]
nickname = om15_01_girder07
pos = -1155, -1, 1050
rotate = 0, 0, 0
archetype = space_girder
parent = om15_01

[Object]
nickname = om15_01_girder08
pos = -1155, -0.5, 700
rotate = 0, 0, 0
archetype = space_girder
parent = om15_01

[Object]
nickname = om15_01_shipyard01
pos = -925, -465, 1500
rotate = 0, -90, 0
archetype = shipyard
parent = om15_01

[Object]
nickname = om15_01_shipyard02
pos = -925, -465, 1000
rotate = 0, -90, 0
archetype = shipyard
parent = om15_01

[Object]
nickname = om15_01_shipyard03
pos = -925, -465, 500
rotate = 0, -90, 0
archetype = shipyard
parent = om15_01

[Object]
nickname = om15_01_panel01
pos = -55, 35, 0
rotate = 0, 70, 0
archetype = space_solar_pnl
parent = om15_01

[Object]
nickname = om15_01_panel02
pos = 601, 35, 0
rotate = 0, 70, 0
archetype = space_solar_pnl
parent = om15_01
'''


class LibertyRoidMining(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_cal_05'
    TEMPLATE = '''[Object]
nickname = li_cal_05
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_mining01
{dock_props}

[Object]
nickname = li_cal_05_research01
pos = 220, -380, 373
rotate = 0, 0, 0
archetype = space_research
parent = li_cal_05

[Object]
nickname = li_cal_05_research02
pos = -220, -380, 373
rotate = 0, 0, 0
archetype = space_research
parent = li_cal_05

[Object]
nickname = li_cal_05_girder01
pos = 135, -235, 373
rotate = 45, 90, 0
archetype = space_girder
parent = li_cal_05

[Object]
nickname = li_cal_05_girder02
pos = -135, -235, 373
rotate = -45, 90, 0
archetype = space_girder
parent = li_cal_05

[Object]
nickname = li_cal_05_industrial01
pos = 650, -380, 373
rotate = 0, -90, 0
archetype = space_industrial
parent = li_cal_05

[Object]
nickname = li_cal_05_industrial02
pos = -650, -380, 373
rotate = 0, 90, 0
archetype = space_industrial
parent = li_cal_05

[Object]
nickname = li_cal_05_industrial03
pos = 650, -380, 2173
rotate = 0, -90, 0
archetype = space_industrial
parent = li_cal_05

[Object]
nickname = li_cal_05_industrial04
pos = -650, -380, 2173
rotate = 0, 90, 0
archetype = space_industrial
parent = li_cal_05

[Object]
nickname = li_cal_05_shipyard01
pos = 0, -550, 750
rotate = 0, 90, 0
archetype = shipyard
parent = li_cal_05

[Object]
nickname = li_cal_05_shipyard02
pos = 0, -550, 1300
rotate = 0, -90, 0
archetype = shipyard
parent = li_cal_05

[Object]
nickname = li_cal_05_shipyard03
pos = 0, -550, 1850
rotate = 0, 90, 0
archetype = shipyard
parent = li_cal_05

[Object]
nickname = li_cal_05_panel01
pos = -220, -360, 675
rotate = 0, 45, 0
archetype = space_solar_pnl
parent = li_cal_05

[Object]
nickname = li_cal_05_panel02
pos = 220, -360, 1075
rotate = 0, 45, 0
archetype = space_solar_pnl
parent = li_cal_05

[Object]
nickname = li_cal_05_panel03
pos = -220, -360, 1475
rotate = 0, 45, 0
archetype = space_solar_pnl
parent = li_cal_05

[Object]
nickname = li_cal_05_panel04
pos = 220, -360, 1875
rotate = 0, 45, 0
archetype = space_solar_pnl
parent = li_cal_05

[Object]
nickname = li_cal_05_tankl01
pos = 220, -360, 675
rotate = 180, 0, 0
archetype = space_tankl4
parent = li_cal_05

[Object]
nickname = li_cal_05_tankl02
pos = -220, -360, 1075
rotate = 180, 0, 0
archetype = space_tankl4
parent = li_cal_05

[Object]
nickname = li_cal_05_tankl03
pos = 220, -360, 1475
rotate = 180, 0, 0
archetype = space_tankl4
parent = li_cal_05

[Object]
nickname = li_cal_05_tankl04
pos = -220, -360, 1875
rotate = 180, 0, 0
archetype = space_tankl4
parent = li_cal_05

[Object]
nickname = li_cal_05_habitat01
pos = 650, -135, 373
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = li_cal_05

[Object]
nickname = li_cal_05_habitat02
pos = -650, -70, 373
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = li_cal_05

[Object]
nickname = li_cal_05_habitat03
pos = 650, -100, 2173
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = li_cal_05

[Object]
nickname = li_cal_05_habitat04
pos = -650, -160, 2173
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = li_cal_05

[Object]
nickname = li_cal_05_habitat05
pos = 650, -235, 373
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_05

[Object]
nickname = li_cal_05_habitat06
pos = -650, -235, 373
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_05

[Object]
nickname = li_cal_05_habitat07
pos = 650, -235, 2173
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_05

[Object]
nickname = li_cal_05_habitat08
pos = -650, -235, 2173
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_05
'''


class UpsilonRoidMining(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'up1_01'
    TEMPLATE = '''[Object]
nickname = up1_01
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_mining01
{dock_props}

[Object]
nickname = up1_01_ind01
pos = 880, -155, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = up1_01

[Object]
nickname = up1_01_girder01
pos = 627, 145, 0
rotate = 0, 90, 0
archetype = space_girder
parent = up1_01

[Object]
nickname = up1_01_girder02
pos = 1000, -155, 0
rotate = 0, 90, 0
archetype = space_girder
parent = up1_01

[Object]
nickname = up1_01_ctrl_block01
pos = 1250, -90, 0
rotate = 0, 90, 0
archetype = space_small_control_block
parent = up1_01

[Object]
nickname = up1_01_ctrl_twr01
pos = 1250, -155, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = up1_01

[Object]
nickname = up1_01_indA01
pos = 376, -156, -365
rotate = 0, 0, 0
archetype = space_industrial01a
parent = up1_01

[Object]
nickname = up1_01_indA02
pos = 376, -156, 365
rotate = 0, 180, 0
archetype = space_industrial01a
parent = up1_01

[Object]
nickname = up1_01_indA03
pos = 376, 145, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = up1_01

[Object]
nickname = up1_01_girderA01
pos = 376, -100, -377
rotate = -45, 0, 0
archetype = space_girdera
parent = up1_01

[Object]
nickname = up1_01_girderA02
pos = 376, -100, 377
rotate = -45, 180, 0
archetype = space_girdera
parent = up1_01

[Object]
nickname = up1_01_girderA03
pos = 376, -156, -200
rotate = 0, 0, 0
archetype = space_girder
parent = up1_01

[Object]
nickname = up1_01_girderA04
pos = 376, -156, 200
rotate = 0, 0, 0
archetype = space_girder
parent = up1_01

[Object]
nickname = up1_01_habitatA01
pos = 376, -290, 365
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up1_01

[Object]
nickname = up1_01_habitatA02
pos = 376, -290, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up1_01

[Object]
nickname = up1_01_habitatA03
pos = 376, -290, -365
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up1_01

[Object]
nickname = up1_01_habitatA04
pos = 376, -325, 365
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = up1_01

[Object]
nickname = up1_01_habitatA05
pos = 376, -345, -365
rotate = 180, 0, 0
archetype = space_small_control_block
parent = up1_01

[Object]
nickname = up1_01_panelA01
pos = 376, -300, 0
rotate = 180, 60, 0
archetype = space_solar_pnl
parent = up1_01

[Object]
nickname = up1_01_shipyardA01
pos = 376, 280, 0
rotate = 0, 0, 0
archetype = shipyard
parent = up1_01

[Object]
nickname = up1_01_tanksA01
pos = 376, -43, 0
rotate = 90, 0, 0
archetype = space_tanks4x4
parent = up1_01

[Object]
nickname = up1_01_tanksA02
pos = 376, 55, 0
rotate = 90, 0, 0
archetype = space_tanks2x2
parent = up1_01

[Object]
nickname = up1_01_indB01
pos = 627, -156, -365
rotate = 0, 0, 0
archetype = space_industrial01a
parent = up1_01

[Object]
nickname = up1_01_indB02
pos = 627, -156, 365
rotate = 0, 180, 0
archetype = space_industrial01a
parent = up1_01

[Object]
nickname = up1_01_indB03
pos = 627, 145, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = up1_01

[Object]
nickname = up1_01_girderB01
pos = 627, -100, -377
rotate = -45, 0, 0
archetype = space_girdera
parent = up1_01

[Object]
nickname = up1_01_girderB02
pos = 627, -100, 377
rotate = -45, 180, 0
archetype = space_girdera
parent = up1_01

[Object]
nickname = up1_01_girderB03
pos = 627, -156, -200
rotate = 0, 0, 0
archetype = space_girder
parent = up1_01

[Object]
nickname = up1_01_girderB04
pos = 627, -156, 200
rotate = 0, 0, 0
archetype = space_girder
parent = up1_01

[Object]
nickname = up1_01_habitatB01
pos = 627, -290, 365
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up1_01

[Object]
nickname = up1_01_habitatB02
pos = 627, -290, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up1_01

[Object]
nickname = up1_01_habitatB03
pos = 627, -290, -365
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up1_01

[Object]
nickname = up1_01_habitatB04
pos = 627, -325, 365
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = up1_01

[Object]
nickname = up1_01_habitatB05
pos = 627, -345, -365
rotate = 180, 0, 0
archetype = space_small_control_block
parent = up1_01

[Object]
nickname = up1_01_panelB01
pos = 627, -300, 0
rotate = 180, 60, 0
archetype = space_solar_pnl
parent = up1_01

[Object]
nickname = up1_01_shipyardB01
pos = 627, 280, 0
rotate = 0, 0, 0
archetype = shipyard
parent = up1_01

[Object]
nickname = up1_01_tanksB01
pos = 627, -43, 0
rotate = 90, 0, 0
archetype = space_tanks4x4
parent = up1_01

[Object]
nickname = up1_01_tanksB02
pos = 627, 55, 0
rotate = 90, 0, 0
archetype = space_tanks2x2
parent = up1_01

[Object]
nickname = up1_01_indC01
pos = 880, -156, -365
rotate = 0, 0, 0
archetype = space_industrial01a
parent = up1_01

[Object]
nickname = up1_01_indC02
pos = 880, -156, 365
rotate = 0, 180, 0
archetype = space_industrial01a
parent = up1_01

[Object]
nickname = up1_01_indC03
pos = 880, 145, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = up1_01

[Object]
nickname = up1_01_girderC01
pos = 880, -100, -377
rotate = -45, 0, 0
archetype = space_girdera
parent = up1_01

[Object]
nickname = up1_01_girderC02
pos = 880, -100, 377
rotate = -45, 180, 0
archetype = space_girdera
parent = up1_01

[Object]
nickname = up1_01_girderC03
pos = 880, -156, -200
rotate = 0, 0, 0
archetype = space_girder
parent = up1_01

[Object]
nickname = up1_01_girderC04
pos = 880, -156, 200
rotate = 0, 0, 0
archetype = space_girder
parent = up1_01

[Object]
nickname = up1_01_habitatC01
pos = 880, -290, 365
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up1_01

[Object]
nickname = up1_01_habitatC02
pos = 880, -290, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up1_01

[Object]
nickname = up1_01_habitatC03
pos = 880, -290, -365
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up1_01

[Object]
nickname = up1_01_habitatC04
pos = 880, -325, 365
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = up1_01

[Object]
nickname = up1_01_habitatC05
pos = 880, -345, -365
rotate = 180, 0, 0
archetype = space_small_control_block
parent = up1_01

[Object]
nickname = up1_01_panelC01
pos = 880, -300, 0
rotate = 180, 60, 0
archetype = space_solar_pnl
parent = up1_01

[Object]
nickname = up1_01_shipyardC01
pos = 880, 280, 0
rotate = 0, 0, 0
archetype = shipyard
parent = up1_01

[Object]
nickname = up1_01_tanksC01
pos = 880, -43, 0
rotate = 90, 0, 0
archetype = space_tanks4x4
parent = up1_01

[Object]
nickname = up1_01_tanksC02
pos = 880, 55, 0
rotate = 90, 0, 0
archetype = space_tanks2x2
parent = up1_01
'''
