from templates.space_object_template import SpaceObjectTemplate


class CambridgeResearch(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'br_cam_04'
    TEMPLATE = '''[Object]
nickname = br_cam_04
ids_name = 203614
pos = 0, 0, -1180
rotate = 0, 90, 0
archetype = cambridge_core
ids_info = 065550
base = br_cam_04_base
reputation = br_grp
behavior = NOTHING

[Object]
nickname = br_cam_04_dock
ids_name = 208608
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_shipping01
ids_info = 065642
base = br_cam_04_base
dock_with = br_cam_04_base
reputation = br_grp
behavior = NOTHING
voice = atc_leg_f01
space_costume = br_karina_head_gen, sc_female1_body
loadout = br_space_police01

[Object]
nickname = br_cam_04_PAD_ctrl_twr01
pos = 0, 0, -1180
rotate = 180, 0, 0
archetype = space_control_tower
parent = br_cam_04

[Object]
nickname = br_cam_04_PAD_ctrl_twr02
pos = 0, 0, -730
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = br_cam_04

[Object]
nickname = br_cam_04_PAD_ctrl_twr03
pos = -210, 0, -790
rotate = 0, -30, 0
archetype = space_small_control_tower
parent = br_cam_04

[Object]
nickname = br_cam_04_PAD_ctrl_twr04
pos = 210, 0, -790
rotate = 0, 30, 0
archetype = space_small_control_tower
parent = br_cam_04

[Object]
nickname = br_cam_04_PAD_airlock01
pos = 0, 100, -1180
rotate = 90, 0, 0
archetype = space_airlock_dummy
parent = br_cam_04

[Object]
nickname = br_cam_04_PAD_airlock02
pos = 0, -100, -1180
rotate = -90, 0, 0
archetype = space_airlock_dummy
parent = br_cam_04

[Object]
nickname = br_cam_04_PAD_industrial01
pos = 0, 0, -930
rotate = 0, 0, 0
archetype = space_industriala
parent = br_cam_04

[Object]
nickname = br_cam_04_PAD_industrial02
pos = 0, 0, -1430
rotate = 0, 0, 0
archetype = space_industriala
parent = br_cam_04

[Object]
nickname = br_cam_04_PAD_industrial03
pos = -110, 0, -960
rotate = 0, -30, 0
archetype = space_industriala
parent = br_cam_04

[Object]
nickname = br_cam_04_PAD_industrial04
pos = 110, 0, -960
rotate = 0, 30, 0
archetype = space_industriala
parent = br_cam_04

[Object]
nickname = br_cam_04_PAD_industrial05
pos = -110, 0, -1400
rotate = 0, 30, 0
archetype = space_industriala
parent = br_cam_04

[Object]
nickname = br_cam_04_PAD_industrial06
pos = 110, 0, -1400
rotate = 0, -30, 0
archetype = space_industriala
parent = br_cam_04

[Object]
nickname = br_cam_04_PAD_industrial07
pos = 0, 0, -1665
rotate = 0, 0, 0
archetype = space_industriala
parent = br_cam_04

[Object]
nickname = br_cam_04_PAD_industrial08
pos = 0, 0, -1900
rotate = 0, 0, 0
archetype = space_industriala
parent = br_cam_04

[Object]
nickname = br_cam_04_PAD_industrial08
pos = 0, 0, -2135
rotate = 0, 0, 0
archetype = space_industriala
parent = br_cam_04

[Object]
nickname = br_cam_04_PAD_dome01
pos = -320, 30, -1760
rotate = 0, 30, 0
archetype = space_dome
parent = br_cam_04

[Object]
nickname = br_cam_04_PAD_dome02
pos = 320, 30, -1760
rotate = 0, -30, 0
archetype = space_dome
parent = br_cam_04

[Object]
nickname = br_cam_04_PAD_dome03
pos = -200, 30, -2150
rotate = 0, 30, 0
archetype = space_dome
parent = br_cam_04

[Object]
nickname = br_cam_04_PAD_dome04
pos = 200, 30, -2150
rotate = 0, -30, 0
archetype = space_dome
parent = br_cam_04

[Object]
nickname = br_cam_04_PAD_dome05
pos = 0, 30, -2550
rotate = 0, 0, 0
archetype = space_dome
parent = br_cam_04



[Object]
nickname = br_cam_04_BTM_industrial01
pos = 0, -250, -1180
rotate = 90, 0, 0
archetype = space_industriala
parent = br_cam_04

[Object]
nickname = br_cam_04_BTM_industrial02
pos = 0, -150, -1010
rotate = 0, 0, 90
archetype = space_industrial02d
parent = br_cam_04

[Object]
nickname = br_cam_04_BTM_industrial03
pos = 0, -150, -1350
rotate = 0, 0, 90
archetype = space_industrial02d
parent = br_cam_04

[Object]
nickname = br_cam_04_BTM_industrial04
pos = 0, -150, -855
rotate = 0, 180, 0
archetype = space_industrial02b
parent = br_cam_04

[Object]
nickname = br_cam_04_BTM_industrial05
pos = 0, -150, -1505
rotate = 0, 180, 0
archetype = space_industrial02b
parent = br_cam_04

[Object]
nickname = br_cam_04_BTM_tank_01
pos = 0, -150, -680
rotate = 0, 0, 0
archetype = space_tankl4
parent = br_cam_04

[Object]
nickname = br_cam_04_BTM_tank_02
pos = 0, -250, -980
rotate = 0, 0, 0
archetype = space_tankl4
parent = br_cam_04

[Object]
nickname = br_cam_04_BTM_tank_03
pos = 0, -150, -1680
rotate = 0, 0, 0
archetype = space_tankl4
parent = br_cam_04

[Object]
nickname = br_cam_04_BTM_tank_04
pos = 0, -250, -1380
rotate = 0, 0, 0
archetype = space_tankl4
parent = br_cam_04

[Object]
nickname = br_cam_04_BTM_tank_05
pos = 0, -455, -1180
rotate = 0, 0, 0
archetype = space_tankl2
parent = br_cam_04



[Object]
nickname = br_cam_04_TREE_industrial01
pos = 0, 500, -1180
rotate = 90, 0, 0
archetype = space_industriala
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial02
pos = 0, 750, -1180
rotate = 90, 0, 0
archetype = space_industriala
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial03
pos = 0, 1005, -1180
rotate = -90, 0, 0
archetype = space_industriala
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial04
pos = -175, 790, -1180
rotate = 0, 0, 60
archetype = space_industrial02d
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial05
pos = 175, 790, -1180
rotate = 0, 0, -60
archetype = space_industrial02d
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial06
pos = -315, 550, -1180
rotate = 0, 0, 60
archetype = space_industrial02d
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial07
pos = 315, 550, -1180
rotate = 0, 0, -60
archetype = space_industrial02d
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial08
pos = 0, 790, -1005
rotate = 90, 30, 90
archetype = space_industrial02d
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial09
pos = 0, 790, -1355
rotate = 90, -30, 90
archetype = space_industrial02d
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial10
pos = 0, 550, -865
rotate = 90, 30, 90
archetype = space_industrial02d
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial11
pos = 0, 550, -1495
rotate = 90, -30, 90
archetype = space_industrial02d
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial12
pos = 0, 250, -1180
rotate = 90, 0, 0
archetype = space_industriala
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial13
pos = -450, 250, -1180
rotate = 0, 0, 0
archetype = space_industrial02a
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial14
pos = 450, 250, -1180
rotate = 0, 0, 0
archetype = space_industrial02a
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial15
pos = 0, 250, -730
rotate = 0, 90, 0
archetype = space_industrial02a
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial16
pos = 0, 250, -1630
rotate = 0, 90, 0
archetype = space_industrial02a
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial17
pos = 320, 250, -860
rotate = 0, -45, 0
archetype = space_industrial02a
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial18
pos = -320, 250, -860
rotate = 0, 45, 0
archetype = space_industrial02a
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial19
pos = 320, 250, -1500
rotate = 0, 45, 0
archetype = space_industrial02a
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial20
pos = -320, 250, -1500
rotate = 0, -45, 0
archetype = space_industrial02a
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial21
pos = -120, 250, -1060
rotate = 0, -45, 0
archetype = space_industriala
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial22
pos = -120, 250, -1300
rotate = 0, 45, 0
archetype = space_industriala
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial23
pos = 120, 250, -1060
rotate = 0, 45, 0
archetype = space_industriala
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial24
pos = 120, 250, -1300
rotate = 0, -45, 0
archetype = space_industriala
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial25
pos = -410, 250, -1355
rotate = 0, -22.5, 0
archetype = space_industrial01d
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial26
pos = -410, 250, -1005
rotate = 0, 22.5, 0
archetype = space_industrial01d
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial27
pos = 410, 250, -1355
rotate = 0, 22.5, 0
archetype = space_industrial01d
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial28
pos = 410, 250, -1005
rotate = 0, -22.5, 0
archetype = space_industrial01d
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial29
pos = 175, 250, -770
rotate = 0, -67.5, 0
archetype = space_industrial01d
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial30
pos = 175, 250, -1590
rotate = 0, 67.5, 0
archetype = space_industrial01d
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial31
pos = -175, 250, -770
rotate = 0, 67.5, 0
archetype = space_industrial01d
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_industrial32
pos = -175, 250, -1590
rotate = 0, -67.5, 0
archetype = space_industrial01d
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder01
pos = -25, 1050, -1180
rotate = 60, -90, 0
archetype = space_girdera
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder02
pos = 25, 1050, -1180
rotate = 60, 90, 0
archetype = space_girdera
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder03
pos = -160, 820, -1180
rotate = 60, -90, 0
archetype = space_girdera
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder04
pos = 160, 820, -1180
rotate = 60, 90, 0
archetype = space_girdera
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder05
pos = 100, 755, -1180
rotate = -10, 90, 0
archetype = space_girderc
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder06
pos = -100, 755, -1180
rotate = 10, 90, 0
archetype = space_girderc
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder07
pos = 150, 508, -1180
rotate = -5, 90, 0
archetype = space_girder
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder08
pos = -150, 508, -1180
rotate = 5, 90, 0
archetype = space_girder
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder09
pos = 0, 1050, -1155
rotate = 60, 0, 0
archetype = space_girdera
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder10
pos = 0, 1050, -1205
rotate = 60, 180, 0
archetype = space_girdera
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder11
pos = 0, 820, -1020
rotate = 60, 0, 0
archetype = space_girdera
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder12
pos = 0, 820, -1340
rotate = 60, 180, 0
archetype = space_girdera
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder13
pos = 0, 755, -1280
rotate = -10, 180, 0
archetype = space_girderc
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder14
pos = 0, 755, -1080
rotate = 10, 180, 0
archetype = space_girderc
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder15
pos = 0, 508, -1330
rotate = -5, 180, 0
archetype = space_girder
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder16
pos = 0, 508, -1030
rotate = 5, 180, 0
archetype = space_girder
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder17
pos = 310, 550, -1180
rotate = 60, 90, 0
archetype = space_girdera
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder18
pos = -310, 550, -1180
rotate = 60, -90, 0
archetype = space_girdera
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder19
pos = 0, 550, -1490
rotate = 60, 180, 0
archetype = space_girdera
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder20
pos = 0, 550, -870
rotate = 60, 0, 0
archetype = space_girdera
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder21
pos = 0, 250, -1130
rotate = 0, 0, 0
archetype = space_girdera
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder22
pos = 0, 250, -1230
rotate = 0, 180, 0
archetype = space_girdera
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder23
pos = -50, 250, -1180
rotate = 0, -90, 0
archetype = space_girdera
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder24
pos = 50, 250, -1180
rotate = 0, 90, 0
archetype = space_girdera
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder25
pos = -250, 250, -930
rotate = 0, -45, 0
archetype = space_girderc
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder26
pos = -250, 250, -1430
rotate = 0, 45, 0
archetype = space_girderc
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder27
pos = 250, 250, -930
rotate = 0, 45, 0
archetype = space_girderc
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_girder28
pos = 250, 250, -1430
rotate = 0, -45, 0
archetype = space_girderc
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel01
pos = -75, 910, -1105
rotate = 0, 45, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel02
pos = -75, 910, -1255
rotate = 0, -45, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel03
pos = 75, 910, -1105
rotate = 0, 135, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel04
pos = 75, 910, -1255
rotate = 0, -135, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel05
pos = -270, 680, -1180
rotate = 0, 0, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel06
pos = 270, 680, -1180
rotate = 0, 180, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel07
pos = 0, 680, -910
rotate = 0, 90, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel08
pos = 0, 680, -1450
rotate = 0, -90, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel09
pos = -290, 600, -1020
rotate = 0, 30, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel10
pos = -160, 600, -890
rotate = 0, 60, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel11
pos = -175, 750, -1005
rotate = 0, 45, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel12
pos = 290, 600, -1020
rotate = 0, 150, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel13
pos = 160, 600, -890
rotate = 0, 120, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel14
pos = 175, 750, -1005
rotate = 0, 135, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel15
pos = -290, 600, -1340
rotate = 0, -30, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel16
pos = -160, 600, -1470
rotate = 0, -60, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel17
pos = -175, 750, -1355
rotate = 0, -45, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel18
pos = 290, 600, -1340
rotate = 0, -150, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel19
pos = 160, 600, -1470
rotate = 0, -120, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel20
pos = 175, 750, -1355
rotate = 0, -135, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel21
pos = 0, 530, -820
rotate = 0, 90, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel22
pos = 0, 380, -730
rotate = 0, 90, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel23
pos = 0, 530, -1540
rotate = 0, -90, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel24
pos = 0, 380, -1630
rotate = 0, -90, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel25
pos = -360, 530, -1180
rotate = 0, 0, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel26
pos = -450, 380, -1180
rotate = 0, 0, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel27
pos = 360, 530, -1180
rotate = 0, 180, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel28
pos = 450, 380, -1180
rotate = 0, 180, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel29
pos = -280, 470, -900
rotate = 0, 45, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel30
pos = -400, 380, -980
rotate = 0, 30, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel31
pos = -200, 380, -780
rotate = 0, 60, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel32
pos = 280, 470, -900
rotate = 0, 135, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel33
pos = 400, 380, -980
rotate = 0, 150, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel34
pos = 200, 380, -780
rotate = 0, 120, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel35
pos = 280, 470, -1460
rotate = 0, -135, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel36
pos = 400, 380, -1380
rotate = 0, -150, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel37
pos = 200, 380, -1580
rotate = 0, -120, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel38
pos = -280, 470, -1460
rotate = 0, -45, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel39
pos = -400, 380, -1380
rotate = 0, -30, 0
archetype = space_panel30
parent = br_cam_04

[Object]
nickname = br_cam_04_TREE_panel40
pos = -200, 380, -1580
rotate = 0, -60, 0
archetype = space_panel30
parent = br_cam_04
'''