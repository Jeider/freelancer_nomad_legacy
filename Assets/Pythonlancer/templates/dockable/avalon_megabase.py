from templates.space_object_template import SpaceObjectTemplate


class AvalonMegabaseOriginal(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'br_avl_06'
    TEMPLATE = '''[Object]
nickname = br_avl_06
pos = 0, -750, 0
rotate = 0, 90, 0
archetype = bristol_core
{root_props}

[Object]
nickname = br_avl_06_dock
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_police01
{dock_props}

[Object]
nickname = br_avl_06_TOP_habitat01
pos = 0, -245, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_TOP_twr01
pos = 0, -150, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = br_avl_06

[Object]
nickname = br_avl_06_TOP_girder01
pos = 0, -216, 140
rotate = 45, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_TOP_girder02
pos = 0, -215, -137
rotate = -45, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_TOP_girder03
pos = 0, -350, 0
rotate = -90, 0, 0
archetype = space_girdera
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indA01
pos = 0, -400, 200
rotate = 90, 0, 0
archetype = space_industrial01a
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indA02
pos = 0, -400, -200
rotate = 90, 0, 0
archetype = space_industrial01a
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_prison01
pos = 0, -400, 0
rotate = 0, 90, 0
archetype = space_prison
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indB01
pos = -120, -347, 200
rotate = 75, 0, 90
archetype = space_industrial02d
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indB02
pos = -120, -453, 200
rotate = 75, 0, 90
archetype = space_industrial02d
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indB03
pos = -120, -347, -200
rotate = -75, 0, 90
archetype = space_industrial02d
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indB04
pos = -120, -453, -200
rotate = -75, 0, 90
archetype = space_industrial02d
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indB05
pos = 120, -347, 200
rotate = 75, 0, -90
archetype = space_industrial02d
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indB06
pos = 120, -453, 200
rotate = 75, 0, -90
archetype = space_industrial02d
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indB07
pos = 120, -347, -200
rotate = -75, 0, -90
archetype = space_industrial02d
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indB08
pos = 120, -453, -200
rotate = -75, 0, -90
archetype = space_industrial02d
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_tube01
pos = 0, -400, 125
rotate = 92, 0, 0
archetype = space_tube_fix
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_tube02
pos = 0, -400, -125
rotate = 88, 0, 0
archetype = space_tube_fix
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_twr01
pos = -200, -300, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_twr02
pos = -200, -400, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_twr03
pos = -200, -500, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_ind01
pos = -300, -500, 0
rotate = 90, 0, 0
archetype = space_industrialc
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_ind02
pos = -200, -400, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_habitat01
pos = -360, -400, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_habitat02
pos = -330, -400, 75
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_habitat03
pos = -280, -400, 130
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_habitat04
pos = -330, -400, -75
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_habitat05
pos = -280, -400, -130
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_girder01
pos = -360, -400, 0
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_girder02
pos = -330, -400, 75
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_girder03
pos = -280, -400, 130
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_girder04
pos = -330, -400, -75
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_girder05
pos = -280, -400, -130
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_twr01
pos = 200, -300, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_twr02
pos = 200, -400, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_twr03
pos = 200, -500, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_ind01
pos = 300, -500, 0
rotate = 90, 0, 0
archetype = space_industrialc
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_ind02
pos = 200, -400, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_habitat01
pos = 360, -400, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_habitat02
pos = 330, -400, 75
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_habitat03
pos = 280, -400, 130
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_habitat04
pos = 330, -400, -75
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_habitat05
pos = 280, -400, -130
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_girder01
pos = 360, -400, 0
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_girder02
pos = 330, -400, 75
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_girder03
pos = 280, -400, 130
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_girder04
pos = 330, -400, -75
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_girder05
pos = 280, -400, -130
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_shipyard01
pos = 100, -750, 0
rotate = 0, 0, -90
archetype = shipyard
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_shipyard02
pos = 100, -1150, 0
rotate = 0, 0, -90
archetype = shipyard
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_shipyard03
pos = 100, -1550, 0
rotate = 0, 0, -90
archetype = shipyard
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_shipyard04
pos = -100, -750, 0
rotate = 0, 180, 90
archetype = shipyard
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_shipyard05
pos = -100, -1150, 0
rotate = 0, 180, 90
archetype = shipyard
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_shipyard06
pos = -100, -1550, 0
rotate = 0, 180, 90
archetype = shipyard
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_ind01
pos = 0, -950, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_ind02
pos = 0, -1350, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_ind03
pos = 150, -950, 0
rotate = 0, 90, 0
archetype = space_industrial02d
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_ind04
pos = -150, -950, 0
rotate = 0, 90, 0
archetype = space_industrial02d
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_ind05
pos = 125, -1350, 0
rotate = 0, 90, 0
archetype = space_industrial02d
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_ind06
pos = -125, -1350, 0
rotate = 0, 90, 0
archetype = space_industrial02d
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_tube01
pos = 300, -575, 0
rotate = 90, 0, -5
archetype = space_short_tube
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_tube02
pos = -300, -575, 0
rotate = 90, 0, 5
archetype = space_short_tube
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_twr01
pos = 0, -1942, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_twr02
pos = 0, -1760, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_habitat01
pos = 0, -2002, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_habitat02
pos = 0, -1850, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_habitat03
pos = 0, -1550, 0
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_habitat04
pos = 0, -1150, 0
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_habitat05
pos = 0, -750, 0
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_habitat06
pos = 0, -1700, 0
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_habitat07
pos = 0, -1400, 0
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_habitat08
pos = 0, -1300, 0
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_habitat09
pos = 0, -1000, 0
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_habitat10
pos = 0, -900, 0
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_habitat11
pos = 0, -650, 0
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_habitat12
pos = 0, -540, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_girder01
pos = 0, -750, 0
rotate = 0, 0, 0
archetype = space_girderc
parent = br_avl_06
'''


class AvalonMegabaseShortOriginal(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'br_avl_06'
    TEMPLATE = '''[Object]
nickname = br_avl_06
pos = 0, 160, 0
rotate = 0, 90, 0
archetype = space_police01
{dock_props}

[Object]
nickname = br_avl_06_TOP_twr01
pos = 0, -150, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = br_avl_06

[Object]
nickname = br_avl_06_TOP_girder01
pos = 0, -216, 140
rotate = 45, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_TOP_girder02
pos = 0, -215, -137
rotate = -45, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_TOP_girder03
pos = 0, 26, 0
rotate = -90, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_TOP_girder03
pos = 0, -210, 0
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indA01
pos = 0, -400, 200
rotate = 90, 0, 0
archetype = space_industrial01a
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indA02
pos = 0, -400, -200
rotate = 90, 0, 0
archetype = space_industrial01a
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_prison01
pos = 0, -400, 0
rotate = 0, 90, 0
archetype = space_prison
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indB01
pos = -120, -347, 200
rotate = 75, 0, 90
archetype = space_industrial02d
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indB02
pos = -120, -453, 200
rotate = 75, 0, 90
archetype = space_industrial02d
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indB03
pos = -120, -347, -200
rotate = -75, 0, 90
archetype = space_industrial02d
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indB04
pos = -120, -453, -200
rotate = -75, 0, 90
archetype = space_industrial02d
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indB05
pos = 120, -347, 200
rotate = 75, 0, -90
archetype = space_industrial02d
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indB06
pos = 120, -453, 200
rotate = 75, 0, -90
archetype = space_industrial02d
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indB07
pos = 120, -347, -200
rotate = -75, 0, -90
archetype = space_industrial02d
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indB08
pos = 120, -453, -200
rotate = -75, 0, -90
archetype = space_industrial02d
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_twr01
pos = -200, -300, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_twr02
pos = -200, -400, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_twr03
pos = -200, -500, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_ind02
pos = -200, -400, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_habitat01
pos = -360, -400, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_habitat02
pos = -330, -400, 75
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_habitat03
pos = -280, -400, 130
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_habitat04
pos = -330, -400, -75
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_habitat05
pos = -280, -400, -130
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_girder01
pos = -360, -400, 0
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_girder02
pos = -330, -400, 75
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_girder03
pos = -280, -400, 130
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_girder04
pos = -330, -400, -75
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_girder05
pos = -280, -400, -130
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_twr01
pos = 200, -300, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_twr02
pos = 200, -400, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_twr03
pos = 200, -500, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_ind02
pos = 200, -400, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_habitat01
pos = 360, -400, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_habitat02
pos = 330, -400, 75
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_habitat03
pos = 280, -400, 130
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_habitat04
pos = 330, -400, -75
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_habitat05
pos = 280, -400, -130
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_girder01
pos = 360, -400, 0
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_girder02
pos = 330, -400, 75
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_girder03
pos = 280, -400, 130
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_girder04
pos = 330, -400, -75
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_girder05
pos = 280, -400, -130
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_shipyard01
pos = 0, -600, 0
rotate = 0, 0, -180
archetype = shipyard
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_shipyard02
pos = 280, -600, 0
rotate = 0, 0, -180
archetype = shipyard
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_shipyard03
pos = -280, -600, 0
rotate = 0, 0, -180
archetype = shipyard
parent = br_avl_06
'''


class AvalonMegabase(AvalonMegabaseOriginal):
    TEMPLATE = '''[Object]
nickname = br_avl_06
pos = 0, -750, 0
rotate = 0, 90, 0
archetype = bristol_core
{root_props}

[Object]
nickname = br_avl_06_dock
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_police01
{dock_props}

[Object]
nickname = br_avl_06_TOP_habitat01
pos = 0, -250, 1.5
rotate = 0, 0, 0
archetype = batch_avalon_megabase_top0
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indA01
pos = 0, -400, 0
rotate = 0, 0, 0
archetype = batch_avalon_megabase_core0
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_prison01
pos = 0, -400, 0
rotate = 0, 90, 0
archetype = space_prison
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_twr01
pos = -280, -400, 0
rotate = 0, 0, 0
archetype = batch_avalon_megabase_left0
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_twr01
pos = 280, -400, 0
rotate = 0, 0, 0
archetype = batch_avalon_megabase_right0
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_shipyard01
pos = 0, -1271, 0
rotate = 0, 0, 0
archetype = batch_avalon_megabase_bottom0
parent = br_avl_06



[Object]
nickname = br_avl_06_batch_avalon_megabase_top0_collision00
pos = -0.271690369, -174.485816, 1.47555247
rotate = 0, 0, 0
archetype = batch_avalon_megabase_top0_collision00
parent = br_avl_06

[Object]
nickname = br_avl_06_batch_avalon_megabase_core0_collision00
pos = -86.1471357, -399.826004, -0.182335252
rotate = 0, 0, 0
archetype = batch_avalon_megabase_core0_collision00
parent = br_avl_06

[Object]
nickname = br_avl_06_batch_avalon_megabase_core0_collision01
pos = 111.734581, -1123.21008, 0.416172575
rotate = 0, 0, 0
archetype = batch_avalon_megabase_core0_collision01
parent = br_avl_06

[Object]
nickname = br_avl_06_batch_avalon_megabase_left0_collision00
pos = -200.067978, -350.149987, 0.0143051147
rotate = 0, 0, 0
archetype = batch_avalon_megabase_left0_collision00
parent = br_avl_06

[Object]
nickname = br_avl_06_batch_avalon_megabase_left0_collision01
pos = -200.067978, -451.764076, 0.0143051147
rotate = 0, 0, 0
archetype = batch_avalon_megabase_left0_collision01
parent = br_avl_06

[Object]
nickname = br_avl_06_batch_avalon_megabase_right0_collision00
pos = 199.932022, -350.149987, 0.0143051147
rotate = 0, 0, 0
archetype = batch_avalon_megabase_right0_collision00
parent = br_avl_06

[Object]
nickname = br_avl_06_batch_avalon_megabase_right0_collision01
pos = 199.932022, -451.764076, 0.0143051147
rotate = 0, 0, 0
archetype = batch_avalon_megabase_right0_collision01
parent = br_avl_06

[Object]
nickname = br_avl_06_batch_avalon_megabase_bottom0_collision00
pos = 1.664196, -1150.2005, -4.63355863e-06
rotate = 0, 0, 0
archetype = batch_avalon_megabase_bottom0_collision00
parent = br_avl_06

[Object]
nickname = br_avl_06_batch_avalon_megabase_bottom0_collision01
pos = -0.19414702, -1267.46208, 1.30706024
rotate = 0, 0, 0
archetype = batch_avalon_megabase_bottom0_collision01
parent = br_avl_06

[Object]
nickname = br_avl_06_batch_avalon_megabase_bottom0_collision02
pos = 0.0692892075, -1306.94909, 0.0343093872
rotate = 0, 0, 0
archetype = batch_avalon_megabase_bottom0_collision02
parent = br_avl_06

'''


class AvalonMegabaseShort(AvalonMegabaseShortOriginal):
    TEMPLATE = '''[Object]
nickname = br_avl_06
pos = 0, 160, 0
rotate = 0, 90, 0
archetype = space_police01
{dock_props}

[Object]
nickname = br_avl_06_TOP_twr01
pos = 0, -95, 1.5
rotate = 0, 0, 0
archetype = batch_avalon_me_e87709e4_top0
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_indA01
pos = 0, -400, 0
rotate = 0, 0, 0
archetype = batch_avalon_me_e87709e4_core0
parent = br_avl_06

[Object]
nickname = br_avl_06_CORE_prison01
pos = 0, -400, 0
rotate = 0, 90, 0
archetype = space_prison
parent = br_avl_06

[Object]
nickname = br_avl_06_LEFT_twr01
pos = -280, -400, 0
rotate = 0, 0, 0
archetype = batch_avalon_me_e87709e4_left0
parent = br_avl_06

[Object]
nickname = br_avl_06_RIGHT_twr01
pos = 280, -400, 0
rotate = 0, 0, 0
archetype = batch_avalon_me_e87709e4_right0
parent = br_avl_06

[Object]
nickname = br_avl_06_BOTTOM_shipyard01
pos = 0, -600, 0
rotate = 0, 0, 0
archetype = batch_avalon_me_e87709e4_bottom0
parent = br_avl_06



[Object]
nickname = br_avl_06_col_top0_collision00
pos = -0.271690369, -115.372707, 1.47555247
rotate = 0, 0, 0
archetype = batch_avalon_me_e87709e4_top0_collision00
parent = br_avl_06

[Object]
nickname = br_avl_06_col_core0_collision00
pos = -86.1471357, -399.826004, -0.182335252
rotate = 0, 0, 0
archetype = batch_avalon_me_e87709e4_core0_collision00
parent = br_avl_06

[Object]
nickname = br_avl_06_col_core0_collision01
pos = 119.999979, -399.29899, 0.416172575
rotate = 0, 0, 0
archetype = batch_avalon_me_e87709e4_core0_collision01
parent = br_avl_06

[Object]
nickname = br_avl_06_col_left0_collision00
pos = -200.067978, -350.149987, 0.0143051147
rotate = 0, 0, 0
archetype = batch_avalon_me_e87709e4_left0_collision00
parent = br_avl_06

[Object]
nickname = br_avl_06_col_left0_collision01
pos = -200.067978, -402.058633, 0.0143051147
rotate = 0, 0, 0
archetype = batch_avalon_me_e87709e4_left0_collision01
parent = br_avl_06

[Object]
nickname = br_avl_06_col_right0_collision00
pos = 199.932022, -350.149987, 0.0143051147
rotate = 0, 0, 0
archetype = batch_avalon_me_e87709e4_right0_collision00
parent = br_avl_06

[Object]
nickname = br_avl_06_col_right0_collision01
pos = 199.932022, -402.058633, 0.0143051147
rotate = 0, 0, 0
archetype = batch_avalon_me_e87709e4_right0_collision01
parent = br_avl_06

[Object]
nickname = br_avl_06_col_bottom0_collision00
pos = -0.200520522, -631.213691, 0.772064209
rotate = 0, 0, 0
archetype = batch_avalon_me_e87709e4_bottom0_collision00
parent = br_avl_06

'''
