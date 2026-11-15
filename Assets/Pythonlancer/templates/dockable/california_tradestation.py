from templates.space_object_template import SpaceObjectTemplate


class CaliforniaTradestationOriginal(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_cal_07'
    TEMPLATE = '''[Object]
nickname = li_cal_07
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = space_police02_losangeles
{dock_props}

[Object]
nickname = li_cal_07_shipyard01
pos = 200, -275, -315
rotate = 180, 00, 0
archetype = shipyard_small
parent = li_cal_07

[Object]
nickname = li_cal_07_shipyard02
pos = 65, -275, -315
rotate = 180, 00, 0
archetype = shipyard_small
parent = li_cal_07

[Object]
nickname = li_cal_07_shipyard03
pos = -65, -275, -315
rotate = 180, 00, 0
archetype = shipyard_small
parent = li_cal_07

[Object]
nickname = li_cal_07_shipyard04
pos = -200, -275, -315
rotate = 180, 00, 0
archetype = shipyard_small
parent = li_cal_07

[Object]
nickname = li_cal_07_ind01
pos = 125, 180, -315
rotate = 0, 90, 0
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind02
pos = 125, -180, -315
rotate = 0, 90, 0
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind03
pos = 125, 0, -495
rotate = 90, 0, 90
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind04
pos = 125, 0, -135
rotate = 90, 0, 90
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind05
pos = 125, -90, -470
rotate = 90, 30, 90
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind06
pos = 125, 90, -470
rotate = 90, -30, 90
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind07
pos = 125, 90, -160
rotate = 90, 30, 90
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind08
pos = 125, -90, -160
rotate = 90, -30, 90
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind09
pos = 125, -155, -225
rotate = 90, -60, 90
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind10
pos = 125, 155, -405
rotate = 90, -60, 90
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind11
pos = 125, 155, -225
rotate = 90, 60, 90
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind12
pos = 125, -155, -405
rotate = 90, 60, 90
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind13
pos = -125, 180, -315
rotate = 0, 90, 0
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind14
pos = -125, -180, -315
rotate = 0, 90, 0
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind15
pos = -125, 0, -495
rotate = 90, 0, 90
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind16
pos = -125, 0, -135
rotate = 90, 0, 90
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind17
pos = -125, -90, -470
rotate = 90, 30, 90
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind18
pos = -125, 90, -470
rotate = 90, -30, 90
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind19
pos = -125, 90, -160
rotate = 90, 30, 90
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind20
pos = -125, -90, -160
rotate = 90, -30, 90
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind21
pos = -125, -155, -225
rotate = 90, -60, 90
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind22
pos = -125, 155, -405
rotate = 90, -60, 90
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind23
pos = -125, 155, -225
rotate = 90, 60, 90
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind24
pos = -125, -155, -405
rotate = 90, 60, 90
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind25
pos = 0, 395, -315
rotate = -90, 0, 0
archetype = space_industriala
parent = li_cal_07

[Object]
nickname = li_cal_07_ind26
pos = 250, 125, -315
rotate = 0, -90, 0
archetype = space_industrialc
parent = li_cal_07

[Object]
nickname = li_cal_07_ind27
pos = -250, 125, -315
rotate = 0, 90, 0
archetype = space_industrialc
parent = li_cal_07

[Object]
nickname = li_cal_07_ind28
pos = 0, 680, -315
rotate = -90, 0, 0
archetype = space_industrialc
parent = li_cal_07

[Object]
nickname = li_cal_07_ind29
pos = -125, -225, -315
rotate = 0, 90, 0
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_ind30
pos = 125, -225, -315
rotate = 0, 90, 0
archetype = space_industrial02d
parent = li_cal_07

[Object]
nickname = li_cal_07_contol_tower01
pos = -2, 0, -315
rotate = 0, 90, 90
archetype = space_control_tower
parent = li_cal_07

[Object]
nickname = li_cal_07_contol_tower02
pos = 82, 0, -315
rotate = 0, 90, 90
archetype = space_control_tower
parent = li_cal_07

[Object]
nickname = li_cal_07_contol_tower03
pos = 165, 0, -315
rotate = 0, 90, 90
archetype = space_control_tower
parent = li_cal_07

[Object]
nickname = li_cal_07_contol_tower04
pos = -84, 0, -315
rotate = 0, 90, 90
archetype = space_control_tower
parent = li_cal_07

[Object]
nickname = li_cal_07_contol_tower05
pos = -165, 0, -315
rotate = 0, 90, 90
archetype = space_control_tower
parent = li_cal_07

[Object]
nickname = li_cal_07_contol_tower06
pos = 245, 0, -315
rotate = 0, -90, 90
archetype = space_control_tower
parent = li_cal_07

[Object]
nickname = li_cal_07_contol_tower07
pos = -245, 0, -315
rotate = 0, 90, 90
archetype = space_control_tower
parent = li_cal_07

[Object]
nickname = li_cal_07_contol_tower08
pos = 0, 210, -315
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = li_cal_07

[Object]
nickname = li_cal_07_contol_tower09
pos = 0, 0, -525
rotate = 90, 0, 0
archetype = space_medium_control_tower
parent = li_cal_07

[Object]
nickname = li_cal_07_contol_tower10
pos = 0, 0, -105
rotate = 90, 0, 0
archetype = space_medium_control_tower
parent = li_cal_07

[Object]
nickname = li_cal_07_contol_tower11
pos = 0, 520, -315
rotate = 0, 0, 0
archetype = space_control_tower
parent = li_cal_07

[Object]
nickname = li_cal_07_contol_tower12
pos = 0, 688, -315
rotate = 180, 45, 0
archetype = space_control_tower
parent = li_cal_07

[Object]
nickname = li_cal_07_contol_tower13
pos = 0, 0, -665
rotate = 90, 0, 0
archetype = space_small_control_tower
parent = li_cal_07

[Object]
nickname = li_cal_07_airlock01
pos = 0, 325, -315
rotate = 90, 45, 0
archetype = space_airlock_dummy
parent = li_cal_07

[Object]
nickname = li_cal_07_airlock02
pos = 0, 0, -615
rotate = 0, 0, 0
archetype = space_airlock_dummy
parent = li_cal_07

[Object]
nickname = li_cal_07_airlock03
pos = 0, 0, -15
rotate = 0, 180, 0
archetype = space_airlock_dummy
parent = li_cal_07

[Object]
nickname = li_cal_07_research01
pos = 125, 125, -315
rotate = 0, -90, 0
archetype = space_tube_fix
parent = li_cal_07

[Object]
nickname = li_cal_07_research02
pos = 50, -100, -440
rotate = 0, -90, 0
archetype = space_tube_fix
parent = li_cal_07

[Object]
nickname = li_cal_07_research03
pos = 50, -100, -190
rotate = 0, -90, 0
archetype = space_tube_fix
parent = li_cal_07

[Object]
nickname = li_cal_07_research04
pos = -125, 125, -315
rotate = 0, 90, 0
archetype = space_tube_fix
parent = li_cal_07

[Object]
nickname = li_cal_07_research05
pos = -50, -100, -440
rotate = 0, 90, 0
archetype = space_tube_fix
parent = li_cal_07

[Object]
nickname = li_cal_07_research06
pos = -50, -100, -190
rotate = 0, 90, 0
archetype = space_tube_fix
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks01
pos = 390, -125, -440
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks02
pos = 655, -125, -440
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks03
pos = 920, -125, -440
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks04
pos = 1185, -125, -440
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks05
pos = 1450, -125, -440
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks06
pos = 390, -125, -190
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks07
pos = 655, -125, -190
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks08
pos = 920, -125, -190
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks09
pos = 1185, -125, -190
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks10
pos = 1450, -125, -190
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks11
pos = 390, -110, -465
rotate = 90, 30, 90
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks12
pos = 655, -110, -465
rotate = 90, 30, 90
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks13
pos = 920, -110, -465
rotate = 90, 30, 90
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks14
pos = 1185, -110, -465
rotate = 90, 30, 90
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks15
pos = 1450, -110, -465
rotate = 90, 30, 90
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks16
pos = 390, -110, -165
rotate = 90, 150, 90
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks17
pos = 655, -110, -165
rotate = 90, 150, 90
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks18
pos = 920, -110, -165
rotate = 90, 150, 90
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks19
pos = 1185, -110, -165
rotate = 90, 150, 90
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks20
pos = 1450, -110, -165
rotate = 90, 150, 90
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks21
pos = -390, -125, -440
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks22
pos = -655, -125, -440
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks23
pos = -920, -125, -440
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks24
pos = -1185, -125, -440
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks25
pos = -1450, -125, -440
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks26
pos = -390, -125, -190
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks27
pos = -655, -125, -190
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks28
pos = -920, -125, -190
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks29
pos = -1185, -125, -190
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks30
pos = -1450, -125, -190
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks31
pos = -390, -110, -465
rotate = 90, 30, 90
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks32
pos = -655, -110, -465
rotate = 90, 30, 90
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks33
pos = -920, -110, -465
rotate = 90, 30, 90
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks34
pos = -1185, -110, -465
rotate = 90, 30, 90
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks35
pos = -1450, -110, -465
rotate = 90, 30, 90
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks36
pos = -390, -110, -165
rotate = 90, 150, 90
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks37
pos = -655, -110, -165
rotate = 90, 150, 90
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks38
pos = -920, -110, -165
rotate = 90, 150, 90
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks39
pos = -1185, -110, -165
rotate = 90, 150, 90
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_tanks40
pos = -1450, -110, -165
rotate = 90, 150, 90
archetype = space_tankl4
parent = li_cal_07

[Object]
nickname = li_cal_07_girder01
pos = 500, 125, -315
rotate = 65, 30, 30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder02
pos = 501, 125, -315
rotate = 65, -30, -30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder03
pos = 920, 125, -315
rotate = 65, 30, 30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder04
pos = 921, 125, -315
rotate = 65, -30, -30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder05
pos = 1340, 125, -315
rotate = 65, 30, 30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder06
pos = 1341, 125, -315
rotate = 65, -30, -30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder07
pos = 500, 125, -315
rotate = 65, 150, 30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder08
pos = 501, 125, -315
rotate = 65, 210, -30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder09
pos = 920, 125, -315
rotate = 65, 150, 30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder10
pos = 921, 125, -315
rotate = 65, 210, -30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder11
pos = 1340, 125, -315
rotate = 65, 150, 30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder12
pos = 1341, 125, -315
rotate = 65, 210, -30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder13
pos = -500, 125, -315
rotate = 65, 30, 30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder14
pos = -499, 125, -315
rotate = 65, -30, -30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder15
pos = -920, 125, -315
rotate = 65, 30, 30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder16
pos = -919, 125, -315
rotate = 65, -30, -30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder17
pos = -1340, 125, -315
rotate = 65, 30, 30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder18
pos = -1339, 125, -315
rotate = 65, -30, -30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder19
pos = -500, 125, -315
rotate = 65, 150, 30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder20
pos = -499, 125, -315
rotate = 65, 210, -30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder21
pos = -920, 125, -315
rotate = 65, 150, 30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder22
pos = -919, 125, -315
rotate = 65, 210, -30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder23
pos = -1340, 125, -315
rotate = 65, 150, 30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder24
pos = -1339, 125, -315
rotate = 65, 210, -30
archetype = space_girdera
parent = li_cal_07

[Object]
nickname = li_cal_07_girder25
pos = 0, 480, -215
rotate = -30, 0, 0
archetype = space_girderc
parent = li_cal_07

[Object]
nickname = li_cal_07_girder26
pos = 0, 480, -415
rotate = 30, 0, 0
archetype = space_girderc
parent = li_cal_07

[Object]
nickname = li_cal_07_girder27
pos = 100, 480, -315
rotate = -30, 90, 0
archetype = space_girderc
parent = li_cal_07

[Object]
nickname = li_cal_07_girder28
pos = -100, 480, -315
rotate = 30, 90, 0
archetype = space_girderc
parent = li_cal_07

[Object]
nickname = li_cal_07_girder29
pos = 0, 740, -215
rotate = 30, 0, 0
archetype = space_girderc
parent = li_cal_07

[Object]
nickname = li_cal_07_girder30
pos = 0, 740, -415
rotate = -30, 0, 0
archetype = space_girderc
parent = li_cal_07

[Object]
nickname = li_cal_07_girder31
pos = 100, 740, -315
rotate = 30, 90, 0
archetype = space_girderc
parent = li_cal_07

[Object]
nickname = li_cal_07_girder32
pos = -100, 740, -315
rotate = -30, 90, 0
archetype = space_girderc
parent = li_cal_07

[Object]
nickname = li_cal_07_habitat01
pos = 0, 605, -490
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_07

[Object]
nickname = li_cal_07_habitat02
pos = 0, 605, -140
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_07

[Object]
nickname = li_cal_07_habitat03
pos = 175, 605, -315
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_07

[Object]
nickname = li_cal_07_habitat04
pos = -175, 605, -315
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_07

[Object]
nickname = li_cal_07_habitat06
pos = -160, 605, -249
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_07

[Object]
nickname = li_cal_07_habitat07
pos = 160, 605, -249
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_07

[Object]
nickname = li_cal_07_habitat08
pos = -160, 605, -381
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_07

[Object]
nickname = li_cal_07_habitat09
pos = 160, 605, -381
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_07

[Object]
nickname = li_cal_07_habitat10
pos = -66, 605, -155
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_07

[Object]
nickname = li_cal_07_habitat11
pos = -66, 605, -475
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_07

[Object]
nickname = li_cal_07_habitat12
pos = 66, 605, -155
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_07

[Object]
nickname = li_cal_07_habitat13
pos = 66, 605, -475
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_07

[Object]
nickname = li_cal_07_habitat14
pos = -122, 605, -193
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_07

[Object]
nickname = li_cal_07_habitat15
pos = 122, 605, -193
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_07

[Object]
nickname = li_cal_07_habitat16
pos = -122, 605, -437
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_07

[Object]
nickname = li_cal_07_habitat17
pos = 122, 605, -437
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_07

[Object]
nickname = li_cal_07_habitat18
pos = 0, 0, -725
rotate = -90, 0, 0
archetype = space_small_control_block
parent = li_cal_07
'''


class CaliforniaTradestation(CaliforniaTradestationOriginal):
    TEMPLATE = '''[Object]
nickname = li_cal_07
pos = 0, 0, -315
rotate = 0, 0, 0
archetype = losangeles_two_docks
{dock_props}

[Object]
nickname = li_cal_07_shipyard01
pos = 725, 232.5, -315
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1
parent = li_cal_07

[Object]
nickname = li_cal_07_shipyard03
pos = -725, 232.5, -315
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0
parent = li_cal_07

[Object]
nickname = li_cal_07_airlock01
pos = 0, 325, -315
rotate = 90, 45, 0
archetype = space_airlock_dummy
parent = li_cal_07

[Object]
nickname = li_cal_07_airlock02
pos = 0, 0, -615
rotate = 0, 0, 0
archetype = space_airlock_dummy
parent = li_cal_07

[Object]
nickname = li_cal_07_airlock03
pos = 0, 0, -15
rotate = 0, 180, 0
archetype = space_airlock_dummy
parent = li_cal_07



[Object]
nickname = li_cal_07_col_structure1_collision00
pos = 200.000046, -285.813172, -393.570226
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision00
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision01
pos = 200.000046, -285.813293, -338.622437
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision01
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision02
pos = 200.000065, -287.504022, -244.413169
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision02
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision03
pos = 200.000051, -290.383243, -236.735246
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision03
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision04
pos = 65.0000458, -285.813172, -393.570226
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision04
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision05
pos = 65.0000458, -285.813293, -338.622437
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision05
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision06
pos = 65.0000648, -287.504022, -244.413169
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision06
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision07
pos = 65.0000515, -290.383243, -236.735246
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision07
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision08
pos = 126.664196, 179.649204, -314.29899
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision08
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision09
pos = 126.664196, -180.350796, -314.29899
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision09
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision10
pos = 126.664196, -0.701009771, -495.350796
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision10
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision11
pos = 126.664196, -0.701009771, -135.350796
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision11
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision12
pos = 126.664196, -90.5380612, -470.130755
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision12
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision13
pos = 126.664196, 89.8498858, -470.509617
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision13
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision14
pos = 126.664196, 89.4619388, -160.130755
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision14
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision15
pos = 126.664196, -90.1501142, -160.509617
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision15
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision16
pos = 126.664196, -154.869245, -225.538059
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision16
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision17
pos = 126.664196, 155.130755, -405.538059
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision17
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision18
pos = 126.664196, 154.490384, -224.849887
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision18
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision19
pos = 126.664196, -155.509616, -404.849887
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision19
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision20
pos = 186.359285, 125.2225, -315.012764
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision20
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision21
pos = 126.664196, -225.350796, -314.29899
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision21
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision22
pos = 82.1499867, 0.0143051091, -314.932022
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision22
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision23
pos = 82.1499877, 0.0143051091, -314.932014
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision23
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision24
pos = 165.149987, 0.0143051091, -314.932022
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision24
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision25
pos = 165.149988, 0.0143051091, -314.932014
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision25
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision26
pos = 245.149988, -0.0143058299, -315.067986
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision26
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision27
pos = 245.149988, -0.0143058299, -315.067978
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision27
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision28
pos = -0.0651258312, 688.149989, -314.968984
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision28
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision29
pos = -0.0651258312, 688.149989, -251.114244
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision29
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision30
pos = 40.0810699, -63.0562706, -314.988477
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision30
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure1_collision31
pos = 773.172622, 336.717881, -314.908031
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure1_collision31
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision00
pos = -64.9999542, -285.813172, -393.570226
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision00
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision01
pos = -64.9999542, -285.813293, -338.622437
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision01
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision02
pos = -64.9999352, -287.504022, -244.413169
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision02
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision03
pos = -64.9999485, -290.383243, -236.735246
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision03
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision04
pos = -199.999954, -285.813172, -393.570226
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision04
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision05
pos = -199.999954, -285.813293, -338.622437
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision05
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision06
pos = -199.999935, -287.504022, -244.413169
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision06
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision07
pos = -199.999949, -290.383243, -236.735246
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision07
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision08
pos = -123.335804, 179.649204, -314.29899
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision08
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision09
pos = -123.335804, -180.350796, -314.29899
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision09
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision10
pos = -123.335804, -0.701009771, -495.350796
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision10
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision11
pos = -123.335804, -0.701009771, -135.350796
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision11
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision12
pos = -123.335804, -90.5380612, -470.130755
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision12
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision13
pos = -123.335804, 89.8498858, -470.509617
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision13
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision14
pos = -123.335804, 89.4619388, -160.130755
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision14
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision15
pos = -123.335804, -90.1501142, -160.509617
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision15
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision16
pos = -123.335804, -154.869245, -225.538059
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision16
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision17
pos = -123.335804, 155.130755, -405.538059
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision17
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision18
pos = -123.335804, 154.490384, -224.849887
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision18
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision19
pos = -123.335804, -155.509616, -404.849887
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision19
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision20
pos = -0.0127677917, 396.764076, -315.2225
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision20
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision21
pos = -91.7256911, 432.969258, -315.106888
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision21
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision22
pos = -123.335804, -225.350796, -314.29899
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision22
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision23
pos = -1.85001329, 0.0143051091, -314.932022
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision23
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision24
pos = -1.85001227, 0.0143051091, -314.932014
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision24
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision25
pos = -83.8500133, 0.0143051091, -314.932022
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision25
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision26
pos = -83.8500123, 0.0143051091, -314.932014
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision26
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision27
pos = -164.850013, 0.0143051091, -314.932022
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision27
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision28
pos = -164.850012, 0.0143051091, -314.932014
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision28
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision29
pos = -244.850013, 0.0143051091, -314.932022
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision29
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision30
pos = -244.850012, 0.0143051091, -314.932014
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision30
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision31
pos = -0.043510437, 209.850012, -314.990845
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision31
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision32
pos = 6.79901886, 209.850012, -314.990845
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision32
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision33
pos = -0.043510437, -0.00915573024, -525.149989
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision33
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision34
pos = 6.79901886, -0.00915573024, -525.149989
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision34
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision35
pos = -0.043510437, -0.00915573024, -105.149989
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision35
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision36
pos = 6.79901886, -0.00915573024, -105.149989
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision36
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision37
pos = -0.0679855347, 519.850013, -314.985695
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision37
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision38
pos = -0.0679779053, 519.850013, -314.985695
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision38
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision39
pos = -40.0755538, -63.0562706, -314.988477
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision39
parent = li_cal_07

[Object]
nickname = li_cal_07_col_structure0_collision40
pos = -791.381983, 336.675381, -314.908031
rotate = 0, 0, 0
archetype = batch_californi_18ddf783_structure0_collision40
parent = li_cal_07

'''
