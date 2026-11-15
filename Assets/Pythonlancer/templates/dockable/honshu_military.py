from templates.space_object_template import SpaceObjectTemplate


class HonshuMilitaryOriginal(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_hns_02'
    TEMPLATE = '''[Object]
nickname = ku_hns_02
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = space_police01_honshu
{dock_props}

[Object]
nickname = ku_hns_02_panelA01
pos = -480, 35, -120
rotate = 15, 0, 0
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_panelA02
pos = -315, 35, -120
rotate = -15, 0, 180
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_panelA03
pos = -150, 35, -120
rotate = 15, 0, 0
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_panelA04
pos = -480, 35, 120
rotate = -15, 0, 0
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_panelA05
pos = -315, 35, 120
rotate = 15, 0, 180
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_panelA06
pos = -150, 35, 120
rotate = -15, 0, 0
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indA01
pos = -430, 135, -52
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indA02
pos = -430, 135, 54
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indA03
pos = -200, 135, -52
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indA04
pos = -200, 135, 54
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indA05
pos = -480, -85, -105
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indA06
pos = -480, -85, 0
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indA07
pos = -480, -85, 105
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indA08
pos = -250, -85, -105
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indA09
pos = -250, -85, 0
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indA10
pos = -250, -85, 105
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_panelB01
pos = 480, 35, -120
rotate = 15, 0, 0
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_panelB02
pos = 315, 35, -120
rotate = -15, 0, 180
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_panelB03
pos = 150, 35, -120
rotate = 15, 0, 0
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_panelB04
pos = 480, 35, 120
rotate = -15, 0, 0
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_panelB05
pos = 315, 35, 120
rotate = 15, 0, 180
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_panelB06
pos = 150, 35, 120
rotate = -15, 0, 0
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indB01
pos = 430, 135, -52
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indB02
pos = 430, 135, 54
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indB03
pos = 200, 135, -52
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indB04
pos = 200, 135, 54
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indB05
pos = 480, -85, -105
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indB06
pos = 480, -85, 0
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indB07
pos = 480, -85, 105
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indB08
pos = 250, -85, -105
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indB09
pos = 250, -85, 0
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indB10
pos = 250, -85, 105
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_airlockA01
pos = 0, 385, 0
rotate = 90, 0, 0
archetype = space_airlock_dummy
parent = ku_hns_02

[Object]
nickname = ku_hns_02_towerA01
pos = 0, -85, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = ku_hns_02

[Object]
nickname = ku_hns_02_towerA02
pos = 0, 135, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = ku_hns_02

[Object]
nickname = ku_hns_02_towerA03
pos = 0, 285, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = ku_hns_02

[Object]
nickname = ku_hns_02_towerA04
pos = 0, 435, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = ku_hns_02

[Object]
nickname = ku_hns_02_towerA05
pos = 0, 500, 0
rotate = 0, 0, 0
archetype = space_small_control_block
parent = ku_hns_02

[Object]
nickname = ku_hns_02_girdA01
pos = -80, 105, -125
rotate = -75, 0, -5
archetype = space_girder
parent = ku_hns_02

[Object]
nickname = ku_hns_02_girdA02
pos = -80, 105, 125
rotate = 75, 0, -5
archetype = space_girder
parent = ku_hns_02

[Object]
nickname = ku_hns_02_girdA03
pos = 80, 105, -125
rotate = -75, 0, 5
archetype = space_girder
parent = ku_hns_02

[Object]
nickname = ku_hns_02_girdA04
pos = 80, 105, 125
rotate = 75, 0, 5
archetype = space_girder
parent = ku_hns_02

[Object]
nickname = ku_hns_02_panelC01
pos = 0, 175, -130
rotate = 15, 0, 0
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_panelC02
pos = 0, 175, 120
rotate = -15, 0, 0
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indC01
pos = 0, -195, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indC02
pos = -180, -195, 0
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indC03
pos = 180, -195, 0
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = ku_hns_02

[Object]
nickname = ku_hns_02_girdB01
pos = -398, -155, 0
rotate = 0, -90, -25.5
archetype = space_girderc
parent = ku_hns_02

[Object]
nickname = ku_hns_02_girdB02
pos = 398, -155, 0
rotate = 0, 90, 25.5
archetype = space_girderc
parent = ku_hns_02

[Object]
nickname = ku_hns_02_domeA01
pos = 0, -210, -120
rotate = -90, 0, 0
archetype = space_domea
parent = ku_hns_02

[Object]
nickname = ku_hns_02_domeA02
pos = 0, -210, 120
rotate = 90, 0, 0
archetype = space_domea
parent = ku_hns_02

[Object]
nickname = ku_hns_02_towerB01
pos = 0, -305, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = ku_hns_02

[Object]
nickname = ku_hns_02_towerB02
pos = 0, -475, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = ku_hns_02

[Object]
nickname = ku_hns_02_towerB03
pos = 0, -620, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = ku_hns_02

[Object]
nickname = ku_hns_02_towerB04
pos = 0, -527, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = ku_hns_02

[Object]
nickname = ku_hns_02_airlockA02
pos = 0, -565, 0
rotate = -90, 0, 0
archetype = space_airlock_dummy
parent = ku_hns_02

[Object]
nickname = ku_hns_02_habitatA01
pos = 0, -390, 80
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_hns_02

[Object]
nickname = ku_hns_02_habitatA02
pos = 0, -390, -80
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_hns_02

[Object]
nickname = ku_hns_02_habitatA03
pos = 80, -390, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_hns_02

[Object]
nickname = ku_hns_02_habitatA04
pos = -80, -390, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_hns_02

[Object]
nickname = ku_hns_02_habitatA05
pos = 0, -390, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_hns_02

[Object]
nickname = ku_hns_02_habitatB02
pos = 0, -760, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = ku_hns_02

[Object]
nickname = ku_hns_02_habitatB03
pos = 0, -645, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_shipayrd01
pos = -300, 25, 20
rotate = -90, 0, 90
archetype = shipyard_medium
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_shipayrd02
pos = 315, 15, 20
rotate = -90, 0, 90
archetype = shipyard_medium
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_hand01
pos = -360, 100, 10
rotate = 0, 30, 0
archetype = space_hand
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_hand02
pos = -130, 100, 10
rotate = 0, 50, 0
archetype = space_hand
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_hand03
pos = -275, -50, 0
rotate = 180, 0, 0
archetype = space_hand
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_hand04
pos = 170, 100, 10
rotate = 0, 30, 0
archetype = space_hand
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_hand05
pos = 420, 100, 10
rotate = 0, 50, 0
archetype = space_hand
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_hand06
pos = 325, -50, 0
rotate = 180, 0, 0
archetype = space_hand
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_smlgird01
pos = -275, -60, 0
rotate = 0, 0, 0
archetype = space_girderb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_smlgird02
pos = -360, 110, 10
rotate = 0, 0, 0
archetype = space_girderb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_smlgird03
pos = -130, 110, 10
rotate = 0, 0, 0
archetype = space_girderb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_smlgird04
pos = 325, -60, 0
rotate = 0, 0, 0
archetype = space_girderb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_smlgird05
pos = 170, 110, 10
rotate = 0, 0, 0
archetype = space_girderb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_smlgird06
pos = 420, 110, 10
rotate = 0, 0, 0
archetype = space_girderb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_gird01
pos = 400, 15, 80
rotate = 90, 0, 0
archetype = space_girderc
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_gird02
pos = 330, 15, -60
rotate = 90, 0, 45
archetype = space_girder
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_gird03
pos = 95, 100, 0
rotate = 0, 0, 0
archetype = space_girderc
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_gird04
pos = -370, 35, -60
rotate = 90, 0, 0
archetype = space_girderc
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_gird05
pos = -350, 25, 60
rotate = 90, 0, 55
archetype = space_girder
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_gird06
pos = -100, -35, 40
rotate = -30, 0, 0
archetype = space_girderc
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_gird07
pos = 0, -45, 0
rotate = 90, 0, 0
archetype = space_girderc
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_habitat01
pos = -480, 15, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_habitat02
pos = -480, 15, -95
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_habitat03
pos = -260, 15, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_habitat04
pos = -260, 15, -95
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_habitat05
pos = 250, 15, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_habitat06
pos = 250, 15, -95
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_habitat07
pos = 480, 15, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_habitat08
pos = 480, 15, -95
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_tanks01
pos = 0, 190, 0
rotate = 90, -30, 0
archetype = space_tanks4x4
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_tanks02
pos = 0, 190, 0
rotate = 90, 30, 0
archetype = space_tanks4x4
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_tanks03
pos = 0, 190, 0
rotate = 90, 90, 0
archetype = space_tanks4x4
parent = ku_hns_02
'''

class HonshuRefineryEdition(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_hns_02'
    TEMPLATE = '''[Object]
nickname = ku_hns_02
pos = 0, 550, 0
rotate = 0, 0, 0
archetype = space_police01
{dock_props}

[Object]
nickname = ku_hns_02_panelA03
pos = -150, 35, -120
rotate = 15, 0, 0
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_panelA06
pos = -150, 35, 120
rotate = -15, 0, 0
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indA08
pos = -250, -85, -105
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indA09
pos = -250, -85, 0
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indA10
pos = -250, -85, 105
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_panelB03
pos = 150, 35, -120
rotate = 15, 0, 0
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_panelB06
pos = 150, 35, 120
rotate = -15, 0, 0
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indB04
pos = -150, 135, 0
rotate = 0, 0, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indB04c
pos = 150, 135, 0
rotate = 0, 0, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indB08
pos = 250, -85, -105
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indB09
pos = 250, -85, 0
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indB10
pos = 250, -85, 105
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indB09X
pos = 250, -273, 0
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_indB09X2
pos = -250, -273, 0
rotate = 0, 90, 0
archetype = space_industrial02d
parent = ku_hns_02

[Object]
nickname = ku_hns_02_towerA01
pos = 0, -85, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = ku_hns_02

[Object]
nickname = ku_hns_02_towerA02
pos = 0, 135, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = ku_hns_02

[Object]
nickname = ku_hns_02_towerA03
pos = 0, 285, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = ku_hns_02

[Object]
nickname = ku_hns_02_gird01
pos = 0, 350, 0
rotate = 90, 0, 0
archetype = space_girder
parent = ku_hns_02

[Object]
nickname = ku_hns_02_girdA01
pos = -80, 105, -125
rotate = -75, 0, -5
archetype = space_girder
parent = ku_hns_02

[Object]
nickname = ku_hns_02_girdA02
pos = -80, 105, 125
rotate = 75, 0, -5
archetype = space_girder
parent = ku_hns_02

[Object]
nickname = ku_hns_02_girdA03
pos = 80, 105, -125
rotate = -75, 0, 5
archetype = space_girder
parent = ku_hns_02

[Object]
nickname = ku_hns_02_girdA04
pos = 80, 105, 125
rotate = 75, 0, 5
archetype = space_girder
parent = ku_hns_02

[Object]
nickname = ku_hns_02_towerB02
pos = 0, -120, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = ku_hns_02

[Object]
nickname = ku_hns_02_towerB04
pos = 0, -273, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = ku_hns_02

[Object]
nickname = ku_hns_02_towerB04
pos = 1, -273, 0
rotate = 0, 90, 0
archetype = space_girder
parent = ku_hns_02

[Object]
nickname = ku_hns_02_airlockA02
pos = 0, -220, 0
rotate = -90, 0, 0
archetype = space_airlock_dummy
parent = ku_hns_02

[Object]
nickname = ku_hns_02_habitatB02
pos = 0, -475, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = ku_hns_02

[Object]
nickname = ku_hns_02_habitatB03
pos = 0, -365, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_hns_02

[Object]
nickname = ku_hns_02_tankX01
pos = 150, -180, 0
rotate = -90, 0, 0
archetype = space_tanks4x4
parent = ku_hns_02

[Object]
nickname = ku_hns_02_tankX02
pos = 250, -180, 0
rotate = -90, 0, 0
archetype = space_tanks4x4
parent = ku_hns_02

[Object]
nickname = ku_hns_02_tankX03
pos = 360, -180, 0
rotate = -90, 0, 0
archetype = space_tanks4x4
parent = ku_hns_02

[Object]
nickname = ku_hns_02_tankX01
pos = -150, -180, 0
rotate = -90, 0, 0
archetype = space_tanks4x4
parent = ku_hns_02

[Object]
nickname = ku_hns_02_tankX02
pos = -250, -180, 0
rotate = -90, 0, 0
archetype = space_tanks4x4
parent = ku_hns_02

[Object]
nickname = ku_hns_02_tankX03
pos = -360, -180, 0
rotate = -90, 0, 0
archetype = space_tanks4x4
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_smlgird01
pos = -275, -60, 0
rotate = 0, 0, 0
archetype = space_girderb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_smlgird03
pos = -130, 110, 10
rotate = 0, 0, 0
archetype = space_girderb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_smlgird04
pos = 325, -60, 0
rotate = 0, 0, 0
archetype = space_girderb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_prod01
pos = -420, -20, -90
rotate = 0, 90, 0
archetype = space_large_production
parent = ku_hns_02

[Object]
nickname = ku_hns_02_prod02
pos = -420, -20, 90
rotate = 0, 90, 0
archetype = space_large_production
parent = ku_hns_02

[Object]
nickname = ku_hns_02_prod01B
pos = 420, -20, -90
rotate = 0, -90, 0
archetype = space_large_production
parent = ku_hns_02

[Object]
nickname = ku_hns_02_prod02B
pos = 420, -20, 90
rotate = 0, -90, 0
archetype = space_large_production
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_tanks01
pos = 0, 189, 0
rotate = 90, -30, 0
archetype = space_tanks4x4
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_tanks02
pos = 0, 190, 0
rotate = 90, 30, 0
archetype = space_tanks4x4
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_tanks03
pos = 0, 191, 0
rotate = 90, 90, 0
archetype = space_tanks4x4
parent = ku_hns_02
'''


class HonshuMilitary(HonshuMilitaryOriginal):
    TEMPLATE = '''[Object]
nickname = ku_hns_02
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = space_police01_honshu
{dock_props}

[Object]
nickname = ku_hns_02_panelA01
pos = 0, -130, 0
rotate = 0, 0, 0
archetype = batch_honshu_military_structure0
parent = ku_hns_02

[Object]
nickname = ku_hns_02_panelA05
pos = -315, 35, 120
rotate = 15, 0, 180
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_panelB05
pos = 315, 35, 120
rotate = 15, 0, 180
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_panelC01
pos = 0, 175, -130
rotate = 15, 0, 0
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_panelC02
pos = 0, 175, 120
rotate = -15, 0, 0
archetype = space_station_panelb
parent = ku_hns_02

[Object]
nickname = ku_hns_02_INNER_shipayrd01
pos = 0, 65, 2.5
rotate = 0, 0, 0
archetype = batch_honshu_military_inner0
parent = ku_hns_02



[Object]
nickname = ku_hns_02_col_structure0_collision00
pos = -315, 46.3682704, 1.45101923
rotate = 0, 0, 0
archetype = batch_honshu_military_structure0_collision00
parent = ku_hns_02

[Object]
nickname = ku_hns_02_col_structure0_collision01
pos = -338.335804, 24.6492043, 0.701009771
rotate = 0, 0, 0
archetype = batch_honshu_military_structure0_collision01
parent = ku_hns_02

[Object]
nickname = ku_hns_02_col_structure0_collision02
pos = 107.369655, 24.6492043, 1.45101923
rotate = 0, 0, 0
archetype = batch_honshu_military_structure0_collision02
parent = ku_hns_02

[Object]
nickname = ku_hns_02_col_structure0_collision03
pos = 341.664196, 24.6492043, -24.7989902
rotate = 0, 0, 0
archetype = batch_honshu_military_structure0_collision03
parent = ku_hns_02

[Object]
nickname = ku_hns_02_col_structure0_collision04
pos = 263.921433, 159.183954, 0.701009771
rotate = 0, 0, 0
archetype = batch_honshu_military_structure0_collision04
parent = ku_hns_02

[Object]
nickname = ku_hns_02_col_structure0_collision05
pos = -0.0679779053, 24.8500118, 0.0143051147
rotate = 0, 0, 0
archetype = batch_honshu_military_structure0_collision05
parent = ku_hns_02

[Object]
nickname = ku_hns_02_col_structure0_collision06
pos = -0.043510437, 283.783196, -0.0491121121
rotate = 0, 0, 0
archetype = batch_honshu_military_structure0_collision06
parent = ku_hns_02

[Object]
nickname = ku_hns_02_col_structure0_collision07
pos = 3.83164831e-07, -196.764076, 0.18249136
rotate = 0, 0, 0
archetype = batch_honshu_military_structure0_collision07
parent = ku_hns_02

[Object]
nickname = ku_hns_02_col_structure0_collision08
pos = -0.043510437, -210, -3.64209995e-10
rotate = 0, 0, 0
archetype = batch_honshu_military_structure0_collision08
parent = ku_hns_02

[Object]
nickname = ku_hns_02_col_structure0_collision09
pos = -0.043510437, -475.633264, 0.00915527344
rotate = 0, 0, 0
archetype = batch_honshu_military_structure0_collision09
parent = ku_hns_02

[Object]
nickname = ku_hns_02_col_structure0_collision10
pos = 0.0692892075, -738.449093, 0.0650351536
rotate = 0, 0, 0
archetype = batch_honshu_military_structure0_collision10
parent = ku_hns_02

[Object]
nickname = ku_hns_02_col_inner0_collision00
pos = -300.302945, 25.0000574, 4.36996864
rotate = 0, 0, 0
archetype = batch_honshu_military_inner0_collision00
parent = ku_hns_02

[Object]
nickname = ku_hns_02_col_inner0_collision01
pos = 68.1827327, 24.9999999, 4.36996864
rotate = 0, 0, 0
archetype = batch_honshu_military_inner0_collision01
parent = ku_hns_02

[Object]
nickname = ku_hns_02_col_inner0_collision02
pos = -3.33216721, 60.23843, 3.69892025
rotate = 0, 0, 0
archetype = batch_honshu_military_inner0_collision02
parent = ku_hns_02

'''
