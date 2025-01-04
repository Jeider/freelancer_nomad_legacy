from templates.space_object_template import SpaceObjectTemplate


class RockfordGenerator(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_col_05'
    TEMPLATE = '''[Object]
nickname = li_col_05
pos = 0, -240, 0
rotate = 180, -90, 0
archetype = space_small_control_block

[Object]
nickname = li_col_05_industrial_B01
pos = 0, 0, -75
rotate = 0, 90, 0
archetype = space_industrial02a
parent = li_col_05

[Object]
nickname = li_col_05_industrial_B02
pos = 0, 0, 75
rotate = 0, 90, 0
archetype = space_industrial02a
parent = li_col_05

[Object]
nickname = li_col_05_industrial_B03
pos = 180, 0, 0
rotate = 0, 0, 0
archetype = space_industrial01a
parent = li_col_05

[Object]
nickname = li_col_05_industrial_B04
pos = -180, 0, 0
rotate = , 0, 0
archetype = space_industrial01a
parent = li_col_05

[Object]
nickname = li_col_05_industrial_B05
pos = 0, 0, 465
rotate = 0, 90, 0
archetype = space_industrial02a
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A01
pos = 0, 70, 0
rotate = -90, 0, 0
archetype = space_industrialc
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A02
pos = 0, -70, 0
rotate = 90, 0, 0
archetype = space_industrialc
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A01
pos = 55.5, -32, 205
rotate = -2, 0, -45
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A02
pos = 55.5, 26, 205
rotate = 0, 0, -135
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A03
pos = -59.5, -32, 205
rotate = 0, 2, 45
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A04
pos = -59.5, 26, 205
rotate = 0, 0, 135
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A05
pos = 55.5, -32, 345
rotate = 0, 0, -45
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A06
pos = 55.5, 30, 345
rotate = 0, 0, -135
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A07
pos = -59.5, -33, 345
rotate = 0, 0, 45
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A08
pos = -59.5, 26, 345
rotate = 1, 0, 135
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A09
pos = 0, -42, 205
rotate = 0, 0, 0
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A10
pos = 0, 41, 205
rotate = 0, 0, 180
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A11
pos = 0, -43, 345
rotate = 0, 0, 0
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A12
pos = 0, 41, 345
rotate = 0, 0, 180
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_habitat01
pos = 0, 65, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = li_col_05

[Object]
nickname = li_col_05_habitat02
pos = 0, -65, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = li_col_05

[Object]
nickname = li_col_05_control01
pos = 0, 0, -170
rotate = 90, 0, 45
archetype = space_medium_control_tower
parent = li_col_05

[Object]
nickname = li_col_05_control01
pos = 0, 0, -170
rotate = -90, 0, 0
archetype = space_cloakgen_laser
parent = li_col_05

[Object]
nickname = li_col_05_tube01
pos = 95, 0, 50
rotate = 180, 0, 0
archetype = space_short_tube
parent = li_col_05

[Object]
nickname = li_col_05_tube02
pos = -95, 0, 50
rotate = 180, 0, 0
archetype = space_short_tube
parent = li_col_05

[Object]
nickname = li_col_05_ring01
pos = 0, 0, -300
rotate = 0, 0, 0
archetype = small_ring
parent = li_col_05

[Object]
nickname = li_col_05_ring01
pos = 0, 0, -400
rotate = 0, 0, 0
archetype = small_ring
parent = li_col_05

[Object]
nickname = li_col_05_ring01
pos = 0, 0, -500
rotate = 0, 0, 0
archetype = small_ring
parent = li_col_05

[Object]
nickname = li_col_05_ring01
pos = 0, 0, -600
rotate = 0, 0, 0
archetype = small_ring
parent = li_col_05

[Object]
nickname = li_col_05_ring01
pos = 0, 0, -700
rotate = 0, 0, 0
archetype = small_ring
parent = li_col_05

[Object]
nickname = li_col_05_SHIELDGEN_gird01
pos = 0, 210, -60
rotate = 45, 0, 0
archetype = space_girderb
parent = li_col_05

[Object]
nickname = li_col_05_SHIELDGEN_gird02
pos = 0, 310, -60
rotate = -45, 0, 0
archetype = space_girderb
parent = li_col_05

[Object]
nickname = li_col_05_SHIELDGEN_gird03
pos = 0, 210, 60
rotate = -45, 0, 0
archetype = space_girderb
parent = li_col_05

[Object]
nickname = li_col_05_SHIELDGEN_gird04
pos = 0, 310, 60
rotate = 45, 0, 0
archetype = space_girderb
parent = li_col_05

[Object]
nickname = li_col_05_SHIELDGEN_gird05
pos = 60, 210, 0
rotate = -45, 90, 0
archetype = space_girderb
parent = li_col_05

[Object]
nickname = li_col_05_SHIELDGEN_gird06
pos = 60, 310, 0
rotate = 45, 90, 0
archetype = space_girderb
parent = li_col_05

[Object]
nickname = li_col_05_SHIELDGEN_gird07
pos = -60, 210, 0
rotate = 45, 90, 0
archetype = space_girderb
parent = li_col_05

[Object]
nickname = li_col_05_SHIELDGEN_gird08
pos = -60, 310, 0
rotate = 45, -90, 0
archetype = space_girderb
parent = li_col_05

[Object]
nickname = li_col_05_SHIELDGEN_ring01
pos = 0, 260, 0
rotate = 90, 0, 0
archetype = small_ring
parent = li_col_05

[Object]
nickname = li_col_05_SHIELDGEN_ring02
pos = 0, 310, 0
rotate = 90, 0, 0
archetype = smallest_ring
parent = li_col_05

[Object]
nickname = li_col_05_SHIELDGEN_ring03
pos = 0, 210, 0
rotate = 90, 0, 0
archetype = smallest_ring
parent = li_col_05

[Object]
nickname = li_col_05_gen01
pos = 0, 0, 610
rotate = 90, 0, 0
archetype = dyson_generator
parent = li_col_05

[Object]
nickname = li_col_05_gen02
pos = 330, 0, 0
rotate = 0, 0, -90
archetype = dyson_generator
parent = li_col_05

[Object]
nickname = li_col_05_gen03
pos = -330, 0, 0
rotate = 0, 0, 90
archetype = dyson_generator
parent = li_col_05

[Object]
nickname = li_col_05_kernel01
pos = 0, 260, 0
rotate = 0, 0, 0
archetype = nomad_kernel
parent = li_col_05
'''