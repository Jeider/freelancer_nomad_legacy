from templates.space_object_template import SpaceObjectTemplate


class BlackHoleResearch(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'om13_01'
    TEMPLATE = '''[Object]
nickname = om13_01
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = space_police01_front_dock
{dock_props}

[Object]
nickname = om13_01_panel01
pos = 100, 40, 90
rotate = 0, 0, 25
archetype = space_panel
parent = om13_01

[Object]
nickname = om13_01_panel02
pos = -100, 40, 90
rotate = 0, 0, -25
archetype = space_panel
parent = om13_01

[Object]
nickname = om13_01_panel03
pos = 70, 50, 255
rotate = 10, 145, -10
archetype = space_panel45
parent = om13_01

[Object]
nickname = om13_01_panel04
pos = -70, 50, 255
rotate = 95, -155, -40
archetype = space_panel
parent = om13_01

[Object]
nickname = om13_01_ind01
pos = 0, 0, 120
rotate = 90, 0, 0
archetype = space_industrial02a
parent = om13_01

[Object]
nickname = om13_01_ind02
pos = 0, 0, 240
rotate = 0, 0, 0
archetype = space_industriala
parent = om13_01

[Object]
nickname = om13_01_ind03
pos = 60, -62, 120
rotate = 0, , 0
archetype = space_industrial02a
parent = om13_01

[Object]
nickname = om13_01_ind04
pos = -60, -62, 120
rotate = 0, 0, 0
archetype = space_industrial01a
parent = om13_01

[Object]
nickname = om13_01_habitat01
pos = 0, -400, 120
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = om13_01

[Object]
nickname = om13_01_habitat02
pos = 0, -200, 120
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = om13_01

[Object]
nickname = om13_01_habitat03
pos = 0, 70, 215
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = om13_01

[Object]
nickname = om13_01_habitat04
pos = 0, 160, 215
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = om13_01

[Object]
nickname = om13_01_habitat05
pos = 0, 183, 120
rotate = 0, 90, 0
archetype = space_small_control_block
parent = om13_01

[Object]
nickname = om13_01_tanks01
pos = -50, -260, 120
rotate = 90, 0, 10
archetype = space_tankl4x4
parent = om13_01

[Object]
nickname = om13_01_tanks02
pos = 50, -250, 120
rotate = 90, 0, -5
archetype = space_tankl4x4
parent = om13_01

[Object]
nickname = om13_01_dpanel01
pos = 90, -200, 90
rotate = 0, 0, 220
archetype = space_debris_panel
parent = om13_01

[Object]
nickname = om13_01_dpanel02
pos = 78, -300, 140
rotate = 0, 0, 220
archetype = space_debris_panel
parent = om13_01

[Object]
nickname = om13_01_dpanel03
pos = -95, -200, 90
rotate = 0, 0, 55
archetype = space_debris_panel
parent = om13_01

[Object]
nickname = om13_01_dpanel04
pos = -78, -300, 140
rotate = 0, 0, 55
archetype = space_debris_panel
parent = om13_01
'''


class BlackHoleOutpost(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'om13_02'
    TEMPLATE = '''[Object]
nickname = om13_02
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_port_dmg
{dock_props}

[Object]
nickname = om13_02_ind01
pos = 0, -250, 0
rotate = 90, 90, 0
archetype = space_industriala
parent = om13_02

[Object]
nickname = om13_02_ind02
pos = 175, -250, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = om13_02

[Object]
nickname = om13_02_ind03
pos = -175, -250, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = om13_02

[Object]
nickname = om13_02_ind04
pos = -115, -250, 200
rotate = 90, 0, 90
archetype = space_industrial02d
parent = om13_02

[Object]
nickname = om13_02_ind05
pos = 115, -250, 200
rotate = 90, 0, 90
archetype = space_industrial02d
parent = om13_02

[Object]
nickname = om13_02_ind06
pos = -115, -250, -200
rotate = 90, 0, 90
archetype = space_industrial02d
parent = om13_02

[Object]
nickname = om13_02_ind07
pos = 115, -250, -200
rotate = 90, 0, 90
archetype = space_industrial02d
parent = om13_02

[Object]
nickname = om13_02_ind08
pos = -160, -210, 0
rotate = 90, 0, 90
archetype = space_industrial02d
parent = om13_02

[Object]
nickname = om13_02_ind09
pos = -160, -290, 0
rotate = 90, 0, 90
archetype = space_industrial02d
parent = om13_02

[Object]
nickname = om13_02_ind10
pos = 160, -210, 0
rotate = 90, 0, 90
archetype = space_industrial02d
parent = om13_02

[Object]
nickname = om13_02_ind11
pos = 160, -290, 0
rotate = 90, 0, 90
archetype = space_industrial02d
parent = om13_02

[Object]
nickname = om13_02_shipyard01
pos = 0, -250, 100
rotate = 90, 0, 90
archetype = shipyard_medium
parent = om13_02

[Object]
nickname = om13_02_shipyard02
pos = 0, -250, -100
rotate = -90, 0, 90
archetype = shipyard_medium
parent = om13_02

[Object]
nickname = om13_02_dpanel01
pos = 120, -172, 120
rotate = 90, -28, -90
archetype = space_debris_panel
parent = om13_02

[Object]
nickname = om13_02_dpanel02
pos = -120, -172, 120
rotate = 90, -28, -90
archetype = space_debris_panel
parent = om13_02

[Object]
nickname = om13_02_dpanel03
pos = 120, -172, -120
rotate = -90, 28, -90
archetype = space_debris_panel
parent = om13_02

[Object]
nickname = om13_02_dpanel04
pos = -120, -172, -120
rotate = -90, 28, -90
archetype = space_debris_panel
parent = om13_02

[Object]
nickname = om13_02_dpanel05
pos = 120, -328, 120
rotate = 90, -28, 90
archetype = space_debris_panel
parent = om13_02

[Object]
nickname = om13_02_dpanel06
pos = -120, -328, 120
rotate = 90, -28, 90
archetype = space_debris_panel
parent = om13_02

[Object]
nickname = om13_02_dpanel07
pos = 120, -328, -120
rotate = 90, 152, -90
archetype = space_debris_panel
parent = om13_02

[Object]
nickname = om13_02_dpanel08
pos = -120, -328, -120
rotate = 90, 152, -90
archetype = space_debris_panel
parent = om13_02

[Object]
nickname = om13_02_girder01
pos = -75, -180, 110
rotate = -15, 150, 0
archetype = space_girderc
parent = om13_02

[Object]
nickname = om13_02_girder02
pos = -75, -180, -110
rotate = -15, 30, 0
archetype = space_girderc
parent = om13_02

[Object]
nickname = om13_02_girder03
pos = 75, -180, 110
rotate = 15, 30, 0
archetype = space_girderc
parent = om13_02

[Object]
nickname = om13_02_girder04
pos = 75, -180, -110
rotate = 15, 150, 0
archetype = space_girderc
parent = om13_02

[Object]
nickname = om13_02_girder05
pos = -75, -320, 110
rotate = 15, 150, 0
archetype = space_girderc
parent = om13_02

[Object]
nickname = om13_02_girder06
pos = -75, -320, -110
rotate = 15, 30, 0
archetype = space_girderc
parent = om13_02

[Object]
nickname = om13_02_girder07
pos = 75, -320, 110
rotate = -15, 30, 0
archetype = space_girderc
parent = om13_02

[Object]
nickname = om13_02_girder08
pos = 75, -320, -110
rotate = -15, 150, 0
archetype = space_girderc
parent = om13_02

[Object]
nickname = om13_02_hab01
pos = 0, -408, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = om13_02

[Object]
nickname = om13_02_hab02
pos = 0, -495, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = om13_02
'''


class BlackHoleDestroyedStation(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'om13_03'
    TEMPLATE = '''[Object]
nickname = om13_03
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = space_industrial_station_root
{root_props}

[Object]
nickname = om13_03_ind01
pos = 0, -22, -400
rotate = 10, 180, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = om13_03

[Object]
nickname = om13_03_ind02
pos = -25, -60, -880
rotate = 10, 10, 0
archetype = space_industrial02a
parent = om13_03

[Object]
nickname = om13_03_dome01
pos = 0, -5, 350
rotate = 0, 90, 0
archetype = space_dome_dmg2
parent = om13_03

[Object]
nickname = om13_03_hab01
pos = 200, 0, -350
rotate = 120, 50, 10
archetype = space_habitat_dmg
parent = om13_03

[Object]
nickname = om13_03_hab02
pos = -250, -200, -350
rotate = 34, -45, -23
archetype = space_habitat_dmg
parent = om13_03

[Object]
nickname = om13_03_panel01
pos = 0, 65, 0
rotate = 90, 80, 80
archetype = space_solar_pnl
parent = om13_03

[Object]
nickname = om13_03_panel02
pos = -65, 0, 0
rotate = 0, 40, 60
archetype = space_panel_damaged_01
parent = om13_03

[Object]
nickname = om13_03_panel03
pos = 65, 0, 0
rotate = 0, 0, -120
archetype = space_panel_damaged_01
parent = om13_03

[Object]
nickname = om13_03_tank01
pos = 2, 65, -855
rotate = 100, 20, -20
archetype = space_tankl2x2
parent = om13_03

[Object]
nickname = om13_03_tank02
pos = -30, -250, -875
rotate = 90, 0, 0
archetype = space_tankl4x4_dmg
parent = om13_03

[Object]
nickname = om13_03_tank03
pos = 0, 200, -550
rotate = 180, -30, 0
archetype = space_tankl4_dmg
parent = om13_03
'''


class ShinobiAbandonedResearch(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'om11_04'
    TEMPLATE = '''[Object]
nickname = om11_04
pos = 0, 0, 0
rotate = 0, 0, 5
archetype = space_police01
{dock_props}

[Object]
nickname = om11_04_dock01
pos = 200, 0, 0
rotate = 20, 0, -3
archetype = space_police_dmg
parent = om11_04

[Object]
nickname = om11_04_dock02
pos = 400, 0, 0
rotate = 0, 180, 5
archetype = space_police_dmg
parent = om11_04

[Object]
nickname = om11_04_girder01
pos = 200, 0, 0
rotate = 0, 90, -3
archetype = space_girder
parent = om11_04

[Object]
nickname = om11_04_girder02
pos = 323, -116, 0
rotate = 45, -90, 0
archetype = space_beaml_dmg
parent = om11_04

[Object]
nickname = om11_04_girder03
pos = 117, -150, 0
rotate = -135, 90, 0
archetype = space_beaml_dmg
parent = om11_04

[Object]
nickname = om11_04_girder04
pos = 200, -36, 0
rotate = 90, 0, 5
archetype = space_girdera
parent = om11_04

[Object]
nickname = om11_04_girder05
pos = 303, 130, 0
rotate = -45, -90, 0
archetype = space_beaml_dmg
parent = om11_04

[Object]
nickname = om11_04_girder06
pos = -43, -10, 0
rotate = -45, 90, 0
archetype = space_girdera
parent = om11_04

[Object]
nickname = om11_04_ctrl_twr01
pos = 210, -250, 0
rotate = 0, 0, 6
archetype = space_medium_control_tower
parent = om11_04

[Object]
nickname = om11_04_ctrl_twr02
pos = 200, 190, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = om11_04

[Object]
nickname = om11_04_ctrl_block01
pos = 200, 220, 0
rotate = 0, 0, 0
archetype = space_domea
parent = om11_04

[Object]
nickname = om11_04_ind01
pos = 200, -400, 0
rotate = -90, 45, -5
archetype = space_industrial01a
parent = om11_04

[Object]
nickname = om11_04_ind02
pos = 200, -650, 0
rotate = 90, 0, 10
archetype = space_industrial01a
parent = om11_04

[Object]
nickname = om11_04_panel01
pos = 200, -665, 0
rotate = 0, 110, 90
archetype = space_solar_pnl
parent = om11_04

[Object]
nickname = om11_04_panel02
pos = 200, -626, 0
rotate = 0, 90, -100
archetype = space_solar_pnl
parent = om11_04

[Object]
nickname = om11_04_panel03
pos = 200, -652, 0
rotate = -90, 0, 5
archetype = space_solar_pnl
parent = om11_04

[Object]
nickname = om11_04_panel04
pos = 200, -652, 0
rotate = 90, 0, 0
archetype = space_solar_pnl
parent = om11_04

[Object]
nickname = om11_04_panel05
pos = 250, -405, 50
rotate = 135, 0, 100
archetype = space_panel_damaged_01
parent = om11_04

[Object]
nickname = om11_04_panel06
pos = 200, -391, 0
rotate = 90, -45, 5
archetype = space_solar_pnl
parent = om11_04

[Object]
nickname = om11_04_panel07
pos = 200, -398, 0
rotate = -90, 45, -5
archetype = space_solar_pnl
parent = om11_04

[Object]
nickname = om11_04_panel08
pos = 200, -399, 0
rotate = -90, -45, -4
archetype = space_solar_pnl
parent = om11_04

[Object]
nickname = om11_04_tanks01
pos = 250, -850, 0
rotate = 0, 180, 20
archetype = space_tanklx4_dmg
parent = om11_04
'''


class OchoRiosResearch(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'co_och_04'
    TEMPLATE = '''[Object]
nickname = co_och_04
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_police01
{dock_props}

[Object]
nickname = co_och_04_dome01
pos = 0, 402, 0
rotate = 0, 0, 0
archetype = space_domea
parent = co_och_04

[Object]
nickname = co_och_04_ctrl_twr01
pos = 0, 372, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = co_och_04

[Object]
nickname = co_och_04_ctrl_twr02
pos = 0, 192, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = co_och_04

[Object]
nickname = co_och_04_panel01
pos = 0, 192, -120
rotate = -90, 0, 0
archetype = space_solar_pnl
parent = co_och_04

[Object]
nickname = co_och_04_panel02
pos = 0, 192, 120
rotate = 90, 0, 0
archetype = space_solar_pnl
parent = co_och_04

[Object]
nickname = co_och_04_ind01
pos = 0, 282, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = co_och_04

[Object]
nickname = co_och_04_ind02
pos = 0, 172, 0
rotate = 90, 0, 0
archetype = space_industrialc
parent = co_och_04

[Object]
nickname = co_och_04_ctrl_block01
pos = 0, -89, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = co_och_04

[Object]
nickname = co_och_04_habitat01
pos = 100, 282, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_och_04

[Object]
nickname = co_och_04_habitat02
pos = -100, 282, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_och_04

[Object]
nickname = co_och_04_habitat03
pos = 0, 282, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_och_04

[Object]
nickname = co_och_04_habitat04
pos = 0, 282, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_och_04
'''


class MadridProduction(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'co_mad_03'
    TEMPLATE = '''[Object]
nickname = co_mad_03
pos = 0, 0, 0
rotate = 0, 170, -10
archetype = space_police02_production
{dock_props}

[Object]
nickname = co_mad_03_dock_connect
pos = 0, 0, 10
rotate = 90, -10, -10
archetype = space_medium_control_tower
parent = co_mad_03

[Object]
nickname = co_mad_03_arch
pos = 66, -2, -374
rotate = 10, -15, -103
archetype = space_long_large_arch
parent = co_mad_03

[Object]
nickname = co_mad_03_core
pos = 25, -5, -140
rotate = -10, -145, 0
archetype = sw_center_150
parent = co_mad_03

[Object]
nickname = co_mad_03_ind01
pos = 215, -25, -340
rotate = 10, 80, 0
archetype = space_industrial01a
parent = co_mad_03

[Object]
nickname = co_mad_03_ind02
pos = -85, 25, -390
rotate = 10, 80, 0
archetype = space_industrial01a
parent = co_mad_03

[Object]
nickname = co_mad_03_ind03
pos = 55, -2, -295
rotate = 100, 80, 0
archetype = space_industrial02d
parent = co_mad_03

[Object]
nickname = co_mad_03_LEFT_side
pos = -95, 17, -162
rotate = 80, -100, 0
archetype = space_medium_control_tower
loadout = co_ring_horizontal_side
parent = co_mad_03

[Object]
nickname = co_mad_03_RIGHT_side
pos = 145, -35, -120
rotate = 100, -280, 0
archetype = space_medium_control_tower
loadout = co_ring_horizontal_side
parent = co_mad_03

[Object]
nickname = co_mad_03_TOP_side
pos = 50, 145, -133
rotate = 0, -10, -10
archetype = space_control_tower
loadout = co_ring_vertical_side
parent = co_mad_03

[Object]
nickname = co_mad_03_BOTTOM_side
pos = -5, -155, -145
rotate = 0, 10, -190
archetype = space_control_tower
loadout = co_ring_vertical_side
parent = co_mad_03
'''



class CadizFreeport(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'co_cad_03'
    TEMPLATE = '''[Object]
nickname = co_cad_03
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_police01
{dock_props}

[Object]
nickname = co_cad_03_DOCK_habitat01
pos = 0, -300, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_03

[Object]
nickname = co_cad_03_DOCK_habitat01
pos = 0, -220, 0
rotate = 90, 0, 0
archetype = space_girder
parent = co_cad_03

[Object]
nickname = co_cad_03_CORE_tube01
pos = 0, -525, 0
rotate = 90, 0, 0
archetype = space_short_tube_station_root
parent = co_cad_03

[Object]
nickname = co_cad_03_CORE_ind01
pos = 0, -450, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = co_cad_03

[Object]
nickname = co_cad_03_CORE_ind02
pos = 0, -900, -150
rotate = 0, 0, 0
archetype = space_industriala
parent = co_cad_03

[Object]
nickname = co_cad_03_CORE_ind03
pos = 0, -900, 150
rotate = 0, 0, 0
archetype = space_industriala
parent = co_cad_03

[Object]
nickname = co_cad_03_CORE_ind04
pos = 0, -900, 0
rotate = 0, 90, 250
archetype = space_industrial
parent = co_cad_03

[Object]
nickname = co_cad_03_CORE_ind05
pos = 0, -900, 0
rotate = 0, 90, -70
archetype = space_industrial
parent = co_cad_03

[Object]
nickname = co_cad_03_BOTTOM_airlock01_top
pos = 0, -700, 450
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cad_03

[Object]
nickname = co_cad_03_BOTTOM_airlock01
pos = 0, -750, 450
rotate = 90, 0, 0
archetype = space_airlock_dummy
parent = co_cad_03

[Object]
nickname = co_cad_03_BOTTOM_ctrl_twr01
pos = 0, -900, 450
rotate = 0, 0, 0
archetype = space_control_tower
parent = co_cad_03

[Object]
nickname = co_cad_03_BOTTOM_ctrl_twr02
pos = 0, -870, 450
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = co_cad_03

[Object]
nickname = co_cad_03_BOTTOM_ctrl_twr03
pos = 0, -930, 450
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = co_cad_03

[Object]
nickname = co_cad_03_BOTTOM_ctrl_twr04
pos = 0, -1125, 450
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = co_cad_03

[Object]
nickname = co_cad_03_BOTTOM_ctrl_twr05
pos = 0, -1300, 450
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cad_03

[Object]
nickname = co_cad_03_BOTTOM_ctrl_block01
pos = 0, -1465, 450
rotate = 180, 0, 0
archetype = space_small_control_block
parent = co_cad_03

[Object]
nickname = co_cad_03_BOTTOM_habitat01
pos = -50, -1027, 450
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_03

[Object]
nickname = co_cad_03_BOTTOM_habitat02
pos = 50, -1027, 450
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_03

[Object]
nickname = co_cad_03_BOTTOM_habitat03
pos = 0, -1027, 500
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_03

[Object]
nickname = co_cad_03_BOTTOM_habitat04
pos = 0, -1027, 400
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_03

[Object]
nickname = co_cad_03_BOTTOM_habitat05
pos = -40, -1223, 450
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_03

[Object]
nickname = co_cad_03_BOTTOM_habitat06
pos = 40, -1223, 450
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_03

[Object]
nickname = co_cad_03_BOTTOM_habitat07
pos = 0, -1223, 490
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_03

[Object]
nickname = co_cad_03_BOTTOM_habitat08
pos = 0, -1223, 410
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_03

[Object]
nickname = co_cad_03_BOTTOM_habitat09
pos = 0, -1380, 450
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_03

[Object]
nickname = co_cad_03_BOTTOM_panel01
pos = 0, -825, 565
rotate = 0, 90, 0
archetype = space_panel45
parent = co_cad_03

[Object]
nickname = co_cad_03_BOTTOM_panel02
pos = 0, -825, 335
rotate = 0, -90, 0
archetype = space_panel45
parent = co_cad_03

[Object]
nickname = co_cad_03_BOTTOM_panel03
pos = -115, -825, 450
rotate = 0, 0, 0
archetype = space_panel45
parent = co_cad_03

[Object]
nickname = co_cad_03_BOTTOM_panel04
pos = 115, -825, 450
rotate = 0, 180, 0
archetype = space_panel45
parent = co_cad_03

[Object]
nickname = co_cad_03_TOP_airlock01_top
pos = 0, -700, -450
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cad_03

[Object]
nickname = co_cad_03_TOP_airlock01
pos = 0, -750, -450
rotate = 90, 0, 0
archetype = space_airlock_dummy
parent = co_cad_03

[Object]
nickname = co_cad_03_TOP_ctrl_twr01
pos = 0, -900, -450
rotate = 0, 0, 0
archetype = space_control_tower
parent = co_cad_03

[Object]
nickname = co_cad_03_TOP_ctrl_twr02
pos = 0, -870, -450
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = co_cad_03

[Object]
nickname = co_cad_03_TOP_ctrl_twr03
pos = 0, -930, -450
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = co_cad_03

[Object]
nickname = co_cad_03_TOP_ctrl_twr04
pos = 0, -1125, -450
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = co_cad_03

[Object]
nickname = co_cad_03_TOP_ctrl_twr05
pos = 0, -1300, -450
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cad_03

[Object]
nickname = co_cad_03_TOP_ctrl_block01
pos = 0, -1465, -450
rotate = 180, 0, 0
archetype = space_small_control_block
parent = co_cad_03

[Object]
nickname = co_cad_03_TOP_habitat01
pos = -50, -1027, -450
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_03

[Object]
nickname = co_cad_03_TOP_habitat02
pos = 50, -1027, -450
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_03

[Object]
nickname = co_cad_03_TOP_habitat03
pos = 0, -1027, -500
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_03

[Object]
nickname = co_cad_03_TOP_habitat04
pos = 0, -1027, -400
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_03

[Object]
nickname = co_cad_03_TOP_habitat05
pos = -40, -1223, -450
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_03

[Object]
nickname = co_cad_03_TOP_habitat06
pos = 40, -1223, -450
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_03

[Object]
nickname = co_cad_03_TOP_habitat07
pos = 0, -1223, -490
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_03

[Object]
nickname = co_cad_03_TOP_habitat08
pos = 0, -1223, -410
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_03

[Object]
nickname = co_cad_03_TOP_habitat09
pos = 0, -1380, -450
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_03

[Object]
nickname = co_cad_03_TOP_panel01
pos = 0, -825, -565
rotate = 0, -90, 0
archetype = space_panel45
parent = co_cad_03

[Object]
nickname = co_cad_03_TOP_panel02
pos = 0, -825, -335
rotate = 0, 90, 0
archetype = space_panel45
parent = co_cad_03

[Object]
nickname = co_cad_03_TOP_panel03
pos = -115, -825, -450
rotate = 0, 0, 0
archetype = space_panel45
parent = co_cad_03

[Object]
nickname = co_cad_03_TOP_panel04
pos = 115, -825, -450
rotate = 0, 180, 0
archetype = space_panel45
parent = co_cad_03

[Object]
nickname = co_cad_03_RIGHT_ind01
pos = 250, -575, 0
rotate = 0, 0, 45
archetype = space_industrial02a
parent = co_cad_03

[Object]
nickname = co_cad_03_RIGHT_ind02
pos = 400, -900, 0
rotate = 90, 0, 0
archetype = space_industrial02a
parent = co_cad_03

[Object]
nickname = co_cad_03_RIGHT_ind03
pos = 400, -1350, 0
rotate = -90, 0, 0
archetype = space_industrial02
parent = co_cad_03

[Object]
nickname = co_cad_03_RIGHT_ind04
pos = 200, -900, 0
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_cad_03

[Object]
nickname = co_cad_03_RIGHT_ind05
pos = 135, -1350, 0
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_cad_03

[Object]
nickname = co_cad_03_RIGHT_girder01
pos = 235, -530, 0
rotate = 90, 0, 35
archetype = space_girdera
parent = co_cad_03

[Object]
nickname = co_cad_03_RIGHT_girder02
pos = 300, -580, 0
rotate = -90, 0, 60
archetype = space_girdera
parent = co_cad_03

[Object]
nickname = co_cad_03_RIGHT_girder03
pos = 250, -575, 0
rotate = 135, 90, 0
archetype = space_girdera
parent = co_cad_03

[Object]
nickname = co_cad_03_RIGHT_girder04
pos = 200, -1350, 0
rotate = 0, 90, 0
archetype = space_girder
parent = co_cad_03

[Object]
nickname = co_cad_03_LEFT_ind01
pos = -250, -575, 0
rotate = 0, 0, 45
archetype = space_industrial02a
parent = co_cad_03

[Object]
nickname = co_cad_03_LEFT_ind02
pos = -400, -900, 0
rotate = 90, 0, 0
archetype = space_industrial02a
parent = co_cad_03

[Object]
nickname = co_cad_03_LEFT_ind03
pos = -400, -1350, 0
rotate = -90, 0, 0
archetype = space_industrial02
parent = co_cad_03

[Object]
nickname = co_cad_03_LEFT_ind04
pos = -200, -900, 0
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_cad_03

[Object]
nickname = co_cad_03_LEFT_ind05
pos = -135, -1350, 0
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_cad_03

[Object]
nickname = co_cad_03_LEFT_girder01
pos = -235, -530, 0
rotate = 90, 0, -35
archetype = space_girdera
parent = co_cad_03

[Object]
nickname = co_cad_03_LEFT_girder02
pos = -300, -580, 0
rotate = -90, 0, -60
archetype = space_girdera
parent = co_cad_03

[Object]
nickname = co_cad_03_LEFT_girder03
pos = -250, -575, 0
rotate = 45, 90, 0
archetype = space_girdera
parent = co_cad_03

[Object]
nickname = co_cad_03_LEFT_girder04
pos = -200, -1350, 0
rotate = 0, 90, 0
archetype = space_girder
parent = co_cad_03
'''


class NeutronResearch(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'tau26_02'
    TEMPLATE = '''[Object]
nickname = tau26_02
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_police01
{dock_props}

[Object]
nickname = tau26_02_industrial01
pos = 0, -280, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = tau26_02

[Object]
nickname = tau26_02_industrial02
pos = -120, -280, 0
rotate = 0, 0, 0
archetype = space_industrial01a
parent = tau26_02

[Object]
nickname = tau26_02_industrial03
pos = 120, -280, 0
rotate = 0, 0, 0
archetype = space_industrial01a
parent = tau26_02

[Object]
nickname = tau26_02_girder01
pos = 0, -330, 0
rotate = -90, 0, 0
archetype = space_girdera
parent = tau26_02

[Object]
nickname = tau26_02_girder02
pos = 0, -280, -100
rotate = 0, 0, 0
archetype = space_girdera
parent = tau26_02

[Object]
nickname = tau26_02_girder03
pos = -100, -280, 0
rotate = 0, 90, 0
archetype = space_girdera
parent = tau26_02

[Object]
nickname = tau26_02_girder04
pos = 0, -280, 100
rotate = 0, 180, 0
archetype = space_girdera
parent = tau26_02

[Object]
nickname = tau26_02_girder05
pos = 100, -280, 0
rotate = 0, -90, 0
archetype = space_girdera
parent = tau26_02

[Object]
nickname = tau26_02_panel01
pos = -252, -280, 0
rotate = 0, 0, 0
archetype = space_panel
parent = tau26_02

[Object]
nickname = tau26_02_panel02
pos = 252, -280, 0
rotate = 0, 0, 0
archetype = space_panel
parent = tau26_02

[Object]
nickname = tau26_02_panel03
pos = 0, -280, 252
rotate = 0, 90, 0
archetype = space_panel
parent = tau26_02

[Object]
nickname = tau26_02_panel04
pos = 0, -280, -252
rotate = 0, 90, 0
archetype = space_panel
parent = tau26_02

[Object]
nickname = tau26_02_panel05
pos = -175, -280, 175
rotate = 0, 45, 0
archetype = space_panel
parent = tau26_02

[Object]
nickname = tau26_02_panel06
pos = -175, -280, -175
rotate = 0, -45, 0
archetype = space_panel
parent = tau26_02

[Object]
nickname = tau26_02_panel07
pos = 175, -280, 175
rotate = 0, -45, 0
archetype = space_panel
parent = tau26_02

[Object]
nickname = tau26_02_panel08
pos = 175, -280, -175
rotate = 0, 45, 0
archetype = space_panel
parent = tau26_02

[Object]
nickname = tau26_02_ctrl_twr01
pos = 0, -200, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = tau26_02

[Object]
nickname = tau26_02_ctrl_twr02
pos = 0, -360, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = tau26_02

[Object]
nickname = tau26_02_ctrl_twr03
pos = 0, -100, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = tau26_02

[Object]
nickname = tau26_02_tanks01
pos = 0, -480, 0
rotate = 0, 0, 0
archetype = space_tanklx4
parent = tau26_02

[Object]
nickname = tau26_02_tanks02
pos = 0, -522.5, 150
rotate = 0, 0, 0
archetype = space_tankl2
parent = tau26_02

[Object]
nickname = tau26_02_tanks03
pos = 0, -522.5, -150
rotate = 0, 0, 0
archetype = space_tankl2
parent = tau26_02

[Object]
nickname = tau26_02_tanks04
pos = -150, -522.5, 0
rotate = 0, 90, 0
archetype = space_tankl2
parent = tau26_02

[Object]
nickname = tau26_02_tanks05
pos = 150, -522.5, 0
rotate = 0, 90, 0
archetype = space_tankl2
parent = tau26_02
'''
