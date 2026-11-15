from templates.space_object_template import SpaceObjectTemplate


class OdisseyOriginal(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'tau4_04'
    TEMPLATE = '''[Object]
nickname = tau4_04
pos = 0, 0, -1560
rotate = 0, 0, 0
archetype = odissey_core
{root_props}

[Object]
nickname = tau4_04_dock
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_police01_front_dock
{dock_props}

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


class OdisseySimpleOriginal(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'tau4_04'
    TEMPLATE = '''[Object]
nickname = tau4_04
pos = 0, 0, 779
rotate = 0, 90, 0
archetype = space_shipping01
{dock_props}

[Object]
nickname = tau4_04_CON01_cntrl_twr02
pos = 0, 0, -170
rotate = 90, 0, 0
archetype = space_medium_control_tower_lowdetail
parent = tau4_04

[Object]
nickname = tau4_04_CON01_airlock02
pos = 0, 0, -160
rotate = 0, 180, 45
archetype = space_airlock_dummy
parent = tau4_04

[Object]
nickname = tau4_04_A_ind01
pos = 0, 0, -10
rotate = 0, 0, 0
archetype = space_industriala
parent = tau4_04

[Object]
nickname = tau4_04_A_ind01
pos = 960, 0, -560
rotate = 0, 90, 0
archetype = space_industriala
parent = tau4_04

[Object]
nickname = tau4_04_A_ind01
pos = 710, 0, -560
rotate = 0, 90, 0
archetype = space_industriala
parent = tau4_04

[Object]
nickname = tau4_04_A_ind01
pos = -710, 0, -560
rotate = 0, 90, 0
archetype = space_industriala
parent = tau4_04

[Object]
nickname = tau4_04_A_ind01
pos = -960, 0, -560
rotate = 0, 90, 0
archetype = space_industriala
parent = tau4_04

[Object]
nickname = tau4_04_PAD_dome01
pos = 858, 31, -881.5
rotate = 0, -30, 0
archetype = space_dome
parent = tau4_04

[Object]
nickname = tau4_04_PAD_dome02
pos = 1170, 31, -834
rotate = 0, -45, 0
archetype = space_dome
parent = tau4_04

[Object]
nickname = tau4_04_PAD_dome03
pos = 858, 31, -239
rotate = 0, 210, 0
archetype = space_dome
parent = tau4_04

[Object]
nickname = tau4_04_PAD_dome04
pos = 1170, 31, -287
rotate = 0, 225, 0
archetype = space_dome
parent = tau4_04

[Object]
nickname = tau4_04_PAD_dome05
pos = 1380, 31, -560
rotate = 0, -90, 0
archetype = space_dome
parent = tau4_04

[Object]
nickname = tau4_04_PAD_dome01b
pos = -858, 31, -881.5
rotate = 0, 30, 0
archetype = space_dome
parent = tau4_04

[Object]
nickname = tau4_04_PAD_dome02b
pos = -1170, 31, -834
rotate = 0, 45, 0
archetype = space_dome
parent = tau4_04

[Object]
nickname = tau4_04_PAD_dome03b
pos = -858, 31, -239
rotate = 0, -210, 0
archetype = space_dome
parent = tau4_04

[Object]
nickname = tau4_04_PAD_dome04b
pos = -1170, 31, -287
rotate = 0, -225, 0
archetype = space_dome
parent = tau4_04

[Object]
nickname = tau4_04_PAD_dome05b
pos = -1380, 31, -560
rotate = 0, 90, 0
archetype = space_dome
parent = tau4_04

[Object]
nickname = tau4_04_sphere01
pos = 0, 0, -340
rotate = 0, 0, 0
archetype = sw_center_200
loadout = odissey_sphere_control_towers
parent = tau4_04

[Object]
nickname = tau4_04_sphere02
pos = 380, 0, -560
rotate = 0, 0, 0
archetype = sw_center_200
loadout = odissey_sphere_control_towers
parent = tau4_04

[Object]
nickname = tau4_04_sphere02_wins01
pos = 380, -10, -560
rotate = 0, -45, 0
archetype = hidden_connect_lowdetail
loadout = odissey_front_wins_connect
parent = tau4_04

[Object]
nickname = tau4_04_sphere02_wins02
pos = 380, -10, -560
rotate = 0, -135, 0
archetype = hidden_connect_lowdetail
loadout = odissey_front_wins_connect
parent = tau4_04

[Object]
nickname = tau4_04_sphere03
pos = -380, 0, -560
rotate = 0, 0, 0
archetype = sw_center_200
loadout = odissey_sphere_control_towers
parent = tau4_04

[Object]
nickname = tau4_04_sphere03_wins01
pos = -380, -10, -560
rotate = 0, 45, 0
archetype = hidden_connect_lowdetail
loadout = odissey_front_wins_connect
parent = tau4_04

[Object]
nickname = tau4_04_sphere03_wins02
pos = -380, -10, -560
rotate = 0, 135, 0
archetype = hidden_connect_lowdetail
loadout = odissey_front_wins_connect
parent = tau4_04

[Object]
nickname = tau4_04_sphere04
pos = 0, 0, -790
rotate = 0, 0, 0
archetype = sw_center_200
loadout = odissey_sphere_control_towers
parent = tau4_04

[Object]
nickname = tau4_04_prison01
pos = 230, 0, -380
rotate = 0, 30, 0
archetype = space_prison_dummy
parent = tau4_04

[Object]
nickname = tau4_04_prison02
pos = -230, 0, -380
rotate = 0, -30, 0
archetype = space_prison_dummy
parent = tau4_04

[Object]
nickname = tau4_04_prison03
pos = 230, 0, -735
rotate = 0, -30, 0
archetype = space_prison_dummy
parent = tau4_04

[Object]
nickname = tau4_04_prison04
pos = -230, 0, -735
rotate = 0, 30, 0
archetype = space_prison_dummy
parent = tau4_04

[Object]
nickname = tau4_04_indA01
pos = 230, 140, -380
rotate = 0, -60, 0
archetype = space_industrial02a
parent = tau4_04

[Object]
nickname = tau4_04_indA02
pos = -230, 140, -380
rotate = 0, 60, 0
archetype = space_industrial02a
parent = tau4_04

[Object]
nickname = tau4_04_indA03
pos = 230, 140, -735
rotate = 0, 60, 0
archetype = space_industrial02a
parent = tau4_04

[Object]
nickname = tau4_04_indA04
pos = -230, 140, -735
rotate = 0, -60, 0
archetype = space_industrial02a
parent = tau4_04

[Object]
nickname = tau4_04_indA05
pos = 230, -140, -380
rotate = 0, -60, 0
archetype = space_industrial02a
parent = tau4_04

[Object]
nickname = tau4_04_indA06
pos = -230, -140, -380
rotate = 0, 60, 0
archetype = space_industrial02a
parent = tau4_04

[Object]
nickname = tau4_04_indA07
pos = 230, -140, -735
rotate = 0, 60, 0
archetype = space_industrial02a
parent = tau4_04

[Object]
nickname = tau4_04_indA08
pos = -230, -140, -735
rotate = 0, -60, 0
archetype = space_industrial02a
parent = tau4_04

[Object]
nickname = tau4_04_ctrl_twrA01
pos = 0, 183, -430
rotate = 180, 0, 0
archetype = space_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_ctrl_twrA02
pos = 0, 183, -700
rotate = 180, 0, 0
archetype = space_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_ctrl_twrA03
pos = 280, 182, -560
rotate = 180, 0, 0
archetype = space_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_ctrl_twrA04
pos = -280, 182, -560
rotate = 180, 0, 0
archetype = space_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_ctrl_twrA05
pos = 0, -183, -430
rotate = 0, 0, 0
archetype = space_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_ctrl_twrA06
pos = 0, -183, -700
rotate = 0, 0, 0
archetype = space_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_ctrl_twrA07
pos = 280, -182, -560
rotate = 0, 0, 0
archetype = space_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_ctrl_twrA08
pos = -280, -182, -560
rotate = 0, 0, 0
archetype = space_control_tower
parent = tau4_04

[Object]
nickname = tau4_04_CON02_cntrl_twr01
pos = -550, 0, -560
rotate = 90, 90, 0
archetype = space_medium_control_tower_lowdetail
parent = tau4_04

[Object]
nickname = tau4_04_CON02_airlock01
pos = -560, 0, -560
rotate = 90, 45, 90
archetype = space_airlock_dummy
parent = tau4_04

[Object]
nickname = tau4_04_CON03_cntrl_twr01
pos = 550, 0, -560
rotate = -90, 90, 0
archetype = space_medium_control_tower_lowdetail
parent = tau4_04

[Object]
nickname = tau4_04_CON03_airlock01
pos = 560, 0, -560
rotate = -90, 45, 90
archetype = space_airlock_dummy
parent = tau4_04

[Object]
nickname = tau4_04_BOTTOM_ctrl_block04
pos = 0, 190, -820
rotate = 0, 180, 0
archetype = space_control_block
parent = tau4_04
'''

class OdisseySimple(OdisseySimpleOriginal):
    TEMPLATE = '''[Object]
nickname = tau4_04
pos = 0, 0, 779
rotate = 0, 90, 0
archetype = space_shipping01
{dock_props}

[Object]
nickname = tau4_04_CON01_cntrl_twr02
pos = 0, 0, -452.5
rotate = 0, 0, 0
archetype = batch_odissey_simple_structure0
parent = tau4_04

[Object]
nickname = tau4_04_CON01_airlock02
pos = 0, 0, -160
rotate = 0, 180, 45
archetype = space_airlock_dummy
parent = tau4_04

[Object]
nickname = tau4_04_A_ind01
pos = 0, 0, -285
rotate = 0, 0, 0
archetype = batch_odissey_simple_a0
parent = tau4_04

[Object]
nickname = tau4_04_PAD_dome01
pos = 1119, 31, -560.25
rotate = 0, 0, 0
archetype = batch_odissey_simple_pad1
parent = tau4_04

[Object]
nickname = tau4_04_PAD_dome01b
pos = -1119, 31, -560.25
rotate = 0, 0, 0
archetype = batch_odissey_simple_pad0
parent = tau4_04

[Object]
nickname = tau4_04_sphere01
pos = 0, 0, -340
rotate = 0, 0, 0
archetype = sw_center_200
loadout = odissey_sphere_control_towers
parent = tau4_04

[Object]
nickname = tau4_04_sphere02
pos = 380, 0, -560
rotate = 0, 0, 0
archetype = sw_center_200
loadout = odissey_sphere_control_towers
parent = tau4_04

[Object]
nickname = tau4_04_sphere02_wins01
pos = 380, -10, -560
rotate = 0, -45, 0
archetype = hidden_connect_lowdetail
loadout = odissey_front_wins_connect
parent = tau4_04

[Object]
nickname = tau4_04_sphere02_wins02
pos = 380, -10, -560
rotate = 0, -135, 0
archetype = hidden_connect_lowdetail
loadout = odissey_front_wins_connect
parent = tau4_04

[Object]
nickname = tau4_04_sphere03
pos = -380, 0, -560
rotate = 0, 0, 0
archetype = sw_center_200
loadout = odissey_sphere_control_towers
parent = tau4_04

[Object]
nickname = tau4_04_sphere03_wins01
pos = -380, -10, -560
rotate = 0, 45, 0
archetype = hidden_connect_lowdetail
loadout = odissey_front_wins_connect
parent = tau4_04

[Object]
nickname = tau4_04_sphere03_wins02
pos = -380, -10, -560
rotate = 0, 135, 0
archetype = hidden_connect_lowdetail
loadout = odissey_front_wins_connect
parent = tau4_04

[Object]
nickname = tau4_04_sphere04
pos = 0, 0, -790
rotate = 0, 0, 0
archetype = sw_center_200
loadout = odissey_sphere_control_towers
parent = tau4_04

[Object]
nickname = tau4_04_BOTTOM_ctrl_block04
pos = 0, 190, -820
rotate = 0, 180, 0
archetype = space_control_block
parent = tau4_04


[Object]
nickname = tau4_04_col_structure0_collision00
pos = -0.043510437, -0.00915573024, -170.149989
rotate = 0, 0, 0
archetype = batch_odissey_simple_structure0_collision00
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision01
pos = 230.13284, 3.81469727e-05, -379.575006
rotate = 0, 0, 0
archetype = batch_odissey_simple_structure0_collision01
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision02
pos = -230.461439, 3.81469727e-05, -380.096625
rotate = 0, 0, 0
archetype = batch_odissey_simple_structure0_collision02
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision03
pos = 229.538561, 3.81469727e-05, -735.096625
rotate = 0, 0, 0
archetype = batch_odissey_simple_structure0_collision03
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision04
pos = -64.6665755, 28.2716675, -615.968272
rotate = 0, 0, 0
archetype = batch_odissey_simple_structure0_collision04
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision05
pos = -0.0487976101, -0.1588974, -557.716355
rotate = 0, 0, 0
archetype = batch_odissey_simple_structure0_collision05
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision06
pos = -0.0487938638, -1.08096461, -538.380846
rotate = 0, 0, 0
archetype = batch_odissey_simple_structure0_collision06
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision07
pos = 139.932022, 182.649989, -630.014307
rotate = 0, 0, 0
archetype = batch_odissey_simple_structure0_collision07
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision08
pos = -140.067978, -0.49999861, -495.000001
rotate = 0, 0, 0
archetype = batch_odissey_simple_structure0_collision08
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision09
pos = 139.932022, -182.649987, -629.985695
rotate = 0, 0, 0
archetype = batch_odissey_simple_structure0_collision09
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision10
pos = -329.554121, -41.3646366, -559.985695
rotate = 0, 0, 0
archetype = batch_odissey_simple_structure0_collision10
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision11
pos = 1.65815851e-06, 0.00915527078, -559.95649
rotate = 0, 0, 0
archetype = batch_odissey_simple_structure0_collision11
parent = tau4_04

[Object]
nickname = tau4_04_col_a0_collision00
pos = 1.76407622, 0.222499847, -254.633591
rotate = 0, 0, 0
archetype = batch_odissey_simple_a0_collision00
parent = tau4_04

[Object]
nickname = tau4_04_col_pad1_collision00
pos = 1103.27729, 22.037796, -560.250674
rotate = 0, 0, 0
archetype = batch_odissey_simple_pad1_collision00
parent = tau4_04

[Object]
nickname = tau4_04_col_pad0_collision00
pos = -1103.27728, 22.037796, -560.249324
rotate = 0, 0, 0
archetype = batch_odissey_simple_pad0_collision00
parent = tau4_04

'''


class Odissey(OdisseyOriginal):
    TEMPLATE = '''[Object]
nickname = tau4_04
pos = 0, 0, -1560
rotate = 0, 0, 0
archetype = odissey_eight_docks
{dock_props}

[Object]
nickname = tau4_04_D1_Sphere
pos = 0, 0, -140
rotate = 0, 0, 0
archetype = sw_center_200
loadout = odissey_sphere_control_towers
parent = tau4_04
[Object]
nickname = tau4_04_D1_dock_ctrl_block01
pos = 0, 0, -130
rotate = 0, 0, 0
archetype = batch_odissey_d10
parent = tau4_04

[Object]
nickname = tau4_04_D1_connect01
pos = 0, 0, -141
rotate = 0, 135, 0
archetype = hidden_connect_lowdetail
loadout = odissey_working_dock_windows
parent = tau4_04
[Object]
nickname = tau4_04_D1_connect02
pos = 0, 0, -139
rotate = 0, 90, 0
archetype = hidden_connect_lowdetail
loadout = odissey_working_dock_windows
parent = tau4_04
[Object]
nickname = tau4_04_D1_connect03
pos = 1, 0, -140
rotate = 0, 225, 0
archetype = hidden_connect_lowdetail
loadout = odissey_working_dock_windows
parent = tau4_04
[Object]
nickname = tau4_04_D1_connect04
pos = -1, 0, -140
rotate = 0, 270, 0
archetype = hidden_connect_lowdetail
loadout = odissey_working_dock_windows
parent = tau4_04
[Object]
nickname = tau4_04_D1_connect05
pos = -1, 0, -141
rotate = 0, 45, 0
archetype = hidden_connect_lowdetail
loadout = odissey_lock_dock_connect
parent = tau4_04
[Object]
nickname = tau4_04_D1_connect06
pos = -1, 0, -139
rotate = 0, -45, 0
archetype = hidden_connect_lowdetail
loadout = odissey_lock_dock_connect
parent = tau4_04
[Object]
nickname = tau4_04_D1_connectA01
pos = 0, -10, -141
rotate = 0, -22.5, 0
archetype = hidden_connect_lowdetail
loadout = odissey_front_wins_connect_full
parent = tau4_04
[Object]
nickname = tau4_04_D1_connectA02
pos = 1, -10, -141
rotate = 0, 22.5, 0
archetype = hidden_connect_lowdetail
loadout = odissey_front_wins_connect_full
parent = tau4_04
[Object]
nickname = tau4_04_CON01_cntrl_twr01
pos = 0, 0, -935
rotate = 0, 0, 0
archetype = batch_odissey_structure1
parent = tau4_04

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
nickname = tau4_04_prison03
pos = 0, 0, -2190
rotate = 0, 0, 0
archetype = batch_odissey_structure0
parent = tau4_04

[Object]
nickname = tau4_04_CON02_airlock01
pos = -560, 0, -1560
rotate = 90, 45, 90
archetype = space_airlock_dummy
parent = tau4_04

[Object]
nickname = tau4_04_D2_Sphere
pos = 0, 0, -2990
rotate = 0, 0, 0
archetype = sw_center_200
loadout = odissey_sphere_control_towers
parent = tau4_04

[Object]
nickname = tau4_04_D2_dock_ctrl_block01
pos = 0, 0, -3000
rotate = 0, 0, 0
archetype = batch_odissey_d20
parent = tau4_04

[Object]
nickname = tau4_04_D2_connect01
pos = 0, 0, -2991
rotate = 0, 0, 0
archetype = hidden_connect_lowdetail
loadout = odissey_working_dock_windows
parent = tau4_04

[Object]
nickname = tau4_04_D2_connect02
pos = 0, 0, -2989
rotate = 0, 45, 0
archetype = hidden_connect_lowdetail
loadout = odissey_working_dock_windows
parent = tau4_04

[Object]
nickname = tau4_04_D2_connect03
pos = 1, 0, -2990
rotate = 0, -45, 0
archetype = hidden_connect_lowdetail
loadout = odissey_working_dock_windows
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
nickname = tau4_04_LEFT_ctrl_twr01
pos = -1082.5, -5, -1560
rotate = 0, 0, 0
archetype = batch_odissey_left0
parent = tau4_04

[Object]
nickname = tau4_04_RIGHT_ctrl_twr01
pos = 1082.5, -5, -1560
rotate = 0, 0, 0
archetype = batch_odissey_right0
parent = tau4_04

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
pos = 0, 440, -1560
rotate = 0, 0, 0
archetype = batch_odissey_top0
parent = tau4_04

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
pos = 0, -440, -1560
rotate = 0, 0, 0
archetype = batch_odissey_bottom0
parent = tau4_04



[Object]
nickname = tau4_04_col_d10_collision00
pos = 0.0692892075, -140.981648, 0.0650351536
rotate = 0, 0, 0
archetype = batch_odissey_d10_collision00
parent = tau4_04

[Object]
nickname = tau4_04_col_d10_collision01
pos = 0.0650351569, -140.981648, -280.069289
rotate = 0, 0, 0
archetype = batch_odissey_d10_collision01
parent = tau4_04

[Object]
nickname = tau4_04_col_d10_collision02
pos = 139.930711, -140.981648, -140.065035
rotate = 0, 0, 0
archetype = batch_odissey_d10_collision02
parent = tau4_04

[Object]
nickname = tau4_04_col_d10_collision03
pos = -140.065035, -140.981648, -139.930711
rotate = 0, 0, 0
archetype = batch_odissey_d10_collision03
parent = tau4_04

[Object]
nickname = tau4_04_col_d10_collision04
pos = 0.0692892075, 140.981647, -280.065029
rotate = 0, 0, 0
archetype = batch_odissey_d10_collision04
parent = tau4_04

[Object]
nickname = tau4_04_col_d10_collision05
pos = 139.930711, 140.981647, -139.934971
rotate = 0, 0, 0
archetype = batch_odissey_d10_collision05
parent = tau4_04

[Object]
nickname = tau4_04_col_d10_collision06
pos = -46.5257652, 140.981647, -63.4673252
rotate = 0, 0, 0
archetype = batch_odissey_d10_collision06
parent = tau4_04

[Object]
nickname = tau4_04_col_d10_collision07
pos = 0.678039549, -100.06718, 20.0919695
rotate = 0, 0, 0
archetype = batch_odissey_d10_collision07
parent = tau4_04

[Object]
nickname = tau4_04_col_d10_collision08
pos = -0.043510437, 169.850012, -139.990845
rotate = 0, 0, 0
archetype = batch_odissey_d10_collision08
parent = tau4_04

[Object]
nickname = tau4_04_col_d10_collision09
pos = 6.79901886, 169.850012, -139.990845
rotate = 0, 0, 0
archetype = batch_odissey_d10_collision09
parent = tau4_04

[Object]
nickname = tau4_04_col_d10_collision10
pos = -0.271690369, 200.215936, -138.69294
rotate = 0, 0, 0
archetype = batch_odissey_d10_collision10
parent = tau4_04

[Object]
nickname = tau4_04_col_d10_collision11
pos = -0.043510437, -170.149988, -139.990845
rotate = 0, 0, 0
archetype = batch_odissey_d10_collision11
parent = tau4_04

[Object]
nickname = tau4_04_col_d10_collision12
pos = 6.79901886, -170.149988, -139.990845
rotate = 0, 0, 0
archetype = batch_odissey_d10_collision12
parent = tau4_04

[Object]
nickname = tau4_04_col_d10_collision13
pos = -0.271690369, -199.784064, -138.69294
rotate = 0, 0, 0
archetype = batch_odissey_d10_collision13
parent = tau4_04

[Object]
nickname = tau4_04_col_structure1_collision00
pos = -0.043510437, -0.00915573024, -310.149989
rotate = 0, 0, 0
archetype = batch_odissey_structure1_collision00
parent = tau4_04

[Object]
nickname = tau4_04_col_structure1_collision01
pos = -0.043510437, -0.00915573024, -1170.14999
rotate = 0, 0, 0
archetype = batch_odissey_structure1_collision01
parent = tau4_04

[Object]
nickname = tau4_04_col_structure1_collision02
pos = -2.5332514e-07, 6.99400545e-06, -740.000003
rotate = 0, 0, 0
archetype = batch_odissey_structure1_collision02
parent = tau4_04

[Object]
nickname = tau4_04_col_structure1_collision03
pos = -2.5332514e-07, 6.99400545e-06, -846.933578
rotate = 0, 0, 0
archetype = batch_odissey_structure1_collision03
parent = tau4_04

[Object]
nickname = tau4_04_col_structure1_collision04
pos = 119.59681, 0.841880798, -1335.88405
rotate = 0, 0, 0
archetype = batch_odissey_structure1_collision04
parent = tau4_04

[Object]
nickname = tau4_04_col_structure1_collision05
pos = 305.27677, 3.81469727e-05, -1391.62147
rotate = 0, 0, 0
archetype = batch_odissey_structure1_collision05
parent = tau4_04

[Object]
nickname = tau4_04_col_structure1_collision06
pos = -340.824142, 0.841880798, -1423.67592
rotate = 0, 0, 0
archetype = batch_odissey_structure1_collision06
parent = tau4_04

[Object]
nickname = tau4_04_col_structure1_collision07
pos = -154.896509, 3.81469727e-05, -1368.49018
rotate = 0, 0, 0
archetype = batch_odissey_structure1_collision07
parent = tau4_04

[Object]
nickname = tau4_04_col_structure1_collision08
pos = -0.0487976101, 139.841103, -1380.21635
rotate = 0, 0, 0
archetype = batch_odissey_structure1_collision08
parent = tau4_04

[Object]
nickname = tau4_04_col_structure1_collision09
pos = -0.0487976101, -140.158897, -1380.21635
rotate = 0, 0, 0
archetype = batch_odissey_structure1_collision09
parent = tau4_04

[Object]
nickname = tau4_04_col_structure1_collision10
pos = -0.0679779053, 183.149989, -1430.01431
rotate = 0, 0, 0
archetype = batch_odissey_structure1_collision10
parent = tau4_04

[Object]
nickname = tau4_04_col_structure1_collision11
pos = -0.0679779053, -183.149987, -1429.98569
rotate = 0, 0, 0
archetype = batch_odissey_structure1_collision11
parent = tau4_04

[Object]
nickname = tau4_04_col_structure1_collision12
pos = -550.149989, -0.00915573024, -1559.95649
rotate = 0, 0, 0
archetype = batch_odissey_structure1_collision12
parent = tau4_04

[Object]
nickname = tau4_04_col_structure1_collision13
pos = -709.994484, 6.99400545e-06, -1560.00001
rotate = 0, 0, 0
archetype = batch_odissey_structure1_collision13
parent = tau4_04

[Object]
nickname = tau4_04_col_structure1_collision14
pos = 550.149988, 0.00915527078, -1559.95649
rotate = 0, 0, 0
archetype = batch_odissey_structure1_collision14
parent = tau4_04

[Object]
nickname = tau4_04_col_structure1_collision15
pos = 647.502802, 6.99400545e-06, -1560.00001
rotate = 0, 0, 0
archetype = batch_odissey_structure1_collision15
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision00
pos = 119.175858, 0.841880798, -1778.67592
rotate = 0, 0, 0
archetype = batch_odissey_structure0_collision00
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision01
pos = 305.103491, 3.81469727e-05, -1723.49018
rotate = 0, 0, 0
archetype = batch_odissey_structure0_collision01
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision02
pos = -340.40319, 0.841880798, -1690.88405
rotate = 0, 0, 0
archetype = batch_odissey_structure0_collision02
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision03
pos = -154.72323, 3.81469727e-05, -1746.62147
rotate = 0, 0, 0
archetype = batch_odissey_structure0_collision03
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision04
pos = -0.0487938638, 139.841103, -1735.21635
rotate = 0, 0, 0
archetype = batch_odissey_structure0_collision04
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision05
pos = -0.0487938638, -140.158897, -1735.21635
rotate = 0, 0, 0
archetype = batch_odissey_structure0_collision05
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision06
pos = -0.0679779053, 183.149989, -1700.01431
rotate = 0, 0, 0
archetype = batch_odissey_structure0_collision06
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision07
pos = 279.932022, 182.149989, -1560.01431
rotate = 0, 0, 0
archetype = batch_odissey_structure0_collision07
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision08
pos = -280.067978, 182.149989, -1560.01431
rotate = 0, 0, 0
archetype = batch_odissey_structure0_collision08
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision09
pos = -0.0679779053, -183.149987, -1699.98569
rotate = 0, 0, 0
archetype = batch_odissey_structure0_collision09
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision10
pos = 279.932022, -182.149987, -1559.98569
rotate = 0, 0, 0
archetype = batch_odissey_structure0_collision10
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision11
pos = -280.067978, -182.149987, -1559.98569
rotate = 0, 0, 0
archetype = batch_odissey_structure0_collision11
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision12
pos = -0.043510437, -0.00915573024, -1960.14999
rotate = 0, 0, 0
archetype = batch_odissey_structure0_collision12
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision13
pos = -0.043510437, 0.00915527078, -2819.85001
rotate = 0, 0, 0
archetype = batch_odissey_structure0_collision13
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision14
pos = -2.5332514e-07, 6.99400545e-06, -2390
rotate = 0, 0, 0
archetype = batch_odissey_structure0_collision14
parent = tau4_04

[Object]
nickname = tau4_04_col_structure0_collision15
pos = -2.5332514e-07, 6.99400545e-06, -2496.93358
rotate = 0, 0, 0
archetype = batch_odissey_structure0_collision15
parent = tau4_04

[Object]
nickname = tau4_04_col_d20_collision00
pos = 0.0692892075, -140.981648, -2849.93496
rotate = 0, 0, 0
archetype = batch_odissey_d20_collision00
parent = tau4_04

[Object]
nickname = tau4_04_col_d20_collision01
pos = 0.0650351569, -140.981648, -3130.06929
rotate = 0, 0, 0
archetype = batch_odissey_d20_collision01
parent = tau4_04

[Object]
nickname = tau4_04_col_d20_collision02
pos = 139.930711, -140.981648, -2990.06504
rotate = 0, 0, 0
archetype = batch_odissey_d20_collision02
parent = tau4_04

[Object]
nickname = tau4_04_col_d20_collision03
pos = -140.065035, -140.981648, -2989.93071
rotate = 0, 0, 0
archetype = batch_odissey_d20_collision03
parent = tau4_04

[Object]
nickname = tau4_04_col_d20_collision04
pos = 0.0692892075, 140.981647, -3130.06503
rotate = 0, 0, 0
archetype = batch_odissey_d20_collision04
parent = tau4_04

[Object]
nickname = tau4_04_col_d20_collision05
pos = 139.930711, 140.981647, -2989.93497
rotate = 0, 0, 0
archetype = batch_odissey_d20_collision05
parent = tau4_04

[Object]
nickname = tau4_04_col_d20_collision06
pos = -139.934971, 140.981647, -2989.93071
rotate = 0, 0, 0
archetype = batch_odissey_d20_collision06
parent = tau4_04

[Object]
nickname = tau4_04_col_d20_collision07
pos = 0.678039549, 50.9816475, -2996.43859
rotate = 0, 0, 0
archetype = batch_odissey_d20_collision07
parent = tau4_04

[Object]
nickname = tau4_04_col_d20_collision08
pos = 0.678039549, -100.06718, -3149.90803
rotate = 0, 0, 0
archetype = batch_odissey_d20_collision08
parent = tau4_04

[Object]
nickname = tau4_04_col_d20_collision09
pos = -0.043510437, 169.850012, -2989.99084
rotate = 0, 0, 0
archetype = batch_odissey_d20_collision09
parent = tau4_04

[Object]
nickname = tau4_04_col_d20_collision10
pos = 6.79901886, 169.850012, -2989.99084
rotate = 0, 0, 0
archetype = batch_odissey_d20_collision10
parent = tau4_04

[Object]
nickname = tau4_04_col_d20_collision11
pos = -0.271690369, 200.215936, -2988.69294
rotate = 0, 0, 0
archetype = batch_odissey_d20_collision11
parent = tau4_04

[Object]
nickname = tau4_04_col_d20_collision12
pos = -0.043510437, -170.149988, -2989.99084
rotate = 0, 0, 0
archetype = batch_odissey_d20_collision12
parent = tau4_04

[Object]
nickname = tau4_04_col_d20_collision13
pos = 6.79901886, -170.149988, -2989.99084
rotate = 0, 0, 0
archetype = batch_odissey_d20_collision13
parent = tau4_04

[Object]
nickname = tau4_04_col_d20_collision14
pos = -0.271690369, -199.784064, -2988.69294
rotate = 0, 0, 0
archetype = batch_odissey_d20_collision14
parent = tau4_04

[Object]
nickname = tau4_04_col_left0_collision00
pos = -950.019847, -0.149988174, -1559.95832
rotate = 0, 0, 0
archetype = batch_odissey_left0_collision00
parent = tau4_04

[Object]
nickname = tau4_04_col_left0_collision01
pos = -950.27169, 11.941909, -1560
rotate = 0, 0, 0
archetype = batch_odissey_left0_collision01
parent = tau4_04

[Object]
nickname = tau4_04_col_left0_collision02
pos = -1083.35874, -28.9282057, -1560
rotate = 0, 0, 0
archetype = batch_odissey_left0_collision02
parent = tau4_04

[Object]
nickname = tau4_04_col_right0_collision00
pos = 949.980153, -0.149988174, -1559.95832
rotate = 0, 0, 0
archetype = batch_odissey_right0_collision00
parent = tau4_04

[Object]
nickname = tau4_04_col_right0_collision01
pos = 949.72831, 11.941909, -1560
rotate = 0, 0, 0
archetype = batch_odissey_right0_collision01
parent = tau4_04

[Object]
nickname = tau4_04_col_right0_collision02
pos = 1083.35874, -28.9282057, -1560
rotate = 0, 0, 0
archetype = batch_odissey_right0_collision02
parent = tau4_04

[Object]
nickname = tau4_04_col_top0_collision00
pos = -0.0679779053, 399.850013, -1559.98569
rotate = 0, 0, 0
archetype = batch_odissey_top0_collision00
parent = tau4_04

[Object]
nickname = tau4_04_col_top0_collision01
pos = -0.043510437, 599.850012, -1559.99084
rotate = 0, 0, 0
archetype = batch_odissey_top0_collision01
parent = tau4_04

[Object]
nickname = tau4_04_col_top0_collision02
pos = -0.182491302, 280.173996, -1559.95064
rotate = 0, 0, 0
archetype = batch_odissey_top0_collision02
parent = tau4_04

[Object]
nickname = tau4_04_col_bottom0_collision00
pos = -0.0679779053, -400.149987, -1559.98569
rotate = 0, 0, 0
archetype = batch_odissey_bottom0_collision00
parent = tau4_04

[Object]
nickname = tau4_04_col_bottom0_collision01
pos = -0.043510437, -600.149988, -1559.99084
rotate = 0, 0, 0
archetype = batch_odissey_bottom0_collision01
parent = tau4_04

[Object]
nickname = tau4_04_col_bottom0_collision02
pos = -0.182491302, -279.826004, -1559.95064
rotate = 0, 0, 0
archetype = batch_odissey_bottom0_collision02
parent = tau4_04

'''
