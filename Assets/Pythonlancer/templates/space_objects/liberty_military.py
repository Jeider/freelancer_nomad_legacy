from templates.space_object_template import SpaceObjectTemplate


class LibertyMilitary(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_col_06'
    TEMPLATE = '''[Object]
nickname = li_col_06
ids_name = 203686
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = space_police01_columbia
ids_info = 065603
base = li_col_06_Base
dock_with = li_col_06_Base
visit = 16
reputation = li_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = li_scrote_head, li_scrote_body, prop_neuralnet_b
difficulty_level = 12
loadout = li_space_police01
pilot = pilot_solar_hardest

[Object]
nickname = li_col_06_CORE_Sphere
pos = 0, 0, 140
rotate = 0, 180, 0
archetype = sw_center_200
loadout = odissey_sphere_control_towers
parent = li_col_06

[Object]
nickname = li_col_06_prison01
pos = 0, -1, 640
rotate = 0, 0, 0
archetype = space_prison
parent = li_col_06

[Object]
nickname = li_col_06_prison02
pos = 270, 0, 530
rotate = 0, 225, 0
archetype = space_prison
parent = li_col_06

[Object]
nickname = li_col_06_prison03
pos = -270, 0, 530
rotate = 0, -45, 0
archetype = space_prison
parent = li_col_06

[Object]
nickname = li_col_06_prison04
pos = 335, 0, -160
rotate = 0, -240, 0
archetype = space_prison
parent = li_col_06

[Object]
nickname = li_col_06_prison05
pos = -335, 0, -160
rotate = 0, 60, 0
archetype = space_prison
parent = li_col_06

[Object]
nickname = li_col_06_ind01
pos = -520, 0, 290
rotate = 90, 15, 0
archetype = space_industrial02a
parent = li_col_06

[Object]
nickname = li_col_06_ind02
pos = -530, 0, 120
rotate = 90, -10, 0
archetype = space_industrial02a
parent = li_col_06

[Object]
nickname = li_col_06_ind03
pos = -415, 0, 360
rotate = 0, 10, 0
archetype = space_industrial01b
parent = li_col_06

[Object]
nickname = li_col_06_ind04
pos = -440, 0, 40
rotate = 0, 5, 0
archetype = space_industrial01b
parent = li_col_06

[Object]
nickname = li_col_06_ind05
pos = -430, 0, 200
rotate = 0, 2, 0
archetype = space_industriala
parent = li_col_06

[Object]
nickname = li_col_06_ind06
pos = 520, 0, 290
rotate = 90, -15, 0
archetype = space_industrial02a
parent = li_col_06

[Object]
nickname = li_col_06_ind07
pos = 530, 0, 120
rotate = 90, 10, 0
archetype = space_industrial02a
parent = li_col_06

[Object]
nickname = li_col_06_ind08
pos = 415, 0, 360
rotate = 0, 10, 0
archetype = space_industrial01b
parent = li_col_06

[Object]
nickname = li_col_06_ind09
pos = 440, 0, 40
rotate = 0, 5, 0
archetype = space_industrial01b
parent = li_col_06

[Object]
nickname = li_col_06_ind10
pos = 430, 0, 200
rotate = 0, 2, 0
archetype = space_industriala
parent = li_col_06

[Object]
nickname = li_col_06_tunnel_industrial01
pos = 0, 0, 470
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_06

[Object]
nickname = li_col_06_tunnel_ctrl_twr01
pos = 0, 0, 310
rotate = 90, 0, 0
archetype = space_medium_control_tower_lowdetail
parent = li_col_06

[Object]
nickname = li_col_06_tunnel_airlock01
pos = 0, 0, 320
rotate = 0, 180, 0
archetype = space_airlock_dummy
parent = li_col_06

[Object]
nickname = li_col_06_girderA01
pos = -340, -90, 140
rotate = 0, 0, 0
archetype = space_girder
parent = li_col_06

[Object]
nickname = li_col_06_girderA02
pos = -340, 90, 140
rotate = 0, 0, 0
archetype = space_girder
parent = li_col_06

[Object]
nickname = li_col_06_girderA03
pos = -340, 0, 140
rotate = 0, 0, 0
archetype = space_girder
parent = li_col_06

[Object]
nickname = li_col_06_girderA04
pos = -501, 0, 360
rotate = 0, 200, 0
archetype = space_girderc
parent = li_col_06

[Object]
nickname = li_col_06_girderA05
pos = -501, -90, 360
rotate = 0, 200, 0
archetype = space_girderc
parent = li_col_06

[Object]
nickname = li_col_06_girderA06
pos = -501, 90, 360
rotate = 0, 200, 0
archetype = space_girderc
parent = li_col_06

[Object]
nickname = li_col_06_girderA07
pos = -542, 0, 190
rotate = 0, 5, 0
archetype = space_girderc
parent = li_col_06

[Object]
nickname = li_col_06_girderA08
pos = -542, -90, 190
rotate = 0, 5, 0
archetype = space_girderc
parent = li_col_06

[Object]
nickname = li_col_06_girderA09
pos = -542, 90, 190
rotate = 0, 5, 0
archetype = space_girderc
parent = li_col_06

[Object]
nickname = li_col_06_girderA10
pos = -515, 0, 40
rotate = 0, -10, 0
archetype = space_girderc
parent = li_col_06

[Object]
nickname = li_col_06_girderA11
pos = -515, -90, 40
rotate = 0, -10, 0
archetype = space_girderc
parent = li_col_06

[Object]
nickname = li_col_06_girderA12
pos = -515, 90, 40
rotate = 0, -10, 0
archetype = space_girderc
parent = li_col_06

[Object]
nickname = li_col_06_girderB01
pos = 340, -90, 140
rotate = 0, 0, 0
archetype = space_girder
parent = li_col_06

[Object]
nickname = li_col_06_girderB02
pos = 340, 90, 140
rotate = 0, 0, 0
archetype = space_girder
parent = li_col_06

[Object]
nickname = li_col_06_girderB03
pos = 340, 0, 140
rotate = 0, 0, 0
archetype = space_girder
parent = li_col_06

[Object]
nickname = li_col_06_girderB04
pos = 501, 0, 360
rotate = 0, -200, 0
archetype = space_girderc
parent = li_col_06

[Object]
nickname = li_col_06_girderB05
pos = 501, -90, 360
rotate = 0, -200, 0
archetype = space_girderc
parent = li_col_06

[Object]
nickname = li_col_06_girderB06
pos = 501, 90, 360
rotate = 0, -200, 0
archetype = space_girderc
parent = li_col_06

[Object]
nickname = li_col_06_girderB07
pos = 542, 0, 190
rotate = 0, -5, 0
archetype = space_girderc
parent = li_col_06

[Object]
nickname = li_col_06_girderB08
pos = 542, -90, 190
rotate = 0, -5, 0
archetype = space_girderc
parent = li_col_06

[Object]
nickname = li_col_06_girderB09
pos = 542, 90, 190
rotate = 0, -5, 0
archetype = space_girderc
parent = li_col_06

[Object]
nickname = li_col_06_girderB10
pos = 515, 0, 40
rotate = 0, 10, 0
archetype = space_girderc
parent = li_col_06

[Object]
nickname = li_col_06_girderB11
pos = 515, -90, 40
rotate = 0, 10, 0
archetype = space_girderc
parent = li_col_06

[Object]
nickname = li_col_06_girderB12
pos = 515, 90, 40
rotate = 0, 10, 0
archetype = space_girderc
parent = li_col_06

[Object]
nickname = li_col_06_CORE_dock_ctrl_block01
pos = 0, -90, 280
rotate = 180, 0, 0
archetype = space_small_control_block
parent = li_col_06

[Object]
nickname = li_col_06_CORE_dock_ctrl_block02
pos = 0, -90, 0
rotate = 180, 90, 0
archetype = space_small_control_block
parent = li_col_06

[Object]
nickname = li_col_06_CORE_dock_ctrl_block03
pos = 140, -90, 140
rotate = 180, 180, 0
archetype = space_small_control_block
parent = li_col_06

[Object]
nickname = li_col_06_CORE_dock_ctrl_block04
pos = -140, -90, 140
rotate = 180, -90, 0
archetype = space_small_control_block
parent = li_col_06

[Object]
nickname = li_col_06_CORE_dock_ctrl_block05
pos = 0, 90, 280
rotate = 0, 00, 0
archetype = space_small_control_block
parent = li_col_06

[Object]
nickname = li_col_06_CORE_dock_ctrl_block06
pos = 140, 90, 140
rotate = 0, 180, 0
archetype = space_small_control_block
parent = li_col_06

[Object]
nickname = li_col_06_CORE_dock_ctrl_block07
pos = -140, 90, 140
rotate = 0, -90, 0
archetype = space_small_control_block
parent = li_col_06

[Object]
nickname = li_col_06_CORE_window01
pos = 0, 100, -20
rotate = 0, 0, 90
archetype = space_habitat_wide
parent = li_col_06

[Object]
nickname = li_col_06_CORE_window02
pos = 0, -100, -20
rotate = 0, 0, 90
archetype = space_habitat_wide
parent = li_col_06

[Object]
nickname = li_col_06_CORE_connect01
pos = -1, 0, 140
rotate = 0, 135, 0
archetype = hidden_connect_lowdetail
loadout = odissey_lock_dock_connect
parent = li_col_06

[Object]
nickname = li_col_06_CORE_connect02
pos = 0, 0, 141
rotate = 0, 90, 0
archetype = hidden_connect_lowdetail
loadout = odissey_lock_dock_connect
parent = li_col_06

[Object]
nickname = li_col_06_CORE_connect03
pos = -1, 0, 140
rotate = 0, 225, 0
archetype = hidden_connect_lowdetail
loadout = odissey_lock_dock_connect
parent = li_col_06

[Object]
nickname = li_col_06_CORE_connect04
pos = 1, 0, 140
rotate = 0, 270, 0
archetype = hidden_connect_lowdetail
loadout = odissey_lock_dock_connect
parent = li_col_06

[Object]
nickname = li_col_06_CORE_connect05
pos = 0, 0, 139
rotate = 0, 45, 0
archetype = hidden_connect_lowdetail
loadout = odissey_lock_dock_connect
parent = li_col_06

[Object]
nickname = li_col_06_CORE_connect06
pos = 0, 0, 141
rotate = 0, -45, 0
archetype = hidden_connect_lowdetail
loadout = odissey_lock_dock_connect
parent = li_col_06

[Object]
nickname = li_col_06_CORE_connectA01
pos = -1, -10, 140
rotate = 0, -22.5, 0
archetype = hidden_connect_lowdetail
loadout = odissey_front_wins_connect_full
parent = li_col_06

[Object]
nickname = li_col_06_CORE_connectA02
pos = 0, -10, 139
rotate = 0, 22.5, 0
archetype = hidden_connect_lowdetail
loadout = odissey_front_wins_connect_full
parent = li_col_06

[Object]
nickname = li_col_06_CORE_ctrl_twr03
pos = 0, 170, 140
rotate = 0, 0, 0
archetype = space_medium_control_tower_lowdetail
parent = li_col_06

[Object]
nickname = li_col_06_CORE_ctrl_twr04
pos = 0, 200, 140
rotate = 0, 0, 0
archetype = space_small_control_tower_lowdetail
parent = li_col_06

[Object]
nickname = li_col_06_CORE_ctrl_twr05
pos = 0, -170, 140
rotate = 0, 0, 0
archetype = space_medium_control_tower_lowdetail
parent = li_col_06

[Object]
nickname = li_col_06_CORE_ctrl_twr06
pos = 0, -200, 140
rotate = 0, 0, 0
archetype = space_small_control_tower_lowdetail
parent = li_col_06
'''
