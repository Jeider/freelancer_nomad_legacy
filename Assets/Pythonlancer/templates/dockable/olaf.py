from templates.space_object_template import SpaceObjectTemplate


class OlafOriginal(SpaceObjectTemplate):
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
nickname = olaf_panel_connect08
pos = -0.1, -450.015, 0
rotate = 0, 337.5, 0
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

class Olaf(OlafOriginal):
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
pos = 0, -500, 150
rotate = 0, 0, 0
archetype = batch_olaf_structure0
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
nickname = olaf_panel_connect08
pos = -0.1, -450.015, 0
rotate = 0, 337.5, 0
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
nickname = tau29_03_LEFT_industrial01
pos = -453.5, -706, 0
rotate = 0, 0, 0
archetype = batch_olaf_left0
parent = tau29_03

[Object]
nickname = tau29_03_RIGHT_industrial01
pos = 453.5, -706, 0
rotate = 0, 0, 0
archetype = batch_olaf_right0
parent = tau29_03



[Object]
nickname = tau29_03_col_structure0_collision00
pos = -3.81469727e-06, 263.139271, 2.23675705e-05
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision00
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision01
pos = -0.043510437, 189.850012, 0.00915527344
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision01
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision02
pos = 6.79901886, 189.850012, 0.00915527344
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision02
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision03
pos = -0.271690369, 70.2159357, 1.30706024
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision03
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision04
pos = -0.271690369, 0.215935707, 1.30706024
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision04
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision05
pos = -0.271690369, -139.784064, 1.30706024
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision05
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision06
pos = -0.271690369, -197.385581, 1.30706024
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision06
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision07
pos = -0.271690369, -831.30706, 360.215936
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision07
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision08
pos = -0.271690369, -1081.30706, 360.215936
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision08
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision09
pos = -0.271690369, -548.69294, 236.784065
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision09
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision10
pos = 141.30706, -1079.78406, 1.77169037
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision10
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision11
pos = -138.69294, -1079.78406, 1.77169037
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision11
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision12
pos = 141.30706, -1259.78406, 1.77169037
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision12
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision13
pos = 139.72831, -1289.78406, 2.80706024
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision13
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision14
pos = -138.69294, -1259.78406, 1.77169037
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision14
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision15
pos = -11.6423643, -1189.83136, 2.80706024
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision15
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision16
pos = 0.728309631, -954.784064, 141.30706
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision16
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision17
pos = 0.728309631, -954.784064, -12.4443741
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision17
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision18
pos = -0.0679855347, -830.149987, 0.0143051147
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision18
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision19
pos = -0.0679779053, -830.149987, 0.0143051147
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision19
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision20
pos = -0.043510437, -369.85001, -0.00915618704
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision20
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision21
pos = 6.79901886, -369.850011, -0.00915618704
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision21
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision22
pos = 0.202747345, -1000.64645, 0.0919694901
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision22
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision23
pos = 95.5867599, -830.182335, 198.568069
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision23
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision24
pos = -95.6679869, -830.182335, -198.868724
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision24
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision25
pos = -0.0979101615, -830.182335, -0.0927689248
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision25
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision26
pos = 213.737232, -749.8775, 1.76407623
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision26
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision27
pos = -213.762768, -749.7775, 1.76407623
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision27
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision28
pos = 1.76407622, -749.8775, 213.762768
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision28
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision29
pos = 149.5722, -749.7775, 151.746596
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision29
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision30
pos = 1.76407622, -749.8775, -213.737232
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision30
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision31
pos = -151.9278, -749.7775, -149.753404
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision31
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision32
pos = 151.746596, -749.8775, -149.5722
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision32
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision33
pos = -149.753404, -749.7775, 151.9278
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision33
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision34
pos = 285.269512, -955.158897, -0.501350403
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision34
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision35
pos = -284.730488, -955.158897, -0.501350403
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision35
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision36
pos = -0.501350814, -955.158897, 284.730488
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision36
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision37
pos = 201.236962, -955.158897, 200.625018
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision37
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision38
pos = -0.501350814, -955.158897, -285.269512
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision38
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision39
pos = -200.763038, -955.158897, -201.374982
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision39
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision40
pos = 200.625018, -955.158897, -201.236962
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision40
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision41
pos = -201.374982, -955.158897, 200.763038
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision41
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision42
pos = 0.202747345, -1080.18233, -0.173995972
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision42
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision43
pos = 95.5867599, -1080.18233, 198.568069
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision43
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision44
pos = -95.6679869, -1080.18233, -198.868724
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision44
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision45
pos = -0.0979101615, -1080.18233, -0.0927689248
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision45
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision46
pos = 213.737232, -1154.8775, 1.76407623
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision46
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision47
pos = -213.762768, -1154.7775, 1.76407623
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision47
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision48
pos = 1.76407622, -1154.8775, 213.762768
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision48
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision49
pos = 149.5722, -1154.7775, 151.746596
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision49
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision50
pos = 1.76407622, -1154.8775, -213.737232
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision50
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision51
pos = -151.9278, -1154.7775, -149.753404
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision51
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision52
pos = 151.746596, -1154.8775, -149.5722
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision52
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision53
pos = -60.0303766, -792.376203, 107.062413
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision53
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision54
pos = -5.67471081, -389.877813, 46.0904199
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision54
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision55
pos = -0.15289798, -389.877813, -84.6764294
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision55
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision56
pos = 75.3647627, -179.729111, 4.01300704
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision56
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision57
pos = -213.762768, -9.77750015, 1.76407623
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision57
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision58
pos = 1.76407622, -9.67750015, 213.762768
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision58
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision59
pos = 149.5722, -9.77750015, 151.746596
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision59
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision60
pos = 1.76407622, -9.67750015, -213.737232
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision60
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision61
pos = -151.9278, -9.77750015, -149.753404
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision61
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision62
pos = 151.746596, -9.67750015, -149.5722
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision62
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision63
pos = -60.0303766, 115.123797, 107.062413
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision63
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision64
pos = -5.67471081, 280.122187, 46.0904199
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision64
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision65
pos = -0.15289798, 280.122187, -84.6764294
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision65
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision66
pos = -28.1187387, 149.24869, 200.067322
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision66
parent = tau29_03

[Object]
nickname = tau29_03_col_structure0_collision67
pos = -0.271690369, 68.6929398, 474.211246
rotate = 0, 0, 0
archetype = batch_olaf_structure0_collision67
parent = tau29_03

[Object]
nickname = tau29_03_col_left0_collision00
pos = -420.891673, -681.026955, -0.00231693952
rotate = 0, 0, 0
archetype = batch_olaf_left0_collision00
parent = tau29_03

[Object]
nickname = tau29_03_col_right0_collision00
pos = 420.721321, -680.658073, -0.00231693952
rotate = 0, 0, 0
archetype = batch_olaf_right0_collision00
parent = tau29_03

'''
