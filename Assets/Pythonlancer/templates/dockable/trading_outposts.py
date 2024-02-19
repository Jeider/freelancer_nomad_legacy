from templates.space_object_template import SpaceObjectTemplate


class LibertyTradingOutpost(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'sig17_01'
    TEMPLATE = '''[Object]
nickname = sig17_01
pos = 0, 0, 0
rotate = 0, -90, 0
archetype = outpost_front_dock
{dock_props}

[Object]
nickname = sig17_01_door01
pos = -125, -7, -115
rotate = 0, 90, 0
archetype = space_industrial01c
parent = sig17_01

[Object]
nickname = sig17_01_door02
pos = -125, -7, -57
rotate = 0, 90, 0
archetype = space_industrial01c
parent = sig17_01

[Object]
nickname = sig17_01_door03
pos = -125, -7, 57
rotate = 0, 90, 0
archetype = space_industrial01c
parent = sig17_01

[Object]
nickname = sig17_01_door04
pos = -125, -7, 115
rotate = 0, 90, 0
archetype = space_industrial01b
parent = sig17_01

[Object]
nickname = sig17_01_door05
pos = -45, -7, -270
rotate = 0, 0, 0
archetype = space_industrial01b
parent = sig17_01

[Object]
nickname = sig17_01_door06
pos = 45, -7, -240
rotate = 0, 0, 0
archetype = space_industrial01c
parent = sig17_01

[Object]
nickname = sig17_01_door07
pos = -45, -7, 270
rotate = 0, 0, 0
archetype = space_industrial01b
parent = sig17_01

[Object]
nickname = sig17_01_door08
pos = 45, -7, 240
rotate = 0, 180, 0
archetype = space_industrial01c
parent = sig17_01

[Object]
nickname = sig17_01_tanks01
pos = -153, -7, -65
rotate = 0, 0, 0
archetype = space_tanks4x4
parent = sig17_01

[Object]
nickname = sig17_01_tanks02
pos = -187.5, -7, -193.5
rotate = 0, 30, 0
archetype = space_tanks4x4
parent = sig17_01

[Object]
nickname = sig17_01_tanks03
pos = -153, -7, 65
rotate = 0, 0, 0
archetype = space_tanks4x4
parent = sig17_01

[Object]
nickname = sig17_01_tanks04
pos = -187.5, -7, 193.5
rotate = 0, -30, 0
archetype = space_tanks4x4
parent = sig17_01

[Object]
nickname = sig17_01_tanks05
pos = -293, -7, -65
rotate = 0, 0, 0
archetype = space_tanks4x4
parent = sig17_01

[Object]
nickname = sig17_01_tanks06
pos = -327.5, -7, -193.5
rotate = 0, 30, 0
archetype = space_tanks4x4
parent = sig17_01

[Object]
nickname = sig17_01_tanks07
pos = -293, -7, 65
rotate = 0, 0, 0
archetype = space_tanks4x4
parent = sig17_01

[Object]
nickname = sig17_01_tanks08
pos = -327.5, -7, 193.5
rotate = 0, -30, 0
archetype = space_tanks4x4
parent = sig17_01

[Object]
nickname = sig17_01_girder01
pos = -285, -7, -250
rotate = 0, 90, 0
archetype = space_girderb
parent = sig17_01

[Object]
nickname = sig17_01_girder02
pos = -285, -7, 250
rotate = 0, 90, 0
archetype = space_girderb
parent = sig17_01

[Object]
nickname = sig17_01_girder03
pos = -220, -7, -130
rotate = 0, 90, 0
archetype = space_girderb
parent = sig17_01

[Object]
nickname = sig17_01_girder04
pos = -220, -7, 130
rotate = 0, 90, 0
archetype = space_girderb
parent = sig17_01

[Object]
nickname = sig17_01_girder05
pos = -220, -7, 0
rotate = 0, 90, 0
archetype = space_girderb
parent = sig17_01

[Object]
nickname = sig17_01_habitat01
pos = -45, 75, -270
rotate = 0, 90, 0
archetype = space_habitat_tallb
parent = sig17_01

[Object]
nickname = sig17_01_habitat02
pos = -45, -7, -375
rotate = 90, 180, 0
archetype = space_habitat_tallb
parent = sig17_01

[Object]
nickname = sig17_01_habitat03
pos = -45, -89, -270
rotate = 180, 90, 0
archetype = space_habitat_tallb
parent = sig17_01

[Object]
nickname = sig17_01_habitat04
pos = -45, 75, 270
rotate = 0, 90, 0
archetype = space_habitat_tallb
parent = sig17_01

[Object]
nickname = sig17_01_habitat05
pos = -45, -7, 375
rotate = 90, 0, 0
archetype = space_habitat_tallb
parent = sig17_01

[Object]
nickname = sig17_01_habitat06
pos = -45, -89, 270
rotate = 180, 90, 0
archetype = space_habitat_tallb
parent = sig17_01

[Object]
nickname = sig17_01_dome01
pos = 45, -7, -308
rotate = 0, 0, -90
archetype = space_domeb
parent = sig17_01

[Object]
nickname = sig17_01_dome02
pos = 45, -7, 308
rotate = 0, 0, -90
archetype = space_domeb
parent = sig17_01
'''



class RheinlandTradingOutpost(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_biz_02'
    TEMPLATE = '''[Object]
nickname = rh_biz_02
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = outpost
{dock_props}

[Object]
nickname = rh_biz_02_ADD_industrial01
pos = 45, -7, -240
rotate = 0, 0, 0
archetype = space_industrial01b
parent = rh_biz_02

[Object]
nickname = rh_biz_02_ADD_industrial02
pos = -45, -7, -240
rotate = 0, 0, 0
archetype = space_industrial01b
parent = rh_biz_02

[Object]
nickname = rh_biz_02_ADD_industrial03
pos = 45, -7, 243
rotate = 0, 0, 0
archetype = space_industrial01b
parent = rh_biz_02

[Object]
nickname = rh_biz_02_ADD_habitat01
pos = 45, 34, 243
rotate = 0, 0, 0
archetype = space_habitat_tallb
parent = rh_biz_02

[Object]
nickname = rh_biz_02_ADD_habitat02
pos = -45, 58, -240
rotate = 0, 0, 0
archetype = space_habitat_tallb
parent = rh_biz_02

[Object]
nickname = rh_biz_02_ADD_dome01
pos = 45, -7, -340
rotate = 0, 0, 90
archetype = space_domeb
parent = rh_biz_02

[Object]
nickname = rh_biz_02_ADD_dome02
pos = 45, -7, 343
rotate = 0, 0, 90
archetype = space_domeb
parent = rh_biz_02
'''
