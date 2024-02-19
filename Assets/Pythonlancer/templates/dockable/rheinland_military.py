from templates.space_object_template import SpaceObjectTemplate


# NEED TO REMOVE SECOND DOCK?
class RheinlandMilitary(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_biz_05'
    TEMPLATE = '''[Object]
nickname = rh_biz_05
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = keln_core
{root_props}

[Object]
nickname = rh_biz_05_dock01
pos = 0, 0, -620
rotate = 0, 180, 0
archetype = space_police01_front_dock
{dock_props}

[Object]
nickname = rh_biz_05_dock02
pos = 0, 0, 620
rotate = 0, 0, 0
archetype = space_police01_front_dock
{dock_props}

[Object]
nickname = rh_biz_05_indA01
pos = 0, 0, 500
rotate = 180, 0, 45
archetype = space_industriala
parent = rh_biz_05

[Object]
nickname = rh_biz_05_indA02
pos = 0, 0, -500
rotate = 0, 0, 45
archetype = space_industriala
parent = rh_biz_05

[Object]
nickname = rh_biz_05_indA03
pos = 0, 0, 0
rotate = 0, 0, 45
archetype = space_industriala
parent = rh_biz_05

[Object]
nickname = rh_biz_05_indA05
pos = 0, 0, -250
rotate = 0, 0, 45
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = rh_biz_05

[Object]
nickname = rh_biz_05_indA06
pos = 0, 0, 250
rotate = 0, 0, 45
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = rh_biz_05

[Object]
nickname = rh_biz_05_indB01
pos = 315, 245, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_biz_05

[Object]
nickname = rh_biz_05_indB02
pos = 315, 245, -500
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_biz_05

[Object]
nickname = rh_biz_05_indB03
pos = 315, 245, 500
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_biz_05

[Object]
nickname = rh_biz_05_indB04
pos = 315, -245, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_biz_05

[Object]
nickname = rh_biz_05_indB05
pos = 315, -245, -500
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_biz_05

[Object]
nickname = rh_biz_05_indB06
pos = 315, -245, 500
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_biz_05

[Object]
nickname = rh_biz_05_indB07
pos = -315, 245, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_biz_05

[Object]
nickname = rh_biz_05_indB08
pos = -315, 245, -500
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_biz_05

[Object]
nickname = rh_biz_05_indB09
pos = -315, 245, 500
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_biz_05

[Object]
nickname = rh_biz_05_indB10
pos = -315, -245, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_biz_05

[Object]
nickname = rh_biz_05_indB11
pos = -315, -245, -500
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_biz_05

[Object]
nickname = rh_biz_05_indB12
pos = -315, -245, 500
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_biz_05

[Object]
nickname = rh_biz_05_girderA01
pos = 0, 0, 0
rotate = 0, 90, 45
archetype = space_girdera
parent = rh_biz_05

[Object]
nickname = rh_biz_05_girderA02
pos = 0, 0, 0
rotate = 0, 90, -45
archetype = space_girdera
parent = rh_biz_05

[Object]
nickname = rh_biz_05_girderA03
pos = 0, 0, 0
rotate = 0, 90, 135
archetype = space_girdera
parent = rh_biz_05

[Object]
nickname = rh_biz_05_girderA04
pos = 0, 0, 0
rotate = 0, 90, -135
archetype = space_girdera
parent = rh_biz_05

[Object]
nickname = rh_biz_05_girderA05
pos = 0, 0, -500
rotate = 0, 90, -45
archetype = space_girdera
parent = rh_biz_05

[Object]
nickname = rh_biz_05_girderA06
pos = 0, 0, -500
rotate = 0, 90, 45
archetype = space_girdera
parent = rh_biz_05

[Object]
nickname = rh_biz_05_girderA07
pos = 0, 0, -500
rotate = 0, 90, 135
archetype = space_girdera
parent = rh_biz_05

[Object]
nickname = rh_biz_05_girderA08
pos = 0, 0, -500
rotate = 0, 90, -135
archetype = space_girdera
parent = rh_biz_05

[Object]
nickname = rh_biz_05_girderA09
pos = 0, 0, 500
rotate = 0, 90, 45
archetype = space_girdera
parent = rh_biz_05

[Object]
nickname = rh_biz_05_girderA10
pos = 0, 0, 500
rotate = 0, 90, -45
archetype = space_girdera
parent = rh_biz_05

[Object]
nickname = rh_biz_05_girderA11
pos = 0, 0, 500
rotate = 0, 90, 135
archetype = space_girdera
parent = rh_biz_05

[Object]
nickname = rh_biz_05_girderA12
pos = 0, 0, 500
rotate = 0, 90, -135
archetype = space_girdera
parent = rh_biz_05

[Object]
nickname = rh_biz_05_shipyard01
pos = 320, -50, 0
rotate = 0, 0, 0
archetype = shipyard_2x
parent = rh_biz_05

[Object]
nickname = rh_biz_05_shipyard02
pos = -320, 80, -385
rotate = 0, 0, 0
archetype = shipyard
parent = rh_biz_05

[Object]
nickname = rh_biz_05_shipyard03
pos = -320, 80, 385
rotate = 0, 180, 0
archetype = shipyard
parent = rh_biz_05

[Object]
nickname = rh_biz_05_shipyard04
pos = -320, -80, -385
rotate = 0, 0, 180
archetype = shipyard
parent = rh_biz_05

[Object]
nickname = rh_biz_05_shipyard05
pos = -320, -80, 385
rotate = 0, 0, 180
archetype = shipyard
parent = rh_biz_05

[Object]
nickname = rh_biz_05_tube01
pos = 0, 0, 0
rotate = 90, 0, 0
archetype = space_short_Tube
parent = rh_biz_05

[Object]
nickname = rh_biz_05_tube02
pos = 0, 0, -500
rotate = 50, 0, 0
archetype = space_short_Tube
parent = rh_biz_05

[Object]
nickname = rh_biz_05_tube03
pos = 0, 0, 0
rotate = -90, 0, 0
archetype = space_short_Tube
parent = rh_biz_05

[Object]
nickname = rh_biz_05_tube04
pos = 0, 0, -500
rotate = -50, 0, 0
archetype = space_short_Tube
parent = rh_biz_05

[Object]
nickname = rh_biz_05_tube05
pos = 0, 0, 500
rotate = 50, 180, 0
archetype = space_short_Tube
parent = rh_biz_05

[Object]
nickname = rh_biz_05_tube06
pos = 0, 0, 500
rotate = -50, 180, 0
archetype = space_short_Tube
parent = rh_biz_05

[Object]
nickname = rh_biz_05_ctrl_twr01
pos = 0, 595, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = rh_biz_05

[Object]
nickname = rh_biz_05_ctrl_twr02
pos = 0, 680, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = rh_biz_05

[Object]
nickname = rh_biz_05_ctrl_twr03
pos = 0, 763, 0
rotate = 180, 0, 0
archetype = space_control_tower
parent = rh_biz_05

[Object]
nickname = rh_biz_05_habitat01
pos = -150, 680, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_biz_05

[Object]
nickname = rh_biz_05_habitat02
pos = 150, 680, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_biz_05

[Object]
nickname = rh_biz_05_habitat03
pos = 0, 680, -150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_biz_05

[Object]
nickname = rh_biz_05_habitat04
pos = 0, 680, 150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_biz_05

[Object]
nickname = rh_biz_05_habitat05
pos = -100, 680, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_biz_05

[Object]
nickname = rh_biz_05_habitat06
pos = -100, 680, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_biz_05

[Object]
nickname = rh_biz_05_habitat07
pos = 100, 680, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_biz_05

[Object]
nickname = rh_biz_05_habitat08
pos = 100, 680, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_biz_05

[Object]
nickname = rh_biz_05_ctrl_twr04
pos = 0, -595, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = rh_biz_05

[Object]
nickname = rh_biz_05_ctrl_twr05
pos = 0, -680, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = rh_biz_05

[Object]
nickname = rh_biz_05_ctrl_twr06
pos = 0, -743, 0
rotate = 180, 0, 0
archetype = space_control_tower
parent = rh_biz_05

[Object]
nickname = rh_biz_05_habitatA01
pos = -150, -680, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_biz_05

[Object]
nickname = rh_biz_05_habitatA02
pos = 150, 680, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_biz_05

[Object]
nickname = rh_biz_05_habitatA03
pos = 0, 680, -150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_biz_05

[Object]
nickname = rh_biz_05_habitatA04
pos = 0, 680, 150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_biz_05

[Object]
nickname = rh_biz_05_habitatA05
pos = -100, 680, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_biz_05

[Object]
nickname = rh_biz_05_habitatA06
pos = -100, 680, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_biz_05

[Object]
nickname = rh_biz_05_habitatA07
pos = 100, 680, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_biz_05

[Object]
nickname = rh_biz_05_habitatA08
pos = 100, 680, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_biz_05

[Object]
nickname = rh_biz_05_girderB01
pos = 0, 600, -150
rotate = 110, 0, 0
archetype = space_girdera
parent = rh_biz_05

[Object]
nickname = rh_biz_05_girderB02
pos = 0, 600, 150
rotate = 110, 180, 0
archetype = space_girdera
parent = rh_biz_05

[Object]
nickname = rh_biz_05_girderB03
pos = 0, -600, -150
rotate = -110, 0, 0
archetype = space_girdera
parent = rh_biz_05

[Object]
nickname = rh_biz_05_girderB04
pos = 0, -600, 150
rotate = -110, 180, 0
archetype = space_girdera
parent = rh_biz_05

[Object]
nickname = rh_biz_05_bs01
pos = 320, 0, 0
rotate = 0, 0, 0
archetype = r_battleship
parent = rh_biz_05

[Object]
nickname = rh_biz_05_ctrl_block02
pos = 0, -99, 620
rotate = 180, 0, 0
archetype = space_small_control_block
parent = rh_biz_05

[Object]
nickname = rh_biz_05_ctrl_block03
pos = 0, -99, -620
rotate = 180, 0, 0
archetype = space_small_control_block
parent = rh_biz_05
'''
