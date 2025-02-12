from templates.space_object_template import SpaceObjectTemplate


# CHANGE TO SINGLE DOCK?
class UpsilonMegabase(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'up2_01'
    TEMPLATE = '''[Object]
nickname = up2_01
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_industriala_base_root
{root_props}

[Object]
nickname = up2_01_dockA
pos = 0, 1450, 0
rotate = 0, 0, 0
archetype = space_freeport01
{dock_props}

[Object]
nickname = up2_01_dockB
pos = 0, -1585, 0
rotate = 0, 0, 0
archetype = space_freeport01
{dock_props}

[Object]
nickname = up2_01_CORE_sphere01
pos = -500, 0, 0
rotate = 0, 0, 0
archetype = sw_center_300
parent = up2_01

[Object]
nickname = up2_01_CORE_sphere02
pos = 500, 0, 0
rotate = 0, 0, 0
archetype = sw_center_300
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_twr01
pos = -500, 270, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_twr02
pos = 500, 270, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_twr03
pos = -500, -270, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_twr04
pos = 500, -270, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_twr05
pos = -772, 0, 0
rotate = 0, 0, -90
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_twr06
pos = -228, 0, 0
rotate = 0, 0, 90
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_twr07
pos = 228, 0, 0
rotate = 0, 0, -90
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_twr08
pos = 772, 0, 0
rotate = 0, 0, 90
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_twr09
pos = 800, 0, 0
rotate = 0, 0, 90
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_twr10
pos = -800, 0, 0
rotate = 0, 0, 90
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_CORE_airlock01
pos = -500, 350, 0
rotate = 90, 0, 0
archetype = space_airlock_dummy
parent = up2_01

[Object]
nickname = up2_01_CORE_airlock02
pos = 500, 350, 0
rotate = 90, 0, 0
archetype = space_airlock_dummy
parent = up2_01

[Object]
nickname = up2_01_CORE_airlock03
pos = -500, -350, 0
rotate = -90, 0, 0
archetype = space_airlock_dummy
parent = up2_01

[Object]
nickname = up2_01_CORE_airlock04
pos = 500, -350, 0
rotate = -90, 0, 0
archetype = space_airlock_dummy
parent = up2_01

[Object]
nickname = up2_01_CORE_airlock05
pos = -850, 0, 90
rotate = 0, 90, 0
archetype = space_airlock_dummy
parent = up2_01

[Object]
nickname = up2_01_CORE_airlock06
pos = -150, 0, 0
rotate = 0, -90, 0
archetype = space_airlock_dummy
parent = up2_01

[Object]
nickname = up2_01_CORE_airlock07
pos = 150, 0, 0
rotate = 0, 90, 0
archetype = space_airlock_dummy
parent = up2_01

[Object]
nickname = up2_01_CORE_airlock08
pos = 850, 0, 90
rotate = 0, -90, 0
archetype = space_airlock_dummy
parent = up2_01

[Object]
nickname = up2_01_CORE_airlock09
pos = 850, 0, -90
rotate = 0, -90, 0
archetype = space_airlock_dummy
parent = up2_01

[Object]
nickname = up2_01_CORE_airlock10
pos = -850, 0, -90
rotate = 0, 90, 0
archetype = space_airlock_dummy
parent = up2_01

[Object]
nickname = up2_01_CORE_research01
pos = 512, 370, 0
rotate = -90, 0, 25
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_research02
pos = -512, 370, 0
rotate = -90, 0, -25
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_research03
pos = 512, -370, 0
rotate = 90, 0, -25
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_research04
pos = -512, -370, 0
rotate = 90, 0, 25
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_research05
pos = 0, 1000, 0
rotate = -90, 0, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_research06
pos = 0, -1000, 0
rotate = 90, 0, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_block01
pos = 0, -820, 880
rotate = 180, 0, 0
archetype = space_small_control_block
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_block02
pos = 0, -820, -880
rotate = 180, 0, 0
archetype = space_small_control_block
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_block03
pos = 0, 820, 880
rotate = 0, 0, 0
archetype = space_small_control_block
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_block04
pos = 0, 820, -880
rotate = 0, 0, 0
archetype = space_small_control_block
parent = up2_01

[Object]
nickname = up2_01_TOP_ctrl_twrA01
pos = 0, 1070, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_TOP_ctrl_twrA02
pos = 0, 1330, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_TOP_indA01
pos = 160, 1200, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_TOP_indA02
pos = -160, 1200, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_TOP_indA03
pos = 0, 1200, -160
rotate = 90, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_TOP_indA04
pos = 0, 1200, 160
rotate = 90, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_TOP_indA05
pos = 120, 1200, -60
rotate = 90, 30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_TOP_indA06
pos = 60, 1200, -120
rotate = 90, -30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_TOP_indA07
pos = -120, 1200, -60
rotate = 90, -30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_TOP_indA08
pos = 120, 1200, 60
rotate = 90, -30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_TOP_indA09
pos = -120, 1200, 60
rotate = 90, 30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_TOP_indA10
pos = 60, 1200, 120
rotate = 90, 30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_TOP_indA11
pos = -60, 1200, -120
rotate = 90, 30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_TOP_indA12
pos = -60, 1200, 120
rotate = 90, -30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_TOP_ctrl_twrB01
pos = 0, 1700, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_TOP_ctrl_twrB02
pos = 0, 1960, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_TOP_indB01
pos = 0, 1830, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_TOP_indB02
pos = 150, 1830, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_01

[Object]
nickname = up2_01_TOP_indB03
pos = -150, 1830, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_01

[Object]
nickname = up2_01_TOP_indB04
pos = 80, 1830, -140
rotate = 90, -30, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_01

[Object]
nickname = up2_01_TOP_indB05
pos = -80, 1830, -140
rotate = 90, 30, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_01

[Object]
nickname = up2_01_TOP_indB06
pos = 80, 1830, 140
rotate = 90, 30, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_01

[Object]
nickname = up2_01_TOP_indB07
pos = -80, 1830, 140
rotate = 90, -30, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_01

[Object]
nickname = up2_01_TOP_tube01
pos = 150, 1960, 0
rotate = -90, 0, 30
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_TOP_tube02
pos = 80, 1870, -140
rotate = -90, 0, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_TOP_tube03
pos = -70, 1900, -140
rotate = -90, 0, 20
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_TOP_tube04
pos = -70, 1870, 150
rotate = -90, 0, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_TOP_research01
pos = 80, 2700, -140
rotate = -90, 0, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_TOP_research02
pos = -320, 2700, -140
rotate = -90, 0, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_TOP_research03
pos = -215, 2700, 0
rotate = -90, 0, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_TOP_research04
pos = -70, 2700, 150
rotate = -90, 0, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_ctrl_twrA01
pos = 0, -1070, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_ctrl_twrA02
pos = 0, -1330, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA01
pos = 160, -1200, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA02
pos = -160, -1200, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA03
pos = 0, -1200, -160
rotate = 90, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA04
pos = 0, -1200, 160
rotate = 90, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA05
pos = 120, -1200, -60
rotate = 90, 30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA06
pos = 60, -1200, -120
rotate = 90, -30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA07
pos = -120, -1200, -60
rotate = 90, -30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA08
pos = 120, -1200, 60
rotate = 90, -30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA09
pos = -120, -1200, 60
rotate = 90, 30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA10
pos = 60, -1200, 120
rotate = 90, 30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA11
pos = -60, -1200, -120
rotate = 90, 30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA12
pos = -60, -1200, 120
rotate = 90, -30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_ctrl_twrB01
pos = 0, -1700, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_ctrl_twrB02
pos = 0, -1960, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indB01
pos = 0, -1830, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indB02
pos = 150, -1830, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indB03
pos = -150, -1830, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indB04
pos = 80, -1830, -140
rotate = 90, -30, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indB05
pos = -80, -1830, -140
rotate = 90, 30, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indB06
pos = 80, -1830, 140
rotate = 90, 30, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indB07
pos = -80, -1830, 140
rotate = 90, -30, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_tube01
pos = 150, -1960, 0
rotate = 90, 0, 30
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_tube02
pos = 80, -1870, -140
rotate = 90, 0, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_tube03
pos = -150, -1960, 0
rotate = 90, 0, -30
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_tube04
pos = -100, -1960, 130
rotate = 90, 0, 30
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_research01
pos = 80, -2700, -140
rotate = 90, 0, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_research02
pos = -515, -2700, 0
rotate = 90, 0, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_research03
pos = 515, -2700, 0
rotate = 90, 0, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_research04
pos = 260, -2700, 150
rotate = 90, 0, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_tube01
pos = 0, -900, 0
rotate = -90, 0, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_tube02
pos = 0, -775, 880
rotate = -90, 0, 0
archetype = space_tube_fix
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_tube03
pos = 0, 1080, 180
rotate = 25, 0, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_tube04
pos = 0, -1080, 180
rotate = -25, 0, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_tube05
pos = 0, 1080, -180
rotate = 25, 180, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_tube06
pos = 0, -775, -880
rotate = -90, 0, 0
archetype = space_tube_fix
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_tube07
pos = 0, -1080, -180
rotate = -25, 180, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_shipyard01
pos = 150, -700, -700
rotate = 0, -25, 90
archetype = shipyard
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_shipyard02
pos = 150, -300, -700
rotate = 0, -25, 90
archetype = shipyard
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_shipyard03
pos = 150, 700, -700
rotate = 0, 25, 90
archetype = shipyard
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_shipyard04
pos = 150, 300, -700
rotate = 0, 25, 90
archetype = shipyard
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_shipyard05
pos = -150, -700, -700
rotate = 0, 25, -90
archetype = shipyard
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_shipyard06
pos = -150, -300, -700
rotate = 0, 25, -90
archetype = shipyard
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_shipyard07
pos = -150, 700, -700
rotate = 0, -25, -90
archetype = shipyard
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_shipyard08
pos = -150, 300, -700
rotate = 0, -25, -90
archetype = shipyard
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_shipyard09
pos = 150, -700, 700
rotate = 0, -155, 90
archetype = shipyard
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_shipyard10
pos = 150, -300, 700
rotate = 0, -155, 90
archetype = shipyard
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_shipyard11
pos = 150, 700, 700
rotate = 0, 155, 90
archetype = shipyard
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_shipyard12
pos = 150, 300, 700
rotate = 0, 155, 90
archetype = shipyard
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_shipyard13
pos = -150, -700, 700
rotate = 0, 155, -90
archetype = shipyard
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_shipyard14
pos = -150, -300, 700
rotate = 0, 155, -90
archetype = shipyard
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_shipyard15
pos = -150, 700, 700
rotate = 0, -155, -90
archetype = shipyard
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_shipyard16
pos = -150, 300, 700
rotate = 0, -155, -90
archetype = shipyard
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder01
pos = -150, -850, 0
rotate = 0, 90, -30
archetype = space_girder
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder02
pos = 150, -850, 0
rotate = 0, 90, 30
archetype = space_girder
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder03
pos = 0, -790, 0
rotate = 60, 0, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder04
pos = 0, -790, 0
rotate = 60, 180, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder05
pos = 0, -100, 0
rotate = 10, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder06
pos = 0, -100, 0
rotate = 10, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder07
pos = 0, 100, 0
rotate = -10, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder08
pos = 0, 100, 0
rotate = -10, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder09
pos = -150, 850, 0
rotate = 0, 90, 30
archetype = space_girder
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder10
pos = 150, 850, 0
rotate = 0, 90, -30
archetype = space_girder
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder11
pos = 0, 790, 0
rotate = -60, 0, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder12
pos = 0, 790, 0
rotate = -60, 180, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder13
pos = 350, -450, 0
rotate = 90, 0, 10
archetype = space_girder
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder14
pos = -350, -450, 0
rotate = 90, 0, -10
archetype = space_girder
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder15
pos = 350, 450, 0
rotate = 90, 0, -10
archetype = space_girder
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder16
pos = -350, 450, 0
rotate = 90, 0, 10
archetype = space_girder
parent = up2_01

[Object]
nickname = up2_01_LEFT_indA01
pos = -1350, 0, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_LEFT_indA02
pos = -1631, 0, 496
rotate = 0, -60, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_LEFT_indA03
pos = -2190, 0, 496
rotate = 0, -120, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_LEFT_indA04
pos = -2468, 0, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_LEFT_indA05
pos = -1631, 0, -496
rotate = 0, 240, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_LEFT_indA06
pos = -2190, 0, -494
rotate = 0, 120, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_LEFT_indA07
pos = -1920, 20, 0
rotate = -90, 45, 0
archetype = space_industrialc
parent = up2_01

[Object]
nickname = up2_01_LEFT_indA08
pos = -3050, -550, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_LEFT_tube01
pos = -600, 0, 90
rotate = 0, -90, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_LEFT_tube02
pos = -600, 0, -90
rotate = 0, -90, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_LEFT_tube03
pos = -2500, 0, -90
rotate = 45, -90, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_LEFT_tube04
pos = -2500, 0, 90
rotate = 45, -90, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_LEFT_tube05
pos = -3050, -610, 0
rotate = 45, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_tube06
pos = -3286, -910, 0
rotate = 0, -90, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_LEFT_tube07
pos = -3050, -853, 360
rotate = 0, -90, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_LEFT_tube08
pos = -3283, -550, -420
rotate = 0, -90, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder01
pos = -1348, 0, 132
rotate = 0, -30, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder02
pos = -1734, 0, 557
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder03
pos = -2470, 0, 132
rotate = 0, 30, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder04
pos = -1348, 0, -132
rotate = 0, 210, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder05
pos = -2470, 0, -132
rotate = 0, 150, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder06
pos = -1734, 0, -557
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder07
pos = -1400, 0, 0
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder08
pos = -1400, 0, 85
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder09
pos = -1400, 0, -85
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder10
pos = -2418, 0, 0
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder11
pos = -2418, 0, 85
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder12
pos = -2418, 0, -85
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder13
pos = -3046, -550, -120
rotate = 180, 45, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder14
pos = -3050, -548, 118
rotate = 45, 0, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr01
pos = -1920, 0, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr02
pos = -1920, 160, 0
rotate = 180, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr03
pos = -1920, 465, 0
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr04
pos = -1920, 765, 0
rotate = 180, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr05
pos = -1920, 940, 0
rotate = 0, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr06
pos = -1920, 1240, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr07
pos = -1920, 1550, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr08
pos = -1920, -160, 0
rotate = 0, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr09
pos = -1920, -465, 0
rotate = 180, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr10
pos = -1920, -765, 0
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr11
pos = -1920, -940, 0
rotate = 180, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr12
pos = -1920, -1240, 0
rotate = 180, 0, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr13
pos = -1920, -1550, 0
rotate = 180, 90, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA01
pos = -1770, 80, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA02
pos = -2070, 80, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA03
pos = -1920, 80, -150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA04
pos = -1920, 80, 150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA05
pos = -2020, 80, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA06
pos = -1820, 80, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA07
pos = -1820, 80, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA08
pos = -2020, 80, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA09
pos = -1920, 245, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA10
pos = -1920, 245, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA11
pos = -1820, 245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA12
pos = -2020, 245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA13
pos = -1920, 245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA14
pos = -1920, 385, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA15
pos = -1920, 385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA16
pos = -1920, 385, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA17
pos = -1820, 385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA18
pos = -2020, 385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA19
pos = -1920, 545, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA20
pos = -1920, 545, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA21
pos = -1920, 545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA22
pos = -1820, 545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA23
pos = -2020, 545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA24
pos = -1920, 685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA25
pos = -1920, 685, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA26
pos = -1920, 685, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA27
pos = -1820, 685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA28
pos = -2020, 685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA29
pos = -1920, 855, -60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA30
pos = -1920, 855, 60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA31
pos = -1920, 855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA32
pos = -1860, 855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA33
pos = -1980, 855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA34
pos = -1920, 1020, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA35
pos = -1920, 1020, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA36
pos = -1880, 1020, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA37
pos = -1960, 1020, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA38
pos = -1920, 1160, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA39
pos = -1920, 1160, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA40
pos = -1880, 1160, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA41
pos = -1960, 1160, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA42
pos = -1960, 1320, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA43
pos = -1880, 1320, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA44
pos = -1920, 1320, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA45
pos = -1920, 1320, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA46
pos = -1880, 1520, 0
rotate = 0, 90, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA47
pos = -1960, 1520, 0
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA48
pos = -1920, 1520, -40
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA49
pos = -1920, 1520, 40
rotate = 0, 180, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA50
pos = -1920, 1600, 0
rotate = 0, 0, 0
archetype = space_small_control_block
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB01
pos = -1770, -80, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB02
pos = -2070, -80, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB03
pos = -1920, -80, -150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB04
pos = -1920, -80, 150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB05
pos = -2020, -80, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB06
pos = -1820, -80, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB07
pos = -1820, -80, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB08
pos = -2020, -80, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB09
pos = -1920, -245, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB10
pos = -1920, -245, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB11
pos = -1820, -245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB12
pos = -2020, -245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB13
pos = -1920, -245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB14
pos = -1920, -385, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB15
pos = -1920, -385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB16
pos = -1920, -385, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB17
pos = -1820, -385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB18
pos = -2020, -385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB19
pos = -1920, -545, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB20
pos = -1920, -545, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB21
pos = -1920, -545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB22
pos = -1820, -545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB23
pos = -2020, -545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB24
pos = -1920, -685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB25
pos = -1920, -685, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB26
pos = -1920, -685, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB27
pos = -1820, -685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB28
pos = -2020, -685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB29
pos = -1920, -855, -60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB30
pos = -1920, -855, 60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB31
pos = -1920, -855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB32
pos = -1860, -855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB33
pos = -1980, -855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB34
pos = -1920, -1020, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB35
pos = -1920, -1020, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB36
pos = -1880, -1020, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB37
pos = -1960, -1020, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB38
pos = -1920, -1160, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB39
pos = -1920, -1160, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB40
pos = -1880, -1160, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB41
pos = -1960, -1160, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB42
pos = -1960, -1320, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB43
pos = -1880, -1320, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB44
pos = -1920, -1320, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB45
pos = -1920, -1320, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB46
pos = -1880, -1520, 0
rotate = 180, 90, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB47
pos = -1960, -1520, 0
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB48
pos = -1920, -1520, -40
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB49
pos = -1920, -1520, 40
rotate = 180, 180, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB50
pos = -1920, -1600, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatC01
pos = -1680, 0, 410
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatC02
pos = -1582, 0, 580
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatC03
pos = -1680, 0, -410
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatC04
pos = -1582, 0, -580
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatC05
pos = -2141, 0, 410
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatC06
pos = -2237, 0, 580
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatC07
pos = -2141, 0, -410
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatC08
pos = -2237, 0, -578
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_dome01
pos = -1631, 90, 496
rotate = 0, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_LEFT_dome02
pos = -1631, -90, 496
rotate = 180, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_LEFT_dome03
pos = -2190, 90, 496
rotate = 0, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_LEFT_dome04
pos = -2190, -90, 496
rotate = 180, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_LEFT_dome05
pos = -1631, 90, -496
rotate = 0, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_LEFT_dome06
pos = -1631, -90, -496
rotate = 180, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_LEFT_dome07
pos = -2190, 90, -494
rotate = 0, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_LEFT_dome08
pos = -2190, -90, -494
rotate = 180, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_RIGHT_indA01
pos = 1350, 0, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_RIGHT_indA02
pos = 1631, 0, 496
rotate = 0, 60, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_RIGHT_indA03
pos = 2190, 0, 496
rotate = 0, 120, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_RIGHT_indA04
pos = 2468, 0, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_RIGHT_indA05
pos = 1631, 0, -496
rotate = 0, -240, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_RIGHT_indA06
pos = 2190, 0, -494
rotate = 0, -120, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_RIGHT_indA07
pos = 1920, 20, 0
rotate = -90, 45, 0
archetype = space_industrialc
parent = up2_01

[Object]
nickname = up2_01_RIGHT_indA08
pos = 3050, 540, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_RIGHT_tube01
pos = 600, 0, 90
rotate = 0, 90, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_RIGHT_tube02
pos = 600, 0, -90
rotate = 0, 90, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_RIGHT_tube03
pos = 2500, 0, -90
rotate = -45, 90, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_RIGHT_tube04
pos = 2500, 0, 90
rotate = -45, 90, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_RIGHT_tube06
pos = 3285, 540, -420
rotate = 0, 90, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_RIGHT_tube07
pos = 3285, 540, 420
rotate = 0, 90, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder01
pos = 1348, 0, 132
rotate = 0, 30, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder02
pos = 1734, 0, 557
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder03
pos = 2470, 0, 132
rotate = 0, -30, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder04
pos = 1348, 0, -132
rotate = 0, -210, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder05
pos = 2470, 0, -132
rotate = 0, -150, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder06
pos = 1734, 0, -557
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder07
pos = 1400, 0, 0
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder08
pos = 1400, 0, 85
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder09
pos = 1400, 0, -85
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder10
pos = 2418, 0, 0
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder11
pos = 2418, 0, 85
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder12
pos = 2418, 0, -85
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder13
pos = 3047, 540, -120
rotate = 180, -45, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder14
pos = 3047, 540, 120
rotate = 0, 45, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr01
pos = 1920, 0, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr02
pos = 1920, 160, 0
rotate = 180, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr03
pos = 1920, 465, 0
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr04
pos = 1920, 765, 0
rotate = 180, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr05
pos = 1920, 940, 0
rotate = 0, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr06
pos = 1920, 1240, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr07
pos = 1920, 1550, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr08
pos = 1920, -160, 0
rotate = 0, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr09
pos = 1920, -465, 0
rotate = 180, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr10
pos = 1920, -765, 0
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr11
pos = 1920, -940, 0
rotate = 180, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr12
pos = 1920, -1240, 0
rotate = 180, 0, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr13
pos = 1920, -1550, 0
rotate = 180, 90, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA01
pos = 1770, 80, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA02
pos = 2070, 80, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA03
pos = 1920, 80, -150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA04
pos = 1920, 80, 150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA05
pos = 2020, 80, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA06
pos = 1820, 80, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA07
pos = 1820, 80, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA08
pos = 2020, 80, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA09
pos = 1920, 245, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA10
pos = 1920, 245, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA11
pos = 1820, 245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA12
pos = 2020, 245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA13
pos = 1920, 245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA14
pos = 1920, 385, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA15
pos = 1920, 385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA16
pos = 1920, 385, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA17
pos = 1820, 385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA18
pos = 2020, 385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA19
pos = 1920, 545, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA20
pos = 1920, 545, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA21
pos = 1920, 545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA22
pos = 1820, 545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA23
pos = 2020, 545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA24
pos = 1920, 685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA25
pos = 1920, 685, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA26
pos = 1920, 685, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA27
pos = 1820, 685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA28
pos = 2020, 685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA29
pos = 1920, 855, -60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA30
pos = 1920, 855, 60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA31
pos = 1920, 855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA32
pos = 1860, 855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA33
pos = 1980, 855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA34
pos = 1920, 1020, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA35
pos = 1920, 1020, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA36
pos = 1880, 1020, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA37
pos = 1960, 1020, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA38
pos = 1920, 1160, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA39
pos = 1920, 1160, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA40
pos = 1880, 1160, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA41
pos = 1960, 1160, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA42
pos = 1960, 1320, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA43
pos = 1880, 1320, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA44
pos = 1920, 1320, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA45
pos = 1920, 1320, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA46
pos = 1880, 1520, 0
rotate = 0, 90, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA47
pos = 1960, 1520, 0
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA48
pos = 1920, 1520, -40
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA49
pos = 1920, 1520, 40
rotate = 0, 180, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA50
pos = 1920, 1600, 0
rotate = 0, 0, 0
archetype = space_small_control_block
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB01
pos = 1770, -80, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB02
pos = 2070, -80, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB03
pos = 1920, -80, -150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB04
pos = 1920, -80, 150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB05
pos = 2020, -80, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB06
pos = 1820, -80, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB07
pos = 1820, -80, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB08
pos = 2020, -80, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB09
pos = 1920, -245, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB10
pos = 1920, -245, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB11
pos = 1820, -245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB12
pos = 2020, -245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB13
pos = 1920, -245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB14
pos = 1920, -385, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB15
pos = 1920, -385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB16
pos = 1920, -385, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB17
pos = 1820, -385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB18
pos = 2020, -385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB19
pos = 1920, -545, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB20
pos = 1920, -545, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB21
pos = 1920, -545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB22
pos = 1820, -545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB23
pos = 2020, -545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB24
pos = 1920, -685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB25
pos = 1920, -685, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB26
pos = 1920, -685, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB27
pos = 1820, -685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB28
pos = 2020, -685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB29
pos = 1920, -855, -60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB30
pos = 1920, -855, 60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB31
pos = 1920, -855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB32
pos = 1860, -855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB33
pos = 1980, -855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB34
pos = 1920, -1020, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB35
pos = 1920, -1020, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB36
pos = 1880, -1020, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB37
pos = 1960, -1020, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB38
pos = 1920, -1160, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB39
pos = 1920, -1160, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB40
pos = 1880, -1160, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB41
pos = 1960, -1160, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB42
pos = 1960, -1320, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB43
pos = 1880, -1320, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB44
pos = 1920, -1320, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB45
pos = 1920, -1320, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB46
pos = 1880, -1520, 0
rotate = 180, 90, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB47
pos = 1960, -1520, 0
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB48
pos = 1920, -1520, -40
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB49
pos = 1920, -1520, 40
rotate = 180, 180, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB50
pos = 1920, -1600, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatC01
pos = 1680, 0, 410
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatC02
pos = 1582, 0, 580
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatC03
pos = 1680, 0, -410
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatC04
pos = 1582, 0, -580
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatC05
pos = 2141, 0, 410
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatC06
pos = 2237, 0, 580
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatC07
pos = 2141, 0, -410
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatC08
pos = 2237, 0, -578
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_dome01
pos = 1631, 90, 496
rotate = 0, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_RIGHT_dome02
pos = 1631, -90, 496
rotate = 180, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_RIGHT_dome03
pos = 2190, 90, 496
rotate = 0, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_RIGHT_dome04
pos = 2190, -90, 496
rotate = 180, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_RIGHT_dome05
pos = 1631, 90, -496
rotate = 0, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_RIGHT_dome06
pos = 1631, -90, -496
rotate = 180, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_RIGHT_dome07
pos = 2190, 90, -494
rotate = 0, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_RIGHT_dome08
pos = 2190, -90, -494
rotate = 180, -30, 0
archetype = space_domea
parent = up2_01
'''


class UpsilonLostResearch(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'up2_04'
    LOCKED_OBJECT_OFFSETS = [
        # space_prison_dummy objects
        (1300, -100, -50),  # ROTATE 180!
        (-1300, -230, 0),
    ]
    TEMPLATE = '''[Object]
nickname = up2_04
pos = 0, 0, 0
rotate = -10, 10, -100
archetype = space_prison_dummy
{dock_props}

[Object]
nickname = up2_04_prison01
pos = 300, -150, -50
rotate = 10, 0, -10
archetype = space_prison_dummy
parent = up2_04

[Object]
nickname = up2_04_prison02
pos = -320, -100, 0
rotate = -10, 180, 10
archetype = space_prison_dummy
parent = up2_04

[Object]
nickname = up2_04_prison03
pos = 50, -120, 300
rotate = 10, -80, -20
archetype = space_prison_dummy
parent = up2_04

[Object]
nickname = up2_04_prison04
pos = 0, -100, -320
rotate = 10, 90, -10
archetype = space_prison_dummy
parent = up2_04

[Object]
nickname = up2_04_conn_res01
pos = -520, -140, 0
rotate = 10, -90, 0
archetype = space_short_tube
parent = up2_04

[Object]
nickname = up2_04_conn_res02
pos = 520, -200, -50
rotate = -10, 90, 0
archetype = space_short_tube
parent = up2_04

[Object]
nickname = up2_04_conn_res03
pos = 0, -100, -450
rotate = 0, 180, 0
archetype = space_short_tube
parent = up2_04

[Object]
nickname = up2_04_conn_dock01
pos = 100, -120, 700
rotate = 20, 70, 0
archetype = space_police_dmg
parent = up2_04

[Object]
nickname = up2_04_conn_dock02
pos = 70, -120, 950
rotate = 15, -35, 10
archetype = space_police_dmg
parent = up2_04

[Object]
nickname = up2_04_conn_dock03
pos = -50, -120, 1250
rotate = 15, -150, 10
archetype = space_police_dmg
parent = up2_04

[Object]
nickname = up2_04_dmg01
pos = -100, 150, -1300
rotate = -30, 90, 0
archetype = shipyard_dmgA
parent = up2_04

[Object]
nickname = up2_04_dmg02
pos = 0, -530, -1300
rotate = -30, 120, 0
archetype = shipyard_dmgB
parent = up2_04

[Object]
nickname = up2_04_dmg03
pos = 0, -130, -1200
rotate = 0, 90, 30
archetype = space_industrial_dmg
parent = up2_04

[Object]
nickname = up2_04_indA01
pos = 280, -320, -70
rotate = 95, 0, -10
archetype = space_industrial01a
parent = up2_04

[Object]
nickname = up2_04_indA02
pos = -300, -300, -20
rotate = 95, 0, 10
archetype = space_industrial01a
parent = up2_04

[Object]
nickname = up2_04_indA03
pos = 40, -300, 320
rotate = 90, 0, -6
archetype = space_industrial01a
parent = up2_04

[Object]
nickname = up2_04_indA04
pos = -50, -270, -320
rotate = 90, 0, -15
archetype = space_industrial01a
parent = up2_04

[Object]
nickname = up2_04_indA05
pos = -30, -300, 0
rotate = 90, 0, -5
archetype = space_industrial01a
parent = up2_04

[Object]
nickname = up2_04_indB01
pos = 0, -980, 0
rotate = 90, 0, 6
archetype = space_industrial01a
parent = up2_04

[Object]
nickname = up2_04_indB02
pos = 20, -1150, 0
rotate = 0, 0, 10
archetype = space_industrial_dmg
parent = up2_04

[Object]
nickname = up2_04_indB03
pos = 20, -1150, 0
rotate = -7, 90, 0
archetype = space_industriala
parent = up2_04

[Object]
nickname = up2_04_indB04
pos = -375, -1705, 83
rotate = -80, 0, 20
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_04

[Object]
nickname = up2_04_indB05
pos = 529, -1580, 200
rotate = -60, 0, 35
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_04

[Object]
nickname = up2_04_indB06
pos = 0, -1480, 489
rotate = 60, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_04

[Object]
nickname = up2_04_indB07
pos = 100, -1480, -493
rotate = 120, 0, -50
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_04

[Object]
nickname = up2_04_indB08
pos = 0, -1580, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_04

[Object]
nickname = up2_04_indC01
pos = 30, 190, 40
rotate = 95, 0, -10
archetype = space_industrial01b
parent = up2_04

[Object]
nickname = up2_04_hab01
pos = 60, 280, 40
rotate = 0, 0, -20
archetype = space_habitat_dmg
parent = up2_04

[Object]
nickname = up2_04_girder03
pos = -190, -1260, 0
rotate = 240, -90, 0
archetype = space_beaml_dmg
parent = up2_04

[Object]
nickname = up2_04_girder05
pos = 0, -1348, -15
rotate = 100, 0, 0
archetype = space_beamx_dmg
parent = up2_04

[Object]
nickname = up2_04_girder06
pos = 0, -1495, 489
rotate = 20, 180, 0
archetype = space_girdera
parent = up2_04

[Object]
nickname = up2_04_girder07
pos = 200, -1580, 0
rotate = 90, 0, 90
archetype = space_beaml_dmg
parent = up2_04

[Object]
nickname = up2_04_girder08
pos = 0, -1580, -70
rotate = -15, 180, 0
archetype = space_girdera
parent = up2_04

[Object]
nickname = up2_04_girder09
pos = 0, -1555, -25
rotate = 20, -70, 0
archetype = space_girdera
parent = up2_04

[Object]
nickname = up2_04_tube01
pos = -55, -300, 0
rotate = 90, 0, 5
archetype = space_short_tube
parent = up2_04

[Object]
nickname = up2_04_tube02
pos = -290, -400, -30
rotate = 87, 0, 22
archetype = space_short_tube
parent = up2_04

[Object]
nickname = up2_04_tube03
pos = 280, -420, -80
rotate = 105, 0, -25
archetype = space_short_tube
parent = up2_04

[Object]
nickname = up2_04_tube04
pos = 30, -420, 320
rotate = 115, 0, -3
archetype = space_short_tube
parent = up2_04

[Object]
nickname = up2_04_tube05
pos = -80, -370, -320
rotate = 67, 0, 7
archetype = space_short_tube
parent = up2_04

[Object]
nickname = up2_04_tube06
pos = 0, -1600, 0
rotate = 90, 0, 0
archetype = space_short_tube
parent = up2_04

[Object]
nickname = up2_04_tube07
pos = -200, -2260, -693
rotate = 250, -120, 0
archetype = space_short_tube
parent = up2_04

[Object]
nickname = up2_04_tube08
pos = 0, -1700, 289
rotate = 60, 0, 0
archetype = space_short_tube
parent = up2_04

[Object]
nickname = up2_04_tube09
pos = 580, -1650, 140
rotate = 100, 0, 22
archetype = space_short_tube
parent = up2_04

[Object]
nickname = up2_04_tube10
pos = -340, -1800, 50
rotate = 85, 0, 10
archetype = space_short_tube
parent = up2_04

[Object]
nickname = up2_04_research01
pos = -260, -2640, 100
rotate = 90, 0, -15
archetype = space_research
parent = up2_04

[Object]
nickname = up2_04_research02
pos = 850, -2480, 0
rotate = 90, 0, -5
archetype = space_research
parent = up2_04

[Object]
nickname = up2_04_research03
pos = 0, -4300, 680
rotate = -85, 0, -5
archetype = space_tube_fix
parent = up2_04

[Object]
nickname = up2_04_research04
pos = 0, -2480, -500
rotate = 95, 0, 0
archetype = space_research
parent = up2_04

[Object]
nickname = up2_04_research05
pos = 0, -2480, 0
rotate = 90, 0, 0
archetype = space_industrial_dmg
parent = up2_04

[Object]
nickname = up2_04_research01a
pos = -760, -4400, 100
rotate = 90, 0, 5
archetype = space_tube_fix
parent = up2_04

[Object]
nickname = up2_04_research02a
pos = 680, -4400, 0
rotate = 90, 0, 0
archetype = space_tube_fix
parent = up2_04

[Object]
nickname = up2_04_research03a
pos = 0, -4400, 680
rotate = 90, 0, 0
archetype = space_research
parent = up2_04

[Object]
nickname = up2_04_research04a
pos = 0, -4400, -680
rotate = 90, 0, 0
archetype = space_tube_fix
parent = up2_04

[Object]
nickname = up2_04_research05a
pos = 0, -4100, 0
rotate = 85, 0, 5
archetype = space_tube_fix
parent = up2_04
'''


class GasInsideSingleTower(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'up2_01'
    TEMPLATE = '''[Object]
nickname = up2_01_TOWER_indA01
pos = 570, 0, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_TOWER_indA02
pos = 289, 0, 496
rotate = 0, -60, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_TOWER_indA03
pos = -270, 0, 496
rotate = 0, -120, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_TOWER_indA04
pos = -548, 0, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_TOWER_indA05
pos = 289, 0, -496
rotate = 0, 240, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_TOWER_indA06
pos = -270, 0, -494
rotate = 0, 120, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_TOWER_indA07
pos = 0, 20, 0
rotate = -90, 45, 0
archetype = space_industrialc
parent = up2_01

[Object]
nickname = up2_01_TOWER_girder01
pos = 572, 0, 132
rotate = 0, -30, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_TOWER_girder02
pos = 186, 0, 557
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_TOWER_girder03
pos = -550, 0, 132
rotate = 0, 30, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_TOWER_girder04
pos = 572, 0, -132
rotate = 0, 210, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_TOWER_girder05
pos = -550, 0, -132
rotate = 0, 150, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_TOWER_girder06
pos = 186, 0, -557
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_TOWER_girder07
pos = 520, 0, 0
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_TOWER_girder08
pos = 520, 0, 85
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_TOWER_girder09
pos = 520, 0, -85
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_TOWER_girder10
pos = -498, 0, 0
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_TOWER_girder11
pos = -498, 0, 85
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_TOWER_girder12
pos = -498, 0, -85
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_TOWER_ctrl_twr01
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_TOWER_ctrl_twr02
pos = 0, 160, 0
rotate = 180, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_TOWER_ctrl_twr03
pos = 0, 465, 0
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_TOWER_ctrl_twr04
pos = 0, 765, 0
rotate = 180, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_TOWER_ctrl_twr05
pos = 0, 940, 0
rotate = 0, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_TOWER_ctrl_twr06
pos = 0, 1240, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_TOWER_ctrl_twr07
pos = 0, 1550, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_TOWER_ctrl_twr08
pos = 0, -160, 0
rotate = 0, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_TOWER_ctrl_twr09
pos = 0, -465, 0
rotate = 180, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_TOWER_ctrl_twr10
pos = 0, -765, 0
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_TOWER_ctrl_twr11
pos = 0, -940, 0
rotate = 180, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_TOWER_ctrl_twr12
pos = 0, -1240, 0
rotate = 180, 0, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_TOWER_ctrl_twr13
pos = 0, -1550, 0
rotate = 180, 90, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA01
pos = 150, 80, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA02
pos = -150, 80, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA03
pos = 0, 80, -150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA04
pos = 0, 80, 150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA05
pos = -100, 80, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA06
pos = 100, 80, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA07
pos = 100, 80, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA08
pos = -100, 80, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA09
pos = 0, 245, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA10
pos = 0, 245, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA11
pos = 100, 245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA12
pos = -100, 245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA13
pos = 0, 245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA14
pos = 0, 385, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA15
pos = 0, 385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA16
pos = 0, 385, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA17
pos = 100, 385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA18
pos = -100, 385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA19
pos = 0, 545, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA20
pos = 0, 545, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA21
pos = 0, 545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA22
pos = 100, 545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA23
pos = -100, 545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA24
pos = 0, 685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA25
pos = 0, 685, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA26
pos = 0, 685, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA27
pos = 100, 685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA28
pos = -100, 685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA29
pos = 0, 855, -60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA30
pos = 0, 855, 60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA31
pos = 0, 855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA32
pos = 60, 855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA33
pos = -60, 855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA34
pos = 0, 1020, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA35
pos = 0, 1020, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA36
pos = 40, 1020, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA37
pos = -40, 1020, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA38
pos = 0, 1160, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA39
pos = 0, 1160, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA40
pos = 40, 1160, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA41
pos = -40, 1160, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA42
pos = -40, 1320, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA43
pos = 40, 1320, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA44
pos = 0, 1320, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA45
pos = 0, 1320, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA46
pos = 40, 1520, 0
rotate = 0, 90, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA47
pos = -40, 1520, 0
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA48
pos = 0, 1520, -40
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA49
pos = 0, 1520, 40
rotate = 0, 180, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatA50
pos = 0, 1600, 0
rotate = 0, 0, 0
archetype = space_small_control_block
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB01
pos = 150, -80, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB02
pos = -150, -80, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB03
pos = 0, -80, -150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB04
pos = 0, -80, 150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB05
pos = -100, -80, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB06
pos = 100, -80, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB07
pos = 100, -80, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB08
pos = -100, -80, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB09
pos = 0, -245, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB10
pos = 0, -245, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB11
pos = 100, -245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB12
pos = -100, -245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB13
pos = 0, -245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB14
pos = 0, -385, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB15
pos = 0, -385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB16
pos = 0, -385, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB17
pos = 100, -385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB18
pos = -100, -385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB19
pos = 0, -545, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB20
pos = 0, -545, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB21
pos = 0, -545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB22
pos = 100, -545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB23
pos = -100, -545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB24
pos = 0, -685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB25
pos = 0, -685, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB26
pos = 0, -685, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB27
pos = 100, -685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB28
pos = -100, -685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB29
pos = 0, -855, -60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB30
pos = 0, -855, 60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB31
pos = 0, -855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB32
pos = 60, -855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB33
pos = -60, -855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB34
pos = 0, -1020, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB35
pos = 0, -1020, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB36
pos = 40, -1020, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB37
pos = -40, -1020, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB38
pos = 0, -1160, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB39
pos = 0, -1160, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB40
pos = 40, -1160, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB41
pos = -40, -1160, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB42
pos = -40, -1320, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB43
pos = 40, -1320, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB44
pos = 0, -1320, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB45
pos = 0, -1320, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB46
pos = 40, -1520, 0
rotate = 180, 90, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB47
pos = -40, -1520, 0
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB48
pos = 0, -1520, -40
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB49
pos = 0, -1520, 40
rotate = 180, 180, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatB50
pos = 0, -1600, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatC01
pos = 240, 0, 410
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatC02
pos = 338, 0, 580
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatC03
pos = 240, 0, -410
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatC04
pos = 338, 0, -580
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatC05
pos = -221, 0, 410
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatC06
pos = -317, 0, 580
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatC07
pos = -221, 0, -410
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_habitatC08
pos = -317, 0, -578
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_TOWER_dome01
pos = 289, 90, 496
rotate = 0, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_TOWER_dome02
pos = 289, -90, 496
rotate = 180, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_TOWER_dome03
pos = -270, 90, 496
rotate = 0, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_TOWER_dome04
pos = -270, -90, 496
rotate = 180, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_TOWER_dome05
pos = 289, 90, -496
rotate = 0, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_TOWER_dome06
pos = 289, -90, -496
rotate = 180, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_TOWER_dome07
pos = -270, 90, -494
rotate = 0, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_TOWER_dome08
pos = -270, -90, -494
rotate = 180, 30, 0
archetype = space_domea
parent = up2_01
'''


class Vienna(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'up2_01'
    TEMPLATE = '''[Object]
nickname = up2_01
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_industriala_base_root

[Object]
nickname = up2_01_CORE_sphere01
pos = -500, 0, 0
rotate = 0, 0, 0
archetype = sw_center_300
parent = up2_01

[Object]
nickname = up2_01_CORE_sphere02
pos = 500, 0, 0
rotate = 0, 0, 0
archetype = sw_center_300
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_twr01
pos = -500, 270, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_twr02
pos = 500, 270, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_twr03
pos = -500, -270, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_twr04
pos = 500, -270, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_twr05
pos = -772, 0, 0
rotate = 0, 0, -90
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_twr06
pos = -228, 0, 0
rotate = 0, 0, 90
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_twr07
pos = 228, 0, 0
rotate = 0, 0, -90
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_twr08
pos = 772, 0, 0
rotate = 0, 0, 90
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_twr09
pos = 800, 0, 0
rotate = 0, 0, 90
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_CORE_ctrl_twr10
pos = -800, 0, 0
rotate = 0, 0, 90
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_CORE_airlock01
pos = -500, 350, 0
rotate = 90, 0, 0
archetype = space_airlock_dummy
parent = up2_01

[Object]
nickname = up2_01_CORE_airlock02
pos = 500, 350, 0
rotate = 90, 0, 0
archetype = space_airlock_dummy
parent = up2_01

[Object]
nickname = up2_01_CORE_airlock03
pos = -500, -350, 0
rotate = -90, 0, 0
archetype = space_airlock_dummy
parent = up2_01

[Object]
nickname = up2_01_CORE_airlock04
pos = 500, -350, 0
rotate = -90, 0, 0
archetype = space_airlock_dummy
parent = up2_01

[Object]
nickname = up2_01_CORE_airlock05
pos = -850, 0, 90
rotate = 0, 90, 0
archetype = space_airlock_dummy
parent = up2_01

[Object]
nickname = up2_01_CORE_airlock06
pos = -150, 0, 0
rotate = 0, -90, 0
archetype = space_airlock_dummy
parent = up2_01

[Object]
nickname = up2_01_CORE_airlock07
pos = 150, 0, 0
rotate = 0, 90, 0
archetype = space_airlock_dummy
parent = up2_01

[Object]
nickname = up2_01_CORE_airlock08
pos = 850, 0, 90
rotate = 0, -90, 0
archetype = space_airlock_dummy
parent = up2_01

[Object]
nickname = up2_01_CORE_airlock09
pos = 850, 0, -90
rotate = 0, -90, 0
archetype = space_airlock_dummy
parent = up2_01

[Object]
nickname = up2_01_CORE_airlock10
pos = -850, 0, -90
rotate = 0, 90, 0
archetype = space_airlock_dummy
parent = up2_01

[Object]
nickname = up2_01_CORE_research01
pos = 512, 370, 0
rotate = -90, 0, 25
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_research02
pos = -512, 370, 0
rotate = -90, 0, -25
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_research03
pos = 512, -370, 0
rotate = 90, 0, -25
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_research04
pos = -512, -370, 0
rotate = 90, 0, 25
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_research05
pos = 0, 1000, 0
rotate = -90, 0, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_research06
pos = 0, -1000, 0
rotate = 90, 0, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_TOP_ctrl_twrA01
pos = 0, 1070, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_TOP_ctrl_twrA02
pos = 0, 1330, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_TOP_indA01
pos = 160, 1200, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_TOP_indA02
pos = -160, 1200, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_TOP_indA03
pos = 0, 1200, -160
rotate = 90, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_TOP_indA04
pos = 0, 1200, 160
rotate = 90, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_TOP_indA05
pos = 120, 1200, -60
rotate = 90, 30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_TOP_indA06
pos = 60, 1200, -120
rotate = 90, -30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_TOP_indA07
pos = -120, 1200, -60
rotate = 90, -30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_TOP_indA08
pos = 120, 1200, 60
rotate = 90, -30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_TOP_indA09
pos = -120, 1200, 60
rotate = 90, 30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_TOP_indA10
pos = 60, 1200, 120
rotate = 90, 30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_TOP_indA11
pos = -60, 1200, -120
rotate = 90, 30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_TOP_indA12
pos = -60, 1200, 120
rotate = 90, -30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_TOP_ctrl_twrB01
pos = 0, 1700, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_TOP_ctrl_twrB02
pos = 0, 1960, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_TOP_indB01
pos = 0, 1830, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_TOP_indB03
pos = -150, 1830, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_01

[Object]
nickname = up2_01_TOP_indB04
pos = 80, 1830, -140
rotate = 90, -30, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_01

[Object]
nickname = up2_01_TOP_indB06
pos = 80, 1830, 140
rotate = 90, 30, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_01

[Object]
nickname = up2_01_TOP_tube01
pos = 150, 1960, 0
rotate = -90, 0, 30
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_TOP_tube02
pos = 80, 1870, -140
rotate = -90, 0, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_TOP_tube03
pos = -70, 1900, -140
rotate = -90, 0, 20
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_TOP_tube04
pos = -70, 1870, 150
rotate = -90, 0, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_TOP_research01
pos = 80, 2700, -140
rotate = -90, 0, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_TOP_research02
pos = -320, 2700, -140
rotate = -90, 0, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_TOP_research03
pos = -215, 2700, 0
rotate = -90, 0, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_TOP_research04
pos = -70, 2700, 150
rotate = -90, 0, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_ctrl_twrA01
pos = 0, -1070, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_ctrl_twrA02
pos = 0, -1330, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA01
pos = 160, -1200, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA02
pos = -160, -1200, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA03
pos = 0, -1200, -160
rotate = 90, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA04
pos = 0, -1200, 160
rotate = 90, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA05
pos = 120, -1200, -60
rotate = 90, 30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA06
pos = 60, -1200, -120
rotate = 90, -30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA07
pos = -120, -1200, -60
rotate = 90, -30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA08
pos = 120, -1200, 60
rotate = 90, -30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA09
pos = -120, -1200, 60
rotate = 90, 30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA10
pos = 60, -1200, 120
rotate = 90, 30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA11
pos = -60, -1200, -120
rotate = 90, 30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indA12
pos = -60, -1200, 120
rotate = 90, -30, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_ctrl_twrB01
pos = 0, -1700, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_ctrl_twrB02
pos = 0, -1960, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indB01
pos = 0, -1830, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indB03
pos = -150, -1830, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indB04
pos = 80, -1830, -140
rotate = 90, -30, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_indB06
pos = 80, -1830, 140
rotate = 90, 30, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_tube01
pos = 150, -1960, 0
rotate = 90, 0, 30
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_tube02
pos = 80, -1870, -140
rotate = 90, 0, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_tube03
pos = -150, -1960, 0
rotate = 90, 0, -30
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_tube04
pos = -100, -1960, 130
rotate = 90, 0, 30
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_research01
pos = 80, -2700, -140
rotate = 90, 0, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_research02
pos = -515, -2700, 0
rotate = 90, 0, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_research03
pos = 515, -2700, 0
rotate = 90, 0, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_BOTTOM_research04
pos = 260, -2700, 150
rotate = 90, 0, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_CORE_XDETAIL_tube01
pos = 125, 0, -800
rotate = 0, 0, 90
archetype = space_tube_fix
parent = up2_01

[Object]
nickname = up2_01_CORE_XDETAIL_tube02
pos = -125, 0, -800
rotate = 0, 0, 90
archetype = space_tube_fix
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_tube01
pos = 0, -900, 0
rotate = -90, 0, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_tube02
pos = -150, -775, 780
rotate = -90, 0, 0
archetype = space_tube_fix
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_tube03
pos = -150, 1080, 80
rotate = 25, 0, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_tube04
pos = -150, -1080, 80
rotate = -25, 0, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_tube05
pos = -150, 1080, -80
rotate = 25, 180, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_tube06
pos = -150, -775, -780
rotate = -90, 0, 0
archetype = space_tube_fix
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_tube07
pos = -150, -1080, -80
rotate = -25, 180, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_tube08
pos = 150, -775, 780
rotate = -90, 0, 0
archetype = space_tube_fix
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_tube09
pos = 150, 1080, 100
rotate = 25, 0, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_tube10
pos = 150, -1080, 80
rotate = -25, 0, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_tube11
pos = 150, 1080, -80
rotate = 25, 180, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_tube12
pos = 150, -775, -780
rotate = -90, 0, 0
archetype = space_tube_fix
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_tube13
pos = 150, -1080, -80
rotate = -25, 180, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder01
pos = -150, -850, 0
rotate = 0, 90, -30
archetype = space_girder
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder02
pos = 150, -850, 0
rotate = 0, 90, 30
archetype = space_girder
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder03
pos = 0, -790, 0
rotate = 60, 0, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder04
pos = 0, -790, 0
rotate = 60, 180, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder05
pos = 0, -100, 0
rotate = 10, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder06
pos = 0, -100, 0
rotate = 10, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder07
pos = 0, 100, 0
rotate = -10, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder08
pos = 0, 100, 0
rotate = -10, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder09
pos = -150, 850, 0
rotate = 0, 90, 30
archetype = space_girder
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder10
pos = 150, 850, 0
rotate = 0, 90, -30
archetype = space_girder
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder11
pos = 0, 790, 0
rotate = -60, 0, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder12
pos = 0, 790, 0
rotate = -60, 180, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder13
pos = 350, -450, 0
rotate = 90, 0, 10
archetype = space_girder
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder14
pos = -350, -450, 0
rotate = 90, 0, -10
archetype = space_girder
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder15
pos = 350, 450, 0
rotate = 90, 0, -10
archetype = space_girder
parent = up2_01

[Object]
nickname = up2_01_CORE_DETAIL_girder16
pos = -350, 450, 0
rotate = 90, 0, 10
archetype = space_girder
parent = up2_01

[Object]
nickname = up2_01_LEFT_indA01
pos = -1350, 0, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_LEFT_indA02
pos = -1631, 0, 496
rotate = 0, -60, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_LEFT_indA03
pos = -2190, 0, 496
rotate = 0, -120, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_LEFT_indA04
pos = -2468, 0, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_LEFT_indA05
pos = -1631, 0, -496
rotate = 0, 240, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_LEFT_indA06
pos = -2190, 0, -494
rotate = 0, 120, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_LEFT_indA07
pos = -1920, 20, 0
rotate = -90, 45, 0
archetype = space_industrialc
parent = up2_01

[Object]
nickname = up2_01_LEFT_indA08
pos = -3050, -550, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_LEFT_tube01
pos = -600, 0, 90
rotate = 0, -90, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_LEFT_tube02
pos = -600, 0, -90
rotate = 0, -90, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_LEFT_tube03
pos = -2500, 0, -90
rotate = 45, -90, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_LEFT_tube04
pos = -2500, 0, 90
rotate = 45, -90, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_LEFT_tube05
pos = -3050, -610, 0
rotate = 45, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_tube06
pos = -3286, -910, 0
rotate = 0, -90, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_LEFT_tube07
pos = -3050, -853, 360
rotate = 0, -90, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_LEFT_tube08
pos = -3283, -550, -420
rotate = 0, -90, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder01
pos = -1348, 0, 132
rotate = 0, -30, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder02
pos = -1734, 0, 557
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder03
pos = -2470, 0, 132
rotate = 0, 30, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder04
pos = -1348, 0, -132
rotate = 0, 210, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder05
pos = -2470, 0, -132
rotate = 0, 150, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder06
pos = -1734, 0, -557
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder07
pos = -1400, 0, 0
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder08
pos = -1400, 0, 85
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder09
pos = -1400, 0, -85
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder10
pos = -2418, 0, 0
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder11
pos = -2418, 0, 85
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder12
pos = -2418, 0, -85
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder13
pos = -3046, -550, -120
rotate = 180, 45, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_girder14
pos = -3050, -548, 118
rotate = 45, 0, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr01
pos = -1920, 0, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr02
pos = -1920, 160, 0
rotate = 180, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr03
pos = -1920, 465, 0
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr04
pos = -1920, 765, 0
rotate = 180, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr05
pos = -1920, 940, 0
rotate = 0, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr06
pos = -1920, 1240, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr07
pos = -1920, 1550, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr08
pos = -1920, -160, 0
rotate = 0, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr09
pos = -1920, -465, 0
rotate = 180, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr10
pos = -1920, -765, 0
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr11
pos = -1920, -940, 0
rotate = 180, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr12
pos = -1920, -1240, 0
rotate = 180, 0, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_ctrl_twr13
pos = -1920, -1550, 0
rotate = 180, 90, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA01
pos = -1770, 80, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA02
pos = -2070, 80, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA03
pos = -1920, 80, -150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA04
pos = -1920, 80, 150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA05
pos = -2020, 80, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA06
pos = -1820, 80, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA07
pos = -1820, 80, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA08
pos = -2020, 80, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA09
pos = -1920, 245, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA10
pos = -1920, 245, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA11
pos = -1820, 245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA12
pos = -2020, 245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA13
pos = -1920, 245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA14
pos = -1920, 385, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA15
pos = -1920, 385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA16
pos = -1920, 385, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA17
pos = -1820, 385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA18
pos = -2020, 385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA19
pos = -1920, 545, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA20
pos = -1920, 545, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA21
pos = -1920, 545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA22
pos = -1820, 545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA23
pos = -2020, 545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA24
pos = -1920, 685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA25
pos = -1920, 685, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA26
pos = -1920, 685, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA27
pos = -1820, 685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA28
pos = -2020, 685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA29
pos = -1920, 855, -60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA30
pos = -1920, 855, 60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA31
pos = -1920, 855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA32
pos = -1860, 855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA33
pos = -1980, 855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA34
pos = -1920, 1020, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA35
pos = -1920, 1020, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA36
pos = -1880, 1020, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA37
pos = -1960, 1020, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA38
pos = -1920, 1160, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA39
pos = -1920, 1160, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA40
pos = -1880, 1160, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA41
pos = -1960, 1160, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA42
pos = -1960, 1320, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA43
pos = -1880, 1320, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA44
pos = -1920, 1320, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA45
pos = -1920, 1320, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA46
pos = -1880, 1520, 0
rotate = 0, 90, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA47
pos = -1960, 1520, 0
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA48
pos = -1920, 1520, -40
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA49
pos = -1920, 1520, 40
rotate = 0, 180, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatA50
pos = -1920, 1600, 0
rotate = 0, 0, 0
archetype = space_small_control_block
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB01
pos = -1770, -80, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB02
pos = -2070, -80, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB03
pos = -1920, -80, -150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB04
pos = -1920, -80, 150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB05
pos = -2020, -80, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB06
pos = -1820, -80, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB07
pos = -1820, -80, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB08
pos = -2020, -80, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB09
pos = -1920, -245, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB10
pos = -1920, -245, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB11
pos = -1820, -245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB12
pos = -2020, -245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB13
pos = -1920, -245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB14
pos = -1920, -385, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB15
pos = -1920, -385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB16
pos = -1920, -385, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB17
pos = -1820, -385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB18
pos = -2020, -385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB19
pos = -1920, -545, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB20
pos = -1920, -545, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB21
pos = -1920, -545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB22
pos = -1820, -545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB23
pos = -2020, -545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB24
pos = -1920, -685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB25
pos = -1920, -685, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB26
pos = -1920, -685, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB27
pos = -1820, -685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB28
pos = -2020, -685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB29
pos = -1920, -855, -60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB30
pos = -1920, -855, 60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB31
pos = -1920, -855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB32
pos = -1860, -855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB33
pos = -1980, -855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB34
pos = -1920, -1020, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB35
pos = -1920, -1020, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB36
pos = -1880, -1020, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB37
pos = -1960, -1020, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB38
pos = -1920, -1160, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB39
pos = -1920, -1160, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB40
pos = -1880, -1160, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB41
pos = -1960, -1160, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB42
pos = -1960, -1320, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB43
pos = -1880, -1320, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB44
pos = -1920, -1320, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB45
pos = -1920, -1320, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB46
pos = -1880, -1520, 0
rotate = 180, 90, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB47
pos = -1960, -1520, 0
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB48
pos = -1920, -1520, -40
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB49
pos = -1920, -1520, 40
rotate = 180, 180, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatB50
pos = -1920, -1600, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatC01
pos = -1680, 0, 410
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatC02
pos = -1582, 0, 580
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatC03
pos = -1680, 0, -410
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatC04
pos = -1582, 0, -580
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatC05
pos = -2141, 0, 410
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatC06
pos = -2237, 0, 580
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatC07
pos = -2141, 0, -410
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_habitatC08
pos = -2237, 0, -578
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_LEFT_dome01
pos = -1631, 90, 496
rotate = 0, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_LEFT_dome02
pos = -1631, -90, 496
rotate = 180, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_LEFT_dome03
pos = -2190, 90, 496
rotate = 0, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_LEFT_dome04
pos = -2190, -90, 496
rotate = 180, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_LEFT_dome05
pos = -1631, 90, -496
rotate = 0, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_LEFT_dome06
pos = -1631, -90, -496
rotate = 180, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_LEFT_dome07
pos = -2190, 90, -494
rotate = 0, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_LEFT_dome08
pos = -2190, -90, -494
rotate = 180, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_RIGHT_indA01
pos = 1350, 0, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_RIGHT_indA02
pos = 1631, 0, 496
rotate = 0, 60, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_RIGHT_indA03
pos = 2190, 0, 496
rotate = 0, 120, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_RIGHT_indA04
pos = 2468, 0, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_RIGHT_indA05
pos = 1631, 0, -496
rotate = 0, -240, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_RIGHT_indA06
pos = 2190, 0, -494
rotate = 0, -120, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_RIGHT_indA07
pos = 1920, 20, 0
rotate = -90, 45, 0
archetype = space_industrialc
parent = up2_01

[Object]
nickname = up2_01_RIGHT_indA08
pos = 3050, 540, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_RIGHT_tube01
pos = 600, 0, 90
rotate = 0, 90, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_RIGHT_tube02
pos = 600, 0, -90
rotate = 0, 90, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_RIGHT_tube03
pos = 2500, 0, -90
rotate = -45, 90, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_RIGHT_tube04
pos = 2500, 0, 90
rotate = -45, 90, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_RIGHT_tube06
pos = 3285, 540, -420
rotate = 0, 90, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_RIGHT_tube07
pos = 3285, 540, 420
rotate = 0, 90, 0
archetype = space_research
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder01
pos = 1348, 0, 132
rotate = 0, 30, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder02
pos = 1734, 0, 557
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder03
pos = 2470, 0, 132
rotate = 0, -30, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder04
pos = 1348, 0, -132
rotate = 0, -210, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder05
pos = 2470, 0, -132
rotate = 0, -150, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder06
pos = 1734, 0, -557
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder07
pos = 1400, 0, 0
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder08
pos = 1400, 0, 85
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder09
pos = 1400, 0, -85
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder10
pos = 2418, 0, 0
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder11
pos = 2418, 0, 85
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder12
pos = 2418, 0, -85
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder13
pos = 3047, 540, -120
rotate = 180, -45, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_girder14
pos = 3047, 540, 120
rotate = 0, 45, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr01
pos = 1920, 0, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr02
pos = 1920, 160, 0
rotate = 180, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr03
pos = 1920, 465, 0
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr04
pos = 1920, 765, 0
rotate = 180, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr05
pos = 1920, 940, 0
rotate = 0, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr06
pos = 1920, 1240, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr07
pos = 1920, 1550, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr08
pos = 1920, -160, 0
rotate = 0, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr09
pos = 1920, -465, 0
rotate = 180, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr10
pos = 1920, -765, 0
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr11
pos = 1920, -940, 0
rotate = 180, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr12
pos = 1920, -1240, 0
rotate = 180, 0, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_ctrl_twr13
pos = 1920, -1550, 0
rotate = 180, 90, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA01
pos = 1770, 80, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA02
pos = 2070, 80, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA03
pos = 1920, 80, -150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA04
pos = 1920, 80, 150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA05
pos = 2020, 80, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA06
pos = 1820, 80, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA07
pos = 1820, 80, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA08
pos = 2020, 80, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA09
pos = 1920, 245, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA10
pos = 1920, 245, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA11
pos = 1820, 245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA12
pos = 2020, 245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA13
pos = 1920, 245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA14
pos = 1920, 385, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA15
pos = 1920, 385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA16
pos = 1920, 385, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA17
pos = 1820, 385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA18
pos = 2020, 385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA19
pos = 1920, 545, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA20
pos = 1920, 545, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA21
pos = 1920, 545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA22
pos = 1820, 545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA23
pos = 2020, 545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA24
pos = 1920, 685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA25
pos = 1920, 685, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA26
pos = 1920, 685, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA27
pos = 1820, 685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA28
pos = 2020, 685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA29
pos = 1920, 855, -60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA30
pos = 1920, 855, 60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA31
pos = 1920, 855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA32
pos = 1860, 855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA33
pos = 1980, 855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA34
pos = 1920, 1020, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA35
pos = 1920, 1020, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA36
pos = 1880, 1020, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA37
pos = 1960, 1020, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA38
pos = 1920, 1160, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA39
pos = 1920, 1160, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA40
pos = 1880, 1160, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA41
pos = 1960, 1160, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA42
pos = 1960, 1320, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA43
pos = 1880, 1320, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA44
pos = 1920, 1320, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA45
pos = 1920, 1320, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA46
pos = 1880, 1520, 0
rotate = 0, 90, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA47
pos = 1960, 1520, 0
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA48
pos = 1920, 1520, -40
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA49
pos = 1920, 1520, 40
rotate = 0, 180, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatA50
pos = 1920, 1600, 0
rotate = 0, 0, 0
archetype = space_small_control_block
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB01
pos = 1770, -80, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB02
pos = 2070, -80, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB03
pos = 1920, -80, -150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB04
pos = 1920, -80, 150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB05
pos = 2020, -80, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB06
pos = 1820, -80, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB07
pos = 1820, -80, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB08
pos = 2020, -80, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB09
pos = 1920, -245, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB10
pos = 1920, -245, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB11
pos = 1820, -245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB12
pos = 2020, -245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB13
pos = 1920, -245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB14
pos = 1920, -385, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB15
pos = 1920, -385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB16
pos = 1920, -385, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB17
pos = 1820, -385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB18
pos = 2020, -385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB19
pos = 1920, -545, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB20
pos = 1920, -545, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB21
pos = 1920, -545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB22
pos = 1820, -545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB23
pos = 2020, -545, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB24
pos = 1920, -685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB25
pos = 1920, -685, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB26
pos = 1920, -685, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB27
pos = 1820, -685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB28
pos = 2020, -685, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB29
pos = 1920, -855, -60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB30
pos = 1920, -855, 60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB31
pos = 1920, -855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB32
pos = 1860, -855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB33
pos = 1980, -855, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB34
pos = 1920, -1020, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB35
pos = 1920, -1020, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB36
pos = 1880, -1020, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB37
pos = 1960, -1020, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB38
pos = 1920, -1160, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB39
pos = 1920, -1160, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB40
pos = 1880, -1160, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB41
pos = 1960, -1160, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB42
pos = 1960, -1320, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB43
pos = 1880, -1320, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB44
pos = 1920, -1320, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB45
pos = 1920, -1320, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB46
pos = 1880, -1520, 0
rotate = 180, 90, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB47
pos = 1960, -1520, 0
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB48
pos = 1920, -1520, -40
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB49
pos = 1920, -1520, 40
rotate = 180, 180, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatB50
pos = 1920, -1600, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatC01
pos = 1680, 0, 410
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatC02
pos = 1582, 0, 580
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatC03
pos = 1680, 0, -410
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatC04
pos = 1582, 0, -580
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatC05
pos = 2141, 0, 410
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatC06
pos = 2237, 0, 580
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatC07
pos = 2141, 0, -410
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_habitatC08
pos = 2237, 0, -578
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_RIGHT_dome01
pos = 1631, 90, 496
rotate = 0, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_RIGHT_dome02
pos = 1631, -90, 496
rotate = 180, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_RIGHT_dome03
pos = 2190, 90, 496
rotate = 0, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_RIGHT_dome04
pos = 2190, -90, 496
rotate = 180, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_RIGHT_dome05
pos = 1631, 90, -496
rotate = 0, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_RIGHT_dome06
pos = 1631, -90, -496
rotate = 180, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_RIGHT_dome07
pos = 2190, 90, -494
rotate = 0, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_RIGHT_dome08
pos = 2190, -90, -494
rotate = 180, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_SIDES_ind01
pos = 125, 0, 780
rotate = 0, 90, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_SIDES_ind02
pos = -125, 0, 780
rotate = 0, 90, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_SIDES_ind03
pos = -125, 0, -780
rotate = 0, 90, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_SIDES_ind04
pos = 125, 0, -780
rotate = 0, 90, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_SIDES_ind05
pos = 0, 0, 1500
rotate = 0, 90, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_SIDES_ind06
pos = 0, 0, -1500
rotate = 0, 90, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_SIDES_tube01
pos = 80, 0, 750
rotate = 0, 0, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_SIDES_tube02
pos = -80, 0, 750
rotate = 0, 0, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_SIDES_tube03
pos = 80, 0, -780
rotate = 0, 180, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_SIDES_tube04
pos = -80, 0, -780
rotate = 0, 180, 0
archetype = space_short_tube
parent = up2_01

[Object]
nickname = up2_01_SIDES_gird01
pos = 0, 0, 1560
rotate = 0, 0, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_SIDES_gird02
pos = -80, 0, 1550
rotate = 0, 0, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_SIDES_gird03
pos = 80, 0, 1550
rotate = 0, 0, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_SIDES_gird05
pos = 0, 0, -1550
rotate = 0, 180, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_SIDES_gird06
pos = -80, 0, -1550
rotate = 0, 180, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_SIDES_gird07
pos = 80, 0, -1550
rotate = 0, 180, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_FRONT_indA01
pos = 570, 0, 2060
rotate = 0, 0, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_FRONT_indA02
pos = 289, 0, 2556
rotate = 0, -60, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_FRONT_indA03
pos = -270, 0, 2556
rotate = 0, -120, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_FRONT_indA04
pos = -548, 0, 2060
rotate = 0, 0, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_FRONT_indA05
pos = 289, 0, 1564
rotate = 0, 240, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_FRONT_indA06
pos = -270, 0, 1566
rotate = 0, 120, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_FRONT_indA07
pos = 0, 20, 2060
rotate = -90, 45, 0
archetype = space_industrialc
parent = up2_01

[Object]
nickname = up2_01_FRONT_girder01
pos = 572, 0, 2192
rotate = 0, -30, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_FRONT_girder02
pos = 186, 0, 2617
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_FRONT_girder03
pos = -550, 0, 2192
rotate = 0, 30, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_FRONT_girder04
pos = 572, 0, 1928
rotate = 0, 210, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_FRONT_girder05
pos = -550, 0, 1928
rotate = 0, 150, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_FRONT_girder06
pos = 186, 0, 1503
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_FRONT_girder07
pos = 520, 0, 2060
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_FRONT_girder08
pos = 520, 0, 2145
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_FRONT_girder09
pos = 520, 0, 1975
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_FRONT_girder10
pos = -498, 0, 2060
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_FRONT_girder11
pos = -498, 0, 2145
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_FRONT_girder12
pos = -498, 0, 1975
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_FRONT_ctrl_twr01
pos = 0, 0, 2060
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_FRONT_ctrl_twr02
pos = 0, 160, 2060
rotate = 180, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_FRONT_ctrl_twr03
pos = 0, 465, 2060
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_FRONT_ctrl_twr04
pos = 0, 765, 2060
rotate = 180, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_FRONT_ctrl_twr05
pos = 0, 940, 2060
rotate = 0, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_FRONT_ctrl_twr06
pos = 0, 1240, 2060
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_FRONT_ctrl_twr07
pos = 0, 1550, 2060
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_FRONT_ctrl_twr08
pos = 0, -160, 2060
rotate = 0, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_FRONT_ctrl_twr09
pos = 0, -465, 2060
rotate = 180, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_FRONT_ctrl_twr10
pos = 0, -765, 2060
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_FRONT_ctrl_twr11
pos = 0, -940, 2060
rotate = 180, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_FRONT_ctrl_twr12
pos = 0, -1240, 2060
rotate = 180, 0, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_FRONT_ctrl_twr13
pos = 0, -1550, 2060
rotate = 180, 90, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA01
pos = 150, 80, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA02
pos = -150, 80, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA03
pos = 0, 80, 1910
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA04
pos = 0, 80, 2210
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA05
pos = -100, 80, 1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA06
pos = 100, 80, 1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA07
pos = 100, 80, 2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA08
pos = -100, 80, 2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA09
pos = 0, 245, 1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA10
pos = 0, 245, 2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA11
pos = 100, 245, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA12
pos = -100, 245, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA13
pos = 0, 245, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA14
pos = 0, 385, 2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA15
pos = 0, 385, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA16
pos = 0, 385, 1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA17
pos = 100, 385, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA18
pos = -100, 385, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA19
pos = 0, 545, 1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA20
pos = 0, 545, 2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA21
pos = 0, 545, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA22
pos = 100, 545, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA23
pos = -100, 545, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA24
pos = 0, 685, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA25
pos = 0, 685, 2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA26
pos = 0, 685, 1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA27
pos = 100, 685, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA28
pos = -100, 685, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA29
pos = 0, 855, 2000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA30
pos = 0, 855, 2120
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA31
pos = 0, 855, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA32
pos = 60, 855, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA33
pos = -60, 855, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA34
pos = 0, 1020, 2020
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA35
pos = 0, 1020, 2100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA36
pos = 40, 1020, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA37
pos = -40, 1020, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA38
pos = 0, 1160, 2020
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA39
pos = 0, 1160, 2100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA40
pos = 40, 1160, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA41
pos = -40, 1160, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA42
pos = -40, 1320, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA43
pos = 40, 1320, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA44
pos = 0, 1320, 2020
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA45
pos = 0, 1320, 2100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA46
pos = 40, 1520, 2060
rotate = 0, 90, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA47
pos = -40, 1520, 2060
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA48
pos = 0, 1520, 2020
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA49
pos = 0, 1520, 2100
rotate = 0, 180, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatA50
pos = 0, 1600, 2060
rotate = 0, 0, 0
archetype = space_small_control_block
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB01
pos = 150, -80, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB02
pos = -150, -80, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB03
pos = 0, -80, 1910
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB04
pos = 0, -80, 2210
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB05
pos = -100, -80, 1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB06
pos = 100, -80, 1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB07
pos = 100, -80, 2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB08
pos = -100, -80, 2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB09
pos = 0, -245, 1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB10
pos = 0, -245, 2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB11
pos = 100, -245, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB12
pos = -100, -245, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB13
pos = 0, -245, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB14
pos = 0, -385, 2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB15
pos = 0, -385, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB16
pos = 0, -385, 1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB17
pos = 100, -385, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB18
pos = -100, -385, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB19
pos = 0, -545, 1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB20
pos = 0, -545, 2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB21
pos = 0, -545, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB22
pos = 100, -545, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB23
pos = -100, -545, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB24
pos = 0, -685, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB25
pos = 0, -685, 2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB26
pos = 0, -685, 1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB27
pos = 100, -685, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB28
pos = -100, -685, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB29
pos = 0, -855, 2000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB30
pos = 0, -855, 2120
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB31
pos = 0, -855, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB32
pos = 60, -855, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB33
pos = -60, -855, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB34
pos = 0, -1020, 2020
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB35
pos = 0, -1020, 2100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB36
pos = 40, -1020, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB37
pos = -40, -1020, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB38
pos = 0, -1160, 2020
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB39
pos = 0, -1160, 2100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB40
pos = 40, -1160, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB41
pos = -40, -1160, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB42
pos = -40, -1320, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB43
pos = 40, -1320, 2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB44
pos = 0, -1320, 2020
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB45
pos = 0, -1320, 2100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB46
pos = 40, -1520, 2060
rotate = 180, 90, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB47
pos = -40, -1520, 2060
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB48
pos = 0, -1520, 2020
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB49
pos = 0, -1520, 2100
rotate = 180, 180, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatB50
pos = 0, -1600, 2060
rotate = 180, 0, 0
archetype = space_small_control_block
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatC01
pos = 240, 0, 2470
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatC02
pos = 338, 0, 2640
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatC03
pos = 240, 0, 1650
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatC04
pos = 338, 0, 1480
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatC05
pos = -221, 0, 2470
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatC06
pos = -317, 0, 2640
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatC07
pos = -221, 0, 1650
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_habitatC08
pos = -317, 0, 1482
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_FRONT_dome01
pos = 289, 90, 2556
rotate = 0, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_FRONT_dome02
pos = 289, -90, 2556
rotate = 180, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_FRONT_dome03
pos = -270, 90, 2556
rotate = 0, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_FRONT_dome04
pos = -270, -90, 2556
rotate = 180, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_FRONT_dome05
pos = 289, 90, 1564
rotate = 0, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_FRONT_dome06
pos = 289, -90, 1564
rotate = 180, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_FRONT_dome07
pos = -270, 90, 1566
rotate = 0, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_FRONT_dome08
pos = -270, -90, 1566
rotate = 180, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_BACK_indA01
pos = 570, 0, -2060
rotate = 0, 0, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_BACK_indA02
pos = 289, 0, -1564
rotate = 0, -60, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_BACK_indA03
pos = -270, 0, -1564
rotate = 0, -120, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_BACK_indA04
pos = -548, 0, -2060
rotate = 0, 0, 0
archetype = space_industrial02a
parent = up2_01

[Object]
nickname = up2_01_BACK_indA05
pos = 289, 0, -2556
rotate = 0, 240, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_BACK_indA06
pos = -270, 0, -2554
rotate = 0, 120, 0
archetype = space_industriala
parent = up2_01

[Object]
nickname = up2_01_BACK_indA07
pos = 0, 20, -2060
rotate = -90, 45, 0
archetype = space_industrialc
parent = up2_01

[Object]
nickname = up2_01_BACK_girder01
pos = 572, 0, -1928
rotate = 0, -30, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_BACK_girder02
pos = 186, 0, -1503
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_BACK_girder03
pos = -550, 0, -1928
rotate = 0, 30, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_BACK_girder04
pos = 572, 0, -2192
rotate = 0, 210, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_BACK_girder05
pos = -550, 0, -2192
rotate = 0, 150, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_BACK_girder06
pos = 186, 0, -2617
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_BACK_girder07
pos = 520, 0, -2060
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_BACK_girder08
pos = 520, 0, -1975
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_BACK_girder09
pos = 520, 0, -2145
rotate = 0, -90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_BACK_girder10
pos = -498, 0, -2060
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_BACK_girder11
pos = -498, 0, -1975
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_BACK_girder12
pos = -498, 0, -2145
rotate = 0, 90, 0
archetype = space_girdera
parent = up2_01

[Object]
nickname = up2_01_BACK_ctrl_twr01
pos = 0, 0, -2060
rotate = 0, 0, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_BACK_ctrl_twr02
pos = 0, 160, -2060
rotate = 180, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_BACK_ctrl_twr03
pos = 0, 465, -2060
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_BACK_ctrl_twr04
pos = 0, 765, -2060
rotate = 180, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_BACK_ctrl_twr05
pos = 0, 940, -2060
rotate = 0, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_BACK_ctrl_twr06
pos = 0, 1240, -2060
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_BACK_ctrl_twr07
pos = 0, 1550, -2060
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_BACK_ctrl_twr08
pos = 0, -160, -2060
rotate = 0, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_BACK_ctrl_twr09
pos = 0, -465, -2060
rotate = 180, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_BACK_ctrl_twr10
pos = 0, -765, -2060
rotate = 0, 45, 0
archetype = space_medium_control_tower
parent = up2_01

[Object]
nickname = up2_01_BACK_ctrl_twr11
pos = 0, -940, -2060
rotate = 180, 45, 0
archetype = space_control_tower
parent = up2_01

[Object]
nickname = up2_01_BACK_ctrl_twr12
pos = 0, -1240, -2060
rotate = 180, 0, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_BACK_ctrl_twr13
pos = 0, -1550, -2060
rotate = 180, 90, 0
archetype = space_small_control_tower
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA01
pos = 150, 80, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA02
pos = -150, 80, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA03
pos = 0, 80, -2210
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA04
pos = 0, 80, -1910
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA05
pos = -100, 80, -2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA06
pos = 100, 80, -2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA07
pos = 100, 80, -1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA08
pos = -100, 80, -1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA09
pos = 0, 245, -2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA10
pos = 0, 245, -1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA11
pos = 100, 245, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA12
pos = -100, 245, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA13
pos = 0, 245, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA14
pos = 0, 385, -1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA15
pos = 0, 385, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA16
pos = 0, 385, -2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA17
pos = 100, 385, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA18
pos = -100, 385, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA19
pos = 0, 545, -2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA20
pos = 0, 545, -1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA21
pos = 0, 545, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA22
pos = 100, 545, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA23
pos = -100, 545, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA24
pos = 0, 685, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA25
pos = 0, 685, -1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA26
pos = 0, 685, -2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA27
pos = 100, 685, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA28
pos = -100, 685, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA29
pos = 0, 855, -2120
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA30
pos = 0, 855, -2000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA31
pos = 0, 855, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA32
pos = 60, 855, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA33
pos = -60, 855, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA34
pos = 0, 1020, -2100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA35
pos = 0, 1020, -2020
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA36
pos = 40, 1020, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA37
pos = -40, 1020, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA38
pos = 0, 1160, -2100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA39
pos = 0, 1160, -2020
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA40
pos = 40, 1160, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA41
pos = -40, 1160, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA42
pos = -40, 1320, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA43
pos = 40, 1320, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA44
pos = 0, 1320, -2100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA45
pos = 0, 1320, -2020
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA46
pos = 40, 1520, -2060
rotate = 0, 90, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA47
pos = -40, 1520, -2060
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA48
pos = 0, 1520, -2100
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA49
pos = 0, 1520, -2020
rotate = 0, 180, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatA50
pos = 0, 1600, -2060
rotate = 0, 0, 0
archetype = space_small_control_block
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB01
pos = 150, -80, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB02
pos = -150, -80, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB03
pos = 0, -80, -2210
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB04
pos = 0, -80, -1910
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB05
pos = -100, -80, -2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB06
pos = 100, -80, -2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB07
pos = 100, -80, -1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB08
pos = -100, -80, -1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB09
pos = 0, -245, -2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB10
pos = 0, -245, -1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB11
pos = 100, -245, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB12
pos = -100, -245, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB13
pos = 0, -245, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB14
pos = 0, -385, -1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB15
pos = 0, -385, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB16
pos = 0, -385, -2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB17
pos = 100, -385, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB18
pos = -100, -385, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB19
pos = 0, -545, -2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB20
pos = 0, -545, -1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB21
pos = 0, -545, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB22
pos = 100, -545, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB23
pos = -100, -545, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB24
pos = 0, -685, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB25
pos = 0, -685, -1960
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB26
pos = 0, -685, -2160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB27
pos = 100, -685, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB28
pos = -100, -685, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB29
pos = 0, -855, -2120
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB30
pos = 0, -855, -2000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB31
pos = 0, -855, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB32
pos = 60, -855, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB33
pos = -60, -855, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB34
pos = 0, -1020, -2100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB35
pos = 0, -1020, -2020
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB36
pos = 40, -1020, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB37
pos = -40, -1020, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB38
pos = 0, -1160, -2100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB39
pos = 0, -1160, -2020
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB40
pos = 40, -1160, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB41
pos = -40, -1160, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB42
pos = -40, -1320, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB43
pos = 40, -1320, -2060
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB44
pos = 0, -1320, -2100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB45
pos = 0, -1320, -2020
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB46
pos = 40, -1520, -2060
rotate = 180, 90, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB47
pos = -40, -1520, -2060
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB48
pos = 0, -1520, -2100
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB49
pos = 0, -1520, -2020
rotate = 180, 180, 0
archetype = space_habitat_tall
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatB50
pos = 0, -1600, -2060
rotate = 180, 0, 0
archetype = space_small_control_block
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatC01
pos = 240, 0, -1650
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatC02
pos = 338, 0, -1480
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatC03
pos = 240, 0, -2470
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatC04
pos = 338, 0, -2640
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatC05
pos = -221, 0, -1650
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatC06
pos = -317, 0, -1480
rotate = 0, 60, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatC07
pos = -221, 0, -2470
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_habitatC08
pos = -317, 0, -2638
rotate = 0, 30, 0
archetype = space_habitat_wide
parent = up2_01

[Object]
nickname = up2_01_BACK_dome01
pos = 289, 90, -1564
rotate = 0, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_BACK_dome02
pos = 289, -90, -1564
rotate = 180, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_BACK_dome03
pos = -270, 90, -1564
rotate = 0, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_BACK_dome04
pos = -270, -90, -1564
rotate = 180, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_BACK_dome05
pos = 289, 90, -2556
rotate = 0, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_BACK_dome06
pos = 289, -90, -2556
rotate = 180, -30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_BACK_dome07
pos = -270, 90, -2554
rotate = 0, 30, 0
archetype = space_domea
parent = up2_01

[Object]
nickname = up2_01_BACK_dome08
pos = -270, -90, -2554
rotate = 180, 30, 0
archetype = space_domea
parent = up2_01
'''
