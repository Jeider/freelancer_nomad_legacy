from templates.space_object_template import SpaceObjectTemplate


class BretoniaRoidMining(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'tau37_01'
    TEMPLATE = '''[Object]
nickname = tau37_01
ids_name = 203707
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = space_shipping01
ids_info = 065624
dock_with = tau37_01_base
base = tau37_01_Base
reputation = br_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = pl_male7_head, pl_male2_peasant_body, prop_neuralnet_b
difficulty_level = 13
loadout = space_shipping_tau37
pilot = pilot_solar_hardest

[Object]
nickname = tau37_01_research01
pos = -926, -323, 0
rotate = 0, 0, 0
archetype = space_research
parent = tau37_01

[Object]
nickname = tau37_01_industrial01
pos = -926, -323, 350
rotate = 0, -90, 0
archetype = space_industrial
parent = tau37_01

[Object]
nickname = tau37_01_industrial02
pos = -926, -323, 900
rotate = 0, -90, 0
archetype = space_industrial
parent = tau37_01

[Object]
nickname = tau37_01_industrial03
pos = -926, -323, 1450
rotate = 0, -90, 0
archetype = space_industrial
parent = tau37_01

[Object]
nickname = tau37_01_industrial04
pos = -576, -323, 350
rotate = 90, 0, 0
archetype = space_industrial02a
parent = tau37_01

[Object]
nickname = tau37_01_industrial05
pos = -596, -323, 900
rotate = 90, 0, 0
archetype = space_industrial02a
parent = tau37_01

[Object]
nickname = tau37_01_industrial06
pos = -616, -323, 1450
rotate = 90, 0, 0
archetype = space_industrial02a

[Object]
nickname = tau37_01_girder01
pos = -776, -323, 350
rotate = 0, 90, 0
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder02
pos = -776, -323, 900
rotate = 0, 90, 0
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder03
pos = -776, -323, 1450
rotate = 0, 90, 0
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder04
pos = -798, -133, 0
rotate = -45, 90, 0
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder05
pos = -641, -73, 0
rotate = 90, 0, 0
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder06
pos = -786, -503, 0
rotate = 40, 90, 0
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder07
pos = -841, -323, 0
rotate = 0, 90, 0
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder08
pos = -641, -443, 0
rotate = 90, 0, 0
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder09
pos = 561, -473, 0
rotate = 90, 0, 0
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder10
pos = -276, -323, 0
rotate = 90, 45, 90
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder11
pos = -276, -625, 0
rotate = 90, 45, 90
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder12
pos = 174, -323, 0
rotate = 90, 45, 90
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_girder13
pos = 174, -625, 0
rotate = 90, 45, 90
archetype = space_girder
parent = tau37_01

[Object]
nickname = tau37_01_shipyard01
pos = -436, -323, 350
rotate = 90, 90, 0
archetype = shipyard
parent = tau37_01

[Object]
nickname = tau37_01_shipyard02
pos = -456, -323, 900
rotate = 90, 90, 0
archetype = shipyard
parent = tau37_01

[Object]
nickname = tau37_01_shipyard03
pos = -476, -323, 1450
rotate = 90, 90, 0
archetype = shipyard
parent = tau37_01

[Object]
nickname = tau37_01_solar_plant01
pos = -1376, -323, 350
rotate = 0, 0, 0
archetype = space_solar_plant
parent = tau37_01
spin = 0.1, 0, 0

[Object]
nickname = tau37_01_solar_plant02
pos = -1396, -323, 900
rotate = 0, 0, 0
archetype = space_solar_plant
parent = tau37_01
spin = 0.1, 0, 0

[Object]
nickname = tau37_01_solar_plant03
pos = -1416, -323, 1450
rotate = 0, 0, 0
archetype = space_solar_plant
parent = tau37_01
spin = 0.1, 0, 0

[Object]
nickname = tau37_01_tanks01
pos = -561, -625, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks02
pos = -430, -625, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks03
pos = 26, -625, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks04
pos = 350, -625, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks05
pos = 481, -625, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks06
pos = -561, -323, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks07
pos = -430, -323, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks08
pos = 26, -323, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks09
pos = 350, -323, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks10
pos = 481, -323, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks11
pos = -106, -323, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanks12
pos = -106, -625, 0
rotate = 90, 60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA01
pos = -561, -625, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA02
pos = -430, -625, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA03
pos = 26, -625, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA04
pos = 350, -625, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA05
pos = 481, -625, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA06
pos = -561, -323, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA07
pos = -430, -323, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA08
pos = 26, -323, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA09
pos = 350, -323, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA10
pos = 481, -323, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA11
pos = -106, -323, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_tanksA12
pos = -106, -625, 0
rotate = 90, -60, 90
archetype = space_tanks4x4
parent = tau37_01

[Object]
nickname = tau37_01_habitat01
pos = -926, -93, 350
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = tau37_01

[Object]
nickname = tau37_01_habitat02
pos = -926, -3, -100
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = tau37_01

[Object]
nickname = tau37_01_habitat03
pos = -926, -118, 1450
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = tau37_01

[Object]
nickname = tau37_01_habitat04
pos = -926, -181, 350
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau37_01

[Object]
nickname = tau37_01_habitat05
pos = -926, -181, 900
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau37_01

[Object]
nickname = tau37_01_habitat06
pos = -926, -553, 350
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = tau37_01

[Object]
nickname = tau37_01_habitat07
pos = -926, -643, 900
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = tau37_01

[Object]
nickname = tau37_01_habitat08
pos = -926, -528, 1450
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = tau37_01

[Object]
nickname = tau37_01_habitat09
pos = -926, -465, 350
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = tau37_01

[Object]
nickname = tau37_01_habitat10
pos = -926, -465, 900
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = tau37_01
'''


class RheinlandRoidMining(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'om15_01'
    TEMPLATE = '''[Object]
nickname = om15_01
ids_name = 203639
pos = 0, 0, 0
rotate = 0,180, 0
archetype = space_shipping01
ids_info = 065563
dock_with = om15_01_base
base = om15_01_Base
reputation = rh_grp
behavior = NOTHING
voice = atc_leg_f01
space_costume = rh_newscaster_head_gen_hat, pl_female2_peasant_body, prop_hat_female_miner, prop_neuralnet_b_right
difficulty_level = 13
loadout = space_shipping_rh
pilot = pilot_solar_hardest

[Object]
nickname = om15_01_research01
pos = -1035, -300, 0
rotate = 0, 0, 0
archetype = space_research
parent = om15_01

[Object]
nickname = om15_01_research02
pos = -735, -300, 0
rotate = 0, 0, 0
archetype = space_research
parent = om15_01

[Object]
nickname = om15_01_research03
pos = -735, 0, 0
rotate = 0, 0, 0
archetype = space_research
parent = om15_01

[Object]
nickname = om15_01_girder01
pos = -885, -300, 0
rotate = 0, 90, 0
archetype = space_girder
parent = om15_01

[Object]
nickname = om15_01_girder02
pos = -735, -150, 0
rotate = 90, 0, 0
archetype = space_girder
parent = om15_01

[Object]
nickname = om15_01_girder03
pos = -915, -120, 0
rotate = 90, 0, -45
archetype = space_girder
parent = om15_01

[Object]
nickname = om15_01_girder04
pos = -885, -300, 1800
rotate = 0, 90, 0
archetype = space_girder
parent = om15_01

[Object]
nickname = om15_01_girder05
pos = -735, -150, 1800
rotate = 90, 0, 0
archetype = space_girder
parent = om15_01

[Object]
nickname = om15_01_girder06
pos = -915, -120, 1800
rotate = 90, 0, -45
archetype = space_girder
parent = om15_01

[Object]
nickname = om15_01_industrial01
pos = -315, -300, 0
rotate = 0, -90, 0
archetype = space_industrial
parent = om15_01

[Object]
nickname = om15_01_industrial02
pos = 35, -300, 0
rotate = 0, -90, 0
archetype = space_industrial
parent = om15_01

[Object]
nickname = om15_01_industrial03
pos = 385, -300, 0
rotate = 0, -90, 0
archetype = space_industrial
parent = om15_01

[Object]
nickname = om15_01_tankl_01
pos = -315, -300, 200
rotate = 0, 0, 0
archetype = space_tankl4
parent = om15_01

[Object]
nickname = om15_01_tankl_02
pos = -315, -300, -200
rotate = 0, 0, 0
archetype = space_tankl4
parent = om15_01

[Object]
nickname = om15_01_tankl_03
pos = 385, -300, 200
rotate = 0, 0, 0
archetype = space_tankl4
parent = om15_01

[Object]
nickname = om15_01_tankl_04
pos = 35, -300, -200
rotate = 0, 0, 0
archetype = space_tankl4
parent = om15_01

[Object]
nickname = om15_01_tankl_05
pos = 35, -300, 200
rotate = 0, 0, 0
archetype = space_tankl4
parent = om15_01

[Object]
nickname = om15_01_tankl_06
pos = 385, -300, -200
rotate = 0, 0, 0
archetype = space_tankl4
parent = om15_01

[Object]
nickname = om15_01_industrial04
pos = -1155, 0, 0
rotate = 0, 90, 0
archetype = space_industrial02
parent = om15_01

[Object]
nickname = om15_01_industrial05
pos = -1155, 0, 1800
rotate = 0, 90, 0
archetype = space_industrial02
parent = om15_01

[Object]
nickname = om15_01_space_dome01
pos = -1155, 30, 350
rotate = 0, 180, 0
archetype = space_dome
parent = om15_01

[Object]
nickname = om15_01_space_dome02
pos = -1155, 30, 1450
rotate = 0, 0, 0
archetype = space_dome
parent = om15_01

[Object]
nickname = om15_01_habitat01
pos = -1155, 350, 0
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = om15_01

[Object]
nickname = om15_01_habitat02
pos = -1155, 230, 1800
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = om15_01

[Object]
nickname = om15_01_habitat03
pos = -1155, 140, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = om15_01

[Object]
nickname = om15_01_habitat04
pos = -1155, -140, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = om15_01

[Object]
nickname = om15_01_habitat05
pos = -1155, 140, 1800
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = om15_01

[Object]
nickname = om15_01_habitat06
pos = -1155, -140, 1800
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = om15_01

[Object]
nickname = om15_01_habitat07
pos = -1155, -1, 1250
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = om15_01

[Object]
nickname = om15_01_habitat08
pos = -1155, -0.5, 555
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = om15_01

[Object]
nickname = om15_01_habitat09
pos = -1155, -0.5, 900
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = om15_01

[Object]
nickname = om15_01_girder07
pos = -1155, -1, 1050
rotate = 0, 0, 0
archetype = space_girder
parent = om15_01

[Object]
nickname = om15_01_girder08
pos = -1155, -0.5, 700
rotate = 0, 0, 0
archetype = space_girder
parent = om15_01

[Object]
nickname = om15_01_shipyard01
pos = -925, -465, 1500
rotate = 0, -90, 0
archetype = shipyard
parent = om15_01

[Object]
nickname = om15_01_shipyard02
pos = -925, -465, 1000
rotate = 0, -90, 0
archetype = shipyard
parent = om15_01

[Object]
nickname = om15_01_shipyard03
pos = -925, -465, 500
rotate = 0, -90, 0
archetype = shipyard
parent = om15_01

[Object]
nickname = om15_01_panel01
pos = -55, 35, 0
rotate = 0, 70, 0
archetype = space_solar_pnl
parent = om15_01

[Object]
nickname = om15_01_panel02
pos = 601, 35, 0
rotate = 0, 70, 0
archetype = space_solar_pnl
parent = om15_01
'''


class LibertyRoidMining(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_cal_05'
    TEMPLATE = '''[Object]
nickname = li_cal_05
ids_name = 203656
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_mining01
ids_info = 065575
dock_with = li_cal_05_base
base = li_cal_05_base
reputation = li_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = li_manhattan_bartender_head, li_manhattan_bartender_body, prop_neuralnet_e
difficulty_level = 12
loadout = space_mining01_li
pilot = pilot_solar_hardest

[Object]
nickname = li_cal_05_research01
pos = 220, -380, 373
rotate = 0, 0, 0
archetype = space_research
parent = li_cal_05

[Object]
nickname = li_cal_05_research02
pos = -220, -380, 373
rotate = 0, 0, 0
archetype = space_research
parent = li_cal_05

[Object]
nickname = li_cal_05_girder01
pos = 135, -235, 373
rotate = 45, 90, 0
archetype = space_girder
parent = li_cal_05

[Object]
nickname = li_cal_05_girder02
pos = -135, -235, 373
rotate = -45, 90, 0
archetype = space_girder
parent = li_cal_05

[Object]
nickname = li_cal_05_industrial01
pos = 650, -380, 373
rotate = 0, -90, 0
archetype = space_industrial
parent = li_cal_05

[Object]
nickname = li_cal_05_industrial02
pos = -650, -380, 373
rotate = 0, 90, 0
archetype = space_industrial
parent = li_cal_05

[Object]
nickname = li_cal_05_industrial03
pos = 650, -380, 2173
rotate = 0, -90, 0
archetype = space_industrial
parent = li_cal_05

[Object]
nickname = li_cal_05_industrial04
pos = -650, -380, 2173
rotate = 0, 90, 0
archetype = space_industrial
parent = li_cal_05

[Object]
nickname = li_cal_05_shipyard01
pos = 0, -550, 750
rotate = 0, 90, 0
archetype = shipyard
parent = li_cal_05

[Object]
nickname = li_cal_05_shipyard02
pos = 0, -550, 1300
rotate = 0, -90, 0
archetype = shipyard
parent = li_cal_05

[Object]
nickname = li_cal_05_shipyard03
pos = 0, -550, 1850
rotate = 0, 90, 0
archetype = shipyard
parent = li_cal_05

[Object]
nickname = li_cal_05_panel01
pos = -220, -360, 675
rotate = 0, 45, 0
archetype = space_solar_pnl
parent = li_cal_05

[Object]
nickname = li_cal_05_panel02
pos = 220, -360, 1075
rotate = 0, 45, 0
archetype = space_solar_pnl
parent = li_cal_05

[Object]
nickname = li_cal_05_panel03
pos = -220, -360, 1475
rotate = 0, 45, 0
archetype = space_solar_pnl
parent = li_cal_05

[Object]
nickname = li_cal_05_panel04
pos = 220, -360, 1875
rotate = 0, 45, 0
archetype = space_solar_pnl
parent = li_cal_05

[Object]
nickname = li_cal_05_tankl01
pos = 220, -360, 675
rotate = 180, 0, 0
archetype = space_tankl4
parent = li_cal_05

[Object]
nickname = li_cal_05_tankl02
pos = -220, -360, 1075
rotate = 180, 0, 0
archetype = space_tankl4
parent = li_cal_05

[Object]
nickname = li_cal_05_tankl03
pos = 220, -360, 1475
rotate = 180, 0, 0
archetype = space_tankl4
parent = li_cal_05

[Object]
nickname = li_cal_05_tankl04
pos = -220, -360, 1875
rotate = 180, 0, 0
archetype = space_tankl4
parent = li_cal_05

[Object]
nickname = li_cal_05_habitat01
pos = 650, -135, 373
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = li_cal_05

[Object]
nickname = li_cal_05_habitat02
pos = -650, -70, 373
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = li_cal_05

[Object]
nickname = li_cal_05_habitat03
pos = 650, -100, 2173
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = li_cal_05

[Object]
nickname = li_cal_05_habitat04
pos = -650, -160, 2173
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = li_cal_05

[Object]
nickname = li_cal_05_habitat05
pos = 650, -235, 373
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_05

[Object]
nickname = li_cal_05_habitat06
pos = -650, -235, 373
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_05

[Object]
nickname = li_cal_05_habitat07
pos = 650, -235, 2173
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_05

[Object]
nickname = li_cal_05_habitat08
pos = -650, -235, 2173
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_cal_05
'''
