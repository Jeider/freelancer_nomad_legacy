from templates.space_object_template import SpaceObjectTemplate


class Babylon(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'no_station_01'
    TEMPLATE = '''[Object]
nickname = no_station_01
pos = 0, 0, 0
rotate = -90, 0, 0
archetype = space_police02
{dock_props}

[Object]
nickname = no_station_01_CORE_tube01
pos = 0, 370, 0
rotate = -90, 45, 0
archetype = space_short_tube
parent = no_station_01

[Object]
nickname = no_station_01_CORE_control_tower01
pos = -275, 370, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = no_station_01

[Object]
nickname = no_station_01_CORE_control_tower02
pos = 275, 370, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = no_station_01

[Object]
nickname = no_station_01_CORE_control_tower03
pos = 0, 370, -275
rotate = 0, 0, 0
archetype = space_control_tower
parent = no_station_01

[Object]
nickname = no_station_01_CORE_control_tower04
pos = 0, 370, 275
rotate = 0, 0, 0
archetype = space_control_tower
parent = no_station_01

[Object]
nickname = no_station_01_CORE_control_tower05
pos = -275, 550, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = no_station_01

[Object]
nickname = no_station_01_CORE_control_tower06
pos = 275, 550, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = no_station_01

[Object]
nickname = no_station_01_CORE_control_tower07
pos = 0, 550, -275
rotate = 0, 0, 0
archetype = space_control_tower
parent = no_station_01

[Object]
nickname = no_station_01_CORE_control_tower08
pos = 0, 550, 275
rotate = 0, 0, 0
archetype = space_control_tower
parent = no_station_01

[Object]
nickname = no_station_01_CORE_control_tower09
pos = -275, 730, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = no_station_01

[Object]
nickname = no_station_01_CORE_control_tower10
pos = 275, 730, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = no_station_01

[Object]
nickname = no_station_01_CORE_control_tower11
pos = 0, 730, -275
rotate = 0, 0, 0
archetype = space_control_tower
parent = no_station_01

[Object]
nickname = no_station_01_CORE_control_tower12
pos = 0, 730, 275
rotate = 0, 0, 0
archetype = space_control_tower
parent = no_station_01

[Object]
nickname = no_station_01_CORE_dome01
pos = -275, 770, 0
rotate = 0, -142.5, 0
archetype = space_large_dome
parent = no_station_01

[Object]
nickname = no_station_01_CORE_dome02
pos = 275, 770, 0
rotate = 0, 37.5, 0
archetype = space_large_dome
parent = no_station_01

[Object]
nickname = no_station_01_CORE_dome03
pos = 0, 770, -275
rotate = 0, 127.5, 0
archetype = space_large_dome
parent = no_station_01

[Object]
nickname = no_station_01_CORE_dome04
pos = 0, 770, 275
rotate = 0, -52.5, 0
archetype = space_large_dome
parent = no_station_01

[Object]
nickname = no_station_01_CORE_sm_control_tower01
pos = 0, 460, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = no_station_01

[Object]
nickname = no_station_01_CORE_sm_control_tower02
pos = 0, 640, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = no_station_01

[Object]
nickname = no_station_01_CORE_sm_control_tower03
pos = 0, 837, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = no_station_01

[Object]
nickname = no_station_01_CORE_sm_control_tower04
pos = 0, 1300, 0
rotate = 0, 45, 0
archetype = space_small_control_tower
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat01
pos = -275, 460, -150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat02
pos = -275, 640, -150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat03
pos = -275, 460, 150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat04
pos = -275, 640, 150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat05
pos = -425, 460, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat06
pos = -425, 640, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat07
pos = -375, 460, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat08
pos = -375, 640, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat09
pos = -375, 460, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat11
pos = -375, 640, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat12
pos = 275, 460, -150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat13
pos = 275, 640, -150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat14
pos = 275, 460, 150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat15
pos = 275, 640, 150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat16
pos = 425, 460, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat17
pos = 425, 640, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat18
pos = 375, 460, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat19
pos = 375, 640, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat20
pos = 375, 460, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat21
pos = 375, 640, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat22
pos = -150, 460, -275
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat23
pos = -150, 640, -275
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat24
pos = 150, 460, -275
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat25
pos = 150, 640, -275
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat26
pos = 0, 460, -425
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat27
pos = 0, 640, -425
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat28
pos = -100, 460, -375
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat29
pos = -100, 640, -375
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat30
pos = 100, 460, -375
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat31
pos = 100, 640, -375
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat32
pos = -150, 460, 275
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat33
pos = -150, 640, 275
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat34
pos = 150, 460, 275
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat35
pos = 150, 640, 275
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat36
pos = 0, 460, 425
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat37
pos = 0, 640, 425
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat38
pos = -100, 460, 375
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat39
pos = -100, 640, 375
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat40
pos = 100, 460, 375
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat41
pos = 100, 640, 375
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_habitat42
pos = 0, 1210, 0
rotate = 0, 45, 0
archetype = space_habitat_wide
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind01
pos = -275, 460, 0
rotate = -90, 0, 0
archetype = space_industriala
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind02
pos = 275, 460, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind03
pos = 0, 460, -275
rotate = 90, 0, 0
archetype = space_industriala
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind04
pos = 0, 460, 275
rotate = 90, 0, 0
archetype = space_industriala
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind05
pos = 0, 370, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind06
pos = 0, 370, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind07
pos = 0, 550, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind08
pos = 0, 550, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind09
pos = 0, 730, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind10
pos = 0, 730, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind11
pos = -150, 370, -150
rotate = 0, 45, 0
archetype = space_industrial02d
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind12
pos = -150, 550, -150
rotate = 0, 45, 0
archetype = space_industrial02d
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind13
pos = -150, 730, -150
rotate = 0, 45, 0
archetype = space_industrial02d
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind14
pos = -150, 370, 150
rotate = 0, -45, 0
archetype = space_industrial02d
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind15
pos = -150, 550, 150
rotate = 0, -45, 0
archetype = space_industrial02d
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind16
pos = -150, 730, 150
rotate = 0, -45, 0
archetype = space_industrial02d
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind17
pos = 150, 370, -150
rotate = 0, -45, 0
archetype = space_industrial02d
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind18
pos = 150, 550, -150
rotate = 0, -45, 0
archetype = space_industrial02d
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind19
pos = 150, 730, -150
rotate = 0, -45, 0
archetype = space_industrial02d
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind20
pos = 150, 370, 150
rotate = 0, 45, 0
archetype = space_industrial02d
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind21
pos = 150, 550, 150
rotate = 0, 45, 0
archetype = space_industrial02d
parent = no_station_01

[Object]
nickname = no_station_01_CORE_ind22
pos = 150, 730, 150
rotate = 0, 45, 0
archetype = space_industrial02d
parent = no_station_01

[Object]
nickname = no_station_01_CORE_girder01
pos = 0, 460, -125
rotate = 0, 0, 0
archetype = space_girder
parent = no_station_01

[Object]
nickname = no_station_01_CORE_girder02
pos = 0, 460, 125
rotate = 0, 0, 0
archetype = space_girder
parent = no_station_01

[Object]
nickname = no_station_01_CORE_girder03
pos = -125, 460, 0
rotate = 0, 90, 0
archetype = space_girder
parent = no_station_01

[Object]
nickname = no_station_01_CORE_girder04
pos = 125, 460, 0
rotate = 0, 90, 0
archetype = space_girder
parent = no_station_01

[Object]
nickname = no_station_01_CORE_girder05
pos = 0, 640, -105
rotate = 0, 0, 0
archetype = space_girder
parent = no_station_01

[Object]
nickname = no_station_01_CORE_girder06
pos = 0, 640, 105
rotate = 0, 0, 0
archetype = space_girder
parent = no_station_01

[Object]
nickname = no_station_01_CORE_girder07
pos = -105, 640, 0
rotate = 0, 90, 0
archetype = space_girder
parent = no_station_01

[Object]
nickname = no_station_01_CORE_girder08
pos = 105, 640, 0
rotate = 0, 90, 0
archetype = space_girder
parent = no_station_01

[Object]
nickname = no_station_01_CORE_girder09
pos = 0, 837, -125
rotate = 0, 0, 0
archetype = space_girder
parent = no_station_01

[Object]
nickname = no_station_01_CORE_girder10
pos = 0, 837, 125
rotate = 0, 0, 0
archetype = space_girder
parent = no_station_01

[Object]
nickname = no_station_01_CORE_girder11
pos = -125, 837, 0
rotate = 0, 90, 0
archetype = space_girder
parent = no_station_01

[Object]
nickname = no_station_01_CORE_girder12
pos = 125, 837, 0
rotate = 0, 90, 0
archetype = space_girder
parent = no_station_01

[Object]
nickname = no_station_01_CORE_girder13
pos = -150, 550, -150
rotate = 90, 45, 0
archetype = space_girder
parent = no_station_01

[Object]
nickname = no_station_01_CORE_girder14
pos = -150, 550, 150
rotate = 90, -45, 0
archetype = space_girder
parent = no_station_01

[Object]
nickname = no_station_01_CORE_girder15
pos = 150, 550, -150
rotate = 90, -45, 0
archetype = space_girder
parent = no_station_01

[Object]
nickname = no_station_01_CORE_girder16
pos = 150, 550, 150
rotate = 90, 45, 0
archetype = space_girder
parent = no_station_01

[Object]
nickname = no_station_01_CORE_control_block01
pos = -140, 720, -140
rotate = 0, 45, 0
archetype = space_control_block
parent = no_station_01

[Object]
nickname = no_station_01_CORE_control_block02
pos = -140, 720, 140
rotate = 0, 135, 0
archetype = space_control_block
parent = no_station_01

[Object]
nickname = no_station_01_CORE_control_block03
pos = 140, 720, -140
rotate = 0, -45, 0
archetype = space_control_block
parent = no_station_01

[Object]
nickname = no_station_01_CORE_control_block04
pos = 140, 720, 140
rotate = 0, -135, 0
archetype = space_control_block
parent = no_station_01

[Object]
nickname = no_station_01_CORE_sm_control_block01
pos = 0, 1365, 0
rotate = 0, 45, 0
archetype = space_small_control_block
parent = no_station_01

[Object]
nickname = no_station_01_MISC_dome01
pos = 0, 400, -650
rotate = 0, 0, 0
archetype = space_dome
parent = no_station_01

[Object]
nickname = no_station_01_MISC_dome02
pos = 0, 400, 650
rotate = 0, 180, 0
archetype = space_dome
parent = no_station_01

[Object]
nickname = no_station_01_MISC_dome03
pos = -650, 400, 0
rotate = 0, 90, 0
archetype = space_dome
parent = no_station_01

[Object]
nickname = no_station_01_MISC_dome04
pos = 650, 400, 0
rotate = 0, -90, 0
archetype = space_dome
parent = no_station_01

[Object]
nickname = no_station_01_MISC_dome05
pos = -460, 400, -460
rotate = 0, 45, 0
archetype = space_dome
parent = no_station_01

[Object]
nickname = no_station_01_MISC_dome06
pos = -460, 400, 460
rotate = 0, 135, 0
archetype = space_dome
parent = no_station_01

[Object]
nickname = no_station_01_MISC_dome07
pos = 460, 400, -460
rotate = 0, -45, 0
archetype = space_dome
parent = no_station_01

[Object]
nickname = no_station_01_MISC_dome08
pos = 460, 400, 460
rotate = 0, -135, 0
archetype = space_dome
parent = no_station_01

[Object]
nickname = no_station_01_MISC_control_tower01
pos = -275, 370, -275
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = no_station_01

[Object]
nickname = no_station_01_MISC_control_tower02
pos = -275, 370, 275
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = no_station_01

[Object]
nickname = no_station_01_MISC_control_tower03
pos = 275, 370, -275
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = no_station_01

[Object]
nickname = no_station_01_MISC_control_tower04
pos = 275, 370, 275
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = no_station_01

[Object]
nickname = no_station_01_MISC_control_block01
pos = -275, 370, -275
rotate = 0, 45, 0
archetype = space_control_block
parent = no_station_01

[Object]
nickname = no_station_01_MISC_control_block02
pos = -275, 370, 275
rotate = 0, 135, 0
archetype = space_control_block
parent = no_station_01

[Object]
nickname = no_station_01_MISC_control_block03
pos = 275, 370, -275
rotate = 0, -45, 0
archetype = space_control_block
parent = no_station_01

[Object]
nickname = no_station_01_MISC_control_block04
pos = 275, 370, 275
rotate = 0, -135, 0
archetype = space_control_block
parent = no_station_01

[Object]
nickname = no_station_01_MISC_sm_control_block01
pos = -824, 369, 0
rotate = 0, 0, 90
archetype = space_small_control_block
parent = no_station_01

[Object]
nickname = no_station_01_MISC_sm_control_block02
pos = 824, 369, 0
rotate = 0, 0, -90
archetype = space_small_control_block
parent = no_station_01

[Object]
nickname = no_station_01_MISC_sm_control_block03
pos = 0, 369, -824
rotate = -90, 0, 0
archetype = space_small_control_block
parent = no_station_01

[Object]
nickname = no_station_01_MISC_sm_control_block04
pos = 0, 369, 824
rotate = 90, 0, 0
archetype = space_small_control_block
parent = no_station_01

[Object]
nickname = no_station_01_MISC_ind01
pos = 0, 220, -360
rotate = 0, 90, 0
archetype = space_industriala
parent = no_station_01

[Object]
nickname = no_station_01_MISC_ind02
pos = 0, 220, 360
rotate = 0, 90, 0
archetype = space_industriala
parent = no_station_01

[Object]
nickname = no_station_01_MISC_ind03
pos = -360, 220, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = no_station_01

[Object]
nickname = no_station_01_MISC_ind04
pos = 360, 220, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = no_station_01

[Object]
nickname = no_station_01_MISC_ind05
pos = -250, 220, -250
rotate = 0, -45, 0
archetype = space_industriala
parent = no_station_01

[Object]
nickname = no_station_01_MISC_ind06
pos = -250, 220, 250
rotate = 0, -135, 0
archetype = space_industriala
parent = no_station_01

[Object]
nickname = no_station_01_MISC_ind07
pos = 250, 220, -250
rotate = 0, 45, 0
archetype = space_industriala
parent = no_station_01

[Object]
nickname = no_station_01_MISC_ind08
pos = 250, 220, 250
rotate = 0, 135, 0
archetype = space_industriala
parent = no_station_01

[Object]
nickname = no_station_01_MISC_girder01
pos = 0, 350, -650
rotate = 30, 0, 0
archetype = space_girdera
parent = no_station_01

[Object]
nickname = no_station_01_MISC_girder02
pos = 0, 350, 650
rotate = 30, 180, 0
archetype = space_girdera
parent = no_station_01

[Object]
nickname = no_station_01_MISC_girder03
pos = -650, 350, 0
rotate = 30, 90, 0
archetype = space_girdera
parent = no_station_01

[Object]
nickname = no_station_01_MISC_girder04
pos = 650, 350, 0
rotate = 30, -90, 0
archetype = space_girdera
parent = no_station_01

[Object]
nickname = no_station_01_MISC_girder05
pos = -460, 350, -460
rotate = 30, 45, 0
archetype = space_girdera
parent = no_station_01

[Object]
nickname = no_station_01_MISC_girder06
pos = -460, 350, 460
rotate = 30, 135, 0
archetype = space_girdera
parent = no_station_01

[Object]
nickname = no_station_01_MISC_girder07
pos = 460, 350, -460
rotate = 30, -45, 0
archetype = space_girdera
parent = no_station_01

[Object]
nickname = no_station_01_MISC_girder08
pos = 460, 350, 460
rotate = 30, -135, 0
archetype = space_girdera
parent = no_station_01

[Object]
nickname = no_station_01_MISC_sm_girder01
pos = -150, 220, -345
rotate = 0, 120, 0
archetype = space_girderc
parent = no_station_01

[Object]
nickname = no_station_01_MISC_sm_girder02
pos = 150, 220, -345
rotate = 0, -118, 0
archetype = space_girderc
parent = no_station_01

[Object]
nickname = no_station_01_MISC_sm_girder03
pos = -150, 220, 345
rotate = 0, -120, 0
archetype = space_girderc
parent = no_station_01

[Object]
nickname = no_station_01_MISC_sm_girder04
pos = 150, 220, 345
rotate = 0, 118, 0
archetype = space_girderc
parent = no_station_01

[Object]
nickname = no_station_01_MISC_sm_girder05
pos = -345, 220, -150
rotate = 0, -30, 0
archetype = space_girderc
parent = no_station_01

[Object]
nickname = no_station_01_MISC_sm_girder06
pos = -345, 220, 150
rotate = 0, 28, 0
archetype = space_girderc
parent = no_station_01

[Object]
nickname = no_station_01_MISC_sm_girder07
pos = 345, 220, -150
rotate = 0, 30, 0
archetype = space_girderc
parent = no_station_01

[Object]
nickname = no_station_01_MISC_sm_girder08
pos = 345, 220, 150
rotate = 0, -28, 0
archetype = space_girderc
parent = no_station_01

[Object]
nickname = no_station_01_MISC_tanks01
pos = 0, 160, -360
rotate = 0, 90, 0
archetype = space_tankl4
parent = no_station_01

[Object]
nickname = no_station_01_MISC_tanks02
pos = 0, 160, 360
rotate = 0, 90, 0
archetype = space_tankl4
parent = no_station_01

[Object]
nickname = no_station_01_MISC_tanks03
pos = -360, 160, 0
rotate = 0, 0, 0
archetype = space_tankl4
parent = no_station_01

[Object]
nickname = no_station_01_MISC_tanks04
pos = 360, 160, 0
rotate = 0, 0, 0
archetype = space_tankl4
parent = no_station_01

[Object]
nickname = no_station_01_MISC_tanks05
pos = -250, 160, -250
rotate = 0, -45, 0
archetype = space_tankl4
parent = no_station_01

[Object]
nickname = no_station_01_MISC_tanks06
pos = -250, 160, 250
rotate = 0, 45, 0
archetype = space_tankl4
parent = no_station_01

[Object]
nickname = no_station_01_MISC_tanks07
pos = 250, 160, -250
rotate = 0, 45, 0
archetype = space_tankl4
parent = no_station_01

[Object]
nickname = no_station_01_MISC_tanks08
pos = 250, 160, 250
rotate = 0, -45, 0
archetype = space_tankl4
parent = no_station_01

[Object]
nickname = no_station_01_MISC_reactor01
pos = -150, 250, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_station_01

[Object]
nickname = no_station_01_MISC_reactor02
pos = 150, 250, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_station_01

[Object]
nickname = no_station_01_MISC_reactor03
pos = 0, 250, -150
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_station_01

[Object]
nickname = no_station_01_MISC_reactor04
pos = 0, 250, 150
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = no_station_01

[Object]
nickname = no_station_01_MISC_lg_control_tower01
pos = 0, 110, 0
rotate = 0, 45, 0
archetype = space_control_tower
parent = no_station_01

[Object]
nickname = no_station_01_MISC_arilock01
pos = 0, 0, 0
rotate = -90, 0, 0
archetype = space_airlock_dummy
parent = no_station_01

[Object]
nickname = no_station_01_MISC_last_girder01
pos = 0, 270, -360
rotate = 90, 90, 0
archetype = space_girderc
parent = no_station_01

[Object]
nickname = no_station_01_MISC_last_girder02
pos = 0, 270, 360
rotate = 90, 90, 0
archetype = space_girderc
parent = no_station_01

[Object]
nickname = no_station_01_MISC_last_girder03
pos = -360, 270, 0
rotate = 90, 0, 0
archetype = space_girderc
parent = no_station_01

[Object]
nickname = no_station_01_MISC_last_girder04
pos = 360, 270, 0
rotate = 90, 0, 0
archetype = space_girderc
parent = no_station_01

[Object]
nickname = no_station_01_MISC_last_girder05
pos = -250, 270, -250
rotate = 90, -45, 0
archetype = space_girderc
parent = no_station_01

[Object]
nickname = no_station_01_MISC_last_girder06
pos = -250, 270, 250
rotate = 90, -135, 0
archetype = space_girderc
parent = no_station_01

[Object]
nickname = no_station_01_MISC_last_girder07
pos = 250, 270, -250
rotate = 90, 45, 0
archetype = space_girderc
parent = no_station_01

[Object]
nickname = no_station_01_MISC_last_girder08
pos = 250, 270, 250
rotate = 90, 135, 0
archetype = space_girderc
parent = no_station_01
'''
