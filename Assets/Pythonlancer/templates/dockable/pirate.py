from templates.space_object_template import SpaceObjectTemplate


class PirateBaseBizmark(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_biz_06'
    TEMPLATE = '''[Object]
nickname = rh_biz_06
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_police01
{dock_props}

[Object]
nickname = rh_biz_06_industrial01
pos = 0, -200, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_biz_06

[Object]
nickname = rh_biz_06_industrial02
pos = 0, -450, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_biz_06

[Object]
nickname = rh_biz_06_industrial03
pos = 0, -725, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_biz_06

[Object]
nickname = rh_biz_06_industrial04
pos = -175, -490, 0
rotate = 0, 0, -60
archetype = space_industriala
parent = rh_biz_06

[Object]
nickname = rh_biz_06_industrial05
pos = 175, -490, 0
rotate = 0, 0, 60
archetype = space_industriala
parent = rh_biz_06

[Object]
nickname = rh_biz_06_industrial06
pos = -315, -250, 0
rotate = 0, 0, -60
archetype = space_industriala
parent = rh_biz_06

[Object]
nickname = rh_biz_06_industrial07
pos = 315, -250, 0
rotate = 0, 0, 60
archetype = space_industriala
parent = rh_biz_06

[Object]
nickname = rh_biz_06_girder01
pos = 0, -200, 0
rotate = 90, 0, 0
archetype = space_girder
parent = rh_biz_06

[Object]
nickname = rh_biz_06_girder02
pos = 0, -600, 0
rotate = 90, 0, 0
archetype = space_girder
parent = rh_biz_06

[Object]
nickname = rh_biz_06_girder03
pos = -25, -750, 0
rotate = -60, -90, 0
archetype = space_girdera
parent = rh_biz_06

[Object]
nickname = rh_biz_06_girder04
pos = 25, -750, 0
rotate = -60, 90, 0
archetype = space_girdera
parent = rh_biz_06

[Object]
nickname = rh_biz_06_girder05
pos = -160, -520, 0
rotate = -60, -90, 0
archetype = space_girdera
parent = rh_biz_06

[Object]
nickname = rh_biz_06_girder06
pos = 160, -520, 0
rotate = -60, 90, 0
archetype = space_girdera
parent = rh_biz_06

[Object]
nickname = rh_biz_06_girder07
pos = 100, -455, 0
rotate = 10, 90, 0
archetype = space_girderc
parent = rh_biz_06

[Object]
nickname = rh_biz_06_girder08
pos = -100, -455, 0
rotate = -10, 90, 0
archetype = space_girderc
parent = rh_biz_06

[Object]
nickname = rh_biz_06_girder09
pos = 150, -208, 0
rotate = 5, 90, 0
archetype = space_girder
parent = rh_biz_06

[Object]
nickname = rh_biz_06_girder10
pos = -150, -208, 0
rotate = -5, 90, 0
archetype = space_girder
parent = rh_biz_06

[Object]
nickname = rh_biz_06_habitat01
pos = 0, -840, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = rh_biz_06
'''


class PirateBaseHokkaido(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_hkd_06'
    TEMPLATE = '''[Object]
nickname = ku_hkd_06
pos = 0, 0, 0
rotate = 0, -90, 0
archetype = space_police02
{dock_props}

[Object]
nickname = ku_hkd_06_ind01
pos = -30, 0, 0
rotate = 90, 0, 0
archetype = space_industrial02a
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_ind02
pos = -30, -130, -100
rotate = 0, 0, 0
archetype = space_industrial02d
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_ind03
pos = -120, -200, -100
rotate = 0, 90, 90
archetype = space_industrial02d
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_ind04
pos = 60, -200, -100
rotate = -90, 90, 0
archetype = space_industrial02d
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_dome01
pos = -30, -70, -150
rotate = 0, 0, 0
archetype = space_domea
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_twr01
pos = -30, -100, -100
rotate = 0, 0, 0
archetype = space_control_tower
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_twr02
pos = -130, 50, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_twr03
pos = -30, -320, -100
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_block01
pos = -130, 110, 0
rotate = 0, 0, 0
archetype = space_pirate_control_block
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_block02
pos = -30, -380, -100
rotate = 180, 0, 0
archetype = space_pirate_control_block
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_habitat01
pos = -130, -40, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_girder01
pos = -30, -210, -100
rotate = 90, 0, 0
archetype = space_girderc
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_tank01
pos = -30, -170, -100
rotate = 90, 0, 90
archetype = space_tanks4x4
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_tank02
pos = -30, -210, -100
rotate = 90, 0, 90
archetype = space_tanks4x4
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_tank03
pos = -30, -250, -100
rotate = 90, 0, 90
archetype = space_tanks4x4
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_tank04
pos = -30, -290, -100
rotate = 90, 0, 90
archetype = space_tanks4x4
parent = ku_hkd_06
'''


class LibertyRombicPirateBase(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'sig17_04'
    TEMPLATE = '''[Object]
nickname = sig17_04
pos = 0, 0, 0
rotate = 0, -90, 0
archetype = space_port_dmg
{dock_props}

[Object]
nickname = sig17_04_industrial01
pos = 0, -300, 0
rotate = 90, 45, 90
archetype = space_industrial02a
parent = sig17_04

[Object]
nickname = sig17_04_industrial02
pos = 0, -480, 0
rotate = 90, 45, 90
archetype = space_industrial02a
parent = sig17_04

[Object]
nickname = sig17_04_industrial03
pos = 0, -390, -90
rotate = 90, -45, 90
archetype = space_industrial02a
parent = sig17_04

[Object]
nickname = sig17_04_industrial04
pos = 0, -390, 90
rotate = 90, 45, 90
archetype = space_industrial02a
parent = sig17_04

[Object]
nickname = sig17_04_industrial05
pos = 0, -390, -200
rotate = 90, 90, 90
archetype = space_industrial02d
parent = sig17_04

[Object]
nickname = sig17_04_industrial06
pos = 0, -390, -310
rotate = 90, -45, 90
archetype = space_industrial02a
parent = sig17_04

[Object]
nickname = sig17_04_industrial07
pos = 0, -390, 200
rotate = 90, 90, 90
archetype = space_industrial02d
parent = sig17_04

[Object]
nickname = sig17_04_industrial08
pos = 0, -390, 310
rotate = 90, -45, 90
archetype = space_industrial02a
parent = sig17_04

[Object]
nickname = sig17_04_tank01
pos = 0, -680, 0
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = sig17_04

[Object]
nickname = sig17_04_tank02
pos = 0, -600, 90
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = sig17_04

[Object]
nickname = sig17_04_tank03
pos = 0, -600, -90
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = sig17_04

[Object]
nickname = sig17_04_panel01
pos = 0, -300, 102
rotate = 0, 90, 0
archetype = space_debris_panel
parent = sig17_04

[Object]
nickname = sig17_04_panel02
pos = 0, -300, -105
rotate = 0, -90, 0
archetype = space_debris_panel
parent = sig17_04
'''


class PirateBaseStuttgart(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_stut_06'
    TEMPLATE = '''[Object]
nickname = rh_stut_06
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_police01
{dock_props}

[Object]
nickname = rh_stut_06_industrial01
pos = -120, -470, 0
rotate = 0, 90, 60
archetype = space_industrial02a
parent = rh_stut_06

[Object]
nickname = rh_stut_06_industrial02
pos = 120, -470, 0
rotate = 0, 90, -60
archetype = space_industrial02a
parent = rh_stut_06

[Object]
nickname = rh_stut_06_industrial03
pos = -120, -470, 200
rotate = 0, 90, 60
archetype = space_industrial02a
parent = rh_stut_06

[Object]
nickname = rh_stut_06_industrial04
pos = 120, -470, 200
rotate = 0, 90, -60
archetype = space_industrial02a
parent = rh_stut_06

[Object]
nickname = rh_stut_06_industrial05
pos = -120, -470, -200
rotate = 0, 90, 60
archetype = space_industrial02a
parent = rh_stut_06

[Object]
nickname = rh_stut_06_industrial06
pos = 120, -470, -200
rotate = 0, 90, -60
archetype = space_industrial02a
parent = rh_stut_06

[Object]
nickname = rh_stut_06_industrial07
pos = 0, -580, 0
rotate = 0, 90, 0
archetype = space_industrial02d
parent = rh_stut_06

[Object]
nickname = rh_stut_06_industrial08
pos = 0, -580, 200
rotate = 0, 90, 0
archetype = space_industrial02d
parent = rh_stut_06

[Object]
nickname = rh_stut_06_industrial09
pos = 0, -580, -200
rotate = 0, 90, 0
archetype = space_industrial02d
parent = rh_stut_06

[Object]
nickname = rh_stut_06_industrial10
pos = 0, -330, 135
rotate = 0, 0, 45
archetype = space_industrial02a
parent = rh_stut_06

[Object]
nickname = rh_stut_06_industrial11
pos = 0, -330, -135
rotate = 0, 0, 45
archetype = space_industrial02a
parent = rh_stut_06

[Object]
nickname = rh_stut_06_industrial12
pos = 0, -200, 0
rotate = 0, 90, 90
archetype = space_industrial02d
parent = rh_stut_06

[Object]
nickname = rh_stut_06_industrial13
pos = 0, -730, 0
rotate = 0, 90, 90
archetype = space_industrial02d
parent = rh_stut_06

[Object]
nickname = rh_stut_06_control_block01
pos = 0, -900, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = rh_stut_06

[Object]
nickname = rh_stut_06_girder01
pos = -120, -470, 0
rotate = 0, 0, 60
archetype = space_girder
parent = rh_stut_06

[Object]
nickname = rh_stut_06_girder02
pos = 120, -470, 0
rotate = 0, 0, 30
archetype = space_girder
parent = rh_stut_06

[Object]
nickname = rh_stut_06_girder03
pos = 0, -580, 0
rotate = 0, 0, 0
archetype = space_girder
parent = rh_stut_06

[Object]
nickname = rh_stut_06_girder04
pos = 0, 0, 0
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_06

[Object]
nickname = rh_stut_06_girder04
pos = 0, 0, 0
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_06
'''


class PirateBaseCambridge(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'br_cam_05'
    TEMPLATE = '''[Object]
nickname = br_cam_05
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_police01
{dock_props}

[Object]
nickname = br_cam_05_ind01
pos = -48, 48, -400
rotate = 0, 0, 45
archetype = space_industriala
parent = br_cam_05

[Object]
nickname = br_cam_05_ind02
pos = 48, 48, -400
rotate = 0, 0, 45
archetype = space_industriala
parent = br_cam_05

[Object]
nickname = br_cam_05_ind03
pos = 48, -48, -400
rotate = 0, 0, 45
archetype = space_industriala
parent = br_cam_05

[Object]
nickname = br_cam_05_ind04
pos = -48, -48, -400
rotate = 0, 0, 45
archetype = space_industriala
parent = br_cam_05

[Object]
nickname = br_cam_05_tank01
pos = 90, 90, -400
rotate = 0, 0, 135
archetype = space_tankl4
parent = br_cam_05

[Object]
nickname = br_cam_05_tank02
pos = -90, 90, -400
rotate = 0, 0, -135
archetype = space_tankl4
parent = br_cam_05

[Object]
nickname = br_cam_05_tank03
pos = 90, -90, -400
rotate = 0, 0, 45
archetype = space_tankl4
parent = br_cam_05

[Object]
nickname = br_cam_05_tank04
pos = -90, -90, -400
rotate = 0, 0, -45
archetype = space_tankl4
parent = br_cam_05

[Object]
nickname = br_cam_05_girder01
pos = 0, 0, -50
rotate = 0, 180, 0
archetype = space_girdera
parent = br_cam_05

[Object]
nickname = br_cam_05_girder02
pos = 0, 0, -280
rotate = 90, 0, -45
archetype = space_girderc
parent = br_cam_05

[Object]
nickname = br_cam_05_girder03
pos = 0, 0, -520
rotate = 90, 0, -45
archetype = space_girderc
parent = br_cam_05
'''


class ManhattanPirateBase(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_mnh_06'
    TEMPLATE = '''[Object]
nickname = li_mnh_06
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = space_police02
{dock_props}

[Object]
nickname = li_mnh_06_indA01
pos = -85, -85, -150
rotate = 45, 90, 0
archetype = space_industriala
parent = li_mnh_06

[Object]
nickname = li_mnh_06_indA02
pos = -85, 85, -150
rotate = -45, 90, 0
archetype = space_industriala
parent = li_mnh_06

[Object]
nickname = li_mnh_06_indA03
pos = 85, 85, -150
rotate = -45, -90, 0
archetype = space_industriala
parent = li_mnh_06

[Object]
nickname = li_mnh_06_indA04
pos = 85, -85, -150
rotate = 45, -90, 0
archetype = space_industriala
parent = li_mnh_06

[Object]
nickname = li_mnh_06_indA05
pos = -85, -85, -250
rotate = 45, 90, 0
archetype = space_industriala
parent = li_mnh_06

[Object]
nickname = li_mnh_06_indA06
pos = -85, 85, -250
rotate = -45, 90, 0
archetype = space_industriala
parent = li_mnh_06

[Object]
nickname = li_mnh_06_indA07
pos = 85, 85, -250
rotate = -45, -90, 0
archetype = space_industriala
parent = li_mnh_06

[Object]
nickname = li_mnh_06_indA08
pos = 85, -85, -250
rotate = 45, -90, 0
archetype = space_industriala
parent = li_mnh_06

[Object]
nickname = li_mnh_06_indA09
pos = -85, -85, -50
rotate = 45, 90, 0
archetype = space_industriala
parent = li_mnh_06

[Object]
nickname = li_mnh_06_indA10
pos = -85, 85, -50
rotate = -45, 90, 0
archetype = space_industriala
parent = li_mnh_06

[Object]
nickname = li_mnh_06_indA11
pos = 85, 85, -50
rotate = -45, -90, 0
archetype = space_industriala
parent = li_mnh_06

[Object]
nickname = li_mnh_06_indA12
pos = 85, -85, -50
rotate = 45, -90, 0
archetype = space_industriala
parent = li_mnh_06

[Object]
nickname = li_mnh_06_indB01
pos = 250, 0, -150
rotate = 0, 90, 0
archetype = space_industrial02d
parent = li_mnh_06

[Object]
nickname = li_mnh_06_indB02
pos = 250, 0, -250
rotate = 0, 90, 0
archetype = space_industrial02d
parent = li_mnh_06

[Object]
nickname = li_mnh_06_indB03
pos = 250, 0, -50
rotate = 0, 90, 0
archetype = space_industrial02d
parent = li_mnh_06

[Object]
nickname = li_mnh_06_indB04
pos = -250, 0, -150
rotate = 0, 90, 0
archetype = space_industrial02d
parent = li_mnh_06

[Object]
nickname = li_mnh_06_indB05
pos = -250, 0, -250
rotate = 0, 90, 0
archetype = space_industrial02d
parent = li_mnh_06

[Object]
nickname = li_mnh_06_indB06
pos = -250, 0, -50
rotate = 0, 90, 0
archetype = space_industrial02d
parent = li_mnh_06

[Object]
nickname = li_mnh_06_indC01
pos = 0, 0, -75
rotate = 0, 0, 0
archetype = space_industrial01a
parent = li_mnh_06

[Object]
nickname = li_mnh_06_tower01
pos = 0, 0, -200
rotate = 90, 0, 0
archetype = space_medium_control_tower
parent = li_mnh_06

[Object]
nickname = li_mnh_06_tower02
pos = 0, 0, -100
rotate = 90, 0, 0
archetype = space_medium_control_tower
parent = li_mnh_06

[Object]
nickname = li_mnh_06_tower03
pos = 0, 0, -300
rotate = 90, 0, 0
archetype = space_medium_control_tower
parent = li_mnh_06

[Object]
nickname = li_mnh_06_tank01
pos = 0, -175, -150
rotate = 0, 0, 0
archetype = space_tankl4
parent = li_mnh_06

[Object]
nickname = li_mnh_06_tank02
pos = 0, 175, -150
rotate = 0, 0, 180
archetype = space_tankl4
parent = li_mnh_06
'''


class PirateBaseForbes(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_for_04'
    TEMPLATE = '''[Object]
nickname = li_for_04
pos = 0, 0, 0
rotate = 90, 0, 0
archetype = space_police02
{dock_props}

[Object]
nickname = li_for_04_cntrl_twr01
pos = 0, -150, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = li_for_04

[Object]
nickname = li_for_04_cntrl_twr02
pos = 0, -250, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = li_for_04

[Object]
nickname = li_for_04_cntrl_twr03
pos = 20, -340, 15
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = li_for_04

[Object]
nickname = li_for_04_cntrl_twr03
pos = 40, -460, -40
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = li_for_04

[Object]
nickname = li_for_04_cntrl_block01
pos = 0, -700, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = li_for_04

[Object]
nickname = li_for_04_ind01
pos = 0, -95, 0
rotate = 90, 0, 0
archetype = space_industrial02a
parent = li_for_04

[Object]
nickname = li_for_04_ind02
pos = 0, -330, 0
rotate = 90, 0, 0
archetype = space_industrial01a
parent = li_for_04

[Object]
nickname = li_for_04_ind03
pos = 0, -430, 0
rotate = 90, 0, 0
archetype = space_industrialc
parent = li_for_04

[Object]
nickname = li_for_04_ind04
pos = -90, -250, 0
rotate = 90, 0, 0
archetype = space_industrial02a
parent = li_for_04

[Object]
nickname = li_for_04_ind05
pos = 0, -165, -95
rotate = 90, 0, 0
archetype = space_industrialc
parent = li_for_04

[Object]
nickname = li_for_04_ind06
pos = 0, -280, 70
rotate = 90, 0, 0
archetype = space_industrial01a
parent = li_for_04

[Object]
nickname = li_for_04_ind07
pos = 95, -250, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = li_for_04

[Object]
nickname = li_for_04_habitat01
pos = 0, -610, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_for_04

[Object]
nickname = li_for_04_habitat02
pos = 0, -350, -95
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_for_04

[Object]
nickname = li_for_04_habitat03
pos = 0, -550, -95
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = li_for_04

[Object]
nickname = li_for_04_habitat04
pos = 0, -475, 70
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_for_04

[Object]
nickname = li_for_04_habitat05
pos = 0, -650, 70
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = li_for_04

[Object]
nickname = li_for_04_habitat06
pos = -95, -420, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_for_04

[Object]
nickname = li_for_04_habitat07
pos = -95, -540, 0
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = li_for_04

[Object]
nickname = li_for_04_habitat08
pos = 95, -430, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_for_04

[Object]
nickname = li_for_04_habitat09
pos = 95, -600, 0
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = li_for_04

[Object]
nickname = li_for_04_panel01
pos = 0, -80, -150
rotate = 0, -90, 0
archetype = space_panel45
parent = li_for_04

[Object]
nickname = li_for_04_panel02
pos = -125, -80, -74
rotate = 0, -30, 0
archetype = space_panel45
parent = li_for_04

[Object]
nickname = li_for_04_panel03
pos = 125, -80, -74
rotate = 0, -150, 0
archetype = space_panel45
parent = li_for_04

[Object]
nickname = li_for_04_panel04
pos = 125, -80, 70
rotate = 0, -210, 0
archetype = space_panel45
parent = li_for_04

[Object]
nickname = li_for_04_girder01
pos = -70, -65, -127.5
rotate = -45, 30, 0
archetype = space_girderc
parent = li_for_04

[Object]
nickname = li_for_04_girder02
pos = 70, -65, -127.5
rotate = -45, -30, 0
archetype = space_girderc
parent = li_for_04

[Object]
nickname = li_for_04_girder03
pos = 145, -65, -2
rotate = -45, -90, 0
archetype = space_girderc
parent = li_for_04

[Object]
nickname = li_for_04_girder04
pos = -145, -65, -2
rotate = -45, 90, 0
archetype = space_girderc
parent = li_for_04

[Object]
nickname = li_for_04_girder05
pos = 70, -65, 127.5
rotate = -45, -150, 0
archetype = space_girderc
parent = li_for_04

[Object]
nickname = li_for_04_girder06
pos = -70, -65, 127.5
rotate = -45, 150, 0
archetype = space_girderc
parent = li_for_04

[Object]
nickname = li_for_04_girder07
pos = -105, -130, -187
rotate = 0, -60, 0
archetype = space_girderc
parent = li_for_04

[Object]
nickname = li_for_04_girder08
pos = 105, -130, -187
rotate = 0, 60, 0
archetype = space_girderc
parent = li_for_04

[Object]
nickname = li_for_04_girder09
pos = 212, -130, -2
rotate = 0, 0, 0
archetype = space_girderc
parent = li_for_04

[Object]
nickname = li_for_04_girder10
pos = -212, -130, -2
rotate = 0, 0, 0
archetype = space_girderc
parent = li_for_04

[Object]
nickname = li_for_04_girder11
pos = -105, -130, 187
rotate = 0, 60, 0
archetype = space_girderc
parent = li_for_04

[Object]
nickname = li_for_04_girder12
pos = 105, -130, 187
rotate = 0, -60, 0
archetype = space_girderc
parent = li_for_04

[Object]
nickname = li_for_04_girder13
pos = -125, -80, 74
rotate = 0, -150, 0
archetype = space_girderc
parent = li_for_04

[Object]
nickname = li_for_04_girder14
pos = 0, -80, 150
rotate = 0, 90, 0
archetype = space_girderc
parent = li_for_04
'''


class PirateBaseColumbia(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_biz_06'
    TEMPLATE = '''[Object]
nickname = li_col_07
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_port_dmg
{dock_props}

[Object]
nickname = li_col_07_ind01
pos = 0, -250, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = li_col_07

[Object]
nickname = li_col_07_ind02
pos = 0, -250, -500
rotate = 0, 0, 0
archetype = space_industrial
parent = li_col_07

[Object]
nickname = li_col_07_ind03
pos = 0, -250, 500
rotate = 180, 0, 0
archetype = space_industrial
parent = li_col_07

[Object]
nickname = li_col_07_ind04
pos = 0, -500, 0
rotate = 0, 0, 0
archetype = space_industrial02d
parent = li_col_07

[Object]
nickname = li_col_07_ind05
pos = 0, -500, 250
rotate = 0, 0, 0
archetype = space_industrial02d
parent = li_col_07

[Object]
nickname = li_col_07_ind06
pos = 0, -500, -250
rotate = 0, 0, 0
archetype = space_industrial02d
parent = li_col_07

[Object]
nickname = li_col_07_girder01
pos = 0, -400, 0
rotate = 90, 0, 0
archetype = space_girderc
parent = li_col_07

[Object]
nickname = li_col_07_girder02
pos = 0, -500, 370
rotate = -55, 0, 0
archetype = space_girdera
parent = li_col_07

[Object]
nickname = li_col_07_girder03
pos = 0, -500, -370
rotate = -55, 180, 0
archetype = space_girdera
parent = li_col_07

[Object]
nickname = li_col_07_tank01
pos = 40, -475, 200
rotate = 0, 0, 180
archetype = space_tankl4
parent = li_col_07

[Object]
nickname = li_col_07_tank02
pos = -40, -475, 200
rotate = 0, 0, 180
archetype = space_tankl4
parent = li_col_07

[Object]
nickname = li_col_07_tank03
pos = 40, -475, -200
rotate = 0, 0, 180
archetype = space_tankl4
parent = li_col_07

[Object]
nickname = li_col_07_tank04
pos = -40, -475, -200
rotate = 0, 0, 180
archetype = space_tankl4
parent = li_col_07
'''


class PirateBaseCalifornia(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_cal_08'
    TEMPLATE = '''[Object]
nickname = li_cal_08
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_police01
{dock_props}

[Object]
nickname = li_cal_08_industrial01
pos = 0, -400, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = li_cal_08

[Object]
nickname = li_cal_08_industrial02
pos = 250, -400, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = li_cal_08

[Object]
nickname = li_cal_08_industrial03
pos = -250, -400, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = li_cal_08

[Object]
nickname = li_cal_08_industrial04
pos = 0, -650, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = li_cal_08

[Object]
nickname = li_cal_08_ctrl_twr01
pos = 0, -200, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = li_cal_08

[Object]
nickname = li_cal_08_girder01
pos = 0, -230, 0
rotate = 90, 0, 0
archetype = space_girder
parent = li_cal_08

[Object]
nickname = li_cal_08_girder02
pos = 0, -400, 0
rotate = 0, 90, 0
archetype = space_girder
parent = li_cal_08

[Object]
nickname = li_cal_08_girder03
pos = 0, -550, 0
rotate = 90, 0, 0
archetype = space_girderc
parent = li_cal_08

[Object]
nickname = li_cal_08_tanks01
pos = 0, -850, 0
rotate = 90, 0, 0
archetype = space_tankl4x4
parent = li_cal_08
'''
