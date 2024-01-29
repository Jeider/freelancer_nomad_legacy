from templates.space_object_template import SpaceObjectTemplate


class BlackHoleResearch(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'om13_01'
    TEMPLATE = '''[Object]
nickname = om13_01
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = space_police01_front_dock
ids_name = 203851
ids_info = 065761
behavior = NOTHING
reputation = co_grp
base = om13_01_base
dock_with = om13_01_base
voice = atc_leg_f01
space_costume = br_karina_head_gen, sc_female1_body, prop_neuralnet_d

[Object]
nickname = om13_01_panel01
pos = 100, 40, 90
rotate = 0, 0, 25
archetype = space_panel
parent = om13_01

[Object]
nickname = om13_01_panel02
pos = -100, 40, 90
rotate = 0, 0, -25
archetype = space_panel
parent = om13_01

[Object]
nickname = om13_01_panel03
pos = 70, 50, 255
rotate = 10, 145, -10
archetype = space_panel45
parent = om13_01

[Object]
nickname = om13_01_panel04
pos = -70, 50, 255
rotate = 95, -155, -40
archetype = space_panel
parent = om13_01

[Object]
nickname = om13_01_ind01
pos = 0, 0, 120
rotate = 90, 0, 0
archetype = space_industrial02a
parent = om13_01

[Object]
nickname = om13_01_ind02
pos = 0, 0, 240
rotate = 0, 0, 0
archetype = space_industriala
parent = om13_01

[Object]
nickname = om13_01_ind03
pos = 60, -62, 120
rotate = 0, , 0
archetype = space_industrial02a
parent = om13_01

[Object]
nickname = om13_01_ind04
pos = -60, -62, 120
rotate = 0, 0, 0
archetype = space_industrial01a
parent = om13_01

[Object]
nickname = om13_01_habitat01
pos = 0, -400, 120
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = om13_01

[Object]
nickname = om13_01_habitat02
pos = 0, -200, 120
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = om13_01

[Object]
nickname = om13_01_habitat03
pos = 0, 70, 215
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = om13_01

[Object]
nickname = om13_01_habitat04
pos = 0, 160, 215
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = om13_01

[Object]
nickname = om13_01_habitat05
pos = 0, 183, 120
rotate = 0, 90, 0
archetype = space_small_control_block
parent = om13_01

[Object]
nickname = om13_01_tanks01
pos = -50, -260, 120
rotate = 90, 0, 10
archetype = space_tankl4x4
parent = om13_01

[Object]
nickname = om13_01_tanks02
pos = 50, -250, 120
rotate = 90, 0, -5
archetype = space_tankl4x4
parent = om13_01

[Object]
nickname = om13_01_dpanel01
pos = 90, -200, 90
rotate = 0, 0, 220
archetype = space_debris_panel
parent = om13_01

[Object]
nickname = om13_01_dpanel02
pos = 78, -300, 140
rotate = 0, 0, 220
archetype = space_debris_panel
parent = om13_01

[Object]
nickname = om13_01_dpanel03
pos = -95, -200, 90
rotate = 0, 0, 55
archetype = space_debris_panel
parent = om13_01

[Object]
nickname = om13_01_dpanel04
pos = -78, -300, 140
rotate = 0, 0, 55
archetype = space_debris_panel
parent = om13_01
'''


class BlackHoleOutpost(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'om13_02'
    TEMPLATE = '''[Object]
nickname = om13_02
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_port_dmg
ids_name = 203852
ids_info = 065762
behavior = NOTHING
reputation = co_grp
base = om13_02_base
dock_with = om13_02_base
voice = atc_leg_m01
space_costume = sh_male4_head, sh_male1_body, prop_neuralnet_b_right, prop_hat_male_cap_a

[Object]
nickname = om13_02_ind01
pos = 0, -250, 0
rotate = 90, 90, 0
archetype = space_industriala
parent = om13_02

[Object]
nickname = om13_02_ind02
pos = 175, -250, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = om13_02

[Object]
nickname = om13_02_ind03
pos = -175, -250, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = om13_02

[Object]
nickname = om13_02_ind04
pos = -115, -250, 200
rotate = 90, 0, 90
archetype = space_industrial02d
parent = om13_02

[Object]
nickname = om13_02_ind05
pos = 115, -250, 200
rotate = 90, 0, 90
archetype = space_industrial02d
parent = om13_02

[Object]
nickname = om13_02_ind06
pos = -115, -250, -200
rotate = 90, 0, 90
archetype = space_industrial02d
parent = om13_02

[Object]
nickname = om13_02_ind07
pos = 115, -250, -200
rotate = 90, 0, 90
archetype = space_industrial02d
parent = om13_02

[Object]
nickname = om13_02_ind08
pos = -160, -210, 0
rotate = 90, 0, 90
archetype = space_industrial02d
parent = om13_02

[Object]
nickname = om13_02_ind09
pos = -160, -290, 0
rotate = 90, 0, 90
archetype = space_industrial02d
parent = om13_02

[Object]
nickname = om13_02_ind10
pos = 160, -210, 0
rotate = 90, 0, 90
archetype = space_industrial02d
parent = om13_02

[Object]
nickname = om13_02_ind11
pos = 160, -290, 0
rotate = 90, 0, 90
archetype = space_industrial02d
parent = om13_02

[Object]
nickname = om13_02_shipyard01
pos = 0, -250, 100
rotate = 90, 0, 90
archetype = shipyard_medium
parent = om13_02

[Object]
nickname = om13_02_shipyard02
pos = 0, -250, -100
rotate = -90, 0, 90
archetype = shipyard_medium
parent = om13_02

[Object]
nickname = om13_02_dpanel01
pos = 120, -172, 120
rotate = 90, -28, -90
archetype = space_debris_panel
parent = om13_02

[Object]
nickname = om13_02_dpanel02
pos = -120, -172, 120
rotate = 90, -28, -90
archetype = space_debris_panel
parent = om13_02

[Object]
nickname = om13_02_dpanel03
pos = 120, -172, -120
rotate = -90, 28, -90
archetype = space_debris_panel
parent = om13_02

[Object]
nickname = om13_02_dpanel04
pos = -120, -172, -120
rotate = -90, 28, -90
archetype = space_debris_panel
parent = om13_02

[Object]
nickname = om13_02_dpanel05
pos = 120, -328, 120
rotate = 90, -28, 90
archetype = space_debris_panel
parent = om13_02

[Object]
nickname = om13_02_dpanel06
pos = -120, -328, 120
rotate = 90, -28, 90
archetype = space_debris_panel
parent = om13_02

[Object]
nickname = om13_02_dpanel07
pos = 120, -328, -120
rotate = 90, 152, -90
archetype = space_debris_panel
parent = om13_02

[Object]
nickname = om13_02_dpanel08
pos = -120, -328, -120
rotate = 90, 152, -90
archetype = space_debris_panel
parent = om13_02

[Object]
nickname = om13_02_girder01
pos = -75, -180, 110
rotate = -15, 150, 0
archetype = space_girderc
parent = om13_02

[Object]
nickname = om13_02_girder02
pos = -75, -180, -110
rotate = -15, 30, 0
archetype = space_girderc
parent = om13_02

[Object]
nickname = om13_02_girder03
pos = 75, -180, 110
rotate = 15, 30, 0
archetype = space_girderc
parent = om13_02

[Object]
nickname = om13_02_girder04
pos = 75, -180, -110
rotate = 15, 150, 0
archetype = space_girderc
parent = om13_02

[Object]
nickname = om13_02_girder05
pos = -75, -320, 110
rotate = 15, 150, 0
archetype = space_girderc
parent = om13_02

[Object]
nickname = om13_02_girder06
pos = -75, -320, -110
rotate = 15, 30, 0
archetype = space_girderc
parent = om13_02

[Object]
nickname = om13_02_girder07
pos = 75, -320, 110
rotate = -15, 30, 0
archetype = space_girderc
parent = om13_02

[Object]
nickname = om13_02_girder08
pos = 75, -320, -110
rotate = -15, 150, 0
archetype = space_girderc
parent = om13_02

[Object]
nickname = om13_02_hab01
pos = 0, -408, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = om13_02

[Object]
nickname = om13_02_hab02
pos = 0, -495, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = om13_02
'''


class BlackHoleDestroyedStation(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'om13_03'
    TEMPLATE = '''[Object]
nickname = om13_03
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = space_industrial_station_root
ids_name = 203850
ids_info = 065760
reputation = fc_uk_grp
behavior = NOTHING

[Object]
nickname = om13_03_ind01
pos = 0, -22, -400
rotate = 10, 180, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = om13_03

[Object]
nickname = om13_03_ind02
pos = -25, -60, -880
rotate = 10, 10, 0
archetype = space_industrial02a
parent = om13_03

[Object]
nickname = om13_03_dome01
pos = 0, -5, 350
rotate = 0, 90, 0
archetype = space_dome_dmg2
parent = om13_03

[Object]
nickname = om13_03_hab01
pos = 200, 0, -350
rotate = 120, 50, 10
archetype = space_habitat_dmg
parent = om13_03

[Object]
nickname = om13_03_hab02
pos = -250, -200, -350
rotate = 34, -45, -23
archetype = space_habitat_dmg
parent = om13_03

[Object]
nickname = om13_03_panel01
pos = 0, 65, 0
rotate = 90, 80, 80
archetype = space_solar_pnl
parent = om13_03

[Object]
nickname = om13_03_panel02
pos = -65, 0, 0
rotate = 0, 40, 60
archetype = space_panel_damaged_01
parent = om13_03

[Object]
nickname = om13_03_panel03
pos = 65, 0, 0
rotate = 0, 0, -120
archetype = space_panel_damaged_01
parent = om13_03

[Object]
nickname = om13_03_tank01
pos = 2, 65, -855
rotate = 100, 20, -20
archetype = space_tankl2x2
parent = om13_03

[Object]
nickname = om13_03_tank02
pos = -30, -250, -875
rotate = 90, 0, 0
archetype = space_tankl4x4_dmg
parent = om13_03

[Object]
nickname = om13_03_tank03
pos = 0, 200, -550
rotate = 180, -30, 0
archetype = space_tankl4_dmg
parent = om13_03
'''


class ShinobiAbandonedResearch(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'om11_04'
    TEMPLATE = '''[Object]
nickname = om11_04
ids_name = 203819
pos = 0, 0, 0
rotate = 0, 0, 5
archetype = space_police01
ids_info = 065726
base = om11_04_base
dock_with = om11_04_base
reputation = kx_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = ku_bartender_head, pi_orillion_body, prop_neuralnet_d
difficulty_level = 12
loadout = ku_space_police01
pilot = pilot_solar_hardest

[Object]
nickname = om11_04_dock01
pos = 200, 0, 0
rotate = 20, 0, -3
archetype = space_police_dmg
parent = om11_04

[Object]
nickname = om11_04_dock02
pos = 400, 0, 0
rotate = 0, 180, 5
archetype = space_police_dmg
parent = om11_04

[Object]
nickname = om11_04_girder01
pos = 200, 0, 0
rotate = 0, 90, -3
archetype = space_girder
parent = om11_04

[Object]
nickname = om11_04_girder02
pos = 323, -116, 0
rotate = 45, -90, 0
archetype = space_beaml_dmg
parent = om11_04

[Object]
nickname = om11_04_girder03
pos = 117, -150, 0
rotate = -135, 90, 0
archetype = space_beaml_dmg
parent = om11_04

[Object]
nickname = om11_04_girder04
pos = 200, -36, 0
rotate = 90, 0, 5
archetype = space_girdera
parent = om11_04

[Object]
nickname = om11_04_girder05
pos = 303, 130, 0
rotate = -45, -90, 0
archetype = space_beaml_dmg
parent = om11_04

[Object]
nickname = om11_04_girder06
pos = -43, -10, 0
rotate = -45, 90, 0
archetype = space_girdera
parent = om11_04

[Object]
nickname = om11_04_ctrl_twr01
pos = 210, -250, 0
rotate = 0, 0, 6
archetype = space_medium_control_tower
parent = om11_04

[Object]
nickname = om11_04_ctrl_twr02
pos = 200, 190, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = om11_04

[Object]
nickname = om11_04_ctrl_block01
pos = 200, 220, 0
rotate = 0, 0, 0
archetype = space_domea
parent = om11_04

[Object]
nickname = om11_04_ind01
pos = 200, -400, 0
rotate = -90, 45, -5
archetype = space_industrial01a
parent = om11_04

[Object]
nickname = om11_04_ind02
pos = 200, -650, 0
rotate = 90, 0, 10
archetype = space_industrial01a
parent = om11_04

[Object]
nickname = om11_04_panel01
pos = 200, -665, 0
rotate = 0, 110, 90
archetype = space_solar_pnl
parent = om11_04

[Object]
nickname = om11_04_panel02
pos = 200, -626, 0
rotate = 0, 90, -100
archetype = space_solar_pnl
parent = om11_04

[Object]
nickname = om11_04_panel03
pos = 200, -652, 0
rotate = -90, 0, 5
archetype = space_solar_pnl
parent = om11_04

[Object]
nickname = om11_04_panel04
pos = 200, -652, 0
rotate = 90, 0, 0
archetype = space_solar_pnl
parent = om11_04

[Object]
nickname = om11_04_panel05
pos = 250, -405, 50
rotate = 135, 0, 100
archetype = space_panel_damaged_01
parent = om11_04

[Object]
nickname = om11_04_panel06
pos = 200, -391, 0
rotate = 90, -45, 5
archetype = space_solar_pnl
parent = om11_04

[Object]
nickname = om11_04_panel07
pos = 200, -398, 0
rotate = -90, 45, -5
archetype = space_solar_pnl
parent = om11_04

[Object]
nickname = om11_04_panel08
pos = 200, -399, 0
rotate = -90, -45, -4
archetype = space_solar_pnl
parent = om11_04

[Object]
nickname = om11_04_tanks01
pos = 250, -850, 0
rotate = 0, 180, 20
archetype = space_tanklx4_dmg
parent = om11_04
'''