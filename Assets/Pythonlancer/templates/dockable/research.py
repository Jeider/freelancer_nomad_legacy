from templates.space_object_template import SpaceObjectTemplate


class KyushuResearch(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_ksu_04'
    TEMPLATE = '''[Object]
nickname = ku_ksu_04
ids_name = 203744
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_police02
ids_info = 065659
base = ku_ksu_04_base
dock_with = ku_ksu_04_base
visit = 16
reputation = ku_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = sc_scientist2_head, sc_scientist3_body, prop_neuralnet_d
difficulty_level = 10
pilot = pilot_solar_hardest

[Object]
nickname = ku_ksu_04_lightpanel01
pos = 563, 0, 0
rotate = 0, 90, 0
archetype = space_industriala
loadout = lightpanels_x3
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_lightpanel02
pos = 308, 0, 0
rotate = 90, 45, 90
archetype = space_industriala
loadout = lightpanels_x3
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_ind01
pos = 73, 0, 0
rotate = 0, -90, 0
archetype = space_industrialc
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_ctrl_twr01
pos = 148, 0, 0
rotate = 90, 90, 0
archetype = space_control_tower
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_ctrl_twr02
pos = 78, 0, 0
rotate = 90, 90, 0
archetype = space_control_tower
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_ctrl_twr03
pos = 8, 0, 0
rotate = 90, 90, 0
archetype = space_control_tower
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatA01
pos = 113, -162, 0
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatA02
pos = 113, 162, 0
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatA03
pos = 113, 0, -162
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatA04
pos = 113, 0, 162
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatA05
pos = 113, -115, 115
rotate = 45, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatA06
pos = 113, -115, -115
rotate = -45, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatA07
pos = 113, 115, -115
rotate = 45, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatA08
pos = 113, 115, 115
rotate = -45, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatB01
pos = 43, -162, 0
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatB02
pos = 43, 162, 0
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatB03
pos = 43, 0, -162
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatB04
pos = 43, 0, 162
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatB05
pos = 43, -115, 115
rotate = 45, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatB06
pos = 43, -115, -115
rotate = -45, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatB07
pos = 43, 115, -115
rotate = 45, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatB08
pos = 43, 115, 115
rotate = -45, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_tank01
pos = -47, 100, 0
rotate = 0, 90, 180
archetype = space_tanks2
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_tank02
pos = -47, -100, 0
rotate = 0, 90, 0
archetype = space_tanks2
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_tank03
pos = -47, 0, 100
rotate = -90, 0, 90
archetype = space_tanks2
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_tank04
pos = -47, 0, -100
rotate = 90, 0, -90
archetype = space_tanks2
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_tank05
pos = -47, -75, 75
rotate = 90, 135, 90
archetype = space_tanks2
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_tank06
pos = -47, -75, -75
rotate = 90, 45, 90
archetype = space_tanks2
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_tank07
pos = -47, 75, 75
rotate = 90, -135, 90
archetype = space_tanks2
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_tank08
pos = -47, 75, -75
rotate = 90, -45, 90
archetype = space_tanks2
parent = ku_ksu_04
'''


class SiriusResearch(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'sig42_02'
    TEMPLATE = '''[Object]
nickname = sig42_02
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_police01
ids_name = 203698
ids_info = 065615
behavior = NOTHING
base = sig42_02_base
dock_with = sig42_02_base
reputation = kc_grp
voice = atc_leg_f01
space_costume = pl_female3_head, sc_female1_body, prop_neuralnet_d

[Object]
nickname = sig42_02_girderA01
pos = 0, -375, 0
rotate = 0, 90, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_girderA02
pos = 0, -375, 0
rotate = 0, -90, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_girderA03
pos = 0, -375, 0
rotate = 0, 180, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_girderA04
pos = 0, -375, 0
rotate = 0, 0, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_girderA05
pos = -20, -110, 0
rotate = -90, 0, 0
archetype = space_girderc
parent = sig42_02

[Object]
nickname = sig42_02_girderA06
pos = 20, -110, 0
rotate = -90, 0, 0
archetype = space_girderc
parent = sig42_02

[Object]
nickname = sig42_02_ctrl_twr01
pos = 0, -375, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = sig42_02

[Object]
nickname = sig42_02_ctrl_twr02
pos = 0, -200, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = sig42_02

[Object]
nickname = sig42_02_ctrl_hab01
pos = 0, -290, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sig42_02

[Object]
nickname = sig42_02_indA01
pos = 0, -375, -376
rotate = 0, 0, 0
archetype = space_industriala
parent = sig42_02

[Object]
nickname = sig42_02_indA02
pos = 376, -375, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = sig42_02

[Object]
nickname = sig42_02_indA03
pos = -376, -375, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = sig42_02

[Object]
nickname = sig42_02_indA04
pos = 0, -375, -626
rotate = 0, 0, 0
archetype = space_industriala
parent = sig42_02

[Object]
nickname = sig42_02_indA05
pos = 626, -375, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = sig42_02

[Object]
nickname = sig42_02_indA06
pos = -626, -375, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = sig42_02

[Object]
nickname = sig42_02_indA07
pos = 180, -375, 180
rotate = 0, 45, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = sig42_02

[Object]
nickname = sig42_02_indA08
pos = 180, -375, -180
rotate = 0, -45, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = sig42_02

[Object]
nickname = sig42_02_indA09
pos = -180, -375, 180
rotate = 0, -45, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = sig42_02

[Object]
nickname = sig42_02_indA10
pos = -180, -375, -180
rotate = 0, 45, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = sig42_02

[Object]
nickname = sig42_02_indA11
pos = 0, -375, 376
rotate = 0, 0, 0
archetype = space_industriala
parent = sig42_02

[Object]
nickname = sig42_02_indA12
pos = 0, -375, 626
rotate = 0, 0, 0
archetype = space_industriala
parent = sig42_02

[Object]
nickname = sig42_02_panelA01
pos = 0, -310, 376
rotate = 0, 0, 0
archetype = hidden_connect
loadout = space_sirius_panels01
parent = sig42_02

[Object]
nickname = sig42_02_panelA02
pos = 0, -310, 626
rotate = 0, 0, 0
archetype = hidden_connect
loadout = space_sirius_panels02
parent = sig42_02

[Object]
nickname = sig42_02_panelA03
pos = 0, -310, -376
rotate = 0, 0, 0
archetype = hidden_connect
loadout = space_sirius_panels01
parent = sig42_02

[Object]
nickname = sig42_02_panelA04
pos = 0, -310, -626
rotate = 0, 180, 0
archetype = hidden_connect
loadout = space_sirius_panels02
parent = sig42_02

[Object]
nickname = sig42_02_panelA05
pos = 0, -440, 376
rotate = 180, 0, 0
archetype = hidden_connect
loadout = space_sirius_panels01
parent = sig42_02

[Object]
nickname = sig42_02_panelA06
pos = 0, -440, 626
rotate = 180, 180, 0
archetype = hidden_connect
loadout = space_sirius_panels02
parent = sig42_02

[Object]
nickname = sig42_02_panelA07
pos = 0, -440, -376
rotate = 180, 0, 0
archetype = hidden_connect
loadout = space_sirius_panels01
parent = sig42_02

[Object]
nickname = sig42_02_panelA08
pos = 0, -440, -626
rotate = 180, 0, 0
archetype = hidden_connect
loadout = space_sirius_panels02
parent = sig42_02

[Object]
nickname = sig42_02_domeA01
pos = 0, -375, 875
rotate = 0, 0, 0
archetype = space_domea
parent = sig42_02

[Object]
nickname = sig42_02_domeA02
pos = 0, -375, -880
rotate = 0, 0, 0
archetype = space_domea
parent = sig42_02

[Object]
nickname = sig42_02_domeA03
pos = 880, -375, 0
rotate = 0, 90, 0
archetype = space_domea
parent = sig42_02

[Object]
nickname = sig42_02_domeA04
pos = -880, -375, 0
rotate = 0, 0, 0
archetype = space_domea
parent = sig42_02

[Object]
nickname = sig42_02_girderB01
pos = 610, -489.6999999999998, 0
rotate = -19, 90, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_girderB02
pos = -610, -489.6999999999998, 0
rotate = -19, -90, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_girderB03
pos = 180, -375, 180
rotate = 0, 45, 0
archetype = space_girder
parent = sig42_02

[Object]
nickname = sig42_02_girderB04
pos = -180, -375, 180
rotate = 0, -45, 0
archetype = space_girder
parent = sig42_02

[Object]
nickname = sig42_02_girderB05
pos = 180, -375, -180
rotate = 0, -45, 0
archetype = space_girder
parent = sig42_02

[Object]
nickname = sig42_02_girderB06
pos = -180, -375, -180
rotate = 0, 45, 0
archetype = space_girder
parent = sig42_02

[Object]
nickname = sig42_02_tankl01
pos = 0, -520, 0
rotate = 0, 0, 0
archetype = space_tanklx4
parent = sig42_02

[Object]
nickname = sig42_02_tankl02
pos = 215, -489.6999999999998, 0
rotate = 0, 90, 0
archetype = space_tankl4
parent = sig42_02

[Object]
nickname = sig42_02_tankl03
pos = 480, -489.6999999999998, 0
rotate = 0, 90, 0
archetype = space_tankl4
parent = sig42_02

[Object]
nickname = sig42_02_tankl04
pos = -215, -489.6999999999998, 0
rotate = 0, 90, 0
archetype = space_tankl4
parent = sig42_02

[Object]
nickname = sig42_02_tankl05
pos = -480, -489.6999999999998, 0
rotate = 0, 90, 0
archetype = space_tankl4
parent = sig42_02

[Object]
nickname = sig42_02_tankl06
pos = 0, -562.3999999999996, 148
rotate = 0, 0, 0
archetype = space_tankl2
parent = sig42_02

[Object]
nickname = sig42_02_tankl07
pos = 0, -562.3999999999996, -148
rotate = 0, 0, 0
archetype = space_tankl2
parent = sig42_02

[Object]
nickname = sig42_02_habitatA01
pos = 125, -375, 376
rotate = 0, 0, -90
archetype = space_habitat_wide
parent = sig42_02

[Object]
nickname = sig42_02_habitatA02
pos = -125, -375, 376
rotate = 0, 0, 90
archetype = space_habitat_wide
parent = sig42_02

[Object]
nickname = sig42_02_habitatA03
pos = 125, -375, -376
rotate = 0, 0, 90
archetype = space_habitat_wide
parent = sig42_02

[Object]
nickname = sig42_02_habitatA04
pos = -125, -375, -376
rotate = 0, 0, 90
archetype = space_habitat_wide
parent = sig42_02

[Object]
nickname = sig42_02_habitatA05
pos = 376, -375, 125
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = sig42_02

[Object]
nickname = sig42_02_habitatA06
pos = 376, -375, -125
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = sig42_02

[Object]
nickname = sig42_02_habitatA07
pos = -376, -375, 125
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = sig42_02

[Object]
nickname = sig42_02_habitatA08
pos = -376, -375, -125
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = sig42_02

[Object]
nickname = sig42_02_ctrl_twr01
pos = 400, -375, 400
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = sig42_02

[Object]
nickname = sig42_02_ctrl_twr02
pos = -400, -375, 400
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = sig42_02

[Object]
nickname = sig42_02_ctrl_twr03
pos = 400, -375, -400
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = sig42_02

[Object]
nickname = sig42_02_ctrl_twr04
pos = -400, -375, -400
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = sig42_02

[Object]
nickname = sig42_02_habitatB01
pos = 125, -375, 626
rotate = 0, 0, 90
archetype = space_habitat_wide
parent = sig42_02

[Object]
nickname = sig42_02_habitatB02
pos = -125, -375, 626
rotate = 0, 0, 90
archetype = space_habitat_wide
parent = sig42_02

[Object]
nickname = sig42_02_habitatB03
pos = 125, -375, -626
rotate = 0, 0, 90
archetype = space_habitat_wide
parent = sig42_02

[Object]
nickname = sig42_02_habitatB04
pos = -125, -375, -626
rotate = 0, 0, 90
archetype = space_habitat_wide
parent = sig42_02

[Object]
nickname = sig42_02_habitatB05
pos = 626, -375, 125
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = sig42_02

[Object]
nickname = sig42_02_habitatB06
pos = 626, -375, -125
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = sig42_02

[Object]
nickname = sig42_02_habitatB07
pos = -626, -375, 125
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = sig42_02

[Object]
nickname = sig42_02_habitatB08
pos = -626, -375, -125
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = sig42_02

[Object]
nickname = sig42_02_habitatC01
pos = 330, -375, 626
rotate = 0, 0, -90
archetype = space_habitat_tall
parent = sig42_02

[Object]
nickname = sig42_02_habitatC02
pos = -330, -375, 626
rotate = 0, 0, 90
archetype = space_habitat_tall
parent = sig42_02

[Object]
nickname = sig42_02_habitatC03
pos = 330, -375, -626
rotate = 0, 0, -90
archetype = space_habitat_tall
parent = sig42_02

[Object]
nickname = sig42_02_habitatC04
pos = -330, -375, -626
rotate = 0, 0, 90
archetype = space_habitat_tall
parent = sig42_02

[Object]
nickname = sig42_02_habitatC05
pos = 626, -375, 330
rotate = 90, 0, 0
archetype = space_habitat_tall
parent = sig42_02

[Object]
nickname = sig42_02_habitatC06
pos = 626, -375, -330
rotate = -90, 0, 0
archetype = space_habitat_tall
parent = sig42_02

[Object]
nickname = sig42_02_habitatC07
pos = -626, -375, 330
rotate = 90, 0, 0
archetype = space_habitat_tall
parent = sig42_02

[Object]
nickname = sig42_02_habitatC08
pos = -626, -375, -330
rotate = -90, 0, 0
archetype = space_habitat_tall
parent = sig42_02

[Object]
nickname = sig42_02_girderC01
pos = 125, -375, 376
rotate = 0, 90, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_girderC02
pos = 376, -375, 125
rotate = 0, 0, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_girderC03
pos = 626, -375, 400
rotate = 0, -90, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_girderC04
pos = 400, -375, 626
rotate = 0, 180, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_girderC05
pos = -125, -375, 376
rotate = 0, -90, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_girderC06
pos = -376, -375, 125
rotate = 0, 0, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_girderC07
pos = -626, -375, 400
rotate = 0, 90, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_girderC08
pos = -400, -375, 626
rotate = 0, 180, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_girderD01
pos = 125, -375, -374
rotate = 0, 90, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_girderD02
pos = 376, -375, -125
rotate = 0, 180, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_girderD03
pos = 626, -375, -400
rotate = 0, -90, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_girderD04
pos = 400, -375, -626
rotate = 0, 0, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_girderD05
pos = -125, -375, -374
rotate = 0, -90, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_girderD06
pos = -376, -375, -175
rotate = 0, 180, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_girderD07
pos = -626, -375, -400
rotate = 0, 90, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_girderD08
pos = -400, -375, -626
rotate = 0, 0, 0
archetype = space_girdera
parent = sig42_02

[Object]
nickname = sig42_02_ctrl_block01
pos = 400, -315, 400
rotate = 0, 0, 0
archetype = space_small_control_block
parent = sig42_02

[Object]
nickname = sig42_02_ctrl_block02
pos = -400, -315, 400
rotate = 0, 45, 0
archetype = space_small_control_block
parent = sig42_02

[Object]
nickname = sig42_02_ctrl_block03
pos = 400, -315, -400
rotate = 0, 60, 0
archetype = space_small_control_block
parent = sig42_02

[Object]
nickname = sig42_02_ctrl_block04
pos = -400, -315, -400
rotate = 0, -30, 0
archetype = space_small_control_block
parent = sig42_02

[Object]
nickname = sig42_02_ctrl_block05
pos = 400, -435, 400
rotate = 180, 30, 0
archetype = space_small_control_block
parent = sig42_02

[Object]
nickname = sig42_02_ctrl_block06
pos = -400, -435, 400
rotate = 180, -60, 0
archetype = space_small_control_block
parent = sig42_02

[Object]
nickname = sig42_02_ctrl_block07
pos = 400, -435, -400
rotate = 180, -124, 0
archetype = space_small_control_block
parent = sig42_02

[Object]
nickname = sig42_02_ctrl_block08
pos = -400, -435, -400
rotate = 180, 54, 0
archetype = space_small_control_block
parent = sig42_02

[Object]
nickname = sig42_02_domeB01
pos = 400, -350, 400
rotate = 0, 0, 0
archetype = space_domeb
parent = sig42_02

[Object]
nickname = sig42_02_domeB02
pos = -400, -350, 400
rotate = 0, 0, 0
archetype = space_domeb
parent = sig42_02

[Object]
nickname = sig42_02_domeB03
pos = 400, -350, -400
rotate = 0, 0, 0
archetype = space_domeb
parent = sig42_02

[Object]
nickname = sig42_02_domeB04
pos = -400, -350, -400
rotate = 0, 0, 0
archetype = space_domeb
parent = sig42_02

[Object]
nickname = sig42_02_domeB05
pos = 400, -400, 400
rotate = 180, 0, 0
archetype = space_domeb
parent = sig42_02

[Object]
nickname = sig42_02_domeB06
pos = -400, -400, 400
rotate = 180, 0, 0
archetype = space_domeb
parent = sig42_02

[Object]
nickname = sig42_02_domeB07
pos = 400, -400, -400
rotate = 180, 0, 0
archetype = space_domeb
parent = sig42_02

[Object]
nickname = sig42_02_domeB08
pos = -400, -400, -400
rotate = 180, 0, 0
archetype = space_domeb
parent = sig42_02
'''


class RheinlandResearch(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_biz_04'
    TEMPLATE = '''[Object]
nickname = rh_biz_04
ids_name = 203613
pos = 0, 0, 0
rotate = 290, 20, -3
archetype = space_police01_front_dock
ids_info = 065549
base = rh_biz_04_base
dock_with = rh_biz_04_base
reputation = rh_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = sc_scientist2_head, sc_scientist3_body, prop_neuralnet_d_combo
difficulty_level = 5
loadout = rh_space_police01
pilot = pilot_solar_hardest

[Object]
nickname = rh_biz_04_station_root01
pos = -25, 85, -80
rotate = -20, 200, -3
archetype = space_station_root
parent = rh_biz_04

[Object]
nickname = rh_biz_04_arch01
pos = 95, -173, 316
rotate = -20, 160, 80
archetype = space_long_large_arch
loadout = space_very_long_arch
parent = rh_biz_04

[Object]
nickname = rh_biz_04_girder01
pos = 95, -173, 316
rotate = -20, 160, 80
archetype = space_girdera
parent = rh_biz_04

[Object]
nickname = rh_biz_04_girder02
pos = 160, -167, 316
rotate = -20, 160, 80
archetype = space_girdera
parent = rh_biz_04

[Object]
nickname = rh_biz_04_girder03
pos = 128, -179, 312
rotate = -20, 160, 80
archetype = space_girdera
parent = rh_biz_04

[Object]
nickname = rh_biz_04_girder04
pos = 85, -198, 302
rotate = -20, 160, 80
archetype = space_girdera
parent = rh_biz_04

[Object]
nickname = rh_biz_04_girder05
pos = 115, -158, 330
rotate = -20, 160, 80
archetype = space_girdera
parent = rh_biz_04
'''


class ForbesResearch(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_for_05'
    TEMPLATE = '''[Object]
nickname = li_for_05
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_police01
base = li_for_05_base
dock_with = li_for_05_base
reputation = li_grp
behavior = NOTHING
difficulty_level = 10
loadout = li_space_police01
pilot = pilot_solar_hardest
ids_name = 203668
ids_info = 065587
voice = atc_leg_m01
space_costume = rh_deidrich_head, sc_scientist2_body, prop_neuralnet_a_right

[Object]
nickname = li_for_05_solar_plant
pos = 0, 0, -900
rotate = 0, 90, 0
archetype = space_solar_plant
parent = li_for_05

[Object]
nickname = li_for_05_ind01
pos = 0, 0, -735
rotate = 0, 0, 0
archetype = space_industriala
parent = li_for_05

[Object]
nickname = li_for_05_ind02
pos = -200, 0, -735
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_05

[Object]
nickname = li_for_05_ind03
pos = 200, 0, -735
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_05

[Object]
nickname = li_for_05_ind04
pos = 0, 0, -510
rotate = 0, 0, 0
archetype = space_industriala
parent = li_for_05

[Object]
nickname = li_for_05_ind05
pos = 0, 0, -280
rotate = 0, 0, 0
archetype = space_industriala
parent = li_for_05

[Object]
nickname = li_for_05_cntrl_twr01
pos = 0, 0, -600
rotate = 90, 0, 45
archetype = space_medium_control_tower
parent = li_for_05

[Object]
nickname = li_for_05_cntrl_twr02
pos = 0, 0, -420
rotate = 90, 0, 45
archetype = space_medium_control_tower
parent = li_for_05

[Object]
nickname = li_for_05_habitat01
pos = 0, -90, -510
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = li_for_05

[Object]
nickname = li_for_05_habitat02
pos = 0, 90, -510
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = li_for_05

[Object]
nickname = li_for_05_habitat03
pos = -90, 0, -510
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = li_for_05

[Object]
nickname = li_for_05_habitat04
pos = 90, 0, -510
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = li_for_05

[Object]
nickname = li_for_05_girder01
pos = 0, 0, -250
rotate = 0, 0, 0
archetype = space_girder
parent = li_for_05

[Object]
nickname = li_for_05_tanks01
pos = 120, 0, -280
rotate = 0, 0, 90
archetype = space_tanklx4
parent = li_for_05

[Object]
nickname = li_for_05_tanks02
pos = -120, 0, -280
rotate = 0, 0, -90
archetype = space_tanklx4
parent = li_for_05
'''
