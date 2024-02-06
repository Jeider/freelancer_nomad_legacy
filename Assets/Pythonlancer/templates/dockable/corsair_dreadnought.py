from templates.space_object_template import SpaceObjectTemplate


class CorsairDreadnoughtDestroyed(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'om2_02'
    TEMPLATE = '''[Object]
nickname = om2_02
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = sw_center_200_root
ids_name = 203857
ids_info = 065768
reputation = co_grp
behavior = NOTHING

[Object]
nickname = om2_02_locked_dock_old_root
pos = -310, -175, -280
rotate = 0, 180, 0
archetype = space_locked_dock
parent = om2_02

[Object]
nickname = om2_02_FRONT_root01
pos = 1740, -210, 0
rotate = 20, 90, 0
archetype = space_station_small_root
parent = om2_02

[Object]
nickname = om2_02_FRONT_industrialA01
pos = 1490, -240, 150
rotate = 0, 110, 0
archetype = space_industrial02a
parent = om2_02

[Object]
nickname = om2_02_FRONT_industrialA02
pos = 1490, -180, -150
rotate = -15, -110, 0
archetype = space_industrial02a
parent = om2_02

[Object]
nickname = om2_02_FRONT_industrialA04
pos = 1262, -180, -233
rotate = 20, -110, 0
archetype = space_industrial02a
parent = om2_02

[Object]
nickname = om2_02_FRONT_industrialA08
pos = 1440, -360, 0
rotate = -30, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = om2_02

[Object]
nickname = om2_02_FRONT_cntrl_twr01
pos = 1450, -220, 0
rotate = 10, 0, 0
archetype = space_control_tower
parent = om2_02

[Object]
nickname = om2_02_FRONT_cntrl_twr02
pos = 1450, -280, 0
rotate = 0, 0, 20
archetype = space_control_tower
parent = om2_02

[Object]
nickname = om2_02_FRONT_cntrl_twr04
pos = 1440, -160, 0
rotate = 180, 0, 0
archetype = space_medium_control_tower
parent = om2_02

[Object]
nickname = om2_02_FRONT_cntrl_twr05
pos = 1340, -120, 0
rotate = 175, 0, -10
archetype = space_control_tower
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S1_ind03
pos = 195, -118, -280
rotate = 0, 90, 0
archetype = space_industriala
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S1_ind04
pos = 195, -232, -280
rotate = 0, 90, 0
archetype = space_industriala
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S1_hab03
pos = 260, -175, -300
rotate = 90, 90, 0
archetype = space_habitat_wide
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S1_dock01
pos = 170, -175, -240
rotate = 0, 160, 0
archetype = space_industrial02a
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S2_ind01
pos = -35, -118, -280
rotate = 0, 90, 0
archetype = space_industrial02a
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S2_ind02
pos = -35, -232, -280
rotate = 0, 90, 0
archetype = space_industrial02a
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S2_ind03
pos = -265, -118, -280
rotate = 0, 90, 0
archetype = space_industriala
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S2_ind04
pos = -265, -232, -280
rotate = 0, 90, 0
archetype = space_industriala
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S2_hab01
pos = 9, -175, -330
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S2_hab02
pos = -80, -175, -330
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S2_hab03
pos = -200, -175, -300
rotate = 90, 90, 0
archetype = space_habitat_wide
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S3_ind01
pos = -495, -118, -280
rotate = 0, 90, 0
archetype = space_industrial02a
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S3_ind02
pos = -495, -232, -280
rotate = 0, 90, 0
archetype = space_industrial02a
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S3_hab01
pos = -451, -175, -330
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S3_hab02
pos = -540, -175, -330
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = om2_02

[Object]
nickname = om2_02_TOP_S1_panel04
pos = 160, 40, 100
rotate = -75, 180, 0
archetype = space_station_panel
parent = om2_02

[Object]
nickname = om2_02_TOP_S1_panel07
pos = -200, 20, 0
rotate = -90, 90, 0
archetype = space_station_panel
parent = om2_02

[Object]
nickname = om2_02_TOP_S1_panel09
pos = -335, 40, -120
rotate = -80, -10, 0
archetype = space_station_panel
parent = om2_02

[Object]
nickname = om2_02_TOP_S1_panel10
pos = 160, 40, -100
rotate = -75, 0, 0
archetype = space_station_panel
parent = om2_02

[Object]
nickname = om2_02_TOP_S2_panel14
pos = -341.5, 34, -86.5
rotate = -100, 170, 0
archetype = space_station_panel
parent = om2_02

[Object]
nickname = om2_02_TOP_S2_panel17
pos = -170, 40, 100
rotate = -75, 180, 0
archetype = space_station_panel
parent = om2_02

[Object]
nickname = om2_02_TOP_S2_panel18
pos = -170, 31, 67
rotate = -105, 0, 0
archetype = space_station_panel
parent = om2_02

[Object]
nickname = om2_02_TOP_S2_panel19
pos = -170, 40, -100
rotate = -75, 0, 0
archetype = space_station_panel
parent = om2_02

[Object]
nickname = om2_02_TOP_S2_panel20
pos = -170, 31, -67
rotate = -105, 180, 0
archetype = space_station_panel
parent = om2_02

[Object]
nickname = om2_02_TOP_S1_cntrl_A01
pos = -330, -30, 0
rotate = 0, 90, 0
archetype = space_control_tower
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S4_ind02
pos = 195, -58, -160
rotate = 0, 90, 0
archetype = space_industrial02a
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S4_ind03
pos = -35, -58, -170
rotate = 0, 90, 0
archetype = space_industrial01a
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S4_ind04
pos = -265, -58, -160
rotate = 0, 90, 0
archetype = space_industrial02a
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S4_ind05
pos = -495, -58, -170
rotate = 0, 90, 0
archetype = space_industrial01a
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S4_tanks01
pos = 195, -88, -210
rotate = 0, -45, 90
archetype = space_tankl2x2
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S4_tanks02
pos = -265, -88, -210
rotate = 0, -45, 90
archetype = space_tankl2x2
parent = om2_02

[Object]
nickname = om2_02_TOP_S2_ind02
pos = 188, 100, 0
rotate = 0, 90, 0
archetype = space_industrial02a
parent = om2_02

[Object]
nickname = om2_02_TOP_S2_cntrl_twr01
pos = 0, 70, 0
rotate = 180, 0, 0
archetype = space_control_tower
parent = om2_02

[Object]
nickname = om2_02_TOP_S2_cntrl_twr02
pos = 0, 162, 0
rotate = 0, 90, 0
archetype = space_medium_control_tower
parent = om2_02

[Object]
nickname = om2_02_FINAL_dome01
pos = 0, 185, 0
rotate = 0, 0, -15
archetype = space_dome_dmg2
parent = om2_02

[Object]
nickname = om2_02_FINAL_control01
pos = -90, 80, 0
rotate = -30, -105, 0
archetype = space_control_block
parent = om2_02

[Object]
nickname = om2_02_LEFT_S5_ind04
pos = -265, -262, 160
rotate = 0, 90, 0
archetype = space_industrial02a
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S5_ind02
pos = 195, -262, -160
rotate = 0, 90, 0
archetype = space_industrial02a
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S5_ind03
pos = -35, -262, -170
rotate = 0, 90, 0
archetype = space_industrial01a
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S5_ind04
pos = -265, -262, -160
rotate = 0, 90, 0
archetype = space_industrial02a
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S5_ind05
pos = -495, -262, -170
rotate = 0, 90, 0
archetype = space_industrial01a
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S5_tanks01
pos = 195, -232, -210
rotate = 0, 45, 90
archetype = space_tankl2x2
parent = om2_02

[Object]
nickname = om2_02_RIGHT_S5_tanks02
pos = -265, -232, -210
rotate = 0, 45, 90
archetype = space_tankl2x2
parent = om2_02

[Object]
nickname = om2_02_BOTTOM_S1_core02
pos = -265, -210, 0
rotate = 0, 0, 0
archetype = sw_center_200
parent = om2_02

[Object]
nickname = om2_02_BOTTOM_S1_ind02
pos = 20, -290, 0
rotate = 0, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = om2_02

[Object]
nickname = om2_02_BOTTOM_S1_ind03
pos = -440, -290, 0
rotate = 0, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = om2_02

[Object]
nickname = om2_02_BOTTOM_S1_ind04
pos = 140, -280, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = om2_02

[Object]
nickname = om2_02_BOTTOM_S1_ind05
pos = -90, -260, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = om2_02

[Object]
nickname = om2_02_BOTTOM_S1_cntrl_twr02
pos = -265, -320, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = om2_02

[Object]
nickname = om2_02_BOTTOM_S1_cntrl_twr04
pos = -265, -385, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = om2_02

[Object]
nickname = om2_02_ENGINE_S1_cntrl_twr02
pos = -570, -160, -120
rotate = 0, 45, 90
archetype = space_medium_control_tower
parent = om2_02

[Object]
nickname = om2_02_ENGINE_S1_engine02
pos = -610, -58, -170
rotate = 0, 0, 90
archetype = space_large_engine
parent = om2_02

[Object]
nickname = om2_02_ENGINE_S1_engine04
pos = -610, -262, -170
rotate = 0, 0, 90
archetype = space_large_engine
parent = om2_02

[Object]
nickname = om2_02_GUN01_ind01
pos = 220, 20, 43
rotate = -10, 105, 90
archetype = space_industrial02d
parent = om2_02

[Object]
nickname = om2_02_GUN01_ind02
pos = 225, 20, -43
rotate = 10, -105, 90
archetype = space_industrial02d
parent = om2_02

[Object]
nickname = om2_02_GUN01_ind03
pos = 195, -58, 160
rotate = 0, -90, 0
archetype = space_industrial02a
parent = om2_02

[Object]
nickname = om2_02_GUN01_girder02
pos = 1320, -80, 80
rotate = 90, 0, 45
archetype = space_beaml_dmg
parent = om2_02

[Object]
nickname = om2_02_GUN01_girder03
pos = 1250, 50, -60
rotate = 90, 0, 40
archetype = space_girdera
parent = om2_02

[Object]
nickname = om2_02_GUN01_girder04
pos = 1250, 80, -60
rotate = 90, 0, 40
archetype = space_girdera
parent = om2_02

[Object]
nickname = om2_02_GUN01_girder05
pos = 1360, 29, 20
rotate = 0, 80, 0
archetype = space_beaml_dmg
parent = om2_02

[Object]
nickname = om2_02_GUN01_girder06
pos = 1360, -1, 100
rotate = 80, 0, 90
archetype = space_beaml_dmg
parent = om2_02

[Object]
nickname = om2_02_GUN01_girder08
pos = 1340, 11, 20
rotate = 0, -90, 0
archetype = space_beaml_dmg
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_TWR01
pos = 100, -160, -50
rotate = 10, 0, 50
archetype = space_control_tower
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_TWR02
pos = -265, -140, 165
rotate = 90, 15, 90
archetype = space_medium_control_tower
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_IND01
pos = 1340, -120, 0
rotate = -80, 0, -20
archetype = space_industrialc
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_IND02
pos = 1250, 20, 0
rotate = 0, -20, 45
archetype = space_industriala
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_IND03
pos = -35, -58, 170
rotate = 0, 90, 0
archetype = space_industrial01a
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_IND04
pos = -265, -58, 160
rotate = 0, 90, 0
archetype = space_industrial02a
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_IND05
pos = -25, -160, 115
rotate = 0, 105, 5
archetype = space_industrial02a
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_IND06
pos = -410, -80, 0
rotate = 0, 0, 45
archetype = space_industriala
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_IND07
pos = -410, -210, 120
rotate = 100, 20, 20
archetype = space_industriala
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_IND08
pos = -310, -175, -200
rotate = 0, 0, 0
archetype = space_industrial02a
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_IND09
pos = -495, -312, 170
rotate = -20, 90, 0
archetype = space_industrial01a
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_GIRDER01
pos = -490, -175, -160
rotate = 0, 0, 0
archetype = space_beaml_dmg
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_GIRDER02
pos = -411, -175, -330
rotate = 0, 0, 0
archetype = space_girdera
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_GIRDER03
pos = -431, -140, -330
rotate = 0, 0, 0
archetype = space_girdera
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_GIRDER04
pos = -491, -170, -330
rotate = -10, 0, 0
archetype = space_girdera
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_GIRDER05
pos = -570, -160, -60
rotate = 0, 170, 0
archetype = space_girdera
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_GIRDER06
pos = -495, -160, 170
rotate = 0, 90, 75
archetype = space_beaml_dmg
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_GIRDER07
pos = -495, -215, -170
rotate = 1, 20, 20
archetype = space_girdera
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_GIRDER08
pos = -535, -312, 170
rotate = -40, 160, 0
archetype = space_girdera
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_GIRDER09
pos = 240, -160, -50
rotate = 20, 90, 180
archetype = space_beaml_dmg
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_GIRDER10
pos = 220, -160, 50
rotate = 0, -90, 0
archetype = space_beaml_dmg
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_GIRDER11
pos = 40, -210, 0
rotate = -5, 90, 0
archetype = space_girdera
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_GIRDER12
pos = 195, -210, 160
rotate = 90, 0, 0
archetype = space_beaml_dmg
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_GIRDER13
pos = -10, -190, 160
rotate = 40, 40, 0
archetype = space_beaml_dmg
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_GIRDER14
pos = 320, 40, 80
rotate = 0, 90, 0
archetype = space_beaml_dmg
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_GIRDER15
pos = 390, 40, 0
rotate = 0, 0, 0
archetype = space_beamx_dmg
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_GIRDER16
pos = 320, -10, -50
rotate = -30, -90, 180
archetype = space_beaml_dmg
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_GIRDER17
pos = 1450, -220, 0
rotate = 5, -70, 0
archetype = space_girdera
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_GIRDER18
pos = 1450, -220, 0
rotate = 0, 0, 0
archetype = space_beaml_dmg
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_GIRDER19
pos = 1340, -410, 0
rotate = -100, -90, 0
archetype = space_girdera
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_GIRDER20
pos = 1340, -430, 0
rotate = -85, 0, 0
archetype = space_girdera
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_TANK01
pos = 1240, -160, 0
rotate = 0, 0, 0
archetype = space_tankl2x2
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_TANK02
pos = 1240, -160, 0
rotate = 0, 0, 0
archetype = space_tankl2x2
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_TANK03
pos = 1240, -160, 0
rotate = 0, 0, 0
archetype = space_tankl2x2
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_TANK04
pos = 1240, -160, 0
rotate = 0, 0, 0
archetype = space_tankl2x2
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_TANK05
pos = 1240, -160, 0
rotate = 0, 0, 0
archetype = space_tankl2x2
parent = om2_02

[Object]
nickname = om2_02_DAMAGE_TANK06
pos = 1240, -160, 0
rotate = 0, 0, 0
archetype = space_tankl2x2
parent = om2_02
'''


class CorsairDreadnoughtAlive(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'co_och_02'
    TEMPLATE = '''[Object]
nickname = co_och_02
pos = 550, 15, 280
rotate = 0, 90, 0
archetype = dread_core
base = co_och_02_base
reputation = co_grp
behavior = NOTHING
ids_name = 203823
ids_info = 065732

[Object]
nickname = co_och_02_dock
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = space_police01_front_dock
dock_with = co_och_02_base
base = co_och_02_base
reputation = co_grp
behavior = NOTHING
visit = 0
voice = atc_leg_m01
space_costume = syd_head, pi_pirate5_body, prop_neuralnet_a_right
difficulty_level = 13
;loadout = co_base_rock_large01_pi_01
pilot = pilot_solar_hardest
ids_name = 196722
ids_info = 065739

[Object]
nickname = co_och_02_FRONT_root01
pos = 1550, 15, 280
rotate = 0, 90, 0
archetype = space_station_small_root
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_industrialA01
pos = 1300, -65, 430
rotate = 0, 110, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_industrialA02
pos = 1300, -65, 130
rotate = 0, -110, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_industrialA03
pos = 1072, -65, 513
rotate = 0, 110, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_industrialA04
pos = 1072, -65, 47
rotate = 0, -110, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_industrialA05
pos = 980, -65, 170
rotate = 0, 0, 0
archetype = space_industriala
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_industrialA06
pos = 980, -65, 390
rotate = 0, 0, 0
archetype = space_industriala
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_industrialA07
pos = 1050, -55, 280
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_industrialA08
pos = 1250, -95, 280
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_cntrl_twr01
pos = 1260, -45, 280
rotate = 180, 0, 0
archetype = space_control_tower
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_cntrl_twr02
pos = 1260, -85, 280
rotate = 0, 0, 0
archetype = space_control_tower
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_cntrl_twr03
pos = 1050, 15, 280
rotate = 180, 0, 0
archetype = space_medium_control_tower
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_cntrl_twr04
pos = 1250, 15, 280
rotate = 180, 0, 0
archetype = space_medium_control_tower
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_cntrl_twr05
pos = 1150, 55, 280
rotate = 180, 45, 0
archetype = space_control_tower
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_industrialB01
pos = 900, 0, 567.5
rotate = 90, 0, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_industrialB02
pos = 900, 0, 452.5
rotate = 90, 0, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_industrialB03
pos = 900, 0, 337.5
rotate = 90, 0, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_industrialB04
pos = 900, 0, 222.5
rotate = 90, 0, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_industrialB05
pos = 900, 0, 107.5
rotate = 90, 0, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_industrialB06
pos = 900, 0, -7.5
rotate = 90, 0, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_habitatA01
pos = 950, 50, 530
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_habitatA02
pos = 950, 50, 375
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_habitatA03
pos = 950, 50, 30
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_och_02

[Object]
nickname = co_och_02_FRONT_habitatA04
pos = 950, 50, 185
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S1_ind01
pos = 735, 57, 560
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S1_ind02
pos = 735, -57, 560
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S1_ind03
pos = 505, 57, 560
rotate = 0, 90, 0
archetype = space_industriala
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S1_ind04
pos = 505, -57, 560
rotate = 0, 90, 0
archetype = space_industriala
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S1_hab01
pos = 779, 0, 610
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S1_hab02
pos = 690, 0, 610
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S1_hab03
pos = 570, 0, 580
rotate = 90, 90, 0
archetype = space_habitat_wide
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S1_dock01
pos = 460, 0, 560
rotate = 0, 0, 0
archetype = space_locked_dock
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S2_ind01
pos = 275, 57, 560
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S2_ind02
pos = 275, -57, 560
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S2_ind03
pos = 45, 57, 560
rotate = 0, 90, 0
archetype = space_industriala
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S2_ind04
pos = 45, -57, 560
rotate = 0, 90, 0
archetype = space_industriala
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S2_hab01
pos = 319, 0, 610
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S2_hab02
pos = 230, 0, 610
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S2_hab03
pos = 110, 0, 580
rotate = 90, 90, 0
archetype = space_habitat_wide
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S2_dock01
pos = 0, 0, 560
rotate = 0, 0, 0
archetype = space_locked_dock
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S3_ind01
pos = -185, 57, 560
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S3_ind02
pos = -185, -57, 560
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S3_hab01
pos = -141, 0, 610
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S3_hab02
pos = -230, 0, 610
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S1_ind01
pos = 735, 57, 0
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S1_ind02
pos = 735, -57, 0
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S1_ind03
pos = 505, 57, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S1_ind04
pos = 505, -57, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S1_hab01
pos = 779, 0, -50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S1_hab02
pos = 690, 0, -50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S1_hab03
pos = 570, 0, -20
rotate = 90, 90, 0
archetype = space_habitat_wide
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S1_dock01
pos = 460, 0, 0
rotate = 0, 180, 0
archetype = space_locked_dock
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S2_ind01
pos = 275, 57, 0
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S2_ind02
pos = 275, -57, 0
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S2_ind03
pos = 45, 57, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S2_ind04
pos = 45, -57, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S2_hab01
pos = 319, 0, -50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S2_hab02
pos = 230, 0, -50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S2_hab03
pos = 110, 0, -20
rotate = 90, 90, 0
archetype = space_habitat_wide
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S3_ind01
pos = -185, 57, 0
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S3_ind02
pos = -185, -57, 0
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S3_hab01
pos = -141, 0, -50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S3_hab02
pos = -230, 0, -50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_window01
pos = 650, 265, 353
rotate = 90, -15, -90
archetype = space_windows
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_window02
pos = 800, 235, 375
rotate = 90, -15, -90
archetype = space_windows
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_window03
pos = -180, 225, 376
rotate = 90, -15, -90
archetype = space_windows
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_window04
pos = -180, 225, 184
rotate = -90, 15, -90
archetype = space_windows
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_window05
pos = 800, 235, 185
rotate = -90, 15, -90
archetype = space_windows
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_window06
pos = 650, 265, 207
rotate = -90, 15, -90
archetype = space_windows
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_panel01
pos = 900, 215, 280
rotate = -75, -90, 0
archetype = space_station_panel
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_panel02
pos = 800, 215, 380
rotate = -75, 180, 0
archetype = space_station_panel
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_panel03
pos = 635, 245, 360
rotate = -105, 180, 180
archetype = space_station_panel
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_panel04
pos = 470, 215, 380
rotate = -75, 180, 0
archetype = space_station_panel
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_panel05
pos = -25, 245, 360
rotate = -105, 180, 180
archetype = space_station_panel
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_panel06
pos = -190, 215, 380
rotate = -75, 180, 0
archetype = space_station_panel
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_panel07
pos = 110, 195, 280
rotate = -90, 90, 0
archetype = space_station_panel
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_panel08
pos = -190, 215, 180
rotate = -75, 0, 0
archetype = space_station_panel
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_panel09
pos = -25, 245, 200
rotate = -105, 0, 180
archetype = space_station_panel
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_panel10
pos = 470, 215, 180
rotate = -75, 0, 0
archetype = space_station_panel
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_panel11
pos = 635, 245, 200
rotate = -105, 0, 180
archetype = space_station_panel
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_panel12
pos = 800, 215, 180
rotate = -75, 0, 0
archetype = space_station_panel
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S2_panel13
pos = -190, 206, 213
rotate = -105, 180, 0
archetype = space_station_panel
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S2_panel14
pos = -25, 236, 233
rotate = -75, 180, 180
archetype = space_station_panel
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S2_panel15
pos = -190, 206, 347
rotate = -105, 0, 0
archetype = space_station_panel
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S2_panel16
pos = -25, 236, 327
rotate = -75, 0, 180
archetype = space_station_panel
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S2_panel17
pos = 140, 215, 380
rotate = -75, 180, 0
archetype = space_station_panel
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S2_panel18
pos = 140, 206, 347
rotate = -105, 0, 0
archetype = space_station_panel
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S2_panel19
pos = 140, 215, 180
rotate = -75, 0, 0
archetype = space_station_panel
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S2_panel20
pos = 140, 206, 213
rotate = -105, 180, 0
archetype = space_station_panel
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_cntrl_A01
pos = -20, 140, 280
rotate = 0, 90, 0
archetype = space_control_tower
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_shipyard01
pos = -80, 215, 280
rotate = 0, 90, 0
archetype = shipyard_medium
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_shipyard02
pos = -80, 230, 280
rotate = 0, 90, 0
archetype = luxury_liner
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_core01
pos = 310, 175, 280
rotate = 0, 0, 0
archetype = sw_center_200
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S1_ind01
pos = -250, 117, 280
rotate = 0, 0, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S4_ind01
pos = 735, 117, 450
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S4_ind02
pos = 505, 117, 440
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S4_ind03
pos = 275, 117, 450
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S4_ind04
pos = 45, 117, 440
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S4_ind05
pos = -185, 117, 450
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S4_tanks01
pos = 505, 87, 490
rotate = 0, 45, 90
archetype = space_tankl2x2
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S4_tanks02
pos = 45, 87, 490
rotate = 0, 45, 90
archetype = space_tankl2x2
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S4_ind01
pos = 735, 117, 110
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S4_ind02
pos = 505, 117, 120
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S4_ind03
pos = 275, 117, 110
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S4_ind04
pos = 45, 117, 120
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S4_ind05
pos = -185, 117, 110
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S4_tanks01
pos = 505, 87, 70
rotate = 0, -45, 90
archetype = space_tankl2x2
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S4_tanks02
pos = 45, 87, 70
rotate = 0, -45, 90
archetype = space_tankl2x2
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S2_ind01
pos = 740, 275, 280
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S2_ind02
pos = 498, 275, 280
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S2_ind03
pos = 86, 315, 280
rotate = 0, 90, 0
archetype = space_industrial02d
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S2_ind04
pos = -137, 315, 280
rotate = 0, 90, 0
archetype = space_industrial02d
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S2_cntrl_twr01
pos = 310, 245, 280
rotate = 180, 0, 0
archetype = space_control_tower
parent = co_och_02

[Object]
nickname = co_och_02_TOP_S2_cntrl_twr02
pos = 310, 337, 280
rotate = 0, 90, 0
archetype = space_medium_control_tower
parent = co_och_02

[Object]
nickname = co_och_02_FINAL_dome01
pos = 310, 360, 280
rotate = 0, 0, 0
archetype = space_domea
parent = co_och_02

[Object]
nickname = co_och_02_FINAL_control01
pos = 230, 215, 280
rotate = 0, -90, 0
archetype = space_control_block
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S5_ind01
pos = 735, -87, 450
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S5_ind02
pos = 505, -87, 440
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S5_ind03
pos = 275, -87, 450
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S5_ind04
pos = 45, -87, 440
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S5_ind05
pos = -185, -87, 450
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S5_tanks01
pos = 505, -57, 490
rotate = 0, -45, 90
archetype = space_tankl2x2
parent = co_och_02

[Object]
nickname = co_och_02_LEFT_S5_tanks02
pos = 45, -57, 490
rotate = 0, -45, 90
archetype = space_tankl2x2
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S5_ind01
pos = 735, -87, 110
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S5_ind02
pos = 505, -87, 120
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S5_ind03
pos = 275, -87, 110
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S5_ind04
pos = 45, -87, 120
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S5_ind05
pos = -185, -87, 110
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S5_tanks01
pos = 505, -57, 70
rotate = 0, 45, 90
archetype = space_tankl2x2
parent = co_och_02

[Object]
nickname = co_och_02_RIGHT_S5_tanks02
pos = 45, -57, 70
rotate = 0, 45, 90
archetype = space_tankl2x2
parent = co_och_02

[Object]
nickname = co_och_02_BOTTOM_S1_core01
pos = 645, -35, 280
rotate = 0, 0, 0
archetype = sw_center_200
parent = co_och_02

[Object]
nickname = co_och_02_BOTTOM_S1_core02
pos = 45, -35, 280
rotate = 0, 0, 0
archetype = sw_center_200
parent = co_och_02

[Object]
nickname = co_och_02_BOTTOM_S1_ind01
pos = 800, -115, 280
rotate = 0, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_och_02

[Object]
nickname = co_och_02_BOTTOM_S1_ind02
pos = 330, -115, 280
rotate = 0, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_och_02

[Object]
nickname = co_och_02_BOTTOM_S1_ind03
pos = -130, -115, 280
rotate = 0, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_och_02

[Object]
nickname = co_och_02_BOTTOM_S1_ind04
pos = 450, -105, 280
rotate = 0, 0, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_BOTTOM_S1_ind05
pos = 220, -85, 280
rotate = 0, 0, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_BOTTOM_S1_ind06
pos = -250, -85, 280
rotate = 0, 0, 0
archetype = space_industrial02a
parent = co_och_02

[Object]
nickname = co_och_02_BOTTOM_S1_cntrl_twr01
pos = 645, -145, 280
rotate = 0, 0, 0
archetype = space_control_tower
parent = co_och_02

[Object]
nickname = co_och_02_BOTTOM_S1_cntrl_twr02
pos = 45, -145, 280
rotate = 0, 0, 0
archetype = space_control_tower
parent = co_och_02

[Object]
nickname = co_och_02_BOTTOM_S1_cntrl_twr03
pos = 645, -210, 280
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = co_och_02

[Object]
nickname = co_och_02_BOTTOM_S1_cntrl_twr04
pos = 45, -210, 280
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = co_och_02

[Object]
nickname = co_och_02_ENGINE_S1_cntrl_twr01
pos = -260, 15, 400
rotate = 0, 45, 90
archetype = space_medium_control_tower
parent = co_och_02

[Object]
nickname = co_och_02_ENGINE_S1_cntrl_twr02
pos = -260, 15, 160
rotate = 0, 45, 90
archetype = space_medium_control_tower
parent = co_och_02

[Object]
nickname = co_och_02_ENGINE_S1_ind01
pos = -240, 15, 280
rotate = 90, 0, 0
archetype = space_industriala
parent = co_och_02

[Object]
nickname = co_och_02_ENGINE_S1_engine01
pos = -300, 117, 450
rotate = 0, 0, 90
archetype = space_large_engine
parent = co_och_02

[Object]
nickname = co_och_02_ENGINE_S1_engine02
pos = -300, 117, 110
rotate = 0, 0, 90
archetype = space_large_engine
parent = co_och_02

[Object]
nickname = co_och_02_ENGINE_S1_engine03
pos = -300, -87, 450
rotate = 0, 0, 90
archetype = space_large_engine
parent = co_och_02

[Object]
nickname = co_och_02_ENGINE_S1_engine04
pos = -300, -87, 110
rotate = 0, 0, 90
archetype = space_large_engine
parent = co_och_02

[Object]
nickname = co_och_02_ENGINE_S1_engine05
pos = -290, 15, 280
rotate = 0, 0, 90
archetype = space_large_engine
parent = co_och_02

[Object]
nickname = co_och_02_ENGINE_S1_engine06
pos = -285, 15, 400
rotate = 0, 0, 90
archetype = space_engine
parent = co_och_02

[Object]
nickname = co_och_02_ENGINE_S1_engine07
pos = -285, 15, 160
rotate = 0, 0, 90
archetype = space_engine
parent = co_och_02

[Object]
nickname = co_och_02_GUN01_ind01
pos = 1150, 35, 280
rotate = 90, 0, 0
archetype = space_industriala
parent = co_och_02

[Object]
nickname = co_och_02_GUN01_ind02
pos = 1060, 195, 280
rotate = 0, 0, 45
archetype = space_industriala
parent = co_och_02

[Object]
nickname = co_och_02_GUN01_ind04
pos = 1315, 195, 280
rotate = 0, -90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN01_ind05
pos = 1315, 195, 340
rotate = 0, -90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN01_ind06
pos = 1315, 195, 220
rotate = 0, -90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN01_ind07
pos = 1280, 195, 340
rotate = 0, -90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN01_ind08
pos = 1280, 195, 280
rotate = 0, -90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN01_ind09
pos = 1280, 195, 220
rotate = 0, -90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN01_ind10
pos = 1240, 195, 280
rotate = 0, 90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN01_ind11
pos = 1240, 195, 340
rotate = 0, 90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN01_ind12
pos = 1240, 195, 220
rotate = 0, 90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN01_girder01
pos = 1060, 175, 340
rotate = 90, 0, 45
archetype = space_girdera
parent = co_och_02

[Object]
nickname = co_och_02_GUN01_girder02
pos = 1060, 205, 340
rotate = 90, 0, 45
archetype = space_girdera
parent = co_och_02

[Object]
nickname = co_och_02_GUN01_girder03
pos = 1060, 175, 220
rotate = 90, 0, 45
archetype = space_girdera
parent = co_och_02

[Object]
nickname = co_och_02_GUN01_girder04
pos = 1060, 205, 220
rotate = 90, 0, 45
archetype = space_girdera
parent = co_och_02

[Object]
nickname = co_och_02_GUN01_girder05
pos = 970, 204, 280
rotate = 0, 90, 0
archetype = space_girdera
parent = co_och_02

[Object]
nickname = co_och_02_GUN01_girder06
pos = 970, 204, 340
rotate = 0, 90, 0
archetype = space_girdera
parent = co_och_02

[Object]
nickname = co_och_02_GUN01_girder07
pos = 970, 204, 220
rotate = 0, 90, 0
archetype = space_girdera
parent = co_och_02

[Object]
nickname = co_och_02_GUN01_girder08
pos = 970, 186, 280
rotate = 0, 90, 0
archetype = space_girdera
parent = co_och_02

[Object]
nickname = co_och_02_GUN01_girder09
pos = 970, 186, 340
rotate = 0, 90, 0
archetype = space_girdera
parent = co_och_02

[Object]
nickname = co_och_02_GUN01_girder10
pos = 970, 186, 220
rotate = 0, 90, 0
archetype = space_girdera
parent = co_och_02

[Object]
nickname = co_och_02_GUN02_ind01
pos = 1550, -35, 280
rotate = 90, 0, 0
archetype = space_industriala
parent = co_och_02

[Object]
nickname = co_och_02_GUN02_ind02
pos = 1465, 115, 280
rotate = 0, 0, 45
archetype = space_industriala
parent = co_och_02

[Object]
nickname = co_och_02_GUN02_ind04
pos = 1715, 115, 315
rotate = 0, -90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN02_ind05
pos = 1715, 115, 245
rotate = 0, -90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN02_ind06
pos = 1680, 115, 315
rotate = 0, -90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN02_ind07
pos = 1680, 115, 245
rotate = 0, -90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN02_ind08
pos = 1640, 115, 315
rotate = 0, 90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN02_ind09
pos = 1640, 115, 245
rotate = 0, 90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN02_girder01
pos = 1565, 15, 340
rotate = -90, 0, 45
archetype = space_girder
parent = co_och_02

[Object]
nickname = co_och_02_GUN02_girder02
pos = 1565, 15, 220
rotate = -90, 0, 45
archetype = space_girder
parent = co_och_02

[Object]
nickname = co_och_02_GUN02_girder03
pos = 1365, 115, 315
rotate = 0, 90, 0
archetype = space_girdera
parent = co_och_02

[Object]
nickname = co_och_02_GUN02_girder04
pos = 1365, 115, 245
rotate = 0, 90, 0
archetype = space_girdera
parent = co_och_02

[Object]
nickname = co_och_02_GUN03_ind01
pos = 645, -175, 280
rotate = 90, 0, 0
archetype = space_industriala
parent = co_och_02

[Object]
nickname = co_och_02_GUN03_ind02
pos = 570, -325, 280
rotate = 0, 0, 45
archetype = space_industriala
parent = co_och_02

[Object]
nickname = co_och_02_GUN03_ind04
pos = 820, -325, 315
rotate = 0, -90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN03_ind05
pos = 820, -325, 245
rotate = 0, -90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN03_ind06
pos = 785, -325, 315
rotate = 0, -90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN03_ind07
pos = 785, -325, 245
rotate = 0, -90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN03_ind08
pos = 745, -325, 315
rotate = 0, 90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN03_ind09
pos = 745, -325, 245
rotate = 0, 90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN03_girder01
pos = 570, -325, 340
rotate = -90, 0, -45
archetype = space_girdera
parent = co_och_02

[Object]
nickname = co_och_02_GUN03_girder02
pos = 570, -325, 220
rotate = -90, 0, -45
archetype = space_girdera
parent = co_och_02

[Object]
nickname = co_och_02_GUN03_girder03
pos = 470, -325, 315
rotate = 0, 90, 0
archetype = space_girdera
parent = co_och_02

[Object]
nickname = co_och_02_GUN03_girder04
pos = 470, -325, 245
rotate = 0, 90, 0
archetype = space_girdera
parent = co_och_02

[Object]
nickname = co_och_02_GUN04_ind01
pos = 45, -175, 280
rotate = 90, 0, 0
archetype = space_industriala
parent = co_och_02

[Object]
nickname = co_och_02_GUN04_ind02
pos = 130, -325, 280
rotate = 0, 0, 45
archetype = space_industriala
parent = co_och_02

[Object]
nickname = co_och_02_GUN04_ind04
pos = -110, -325, 315
rotate = 0, 90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN04_ind05
pos = -110, -325, 245
rotate = 0, 90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN04_ind06
pos = -75, -325, 315
rotate = 0, 90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN04_ind07
pos = -75, -325, 245
rotate = 0, 90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN04_ind08
pos = -35, -325, 315
rotate = 0, -90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN04_ind09
pos = -35, -325, 245
rotate = 0, -90, 0
archetype = space_industrial01c
parent = co_och_02

[Object]
nickname = co_och_02_GUN04_girder01
pos = 130, -325, 340
rotate = -90, 0, 45
archetype = space_girdera
parent = co_och_02

[Object]
nickname = co_och_02_GUN04_girder02
pos = 130, -325, 220
rotate = -90, 0, 45
archetype = space_girdera
parent = co_och_02

[Object]
nickname = co_och_02_GUN04_girder03
pos = 230, -325, 315
rotate = 0, -90, 0
archetype = space_girdera
parent = co_och_02

[Object]
nickname = co_och_02_GUN04_girder04
pos = 230, -325, 245
rotate = 0, -90, 0
archetype = space_girdera
parent = co_och_02
'''
