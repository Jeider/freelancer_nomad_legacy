from templates.space_object_template import SpaceObjectTemplate


class Olaf(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'tau29_03'
    TEMPLATE = '''[Object]
nickname = tau29_03
pos = 0, -600, 0
rotate = 0, 0, 0
archetype = arendal_core
{root_props}

[Object]
nickname = tau29_03_dock
pos = 0, 305, 0
rotate = 90, 0, 0
archetype = space_police02
{dock_props}

[Object]
nickname = tau29_03_center
pos = 0, -600, 0
rotate = 0, 45, 0
archetype = sw_center_250
parent = tau29_03

[Object]
nickname = tau29_03_tunnel01
pos = 0, 290, 0
rotate = 90, 0, 0
archetype = space_airlock_dummy
parent = tau29_03

[Object]
nickname = tau29_03_xtower01
pos = 0, 190, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_xtower02
pos = 0, 70, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_xtower03
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_xtower04
pos = 0, -140, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_xtower05
pos = 0, -70, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_xtube01
pos = 0, 190, 0
rotate = 90, 0, 0
archetype = space_short_tube
parent = tau29_03

[Object]
nickname = tau29_03_cntrl_twr01
pos = 0, -830, 360
rotate = 90, 0, 0
archetype = space_small_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_cntrl_twr02
pos = 0, -1080, 360
rotate = 90, 0, 0
archetype = space_small_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_cntrl_twr03
pos = 0, -550, 237
rotate = -90, 0, 0
archetype = space_small_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_cntrl_twr04
pos = 140, -1080, 1.5
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_cntrl_twr05
pos = -140, -1080, 1.5
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_cntrl_twr06
pos = 140, -1260, 1.5
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_cntrl_twr06a
pos = 140, -1290, 1.5
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_cntrl_twr07
pos = -140, -1260, 1.5
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_cntrl_twr07a
pos = -140, -1290, 1.5
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_cntrl_twr_girder01
pos = 0, -1080, 1.5
rotate = 0, 90, 0
archetype = space_girder
parent = tau29_03

[Object]
nickname = tau29_03_cntrl_twr08
pos = 1, -955, 140
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_cntrl_twr09
pos = 1, -955, -140
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_cntrl_twr_girder02
pos = 1, -955, 0
rotate = 0, 0, 0
archetype = space_girder
parent = tau29_03

[Object]
nickname = tau29_03_cntrl_twr10
pos = 0, -830, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_cntrl_twr11
pos = 0, -370, 0
rotate = 180, 0, 0
archetype = space_medium_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_habitat01
pos = 140, -1165, 1.5
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau29_03

[Object]
nickname = tau29_03_habitat02
pos = -140, -1165, 1.5
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau29_03

[Object]
nickname = tau29_03_habitat03
pos = 1, -873, 140
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau29_03

[Object]
nickname = tau29_03_habitat04
pos = 1, -873, -140
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau29_03

[Object]
nickname = tau29_03_habitat05
pos = 1, -985, 140
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = tau29_03

[Object]
nickname = tau29_03_habitat06
pos = 1, -985, -140
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = tau29_03

[Object]
nickname = tau29_03_habitat07
pos = -140, -995, 1.5
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = tau29_03

[Object]
nickname = tau29_03_habitat08
pos = 140, -995, 1.5
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = tau29_03

[Object]
nickname = tau29_03_tanks01
pos = -125, -955, -125
rotate = 0, 45, 0
archetype = space_tanks2x2
parent = tau29_03

[Object]
nickname = tau29_03_tanks02
pos = 125, -955, -125
rotate = 0, -45, 0
archetype = space_tanks2x2
parent = tau29_03

[Object]
nickname = tau29_03_tanks03
pos = -125, -955, 125
rotate = 0, -45, 0
archetype = space_tanks2x2
parent = tau29_03

[Object]
nickname = tau29_03_tanks04
pos = 125, -955, 125
rotate = 0, 45, 0
archetype = space_tanks2x2
parent = tau29_03

[Object]
nickname = tau29_03_tanks05
pos = 0, -1155.1, 110
rotate = 0, 0, 90
archetype = space_tanks2x2
parent = tau29_03

[Object]
nickname = tau29_03_tanks06
pos = 0, -1155.1, -110
rotate = 0, 0, 90
archetype = space_tanks2x2
parent = tau29_03

[Object]
nickname = tau29_03_industrial05
pos = 270.75, -830, 0
rotate = 0, 0, 0
archetype = space_industrial01a
parent = tau29_03

[Object]
nickname = tau29_03_industrial06
pos = -270.75, -830, 0
rotate = 0, 0, 0
archetype = space_industrial01a
parent = tau29_03

[Object]
nickname = tau29_03_industrial07
pos = 0, -830, 270.75
rotate = 0, 90, 0
archetype = space_industrial01a
parent = tau29_03

[Object]
nickname = tau29_03_industrial09
pos = 190.95000000000073, -830, 190.95
rotate = 0, -45, 0
archetype = space_industrial01a
parent = tau29_03

[Object]
nickname = tau29_03_industrial08
pos = 0, -830, -270.75
rotate = 0, 90, 0
archetype = space_industrial01a
parent = tau29_03

[Object]
nickname = tau29_03_industrial10
pos = -190.95000000000073, -830, -190.95
rotate = 0, -45, 0
archetype = space_industrial01a
parent = tau29_03

[Object]
nickname = tau29_03_industrial11
pos = 190.95000000000073, -830, -190.95
rotate = 0, 45, 0
archetype = space_industrial01a
parent = tau29_03

[Object]
nickname = tau29_03_industrial12
pos = -190.95000000000073, -830, 190.95
rotate = 0, 45, 0
archetype = space_industrial01a
parent = tau29_03

[Object]
nickname = tau29_03_industrial13
pos = 213.75, -750.1, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial14
pos = -213.75, -750, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial15
pos = 0, -750.1, 213.75
rotate = 0, 90, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial16
pos = 150.75, -750, 150.75
rotate = 0, -45, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial17
pos = 0, -750.1, -213.75
rotate = 0, 90, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial18
pos = -150.75, -750, -150.75
rotate = 0, -45, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial19
pos = 150.75, -750.1, -150.75
rotate = 0, 45, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial20
pos = -150.75, -750, 150.75
rotate = 0, 45, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial21
pos = 285, -955, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = tau29_03

[Object]
nickname = tau29_03_industrial22
pos = -285, -955, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = tau29_03

[Object]
nickname = tau29_03_industrial23
pos = 0, -955, 285
rotate = 0, 90, 0
archetype = space_industrial02a
parent = tau29_03

[Object]
nickname = tau29_03_industrial24
pos = 201, -955, 201
rotate = 0, -45, 0
archetype = space_industrial02a
parent = tau29_03

[Object]
nickname = tau29_03_industrial25
pos = 0, -955, -285
rotate = 0, 90, 0
archetype = space_industrial02a
parent = tau29_03

[Object]
nickname = tau29_03_industrial26
pos = -201, -955, -201
rotate = 0, -45, 0
archetype = space_industrial02a
parent = tau29_03

[Object]
nickname = tau29_03_industrial27
pos = 201, -955, -201
rotate = 0, 45, 0
archetype = space_industrial02a
parent = tau29_03

[Object]
nickname = tau29_03_industrial28
pos = -201, -955, 201
rotate = 0, 45, 0
archetype = space_industrial02a
parent = tau29_03

[Object]
nickname = tau29_03_industrial29
pos = 270.75, -1080, 0
rotate = 0, 0, 0
archetype = space_industrial01a
parent = tau29_03

[Object]
nickname = tau29_03_industrial30
pos = -270.75, -1080, 0
rotate = 0, 0, 0
archetype = space_industrial01a
parent = tau29_03

[Object]
nickname = tau29_03_industrial31
pos = 0, -1080, 270.75
rotate = 0, 90, 0
archetype = space_industrial01a
parent = tau29_03

[Object]
nickname = tau29_03_industrial32
pos = 190.95000000000073, -1080, 190.95
rotate = 0, -45, 0
archetype = space_industrial01a
parent = tau29_03

[Object]
nickname = tau29_03_industrial33
pos = 0, -1080, -270.75
rotate = 0, 90, 0
archetype = space_industrial01a
parent = tau29_03

[Object]
nickname = tau29_03_industrial34
pos = -190.95000000000073, -1080, -190.95
rotate = 0, -45, 0
archetype = space_industrial01a
parent = tau29_03

[Object]
nickname = tau29_03_industrial35
pos = 190.95000000000073, -1080, -190.95
rotate = 0, 45, 0
archetype = space_industrial01a
parent = tau29_03

[Object]
nickname = tau29_03_industrial36
pos = -190.95000000000073, -1080, 190.95
rotate = 0, 45, 0
archetype = space_industrial01a
parent = tau29_03

[Object]
nickname = tau29_03_industrial37
pos = 213.75, -1155.1, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial38
pos = -213.75, -1155, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial39
pos = 0, -1155.1, 213.75
rotate = 0, 90, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial40
pos = 150.75, -1155, 150.75
rotate = 0, -45, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial41
pos = 0, -1155.1, -213.75
rotate = 0, 90, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial42
pos = -150.75, -1155, -150.75
rotate = 0, -45, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial43
pos = 150.75, -1155.1, -150.75
rotate = 0, 45, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial44
pos = -150.75, -1155, 150.75
rotate = 0, 45, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial51
pos = 114, -390, 0
rotate = 0, 0, 0
archetype = space_industrial01b
parent = tau29_03

[Object]
nickname = tau29_03_industrial52
pos = -114, -390, 0
rotate = 0, 0, 0
archetype = space_industrial01b
parent = tau29_03

[Object]
nickname = tau29_03_industrial53
pos = 0, -390, 114
rotate = 0, 90, 0
archetype = space_industrial01b
parent = tau29_03

[Object]
nickname = tau29_03_industrial54
pos = 80.40000000000146, -390, 80.4
rotate = 0, -45, 0
archetype = space_industrial01b
parent = tau29_03

[Object]
nickname = tau29_03_industrial55
pos = 0, -390, -114
rotate = 0, 90, 0
archetype = space_industrial01b
parent = tau29_03

[Object]
nickname = tau29_03_industrial56
pos = -80.40000000000146, -390, -80.4
rotate = 0, -45, 0
archetype = space_industrial01b
parent = tau29_03

[Object]
nickname = tau29_03_industrial57
pos = 80.40000000000146, -390, -80.4
rotate = 0, 45, 0
archetype = space_industrial01b
parent = tau29_03

[Object]
nickname = tau29_03_industrial58
pos = -80.40000000000146, -390, 80.4
rotate = 0, 45, 0
archetype = space_industrial01b
parent = tau29_03

[Object]
nickname = tau29_03_industrial59
pos = 213.75, -9.899999999999977, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial60
pos = -213.75, -10, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial61
pos = 0, -9.899999999999977, 213.75
rotate = 0, 90, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial62
pos = 150.75, -10, 150.75
rotate = 0, -45, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial63
pos = 0, -9.899999999999977, -213.75
rotate = 0, 90, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial64
pos = -150.75, -10, -150.75
rotate = 0, -45, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial65
pos = 150.75, -9.899999999999977, -150.75
rotate = 0, 45, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial66
pos = -150.75, -10, 150.75
rotate = 0, 45, 0
archetype = space_industriala
parent = tau29_03

[Object]
nickname = tau29_03_industrial67
pos = 114, 280, 0
rotate = 0, 0, 0
archetype = space_industrial01b
parent = tau29_03

[Object]
nickname = tau29_03_industrial68
pos = -114, 280, 0
rotate = 0, 0, 0
archetype = space_industrial01b
parent = tau29_03

[Object]
nickname = tau29_03_industrial69
pos = 0, 280, 114
rotate = 0, 90, 0
archetype = space_industrial01b
parent = tau29_03

[Object]
nickname = tau29_03_industrial70
pos = 80.40000000000146, 280, 80.4
rotate = 0, -45, 0
archetype = space_industrial01b
parent = tau29_03

[Object]
nickname = tau29_03_industrial71
pos = 0, 280, -114
rotate = 0, 90, 0
archetype = space_industrial01b
parent = tau29_03

[Object]
nickname = tau29_03_industrial72
pos = -80.40000000000146, 280, -80.4
rotate = 0, -45, 0
archetype = space_industrial01b
parent = tau29_03

[Object]
nickname = tau29_03_industrial73
pos = 80.40000000000146, 280, -80.4
rotate = 0, 45, 0
archetype = space_industrial01b
parent = tau29_03

[Object]
nickname = tau29_03_industrial74
pos = -80.40000000000146, 280, 80.4
rotate = 0, 45, 0
archetype = space_industrial01b
parent = tau29_03

[Object]
nickname = tau29_03_panel_connect01
pos = 0.00999999999839929, -449.99, 0
rotate = 0, 22.5, 0
archetype = hidden_connect
loadout = hidden_head_panels01
parent = tau29_03

[Object]
nickname = tau29_03_panel_connect02
pos = 0, -449.985, 0
rotate = 0, 67.5, 0
archetype = hidden_connect
loadout = hidden_head_panels01
parent = tau29_03

[Object]
nickname = tau29_03_panel_connect03
pos = 0.014999999999417923, -449.99, 0
rotate = 0, 112.5, 0
archetype = hidden_connect
loadout = hidden_head_panels01
parent = tau29_03

[Object]
nickname = tau29_03_panel_connect04
pos = 0, -449.985, 0
rotate = 0, 157.5, 0
archetype = hidden_connect
loadout = hidden_head_panels03
parent = tau29_03

[Object]
nickname = tau29_03_panel_connect05
pos = 0.00999999999839929, -450.01, 0
rotate = 0, 202.5, 0
archetype = hidden_connect
loadout = hidden_head_panels02
parent = tau29_03

[Object]
nickname = tau29_03_panel_connect06
pos = 0.014999999999417923, -450.015, 0
rotate = 0, 247.5, 0
archetype = hidden_connect
loadout = hidden_head_panels01
parent = tau29_03

[Object]
nickname = tau29_03_panel_connect07
pos = 0.014999999999417923, -450.01, 0
rotate = 0, 292.5, 0
archetype = hidden_connect
loadout = hidden_head_panels01
parent = tau29_03

[Object]
nickname = tau29_03_connect01
pos = 0, -260, 0
rotate = 90, 0, 0
archetype = space_airlock_dummy
parent = tau29_03

[Object]
nickname = tau29_03_connect02
pos = 0, 70, 200
rotate = 0, 0, 0
archetype = space_girder
parent = tau29_03

[Object]
nickname = tau29_03_front_cntrl_twr01
pos = 0, 70, 213.75
rotate = 90, 0, 0
archetype = space_small_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_front_cntrl_twr02
pos = 0, 70, 385
rotate = 90, 0, 0
archetype = space_small_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_front_habitat01
pos = -45, 70, 300
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = tau29_03

[Object]
nickname = tau29_03_front_habitat02
pos = 0, 115, 300
rotate = 90, 0, 22.5
archetype = space_habitat_wide
parent = tau29_03

[Object]
nickname = tau29_03_front_habitat03
pos = 0, 25, 300
rotate = 90, 0, 22.5
archetype = space_habitat_wide
parent = tau29_03

[Object]
nickname = tau29_03_front_habitat04
pos = 0, 70, 300
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = tau29_03

[Object]
nickname = tau29_03_front_habitat05
pos = 45, 70, 300
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = tau29_03

[Object]
nickname = tau29_03_front_habitat06
pos = -45, 70, 470
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = tau29_03

[Object]
nickname = tau29_03_front_habitat07
pos = 0, 70, 470
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = tau29_03

[Object]
nickname = tau29_03_front_habitat08
pos = 45, 70, 470
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = tau29_03

[Object]
nickname = tau29_03_front_habitat09
pos = 0, 25, 470
rotate = 90, 0, 22.5
archetype = space_habitat_wide
parent = tau29_03

[Object]
nickname = tau29_03_front_habitat10
pos = 0, 70, 585
rotate = 90, 0, 0
archetype = space_habitat_tall
parent = tau29_03

[Object]
nickname = tau29_03_LEFT_industrial01
pos = -175, -512, 0
rotate = 0, 90, 30
archetype = space_industrial01a
parent = tau29_03

[Object]
nickname = tau29_03_LEFT_habitat01
pos = -355, -615, 0
rotate = 90, 90, 30
archetype = space_habitat_wide
parent = tau29_03

[Object]
nickname = tau29_03_LEFT_habitat02
pos = -478, -688, 0
rotate = 90, 90, 30
archetype = space_habitat_wide
parent = tau29_03

[Object]
nickname = tau29_03_LEFT_cntrl_twr01
pos = -600, -757, 0
rotate = 90, 0, 120
archetype = space_small_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_LEFT_tanks01
pos = -732, -700, 0
rotate = 90, 90, 50
archetype = space_tanks4
parent = tau29_03

[Object]
nickname = tau29_03_LEFT_tanks02
pos = -610, -900, 0
rotate = -90, 90, 192
archetype = space_tanks4
parent = tau29_03

[Object]
nickname = tau29_03_LEFT_tanks03
pos = -720, -827, 0
rotate = 90, 0, 120
archetype = space_tanks4x4
parent = tau29_03

[Object]
nickname = tau29_03_RIGHT_industrial01
pos = 175, -512, 0
rotate = 0, 90, -30
archetype = space_industrial01a
parent = tau29_03

[Object]
nickname = tau29_03_RIGHT_habitat01
pos = 355, -615, 0
rotate = 90, 90, -30
archetype = space_habitat_wide
parent = tau29_03

[Object]
nickname = tau29_03_RIGHT_habitat02
pos = 478, -688, 0
rotate = 90, 90, -30
archetype = space_habitat_wide
parent = tau29_03

[Object]
nickname = tau29_03_RIGHT_cntrl_twr01
pos = 600, -757, 0
rotate = 90, 0, 60
archetype = space_small_control_tower
parent = tau29_03

[Object]
nickname = tau29_03_RIGHT_tanks01
pos = 732, -700, 0
rotate = 90, 90, 131
archetype = space_tanks4
parent = tau29_03

[Object]
nickname = tau29_03_RIGHT_tanks02
pos = 610, -900, 0
rotate = 90, 90, 169
archetype = space_tanks4
parent = tau29_03

[Object]
nickname = tau29_03_RIGHT_tanks03
pos = 720, -827, 0
rotate = 90, 0, -120
archetype = space_tanks4x4
parent = tau29_03
'''