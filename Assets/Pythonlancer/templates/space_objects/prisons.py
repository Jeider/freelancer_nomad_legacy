from templates.space_object_template import SpaceObjectTemplate


class AvalonPrison(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'br_avl_03'
    TEMPLATE = '''[Object]
nickname = br_avl_03
ids_name = 203733
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = prison
ids_info = 065648
dock_with = br_avl_03_Base
base = br_avl_03_Base
reputation = br_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = br_sales_head_hat, br_male_guard_body, prop_hat_male_br_elite
difficulty_level = 5 ;12
loadout = prison_br
pilot = pilot_solar_hardest
visit = 16

[Object]
nickname = br_avl_03_girder01
pos = -201, 0, 0
rotate = 0, 90, 0
archetype = space_girder
parent = br_avl_03

[Object]
nickname = br_avl_03_girder02
pos = -400, 0, -210
rotate = 0, 0, 0
archetype = space_girder
parent = br_avl_03

[Object]
nickname = br_avl_03_girder03
pos = -400, 0, 210
rotate = 0, 0, 0
archetype = space_girder
parent = br_avl_03

[Object]
nickname = br_avl_03_girder04
pos = -640, 0, 210
rotate = 0, 0, 0
archetype = space_girder
parent = br_avl_03

[Object]
nickname = br_avl_03_girder05
pos = -640, 0, -190
rotate = 0, 0, 0
archetype = space_girder
parent = br_avl_03

[Object]
nickname = br_avl_03_prison01
pos = -640, 0, 0
rotate = 0, 180, 0
archetype = space_prison
parent = br_avl_03

[Object]
nickname = br_avl_03_prison02
pos = -640, 0, -400
rotate = 0, 180, 0
archetype = space_prison
parent = br_avl_03

[Object]
nickname = br_avl_03_prison03
pos = -640, 0, 400
rotate = 0, 180, 0
archetype = space_prison
parent = br_avl_03

[Object]
nickname = br_avl_03_industrial01
pos = -400, 0, 0
rotate = 0, 90, 0
archetype = space_industrial01b
parent = br_avl_03

[Object]
nickname = br_avl_03_industrial02
pos = -400, 0, -400
rotate = 0, 90, 0
archetype = space_industrial01b
parent = br_avl_03

[Object]
nickname = br_avl_03_industrial03
pos = -400, 0, 400
rotate = 0, 90, 0
archetype = space_industrial01b
parent = br_avl_03

[Object]
nickname = br_avl_03_girder06
pos = -640, 100, 0
rotate = 90, 0, 0
archetype = space_girder
parent = br_avl_03

[Object]
nickname = br_avl_03_girder07
pos = -640, -100, 0
rotate = 90, 0, 0
archetype = space_girder
parent = br_avl_03

[Object]
nickname = br_avl_03_industrial04
pos = -640, 260, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = br_avl_03

[Object]
nickname = br_avl_03_industrial05
pos = -640, -260, 0
rotate = 0, 90, 0
archetype = space_industrial02a
parent = br_avl_03

[Object]
nickname = br_avl_03_industrial06
pos = -785, 260, 0
rotate = 180, 0, 90
archetype = space_industrial02a
loadout = space_ind01_reactor
parent = br_avl_03

[Object]
nickname = br_avl_03_shipyard
pos = -925, 260, 0
rotate = 0, 0, 90
archetype = shipyard
parent = br_avl_03

[Object]
nickname = br_avl_03_dome01
pos = -640, 290, -400
rotate = 0, 0, 0
archetype = space_dome
parent = br_avl_03

[Object]
nickname = br_avl_03_dome02
pos = -640, 290, 400
rotate = 0, 180, 0
archetype = space_dome
parent = br_avl_03

[Object]
nickname = br_avl_03_tanks01
pos = -640, -260, -190
rotate = 0, 0, 0
archetype = space_tankl4
parent = br_avl_03

[Object]
nickname = br_avl_03_tanks02
pos = -640, -260, -455
rotate = 0, 0, 0
archetype = space_tankl4
parent = br_avl_03

[Object]
nickname = br_avl_03_tanks03
pos = -640, -260, 190
rotate = 0, 0, 0
archetype = space_tankl4
parent = br_avl_03

[Object]
nickname = br_avl_03_tanks04
pos = -640, -260, 455
rotate = 0, 0, 0
archetype = space_tankl4
parent = br_avl_03

[Object]
nickname = br_avl_03_tanks05
pos = -640, -260, -190
rotate = 0, 0, 90
archetype = space_tankl4x4
parent = br_avl_03

[Object]
nickname = br_avl_03_tanks06
pos = -640, -260, -455
rotate = 0, 0, 90
archetype = space_tankl4x4
parent = br_avl_03

[Object]
nickname = br_avl_03_tanks07
pos = -640, -260, 190
rotate = 0, 0, 90
archetype = space_tankl4x4
parent = br_avl_03

[Object]
nickname = br_avl_03_tanks08
pos = -640, -260, 455
rotate = 0, 0, 90
archetype = space_tankl4x4
parent = br_avl_03
'''


class HonshuPrison(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_hns_03'
    TEMPLATE = '''[Object]
nickname = ku_hns_03
ids_name = 203767
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_police01_prison
ids_info = 065682
dock_with = ku_hns_03_base
base = ku_hns_03_base
reputation = ku_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = pl_male8_head_hat, ku_male_guard_body, prop_hat_male_ku_grd_visor
difficulty_level = 10
loadout = ku_space_police01
pilot = pilot_solar_hardest
visit = 16

[Object]
nickname = ku_hns_03_prison_root01
pos = -330, 0, 0
rotate = 0, 0, 0
archetype = space_industrial01b
parent = ku_hns_03

[Object]
nickname = ku_hns_03_prison01
pos = -330, 0, -255
rotate = 0, 90, 0
archetype = space_prison
parent = ku_hns_03

[Object]
nickname = ku_hns_03_prison02
pos = -330, 0, 255
rotate = 0, -90, 0
archetype = space_prison
parent = ku_hns_03

[Object]
nickname = ku_hns_03_industrial01
pos = -405, 0, 0
rotate = 0, 90, 0
archetype = space_industrial01b
parent = ku_hns_03

[Object]
nickname = ku_hns_03_industrial02
pos = -255, 0, 0
rotate = 0, 90, 0
archetype = space_industrial01b
parent = ku_hns_03

[Object]
nickname = ku_hns_03_girder01
pos = -410, 0, 0
rotate = 0, 90, 0
archetype = space_girder
parent = ku_hns_03

[Object]
nickname = ku_hns_03_girder02
pos = -250, 0, 0
rotate = 0, 90, 0
archetype = space_girder
parent = ku_hns_03

[Object]
nickname = ku_hns_03_tanks01
pos = -592, 0, -143
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = ku_hns_03

[Object]
nickname = ku_hns_03_tanks02
pos = -592, 0, 143
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = ku_hns_03

[Object]
nickname = ku_hns_03_dome01
pos = -300, -300, 0
rotate = 0, -90, -90
archetype = space_dome
parent = ku_hns_03

[Object]
nickname = ku_hns_03_dome02
pos = -300, 300, 0
rotate = 0, 90, -90
archetype = space_dome
parent = ku_hns_03

[Object]
nickname = ku_hns_03_radar01
pos = -330, 156, -254
rotate = 0, 90, 0
archetype = old_panel_x2
parent = ku_hns_03

[Object]
nickname = ku_hns_03_radar02
pos = -330, -154, -254
rotate = 0, -90, 180
archetype = old_panel_x2
parent = ku_hns_03

[Object]
nickname = ku_hns_03_radar03
pos = -330, -154, 254
rotate = 0, -90, 180
archetype = old_panel_x2
parent = ku_hns_03

[Object]
nickname = ku_hns_03_radar04
pos = -330, 156, 254
rotate = 0, 90, 0
archetype = old_panel_x2
parent = ku_hns_03
'''


class BerlinPrison(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_ber_02'
    TEMPLATE = '''[Object]
nickname = rh_ber_02
ids_name = 203630
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_police01_prison
ids_info = 066627
base = Rh_Ber_02_Base
dock_with = Rh_Ber_02_Base
visit = 16
reputation = rh_grp
behavior = NOTHING
voice = atc_leg_F01
space_costume = br_newscaster_head_gen_hat, rh_female_elite_body, prop_hat_female_rh_elite
difficulty_level = 12
pilot = pilot_solar_hardest

[Object]
nickname = rh_ber_02_prison
pos = -500, 0, 0
rotate = 0, 180, 0
archetype = space_prison
parent = rh_ber_02

[Object]
nickname = rh_ber_02_tankl01
pos = -500, -290, 0
rotate = 90, 0, 0
archetype = space_tankl4x4
parent = rh_ber_02

[Object]
nickname = rh_ber_02_tankl02
pos = -500, -290, 0
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = rh_ber_02

[Object]
nickname = rh_ber_02_tankl03
pos = -500, -460, 0
rotate = 0, 0, 0
archetype = space_tanklx4
parent = rh_ber_02

[Object]
nickname = rh_ber_02_industrial01
pos = -500, 0, 450
rotate = 0, 180, 0
archetype = space_industrial
parent = rh_ber_02

[Object]
nickname = rh_ber_02_industrial02
pos = -500, 0, -450
rotate = 0, 0, 0
archetype = space_industrial02
parent = rh_ber_02

[Object]
nickname = rh_ber_02_industrial03
pos = -300, 0, 0
rotate = 0, 90, 0
archetype = space_industrial01b_lod
parent = rh_ber_02

[Object]
nickname = rh_ber_02_girder01
pos = -265, 0, 0
rotate = 0, 90, 0
archetype = space_girder
parent = rh_ber_02

[Object]
nickname = rh_ber_02_dome01
pos = -840, 30, 450
rotate = 0, 90, 0
archetype = space_dome_lod
parent = rh_ber_02

[Object]
nickname = rh_ber_02_dome02
pos = -500, 30, 700
rotate = 0, 180, 0
archetype = space_dome_lod
parent = rh_ber_02

[Object]
nickname = rh_ber_02_shipyard01
pos = -680, -215, -450
rotate = 0, -90, 0
archetype = shipyard
parent = rh_ber_02

[Object]
nickname = rh_ber_02_habitat01
pos = -500, 180, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_ber_02

[Object]
nickname = rh_ber_02_habitat02
pos = -500, 270, 0
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = rh_ber_02
'''


class AlaskaPrison(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_mnh_05'
    TEMPLATE = '''[Object]
nickname = li_mnh_05
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = prison
loadout = prison_li
ids_name = 208615
ids_info = 067009
visit = 0
base = li_mnh_05_base
dock_with = li_mnh_05_base
reputation = li_grp
behavior = NOTHING
difficulty_level = 6
voice = atc_leg_m01
space_costume = ge_male7_head, li_tilton_body, prop_hat_male_li_grd, prop_neuralnet_d

[Object]
nickname = li_mnh_05_indA01
pos = 0, 0, -600
rotate = 90, 0, 0
archetype = space_industrial02a
parent = li_mnh_05

[Object]
nickname = li_mnh_05_indA02
pos = 190, 0, -600
rotate = 0, 90, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = li_mnh_05

[Object]
nickname = li_mnh_05_indA03
pos = -190, 0, -600
rotate = 0, -90, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = li_mnh_05

[Object]
nickname = li_mnh_05_indA04
pos = 0, 0, -405
rotate = 0, 0, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = li_mnh_05

[Object]
nickname = li_mnh_05_indA05
pos = 0, 0, -795
rotate = 0, 180, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = li_mnh_05

[Object]
nickname = li_mnh_05_indA06
pos = 0, 220, -600
rotate = 90, 0, 0
archetype = space_industriala
parent = li_mnh_05

[Object]
nickname = li_mnh_05_indA07
pos = 0, -110, -600
rotate = 90, 45, 0
archetype = space_industrialc
parent = li_mnh_05

[Object]
nickname = li_mnh_05_indA08
pos = 0, 0, -230
rotate = 0, 0, 0
archetype = space_industrial01c
parent = li_mnh_05

[Object]
nickname = li_mnh_05_domeA01
pos = 0, 25, -1200
rotate = 0, 90, 0
archetype = space_domea
parent = li_mnh_05

[Object]
nickname = li_mnh_05_domeA02
pos = 0, -25, -1200
rotate = 180, 90, 0
archetype = space_domea
parent = li_mnh_05

[Object]
nickname = li_mnh_05_domeA03
pos = 600, 25, -600
rotate = 0, 0, 0
archetype = space_domea
parent = li_mnh_05

[Object]
nickname = li_mnh_05_domeA04
pos = 600, -25, -600
rotate = 180, 0, 0
archetype = space_domea
parent = li_mnh_05

[Object]
nickname = li_mnh_05_domeA05
pos = -600, 25, -600
rotate = 0, 0, 0
archetype = space_domea
parent = li_mnh_05

[Object]
nickname = li_mnh_05_domeA06
pos = -600, -25, -600
rotate = 180, 0, 0
archetype = space_domea
parent = li_mnh_05

[Object]
nickname = li_mnh_05_cntrl_twrA01
pos = 0, 0, -1200
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = li_mnh_05

[Object]
nickname = li_mnh_05_cntrl_twrA02
pos = 600, 0, -600
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = li_mnh_05

[Object]
nickname = li_mnh_05_cntrl_twrA03
pos = -600, 0, -600
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = li_mnh_05

[Object]
nickname = li_mnh_05_cntrl_twrB01
pos = 0, 220, -600
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = li_mnh_05

[Object]
nickname = li_mnh_05_cntrl_twrB02
pos = 0, 400, -600
rotate = 180, 45, 0
archetype = space_medium_control_tower
parent = li_mnh_05

[Object]
nickname = li_mnh_05_cntrl_twrB03
pos = 0, 180, -600
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = li_mnh_05

[Object]
nickname = li_mnh_05_cntrl_twrB04
pos = 0, 430, -600
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = li_mnh_05

[Object]
nickname = li_mnh_05_habitat01
pos = 90, 310, -600
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_mnh_05

[Object]
nickname = li_mnh_05_habitat02
pos = -90, 310, -600
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_mnh_05

[Object]
nickname = li_mnh_05_habitat03
pos = 0, 310, -510
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_mnh_05

[Object]
nickname = li_mnh_05_habitat04
pos = 0, 310, -680
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_mnh_05

[Object]
nickname = li_mnh_05_habitat05
pos = 0, 310, -600
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_mnh_05

[Object]
nickname = li_mnh_05_habitat06
pos = 0, 455, -600
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_mnh_05

[Object]
nickname = li_mnh_05_habitat07
pos = 90, 535, -600
rotate = 0, -80, 0
archetype = space_habitat_tall
parent = li_mnh_05

[Object]
nickname = li_mnh_05_control_block01
pos = 0, 545, -600
rotate = 0, 0, 0
archetype = space_small_control_block
parent = li_mnh_05

[Object]
nickname = li_mnh_05_control_block02
pos = -90, 350, -600
rotate = 0, 135, 0
archetype = space_small_control_block
parent = li_mnh_05

[Object]
nickname = li_mnh_05_tanks01
pos = 0, -360, -600
rotate = 90, 0, 0
archetype = space_tankl4x4
parent = li_mnh_05

[Object]
nickname = li_mnh_05_tanks02
pos = 0, -360, -600
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = li_mnh_05

[Object]
nickname = li_mnh_05_tanks03
pos = 0, -360, -600
rotate = 90, 45, 0
archetype = space_tankl4x4
parent = li_mnh_05

[Object]
nickname = li_mnh_05_tanks04
pos = 0, -360, -600
rotate = 90, -45, 0
archetype = space_tankl4x4
parent = li_mnh_05

[Object]
nickname = li_mnh_05_tanks05
pos = 0, -500, -600
rotate = 0, 0, 0
archetype = space_tanklx4
parent = li_mnh_05
'''


class ColumbiaPrison(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_col_02'
    TEMPLATE = '''[Object]
nickname = li_col_02
ids_name = 203695
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_police01_prison
ids_info = 065608
dock_with = li_col_02_Base
base = li_col_02_Base
reputation = li_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = li_rockford_head, li_male_guard_body, prop_hat_male_li_elite_visor
difficulty_level = 12
loadout = li_space_police01
pilot = pilot_solar_hardest
visit = 16

[Object]
nickname = li_col_02_control_tower01
pos = 650, 0, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = li_col_02

[Object]
nickname = li_col_02_control_tower02
pos = 650, 82, 0
rotate = 0, 0, 180
archetype = space_control_tower
parent = li_col_02

[Object]
nickname = li_col_02_control_tower03
pos = 650, -82, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = li_col_02

[Object]
nickname = li_col_02_space_habitat_wide01
pos = 490, 0, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_col_02

[Object]
nickname = li_col_02_space_habitat_wide02
pos = 810, 0, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_col_02

[Object]
nickname = li_col_02_space_habitat_wide03
pos = 650, 0, 160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_col_02

[Object]
nickname = li_col_02_space_habitat_wide04
pos = 650, 0, -160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_col_02

[Object]
nickname = li_col_02_space_habitat_wide05
pos = 650, 0, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_col_02

[Object]
nickname = li_col_02_habitat_wide06
pos = 650, 158, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_col_02

[Object]
nickname = li_col_02_habitat_tall01
pos = 650, 250, 0
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = li_col_02

[Object]
nickname = li_col_02_industrial01
pos = 650, 0, 210
rotate = 0, 0, 0
archetype = space_industrial01b
parent = li_col_02

[Object]
nickname = li_col_02_industrial02
pos = 650, 0, -210
rotate = 0, 0, 0
archetype = space_industrial01b
parent = li_col_02

[Object]
nickname = li_col_02_industrial03
pos = 860, 0, 0
rotate = 0, 90, 0
archetype = space_industrial01b
parent = li_col_02

[Object]
nickname = li_col_02_industrial04
pos = 440, 0, 0
rotate = 0, 90, 0
archetype = space_industrial01b
parent = li_col_02

[Object]
nickname = li_col_02_industrial05
pos = 1280, 0, 0
rotate = 0, -90, 0
archetype = space_industrial02
parent = li_col_02

[Object]
nickname = li_col_02_prison01
pos = 650, 0, -440
rotate = 0, 90, 0
archetype = space_prison
parent = li_col_02

[Object]
nickname = li_col_02_prison02
pos = 650, 0, 440
rotate = 0, -90, 0
archetype = space_prison
parent = li_col_02

[Object]
nickname = li_col_02_dome01
pos = 950, 30, 300
rotate = 0, 225, 0
archetype = space_dome
parent = li_col_02

[Object]
nickname = li_col_02_dome02
pos = 950, 30, -300
rotate = 0, -45, 0
archetype = space_dome
parent = li_col_02

[Object]
nickname = li_col_02_dome03
pos = 350, 30, 300
rotate = 0, 135, 0
archetype = space_dome
parent = li_col_02

[Object]
nickname = li_col_02_dome04
pos = 350, 30, -300
rotate = 0, 45, 0
archetype = space_dome
parent = li_col_02

[Object]
nickname = li_col_02_tanks01
pos = 650, -240, 0
rotate = 90, 0, 0
archetype = space_tankl4x4
parent = li_col_02

[Object]
nickname = li_col_02_tanks02
pos = 650, -240, 0
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = li_col_02

[Object]
nickname = li_col_02_tanks03
pos = 650, -410, 0
rotate = 0, 0, 0
archetype = space_tanklx4
parent = li_col_02

[Object]
nickname = li_col_02_girder01
pos = 250, 0, 0
rotate = 0, -90, 0
archetype = space_girder
parent = li_col_02

[Object]
nickname = li_col_02_shipyard01
pos = 1280, 190, 0
rotate = 180,90,0
archetype = shipyard
parent = li_col_02

[Object]
nickname = li_col_02_shipyard02
pos = 1280, -190, 0
rotate = 0, 90, 0
archetype = shipyard
parent = li_col_02
'''
