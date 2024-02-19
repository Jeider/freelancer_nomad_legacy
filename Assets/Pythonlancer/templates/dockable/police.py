from templates.space_object_template import SpaceObjectTemplate


class PoliceOutpostBretonia(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'tau37_04'
    TEMPLATE = '''[Object]
nickname = tau37_04
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_police01
{dock_props}

[Object]
nickname = tau37_04_ind01
pos = 0, 525, -75
rotate = 0, 90, 0
archetype = space_industriala
parent = tau37_04

[Object]
nickname = tau37_04_ind02
pos = 0, 525, 75
rotate = 0, 90, 0
archetype = space_industriala
parent = tau37_04

[Object]
nickname = tau37_04_ind03
pos = 140, 525, 0
rotate = 0, 0, 90
archetype = space_industrial02d
parent = tau37_04

[Object]
nickname = tau37_04_ind04
pos = -140, 525, 0
rotate = 0, 0, 90
archetype = space_industrial02d
parent = tau37_04

[Object]
nickname = tau37_04_ind05
pos = 450, 555, 0
rotate = 0, -90, 0
archetype = space_dome ;space_industrial01
;loadout = space_ind01_reactor
parent = tau37_04

[Object]
nickname = tau37_04_ind06
pos = -450, 555, 0
rotate = 0, 90, 0
archetype = space_dome ;space_industrial01
;loadout = space_ind01_reactor
parent = tau37_04

[Object]
nickname = tau37_04_ind07
pos = 0, 315, 0
rotate = -90, 0, 0
archetype = space_industrialc
parent = tau37_04

[Object]
nickname = tau37_04_ind08
pos = 0, 275, 0
rotate = 90,45, 0
archetype = space_industrialc
parent = tau37_04

[Object]
nickname = tau37_04_ind09
pos = 0, 555, 425
rotate = 0, 180, 0
archetype = space_dome ;space_industrial01
;loadout = space_ind01_reactor
parent = tau37_04

[Object]
nickname = tau37_04_ind10
pos = 0, 555, -425
rotate = 0, 0, 0
archetype = space_dome ;space_industrial01
;loadout = space_ind01_reactor
parent = tau37_04

[Object]
nickname = tau37_04_girder01
pos = 0, 535, -400
rotate = 45, 0, 0
archetype = space_girdera
parent = tau37_04

[Object]
nickname = tau37_04_girder02
pos = 0, 535, 400
rotate = 45, 180, 0
archetype = space_girdera
parent = tau37_04

[Object]
nickname = tau37_04_girder03
pos = -400, 535, 0
rotate = 45, 90, 0
archetype = space_girdera
parent = tau37_04

[Object]
nickname = tau37_04_girder04
pos = 400, 535, 0
rotate = 45, -90, 0
archetype = space_girdera
parent = tau37_04

[Object]
nickname = tau37_04_tank01
pos = 0, 215, -120
rotate = 90, 0, 0
archetype = space_tanks4
parent = tau37_04

[Object]
nickname = tau37_04_tank02
pos = -120, 215, 0
rotate = 90, 90, 0
archetype = space_tanks4
parent = tau37_04

[Object]
nickname = tau37_04_tank03
pos = 0, 215, 120
rotate = -90, 0, 0
archetype = space_tanks4
parent = tau37_04

[Object]
nickname = tau37_04_tank04
pos = 120, 215, 0
rotate = 90, -90, 0
archetype = space_tanks4
parent = tau37_04

[Object]
nickname = tau37_04_ctrltwr01
pos = 0, 455, 0
rotate = 0, 45, 0
archetype = space_control_tower
parent = tau37_04

[Object]
nickname = tau37_04_ctrltwr02
pos = 0, 295, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = tau37_04

[Object]
nickname = tau37_04_ctrltwr04
pos = 0, 150, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = tau37_04

[Object]
nickname = tau37_04_ctrltwr03
pos = 0, 585, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = tau37_04

[Object]
nickname = tau37_04_dome01
pos = 0, 700, 0
rotate = 0, 0, 0
archetype = space_large_dome
parent = tau37_04

[Object]
nickname = tau37_04_habitat01
pos = -150, 375, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau37_04

[Object]
nickname = tau37_04_habitat02
pos = 150, 375, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau37_04

[Object]
nickname = tau37_04_habitat03
pos = 0, 375, 150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau37_04

[Object]
nickname = tau37_04_habitat04
pos = 0, 375, -150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau37_04

[Object]
nickname = tau37_04_habitat05
pos = -110, 375, 110
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau37_04

[Object]
nickname = tau37_04_habitat06
pos = 110, 375, 110
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau37_04

[Object]
nickname = tau37_04_habitat07
pos = -110, 375, -110
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau37_04

[Object]
nickname = tau37_04_habitat08
pos = 110, 375, -110
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau37_04
'''



class SigmaEightPoliceOutpost(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'sig8_04'
    TEMPLATE = '''[Object]
nickname = sig8_04
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = space_police01_front_dock
{dock_props}

[Object]
nickname = sig8_04_space_control_block
pos = 0, -88, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = sig8_04

[Object]
nickname = sig8_04_space_ind01
pos = 0, 0, 170
rotate = 0, 0, 0
archetype = space_industriala
loadout = space_ind_girder
parent = sig8_04

[Object]
nickname = sig8_04_space_ind02
pos = 0, 0, 420
rotate = 0, 0, 0
archetype = space_industriala
loadout = space_ind_girder
parent = sig8_04

[Object]
nickname = sig8_04_shipyard
pos = 0, 0, 580
rotate = 90, 0, 90
archetype = shipyard_medium
parent = sig8_04
'''



class StuttgartPoliceOutpost(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_stut_03'
    TEMPLATE = '''[Object]
nickname = rh_stut_03
pos = 0, 0, 0
rotate = 0, -45, 0
archetype = space_police01
{dock_props}

[Object]
nickname = rh_stut_03_industrial01
pos = 280, 0, 280
rotate = 90, 0, 0
archetype = space_industriala
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_industrial02
pos = 280, 0, 280
rotate = 90, 45, 0
archetype = space_industriala
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_girder01
pos = 280, 0, 280
rotate = 0, 90, 0
archetype = space_girder
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_girder02
pos = 280, 0, 280
rotate = 0, 0, 0
archetype = space_girder
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_girder03
pos = 160, 0, 160
rotate = 0, 45, 0
archetype = space_girder
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_girder04
pos = 380, 0, 380
rotate = 0, 45, 0
archetype = space_girder
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_girder05
pos = 180, 0, 380
rotate = 0, -45, 0
archetype = space_girder
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_girder06
pos = 380, 0, 180
rotate = 0, -45, 0
archetype = space_girder
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_girder07
pos = 50, 0, 510
rotate = 90, 45, 0
archetype = space_girder
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_girder08
pos = 510, 0, 50
rotate = 90,45,0
archetype = space_girder
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_dome01
pos = 560, 37, 560
rotate = 0, -135, 0
archetype = space_dome
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_habitat01
pos = 280, -255, 280
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_habitat02
pos = 280, 255, 280
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_habitat03
pos = 280, 375, 280
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_habitat04
pos = 280, -315, 280
rotate = 180, 45, 0
archetype = space_habitat_tall
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_controller01
pos = 280, 160, 280
rotate = 0, 90, 0
archetype = space_control_tower
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_controller02
pos = 280, -160, 280
rotate = 0, 90, 0
archetype = space_control_tower
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_tank01
pos = 280, 78, 98
rotate = 90, 90, 0
archetype = space_tanks4x4
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_tank02
pos = 280, 78, 462
rotate = 90, 90, 0
archetype = space_tanks4x4
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_tank03
pos = 98, 78, 280
rotate = 90,0,0
archetype = space_tanks4x4
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_tank04
pos = 462, 78, 280
rotate = 90, 0, 0
archetype = space_tanks4x4
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_tank05
pos = 280, -78, 98
rotate = 90, 90, 0
archetype = space_tanks4x4
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_tank06
pos = 280, -78, 462
rotate = 90, 90, 0
archetype = space_tanks4x4
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_tank07
pos = 98, -78, 280
rotate = 90,0,0
archetype = space_tanks4x4
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_tank08
pos = 462, -78, 280
rotate = 90, 0, 0
archetype = space_tanks4x4
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_tank01a
pos = 280, 78, 57
rotate = 90, 0, 0
archetype = space_tanks4
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_tank02a
pos = 280, 78, 503
rotate = 90, 180, 0
archetype = space_tanks4
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_tank03a
pos = 57, 78, 280
rotate = 90,90,0
archetype = space_tanks4
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_tank04a
pos = 503, 78, 280
rotate = 90, -90, 0
archetype = space_tanks4
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_tank05a
pos = 280, -78, 57
rotate = 90, 0, 0
archetype = space_tanks4
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_tank06a
pos = 280, -78, 503
rotate = 90, 180, 0
archetype = space_tanks4
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_tank07a
pos = 57, -78, 280
rotate = 90,90,0
archetype = space_tanks4
parent = Rh_stut_03

[Object]
nickname = rh_stut_03_tank08a
pos = 503, -78, 280
rotate = 90, -90, 0
archetype = space_tanks4
parent = Rh_stut_03
'''


class BerlinPoliceOutpost(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_ber_06'
    TEMPLATE = '''[Object]
nickname = rh_ber_06
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_police01
{dock_props}

[Object]
nickname = rh_ber_06_ctrl_twr01
pos = 0, -150, 180
rotate = 0, 0, 0
archetype = space_control_tower
parent = rh_ber_06

[Object]
nickname = rh_ber_06_ctrl_twr02
pos = 0, -350, 180
rotate = 0, 0, 0
archetype = space_control_tower
parent = rh_ber_06

[Object]
nickname = rh_ber_06_ctrl_twr03a
pos = 0, -665, 180
rotate = 180, 0, 0
archetype = space_small_control_block
parent = rh_ber_06

[Object]
nickname = rh_ber_06_ctrl_twr03
pos = 0, -600, 180
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = rh_ber_06

[Object]
nickname = rh_ber_06_ctrl_twr04
pos = 0, -50, 360
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = rh_ber_06

[Object]
nickname = rh_ber_06_ctrl_twr06
pos = 0, -125, 180
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = rh_ber_06

[Object]
nickname = rh_ber_06_shipyard01
pos = -100, -520, 60
rotate = -75, 0, 90
archetype = shipyard_medium
parent = rh_ber_06

[Object]
nickname = rh_ber_06_shipyard02
pos = -100, -520, 300
rotate = 105, 0, -90
archetype = shipyard_medium
parent = rh_ber_06

[Object]
nickname = rh_ber_06_industrial01
pos = 200, -150, 180
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_ber_06

[Object]
nickname = rh_ber_06_industrial02
pos = 0, -250, 180
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = rh_ber_06

[Object]
nickname = rh_ber_06_industrial03
pos = 130, -170, 35
rotate = 0, 60, 0
archetype = space_industriala
parent = rh_ber_06

[Object]
nickname = rh_ber_06_industrial04
pos = 130, -170, 325
rotate = 0, -60, 0
archetype = space_industriala
parent = rh_ber_06

[Object]
nickname = rh_ber_06_industrial05
pos = -180, -250, 180
rotate = 90, 0, 0
archetype = space_industrial02a
parent = rh_ber_06

[Object]
nickname = rh_ber_06_industrial06
pos = -215, -480, 180
rotate = 90, 90, 0
archetype = space_industrial02d
parent = rh_ber_06

[Object]
nickname = rh_ber_06_industrial07
pos = 0, -250, 0
rotate = 90, 0, 0
archetype = space_industrial02a
parent = rh_ber_06

[Object]
nickname = rh_ber_06_industrial08
pos = 0, -480, -35
rotate = 90, 0, 0
archetype = space_industrial02d
parent = rh_ber_06

[Object]
nickname = rh_ber_06_industrial09
pos = 0, -250, 360
rotate = 90, 0, 0
archetype = space_industrial02a
parent = rh_ber_06

[Object]
nickname = rh_ber_06_industrial10
pos = 0, -480, 395
rotate = 90, 0, 0
archetype = space_industrial02d
parent = rh_ber_06

[Object]
nickname = rh_ber_06_industrial11
pos = 0, -480, 180
rotate = 90, 0, 0
archetype = space_industriala
parent = rh_ber_06

[Object]
nickname = rh_ber_06_tank01
pos = 50, -350, -35
rotate = 90, -120, 0
archetype = space_tankl4
parent = rh_ber_06

[Object]
nickname = rh_ber_06_tank02
pos = 50, -350, 395
rotate = 90, -60, 0
archetype = space_tankl4
parent = rh_ber_06

[Object]
nickname = rh_ber_06_habitat01
pos = 200, -50, 180
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_ber_06

[Object]
nickname = rh_ber_06_habitat02
pos = 200, 50, 180
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = rh_ber_06

[Object]
nickname = rh_ber_06_habitat03
pos = 200, -50, 270
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = rh_ber_06

[Object]
nickname = rh_ber_06_habitat04
pos = 0, -75, 360
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_ber_06

[Object]
nickname = rh_ber_06_habitat05
pos = 0, -14, 360
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = rh_ber_06

[Object]
nickname = rh_ber_06_habitat06
pos = 0, -180, 0
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = rh_ber_06
'''


class OmicronPoliceOutpost(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'om2_03'
    TEMPLATE = '''[Object]
nickname = om2_03
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = space_police01_front_dock
{dock_props}

[Object]
nickname = om2_03_control_tower01
pos = 0, 0, 90
rotate = 0, 0, 90
archetype = space_small_control_tower
parent = om2_03

[Object]
nickname = om2_03_control_tower02
pos = 0, 0, 280
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = om2_03

[Object]
nickname = om2_03_control_dome01
pos = 0, 40, 280
rotate = 0, 90, 0
archetype = space_domea
parent = om2_03

[Object]
nickname = om2_03_control_dome02
pos = 0, -40, 280
rotate = 180, 90, 0
archetype = space_domea
parent = om2_03

[Object]
nickname = om2_03_control_control01
pos = 0, -90, 0
rotate = 180, 90, 0
archetype = space_small_control_block
parent = om2_03

[Object]
nickname = om2_03_control_habitat01
pos = 0, 0, 140
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = om2_03

[Object]
nickname = om2_03_control_habitat02
pos = 0, 0, 400
rotate = 90, 0, 0
archetype = space_habitat_tall
parent = om2_03
'''


class PoliceOutpostLiberty(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_cal_06'
    TEMPLATE = '''[Object]
nickname = li_cal_06
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_police01
{dock_props}

[Object]
nickname = li_cal_06_shipyard01
pos = -800, 60, 0
rotate = 0, 0, 0
archetype = shipyard_medium
parent = li_cal_06

[Object]
nickname = li_cal_06_shipyard02
pos = -800, -60, 0
rotate = 0, 0, 180
archetype = shipyard_medium
parent = li_cal_06

[Object]
nickname = li_cal_06_panel01
pos = -400, 135, -100
rotate = -75, 0, 0
archetype = space_station_panel
loadout = co_dread_panel_with_windows
parent = li_cal_06

[Object]
nickname = li_cal_06_panel02
pos = -500, 135, 0
rotate = -75, 90, 0
archetype = space_station_panel
loadout = co_dread_panel_with_windows
parent = li_cal_06

[Object]
nickname = li_cal_06_panel03
pos = -300, 135, 0
rotate = -75, -90, 0
archetype = space_station_panel
loadout = co_dread_panel_with_windows
parent = li_cal_06

[Object]
nickname = li_cal_06_panel04
pos = -400, 135, 100
rotate = -75, 180, 0
archetype = space_station_panel
loadout = co_dread_panel_with_windows
parent = li_cal_06

[Object]
nickname = li_cal_06_panel05
pos = -400, -135, -100
rotate = -75, 0, 180
archetype = space_station_panel
loadout = co_dread_panel_with_windows
parent = li_cal_06

[Object]
nickname = li_cal_06_panel06
pos = -500, -135, 0
rotate = -75, -90, 180
archetype = space_station_panel
loadout = co_dread_panel_with_windows
parent = li_cal_06

[Object]
nickname = li_cal_06_panel07
pos = -300, -135, 0
rotate = -75, 90, 180
archetype = space_station_panel
loadout = co_dread_panel_with_windows
parent = li_cal_06

[Object]
nickname = li_cal_06_panel08
pos = -400, -135, 100
rotate = -75, 180, 180
archetype = space_station_panel
loadout = co_dread_panel_with_windows
parent = li_cal_06

[Object]
nickname = li_cal_06_ind01
pos = -485, 0, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = li_cal_06

[Object]
nickname = li_cal_06_ind02
pos = -315, 0, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = li_cal_06

[Object]
nickname = li_cal_06_ind03
pos = -400, 0, -120
rotate = 90, 0, 90
archetype = space_industrial02d
parent = li_cal_06

[Object]
nickname = li_cal_06_ind04
pos = -400, 0, 120
rotate = 90, 0, 90
archetype = space_industrial02d
parent = li_cal_06

[Object]
nickname = li_cal_06_ind05
pos = -800, 0, 0
rotate = 0, 0, 0
archetype = space_industrial02d
parent = li_cal_06

[Object]
nickname = li_cal_06_girder01
pos = -400, 0, 0
rotate = 0, 90, 0
archetype = space_girdera
parent = li_cal_06

[Object]
nickname = li_cal_06_girder02
pos = -400, 0, 0
rotate = 0, -90, 0
archetype = space_girdera
parent = li_cal_06

[Object]
nickname = li_cal_06_ctrl_twr01
pos = -400, 265, 0
rotate = 0, 45, 0
archetype = space_small_control_tower
parent = li_cal_06

[Object]
nickname = li_cal_06_ctrl_twr02
pos = -400, 0, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = li_cal_06

[Object]
nickname = li_cal_06_ctrl_twr03
pos = -400, -265, 0
rotate = 0, -45, 0
archetype = space_small_control_tower
parent = li_cal_06

[Object]
nickname = li_cal_06_dome01
pos = -400, 285, 0
rotate = 0, 45, 0
archetype = space_domeb
parent = li_cal_06

[Object]
nickname = li_cal_06_dome02
pos = -400, -285, 0
rotate = 180, 45, 0
archetype = space_domeb
parent = li_cal_06
'''
