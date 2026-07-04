from templates.space_object_template import SpaceObjectTemplate

WILLARD_GEN_ORIGINAL = '''[Object]
nickname = sig13_gasfield_super01_gen01
pos = -330, -60, 190
rotate = 90, -60, 0
archetype = dyson_small_generator

[Object]
nickname = sig13_gasfield_super01_gen02
pos = 330, -60, 190
rotate = 90, 60, 0
archetype = dyson_small_generator

[Object]
nickname = sig13_gasfield_super01_gen03
pos = 0, -60, -375
rotate = -90, 0, 0
archetype = dyson_small_generator
'''


class WillardFull(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'sig13_gasfield_super01'
    TEMPLATE = '''[Object]
nickname = sig13_gasfield_super01_ast_main
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = ice_asteroid_mineable_base

[Object]
nickname = sig13_gasfield_super01_gen01
pos = 0, -60, 0
rotate = 0, -30, 0
archetype = dyson_small_generator_sig13

[Object]
nickname = sig13_gasfield_super01_gen02
pos = 0, -60, 0
rotate = 0, -150, 0
archetype = dyson_small_generator_sig13

[Object]
nickname = sig13_gasfield_super01_gen03
pos = 0, -60, 0
rotate = 0, 90, 0
archetype = dyson_small_generator_sig13

[Object]
nickname = sig13_gasfield_super01_ROOT
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_hidden_connect

[Object]
nickname = sig13_gasfield_super01_ctrl_twr01
pos = 0, -160, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_girder01
pos = 0, -160, 0
rotate = -16.5, -60, 0
archetype = space_girdera
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_girder02
pos = 0, -160, 0
rotate = -16.5, 60, 0
archetype = space_girdera
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_girder03
pos = 0, -160, 0
rotate = -16.5, 180, 0
archetype = space_girdera
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_girder04
pos = -1, -60, 0
rotate = 0, -60, 0
archetype = space_girdera
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_girder05
pos = -1, -60, 0
rotate = 0, 60, 0
archetype = space_girdera
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_girder06
pos = -1, -60, 0
rotate = 0, 180, 0
archetype = space_girdera
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_ind01
pos = 0, -150, 0
rotate = -90, 0, 0
archetype = space_industrialc
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_gird01
pos = 0, 10, -60
rotate = 45, 0, 0
archetype = space_girderb
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_gird02
pos = 0, 110, -60
rotate = -45, 0, 0
archetype = space_girderb
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_gird03
pos = 0, 10, 60
rotate = -45, 0, 0
archetype = space_girderb
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_gird04
pos = 0, 110, 60
rotate = 45, 0, 0
archetype = space_girderb
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_gird05
pos = 60, 10, 0
rotate = -45, 90, 0
archetype = space_girderb
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_gird06
pos = 60, 110, 0
rotate = 45, 90, 0
archetype = space_girderb
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_gird07
pos = -60, 10, 0
rotate = 45, 90, 0
archetype = space_girderb
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_gird08
pos = -60, 110, 0
rotate = 45, -90, 0
archetype = space_girderb
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_ring01
pos = 0, 60, 0
rotate = 90, 0, 0
archetype = small_ring
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_ring02
pos = 0, 110, 0
rotate = 90, 0, 0
archetype = smallest_ring
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_ring03
pos = 0, 10, 0
rotate = 90, 0, 0
archetype = smallest_ring
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_gas_inner01
pos = 0, 50, 0
rotate = 90, 0, 0
archetype = ice_research_block
visit = 16

[Object]
nickname = sig13_gasfield_super01_gas_inner02
pos = 0, -600, 0
rotate = 0, 0, 0
archetype = sig13_mineable_gas_static
visit = 16
'''


class Willard(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'sig13_gasfield_super01'
    TEMPLATE = '''[Object]
nickname = sig13_gasfield_super01_ast_main
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = ice_asteroid_mineable_base

[Object]
nickname = sig13_gasfield_super01_gen01
pos = 0, -60, 0
rotate = 0, -30, 0
archetype = dyson_small_generator_sig13

[Object]
nickname = sig13_gasfield_super01_gen02
pos = 0, -60, 0
rotate = 0, -150, 0
archetype = dyson_small_generator_sig13

[Object]
nickname = sig13_gasfield_super01_gen03
pos = 0, -60, 0
rotate = 0, 90, 0
archetype = dyson_small_generator_sig13

[Object]
nickname = sig13_gasfield_super01_ROOT
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = ice_scient_base

[Object]
nickname = sig13_gasfield_super01_gas_inner01
pos = 0, 50, 0
rotate = 90, 0, 0
archetype = ice_research_block
visit = 16
'''


class ScientRootComponents(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'sig13_gasfield_super01'
    TEMPLATE = '''[Object]
nickname = sig13_gasfield_super01_ctrl_twr01
pos = 0, -160, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_girder01
pos = 0, -160, 0
rotate = -16.5, -60, 0
archetype = space_girdera
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_girder02
pos = 0, -160, 0
rotate = -16.5, 60, 0
archetype = space_girdera
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_girder03
pos = 0, -160, 0
rotate = -16.5, 180, 0
archetype = space_girdera
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_girder04
pos = -1, -60, 0
rotate = 0, -60, 0
archetype = space_girdera
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_girder05
pos = -1, -60, 0
rotate = 0, 60, 0
archetype = space_girdera
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_girder06
pos = -1, -60, 0
rotate = 0, 180, 0
archetype = space_girdera
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_ind01
pos = 0, -150, 0
rotate = -90, 0, 0
archetype = space_industrialc
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_gird01
pos = 0, 10, -60
rotate = 45, 0, 0
archetype = space_girderb
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_gird02
pos = 0, 110, -60
rotate = -45, 0, 0
archetype = space_girderb
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_gird03
pos = 0, 10, 60
rotate = -45, 0, 0
archetype = space_girderb
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_gird04
pos = 0, 110, 60
rotate = 45, 0, 0
archetype = space_girderb
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_gird05
pos = 60, 10, 0
rotate = -45, 90, 0
archetype = space_girderb
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_gird06
pos = 60, 110, 0
rotate = 45, 90, 0
archetype = space_girderb
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_gird07
pos = -60, 10, 0
rotate = 45, 90, 0
archetype = space_girderb
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_gird08
pos = -60, 110, 0
rotate = 45, -90, 0
archetype = space_girderb
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_ring01
pos = 0, 60, 0
rotate = 90, 0, 0
archetype = small_ring
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_ring02
pos = 0, 110, 0
rotate = 90, 0, 0
archetype = smallest_ring
parent = sig13_gasfield_super01_ROOT

[Object]
nickname = sig13_gasfield_super01_SHIELDGEN_ring03
pos = 0, 10, 0
rotate = 90, 0, 0
archetype = smallest_ring
parent = sig13_gasfield_super01_ROOT
'''
