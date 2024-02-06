from templates.space_object_template import SpaceObjectTemplate


class Tortuga(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'OM2_01'
    TEMPLATE = '''[Object]
nickname = OM2_01
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = prison
dock_with = om2_01_base
base = om2_01_base
loadout = prison_co
ids_name = 203856
ids_info = 065767
behavior = NOTHING
reputation = pi_grp
voice = atc_leg_m01
space_costume = li_rockford_head, sh_male2_body, prop_hat_male_pirate_a, prop_neuralnet_d

[Object]
nickname = OM2_01_CORE
pos = 1312, 60, -200
rotate = 0, 90, 0
archetype = co_large_asteroid
parent = OM2_01


[Object]
nickname = OM2_01_EXIT_industrial01
pos = 792, -190, 0
rotate = 0, 90, 0
archetype = space_industrial01a
parent = OM2_01

[Object]
nickname = OM2_01_EXIT_industrial02
pos = 1632, -70, -550
rotate = 0, -45, 0
archetype = space_industrial01a
parent = OM2_01

[Object]
nickname = OM2_01_EXIT_industrial03
pos = 1452, 340, 360
rotate = 0, 0, 0
archetype = space_industrial01a
parent = OM2_01

[Object]
nickname = OM2_01_EXIT_industrial04
pos = 1632, 110, -550
rotate = 0, -45, 0
archetype = space_industrial02a
parent = OM2_01

[Object]
nickname = OM2_01_EXIT_industrial05
pos = 1452, 470, 360
rotate = 0, 0, 0
archetype = space_industrial02a
parent = OM2_01

[Object]
nickname = OM2_01_asteroid01
pos = 1452, 180, 1055
rotate = 0, 90, 0
archetype = co_medium_asteroid01
parent = OM2_01

[Object]
nickname = OM2_01_asteroid02
pos = 100, 0, 0
rotate = 0, -30, 0
archetype = co_medium_asteroid01
parent = OM2_01

[Object]
nickname = OM2_01_asteroid03
pos = 1412, -240, -1400
rotate = 0, 80, 0
archetype = co_medium_asteroid01
parent = OM2_01

[Object]
nickname = OM2_01_asteroid04
pos = 2182, -20, -1100
rotate = 180, -90, 0
archetype = co_medium_asteroid02
parent = OM2_01

[Object]
nickname = OM2_01_asteroid05
pos = 612, 115, 800
rotate = 0, -60, 0
archetype = co_medium_asteroid02
parent = OM2_01

[Object]
nickname = OM2_01_asteroid06
pos = 2262, -40, 605
rotate = 0, 30, 0
archetype = co_medium_asteroid02
parent = OM2_01

[Object]
nickname = OM2_01_asteroid07
pos = 2672, -40, -300
rotate = 0, 90, 0
archetype = co_medium_asteroid01
parent = OM2_01

[Object]
nickname = OM2_01_girder01
pos = 1452, 260, 630
rotate = 30, 0, 0
archetype = space_girder
parent = OM2_01

[Object]
nickname = OM2_01_girder02
pos = 1452, 235, 630
rotate = 30, 0, 0
archetype = space_girder
parent = OM2_01

[Object]
nickname = OM2_01_girder03
pos = 512, -105, 0
rotate = 30, 90, 0
archetype = space_girder
parent = OM2_01

[Object]
nickname = OM2_01_girder04
pos = 512, -80, 0
rotate = 30, 90, 0
archetype = space_girder
parent = OM2_01

[Object]
nickname = OM2_01_girder05
pos = 1832, -45, -750
rotate = 10, -45, 0
archetype = space_girder
parent = OM2_01

[Object]
nickname = OM2_01_girder06
pos = 1832, -25, -750
rotate = 10, -45, 0
archetype = space_girder
parent = OM2_01

[Object]
nickname = OM2_01_girder07
pos = 1832, -65, -750
rotate = 10, -45, 0
archetype = space_girder
parent = OM2_01

[Object]
nickname = OM2_01_girder08
pos = 999, 155, 971
rotate = -8, 75, 0
archetype = space_girder
parent = OM2_01

[Object]
nickname = OM2_01_girder09
pos = 322, 50, 475
rotate = -15, 30, 0
archetype = space_girder
parent = OM2_01

[Object]
nickname = OM2_01_girder10
pos = 1862, 92, 914
rotate = 30, 120, 0
archetype = space_girder
parent = OM2_01

[Object]
nickname = OM2_01_girder11
pos = 2544, -40, 170
rotate = 0, -30, 0
archetype = space_girder
parent = OM2_01

[Object]
nickname = OM2_01_girder12
pos = 2529, -40, -762
rotate = 0, 30, 0
archetype = space_girder
parent = OM2_01

[Object]
nickname = OM2_01_girder13
pos = 1857, -130, -1274
rotate = -30, 75, 0
archetype = space_girder
parent = OM2_01

[Object]
nickname = OM2_01_industrial01
pos = 1452, 180, 905
rotate = 0, 0, 0
archetype = space_industrial01a
parent = OM2_01

[Object]
nickname = OM2_01_industrial02
pos = 240, 0, 0
rotate = 0, 90, 0
archetype = space_industrial01a
parent = OM2_01

[Object]
nickname = OM2_01_industrial03
pos = 2032, -20, -950
rotate = 0, -45, 0
archetype = space_industrial01a
parent = OM2_01

[Object]
nickname = OM2_01_industrial04
pos = 162, 0, 200
rotate = 0, 30, 0
archetype = space_industrial01a
parent = OM2_01

[Object]
nickname = OM2_01_industrial05
pos = 1312, 180, 1055
rotate = 0, 75, 0
archetype = space_industrial01a
parent = OM2_01

[Object]
nickname = OM2_01_industrial06
pos = 712, 133, 895
rotate = 0, 75, 0
archetype = space_industrial01a
parent = OM2_01

[Object]
nickname = OM2_01_industrial07
pos = 462, 90, 720
rotate = 0, 30, 0
archetype = space_industrial01a
parent = OM2_01

[Object]
nickname = OM2_01_industrial08
pos = 1612, 180, 1055
rotate = 0, 120, 0
archetype = space_industrial01a
parent = OM2_01

[Object]
nickname = OM2_01_industrial09
pos = 2112, 3, 770
rotate = 0, 120, 0
archetype = space_industrial01a
parent = OM2_01

[Object]
nickname = OM2_01_industrial10
pos = 2382, -40, 450
rotate = 0, -30, 0
archetype = space_industrial01a
parent = OM2_01

[Object]
nickname = OM2_01_industrial11
pos = 2697, -40, -95
rotate = 0, -30, 0
archetype = space_industrial01a
parent = OM2_01

[Object]
nickname = OM2_01_industrial12
pos = 2692, -40, -480
rotate = 0, 30, 0
archetype = space_industrial01a
parent = OM2_01

[Object]
nickname = OM2_01_industrial13
pos = 2367, -40, -1040
rotate = 0, 30, 0
archetype = space_industrial01a
parent = OM2_01

[Object]
nickname = OM2_01_industrial14
pos = 2137, -40, -1200
rotate = 0, 75, 0
archetype = space_industrial01a
parent = OM2_01

[Object]
nickname = OM2_01_industrial15
pos = 1572, -220, -1350
rotate = 0, 75, 0
archetype = space_industrial01a
parent = OM2_01

[Object]
nickname = OM2_01_industrial16
pos = 1272, -220, -1350
rotate = 0, -60, 0
archetype = space_industrial01a
parent = OM2_01

[Object]
nickname = OM2_01_industrial17
pos = 80, 0, -150
rotate = 0, -15, 0
archetype = space_industrial01a
parent = OM2_01

[Object]
nickname = OM2_01_beam_dmg01
pos = 1042, -220, -1215
rotate = 0, -60, 0
archetype = space_beaml_dmg
parent = OM2_01

[Object]
nickname = OM2_01_beam_dmg02
pos = 147, -25, -400
rotate = 0, -15, 0
archetype = space_beaml_dmg
parent = OM2_01

[Object]
nickname = OM2_01_industrial_dmg01
pos = 732, -182, -1035
rotate = 0, 120, 0
archetype = space_industrial_dmg
parent = OM2_01

[Object]
nickname = OM2_01_GUN01_cntrl_twr01
pos = 1452, 380, 1055
rotate = 180, 45, 0
archetype = space_control_tower
parent = OM2_01

[Object]
nickname = OM2_01_GUN01_girder01
pos = 1512, 510, 1010
rotate = 45, 0, 0
archetype = space_girder
parent = OM2_01

[Object]
nickname = OM2_01_GUN01_girder02
pos = 1392, 510, 1010
rotate = 45, 0, 0
archetype = space_girder
parent = OM2_01

[Object]
nickname = OM2_01_GUN01_girder03
pos = 1452, 640, 1100
rotate = 0, 0, 0
archetype = space_girder
parent = OM2_01

[Object]
nickname = OM2_01_GUN01_industrial01
pos = 1452, 390, 1055
rotate = -90, 0, 0
archetype = space_industriala
parent = OM2_01

[Object]
nickname = OM2_01_GUN01_industrial02
pos = 1452, 640, 880
rotate = 0, 0, 0
archetype = space_industriala
parent = OM2_01

[Object]
nickname = OM2_01_GUN01_industrial03
pos = 1452, 640, 1305
rotate = 180, 0, 0
archetype = space_industrial01c
parent = OM2_01

[Object]
nickname = OM2_01_GUN01_industrial04
pos = 1452, 640, 1270
rotate = 180, 0, 0
archetype = space_industrial01c
parent = OM2_01

[Object]
nickname = OM2_01_GUN01_industrial05
pos = 1452, 640, 1230
rotate = 0, 0, 0
archetype = space_industrial01c
parent = OM2_01

[Object]
nickname = OM2_01_GUN01_industrial06
pos = 1452, 130, 1190
rotate = -55, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = OM2_01

[Object]
nickname = OM2_01_GUN02_cntrl_twr01
pos = 2182, 140, -1100
rotate = 180, 45, 0
archetype = space_control_tower
parent = OM2_01

[Object]
nickname = OM2_01_GUN02_girder01
pos = 2242, 270, -1050
rotate = 45, 180, 0
archetype = space_girder
parent = OM2_01

[Object]
nickname = OM2_01_GUN02_girder02
pos = 2122, 270, -1050
rotate = 45, 180, 0
archetype = space_girder
parent = OM2_01

[Object]
nickname = OM2_01_GUN02_girder03
pos = 2182, 400, -1150
rotate = 0, 0, 0
archetype = space_girder
parent = OM2_01

[Object]
nickname = OM2_01_GUN02_industrial01
pos = 2182, 150, -1100
rotate = -90, 0, 0
archetype = space_industriala
parent = OM2_01

[Object]
nickname = OM2_01_GUN02_industrial02
pos = 2182, 400, -922
rotate = 0, 0, 0
archetype = space_industriala
parent = OM2_01

[Object]
nickname = OM2_01_GUN02_industrial03
pos = 2182, 400, -1360
rotate = 0, 0, 0
archetype = space_industrial01c
parent = OM2_01

[Object]
nickname = OM2_01_GUN02_industrial04
pos = 2182, 400, -1325
rotate = 0, 0, 0
archetype = space_industrial01c
parent = OM2_01

[Object]
nickname = OM2_01_GUN02_industrial05
pos = 2182, 400, -1285
rotate = 180, 0, 0
archetype = space_industrial01c
parent = OM2_01

[Object]
nickname = OM2_01_GUN02_industrial06
pos = 2182, -120, -1100
rotate = 0, 60, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = OM2_01

[Object]
nickname = OM2_01_HILL01_cntrl_tower01
pos = 2672, 260, -300
rotate = 180, 0, 0
archetype = space_control_tower
parent = OM2_01

[Object]
nickname = OM2_01_HILL01_cntrl_tower02
pos = 2672, -210, -300
rotate = 0, 0, 0
archetype = space_control_tower
parent = OM2_01

[Object]
nickname = OM2_01_HILL01_cntrl_tower03
pos = 2772, -420, -250
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = OM2_01

[Object]
nickname = OM2_01_HILL01_cntrl_tower04
pos = 2572, -290, -350
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = OM2_01

[Object]
nickname = OM2_01_HILL01_habitat01
pos = 2672, 175, -170
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = OM2_01

[Object]
nickname = OM2_01_HILL01_habitat02
pos = 2792, 180, -300
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = OM2_01

[Object]
nickname = OM2_01_HILL01_habitat03
pos = 2552, 180, -300
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = OM2_01

[Object]
nickname = OM2_01_HILL01_habitat04
pos = 2672, 180, -400
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = OM2_01

[Object]
nickname = OM2_01_HILL01_habitat05
pos = 2572, -290, -350
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = OM2_01

[Object]
nickname = OM2_01_HILL01_habitat06
pos = 2772, -360, -250
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = OM2_01

[Object]
nickname = OM2_01_HILL01_dome01
pos = 2672, 310, -300
rotate = 0, 0, 0
archetype = space_domea
parent = OM2_01

[Object]
nickname = OM2_01_HILL01_dome02
pos = 2572, -355, -350
rotate = 180, 0, 0
archetype = space_domea
parent = OM2_01

[Object]
nickname = OM2_01_HILL02_cntrl_tower01
pos = 612, 255, 800
rotate = 180, 0, 0
archetype = space_control_tower
parent = OM2_01

[Object]
nickname = OM2_01_HILL02_cntrl_tower02
pos = 512, -120, 830
rotate = 0, 0, 0
archetype = space_control_tower
parent = OM2_01

[Object]
nickname = OM2_01_HILL02_cntrl_tower03
pos = 512, 340, 750
rotate = 0, -60, 0
archetype = space_small_control_tower
parent = OM2_01

[Object]
nickname = OM2_01_HILL02_cntrl_tower04
pos = 712, 408, 700
rotate = 0, 30, 0
archetype = space_small_control_tower
parent = OM2_01

[Object]
nickname = OM2_01_HILL02_habitat01
pos = 512, 340, 750
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = OM2_01

[Object]
nickname = OM2_01_HILL02_habitat02
pos = 712, 408, 700
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = OM2_01

[Object]
nickname = OM2_01_HILL02_habitat03
pos = 612, -40, 800
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = OM2_01

[Object]
nickname = OM2_01_HILL02_habitat04
pos = 512, -40, 700
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = OM2_01

[Object]
nickname = OM2_01_HILL02_habitat05
pos = 562, -40, 950
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = OM2_01

[Object]
nickname = OM2_01_HILL02_habitat06
pos = 412, -40, 850
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = OM2_01

[Object]
nickname = OM2_01_HILL02_dome01
pos = 512, 440, 750
rotate = 0, 0, 0
archetype = space_domea
parent = OM2_01

[Object]
nickname = OM2_01_HILL02_dome02
pos = 512, -170, 830
rotate = 180, 0, 0
archetype = space_domea
parent = OM2_01

[Object]
nickname = OM2_01_STORE01_habitat01
pos = 1412, 20, -1400
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = OM2_01

[Object]
nickname = OM2_01_STORE01_habitat02
pos = 1562, -435, -1400
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = OM2_01

[Object]
nickname = OM2_01_STORE01_habitat03
pos = 1267, -435, -1400
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = OM2_01

[Object]
nickname = OM2_01_STORE01_cntrl_twr01
pos = 1412, 115, -1400
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = OM2_01

[Object]
nickname = OM2_01_STORE01_cntrl_twr02
pos = 1562, -460, -1400
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = OM2_01

[Object]
nickname = OM2_01_STORE01_cntrl_twr03
pos = 1267, -460, -1400
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = OM2_01

[Object]
nickname = OM2_01_STORE01_tanks01
pos = 1412, 180, -1400
rotate = 180, 0, 0
archetype = space_tanksx4
parent = OM2_01

[Object]
nickname = OM2_01_STORE01_tanks02
pos = 1557, 74, -1400
rotate = 0, 90, 0
archetype = space_tanks4
parent = OM2_01

[Object]
nickname = OM2_01_STORE01_tanks03
pos = 1267, 74, -1400
rotate = 0, 90, 0
archetype = space_tanks4
parent = OM2_01

[Object]
nickname = OM2_01_STORE01_tanks04
pos = 1416, -460, -1400
rotate = 90, 20, 90
archetype = space_tanks4x4
parent = OM2_01

[Object]
nickname = OM2_01_STORE01_tanks05
pos = 1416, -460, -1400
rotate = 90, -30, 90
archetype = space_tanks4x4
parent = OM2_01

[Object]
nickname = OM2_01_STORE02_habitat01
pos = 2212, 160, 585
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = OM2_01

[Object]
nickname = OM2_01_STORE02_habitat02
pos = 2112, -230, 605
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = OM2_01

[Object]
nickname = OM2_01_STORE02_habitat03
pos = 2402, -230, 605
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = OM2_01

[Object]
nickname = OM2_01_STORE02_cntrl_twr01
pos = 2212, 250, 585
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = OM2_01

[Object]
nickname = OM2_01_STORE02_cntrl_twr02
pos = 2112, -285, 605
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = OM2_01

[Object]
nickname = OM2_01_STORE02_cntrl_twr03
pos = 2402, -285, 605
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = OM2_01

[Object]
nickname = OM2_01_STORE02_tanks01
pos = 2212, 310, 585
rotate = 180, 0, 0
archetype = space_tanksx4
parent = OM2_01

[Object]
nickname = OM2_01_STORE02_tanks02
pos = 2067, 210, 585
rotate = 0, 90, 0
archetype = space_tanks4
parent = OM2_01

[Object]
nickname = OM2_01_STORE02_tanks03
pos = 2357, 210, 585
rotate = 0, 90, 0
archetype = space_tanks4
parent = OM2_01

[Object]
nickname = OM2_01_STORE02_tanks04
pos = 2257, -285, 605
rotate = 90, 0, 90
archetype = space_tanks4x4
parent = OM2_01

[Object]
nickname = OM2_01_STORE02_tanks05
pos = 2257, -285, 605
rotate = 90, 90, 90
archetype = space_tanks4x4
parent = OM2_01
'''