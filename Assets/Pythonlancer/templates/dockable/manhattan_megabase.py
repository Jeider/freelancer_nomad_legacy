from templates.space_object_template import SpaceObjectTemplate


class ManhattanMegabase(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_mnh_04'
    TEMPLATE = '''[Object]
nickname = li_mnh_04
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = manhattan_core
{root_props}

[Object]
nickname = li_mnh_04_dock
pos = 0, 500, -1340
rotate = 0, -90, 0
archetype = space_shipping01
{dock_props}

[Object]
nickname = li_mnh_04_MAIN_space_ind01
pos = 0, 500, 0
rotate = 90, 0, 0
archetype = space_industrial02a
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_space_ind02
pos = 0, 500, 0
rotate = 90, 45, 0
archetype = space_industrial02a
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_space_ind03
pos = 0, 500, -550
rotate = 0, 0, 0
archetype = space_industrial02
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_space_ind04
pos = 0, 500, 550
rotate = 0, 180, 0
archetype = space_industrial02
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_space_ind05
pos = -389, 500, -390
rotate = 0, 45, 0
archetype = space_industrial02
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_space_ind06
pos = -389, 500, 390
rotate = 0, 135, 0
archetype = space_industrial02
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_space_ind07
pos = 389, 500, -390
rotate = 0, -45, 0
archetype = space_industrial02
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_space_ind08
pos = 389, 500, 390
rotate = 0, -135, 0
archetype = space_industrial02
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_space_ind09
pos = -550, 500, 0
rotate = 0, 90, 0
archetype = space_industrial02
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_space_ind10
pos = 550, 500, 0
rotate = 0, -90, 0
archetype = space_industrial02
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_research01
pos = 0, 205, 0
rotate = 90, 0, 0
archetype = space_research
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_ctrl_twr01
pos = 0, 645, -5
rotate = 0, 0, 0
archetype = space_control_tower
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_ctrl_twr02
pos = 0, 355, -5
rotate = 0, 180, 0
archetype = space_control_tower
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel01
pos = -250, 570, 0
rotate = 0, 0, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel02
pos = -180, 570, 175
rotate = 0, 45, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel03
pos = 0, 570, 250
rotate = 0, 90, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel04
pos = 180, 570, 175
rotate = 0, 130, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel05
pos = 250, 570, 0
rotate = 0, 180, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel06
pos = 180, 570, -175
rotate = 0, -135, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel07
pos = 0, 570, -250
rotate = 0, -90, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel08
pos = -180, 570, -175
rotate = 0, -45, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel09
pos = -250, 430, 0
rotate = 180, 0, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel10
pos = -180, 430, 175
rotate = 180, 45, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel11
pos = 0, 430, 250
rotate = 180, 90, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel12
pos = 180, 430, 175
rotate = 180, 130, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel13
pos = 250, 430, 0
rotate = 180, 180, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel14
pos = 180, 430, -175
rotate = 180, -135, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel15
pos = 0, 430, -250
rotate = 180, -90, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel16
pos = -180, 430, -175
rotate = 180, -45, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_habitat01
pos = 0, 750, -5
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_habitat02
pos = 0, 710, -120
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_habitat03
pos = 110, 735, -5
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_habitat04
pos = -110, 735, -5
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_habitat05
pos = 0, 735, 105
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_habitat06
pos = 0, 955, -5
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_habitat07
pos = 110, 880, -5
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_habitat08
pos = -110, 850, -5
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_tank01
pos = 390, 660, 390
rotate = 180, 45, 0
archetype = space_tanklx4
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_tank02
pos = 390, 340, 390
rotate = 0, 45, 0
archetype = space_tanklx4
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_tank03
pos = 390, 660, -390
rotate = 180, 45, 0
archetype = space_tanklx4
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_tank04
pos = 390, 340, -390
rotate = 0, 45, 0
archetype = space_tanklx4
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_tank05
pos = -390, 660, -390
rotate = 180, 45, 0
archetype = space_tanklx4
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_tank06
pos = -390, 340, -390
rotate = 0, 45, 0
archetype = space_tanklx4
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_tank07
pos = -390, 660, 390
rotate = 180, 45, 0
archetype = space_tanklx4
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_tank08
pos = -390, 340, 390
rotate = 0, 45, 0
archetype = space_tanklx4
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_industrial_A01
pos = -920, 500, 0
rotate = 0, 90, 0
archetype = space_industrial
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_industrial_A02
pos = -1290, 500, 0
rotate = 0, 90, 0
archetype = space_industrial
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_industrial_A03
pos = 920, 500, 0
rotate = 0, -90, 0
archetype = space_industrial
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_industrial_A04
pos = 1290, 500, 0
rotate = 0, -90, 0
archetype = space_industrial
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_shipyard_01
pos = -920, 710, -185
rotate = 180, 0, 0
archetype = shipyard
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_shipyard_02
pos = -1290, 710, -185
rotate = 180, 0, 0
archetype = shipyard
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_shipyard_03
pos = -920, 290, 185
rotate = 0, 0, 0
archetype = shipyard
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_shipyard_04
pos = -1290, 290, 185
rotate = 0, 0, 0
archetype = shipyard
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_shipyard_05
pos = 920, 710, 185
rotate = 0, 0, 180
archetype = shipyard
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_shipyard_06
pos = 1290, 710, 185
rotate = 0, 0, 180
archetype = shipyard
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_shipyard_07
pos = 920, 290, -185
rotate = 0, 180, 0
archetype = shipyard
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_shipyard_08
pos = 1290, 290, -185
rotate = 0, 180, 0
archetype = shipyard
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_industrial_A05
pos = 0, 500, 1150
rotate = 0, 180, 45
archetype = space_industrial
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_girder01
pos = -140, 640, 1150
rotate = 45, 90, 0
archetype = space_girder
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_girder02
pos = 140, 640, 1150
rotate = 45, -90,0
archetype = space_girder
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_girder03
pos = -140, 360, 1150
rotate = 45, -90, 0
archetype = space_girder
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_girder04
pos = 140, 360, 1150
rotate = 45, 90, 0
archetype = space_girder
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_shipyard_09
pos = -100, 800, 1350
rotate = 0, 0, 135
archetype = shipyard
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_shipyard_10
pos = 100, 800, 1350
rotate = 0, 0, -135
archetype = shipyard
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_shipyard_11
pos = -100, 200, 1350
rotate = 0, 0, 45
archetype = shipyard
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_shipyard_12
pos = 100, 200, 1350
rotate = 0, 0, -45
archetype = shipyard
parent = li_mnh_04

[Object]
nickname = li_mnh_04_TENG_industrial01
pos = 0, 50, -400
rotate = 0, 0, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = li_mnh_04

[Object]
nickname = li_mnh_04_TENG_industrial02
pos = 0, 50, 400
rotate = 0, 180, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = li_mnh_04

[Object]
nickname = li_mnh_04_TENG_industrial03
pos = 400, 50, 0
rotate = 0, -90, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = li_mnh_04

[Object]
nickname = li_mnh_04_TENG_industrial04
pos = -400, 50, 0
rotate = 0, 90, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = li_mnh_04

[Object]
nickname = li_mnh_04_TENG_industrial05
pos = 275, 50, -275
rotate = 0, -45, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = li_mnh_04

[Object]
nickname = li_mnh_04_TENG_industrial06
pos = 275, 50, 275
rotate = 0, -135, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = li_mnh_04

[Object]
nickname = li_mnh_04_TENG_industrial07
pos = -275, 50, -275
rotate = 0, 45, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = li_mnh_04

[Object]
nickname = li_mnh_04_TENG_industrial08
pos = -275, 50, 275
rotate = 0, 135, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = li_mnh_04

[Object]
nickname = li_mnh_04_IND_industrial01
pos = 275, -150, -275
rotate = 0, -45, 0
archetype = space_industrial02
parent = li_mnh_04

[Object]
nickname = li_mnh_04_IND_industrial02
pos = 275, -150, 275
rotate = 0, -135, 0
archetype = space_industrial02
parent = li_mnh_04

[Object]
nickname = li_mnh_04_IND_industrial03
pos = -275, -150, -275
rotate = 0, 45, 0
archetype = space_industrial02
parent = li_mnh_04

[Object]
nickname = li_mnh_04_IND_industrial04
pos = -275, -150, 275
rotate = 0, 135, 0
archetype = space_industrial02
parent = li_mnh_04

[Object]
nickname = li_mnh_04_IND_industrial05
pos = 275, -350, -275
rotate = 90, -45, 0
archetype = space_industrial02a
parent = li_mnh_04

[Object]
nickname = li_mnh_04_IND_industrial16
pos = 275, -350, 275
rotate = 90, -135, 0
archetype = space_industrial02a
parent = li_mnh_04

[Object]
nickname = li_mnh_04_IND_industrial17
pos = -275, -350, -275
rotate = 90, 45, 0
archetype = space_industrial02a
parent = li_mnh_04

[Object]
nickname = li_mnh_04_IND_industrial18
pos = -275, -350, 275
rotate = 90, 135, 0
archetype = space_industrial02a
parent = li_mnh_04

[Object]
nickname = li_mnh_04_IND_industrial09
pos = 275, -550, -275
rotate = 0, -45, 0
archetype = space_industrial02
parent = li_mnh_04

[Object]
nickname = li_mnh_04_IND_industrial10
pos = 275, -550, 275
rotate = 0, -135, 0
archetype = space_industrial02
parent = li_mnh_04

[Object]
nickname = li_mnh_04_IND_industrial11
pos = -275, -550, -275
rotate = 0, 45, 0
archetype = space_industrial02
parent = li_mnh_04

[Object]
nickname = li_mnh_04_IND_industrial12
pos = -275, -550, 275
rotate = 0, 135, 0
archetype = space_industrial02
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_industrial01
pos = 0, -750, -400
rotate = 0, 0, 0
archetype = space_industrial
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_industrial02
pos = 0, -750, 400
rotate = 0, 180, 0
archetype = space_industrial
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_industrial03
pos = 400, -750, 0
rotate = 0, -90, 0
archetype = space_industrial
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_industrial04
pos = -400, -750, 0
rotate = 0, 90, 0
archetype = space_industrial
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_industrial05
pos = 0, -1150, -400
rotate = 0, 0, 0
archetype = space_industrial
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_industrial06
pos = 0, -1150, 400
rotate = 0, 180, 0
archetype = space_industrial
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_industrial07
pos = 400, -1150, 0
rotate = 0, -90, 0
archetype = space_industrial
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_industrial08
pos = -400, -1150, 0
rotate = 0, 90, 0
archetype = space_industrial
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_tankl01
pos = 0, -950, -400
rotate = 90, 0, 0
archetype = space_tankl4x4
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_tankl02
pos = 0, -950, 400
rotate = 90, 180, 0
archetype = space_tankl4x4
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_tankl03
pos = 400, -950, 0
rotate = 90, -90, 0
archetype = space_tankl4x4
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_tankl04
pos = -400, -950, 0
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_tankl05
pos = 0, -950, -400
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_tankl06
pos = 0, -950, 400
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_tankl07
pos = 400, -950, 0
rotate = 90, 0, 0
archetype = space_tankl4x4
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_tankl08
pos = -400, -950, 0
rotate = 90, 0, 0
archetype = space_tankl4x4
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_dome01
pos = -350, -720, -400
rotate = 0, 90, 0
archetype = space_dome
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_dome02
pos = 350, -720, 400
rotate = 0, -90, 0
archetype = space_dome
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_dome03
pos = 400, -720, -360
rotate = 0, 0, 0
archetype = space_dome
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_dome04
pos = -400, -720, 360
rotate = 0, 180, 0
archetype = space_dome
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_dome05
pos = -350, -1182, -400
rotate = 0, -90, 180
archetype = space_dome
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_dome06
pos = 350, -1182, 400
rotate = 0, 90, 180
archetype = space_dome
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_dome07
pos = 400, -1182, -360
rotate = 0, 0, 180
archetype = space_dome
parent = li_mnh_04

[Object]
nickname = li_mnh_04_HILL_dome08
pos = -400, -1182, 360
rotate = 0, 180, 180
archetype = space_dome
parent = li_mnh_04

[Object]
nickname = li_mnh_04_BENG_industrial01
pos = 0, -1400, -400
rotate = 0, 0, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = li_mnh_04

[Object]
nickname = li_mnh_04_BENG_industrial02
pos = 0, -1400, 400
rotate = 0, 180, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = li_mnh_04

[Object]
nickname = li_mnh_04_BENG_industrial03
pos = 400, -1400, 0
rotate = 0, -90, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = li_mnh_04

[Object]
nickname = li_mnh_04_BENG_industrial04
pos = -400, -1400, 0
rotate = 0, 90, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = li_mnh_04

[Object]
nickname = li_mnh_04_BENG_industrial05
pos = 275, -1400, -275
rotate = 0, -45, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = li_mnh_04

[Object]
nickname = li_mnh_04_BENG_industrial06
pos = 275, -1400, 275
rotate = 0, -135, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = li_mnh_04

[Object]
nickname = li_mnh_04_BENG_industrial07
pos = -275, -1400, -275
rotate = 0, 45, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = li_mnh_04

[Object]
nickname = li_mnh_04_BENG_industrial08
pos = -275, -1400, 275
rotate = 0, 135, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = li_mnh_04

[Object]
nickname = li_mnh_04_END_ctrl_twr01
pos = 0, -1750, -5
rotate = 0, 0, 0
archetype = space_control_tower
parent = li_mnh_04
'''


class ManhattanMegabaseOutpost(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_mnh_04'
    TEMPLATE = '''[Object]
nickname = li_mnh_04
pos = 0, 0, 0
rotate = 0, -90, 0
archetype = space_police01
{dock_props}

[Object]
nickname = li_mnh_04_MAIN_space_ind01
pos = 0, -580, 0
rotate = 90, 0, 0
archetype = space_industrial02a
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_girder01
pos = 0, -230, 0
rotate = 90, 0, 0
archetype = space_girder
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_habitat01
pos = 0, -340, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_habitat02
pos = 60, -810, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_habitat02
pos = 0, -810, -60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_habitat02
pos = 0, -810, 60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_habitat02
pos = -60, -810, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_ctrl_twr02
pos = 0, -440, -5
rotate = 0, 180, 0
archetype = space_control_tower
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_ctrl_twr02
pos = 0, -725, -5
rotate = 0, 180, 0
archetype = space_control_tower
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_ctrl_twr03
pos = 0, -910, -5
rotate = 0, 180, 0
archetype = space_medium_control_tower
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_ctrl_twr02
pos = 0, -980, 0
rotate = 0, 0, 0
archetype = space_tanklx4
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_ctrl_twr02
pos = 0, -1030, 0
rotate = 0, 0, 0
archetype = space_tanklx4
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel01
pos = -250, -510, 0
rotate = 0, 0, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel02
pos = -180, -510, 175
rotate = 0, 45, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel03
pos = 0, -510, 250
rotate = 0, 90, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel04
pos = 180, -510, 175
rotate = 0, 130, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel05
pos = 250, -510, 0
rotate = 0, 180, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel06
pos = 180, -510, -175
rotate = 0, -135, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel07
pos = 0, -510, -250
rotate = 0, -90, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel08
pos = -180, -510, -175
rotate = 0, -45, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel09
pos = -250, -650, 0
rotate = 180, 0, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel10
pos = -180, -650, 175
rotate = 180, 45, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel11
pos = 0, -650, 250
rotate = 180, 90, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel12
pos = 180, -650, 175
rotate = 180, 130, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel13
pos = 250, -650, 0
rotate = 180, 180, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel14
pos = 180, -650, -175
rotate = 180, -135, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel15
pos = 0, -650, -250
rotate = 180, -90, 0
archetype = space_panel45
parent = li_mnh_04

[Object]
nickname = li_mnh_04_MAIN_panel16
pos = -180, -650, -175
rotate = 180, -45, 0
archetype = space_panel45
parent = li_mnh_04
'''
