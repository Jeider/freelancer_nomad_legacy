from templates.space_object_template import SpaceObjectTemplate


class SpaceArch(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'arch_02'
    TEMPLATE = '''[Object]
nickname = arch_02
pos = 0.00000, 0.00000, 0.00000
rotate = 0, -71, 2
archetype = space_arch
{dock_props}

[Object]
nickname = arch_02_Asteroid
ids_name = 196765
pos = 0.00000, 0.00000, 0.00000
rotate = 0, -71, 2
archetype = space_arch_asteroid2
ids_info = 65879
visit = 128
behavior = NOTHING
parent = arch_02

[Object]
nickname = arch_02_space_arch_chunk1a_1
pos = -1343.00000, -1000.00000, -9018.00000
rotate = 0, -70, 0
archetype = space_arch_chunk1a

[Object]
nickname = arch_02_space_arch_chunk1b_1
pos = -7436.00000, 200.00000, -13820.00000
rotate = 0, -60, 0
archetype = space_arch_chunk1b

[Object]
nickname = arch_02_space_arch_chunk2a_1
pos = -9825.00000, 0.00000, -17760.00000
rotate = 20, -20, 0
archetype = space_arch_chunk2a

[Object]
nickname = arch_02_space_arch_chunk2b_1
pos = -4921.00000, -1300.00000, -4822.00000
rotate = -110, -49, 102
archetype = space_arch_chunk2b

[Object]
nickname = arch_02_space_arch_chunk3a_1
pos = 1277.00000, 0.00000, -15431.00000
rotate = 30, 60, 0
archetype = space_arch_chunk3a

[Object]
nickname = arch_02_space_arch_chunk3b_1
pos = -2904.00000, 0.00000, -18345.00000
rotate = 0, -20, 0
archetype = space_arch_chunk3b

[Object]
nickname = arch_02_space_arch_chunk3c_1
pos = -2136.00000, 0.00000, -11249.00000
archetype = space_arch_chunk3c

[Object]
nickname = arch_02_space_arch_chunk3d_1
pos = -1606.00000, 0.00000, -13286.00000
rotate = 0, -20, 0
archetype = space_arch_chunk3d

[Object]
nickname = arch_02_space_arch_chunk3e_1
pos = -7587.00000, 0.00000, -8275.00000
rotate = 115, -20, 0
archetype = space_arch_chunk3e
'''
