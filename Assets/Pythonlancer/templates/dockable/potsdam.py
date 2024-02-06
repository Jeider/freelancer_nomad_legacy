from templates.space_object_template import SpaceObjectTemplate


class Potsdam(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_ber_04'
    TEMPLATE = '''[Object]
nickname = rh_ber_04
ids_name = 203628
pos = 1980, -545, 935
rotate = 0, 0, 0
archetype = potsdam_core
ids_info = 066628
reputation = rh_grp
behavior = NOTHING
difficulty_level = 12
base = rh_ber_04_base
pilot = pilot_solar_hardest

[Object]; dock
nickname = rh_ber_04_dock
pos = 0, 0, 0
rotate = 0, -90, 0
archetype = space_shipping01
reputation = rh_grp
behavior = NOTHING
difficulty_level = 12
base = rh_ber_04_base
dock_with = rh_ber_04_base
pilot = pilot_solar_hardest
visit = 16
voice = atc_leg_m01
space_costume = sh_male1_head, rh_wilham_body, prop_neuralnet_f, prop_neuralnet_f_up_right
ids_name = 196722
ids_info = 065739

;main construction
[Object]
nickname = rh_ber_04_space_research01
pos = 1980, -545, -1065
rotate = 0, 0, 0
archetype = space_research
parent = rh_ber_04

[Object]
nickname = rh_ber_04_space_research02
pos = 1980, -545, 985
rotate = 0, 0, 0
archetype = space_research
parent = rh_ber_04

[Object]
nickname = rh_ber_04_space_research03
pos = 2160, -545, 985
rotate = 0, 90, 0
archetype = space_research
parent = rh_ber_04

[Object]
nickname = rh_ber_04_space_research04
pos = 1800, -545, 735
rotate = 0, -90, 0
archetype = space_research
parent = rh_ber_04

[Object]
nickname = rh_ber_04_space_research05
pos = 1980, -725, 985
rotate = 90, 0, 0
archetype = space_research
parent = rh_ber_04

[Object]
nickname = rh_ber_04_space_research06
pos = 1980, -365, 735
rotate = -90, 0, 0
archetype = space_research
parent = rh_ber_04

;shipyard block
[Object]
nickname = rh_ber_04_SH_space_industrial01
pos = 3960, -545, 445
rotate = 0, 0, 0
archetype = space_industrial
parent = rh_ber_04

[Object]
nickname = rh_ber_04_SH_space_industrial02
pos = 3960, -545, -155
rotate = 0, 0, 0
archetype = space_industrial
parent = rh_ber_04

[Object]
nickname = rh_ber_04_SH_space_industrial03
pos = 3960, -545, 1530
rotate = 0, 180, 0
archetype = space_industrial
parent = rh_ber_04

[Object]
nickname = rh_ber_04_SH_space_industrial04
pos = 3960, -545, 2130
rotate = 0, 180, 0
archetype = space_industrial
parent = rh_ber_04

[Object]
nickname = rh_ber_04_SH_shipyard01
pos = 3780, -755, -155
rotate = 0, -90, 0
archetype = shipyard
parent = rh_ber_04

[Object]
nickname = rh_ber_04_SH_shipyard02
pos = 3780, -335, -155
rotate = 180, 90, 0
archetype = shipyard
parent = rh_ber_04

[Object]
nickname = rh_ber_04_SH_shipyard03
pos = 3780, -755, 445
rotate = 0, -90, 0
archetype = shipyard
parent = rh_ber_04

[Object]
nickname = rh_ber_04_SH_shipyard04
pos = 3780, -335, 445
rotate = 180, 90, 0
archetype = shipyard
parent = rh_ber_04

[Object]
nickname = rh_ber_04_SH_shipyard05
pos = 3780, -755, 1525
rotate = 0, -90, 0
archetype = shipyard
parent = rh_ber_04

[Object]
nickname = rh_ber_04_SH_shipyard06
pos = 3780, -335, 1525
rotate = 180, 90, 0
archetype = shipyard
parent = rh_ber_04

[Object]
nickname = rh_ber_04_SH_shipyard07
pos = 3780, -755, 2130
rotate = 0, -90, 0
archetype = shipyard
parent = rh_ber_04

[Object]
nickname = rh_ber_04_SH_shipyard08
pos = 3780, -335, 2130
rotate = 180, 90, 0
archetype = shipyard
parent = rh_ber_04

;industrial block
[Object]
nickname = rh_ber_04_IND_LVL1_space_industrial01
pos = 1980, 0, 2785
rotate = 90, 0, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_LVL1_space_industrial02
pos = 1980, 0, 2245
rotate = 0, 0, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_LVL1_space_industrial03
pos = 1980, 0, 1645
rotate = 0, 0, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_LVL1_space_industrial04
pos = 1980, -1090, 2785
rotate = -90, 0, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_LVL1_space_industrial05
pos = 1980, -1090, 2245
rotate = 0, 0, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_LVL1_space_industrial06
pos = 1980, -1090, 1645
rotate = 0, 0, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_LVL2_space_industrial01
pos = 1680, 0, 2375
rotate = 0, 30, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_LVL2_space_industrial02
pos = 1680, 0, 1835
rotate = 0, 30, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_LVL2_space_industrial03
pos = 1680, 0, 1235
rotate = 0, 30, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_LVL2_space_industrial04
pos = 2280, 0, 2375
rotate = 0, -30, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_LVL2_space_industrial05
pos = 2280, 0, 1835
rotate = 0, -30, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_LVL2_space_industrial06
pos = 2280, 0, 1235
rotate = 0, -30, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_LVL3_space_industrial01
pos = 1680, -1090, 2375
rotate = 0, 30, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_LVL3_space_industrial02
pos = 1680, -1090, 1835
rotate = 0, 30, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_LVL3_space_industrial03
pos = 1680, -1090, 1235
rotate = 0, 30, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_LVL3_space_industrial04
pos = 2280, -1090, 2375
rotate = 0, -30, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_LVL3_space_industrial05
pos = 2280, -1090, 1835
rotate = 0, -30, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_LVL3_space_industrial06
pos = 2280, -1090, 1235
rotate = 0, -30, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_NRG_space_industrial01
pos = 1680, -425, 2375
rotate = -90, 30, 0
archetype = space_industrial01
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_NRG_space_industrial02
pos = 1680, -665, 2375
rotate = 90, 30, 0
archetype = space_industrial01
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_NRG_space_industrial03
pos = 1680, -425, 1835
rotate = -90, 30, 0
archetype = space_industrial01
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_NRG_space_industrial04
pos = 1680, -665, 1835
rotate = 90, 30, 0
archetype = space_industrial01
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_NRG_space_industrial05
pos = 1680, -425, 1235
rotate = -90, 30, 0
archetype = space_industrial01
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_NRG_space_industrial06
pos = 1680, -665, 1235
rotate = 90, 30, 0
archetype = space_industrial01
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_NRG_space_industrial07
pos = 2280, -425, 2375
rotate = -90, -30, 0
archetype = space_industrial01
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_NRG_space_industrial08
pos = 2280, -665, 2375
rotate = 90, -30, 0
archetype = space_industrial01
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_NRG_space_industrial09
pos = 2280, -425, 1835
rotate = -90, -30, 0
archetype = space_industrial01
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_NRG_space_industrial10
pos = 2280, -665, 1835
rotate = 90, -30, 0
archetype = space_industrial01
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_NRG_space_industrial11
pos = 2280, -425, 1235
rotate = -90, -30, 0
archetype = space_industrial01
parent = rh_ber_04

[Object]
nickname = rh_ber_04_IND_NRG_space_industrial12
pos = 2280, -665, 1235
rotate = 90, -30, 0
archetype = space_industrial01
parent = rh_ber_04

;HILL block

[Object]
nickname = rh_ber_04_HILL_space_industrial01
pos = 1435, -545, -1065
rotate = 0, 90, 0
archetype = space_industrial
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_industrial02
pos = 2525, -545, -1065
rotate = 0, -90, 0
archetype = space_industrial
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_industrial03
pos = 1435, -245, -655
rotate = 30, 180, 0
archetype = space_industrial
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_industrial04
pos = 2525, -245, -655
rotate = 30, 180, 0
archetype = space_industrial
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_industrial05
pos = 1435, -185, -75
rotate = 0, 180, 0
archetype = space_industrial
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_industrial06
pos = 2525, -185, -75
rotate = 0, 180, 0
archetype = space_industrial
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_industrial07
pos = 1435, -185, 525
rotate = 0, 180, 0
archetype = space_industrial
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_industrial08
pos = 2525, -185, 525
rotate = 0, 180, 0
archetype = space_industrial
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_industrial09
pos = 1860, -185, -75
rotate = 0, -90, 0
archetype = space_industrial
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_industrial10
pos = 2100, -185, -75
rotate = 0, 90, 0
archetype = space_industrial
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_industrial11
pos = 1435, -725, -75
rotate = -90, 0, 0
archetype = space_industrial
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_industrial12
pos = 2525, -725, -75
rotate = -90, 0, 0
archetype = space_industrial
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_dome01
pos = 1782, -155, -430
rotate = 0, 15, 0
archetype = space_dome_lod
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_dome02
pos = 2178, -155, -430
rotate = 0, -15, 0
archetype = space_dome_lod
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_dome03
pos = 1405, -725, -445
rotate = 0, 0, 90
archetype = space_dome_lod
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_dome04
pos = 1405, -725, 295
rotate = 0, 180, 90
archetype = space_dome_lod
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_dome05
pos = 1405, -1150, -75
rotate = -90, 90, 0
archetype = space_dome_lod
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_dome06
pos = 2555, -725, -445
rotate = 0, 0, -90
archetype = space_dome_lod
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_dome07
pos = 2555, -725, 295
rotate = 0, 180, -90
archetype = space_dome_lod
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_dome08
pos = 2555, -1150, -75
rotate = -90, -90, 0
archetype = space_dome_lod
parent = rh_ber_04


[Object]
nickname = rh_ber_04_HILL_space_hab_wide01
pos = 1435, -40, 525
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_hab_wide02
pos = 1435, -40, -75
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_hab_wide03
pos = 1435, 115, -75
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_hab_wide04
pos = 1435, -327, 525
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_hab_wide05
pos = 1860, -40, -75
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_hab_wide06
pos = 2100, -40, -75
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_hab_wide07
pos = 2525, -327, 525
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_hab_tall01
pos = 2525, 23, 525
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_hab_tall02
pos = 2525, 23, -75
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = rh_ber_04

[Object]
nickname = rh_ber_04_HILL_space_hab_tall03
pos = 1860, 177, -75
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = rh_ber_04

;dock 

[Object]
nickname = rh_ber_04_DOCK_space_industrial01
pos = 0, 0, 735
rotate = 90, 0, 0
archetype = space_industrial
parent = rh_ber_04

[Object]
nickname = rh_ber_04_DOCK_space_industrial02
pos = 0, -545, 1280
rotate = 0, 180, 0
archetype = space_industrial
parent = rh_ber_04

[Object]
nickname = rh_ber_04_DOCK_space_industrial03
pos = 0, -545, 1880
rotate = 0, 180, 0
archetype = space_industrial
parent = rh_ber_04

[Object]
nickname = rh_ber_04_DOCK_battleship01
pos = 580, -495, 1280
rotate = 0, 90, 0
archetype = r_battleship
parent = rh_ber_04

[Object]
nickname = rh_ber_04_DOCK_battleship02
pos = 580, -495, 1880
rotate = 0, 90, 0
archetype = r_Battleship
parent = rh_ber_04

[Object]
nickname = rh_ber_04_DOCK_space_habitat01
pos = 0, -338, 1880
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = rh_ber_04

[Object]
nickname = rh_ber_04_DOCK_space_habitat02
pos = 0, -400, 1280
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_ber_04

[Object]
nickname = rh_ber_04_DOCK_space_tanks01
pos = 0, -665, 1880
rotate = 0, 0, 0
archetype = space_tanksx4
parent = rh_ber_04

[Object]
nickname = rh_ber_04_DOCK_space_tanks02
pos = 0, -665, 1280
rotate = 0, 0, 0
archetype = space_tanksx4
parent = rh_ber_04

[Object]
nickname = rh_ber_04_DOCK_space_industrial04
pos = 545, 0, 735
rotate = 0, -90, 0
archetype = space_industrial
parent = rh_ber_04

[Object]
nickname = rh_ber_04_DOCK_space_industrial05
pos = 1145, 0, 735
rotate = 0, -90, 0
archetype = space_industrial
parent = rh_ber_04

[Object]
nickname = rh_ber_04_DOCK_battleship03
pos = 545, 45, 1305
rotate = 0, 0, 0
archetype = r_battleship
parent = rh_ber_04

;ENERGY top

[Object]
nickname = rh_ber_04_TOP_solar_plant01
pos = 1930, 1455, 685
rotate = 0, -40, 0
;spin = 0.1, 0, 0
archetype = space_solar_plant
parent = rh_ber_04

[Object]
nickname = rh_ber_04_TOP_solar_plant02
pos = 1930, 855, 685
rotate = 0, -40, 0
;spin = 0.1, 0, 0
archetype = space_solar_plant
parent = rh_ber_04

[Object]
nickname = rh_ber_04_TOP_solar_plant03
pos = 1930, 255, 685
rotate = 0, -40, 0
;spin = 0.1, 0, 0
archetype = space_solar_plant
parent = rh_ber_04

;STORAGE bottom

[Object]
nickname = rh_ber_04_STOR_space_industrial01
pos = 1980, -2525, 440
rotate = 0, 0, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_STOR_space_industrial02
pos = 1435, -2525, 985
rotate = 0, 90, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_STOR_space_industrial03
pos = 1980, -2525, 1525
rotate = 0, 180, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_STOR_space_industrial04
pos = 2525, -2525, 985
rotate = 0, -90, 0
archetype = space_industrial02
parent = rh_ber_04

[Object]
nickname = rh_ber_04_STOR_space_tanks01
pos = 1980, -2325, 440
rotate = 90, 0, 0
archetype = space_tankl4x4
parent = rh_ber_04

[Object]
nickname = rh_ber_04_STOR_space_tanks02
pos = 1980, -2060, 440
rotate = 90, 0, 0
archetype = space_tankl4x4
parent = rh_ber_04

[Object]
nickname = rh_ber_04_STOR_space_tanks03
pos = 1980, -1795, 440
rotate = 90, 0, 0
archetype = space_tankl4x4
parent = rh_ber_04

[Object]
nickname = rh_ber_04_STOR_space_tanks04
pos = 1980, -1530, 440
rotate = 90, 0, 0
archetype = space_tankl4x4
parent = rh_ber_04

[Object]
nickname = rh_ber_04_STOR_space_tanks05
pos = 1435, -2325, 985
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = rh_ber_04

[Object]
nickname = rh_ber_04_STOR_space_tanks06
pos = 1435, -2060, 985
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = rh_ber_04

[Object]
nickname = rh_ber_04_STOR_space_tanks07
pos = 1435, -1530, 985
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = rh_ber_04

[Object]
nickname = rh_ber_04_STOR_space_tanks08
pos = 1435, -1795, 985
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = rh_ber_04

[Object]
nickname = rh_ber_04_STOR_space_tanks09
pos = 1980, -2325, 1525
rotate = 90, 0, 0
archetype = space_tankl4x4
parent = rh_ber_04

[Object]
nickname = rh_ber_04_STOR_space_tanks10
pos = 1980, -2060, 1525
rotate = 90, 0, 0
archetype = space_tankl4x4
parent = rh_ber_04

[Object]
nickname = rh_ber_04_STOR_space_tanks11
pos = 1980, -1795, 1525
rotate = 90, 0, 0
archetype = space_tankl4x4
parent = rh_ber_04

[Object]
nickname = rh_ber_04_STOR_space_tanks12
pos = 1980, -1530, 1525
rotate = 90, 0, 0
archetype = space_tankl4x4
parent = rh_ber_04

[Object]
nickname = rh_ber_04_STOR_space_tanks13
pos = 2525, -2325, 985
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = rh_ber_04

[Object]
nickname = rh_ber_04_STOR_space_tanks14
pos = 2525, -2060, 985
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = rh_ber_04

[Object]
nickname = rh_ber_04_STOR_space_tanks15
pos = 2525, -1795, 985
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = rh_ber_04

[Object]
nickname = rh_ber_04_STOR_space_tanks16
pos = 2525, -1530, 985
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = rh_ber_04
'''
