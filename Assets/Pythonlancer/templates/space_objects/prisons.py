from templates.space_object_template import SpaceObjectTemplate


class AvalonPrison(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'br_avl_03'
    TEMPLATE = '''[Object]
nickname = br_avl_03
ids_name = 203733
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = prison
ids_info = 065648
dock_with = br_avl_03_Base
base = br_avl_03_Base
reputation = br_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = br_sales_head_hat, br_male_guard_body, prop_hat_male_br_elite
difficulty_level = 5 ;12
loadout = prison_br
pilot = pilot_solar_hardest
visit = 16

[Object]
nickname = br_avl_03_girder01
pos = -201, 0, 0
rotate = 0, 90, 0
archetype = space_girder
parent = br_avl_03

[Object]
nickname = br_avl_03_girder02
pos = -400, 0, -210
rotate = 0, 0, 0
archetype = space_girder
parent = br_avl_03

[Object]
nickname = br_avl_03_girder03
pos = -400, 0, 210
rotate = 0, 0, 0
archetype = space_girder
parent = br_avl_03

[Object]
nickname = br_avl_03_girder04
pos = -640, 0, 210
rotate = 0, 0, 0
archetype = space_girder
parent = br_avl_03

[Object]
nickname = br_avl_03_girder05
pos = -640, 0, -190
rotate = 0, 0, 0
archetype = space_girder
parent = br_avl_03

[Object]
nickname = br_avl_03_prison01
pos = -640, 0, 0
rotate = 0, 180, 0
archetype = space_prison
parent = br_avl_03

[Object]
nickname = br_avl_03_prison02
pos = -640, 0, -400
rotate = 0, 180, 0
archetype = space_prison
parent = br_avl_03

[Object]
nickname = br_avl_03_prison03
pos = -640, 0, 400
rotate = 0, 180, 0
archetype = space_prison
parent = br_avl_03

[Object]
nickname = br_avl_03_industrial01
pos = -400, 0, 0
rotate = 0, 90, 0
archetype = space_industrial01b
parent = br_avl_03

[Object]
nickname = br_avl_03_industrial02
pos = -400, 0, -400
rotate = 0, 90, 0
archetype = space_industrial01b
parent = br_avl_03

[Object]
nickname = br_avl_03_industrial03
pos = -400, 0, 400
rotate = 0, 90, 0
archetype = space_industrial01b
parent = br_avl_03

[Object]
nickname = br_avl_03_girder06
pos = -640, 100, 0
rotate = 90, 0, 0
archetype = space_girder
parent = br_avl_03

[Object]
nickname = br_avl_03_girder07
pos = -640, -100, 0
rotate = 90, 0, 0
archetype = space_girder
parent = br_avl_03

[Object]
nickname = br_avl_03_industrial04
pos = -640, 260, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = br_avl_03

[Object]
nickname = br_avl_03_industrial05
pos = -640, -260, 0
rotate = 0, 90, 0
archetype = space_industrial02a
parent = br_avl_03

[Object]
nickname = br_avl_03_industrial06
pos = -785, 260, 0
rotate = 180, 0, 90
archetype = space_industrial02a
loadout = space_ind01_reactor
parent = br_avl_03

[Object]
nickname = br_avl_03_shipyard
pos = -925, 260, 0
rotate = 0, 0, 90
archetype = shipyard
parent = br_avl_03

[Object]
nickname = br_avl_03_dome01
pos = -640, 290, -400
rotate = 0, 0, 0
archetype = space_dome
parent = br_avl_03

[Object]
nickname = br_avl_03_dome02
pos = -640, 290, 400
rotate = 0, 180, 0
archetype = space_dome
parent = br_avl_03

[Object]
nickname = br_avl_03_tanks01
pos = -640, -260, -190
rotate = 0, 0, 0
archetype = space_tankl4
parent = br_avl_03

[Object]
nickname = br_avl_03_tanks02
pos = -640, -260, -455
rotate = 0, 0, 0
archetype = space_tankl4
parent = br_avl_03

[Object]
nickname = br_avl_03_tanks03
pos = -640, -260, 190
rotate = 0, 0, 0
archetype = space_tankl4
parent = br_avl_03

[Object]
nickname = br_avl_03_tanks04
pos = -640, -260, 455
rotate = 0, 0, 0
archetype = space_tankl4
parent = br_avl_03

[Object]
nickname = br_avl_03_tanks05
pos = -640, -260, -190
rotate = 0, 0, 90
archetype = space_tankl4x4
parent = br_avl_03

[Object]
nickname = br_avl_03_tanks06
pos = -640, -260, -455
rotate = 0, 0, 90
archetype = space_tankl4x4
parent = br_avl_03

[Object]
nickname = br_avl_03_tanks07
pos = -640, -260, 190
rotate = 0, 0, 90
archetype = space_tankl4x4
parent = br_avl_03

[Object]
nickname = br_avl_03_tanks08
pos = -640, -260, 455
rotate = 0, 0, 90
archetype = space_tankl4x4
parent = br_avl_03
'''


class HonshuPrison(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_hns_03'
    TEMPLATE = '''[Object]
nickname = ku_hns_03
ids_name = 203767
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_police01_prison
ids_info = 065682
dock_with = ku_hns_03_base
base = ku_hns_03_base
reputation = ku_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = pl_male8_head_hat, ku_male_guard_body, prop_hat_male_ku_grd_visor
difficulty_level = 10
loadout = ku_space_police01
pilot = pilot_solar_hardest
visit = 16

[Object]
nickname = ku_hns_03_prison_root01
pos = -330, 0, 0
rotate = 0, 0, 0
archetype = space_industrial01b
parent = ku_hns_03

[Object]
nickname = ku_hns_03_prison01
pos = -330, 0, -255
rotate = 0, 90, 0
archetype = space_prison
parent = ku_hns_03

[Object]
nickname = ku_hns_03_prison02
pos = -330, 0, 255
rotate = 0, -90, 0
archetype = space_prison
parent = ku_hns_03

[Object]
nickname = ku_hns_03_industrial01
pos = -405, 0, 0
rotate = 0, 90, 0
archetype = space_industrial01b
parent = ku_hns_03

[Object]
nickname = ku_hns_03_industrial02
pos = -255, 0, 0
rotate = 0, 90, 0
archetype = space_industrial01b
parent = ku_hns_03

[Object]
nickname = ku_hns_03_girder01
pos = -410, 0, 0
rotate = 0, 90, 0
archetype = space_girder
parent = ku_hns_03

[Object]
nickname = ku_hns_03_girder02
pos = -250, 0, 0
rotate = 0, 90, 0
archetype = space_girder
parent = ku_hns_03

[Object]
nickname = ku_hns_03_tanks01
pos = -592, 0, -143
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = ku_hns_03

[Object]
nickname = ku_hns_03_tanks02
pos = -592, 0, 143
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = ku_hns_03

[Object]
nickname = ku_hns_03_dome01
pos = -300, -300, 0
rotate = 0, -90, -90
archetype = space_dome
parent = ku_hns_03

[Object]
nickname = ku_hns_03_dome02
pos = -300, 300, 0
rotate = 0, 90, -90
archetype = space_dome
parent = ku_hns_03

[Object]
nickname = ku_hns_03_radar01
pos = -330, 156, -254
rotate = 0, 90, 0
archetype = old_panel_x2
parent = ku_hns_03

[Object]
nickname = ku_hns_03_radar02
pos = -330, -154, -254
rotate = 0, -90, 180
archetype = old_panel_x2
parent = ku_hns_03

[Object]
nickname = ku_hns_03_radar03
pos = -330, -154, 254
rotate = 0, -90, 180
archetype = old_panel_x2
parent = ku_hns_03

[Object]
nickname = ku_hns_03_radar04
pos = -330, 156, 254
rotate = 0, 90, 0
archetype = old_panel_x2
parent = ku_hns_03
'''
