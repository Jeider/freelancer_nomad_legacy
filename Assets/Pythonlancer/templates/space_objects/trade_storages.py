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


class TekagiStorage(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_hkd_05'
    TEMPLATE = '''[Object]
nickname = ku_tgk_02
ids_name = 203773
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_police01
ids_info = 065686
visit = 16
base = ku_tgk_02_base
dock_with = ku_tgk_02_base
reputation = ku_grp
behavior = NOTHING
voice = atc_leg_f01
space_costume = ku_newscaster_head_gen, pl_female1_peasant_body, prop_hat_female_miner_visor

[Object]
nickname = ku_tgk_02_ind01
pos = 0, -160, 0
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_ind02
pos = 0, -310, 0
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_shipyard01
pos = 190, -250, 0
rotate = 0, 90, 0
archetype = shipyard_medium
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_shipyard02
pos = -190, -250, 0
rotate = 0, -90, 0
archetype = shipyard_medium
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_girder01
pos = 25, -160, 0
rotate = 0, 90, 0
archetype = space_girdera
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_girder02
pos = -25, -160, 0
rotate = 0, -90, 0
archetype = space_girdera
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_girder03
pos = 25, -310, 0
rotate = 0, 90, 0
archetype = space_girdera
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_girder04
pos = -25, -310, 0
rotate = 0, -90, 0
archetype = space_girdera
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_panel01
pos = -160, -100, 0
rotate = 0, 90, 0
archetype = space_panelc
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_panel02
pos = -320, -100, 0
rotate = 0, 90, 0
archetype = space_panelc
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_panel03
pos = 160, -100, 0
rotate = 0, 90, 0
archetype = space_panelc
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_panel04
pos = 320, -100, 0
rotate = 0, 90, 0
archetype = space_panelc
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_panel05
pos = -160, -370, 0
rotate = 0, 90, 0
archetype = space_panelc
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_panel06
pos = -320, -370, 0
rotate = 0, 90, 0
archetype = space_panelc
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_panel07
pos = 160, -370, 0
rotate = 0, 90, 0
archetype = space_panelc
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_panel08
pos = 320, -370, 0
rotate = 0, 90, 0
archetype = space_panelc
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_ctrl_twr01
pos = 0, -165, -40
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_ctrl_twr02
pos = 0, -305, -40
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_ctrl_twr03
pos = 0, -165, 40
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_ctrl_twr04
pos = 0, -305, 40
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_ctrl_twr05
pos = 0, -450, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_ctrl_block01
pos = 0, -80, 0
rotate = 0, 90, 0
archetype = space_small_control_block
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_ctrl_block02
pos = 0, -390, 0
rotate = 0, 90, 0
archetype = space_small_control_block
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_ctrl_block02
pos = 0, -510, 0
rotate = 180, 90, 0
archetype = space_small_control_block
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_habitat01
pos = 0, -235, -85
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_tgk_02

[Object]
nickname = ku_tgk_02_habitat02
pos = 0, -235, 85
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_tgk_02
'''


class LibertyLongStorage(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'tau31_03'
    TEMPLATE = '''[Object]
nickname = tau31_03
ids_name = 203685
pos = 0, 0, 0
rotate = 0, -90, 0
archetype = space_police01_front_dock
ids_info = 065602
base = tau31_03_base
dock_with = tau31_03_base
reputation = li_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = pl_male6_head, li_commtrader_body, prop_neuralnet_a

[Object]
nickname = tau31_03_station_root
pos = 1550, 105, 0
rotate = 0, 90, 0
archetype = space_station_root
parent = tau31_03

[Object]
nickname = tau31_03_industrial_A01
pos = 1150, 0, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = tau31_03

[Object]
nickname = tau31_03_industrial_A02
pos = 850, 0, 0
rotate = 0, 90, 0
archetype = space_industrial_dmg
parent = tau31_03

[Object]
nickname = tau31_03_industrial_A03
pos = 550, 0, 0
rotate = 0, -90, 0
archetype = space_industrial_dmg
parent = tau31_03

[Object]
nickname = tau31_03_industrial_A04
pos = 250, 0, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = tau31_03

[Object]
nickname = tau31_03_industrial_A05
pos = 50, 0, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = tau31_03

[Object]
nickname = tau31_03_tanks_A01
pos = 1150, 0, -190
rotate = 90, -150, 90
archetype = space_tankl4
parent = tau31_03

[Object]
nickname = tau31_03_tanks_A02
pos = 1150, 0, -190
rotate = 90, 150, 90
archetype = space_tankl4
parent = tau31_03

[Object]
nickname = tau31_03_tanks_A03
pos = 1150, 0, 190
rotate = 90, 30, 90
archetype = space_tankl4
parent = tau31_03

[Object]
nickname = tau31_03_tanks_A04
pos = 1150, 0, 190
rotate = 90, -30, 90
archetype = space_tankl4
parent = tau31_03

[Object]
nickname = tau31_03_tanks_B01
pos = 850, 0, -190
rotate = 90, -150, 90
archetype = space_tankl4_dmg
parent = tau31_03

[Object]
nickname = tau31_03_tanks_B02
pos = 850, 0, -190
rotate = 90, 150, 90
archetype = space_tankl4_dmg
parent = tau31_03

[Object]
nickname = tau31_03_tanks_B04
pos = 850, 0, 190
rotate = 90, -30, 90
archetype = space_tankl4x4_dmg
parent = tau31_03

[Object]
nickname = tau31_03_tanks_C01
pos = 550, 0, -190
rotate = 90, -150, 90
archetype = space_tankl4
parent = tau31_03

[Object]
nickname = tau31_03_tanks_C02
pos = 550, 0, -190
rotate = -90, -30, 90
archetype = space_tankl4_dmg
parent = tau31_03

[Object]
nickname = tau31_03_tanks_C03
pos = 550, 0, 190
rotate = 90, 30, 90
archetype = space_tankl4
parent = tau31_03

[Object]
nickname = tau31_03_tanks_C04
pos = 550, 0, 190
rotate = 90, -30, 90
archetype = space_tankl4
parent = tau31_03

[Object]
nickname = tau31_03_tanks_D01
pos = 250, 0, -190
rotate = 90, -150, 90
archetype = space_tankl4
parent = tau31_03

[Object]
nickname = tau31_03_tanks_D02
pos = 250, 0, -190
rotate = 90, 150, 90
archetype = space_tankl4
parent = tau31_03

[Object]
nickname = tau31_03_tanks_D03
pos = 250, 0, 190
rotate = 90, 30, 90
archetype = space_tankl4
parent = tau31_03

[Object]
nickname = tau31_03_tanks_D04
pos = 250, 0, 190
rotate = 90, -30, 90
archetype = space_tankl4
parent = tau31_03

[Object]
nickname = tau31_03_girder_A01
pos = 1150, 0, 0
rotate = 0, 90, 0
archetype = space_girder
parent = tau31_03

[Object]
nickname = tau31_03_girder_A02
pos = 1150, 0, 0
rotate = 0, 0, 0
archetype = space_girder
parent = tau31_03

[Object]
nickname = tau31_03_girder_A03
pos = 850, 0, 0
rotate = 0, 0, 0
archetype = space_girder
parent = tau31_03

[Object]
nickname = tau31_03_girder_A04
pos = 550, 0, 0
rotate = 0, 0, 0
archetype = space_girder
parent = tau31_03

[Object]
nickname = tau31_03_girder_A05
pos = 250, 0, 0
rotate = 0, 0, 0
archetype = space_girder
parent = tau31_03

[Object]
nickname = tau31_03_girder_A06
pos = 550, 0, 0
rotate = 0, 90, 0
archetype = space_girder
parent = tau31_03

[Object]
nickname = tau31_03_shipyard01
pos = 1450, 164, -100
rotate = 180, 285, 0
archetype = shipyard_small
parent = tau31_03

[Object]
nickname = tau31_03_shipyard02
pos = 1450, 164, 100
rotate = 180, -285, 0
archetype = shipyard_small
parent = tau31_03
'''


class RheinlandOmegaStorage(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'om15_04'
    TEMPLATE = '''[Object]
nickname = om15_04
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_police01
reputation = rh_grp
behavior = NOTHING
voice = atc_leg_f01
space_costume = rh_newscaster_head_gen, pl_female1_peasant_body, prop_hat_female_miner
ids_name = 203648
ids_info = 067023
base = om15_04_base
dock_with = om15_04_base

[Object]
nickname = om15_04_industrial01
pos = 0, -200, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = om15_04

[Object]
nickname = om15_04_girder01
pos = 0, -100, 0
rotate = 90, 0, 0
archetype = space_girderc
parent = om15_04

[Object]
nickname = om15_04_shipyard01
pos = 0, -200, 95
rotate = 90, 0, 90
archetype = shipyard_medium
parent = om15_04

[Object]
nickname = om15_04_shipyard02
pos = 0, -200, -95
rotate = -90, 0, 90
archetype = shipyard_medium
parent = om15_04

[Object]
nickname = om15_04_tank01
pos = 0, -350, 0
rotate = 0, 0, 0
archetype = space_tanklx4
parent = om15_04

[Object]
nickname = om15_04_control_tower01
pos = 0, -75, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = om15_04
'''


class ManhattanStorage(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_mnh_07'
    TEMPLATE = '''[Object]
nickname = li_mnh_07
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_police01
base = li_mnh_07_base
dock_with = li_mnh_07_base
reputation = li_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = rh_alaric_head_hat, li_male_elite_body, prop_hat_male_li_elite_visor
difficulty_level = 10
pilot = pilot_solar_hardest
ids_name = 203897
ids_info = 1

[Object]
nickname = li_mnh_07_shipyard01
pos = 0, -500, 0
rotate = 0, 0, 0
archetype = shipyard
parent = li_mnh_07

[Object]
nickname = li_mnh_07_industial01
pos = 0, -350, 0
rotate = 0, 0, 0
archetype = space_industrial02d
parent = li_mnh_07

[Object]
nickname = li_mnh_07_industial02
pos = -100, -380, 1
rotate = 0, 0, 35
archetype = space_industrial02d
parent = li_mnh_07

[Object]
nickname = li_mnh_07_industial03
pos = 100, -380, 1
rotate = 0, 0, -35
archetype = space_industrial02d
parent = li_mnh_07

[Object]
nickname = li_mnh_07_industial04
pos = -150, -465, 0
rotate = 0, 0, 90
archetype = space_industrial02d
parent = li_mnh_07

[Object]
nickname = li_mnh_07_industial05
pos = 150, -465, 0
rotate = 0, 0, 90
archetype = space_industrial02d
parent = li_mnh_07

[Object]
nickname = li_mnh_07_tanks01
pos = -150, -525, 0
rotate = 0, 0, 0
archetype = space_tankl4
parent = li_mnh_07

[Object]
nickname = li_mnh_07_tanks02
pos = 150, -525, 0
rotate = 0, 0, 0
archetype = space_tankl4
parent = li_mnh_07

[Object]
nickname = li_mnh_07_control_tower01
pos = 0, -175, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = li_mnh_07

[Object]
nickname = li_mnh_07_girder01
pos = 0, -30, 0
rotate = 90, 0, 0
archetype = space_girdera
parent = li_mnh_07
'''
