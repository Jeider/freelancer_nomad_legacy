from templates.space_object_template import SpaceObjectTemplate


class BretoniaPirateGasMiner(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'tau23_04'
    TEMPLATE = '''[Object]
nickname = tau23_04
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_police01_gas_miner
base = tau23_04_base
dock_with = tau23_04_base
behavior = NOTHING
reputation = pi_grp
ids_name = 208623
ids_info = 067021
visit = 16
voice = atc_leg_m01
space_costume = pi_pirate4_head, pi_pirate6_body, prop_neuralnet_b

[Object]
nickname = tau23_04_miner01
pos = 0, -200, 130
rotate = 90, 0, 90
archetype = gas_miner_core
parent = tau23_04

[Object]
nickname = tau23_04_miner02
pos = 0, -200, -130
rotate = -90, 0, 90
archetype = gas_miner_core
parent = tau23_04

[Object]
nickname = tau23_04_girder01
pos = 0, -100, 0
rotate = 90, 0, 0
archetype = space_girderc
parent = tau23_04

[Object]
nickname = tau23_04_ind01
pos = 0, -200, 0
rotate = 0, 90, 0
archetype = space_industrial02d
parent = tau23_04

[Object]
nickname = tau23_04_ind02
pos = 0, -200, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = tau23_04

[Object]
nickname = tau23_04_ind03
pos = 0, -200, -100
rotate = 0, 90, 0
archetype = space_industrial02D
parent = tau23_04

[Object]
nickname = tau23_04_ind04
pos = 0, -200, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = tau23_04

[Object]
nickname = tau23_04_control01
pos = 0, -130, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = tau23_04

[Object]
nickname = tau23_04_control02
pos = 0, -270, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = tau23_04

[Object]
nickname = tau23_04_tanks01
pos = 0, -400, 0
rotate = 0, 0, 0
archetype = space_tanklx4
parent = tau23_04
'''



class BretoniaCivilianGasMiner(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'tau23_01'
    TEMPLATE = '''[Object]
nickname = tau23_01
ids_name = 203737
pos = 0, 0, 0
rotate = 0, 90, 0
;spin = 0, 0, 0
archetype = space_police01_gas_station
ids_info = 065652
dock_with = tau23_01_Base
base = tau23_01_Base
reputation = br_grp
behavior = NOTHING
voice = atc_leg_f01
space_costume = br_kaitlyn_head, pl_female1_peasant_body, prop_neuralnet_a_right
difficulty_level = 12
loadout = br_space_police01
pilot = pilot_solar_hardest

[Object]
nickname = tau23_01_space_dome01
pos = 0, 680, 0
rotate = 0, 0, 0
archetype = space_large_dome
parent = tau23_01

[Object]
nickname = tau23_01_space_dome02
pos = -50, 570, 160
rotate = 0, 90, 0
archetype = space_domea
parent = tau23_01

[Object]
nickname = tau23_01_space_dome03
pos = -100, 615, -130
rotate = 0, -45, 0
archetype = space_domea
parent = tau23_01

[Object]
nickname = tau23_01_gas_miner01
pos = 0, 395, -515
rotate = 0, 0, 0
archetype = gas_miner_old_closed
loadout = gas_miner_old_br
parent = tau23_01

[Object]
nickname = tau23_01_gas_miner02
pos = 0, 395, 515
rotate = 0, 180, 0
archetype = gas_miner_old_closed
loadout = gas_miner_old_br
parent = tau23_01

[Object]
nickname = tau23_01_gas_miner03
pos = 515, 395, 0
rotate = 0, -90, 0
archetype = gas_miner_old_closed
loadout = gas_miner_old_br
parent = tau23_01

[Object]
nickname = tau23_01_gas_miner04
pos = -515, 395, 0
rotate = 0, 90, 0
archetype = gas_miner_old_closed
loadout = gas_miner_old_br
parent = tau23_01

[Object]
nickname = tau23_01_cntrl_tower01
pos = 0, 433, 0
rotate = 180, 0, 0
archetype = space_control_tower
parent = tau23_01

[Object]
nickname = tau23_01_cntrl_tower02
pos = 0, 265, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = tau23_01

[Object]
nickname = tau23_01_cntrl_tower03
pos = 150, 520, 20
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = tau23_01

[Object]
nickname = tau23_01_industrial01
pos = 0, 344, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = tau23_01

[Object]
nickname = tau23_01_industrial02
pos = 0, 348, -185
rotate = 0, 0, 0
archetype = space_industrial02a
parent = tau23_01

[Object]
nickname = tau23_01_industrial03
pos = 0, 348, 175
rotate = 0, 0, 0
archetype = space_industrial02a
parent = tau23_01

[Object]
nickname = tau23_01_industrial04
pos = 185, 348, 0
rotate = 0, 90, 0
archetype = space_industrial02a
parent = tau23_01

[Object]
nickname = tau23_01_industrial05
pos = -175, 348, 0
rotate = 0, 90, 0
archetype = space_industrial02a
parent = tau23_01

[Object]
nickname = tau23_01_industrial06
pos = 0, 180, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = tau23_01

[Object]
nickname = tau23_01_tanks01
pos = 120, 348, -120
rotate = 90, -45, 0
archetype = space_tanks4
parent = tau23_01

[Object]
nickname = tau23_01_tanks02
pos = -120, 348, -120
rotate = 90, 45, 0
archetype = space_tanks4
parent = tau23_01

[Object]
nickname = tau23_01_tanks03
pos = 120, 348, 120
rotate = 90, -135, 0
archetype = space_tanks4
parent = tau23_01

[Object]
nickname = tau23_01_tanks04
pos = -120, 348, 120
rotate = 90, 135, 0
archetype = space_tanks4
parent = tau23_01

[Object]
nickname = tau23_01_habitat01
pos = 0, -80, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau23_01

[Object]
nickname = tau23_01_habitat02
pos = 0, -170, 0
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = tau23_01

[Object]
nickname = tau23_01_habitat03
pos = -100, 520, -130
rotate = 0, -45, 0
archetype = space_habitat_wide
parent = tau23_01

[Object]
nickname = tau23_01_habitat04
pos = -50, 497, 160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau23_01

[Object]
nickname = tau23_01_habitat05
pos = -50, 680, 160
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = tau23_01

[Object]
nickname = tau23_01_habitat06
pos = 150, 520, 20
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = tau23_01

[Object]
nickname = tau23_01_habitat07
pos = 150, 640, 20
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = tau23_01
'''


class RheinlandCivilianGasMiner(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'sig13_01'
    TEMPLATE = '''[Object]
nickname = sig13_01
ids_name = 203646
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_police01_gas_station
ids_info = 065567
base = sig13_01_Base
dock_with = sig13_01_Base
reputation = rh_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = ge_male7_head, rh_wilham_body, prop_neuralnet_c
difficulty_level = 12
loadout = rh_space_police01
pilot = pilot_solar_hardest

[Object]
nickname = sig13_01_gas_miner01
pos = 0, -465, -400
rotate = 0, 90, 0
archetype = gas_miner_nodock
loadout = gasminer_original_rh
parent = sig13_01

[Object]
nickname = sig13_01_gas_miner02
pos = 400, -465, 0
rotate = 0, 0, 0
archetype = gas_miner_nodock
loadout = gasminer_original_rh
parent = sig13_01

[Object]
nickname = sig13_01_gas_miner03
pos = 0, -465, 400
rotate = 0, -90, 0
archetype = gas_miner_nodock
loadout = gasminer_original_rh
parent = sig13_01

[Object]
nickname = sig13_01_gas_miner04
pos = -400, -465, 0
rotate = 0, 180, 0
archetype = gas_miner_nodock
loadout = gasminer_original_rh
parent = sig13_01

[Object]
nickname = sig13_01_ind01
pos = -400, -465, -400
rotate = 90, 0, 0
archetype = space_industriala
parent = sig13_01

[Object]
nickname = sig13_01_ind02
pos = 400, -465, 400
rotate = 90, 0, 0
archetype = space_industriala
parent = sig13_01

[Object]
nickname = sig13_01_ind03
pos = 400, -465, -400
rotate = 90, 0, 0
archetype = space_industriala
parent = sig13_01

[Object]
nickname = sig13_01_ind04
pos = -400, -465, 400
rotate = 90, 0, 0
archetype = space_industriala
parent = sig13_01

[Object]
nickname = sig13_01_ind05
pos = 400, -465, -290
rotate = 0, 0, 0
archetype = space_industrial01b
parent = sig13_01

[Object]
nickname = sig13_01_ind06
pos = 290, -465, -400
rotate = 0, 90, 0
archetype = space_industrial01b
parent = sig13_01

[Object]
nickname = sig13_01_ind07
pos = 400, -465, 290
rotate = 0, 0, 0
archetype = space_industrial01b
parent = sig13_01

[Object]
nickname = sig13_01_ind08
pos = 290, -465, 400
rotate = 0, 90, 0
archetype = space_industrial01b
parent = sig13_01

[Object]
nickname = sig13_01_ind09
pos = -290, -465, 400
rotate = 0, 90, 0
archetype = space_industrial01b
parent = sig13_01

[Object]
nickname = sig13_01_ind10
pos = -290, -465, -400
rotate = 0, 90, 0
archetype = space_industrial01b
parent = sig13_01

[Object]
nickname = sig13_01_ind11
pos = -400, -465, -290
rotate = 0, 0, 0
archetype = space_industrial01b
parent = sig13_01

[Object]
nickname = sig13_01_ind12
pos = -400, -465, 290
rotate = 0, 0, 0
archetype = space_industrial01b
parent = sig13_01

[Object]
nickname = sig13_01_cntrl_twr01
pos = 0, -465, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = sig13_01

[Object]
nickname = sig13_01_cntrl_twr02
pos = 0, -215, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = sig13_01

[Object]
nickname = sig13_01_cntrl_twr03
pos = 0, -325, 0
rotate = 180, 0, 0
archetype = space_medium_control_tower
parent = sig13_01

[Object]
nickname = sig13_01_cntrl_twr04
pos = 0, -605, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = sig13_01

[Object]
nickname = sig13_01_indA01
pos = 150, -465, 0
rotate = 90, 0, 0
archetype = space_industrial02a
parent = sig13_01

[Object]
nickname = sig13_01_indA02
pos = 0, -465, -150
rotate = 90, 0, 0
archetype = space_industrial02a
parent = sig13_01

[Object]
nickname = sig13_01_indA03
pos = -150, -465, 0
rotate = 90, 0, 0
archetype = space_industrial02a
parent = sig13_01

[Object]
nickname = sig13_01_indA04
pos = 0, -465, 150
rotate = 90, 0, 0
archetype = space_industrial02a
parent = sig13_01

[Object]
nickname = sig13_01_indA05
pos = 0, -465, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = sig13_01

[Object]
nickname = sig13_01_tanks01
pos = 0, -695, 0
rotate = 90, 0, 0
archetype = space_tanks4x4
parent = sig13_01

[Object]
nickname = sig13_01_tanks02
pos = 0, -695, 0
rotate = 90, 90, 0
archetype = space_tanks4x4
parent = sig13_01

[Object]
nickname = sig13_01_tanks03
pos = -60, -685, 60
rotate = 90, 45, 0
archetype = space_tanks4x4
parent = sig13_01

[Object]
nickname = sig13_01_tanks04
pos = 60, -685, -60
rotate = 90, 45, 0
archetype = space_tanks4x4
parent = sig13_01

[Object]
nickname = sig13_01_tanks05
pos = -70, -685, -70
rotate = 90, -45, 0
archetype = space_tanks4x4
parent = sig13_01

[Object]
nickname = sig13_01_tanks06
pos = 70, -685, 70
rotate = 90, -45, 0
archetype = space_tanks4x4
parent = sig13_01

[Object]
nickname = sig13_01_tanks07
pos = 0, -785, 0
rotate = 0, 45, 0
archetype = space_tanksx4
parent = sig13_01

[Object]
nickname = sig13_01_girder01
pos = 380, -465, -380
rotate = 0, -45, 0
archetype = space_girdera
parent = sig13_01

[Object]
nickname = sig13_01_girder02
pos = 380, -465, 380
rotate = 0, -135, 0
archetype = space_girdera
parent = sig13_01

[Object]
nickname = sig13_01_girder03
pos = -380, -465, -380
rotate = 0, 45, 0
archetype = space_girdera
parent = sig13_01

[Object]
nickname = sig13_01_girder04
pos = -380, -465, 380
rotate = 0, 135, 0
archetype = space_girdera
parent = sig13_01

[Object]
nickname = sig13_01_habitat01
pos = -60, -285, 0
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig13_01

[Object]
nickname = sig13_01_habitat02
pos = 0, -285, 60
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig13_01

[Object]
nickname = sig13_01_habitat03
pos = 60, -285, 0
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig13_01

[Object]
nickname = sig13_01_habitat04
pos = 0, -285, -60
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig13_01

[Object]
nickname = sig13_01_habitat05
pos = 0, -120, 0
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = sig13_01
'''


class RheinlandPirateGasMiner(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'sig13_03'
    TEMPLATE = '''[Object]
nickname = sig13_03
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = gas_miner_dock
ids_name = 203649
ids_info = 065569
reputation = pi_grp
behavior = NOTHING
voice = atc_leg_f01
space_costume = pl_female1_head, sh_female1_body, prop_neuralnet_a_right
base = sig13_03_base
dock_with = sig13_03_base

[Object]
nickname = sig13_03_dock_dummy
pos = 0, 4, -320
rotate = 0, 0, 180
archetype = gas_miner_dock_dummy
parent = sig13_03

[Object]
nickname = sig13_03_miner_core
pos = -125, 0, -160
rotate = 0, 0, 90
archetype = gas_miner_core
parent = sig13_03

[Object]
nickname = sig13_03_ind01
pos = 0, 0, -160
rotate = 0, 0, 0
archetype = space_industriala
parent = sig13_03

[Object]
nickname = sig13_03_ind02
pos = 0, 0, -240
rotate = 0, 0, 0
archetype = space_industrial01b
parent = sig13_03

[Object]
nickname = sig13_03_tank01
pos = 0, 100, -230
rotate = 0, 0, 180
archetype = space_tanks4
parent = sig13_03

[Object]
nickname = sig13_03_tank02
pos = 100, 0, -230
rotate = 0, 0, 90
archetype = space_tanks4
parent = sig13_03

[Object]
nickname = sig13_03_tank03
pos = 0, -100, -230
rotate = 0, 0, 0
archetype = space_tanks4
parent = sig13_03

[Object]
nickname = sig13_03_tank04
pos = 0, -100, -90
rotate = 0, 0, 0
archetype = space_tanks4
parent = sig13_03

[Object]
nickname = sig13_03_tank05
pos = 100, 0, -90
rotate = 0, 0, 90
archetype = space_tanks4
parent = sig13_03

[Object]
nickname = sig13_03_tank06
pos = 0, 100, -90
rotate = 0, 0, 180
archetype = space_tanks4
parent = sig13_03
'''
