from templates.space_object_template import SpaceObjectTemplate


class HokkaidoStorage(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_hkd_05'
    TEMPLATE = '''[Object]
nickname = ku_hkd_05
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_police01
ids_name = 203760
ids_info = 067023
reputation = ku_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = pl_male8_head, ku_commtrader_body, prop_neuralnet_e_right
difficulty_level = 11
pilot = pilot_solar_hard

[Object]
nickname = ku_hkd_05_xpanel01
pos = -18, -420, 0
rotate = -90, 90, 0
archetype = space_station_panela
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_cntrl_twr01
pos = -290, -700, 0
rotate = 90, 90, 0
archetype = space_control_tower
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_cntrl_twr02
pos = 0, -700, 0
rotate = 90, 90, 0
archetype = space_control_tower

[Object]
nickname = ku_hkd_05_cntrl_twr03
pos = 295, -700, 0
rotate = 90, -90, 0
archetype = space_control_tower
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_tanks01
pos = -145, -530, 0
rotate = 90, 0, 90
archetype = space_tankl4x4
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_tanks02
pos = -145, -870, 0
rotate = 90, 0, 90
archetype = space_tankl4x4
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_tanks03
pos = -145, -700, 170
rotate = 90, 0, 90
archetype = space_tankl4x4
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_tanks04
pos = -145, -700, -170
rotate = 90, 0, 90
archetype = space_tankl4x4
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_tanks05
pos = -145, -530, 0
rotate = 90, 90, 90
archetype = space_tankl4
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_tanks06
pos = -145, -870, 0
rotate = 90, -90, 90
archetype = space_tankl4
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_tanks07
pos = -145, -700, 170
rotate = 90, 90, 90
archetype = space_tankl4x4
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_tanks08
pos = -145, -700, -170
rotate = 90, 90, 90
archetype = space_tankl4x4
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_tanks09
pos = 147, -530, 0
rotate = 90, 0, 90
archetype = space_tankl4x4
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_tanks10
pos = 147, -870, 0
rotate = 90, 0, 90
archetype = space_tankl4x4
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_tanks11
pos = 147, -700, 170
rotate = 90, 0, 90
archetype = space_tankl4x4
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_tanks12
pos = 147, -700, -170
rotate = 90, 0, 90
archetype = space_tankl4x4
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_tanks13
pos = 147, -530, 0
rotate = 90, 90, 90
archetype = space_tankl4
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_tanks14
pos = 147, -870, 0
rotate = 90, -90, 90
archetype = space_tankl4
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_tanks15
pos = 147, -700, 170
rotate = 90, 90, 90
archetype = space_tankl4x4
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_tanks16
pos = 147, -700, -170
rotate = 90, 90, 90
archetype = space_tankl4x4
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_girder01
pos = 0, -800, -100
rotate = 0, 45, 90
archetype = space_girder
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_girder02
pos = 0, -800, 100
rotate = 0, 45, -90
archetype = space_girder
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_girder03
pos = 0, -200, 0
rotate = -90, 0, 0
archetype = space_girder
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_industrial01
pos = 0, -1000, -230
rotate = 0, 90, 0
archetype = space_industrial02a
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_industrial02
pos = 0, -1000, 230
rotate = 0, 90, 0
archetype = space_industrial02a
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_shipyard01
pos = 0, -1140, -230
rotate = 180, -90, 0
archetype = shipyard
parent = ku_hkd_05

[Object]
nickname = ku_hkd_05_shipyard02
pos = 0, -1140, 230
rotate = 180, -90, 0
archetype = shipyard
parent = ku_hkd_05
'''


class HonshuStorage(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_hns_05'
    TEMPLATE = '''[Object]
nickname = ku_hns_05
ids_name = 203783
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_police01
ids_info = 067023
reputation = kc_grp
behavior = NOTHING

[Object]
nickname = ku_hns_05_shipyard
pos = 0, -350, -250
rotate = 0, 0, 0
archetype = shipyard
parent = ku_hns_05

[Object]
nickname = ku_hns_05_ind01
pos = 0, -200, -250
rotate = 0, 0, 0
archetype = space_industrial02d
parent = ku_hns_05

[Object]
nickname = ku_hns_05_ind02
pos = 0, -200, -500
rotate = 0, 0, 0
archetype = space_industrial02d
parent = ku_hns_05

[Object]
nickname = ku_hns_05_ind03
pos = 0, -450, -250
rotate = 0, 0, 0
archetype = space_industrial02d
parent = ku_hns_05

[Object]
nickname = ku_hns_05_ind04
pos = 0, -450, 0
rotate = 0, 0, 0
archetype = space_industrial02d
parent = ku_hns_05

[Object]
nickname = ku_hns_05_ind05
pos = 0, -450, -500
rotate = 0, 0, 0
archetype = space_industrial02d
parent = ku_hns_05

[Object]
nickname = ku_hns_05_twr01
pos = 0, -200, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = ku_hns_05

[Object]
nickname = ku_hns_05_girder01
pos = 0, -200, -80
rotate = 0, 0, 0
archetype = space_girderc
parent = ku_hns_05

[Object]
nickname = ku_hns_05_girder02
pos = 0, -120, 0
rotate = 90, 0, 0
archetype = space_girderc
parent = ku_hns_05

[Object]
nickname = ku_hns_05_tank01
pos = -50, -450, -250
rotate = 0, 0, -45
archetype = space_tankl4
parent = ku_hns_05

[Object]
nickname = ku_hns_05_tank02
pos = 50, -450, -250
rotate = 0, 0, 45
archetype = space_tankl4
parent = ku_hns_05

[Object]
nickname = ku_hns_05_tank03
pos = -50, -451, 15
rotate = 0, 0, -45
archetype = space_tankl4
parent = ku_hns_05

[Object]
nickname = ku_hns_05_tank04
pos = 50, -451, 15
rotate = 0, 0, 45
archetype = space_tankl4
parent = ku_hns_05

[Object]
nickname = ku_hns_05_tank05
pos = -50, -451, -515
rotate = 0, 0, -45
archetype = space_tankl4
parent = ku_hns_05

[Object]
nickname = ku_hns_05_tank06
pos = 50, -451, -515
rotate = 0, 0, 45
archetype = space_tankl4
parent = ku_hns_05
'''
