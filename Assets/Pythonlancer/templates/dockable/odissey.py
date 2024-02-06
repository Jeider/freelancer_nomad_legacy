from templates.space_object_template import SpaceObjectTemplate


class Odissey(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'tau23_04'
    TEMPLATE = '''[Object]
nickname = tau4_04
pos = 0, 0, -1560
rotate = 0, 0, 0
archetype = odissey_core
parent = tau4_04
;loadout = space_police01_ku
ids_name = 203753
ids_info = 065668
base = tau4_04_base
reputation = ku_grp
behavior = NOTHING

[Object]
nickname = tau4_04_dock
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_police01_front_dock
;loadout = space_police01_ku
ids_name = 196722
ids_info = 065739
dock_with = tau4_04_base
base = tau4_04_base
reputation = ku_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = pl_male4_head, pl_trent_body, prop_neuralnet_e_right
difficulty_level = 12
pilot = pilot_solar_hardest
visit = 16

[Object]
nickname = tau4_04_D1_Sphere
pos = 0, 0, -140
rotate = 0, 0, 0
archetype = sw_center_200
loadout = odissey_sphere_control_towers
parent = tau4_04_dock

[Object]
nickname = tau4_04_D1_dock_ctrl_block01
pos = 0, -90, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = tau4_04_dock

[Object]
nickname = tau4_04_D1_dock_ctrl_block02
pos = 0, -90, -280
rotate = 180, 90, 0
archetype = space_small_control_block
parent = tau4_04_dock

[Object]
nickname = tau4_04_D1_dock_ctrl_block03
pos = 140, -90, -140
rotate = 180, 180, 0
archetype = space_small_control_block
parent = tau4_04_dock

[Object]
nickname = tau4_04_D1_dock_ctrl_block04
pos = -140, -90, -140
rotate = 180, -90, 0
archetype = space_small_control_block
parent = tau4_04_dock

[Object]
nickname = tau4_04_D1_dock_ctrl_block05
pos = 0, 90, -280
rotate = 0, 00, 0
archetype = space_small_control_block
parent = tau4_04_dock

[Object]
nickname = tau4_04_D1_dock_ctrl_block06
pos = 140, 90, -140
rotate = 0, 180, 0
archetype = space_small_control_block
parent = tau4_04_dock

[Object]
nickname = tau4_04_D1_dock_ctrl_block07
pos = -140, 90, -140
rotate = 0, -90, 0
archetype = space_small_control_block
parent = tau4_04_dock

[Object]
nickname = tau4_04_D1_window01
pos = 0, 100, 20
rotate = 0, 0, 90
archetype = space_habitat_wide
parent = tau4_04_dock

[Object]
nickname = tau4_04_D1_window02
pos = 0, -100, 20
rotate = 0, 0, 90
archetype = space_habitat_wide
parent = tau4_04_dock

[Object]
nickname = tau4_04_D1_connect01
pos = 0, 0, -141
rotate = 0, 135, 0
archetype = hidden_connect_lowdetail
loadout = odissey_lock_dock_connect
parent = tau4_04_dock

[Object]
nickname = tau4_04_D1_connect02
pos = 0, 0, -139
rotate = 0, 90, 0
archetype = hidden_connect_lowdetail
loadout = odissey_lock_dock_connect
parent = tau4_04_dock

[Object]
nickname = tau4_04_D1_connect03
pos = 1, 0, -140
rotate = 0, 225, 0
archetype = hidden_connect_lowdetail
loadout = odissey_lock_dock_connect
parent = tau4_04_dock

[Object]
nickname = tau4_04_D1_connect04
pos = -1, 0, -140
rotate = 0, 270, 0
archetype = hidden_connect_lowdetail
loadout = odissey_lock_dock_connect
parent = tau4_04_dock

[Object]
nickname = tau4_04_D1_connect05
pos = -1, 0, -141
rotate = 0, 45, 0
archetype = hidden_connect_lowdetail
loadout = odissey_lock_dock_connect
parent = tau4_04_dock

[Object]
nickname = tau4_04_D1_connect06
pos = -1, 0, -139
rotate = 0, -45, 0
archetype = hidden_connect_lowdetail
loadout = odissey_lock_dock_connect
parent = tau4_04_dock

[Object]
nickname = tau4_04_D1_connectA01
pos = 0, -10, -141
rotate = 0, -22.5, 0
archetype = hidden_connect_lowdetail
loadout = odissey_front_wins_connect_full
parent = tau4_04_dock

[Object]
nickname = tau4_04_D1_connectA02
pos = 1, -10, -141
rotate = 0, 22.5, 0
archetype = hidden_connect_lowdetail
loadout = odissey_front_wins_connect_full
parent = tau4_04_dock

[Object]
nickname = tau4_04_D1_ctrl_twr03
pos = 0, 170, -140
rotate = 0, 0, 0
archetype = space_medium_control_tower_lowdetail
parent = tau4_04_dock

[Object]
nickname = tau4_04_D1_ctrl_twr04
pos = 0, 200, -140
rotate = 0, 0, 0
archetype = space_small_control_tower_lowdetail
parent = tau4_04_dock

[Object]
nickname = tau4_04_D1_ctrl_twr05
pos = 0, -170, -140
rotate = 0, 0, 0
archetype = space_medium_control_tower_lowdetail
parent = tau4_04_dock

[Object]
nickname = tau4_04_D1_ctrl_twr06
pos = 0, -200, -140
rotate = 0, 0, 0
archetype = space_small_control_tower_lowdetail
parent = tau4_04_dock

;DOCK->ROOT CONNECTION

[Object]
nickname = tau4_04_CON01_cntrl_twr01
pos = 0, 0, -310
rotate = 90, 0, 0
archetype = space_medium_control_tower_lowdetail
parent = tau4_04

[Object]
nickname = tau4_04_CON01_cntrl_twr02
pos = 0, 0, -1170
rotate = 90, 0, 0
archetype = space_medium_control_tower_lowdetail
parent = tau4_04

[Object]
nickname = tau4_04_CON01_airlock01
pos = 0, 0, -320
rotate = 0, 0, 45
archetype = space_airlock_dummy
parent = tau4_04

[Object]
nickname = tau4_04_CON01_airlock02
pos = 0, 0, -1160
rotate = 0, 180, 45
archetype = space_airlock_dummy
parent = tau4_04

[Object]
nickname = tau4_04_CON01_ind01
pos = 0, 0, -470
rotate = 0, 0, 0
archetype = space_industriala
loadout = space_ind_girder
parent = tau4_04

[Object]
nickname = tau4_04_CON01_ind02
pos = 0, 0, -740
rotate = 0, 0, 0
archetype = space_industriala
loadout = space_ind_girder_middle
parent = tau4_04

[Object]
nickname = tau4_04_CON01_ind03
pos = 0, 0, -1010
rotate = 0, 0, 0
archetype = space_industriala
loadout = space_ind_girder
parent = tau4_04

;STATION ROOT

[Object]
nickname = tau4_04_sphere01
pos = 0, 0, -1340
rotate = 0, 0, 0
archetype = sw_center_200
loadout = odissey_sphere_control_towers
parent = tau4_04

[Object]
nickname = tau4_04_sphere02
pos = 380, 0, -1560
rotate = 0, 0, 0
archetype = sw_center_200
loadout = odissey_sphere_control_towers
parent = tau4_04

[Object]
nickname = tau4_04_sphere02_wins01
pos = 380, -10, -1560
rotate = 0, -45, 0
archetype = hidden_connect_lowdetail
loadout = odissey_front_wins_connect
parent = tau4_04

[Object]
nickname = tau4_04_sphere02_wins02
pos = 380, -10, -1560
rotate = 0, -135, 0
archetype = hidden_connect_lowdetail
loadout = odissey_front_wins_connect
parent = tau4_04

[Object]
nickname = tau4_04_sphere03
pos = -380, 0, -1560
rotate = 0, 0, 0
archetype = sw_center_200
loadout = odissey_sphere_control_towers
parent = tau4_04

[Object]
nickname = tau4_04_sphere03_wins01
pos = -380, -10, -1560
rotate = 0, 45, 0
archetype = hidden_connect_lowdetail
loadout = odissey_front_wins_connect
parent = tau4_04

[Object]
nickname = tau4_04_sphere03_wins02
pos = -380, -10, -1560
rotate = 0, 135, 0
archetype = hidden_connect_lowdetail
loadout = odissey_front_wins_connect
parent = tau4_04

[Object]
nickname = tau4_04_sphere04
pos = 0, 0, -1790
rotate = 0, 0, 0
archetype = sw_center_200
loadout = odissey_sphere_control_towers
parent = tau4_04

[Object]
nickname = tau4_04_prison01
pos = 230, 0, -1380
rotate = 0, 30, 0
archetype = space_prison_dummy
parent = tau4_04

[Object]
nickname = tau4_04_prison02
pos = -230, 0, -1380
rotate = 0, -30, 0
archetype = space_prison_dummy
parent = tau4_04

[Object]
nickname = tau4_04_prison03
pos = 230, 0, -1735
rotate = 0, -30, 0
archetype = space_prison_dummy
parent = tau4_04

[Object]
nickname = tau4_04_prison04
pos = -230, 0, -1735
rotate = 0, 30, 0
archetype = space_prison_dummy
parent = tau4_04

[Object]
nickname = tau4_04_indA01
pos = 230, 140, -1380
rotate = 0, -60, 0
archetype = space_industrial02a
parent = tau4_04

[Object]
nickname = tau4_04_indA02
pos = -230, 140, -1380
rotate = 0, 60, 0
archetype = space_industrial02a
parent = tau4_04

[Object]
nickname = tau4_04_indA03
pos = 230, 140, -1735
rotate = 0, 60, 0
archetype = space_industrial02a
parent = tau4_04

[Object]
nickname = tau4_04_indA04
pos = -230, 140, -1735
rotate = 0, -60, 0
archetype = space_industrial02a
parent = tau4_04

[Object]
nickname = tau4_04_indA05
pos = 230, -140, -1380
rotate = 0, -60, 0
archetype = space_industrial02a
parent = tau4_04

[Object]
nickname = tau4_04_indA06
pos = -230, -140, -1380
rotate = 0, 60, 0
archetype = space_industrial02a
parent = tau4_04

[Object]
nickname = tau4_04_indA07
pos = 230, -140, -1735
rotate = 0, 60, 0
archetype = space_industrial02a
parent = tau4_04

[Object]
nickname = tau4_04_indA08
pos = -230, -140, -1735
rotate = 0, -60, 0
archetype = space_industrial02a
parent = tau4_04

[Object]
nickname = tau4_04_ctrl_twrA01
pos = 0, 183, -1430
rotate = 180, 0, 0
archetype = space_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_ctrl_twrA02
pos = 0, 183, -1700
rotate = 180, 0, 0
archetype = space_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_ctrl_twrA03
pos = 280, 182, -1560
rotate = 180, 0, 0
archetype = space_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_ctrl_twrA04
pos = -280, 182, -1560
rotate = 180, 0, 0
archetype = space_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_ctrl_twrA05
pos = 0, -183, -1430
rotate = 0, 0, 0
archetype = space_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_ctrl_twrA06
pos = 0, -183, -1700
rotate = 0, 0, 0
archetype = space_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_ctrl_twrA07
pos = 280, -182, -1560
rotate = 0, 0, 0
archetype = space_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_ctrl_twrA08
pos = -280, -182, -1560
rotate = 0, 0, 0
archetype = space_control_tower
parent = tau4_04

;ROOT->LEFT CONNECTION

[Object]
nickname = tau4_04_CON02_cntrl_twr01
pos = -550, 0, -1560
rotate = 90, 90, 0
archetype = space_medium_control_tower_lowdetail
parent = tau4_04

[Object]
nickname = tau4_04_CON02_airlock01
pos = -560, 0, -1560
rotate = 90, 45, 90
archetype = space_airlock_dummy
parent = tau4_04

[Object]
nickname = tau4_04_CON02_ind01
pos = -710, 0, -1560
rotate = 0, 90, 0
archetype = space_industriala
loadout = space_ind_girder
parent = tau4_04

;ROOT->RIGHT CONNECTION

[Object]
nickname = tau4_04_CON03_cntrl_twr01
pos = 550, 0, -1560
rotate = -90, 90, 0
archetype = space_medium_control_tower_lowdetail
parent = tau4_04

[Object]
nickname = tau4_04_CON03_airlock01
pos = 560, 0, -1560
rotate = -90, 45, 90
archetype = space_airlock_dummy
parent = tau4_04

[Object]
nickname = tau4_04_CON03_ind01
pos = 710, 0, -1560
rotate = 0, 90, 0
archetype = space_industriala
loadout = space_ind_girder
parent = tau4_04


;ROOT->SHIPYARD CONNECTION

[Object]
nickname = tau4_04_CON04_cntrl_twr01
pos = 0, 0, -1960
rotate = 90, 0, 0
archetype = space_medium_control_tower_lowdetail
parent = tau4_04

[Object]
nickname = tau4_04_CON04_cntrl_twr02
pos = 0, 0, -2820
rotate = -90, 0, 0
archetype = space_medium_control_tower_lowdetail
parent = tau4_04

[Object]
nickname = tau4_04_CON04_airlock01
pos = 0, 0, -1970
rotate = 0, 0, 45
archetype = space_airlock_dummy
parent = tau4_04

[Object]
nickname = tau4_04_CON04_airlock02
pos = 0, 0, -2810
rotate = 0, 180, 45
archetype = space_airlock_dummy
parent = tau4_04

[Object]
nickname = tau4_04_CON04_ind01
pos = 0, 0, -2120
rotate = 0, 0, 0
archetype = space_industriala
loadout = space_ind_girder
parent = tau4_04

[Object]
nickname = tau4_04_CON04_ind02
pos = 0, 0, -2390
rotate = 0, 0, 0
archetype = space_industriala
loadout = space_ind_girder_middle
parent = tau4_04

[Object]
nickname = tau4_04_CON04_ind03
pos = 0, 0, -2660
rotate = 0, 0, 0
archetype = space_industriala
loadout = space_ind_girder
parent = tau4_04

;BACK SECTION (OLD SHIPYARD SECTION)

[Object]
nickname = tau4_04_D2_Sphere
pos = 0, 0, -2990
rotate = 0, 0, 0
archetype = sw_center_200
loadout = odissey_sphere_control_towers
parent = tau4_04

[Object]
nickname = tau4_04_D2_dock_ctrl_block01
pos = 0, -90, -2850
rotate = 180, 0, 0
archetype = space_small_control_block
parent = tau4_04

[Object]
nickname = tau4_04_D2_dock_ctrl_block02
pos = 0, -90, -3130
rotate = 180, 90, 0
archetype = space_small_control_block
parent = tau4_04

[Object]
nickname = tau4_04_D2_dock_ctrl_block03
pos = 140, -90, -2990
rotate = 180, 180, 0
archetype = space_small_control_block
parent = tau4_04

[Object]
nickname = tau4_04_D2_dock_ctrl_block04
pos = -140, -90, -2990
rotate = 180, -90, 0
archetype = space_small_control_block
parent = tau4_04

[Object]
nickname = tau4_04_D2_dock_ctrl_block05
pos = 0, 90, -3130
rotate = 0, 0, 0
archetype = space_small_control_block
parent = tau4_04

[Object]
nickname = tau4_04_D2_dock_ctrl_block06
pos = 140, 90, -2990
rotate = 0, 180, 0
archetype = space_small_control_block
parent = tau4_04

[Object]
nickname = tau4_04_D2_dock_ctrl_block07
pos = -140, 90, -2990
rotate = 0, -90, 0
archetype = space_small_control_block
parent = tau4_04

[Object]
nickname = tau4_04_D2_dock_ctrl_block08
pos = 0, 0, -2850
rotate = 0, 0, 0
archetype = space_small_control_block
parent = tau4_04

[Object]
nickname = tau4_04_D2_window01
pos = 0, 100, -3150
rotate = 0, 0, 90
archetype = space_habitat_wide
parent = tau4_04

[Object]
nickname = tau4_04_D2_window02
pos = 0, -100, -3150
rotate = 0, 0, 90
archetype = space_habitat_wide
parent = tau4_04

[Object]
nickname = tau4_04_D2_connect01
pos = 0, 0, -2991
rotate = 0, 0, 0
archetype = hidden_connect_lowdetail
loadout = odissey_lock_dock_connect
parent = tau4_04

[Object]
nickname = tau4_04_D2_connect02
pos = 0, 0, -2989
rotate = 0, 45, 0
archetype = hidden_connect_lowdetail
loadout = odissey_lock_dock_connect
parent = tau4_04

[Object]
nickname = tau4_04_D2_connect03
pos = 1, 0, -2990
rotate = 0, -45, 0
archetype = hidden_connect_lowdetail
loadout = odissey_lock_dock_connect
parent = tau4_04

[Object]
nickname = tau4_04_D2_connect04
pos = -1, 0, -2990
rotate = 0, 90, 0
archetype = hidden_connect_lowdetail
loadout = odissey_lock_dock_connect
parent = tau4_04

[Object]
nickname = tau4_04_D2_connect05
pos = -1, 0, -2991
rotate = 0, -90, 0
archetype = hidden_connect_lowdetail
loadout = odissey_lock_dock_connect
parent = tau4_04

[Object]
nickname = tau4_04_D2_connect06
pos = -1, 0, -2989
rotate = 0, -135, 0
archetype = hidden_connect_lowdetail
loadout = odissey_lock_dock_connect
parent = tau4_04

[Object]
nickname = tau4_04_D2_connect07
pos = 0, 0, -2992
rotate = 0, 135, 0
archetype = hidden_connect_lowdetail
loadout = odissey_lock_dock_connect
parent = tau4_04

[Object]
nickname = tau4_04_D2_connectA01
pos = 0, -10, -2991
rotate = 0, 22.5, 0
archetype = hidden_connect_lowdetail
loadout = odissey_front_wins_connect_full
parent = tau4_04

[Object]
nickname = tau4_04_D2_connectA02
pos = 1, -10, -2991
rotate = 0, -22.5, 0
archetype = hidden_connect_lowdetail
loadout = odissey_front_wins_connect_full
parent = tau4_04

[Object]
nickname = tau4_04_D2_ctrl_twr03
pos = 0, 170, -2990
rotate = 0, 0, 0
archetype = space_medium_control_tower_lowdetail
parent = tau4_04

[Object]
nickname = tau4_04_D2_ctrl_twr04
pos = 0, 200, -2990
rotate = 0, 0, 0
archetype = space_small_control_tower_lowdetail
parent = tau4_04

[Object]
nickname = tau4_04_D2_ctrl_twr05
pos = 0, -170, -2990
rotate = 0, 0, 0
archetype = space_medium_control_tower_lowdetail
parent = tau4_04

[Object]
nickname = tau4_04_D2_ctrl_twr06
pos = 0, -200, -2990
rotate = 0, 0, 0
archetype = space_small_control_tower_lowdetail
parent = tau4_04

;LEFT SECTION

[Object]
nickname = tau4_04_LEFT_ctrl_twr01
pos = -950, 0, -1560
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_LEFT_ctrl_twr02
pos = -950, 95, -1560
rotate = 180, 0, 0
archetype = space_small_control_tower_lowdetail
parent = tau4_04

[Object]
nickname = tau4_04_LEFT_ctrl_twr03
pos = -950, -105, -1560
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_LEFT_ind01
pos = -950, 20, -1560
rotate = -90, 00, 0
archetype = space_industrialc
parent = tau4_04

[Object]
nickname = tau4_04_LEFT_ind02
pos = -950, -20, -1560
rotate = 90, 0, 0
archetype = space_industrialc
parent = tau4_04

[Object]
nickname = tau4_04_LEFT_dome01
pos = -950, 51, -1825
rotate = 0, 0, 0
archetype = space_dome
parent = tau4_04

[Object]
nickname = tau4_04_LEFT_dome02
pos = -950, 51, -1295
rotate = 0, 180, 0
archetype = space_dome
parent = tau4_04

[Object]
nickname = tau4_04_LEFT_dome03
pos = -1215, 51, -1560
rotate = 0, 90, 0
archetype = space_dome
parent = tau4_04

[Object]
nickname = tau4_04_LEFT_dome04
pos = -950, -51, -1825
rotate = 0, 0, 180
archetype = space_dome
parent = tau4_04

[Object]
nickname = tau4_04_LEFT_dome05
pos = -950, -51, -1295
rotate = 0, 180, 180
archetype = space_dome
parent = tau4_04

[Object]
nickname = tau4_04_LEFT_dome06
pos = -1215, -51, -1560
rotate = 0, -90, 180
archetype = space_dome
parent = tau4_04

;RIGHT SECTION

[Object]
nickname = tau4_04_RIGHT_ctrl_twr01
pos = 950, 0, -1560
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_RIGHT_ctrl_twr02
pos = 950, 95, -1560
rotate = 180, 0, 0
archetype = space_small_control_tower_lowdetail
parent = tau4_04

[Object]
nickname = tau4_04_RIGHT_ctrl_twr03
pos = 950, -105, -1560
rotate = 0, 0, 0
archetype = space_small_control_tower_lowdetail
parent = tau4_04

[Object]
nickname = tau4_04_RIGHT_ind01
pos = 950, 20, -1560
rotate = -90, 00, 0
archetype = space_industrialc
parent = tau4_04

[Object]
nickname = tau4_04_RIGHT_ind02
pos = 950, -20, -1560
rotate = 90, 0, 0
archetype = space_industrialc
parent = tau4_04

[Object]
nickname = tau4_04_RIGHT_dome01
pos = 950, 51, -1825
rotate = 0, 0, 0
archetype = space_dome
parent = tau4_04

[Object]
nickname = tau4_04_RIGHT_dome02
pos = 950, 51, -1295
rotate = 0, 180, 0
archetype = space_dome
parent = tau4_04

[Object]
nickname = tau4_04_RIGHT_dome03
pos = 1215, 51, -1560
rotate = 0, -90, 0
archetype = space_dome
parent = tau4_04

[Object]
nickname = tau4_04_RIGHT_dome04
pos = 950, -51, -1825
rotate = 0, 0, 180
archetype = space_dome
parent = tau4_04

[Object]
nickname = tau4_04_RIGHT_dome05
pos = 950, -51, -1295
rotate = 0, 180, 180
archetype = space_dome
parent = tau4_04

[Object]
nickname = tau4_04_RIGHT_dome06
pos = 1215, -51, -1560
rotate = 0, 90, 180
archetype = space_dome
parent = tau4_04

;TOP

[Object]
nickname = tau4_04_TOP_ctrl_block01
pos = 0, 190, -1340
rotate = 0, 180, 0
archetype = space_control_block
parent = tau4_04

[Object]
nickname = tau4_04_TOP_ctrl_block02
pos = 0, 183, -1790
rotate = 0, 0, 0
archetype = space_control_block
parent = tau4_04

[Object]
nickname = tau4_04_TOP_ctrl_block03
pos = 230, 182, -1560
rotate = 0, -90, 0
archetype = space_control_block
parent = tau4_04

[Object]
nickname = tau4_04_TOP_ctrl_block04
pos = -230, 182, -1560
rotate = 0, 90, 0
archetype = space_control_block
parent = tau4_04

[Object]
nickname = tau4_04_TOP_ctrl_twr01
pos = 0, 400, -1560
rotate = 0, 0, 0
archetype = space_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_TOP_ctrl_twr02
pos = 0, 600, -1560
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_TOP_ind01
pos = 0, 280, -1560
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = tau4_04

;BOTTOM

[Object]
nickname = tau4_04_BOTTOM_ctrl_block01
pos = 0, -190, -1340
rotate = 180, 0, 0
archetype = space_control_block
parent = tau4_04

[Object]
nickname = tau4_04_BOTTOM_ctrl_block02
pos = 0, -190, -1790
rotate = 180, 180, 0
archetype = space_control_block
parent = tau4_04

[Object]
nickname = tau4_04_BOTTOM_ctrl_block03
pos = 230, -190, -1560
rotate = 180, 90, 0
archetype = space_control_block
parent = tau4_04

[Object]
nickname = tau4_04_BOTTOM_ctrl_block04
pos = -230, -190, -1560
rotate = 180, -90, 0
archetype = space_control_block
parent = tau4_04

[Object]
nickname = tau4_04_BOTTOM_ctrl_twr01
pos = 0, -400, -1560
rotate = 0, 0, 0
archetype = space_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_BOTTOM_ctrl_twr02
pos = 0, -600, -1560
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_BOTTOM_ind01
pos = 0, -280, -1560
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = tau4_04
'''
