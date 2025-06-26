from templates.space_object_template import SpaceObjectTemplate


class Cloakgen(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'br_avl_05'
    TEMPLATE = '''[Object]
nickname = br_avl_05
pos = 0, 0, 0
rotate = 90, 90, 0
archetype = xlarge_ring_station
loadout = cloakgen_fx
{root_props}

[Object]
nickname = br_avl_05_arch01
pos = 0, 1480, 0
rotate = 180, 90, 0
archetype = space_arch_closed
parent = br_avl_05

[Object]
nickname = br_avl_05_arch02
pos = 0, -1480, 0
rotate = 0, 90, 0
archetype = space_arch_closed
parent = br_avl_05

[Object]
nickname = br_avl_05_flamer01
pos = 0, 0, -190
rotate = 90, 0, 0
archetype = space_cloakgen_flamer
loadout = cloakgen_flamer_fx
parent = br_avl_05

[Object]
nickname = br_avl_05_flamer02
pos = 0, 0, 190
rotate = -90, 0, 0
archetype = space_cloakgen_flamer
loadout = cloakgen_flamer_fx
parent = br_avl_05

[Object]
nickname = br_avl_05_lasers
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = hidden_connect
loadout = cloakgen_lasers
parent = br_avl_05

[;Object]
nickname = br_avl_05_laser01
pos = 0, 225, 0
rotate = 180, 0, 0
archetype = space_cloakgen_laser
parent = br_avl_05

[;Object]
nickname = br_avl_05_laser02
pos = 190, -115, 0
rotate = 0, 0, 60
archetype = space_cloakgen_laser
parent = br_avl_05

[;Object]
nickname = br_avl_05_laser03
pos = -190, -115, 0
rotate = -60, -90, 0
archetype = space_cloakgen_laser
parent = br_avl_05

[Object]
nickname = br_avl_05_ind01
pos = 0, 200, -375
rotate = 0, 90, 0
archetype = space_industrial01a
parent = br_avl_05

[Object]
nickname = br_avl_05_ind02
pos = 0, -200, -375
rotate = 0, 90, 0
archetype = space_industrial01a
parent = br_avl_05

[Object]
nickname = br_avl_05_ind03
pos = 0, 200, 375
rotate = 0, 90, 0
archetype = space_industrial01a
parent = br_avl_05

[Object]
nickname = br_avl_05_ind04
pos = 0, -200, 375
rotate = 0, 90, 0
archetype = space_industrial01a
parent = br_avl_05

[Object]
nickname = br_avl_05_ind05
pos = 0, 0, 375
rotate = 90, 0, 0
archetype = space_industrial02a
parent = br_avl_05

[Object]
nickname = br_avl_05_ind06
pos = 0, 0, -375
rotate = 90, 0, 0
archetype = space_industrial02a
parent = br_avl_05

[Object]
nickname = br_avl_05_ind07
pos = 0, 0, -335
rotate = 0, 0, 45
archetype = space_industrialc
parent = br_avl_05

[Object]
nickname = br_avl_05_ind07
pos = 0, 0, 335
rotate = 0, 180, 45
archetype = space_industrialc
parent = br_avl_05

[Object]
nickname = br_avl_05_tower01
pos = 0, 105, 375
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = br_avl_05

[Object]
nickname = br_avl_05_tower02
pos = 0, -105, 375
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = br_avl_05

[Object]
nickname = br_avl_05_tower03
pos = 0, 105, -375
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = br_avl_05

[Object]
nickname = br_avl_05_tower04
pos = 0, -105, -375
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = br_avl_05

[Object]
nickname = br_avl_05_habitat01
pos = 100, 0, 375
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_05

[Object]
nickname = br_avl_05_habitat02
pos = -100, 0, 375
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_05

[Object]
nickname = br_avl_05_habitat03
pos = 0, 0, 475
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_05

[Object]
nickname = br_avl_05_habitat04
pos = 100, 0, -375
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_05

[Object]
nickname = br_avl_05_habitat05
pos = -100, 0, -375
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_05

[Object]
nickname = br_avl_05_habitat06
pos = 0, 0, -475
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_avl_05

[Object]
nickname = br_avl_05_girder01
pos = 100, 0, 375
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_05

[Object]
nickname = br_avl_05_girder02
pos = -100, 0, 375
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_05

[Object]
nickname = br_avl_05_girder03
pos = 0, 0, 475
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_05

[Object]
nickname = br_avl_05_girder04
pos = 100, 0, -375
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_05

[Object]
nickname = br_avl_05_girder05
pos = -100, 0, -375
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_05

[Object]
nickname = br_avl_05_girder06
pos = 0, 0, -475
rotate = 90, 0, 0
archetype = space_girderc
parent = br_avl_05
'''