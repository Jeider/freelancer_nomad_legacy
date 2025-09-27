from templates.space_object_template import SpaceObjectTemplate


class KyushuAsteroidBase(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_ksu_05'
    TEMPLATE = '''[Object]
nickname = ku_ksu_05
pos = 0, 0, 0
rotate = 180, 90, 0
archetype = miningbase_small_ice
{dock_props}

[Object]
nickname = ku_ksu_05_ind01
pos = 0, -100, 0
rotate = 90, 0, 0
archetype = space_industrial01b
loadout = space_ind01_reactor
parent = ku_ksu_05

[Object]
nickname = ku_ksu_05_twr01
pos = 0, -150, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = ku_ksu_05

[Object]
nickname = ku_ksu_05_ctrl01
pos = 0, -150, 0
rotate = 180, 0, 0
archetype = space_pirate_control_block
parent = ku_ksu_05

[Object]
nickname = ku_ksu_05_twr02
pos = 0, 30, -90
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = ku_ksu_05

[Object]
nickname = ku_ksu_05_ctrl02
pos = 0, 60, -90
rotate = 0, 0, 0
archetype = space_pirate_control_block
parent = ku_ksu_05

[Object]
nickname = ku_ksu_05_girder01
pos = 0, -100, -85
rotate = 60, 0, 0
archetype = space_girderb
parent = ku_ksu_05

[Object]
nickname = ku_ksu_05_girder02
pos = 80, -95, 0
rotate = 70, -90, 0
archetype = space_girderb
parent = ku_ksu_05

[Object]
nickname = ku_ksu_05_girder03
pos = -80, -95, 0
rotate = 70, 90, 0
archetype = space_girderb
parent = ku_ksu_05

[Object]
nickname = ku_ksu_05_girder04
pos = 0, -90, 75
rotate = -70, 0, 0
archetype = space_girderb
parent = ku_ksu_05

[Object]
nickname = ku_ksu_05_girder05
pos = 30, -20, -95
rotate = 45, 0, 0
archetype = space_girderb
parent = ku_ksu_05

[Object]
nickname = ku_ksu_05_girder06
pos = -30, -20, -95
rotate = 45, 0, 0
archetype = space_girderb
parent = ku_ksu_05
'''


class NomadAsteroidBase(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'sig17_03'
    TEMPLATE = '''[Object]
nickname = sig17_03
pos = 0, 0, 0
rotate = 0, -135, 0
archetype = space_police02
{dock_props}

[Object]
nickname = sig17_03_Ast
pos = -50, 0, -50
rotate = -90, 0, 90
archetype = miningbase_nomad_sattelite
parent = sig17_03

[Object]
nickname = sig17_03_habitat01
pos = -50, 15, -130
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig17_03

[Object]
nickname = sig17_03_habitat02
pos = -50, 120, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig17_03

[Object]
nickname = sig17_03_habitat03
pos = -50, -102, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig17_03

[Object]
nickname = sig17_03_habitat04
pos = -50, 15, -185
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig17_03

[Object]
nickname = sig17_03_habitat05
pos = 0, 15, -150
rotate = 0, 15, 0
archetype = space_habitat_wide
parent = sig17_03

[Object]
nickname = sig17_03_habitat06
pos = -100, 15, -150
rotate = 0, -15, 0
archetype = space_habitat_wide
parent = sig17_03

[Object]
nickname = sig17_03_habitat07
pos = -30, 215, -140
rotate = 0, 90, 0
archetype = space_habitat_tall
parent = sig17_03

[Object]
nickname = sig17_03_habitat08
pos = -55, 275, -25
rotate = 0, 0, 0
archetype = space_small_control_Block
parent = sig17_03

[Object]
nickname = sig17_03_habitat09
pos = -50, -102, -10
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig17_03

[Object]
nickname = sig17_03_habitat10
pos = -50, -60, -55
rotate = 0, -15, 0
archetype = space_habitat_tall
parent = sig17_03

[Object]
nickname = sig17_03_habitat11
pos = -50, -230, -55
rotate = 180, 0, 0
archetype = space_small_control_block
parent = sig17_03

[Object]
nickname = sig17_03_habitat12
pos = 5, 122, 5
rotate = 0, 45, 0
archetype = space_habitat_tallb
parent = sig17_03

[Object]
nickname = sig17_03_control_tower01
pos = -50, 80, -130
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = sig17_03

[Object]
nickname = sig17_03_control_tower02
pos = -50, -52, -130
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = sig17_03

[Object]
nickname = sig17_03_control_tower03
pos = -50, 155, -100
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = sig17_03

[Object]
nickname = sig17_03_control_tower04
pos = -50, 15, -130
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = sig17_03

[Object]
nickname = sig17_03_control_tower05
pos = -50, -105, -55
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = sig17_03

[Object]
nickname = sig17_03_control_tower06
pos = -55, 245, -25
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = sig17_03

[Object]
nickname = sig17_03_control_tower07
pos = -50, -180, -55
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = sig17_03

[Object]
nickname = sig17_03_ind01
pos = -55, 185, -25
rotate = 90, 0, 0
archetype = space_industrial01b
parent = sig17_03

[Object]
nickname = sig17_03_ind02
pos = -50, -50, -10
rotate = 90, 0, 0
archetype = space_industrial01b
parent = sig17_03

[Object]
nickname = sig17_03_ind03
pos = 5, 20, 5
rotate = 90, 45, 0
archetype = space_industrial01b
parent = sig17_03

[Object]
nickname = sig17_03_ind04
pos = 5, -20, 5
rotate = 90, 45, 0
archetype = space_industrial01b
parent = sig17_03

[Object]
nickname = sig17_03_tanks01
pos = -120, 0, 15
rotate = -90, 0, 0
archetype = space_tanks4
parent = sig17_03

[Object]
nickname = sig17_03_tanks02
pos = -160, 0, 10
rotate = -90, -15, 0
archetype = space_tanks4
parent = sig17_03

[Object]
nickname = sig17_03_tanks03
pos = -200, 0, -5
rotate = -90, -30, 0
archetype = space_tanks4
parent = sig17_03

[Object]
nickname = sig17_03_girder01
pos = -50, 205, -115
rotate = -40, 0, 0
archetype = space_girderb
parent = sig17_03

[Object]
nickname = sig17_03_girder02
pos = -70, 205, -100
rotate = -45, 30, 0
archetype = space_girderb
parent = sig17_03

[Object]
nickname = sig17_03_girder03
pos = -22, 205, -95
rotate = -45, -30, 0
archetype = space_girderb
parent = sig17_03

[Object]
nickname = sig17_03_girder04
pos = 0, 140, -120
rotate = -45, 0, 0
archetype = space_girderb
parent = sig17_03

[Object]
nickname = sig17_03_girder05
pos = -50, 100, -180
rotate = -70, 0, 0
archetype = space_girderb
parent = sig17_03

[Object]
nickname = sig17_03_girder06
pos = -95, 90, -145
rotate = -80, 0, 0
archetype = space_girderb
parent = sig17_03

[Object]
nickname = sig17_03_girder07
pos = -95, 90, -145
rotate = -80, 0, 0
archetype = space_girderb
parent = sig17_03

[Object]
nickname = sig17_03_girder06
pos = -95, 90, -145
rotate = -80, 0, 0
archetype = space_girderb
parent = sig17_03

[Object]
nickname = sig17_03_girder07
pos = -50, -95, -145
rotate = 45, 0, 0
archetype = space_girderb
parent = sig17_03

[Object]
nickname = sig17_03_girder08
pos = 0, -85, -110
rotate = 30, 10, 0
archetype = space_girderb
parent = sig17_03

[Object]
nickname = sig17_03_girder09
pos = -90, -85, -120
rotate = 25, -10, 0
archetype = space_girderb
parent = sig17_03

[Object]
nickname = sig17_03_girder10
pos = -55, 122, -30
rotate = 0, 60, 0
archetype = space_girderb
parent = sig17_03
'''


class MunchenAsteroidBase(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_mnh_03'
    TEMPLATE = '''[Object]
nickname = rh_mnh_03
pos = 0, 0, 0
rotate = 0, 40, 0
archetype = miningbase_badlands
{dock_props}

[Object]
nickname = rh_mnh_03_ind01
pos = 0, 134, -130
rotate = 90, 30, 90
archetype = space_industrial01b_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_ind02
pos = 0, 134, 130
rotate = 90, -30, 90
archetype = space_industrial01b_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_ind03
pos = 130, 134, 0
rotate = 0, 0, -30
archetype = space_industrial01b_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_ind04
pos = -130, 134, 0
rotate = 0, 0, 30
archetype = space_industrial01b_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_ind05
pos = 0, -10, -99
rotate = 0, 0, 0
archetype = space_industrial01c_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_ind06
pos = 0, -10, 100
rotate = 0, 180, 0
archetype = space_industrial01c_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_ind07
pos = -18, -10, -75
rotate = 0, 90, 0
archetype = space_industrial02b_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_girder01
pos = 50, 180, 0
rotate = 30, 90, 0
archetype = space_girderb_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_girder02
pos = -50, 180, 0
rotate = -30, 90, 0
archetype = space_girderb_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_girder03
pos = 0, 180, 50
rotate = 30, 0, 0
archetype = space_girderb_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_girder04
pos = 0, 180, -50
rotate = -30, 0, 0
archetype = space_girderb_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_girder05
pos = 90, 134, -90
rotate = 0, 45, 0
archetype = space_girderb_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_girder06
pos = -90, 134, -90
rotate = 0, -45, 0
archetype = space_girderb_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_girder07
pos = 90, 134, 90
rotate = 0, -45, 0
archetype = space_girderb_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_girder08
pos = -90, 134, 90
rotate = 0, 45, 0
archetype = space_girderb_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_girder09
pos = 0, 56, -134
rotate = 75, 0, 0
archetype = space_girderb_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_girder10
pos = 0, 56, 134
rotate = -75, 0, 0
archetype = space_girderb_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_girder11
pos = 1, 160, -75
rotate = 60, 0, 0
archetype = space_girderb_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_girder12
pos = -20, 160, -55
rotate = 60, 25, 0
archetype = space_girderb_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_girder13
pos = 30, 160, -65
rotate = 60, -20, 0
archetype = space_girderb_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_girder14
pos = 30, 20, 65
rotate = -75, 45, 0
archetype = space_girderb_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_girder14
pos = 65, 20, 20
rotate = -75, 75, 0
archetype = space_girderb_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_ctrl_twr01
pos = 20, 80, 20
rotate = 0, -30, 0
archetype = space_small_control_tower_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_ctrl_twr02
pos = 10, 220, -50
rotate = 0, -30, 0
archetype = space_small_control_tower_badland
parent = rh_mnh_03

[Object]
nickname = rh_mnh_03_ctrl_block01
pos = 10, 220, -50
rotate = 0, 0, 0
archetype = space_small_control_block_badland
parent = rh_mnh_03
'''


class BizmarkAsteroidBase(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_biz_07'
    TEMPLATE = '''[Object]
nickname = rh_biz_07
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = miningbase_mineableB
{dock_props}

[Object]
nickname = rh_biz_07_ctrl_twr01
pos = 0, 0, -100
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = rh_biz_07

[Object]
nickname = rh_biz_07_girder01
pos = 0, 0, -164
rotate = 0, 0, 0
archetype = space_girderc
parent = rh_biz_07

[Object]
nickname = rh_biz_07_shipyard01
pos = 0, -50, -250
rotate = 0, 90, 0
archetype = shipyard_small
parent = rh_biz_07

[Object]
nickname = rh_biz_07_ctrl_block01
pos = 0, 50, -250
rotate = 0, 0, 0
archetype = space_small_control_block
parent = rh_biz_07

[Object]
nickname = rh_biz_07_tank01
pos = 0, -60, -110
rotate = 0, 90, 0
archetype = space_tanks2
parent = rh_biz_07

[Object]
nickname = rh_biz_07_tank02
pos = 0, -60, -150
rotate = 0, 90, 0
archetype = space_tanks2
parent = rh_biz_07
'''


class BerlinAsteroidBase(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_ber_05'
    TEMPLATE = '''[Object]
nickname = rh_ber_05
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_police01_front_dock
{dock_props}

[Object]
nickname = rh_ber_05_asteroid01
pos = 0, 190, -50
rotate = 0, 0, 0
archetype = miningbase_mineableA_sattelite
parent = rh_ber_05

[Object]
nickname = rh_ber_05_asteroid02
pos = 0, 0, -57
rotate = 0, 0, 180
archetype = miningbase_mineableB_sattelite
parent = rh_ber_05

[Object]
nickname = rh_ber_05_ind01
pos = 10, 100, -70
rotate = 90, 70, 0
archetype = space_industrial02d
parent = rh_ber_05

[Object]
nickname = rh_ber_05_ind02
pos = -70, 10, -44
rotate = 60, 95, 0
archetype = space_industrial01b_lod
parent = rh_ber_05

[Object]
nickname = rh_ber_05_ind03
pos = -40, 166, -44
rotate = -30, 90, 0
archetype = space_industrial01b_lod
parent = rh_ber_05

[Object]
nickname = rh_ber_05_ind04
pos = 60, 180, -44
rotate = 35, 90, 0
archetype = space_industrial01b_lod
parent = rh_ber_05

[Object]
nickname = rh_ber_05_ind05
pos = 70, 20, -44
rotate = -60, 90, 0
archetype = space_industrial01b_lod
parent = rh_ber_05

[Object]
nickname = rh_ber_05_ind06
pos = 0, 70, -150
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = rh_ber_05

[Object]
nickname = rh_ber_05_girder01
pos = -90, 81, -43
rotate = 98, 90, 0
archetype = space_girderb
parent = rh_ber_05

[Object]
nickname = rh_ber_05_girder02
pos = 20, 30, 20
rotate = -60, 20, 0
archetype = space_girderb
parent = rh_ber_05

[Object]
nickname = rh_ber_05_girder03
pos = -20, 30, 20
rotate = -60, -5, 0
archetype = space_girderb
parent = rh_ber_05

[Object]
nickname = rh_ber_05_habitat01
pos = 90, 195, -44
rotate = 0, 0, 0
archetype = space_habitat_Tall
parent = rh_ber_05

[Object]
nickname = rh_ber_05_habitat02
pos = -50, 100, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_ber_05

[Object]
nickname = rh_ber_05_habitat03
pos = 50, 170, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_ber_05

[Object]
nickname = rh_ber_05_habitat04
pos = 10, 170, 45
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_ber_05

[Object]
nickname = rh_ber_05_ctrl_twr01
pos = 0, 100, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = rh_ber_05

[Object]
nickname = rh_ber_05_ctrl_twr02
pos = 0, -50, -110
rotate = 0, 90, 0
archetype = space_medium_control_tower
parent = rh_ber_05

[Object]
nickname = rh_ber_05_ctrl_twr03
pos = 0, 210, -150
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = rh_ber_05
'''


class ManhattanAsteroidBase(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_mnh_09'
    TEMPLATE = '''[Object]
nickname = li_mnh_09
pos = 0, 0, 0
rotate = 0, -60, 0
archetype = space_port_dmg_front_dock
{dock_props}

[Object]
nickname = li_mnh_09_ast01
pos = 180, 400, -100
rotate = 180, 0, 0
archetype = miningbase_badlands_satellite
parent = li_mnh_09

[Object]
nickname = li_mnh_09_ast02
pos = 180, 0, -150
rotate = 0, 20, 0
archetype = miningbase_badlands_satellite
parent = li_mnh_09

[Object]
nickname = li_mnh_09_ast03
pos = 130, -50, -70
rotate = 0, 80, 0
archetype = miningbase_badlands_satellite
parent = li_mnh_09

[Object]
nickname = li_mnh_09_ast04
pos = 230, 180, -100
rotate = 180, 150, 0
archetype = miningbase_badlands_satellite
parent = li_mnh_09

[Object]
nickname = li_mnh_09_ast05
pos = 180, -120, -100
rotate = 180, 60, 0
archetype = miningbase_badlands_satellite
parent = li_mnh_09

[Object]
nickname = li_mnh_09_ctrl_block02
pos = 270, 490, -110
rotate = 0, 0, 0
archetype = space_small_control_block
parent = li_mnh_09

[Object]
nickname = li_mnh_09_ind02
pos = 270, 220, -80
rotate = 0, 65, 0
archetype = space_industrial01d
parent = li_mnh_09

[Object]
nickname = li_mnh_09_ind03
pos = 230, -15, -150
rotate = 0, 135, 0
archetype = space_industrial01d
parent = li_mnh_09

[Object]
nickname = li_mnh_09_ind04
pos = 125, -90, 10
rotate = -10, 170, 0
archetype = space_industrial01c
parent = li_mnh_09

[Object]
nickname = li_mnh_09_ind05
pos = 210, -85, -170
rotate = 90, 0, 0
archetype = space_industrial01c
parent = li_mnh_09

[Object]
nickname = li_mnh_09_ind06
pos = 265, 435, -110
rotate = 90, 0, -35
archetype = space_industrial01c
parent = li_mnh_09

[Object]
nickname = li_mnh_09_ind07
pos = 100, 435, -107
rotate = 90, 0, 90
archetype = space_industrial01c
parent = li_mnh_09

[Object]
nickname = li_mnh_09_tanks01
pos = 260, -80, -180
rotate = 0, 40, 0
archetype = space_tanks4
parent = li_mnh_09

[Object]
nickname = li_mnh_09_tanks02
pos = 290, -60, -210
rotate = 0, 40, 0
archetype = space_tanks4
parent = li_mnh_09
'''


class CaliforniaAsteroidBase(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_cal_09'
    TEMPLATE = '''[Object]
nickname = li_cal_09
pos = 0, 0, 0
rotate = 0, -90, 0
archetype = miningbase_FragA
{dock_props}

[Object]
nickname = li_cal_09_hand01
pos = 70, 45, -40
rotate = 0, 10, 60
archetype = space_hand
parent = li_cal_09

[Object]
nickname = li_cal_09_hand02
pos = 70, 45, 0
rotate = 0, 10, 60
archetype = space_hand
parent = li_cal_09

[Object]
nickname = li_cal_09_transport01
pos = 140, 0, -25
rotate = 0, 0, -30
archetype = suprise_transport
parent = li_cal_09

[Object]
nickname = li_cal_09_ctrl_twr01
pos = 100, 50, -20
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = li_cal_09

[Object]
nickname = li_cal_09_pad01
pos = 118, -45, 0
rotate = 0, 0, 0
archetype = space_small_pad
parent = li_cal_09

[Object]
nickname = li_cal_09_pad02
pos = 118, -45, -40
rotate = 0, 0, 0
archetype = space_small_pad
parent = li_cal_09

[Object]
nickname = li_cal_09_hangar01
pos = 75, -45, 0
rotate = 0, 90, 0
archetype = space_hangar
parent = li_cal_09

[Object]
nickname = li_cal_09_hangar02
pos = 75, -45, -40
rotate = 0, 90, 0
archetype = space_hangar
parent = li_cal_09
'''
