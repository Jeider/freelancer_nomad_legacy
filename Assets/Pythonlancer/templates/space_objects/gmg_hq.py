from templates.space_object_template import SpaceObjectTemplate


class GmgHQAlive(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_hkd_04'
    TEMPLATE = '''[Object]
nickname = ku_hkd_04
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_industrial02a

[Object]
nickname = ku_hkd_04_ind01
pos = 0, 0, -370
rotate = 0, 0, 0
archetype = space_industrial02
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_ind02
pos = 0, 0, 370
rotate = 0, 180, 0
archetype = space_industrial02
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_ind03
pos = -180, 0, 0
rotate = 0, 90, 0
archetype = space_industrial01a
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_ind04
pos = 180, 0, 0
rotate = 0, 90, 0
archetype = space_industrial01a
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_dome01
pos = -440, 0, 0
rotate = 0, 90, 0
archetype = space_domea
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_dome02
pos = 440, 0, 0
rotate = 0, 90, 0
archetype = space_domea
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_panel01
pos = 0, 73, 0
rotate = 0, 0, 0
archetype = space_solar_pnl
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_panel02
pos = 0, 65, -370
rotate = 0, 0, 0
archetype = space_solar_pnl
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_panel03
pos = 0, 65, 370
rotate = 0, 0, 0
archetype = space_solar_pnl
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_tanks01
pos = 0, -200, 0
rotate = 0, 0, 0
archetype = space_tanklx4
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_tanks02
pos = 0, -170, -230
rotate = 0, 0, 0
archetype = space_tankl4
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_tanks03
pos = 0, -170, 230
rotate = 0, 0, 0
archetype = space_tankl4
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_tanks04
pos = -160, -242.5, 0
rotate = 0, 90, 0
archetype = space_tankl2
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_tanks05
pos = 160, -242.5, 0
rotate = 0, 90, 0
archetype = space_tankl2
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_girder01
pos = 0, 35, -370
rotate = 90, 0, 0
archetype = space_girdera
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_girder02
pos = 0, 35, 370
rotate = 90, 0, 0
archetype = space_girdera
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_girder03
pos = -180, 0, 180
rotate = 0, 0, 0
archetype = space_girder
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_girder04
pos = -180, 0, -180
rotate = 0, 0, 0
archetype = space_girder
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_girder05
pos = 180, 0, 180
rotate = 0, 0, 0
archetype = space_girder
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_girder06
pos = 180, 0, -180
rotate = 0, 0, 0
archetype = space_girder
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatA01
pos = -130, 0, 370
rotate = 0, 0, 90
archetype = space_habitat_wide
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatA02
pos = -130, 0, -370
rotate = 0, 0, 90
archetype = space_habitat_wide
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatA03
pos = 130, 0, 370
rotate = 0, 0, 90
archetype = space_habitat_wide
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatA04
pos = 130, 0, -370
rotate = 0, 0, 90
archetype = space_habitat_wide
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatA05
pos = -180, 0, 130
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatA06
pos = -180, 0, -130
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatA07
pos = 180, 0, 130
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatA08
pos = 180, 0, -130
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatB01
pos = -250, 0, 370
rotate = 0, 0, 90
archetype = space_habitat_tall
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatB02
pos = -250, 0, -370
rotate = 0, 0, 90
archetype = space_habitat_tall
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatB03
pos = 250, 0, 370
rotate = 0, 0, -90
archetype = space_habitat_tall
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatB04
pos = 250, 0, -370
rotate = 0, 0, -90
archetype = space_habitat_tall
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_ctrl_block01
pos = -180, 115, 0
rotate = 0, 0, 0
archetype = space_small_control_block
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_ctrl_block02
pos = 180, 115, 0
rotate = 0, 0, 0
archetype = space_small_control_block
parent = ku_hkd_04
'''


class GmgHQDestroyed(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_hkd_04'
    TEMPLATE = '''[Object]
nickname = ku_hkd_04
ids_name = 203759
pos = 0, 0, 0
rotate = -10, 0, 5
archetype = space_industrial02a_station_root
ids_info = 065674
reputation = fc_uk_grp
behavior = NOTHING

[Object]
nickname = ku_hkd_04_ind01
pos = 0, 0, -370
rotate = 0, 0, 0
archetype = space_industrial02a
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_ind02
pos = 15, -45, 370
rotate = 20, 0, 15
archetype = space_industrial02a
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_ind03
pos = -180, -20, 0
rotate = -10, 90, 0
archetype = space_industrial01a
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_ind04
pos = 180, 0, 0
rotate = 0, 90, 0
archetype = space_industrial01a
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_dome01
pos = -440, -58, 0
rotate = 0, 0, 5
archetype = space_dome_dmg2
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_dome02
pos = 440, 0, 0
rotate = 0, 180, 0
archetype = space_dome_dmg
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_panel01
pos = -5, 70, -13
rotate = -10, 0, 5
archetype = space_solar_pnl
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_panel02
pos = 0, 65, -370
rotate = 0, 0, 0
archetype = space_solar_pnl
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_panel03
pos = 0, 30, 370
rotate = 15, 70, -15
archetype = space_panel_damaged_01
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_tanks01
pos = 0, -190, 0
rotate = 0, 0, 0
archetype = space_tanklx4_dmg
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_tanks02
pos = 0, -160, -230
rotate = -5, 0, 0
archetype = space_tankl4
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_tanks03
pos = 0, -160, 230
rotate = 0, 0, 0
archetype = space_tankl4_dmg
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_tanks04
pos = -160, -212.5, 0
rotate = 0, 90, -10
archetype = space_tankl2
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_tanks05
pos = 125, -225, 0
rotate = -20, 90, 0
archetype = space_tankl_3dmg
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_girder01
pos = 0, 35, -370
rotate = 90, 0, 0
archetype = space_girdera
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_girder02
pos = 0, 45, 0
rotate = 10, 0, 0
archetype = space_girdera
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_girder03
pos = -170, -38, 180
rotate = 100, 0, 10
archetype = space_habitat_dmg
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_girder04
pos = -180, -10, -180
rotate = 3, 0, 0
archetype = space_girder
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_girder05
pos = 180, 30, 250
rotate = -90, 0, 180
archetype = space_habitat_dmg
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_girder06
pos = 180, 0, -180
rotate = 0, 0, 0
archetype = space_girder
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_girder07
pos = 0, -4, -370
rotate = 5, 0, 0
archetype = space_girdera
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatA01
pos = -120, -80, 370
rotate = 0, 20,95
archetype = space_habitat_wide
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatA02
pos = -130, 0, -370
rotate = 0, 0, 90
archetype = space_habitat_wide
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatA03
pos = 130, 0, 370
rotate = 10, 0, 110
archetype = space_habitat_wide
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatA04
pos = 130, 0, -370
rotate = 0, 0, 90
archetype = space_habitat_wide
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatA06
pos = -180, -15, -130
rotate = 95, 0, 0
archetype = space_habitat_wide
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatA07
pos = 180, 20, 130
rotate = 80, 0, 0
archetype = space_habitat_wide
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatA08
pos = 180, 0, -130
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatB01
pos = -250, -80, 370
rotate = 0, 20, 85
archetype = space_habitat_dmg
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatB02
pos = -250, 0, -370
rotate = 0, 0, 90
archetype = space_habitat_tall
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatB03
pos = 240, 50, 360
rotate = 0, 0, -60
archetype = space_habitat_dmg
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_habitatB04
pos = 250, 0, -370
rotate = 0, 0, -90
archetype = space_habitat_tall
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_ctrl_block01
pos = -190, 115, -10
rotate = -10, 0, 0
archetype = space_habitat_dmg
parent = ku_hkd_04

[Object]
nickname = ku_hkd_04_ctrl_block02
pos = 180, 115, 0
rotate = 0, 0, 0
archetype = space_small_control_block
parent = ku_hkd_04

'''