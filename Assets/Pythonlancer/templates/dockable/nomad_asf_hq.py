from templates.space_object_template import SpaceObjectTemplate


# NEED A DOCK?
class AsfHQ(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'no_ord_01'
    TEMPLATE = '''[Object]
nickname = no_ord_01
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = hidden_connect
loadout = orderbase_core_fx
{root_props}

[Object]
nickname = no_ord_01_FRONT_dock01
pos = 480, 180, 884
rotate = 0, -90, 0
archetype = space_police02

[Object]
nickname = no_ord_01_FRONT_dock02
pos = -480, 180, 884
rotate = 0, 90, 0
archetype = space_police02

[Object]
nickname = no_ord_01_FRONT_dock03
pos = -480, -180, 884
rotate = 0, -90, 0
archetype = space_police02

[Object]
nickname = no_ord_01_FRONT_dock04
pos = 480, -180, 884
rotate = 0, 90, 0
archetype = space_police02

[Object]
nickname = no_ord_01_BACK_dock01
pos = 480, 180, -884
rotate = 0, -90, 0
archetype = space_police02

[Object]
nickname = no_ord_01_BACK_dock02
pos = -480, 180, -884
rotate = 0, 90, 0
archetype = space_police02

[Object]
nickname = no_ord_01_BACK_dock03
pos = -480, -180, -884
rotate = 0, -90, 0
archetype = space_police02

[Object]
nickname = no_ord_01_BACK_dock04
pos = 480, -180, -884
rotate = 0, 90, 0
archetype = space_police02

[Object]
nickname = no_ord_01_CORE_ind_A01
pos = 0, 0, 459.8
rotate = 0, -90, 0
archetype = space_industrial02a
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_A02
pos = 229.9, 0, 398.2
rotate = 0, -60, 0
archetype = space_industrial02a
loadout = orderbase_ring_connect
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_A03
pos = -229.9, 0, 398.2
rotate = 0, -120, 0
archetype = space_industrial02a
loadout = orderbase_ring_connect
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_A04
pos = 398.2, 0, 229.9
rotate = 0, -30, 0
archetype = space_industrial02a
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_A05
pos = -398.2, 0, 229.9
rotate = 0, -150, 0
archetype = space_industrial02a
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_A06
pos = 459.8, 0, 0
rotate = 0, 0, 0
archetype = space_industrial02a
loadout = orderbase_ring_connect
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_A07
pos = -459.8, 0, 0
rotate = 0, 180, 0
archetype = space_industrial02a
loadout = orderbase_ring_connect
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_A08
pos = 398.2, 0, -229.9
rotate = 0, 30, 0
archetype = space_industrial02a
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_A09
pos = -398.2, 0, -229.9
rotate = 0, 150, 0
archetype = space_industrial02a
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_A10
pos = 229.9, 0, -398.2
rotate = 0, 60, 0
archetype = space_industrial02a
loadout = orderbase_ring_connect
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_A11
pos = -229.9, 0, -398.2
rotate = 0, 120, 0
archetype = space_industrial02a
loadout = orderbase_ring_connect
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_A12
pos = 0, 0, -459.8
rotate = 0, 90, 0
archetype = space_industrial02a
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_B01
pos = 450, 0, 450
rotate = 0, 45, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_B02
pos = -450, 0, 450
rotate = 0, -45, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_B03
pos = 450, 0, -450
rotate = 0, -45, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_B04
pos = -450, 0, -450
rotate = 0, 45, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_B05
pos = -580, 0, -185
rotate = 0, 60, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_B06
pos = -580, 0, 185
rotate = 0, -60, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_B07
pos = 580, 0, -185
rotate = 0, -60, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_B08
pos = 580, 0, 185
rotate = 0, 60, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_C01
pos = 0, 0, 650
rotate = 0, 0, 0
archetype = space_industrial02a
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_C02
pos = 525, 0, 650
rotate = 0, 0, 0
archetype = space_industrial02a
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_C03
pos = -525, 0, 650
rotate = 0, 0, 0
archetype = space_industrial02a
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_C04
pos = 0, 0, -650
rotate = 0, 0, 0
archetype = space_industrial02a
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_C05
pos = 525, 0, -650
rotate = 0, 0, 0
archetype = space_industrial02a
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_C06
pos = -525, 0, -650
rotate = 0, 0, 0
archetype = space_industrial02a
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_C07
pos = -800, 0, 255
rotate = 0, 90, 0
archetype = space_industrial02a
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_C08
pos = -800, 0, -255
rotate = 0, 90, 0
archetype = space_industrial02a
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_C09
pos = 800, 0, 255
rotate = 0, 90, 0
archetype = space_industrial02a
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ind_C10
pos = 800, 0, -255
rotate = 0, 90, 0
archetype = space_industrial02a
parent = no_ord_01

[Object]
nickname = no_ord_01_CORE_ring01
pos = 0, 325, 0
rotate = 0, 0, 90
archetype = large_ring

[Object]
nickname = no_ord_01_CORE_ring02
pos = 0, 475, 0
rotate = 0, 0, 90
archetype = large_ring

[Object]
nickname = no_ord_01_CORE_ring03
pos = 0, 625, 0
rotate = 0, 0, 90
archetype = large_ring

[Object]
nickname = no_ord_01_CORE_ring04
pos = 0, 775, 0
rotate = 0, 0, 90
archetype = large_ring

[Object]
nickname = no_ord_01_CORE_ring05
pos = 0, -325, 0
rotate = 0, 0, 90
archetype = large_ring

[Object]
nickname = no_ord_01_CORE_ring06
pos = 0, -475, 0
rotate = 0, 0, 90
archetype = large_ring

[Object]
nickname = no_ord_01_CORE_ring07
pos = 0, -625, 0
rotate = 0, 0, 90
archetype = large_ring

[Object]
nickname = no_ord_01_CORE_ring08
pos = 0, -775, 0
rotate = 0, 0, 90
archetype = large_ring

[Object]
nickname = no_ord_01_FRONT_arch01
pos = 275, 300, 1275
rotate = -90, 0, 0
archetype = space_long_large_arch
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_arch02
pos = 275, -300, 1275
rotate = -90, 0, 180
archetype = space_long_large_arch
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_arch03
pos = -275, 300, 1275
rotate = -90, 0, 0
archetype = space_long_large_arch
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_arch04
pos = -275, -300, 1275
rotate = -90, 0, 180
archetype = space_long_large_arch
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_arch01
pos = 275, 300, -1275
rotate = -90, 0, 0
archetype = space_long_large_arch
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_arch02
pos = 275, -300, -1275
rotate = -90, 0, 180
archetype = space_long_large_arch
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_arch03
pos = -275, 300, -1275
rotate = -90, 0, 0
archetype = space_long_large_arch
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_arch04
pos = -275, -300, -1275
rotate = -90, 0, 180
archetype = space_long_large_arch
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_arch01
pos = 1425, 300, 0
rotate = 0, -90, -90
archetype = space_large_arch
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_arch02
pos = 1425, -300, 0
rotate = 0, 90, -90
archetype = space_large_arch
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_arch03
pos = 1725, 0, 0
rotate = 0, -90, 0
archetype = space_short_large_arch
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_arch01
pos = -1425, 300, 0
rotate = 0, 90, 90
archetype = space_large_arch
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_arch02
pos = -1425, -300, 0
rotate = 0, -90, 90
archetype = space_large_arch
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_arch03
pos = -1725, 0, 0
rotate = 0, 90, 0
archetype = space_short_large_arch
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_girder01
pos = 500, 0, 1677
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_girder02
pos = 500, 0, 1518
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_girder03
pos = 500, 0, 1359
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_girder04
pos = 500, 0, 1202
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_girder05
pos = 500, 0, 1043
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_girder06
pos = 500, 0, 884
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_girder07
pos = 0, 0, 1677
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_girder08
pos = 0, 0, 1518
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_girder09
pos = 0, 0, 1359
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_girder10
pos = 0, 0, 1202
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_girder11
pos = 0, 0, 1043
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_girder12
pos = 0, 0, 884
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_girder13
pos = -500, 0, 1677
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_girder14
pos = -500, 0, 1518
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_girder15
pos = -500, 0, 1359
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_girder16
pos = -500, 0, 1202
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_girder17
pos = -500, 0, 1043
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_girder18
pos = -500, 0, 884
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_dome01
pos = 750, 30, 1518
rotate = 0, 90, 0
archetype = space_domea
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_dome02
pos = 750, 30, 1043
rotate = 0, 90, 0
archetype = space_domea
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_dome03
pos = 750, -30, 1518
rotate = 0, 90, 180
archetype = space_domea
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_dome04
pos = 750, -30, 1043
rotate = 0, 90, 180
archetype = space_domea
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_dome05
pos = -750, 30, 1518
rotate = 0, 90, 0
archetype = space_domea
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_dome06
pos = -750, 30, 1043
rotate = 0, 90, 0
archetype = space_domea
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_dome07
pos = -750, -30, 1518
rotate = 0, 90, 180
archetype = space_domea
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_dome08
pos = -750, -30, 1043
rotate = 0, 90, 180
archetype = space_domea
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_sm_ctrltwr01
pos = 650, 0, 1677
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_sm_ctrltwr02
pos = 750, 0, 1518
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_sm_ctrltwr03
pos = 650, 0, 1359
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_sm_ctrltwr04
pos = 650, 0, 1202
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_sm_ctrltwr05
pos = 750, 0, 1043
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_sm_ctrltwr06
pos = 650, 0, 884
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_sm_ctrltwr07
pos = -650, 0, 1677
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_sm_ctrltwr08
pos = -750, 0, 1518
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_sm_ctrltwr09
pos = -650, 0, 1359
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_sm_ctrltwr10
pos = -650, 0, 1202
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_sm_ctrltwr11
pos = -750, 0, 1043
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_sm_ctrltwr12
pos = -650, 0, 884
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_lg_ctrltwr01
pos = 275, 0, 800
rotate = 0, 0, 0
archetype = space_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_lg_ctrltwr02
pos = -275, 0, 800
rotate = 0, 0, 0
archetype = space_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_lg_ctrltwr03
pos = 360, 180, 884
rotate = 0, 0, 90
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_lg_ctrltwr04
pos = 190, 180, 884
rotate = 0, 0, -90
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_lg_ctrltwr05
pos = 275, 180, 750
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_lg_ctrltwr06
pos = -360, 180, 884
rotate = 0, 0, 90
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_lg_ctrltwr07
pos = -190, 180, 884
rotate = 0, 0, -90
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_lg_ctrltwr08
pos = -275, 180, 750
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_lg_ctrltwr09
pos = 360, -180, 884
rotate = 0, 0, 90
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_lg_ctrltwr10
pos = 190, -180, 884
rotate = 0, 0, -90
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_lg_ctrltwr11
pos = 275, -180, 750
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_lg_ctrltwr12
pos = -360, -180, 884
rotate = 0, 0, 90
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_lg_ctrltwr13
pos = -190, -180, 884
rotate = 0, 0, -90
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_lg_ctrltwr14
pos = -275, -180, 750
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ind01
pos = 275, 0, 1677
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ind02
pos = 275, 0, 1518
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ind03
pos = 275, 0,  1359
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ind04
pos = 275, 0, 1202
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ind05
pos = 275, 0, 1043
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ind06
pos = -275, 0, 1677
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ind07
pos = -275, 0, 1518
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ind08
pos = -275, 0,  1359
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ind09
pos = -275, 0, 1202
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ind10
pos = -275, 0, 1043
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ind11
pos = 275, 180, 884
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ind12
pos = 0, 180, 884
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ind13
pos = -275, 180, 884
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ind14
pos = 275, 0, 884
rotate = 90, 0, 0
archetype = space_industrial02d
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ind15
pos = -275, 0, 884
rotate = 90, 0, 0
archetype = space_industrial02d
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ind16
pos = 275, -180, 884
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ind17
pos = 0, -180, 884
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ind18
pos = -275, -180, 884
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_shipyard01
pos = 170, 125, 1400
rotate = 0, 0, 45
archetype = shipyard
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_shipyard02
pos = 380, 125, 1400
rotate = 0, 0, -45
archetype = shipyard
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_shipyard03
pos = 170, -125, 1400
rotate = 0, 0, 135
archetype = shipyard
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_shipyard04
pos = 380, -125, 1400
rotate = 0, 0, -135
archetype = shipyard
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_shipyard05
pos = -170, 125, 1400
rotate = 0, 0, -45
archetype = shipyard
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_shipyard06
pos = -380, 125, 1400
rotate = 0, 0, 45
archetype = shipyard
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_shipyard07
pos = -170, -125, 1400
rotate = 0, 0, -135
archetype = shipyard
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_shipyard08
pos = -380, -125, 1400
rotate = 0, 0, 135
archetype = shipyard
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ctrl_block02
pos = 650, 65, 1359
rotate = 0, 90, 0
archetype = space_small_control_block
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ctrl_block03
pos = 650, 65, 1202
rotate = 0, 90, 0
archetype = space_small_control_block
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ctrl_block06
pos = 650, -65, 1359
rotate = 180, 90, 0
archetype = space_small_control_block
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ctrl_block07
pos = 650, -65, 1202
rotate = 180, 90, 0
archetype = space_small_control_block
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ctrl_block10
pos = -650, 65, 1359
rotate = 0, 90, 0
archetype = space_small_control_block
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ctrl_block11
pos = -650, 65, 1202
rotate = 0, 90, 0
archetype = space_small_control_block
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ctrl_block14
pos = -650, -65, 1359
rotate = 180, 90, 0
archetype = space_small_control_block
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_ctrl_block15
pos = -650, -65, 1202
rotate = 180, 90, 0
archetype = space_small_control_block
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_airlock01
pos = 470, 180, 884
rotate = 0, -90, 0
archetype = space_airlock_dummy
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_airlock02
pos = 80, 180, 884
rotate = 0, 90, 0
archetype = space_airlock_dummy
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_airlock03
pos = -470, 180, 884
rotate = 0, 90, 0
archetype = space_airlock_dummy
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_airlock04
pos = -80, 180, 884
rotate = 0, -90, 0
archetype = space_airlock_dummy
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_airlock05
pos = 470, -180, 884
rotate = 0, -90, 0
archetype = space_airlock_dummy
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_airlock06
pos = 80, -180, 884
rotate = 0, 90, 0
archetype = space_airlock_dummy
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_airlock07
pos = -470, -180, 884
rotate = 0, 90, 0
archetype = space_airlock_dummy
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_airlock08
pos = -80, -180, 884
rotate = 0, -90, 0
archetype = space_airlock_dummy
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_habitat01
pos = 275, 95, 800
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_habitat02
pos = 275, 160, 800
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_habitat03
pos = 275, 160, 735
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_habitat04
pos = 200, 90, 700
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_habitat05
pos = 350, 90, 700
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_habitat06
pos = -275, 95, 800
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_habitat07
pos = -275, 160, 800
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_habitat08
pos = -275, 160, 735
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_habitat09
pos = -200, 90, 700
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_habitat10
pos = -350, 90, 700
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_habitat11
pos = 275, -95, 800
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_habitat12
pos = 275, -160, 800
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_habitat13
pos = 275, -160, 735
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_habitat14
pos = 200, -90, 700
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_habitat15
pos = 350, -90, 700
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_habitat16
pos = -275, -95, 800
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_habitat17
pos = -275, -160, 800
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_habitat18
pos = -275, -160, 735
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_habitat19
pos = -200, -90, 700
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_FRONT_habitat20
pos = -350, -90, 700
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_girder01
pos = 500, 0, -1677
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_girder02
pos = 500, 0, -1518
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_girder03
pos = 500, 0, -1359
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_girder04
pos = 500, 0, -1202
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_girder05
pos = 500, 0, -1043
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_girder06
pos = 500, 0, -884
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_girder07
pos = 0, 0, -1677
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_girder08
pos = 0, 0, -1518
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_girder09
pos = 0, 0, -1359
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_girder10
pos = 0, 0, -1202
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_girder11
pos = 0, 0, -1043
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_girder12
pos = 0, 0, -884
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_girder13
pos = -500, 0, -1677
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_girder14
pos = -500, 0, -1518
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_girder15
pos = -500, 0, -1359
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_girder16
pos = -500, 0, -1202
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_girder17
pos = -500, 0, -1043
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_girder18
pos = -500, 0, -884
rotate = 0, 90, 0
archetype = space_girder
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_dome01
pos = 750, 30, -1518
rotate = 0, 90, 0
archetype = space_domea
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_dome02
pos = 750, 30, -1043
rotate = 0, 90, 0
archetype = space_domea
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_dome03
pos = 750, -30, -1518
rotate = 0, 90, 180
archetype = space_domea
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_dome04
pos = 750, -30, -1043
rotate = 0, 90, 180
archetype = space_domea
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_dome05
pos = -750, 30, -1518
rotate = 0, 90, 0
archetype = space_domea
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_dome06
pos = -750, 30, -1043
rotate = 0, 90, 0
archetype = space_domea
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_dome07
pos = -750, -30, -1518
rotate = 0, 90, 180
archetype = space_domea
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_dome08
pos = -750, -30, -1043
rotate = 0, 90, 180
archetype = space_domea
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_sm_ctrltwr01
pos = 650, 0, -1677
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_sm_ctrltwr02
pos = 750, 0, -1518
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_sm_ctrltwr03
pos = 650, 0, -1359
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_sm_ctrltwr04
pos = 650, 0, -1202
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_sm_ctrltwr05
pos = 750, 0, -1043
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_sm_ctrltwr06
pos = 650, 0, -884
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_sm_ctrltwr07
pos = -650, 0, -1677
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_sm_ctrltwr08
pos = -750, 0, -1518
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_sm_ctrltwr09
pos = -650, 0, -1359
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_sm_ctrltwr10
pos = -650, 0, -1202
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_sm_ctrltwr11
pos = -750, 0, -1043
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_sm_ctrltwr12
pos = -650, 0, -884
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_lg_ctrltwr01
pos = 275, 0, -800
rotate = 0, 0, 0
archetype = space_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_lg_ctrltwr02
pos = -275, 0, -800
rotate = 0, 0, 0
archetype = space_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_lg_ctrltwr03
pos = 360, 180, -884
rotate = 0, 0, 90
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_lg_ctrltwr04
pos = 190, 180, -884
rotate = 0, 0, -90
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_lg_ctrltwr05
pos = 275, 180, -750
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_lg_ctrltwr06
pos = -360, 180, -884
rotate = 0, 0, 90
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_lg_ctrltwr07
pos = -190, 180, -884
rotate = 0, 0, -90
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_lg_ctrltwr08
pos = -275, 180, -750
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_lg_ctrltwr09
pos = 360, -180, -884
rotate = 0, 0, 90
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_lg_ctrltwr10
pos = 190, -180, -884
rotate = 0, 0, -90
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_lg_ctrltwr11
pos = 275, -180, -750
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_lg_ctrltwr12
pos = -360, -180, -884
rotate = 0, 0, 90
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_lg_ctrltwr13
pos = -190, -180, -884
rotate = 0, 0, -90
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_lg_ctrltwr14
pos = -275, -180, -750
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ind01
pos = 275, 0, -1677
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ind02
pos = 275, 0, -1518
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ind03
pos = 275, 0, -1359
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ind04
pos = 275, 0, -1202
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ind05
pos = 275, 0, -1043
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ind06
pos = -275, 0, -1677
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ind07
pos = -275, 0, -1518
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ind08
pos = -275, 0, -1359
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ind09
pos = -275, 0, -1202
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ind10
pos = -275, 0, -1043
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ind11
pos = 275, 180, -884
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ind12
pos = 0, 180, -884
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ind13
pos = -275, 180, -884
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ind14
pos = 275, 0, -884
rotate = 90, 0, 0
archetype = space_industrial02d
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ind15
pos = -275, 0, -884
rotate = 90, 0, 0
archetype = space_industrial02d
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ind16
pos = 275, -180, -884
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ind17
pos = 0, -180, -884
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ind18
pos = -275, -180, -884
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_shipyard01
pos = 170, 125, -1400
rotate = 0, 180, 45
archetype = shipyard
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_shipyard02
pos = 380, 125, -1400
rotate = 0, 180, -45
archetype = shipyard
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_shipyard03
pos = 170, -125, -1400
rotate = 0, 180, 135
archetype = shipyard
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_shipyard04
pos = 380, -125, -1400
rotate = 0, 180, -135
archetype = shipyard
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_shipyard05
pos = -170, 125, -1400
rotate = 0, 180, -45
archetype = shipyard
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_shipyard06
pos = -380, 125, -1400
rotate = 0, 180, 45
archetype = shipyard
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_shipyard07
pos = -170, -125, -1400
rotate = 0, 180, -135
archetype = shipyard
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_shipyard08
pos = -380, -125, -1400
rotate = 0, 180, 135
archetype = shipyard
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ctrl_block02
pos = 650, 65, -1359
rotate = 0, 90, 0
archetype = space_small_control_block
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ctrl_block03
pos = 650, 65, -1202
rotate = 0, 90, 0
archetype = space_small_control_block
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ctrl_block06
pos = 650, -65, -1359
rotate = 180, 90, 0
archetype = space_small_control_block
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ctrl_block07
pos = 650, -65, -1202
rotate = 180, 90, 0
archetype = space_small_control_block
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ctrl_block10
pos = -650, 65, -1359
rotate = 0, 90, 0
archetype = space_small_control_block
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ctrl_block11
pos = -650, 65, -1202
rotate = 0, 90, 0
archetype = space_small_control_block
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ctrl_block14
pos = -650, -65, -1359
rotate = 180, 90, 0
archetype = space_small_control_block
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_ctrl_block15
pos = -650, -65, -1202
rotate = 180, 90, 0
archetype = space_small_control_block
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_airlock01
pos = 470, 180, -884
rotate = 0, -90, 0
archetype = space_airlock_dummy
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_airlock02
pos = 80, 180, -884
rotate = 0, 90, 0
archetype = space_airlock_dummy
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_airlock03
pos = -470, 180, -884
rotate = 0, 90, 0
archetype = space_airlock_dummy
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_airlock04
pos = -80, 180, -884
rotate = 0, -90, 0
archetype = space_airlock_dummy
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_airlock05
pos = 470, -180, -884
rotate = 0, -90, 0
archetype = space_airlock_dummy
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_airlock06
pos = 80, -180, -884
rotate = 0, 90, 0
archetype = space_airlock_dummy
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_airlock07
pos = -470, -180, -884
rotate = 0, 90, 0
archetype = space_airlock_dummy
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_airlock08
pos = -80, -180, -884
rotate = 0, -90, 0
archetype = space_airlock_dummy
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_habitat01
pos = 275, 95, -800
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_habitat02
pos = 275, 160, -800
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_habitat03
pos = 275, 160, -735
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_habitat04
pos = 200, 90, -700
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_habitat05
pos = 350, 90, -700
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_habitat06
pos = -275, 95, -800
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_habitat07
pos = -275, 160, -800
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_habitat08
pos = -275, 160, -735
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_habitat09
pos = -200, 90, -700
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_habitat10
pos = -350, 90, -700
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_habitat11
pos = 275, -95, -800
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_habitat12
pos = 275, -160, -800
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_habitat13
pos = 275, -160, -735
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_habitat14
pos = 200, -90, -700
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_habitat15
pos = 350, -90, -700
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_habitat16
pos = -275, -95, -800
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_habitat17
pos = -275, -160, -800
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_habitat18
pos = -275, -160, -735
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_habitat19
pos = -200, -90, -700
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_BACK_habitat20
pos = -350, -90, -700
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_tube01
pos = 1710, 0, 0
rotate = 0, -90, 0
archetype = space_short_tube
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_arch_part01
pos = 1075, 300, 0
rotate = 0, -90, -90
archetype = space_large_arch_part
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_arch_part02
pos = 1250, 300, 0
rotate = 0, -90, -90
archetype = space_large_arch_part
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_arch_part03
pos = 1600, 300, 0
rotate = 0, -90, -90
archetype = space_large_arch_part
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_arch_part04
pos = 1075, -300, 0
rotate = 0, 90, -90
archetype = space_large_arch_part
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_arch_part05
pos = 1250, -300, 0
rotate = 0, 90, -90
archetype = space_large_arch_part
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_arch_part06
pos = 1600, -300, 0
rotate = 0, 90, -90
archetype = space_large_arch_part
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_arch_part07
pos = 1725, 150, 0
rotate = 0, -90, 0
archetype = space_large_arch_part
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_arch_part08
pos = 1725, -150, 0
rotate = 0, -90, 0
archetype = space_large_arch_part
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_reactor01
pos = 1600, 155, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_reactor02
pos = 1600, -70, 118
rotate = 30, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_reactor03
pos = 1600, -70, -118
rotate = -30, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_reactor04
pos = 1425, -155, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_reactor05
pos = 1425, 70, 118
rotate = -30, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_reactor06
pos = 1425, 70, -118
rotate = 30, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_reactor07
pos = 1250, 155, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_reactor08
pos = 1250, -70, 118
rotate = 30, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_reactor09
pos = 1250, -70, -118
rotate = -30, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_reactor10
pos = 1075, -155, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_reactor11
pos = 1075, 70, 118
rotate = -30, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_reactor12
pos = 1075, 70, -118
rotate = 30, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_ind01
pos = 800, 0, 0
rotate = 0, 90, 0
archetype = space_industrial02a
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_ind02
pos = 580, 0, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_tanks01
pos = 1740, 150, 40
rotate = 90, -90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_tanks02
pos = 1770, 150, 120
rotate = 90, -90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_tanks03
pos = 1830, 150, 200
rotate = 90, -90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_tanks04
pos = 1740, 150, -40
rotate = 90, -90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_tanks05
pos = 1770, 150, -120
rotate = 90, -90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_tanks06
pos = 1830, 150, -200
rotate = 90, -90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_tanks07
pos = 1740, -150, 40
rotate = 90, -90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_tanks08
pos = 1770, -150, 120
rotate = 90, -90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_tanks09
pos = 1830, -150, 200
rotate = 90, -90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_tanks10
pos = 1740, -150, -40
rotate = 90, -90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_tanks11
pos = 1770, -150, -120
rotate = 90, -90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_LEFT_tanks12
pos = 1830, -150, -200
rotate = 90, -90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_tube01
pos = -1710, 0, 0
rotate = 0, 90, 0
archetype = space_short_tube
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_arch_part01
pos = -1075, 300, 0
rotate = 0, -90, -90
archetype = space_large_arch_part
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_arch_part02
pos = -1250, 300, 0
rotate = 0, -90, -90
archetype = space_large_arch_part
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_arch_part03
pos = -1600, 300, 0
rotate = 0, -90, -90
archetype = space_large_arch_part
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_arch_part04
pos = -1075, -300, 0
rotate = 0, 90, -90
archetype = space_large_arch_part
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_arch_part05
pos = -1250, -300, 0
rotate = 0, 90, -90
archetype = space_large_arch_part
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_arch_part06
pos = -1600, -300, 0
rotate = 0, 90, -90
archetype = space_large_arch_part
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_arch_part07
pos = -1725, 150, 0
rotate = 0, 90, 0
archetype = space_large_arch_part
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_arch_part08
pos = -1725, -150, 0
rotate = 0, 90, 0
archetype = space_large_arch_part
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_reactor01
pos = -1600, 155, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_reactor02
pos = -1600, -70, 118
rotate = 30, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_reactor03
pos = -1600, -70, -118
rotate = -30, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_reactor04
pos = -1425, -155, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_reactor05
pos = -1425, 70, 118
rotate = -30, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_reactor06
pos = -1425, 70, -118
rotate = 30, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_reactor07
pos = -1250, 155, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_reactor08
pos = -1250, -70, 118
rotate = 30, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_reactor09
pos = -1250, -70, -118
rotate = -30, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_reactor10
pos = -1075, -155, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_reactor11
pos = -1075, 70, 118
rotate = -30, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_reactor12
pos = -1075, 70, -118
rotate = 30, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_ind01
pos = -800, 0, 0
rotate = 0, 90, 0
archetype = space_industrial02a
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_ind02
pos = -580, 0, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_tanks01
pos = -1740, 150, 40
rotate = 90, 90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_tanks02
pos = -1770, 150, 120
rotate = 90, 90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_tanks03
pos = -1830, 150, 200
rotate = 90, 90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_tanks04
pos = -1740, 150, -40
rotate = 90, 90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_tanks05
pos = -1770, 150, -120
rotate = 90, 90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_tanks06
pos = -1830, 150, -200
rotate = 90, 90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_tanks07
pos = -1740, -150, 40
rotate = 90, 90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_tanks08
pos = -1770, -150, 120
rotate = 90, 90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_tanks09
pos = -1830, -150, 200
rotate = 90, 90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_tanks10
pos = -1740, -150, -40
rotate = 90, 90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_tanks11
pos = -1770, -150, -120
rotate = 90, 90, 0
archetype = space_tankl4
parent = no_ord_01

[Object]
nickname = no_ord_01_RIGHT_tanks12
pos = -1830, -150, -200
rotate = 90, 90, 0
archetype = space_tankl4
parent = no_ord_01
'''