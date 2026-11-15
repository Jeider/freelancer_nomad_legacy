from templates.space_object_template import SpaceObjectTemplate


class KusariPalace(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'om7_03'
    TEMPLATE = '''[Object]
nickname = om7_03
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_police01
{dock_props}

[Object]
nickname = om7_03_asteroid
pos = -1025, -1900, 145
rotate = 0, 0, 0
archetype = ku_xlarge_asteroid

[Object]
nickname = om7_03_asteroid01
pos = 425, -1375, 145
rotate = 0, -10, 60
archetype = co_medium_asteroid02
parent = om7_03


[Object]
nickname = om7_03_industrial01
pos = -2675, -2000, 145
rotate = 0, 0, 0
archetype = space_prison
parent = om7_03

[Object]
nickname = om7_03_PALACE_tube01
pos = 1975, -400, 145
rotate = 90, 0, 0
archetype = space_tube
parent = om7_03

[Object]
nickname = om7_03_PALACE_tube02
pos = 1410, -100, -420
rotate = 90, 0, 0
archetype = space_tube
parent = om7_03

[Object]
nickname = om7_03_PALACE_tube03
pos = 300, -700, -1530
rotate = 0, 45, 0
archetype = space_tube
parent = om7_03

[Object]
nickname = om7_03_PALACE_tube04
pos = 290, -500, -1540
rotate = 90, 0, 0
archetype = space_tube
parent = om7_03

[Object]
nickname = om7_03_PALACE_tube05
pos = 1810, -500, -820
rotate = 90, 0, 0
archetype = space_tube
parent = om7_03

[Object]
nickname = om7_03_PALACE_tube06
pos = 990, -290, 0
rotate = 90, 0, 0
archetype = space_tube
parent = om7_03

[Object]
nickname = om7_03_PALACE_tube07
pos = 0, -300, 0
rotate = 90, 0, 0
archetype = space_tube
parent = om7_03

[Object]
nickname = om7_03_PALACE_tube08
pos = 1310, -100, -420
rotate = 90, 0, 0
archetype = space_tube
parent = om7_03

[Object]
nickname = om7_03_PALACE_tube09
pos = 1510, -100, -420
rotate = 90, 0, 0
archetype = space_tube
parent = om7_03

[Object]
nickname = om7_03_PALACE_industrial01
pos = 1410, -220, -325
rotate = 90, 0, 0
archetype = space_industrial02
parent = om7_03

[Object]
nickname = om7_03_PALACE_industrial02
pos = 1410, -220, -515
rotate = 90, 0, 0
archetype = space_industrial02
parent = om7_03

[Object]
nickname = om7_03_PALACE_industrial03
pos = 1410, -600, -325
rotate = 0, 90, 0
archetype = space_industrial01a
parent = om7_03

[Object]
nickname = om7_03_PALACE_industrial04
pos = 1410, -600, -515
rotate = 0, 90, 0
archetype = space_industrial01a
parent = om7_03

[Object]
nickname = om7_03_PALACE_industrial05
pos = 0, -1500, 0
rotate = 90, 0, 0
archetype = space_industrial01a
parent = om7_03

[Object]
nickname = om7_03_PALACE_industrial06
pos = 290, -1750, -1540
rotate = 90, 0, 0
archetype = space_industrial01a
parent = om7_03

[Object]
nickname = om7_03_PALACE_industrial07
pos = 1810, -1300, -820
rotate = 90, 45, 0
archetype = space_industrial01a
parent = om7_03

[Object]
nickname = om7_03_PALACE_industrial08
pos = 1975, -1500, 145
rotate = 90, 0, 0
archetype = space_industrial01a
parent = om7_03

[Object]
nickname = om7_03_PALACE_industrial09
pos = 990, -990, 0
rotate = 90, 45, 0
archetype = space_industrial01a
parent = om7_03

[Object]
nickname = om7_03_PALACE_industrial10
pos = 1310, -1000, -420
rotate = 90, 0, 0
archetype = space_industrial01a
parent = om7_03

[Object]
nickname = om7_03_PALACE_industrial11
pos = 1510, -1100, -420
rotate = 90, 0, 0
archetype = space_industrial01a
parent = om7_03

[Object]
nickname = om7_03_PALACE_habitat01
pos = 1410, -50, -420
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = om7_03

[Object]
nickname = om7_03_PALACE_habitat02
pos = 290, -420, -1540
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = om7_03

[Object]
nickname = om7_03_PALACE_habitat03
pos = 990, -120, 0
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = om7_03

[Object]
nickname = om7_03_PALACE_habitat04
pos = 1975, -205, 145
rotate = 0, 45, 0
archetype = space_habitat_tall
parent = om7_03

[Object]
nickname = om7_03_PALACE_habitat05
pos = 1560, 50, -420
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = om7_03

[Object]
nickname = om7_03_PALACE_habitat06
pos = 1410, 110, -570
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = om7_03

[Object]
nickname = om7_03_PALACE_habitat07
pos = 1410, -10, -570
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = om7_03

[Object]
nickname = om7_03_PALACE_habitat08
pos = 1260, 25, -420
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = om7_03

[Object]
nickname = om7_03_PALACE_dome01
pos = 1410, 40, -420
rotate = 0, 45, 0
archetype = space_domea
parent = om7_03

[Object]
nickname = om7_03_PALACE_dome02
pos = 1810, -450, -820
rotate = 0, 0, 0
archetype = space_domea
parent = om7_03

[Object]
nickname = om7_03_PALACE_dome03
pos = 2115, -360, 5
rotate = 0, -45, 0
archetype = space_domea
parent = om7_03

[Object]
nickname = om7_03_PALACE_dome04
pos = 1835, -360, 285
rotate = 0, -45, 0
archetype = space_domea
parent = om7_03

[Object]
nickname = om7_03_PALACE_factory01
pos = 360, -330, -1610
rotate = 0, -45, 0
archetype = space_industrial03
parent = om7_03

[Object]
nickname = om7_03_PALACE_factory02
pos = 210, -330, -1470
rotate = 0, 135, 0
archetype = space_industrial03
parent = om7_03

[Object]
nickname = om7_03_PALACE_factory03
pos = 220, -330, -1610
rotate = 0, 45, 0
archetype = space_industrial03
parent = om7_03

[Object]
nickname = om7_03_PALACE_sml_cntrl_twr01
pos = 1975, -360, 145
rotate = 0, -45, 0
archetype = space_small_control_tower
parent = om7_03

[Object]
nickname = om7_03_PALACE_sml_cntrl_twr02
pos = 1810, -490, -820
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = om7_03

[Object]
nickname = om7_03_PALACE_sml_cntrl_twr03
pos = 1810, -900, -820
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = om7_03

[Object]
nickname = om7_03_PALACE_sml_cntrl_twr04
pos = 0, -150, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = om7_03

[Object]
nickname = om7_03_PALACE_sml_cntrl_twr05
pos = 990, -280, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = om7_03

[Object]
nickname = om7_03_PALACE_sml_cntrl_twr06
pos = 0, -500, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = om7_03

[Object]
nickname = om7_03_PALACE_sml_cntrl_twr07
pos = 290, -1000, -1540
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = om7_03

[Object]
nickname = om7_03_PALACE_cntrl_twr01
pos = 1410, -100, -420
rotate = 180, 0, 0
archetype = space_control_tower
parent = om7_03

[Object]
nickname = om7_03_PALACE_cntrl_twr02
pos = 290, -480, -1540
rotate = 0, 0, 0
archetype = space_control_tower
parent = om7_03

[Object]
nickname = om7_03_PALACE_cntrl_twr03
pos = 290, -360, -1540
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = om7_03

[Object]
nickname = om7_03_PALACE_cntrl_twr04
pos = 1410, -700, -420
rotate = 0, 45, 0
archetype = space_control_tower
parent = om7_03

[Object]
nickname = om7_03_PALACE_cntrl_twr05
pos = 1975, -700, 145
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = om7_03

[Object]
nickname = om7_03_PALACE_cntrl_twr06
pos = 290, -700, -1540
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = om7_03

[Object]
nickname = om7_03_PALACE_cntrl_twr07
pos = 1410, -490, -420
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = om7_03

[Object]
nickname = om7_03_PALACE_cntrl_twr08
pos = 990, -490, 0
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = om7_03

[Object]
nickname = om7_03_PALACE_cntrl_twr09
pos = 990, -700, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = om7_03

[Object]
nickname = om7_03_PALACE_cntrl_twr10
pos = 0, -700, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = om7_03

[Object]
nickname = om7_03_PALACE_cntrl_twr11
pos = 290, -700, -1540
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = om7_03

[Object]
nickname = om7_03_PALACE_cntrl_twr12
pos = 0, -280, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = om7_03

[Object]
nickname = om7_03_PALACE_cntrl_twr13
pos = 1975, -400, 145
rotate = 0, 0, 0
archetype = space_control_tower
parent = om7_03

[Object]
nickname = om7_03_PALACE_girder01a
pos = 1825, -700, -5
rotate = 0, 45, 0
archetype = space_girder
parent = om7_03

[Object]
nickname = om7_03_PALACE_girder01
pos = 1560, -700, -270
rotate = 0, 45, 0
archetype = space_girder
parent = om7_03

[Object]
nickname = om7_03_PALACE_girder02
pos = 1660, -700, -670
rotate = 0, -45, 0
archetype = space_girder
parent = om7_03

[Object]
nickname = om7_03_PALACE_girder03
pos = 1190, -490, -200
rotate = 0, -45, 0
archetype = space_girder
parent = om7_03

[Object]
nickname = om7_03_PALACE_girder04
pos = 690, -700, 0
rotate = 0, 90, 0
archetype = space_girder
parent = om7_03

[Object]
nickname = om7_03_PALACE_girder05
pos = 310, -700, 0
rotate = 0, 90, 0
archetype = space_girder
parent = om7_03

[Object]
nickname = om7_03_PALACE_girder06
pos = 0, -150, 0
rotate = 90, 0, 0
archetype = space_girder
parent = om7_03
'''
