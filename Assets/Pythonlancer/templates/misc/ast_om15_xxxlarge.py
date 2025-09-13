from templates.space_object_template import SpaceObjectTemplate


class AsteroidOne(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'om13alt_ast_a01'
    TEMPLATE = '''
[Object]
nickname = om13alt_ast_a01
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = om15_xxxlarge_asteroid

[Object]
nickname = om13alt_ast_a01_01
pos = -1750, 720, 400
rotate = 0, 110, -20
archetype = om15_xxxlarge_door

[Object]
nickname = om13alt_ast_a01_02
pos = -1150, 520, 150
rotate = 0, 120, -25
archetype = om15_xxxlarge_tunnel02

[Object]
nickname = om13alt_ast_a01_03
pos = -780, 150, 100
rotate = -60, -60, 180
archetype = om15_xxxlarge_tunnel02

[Object]
nickname = om13alt_ast_a01_04
pos = -350, -150, 150
rotate = 150, -80, -180
archetype = om15_xxxlarge_tunnel03

[Object]
nickname = om13alt_ast_a01_05
pos = 500, -500, 300
rotate = 180, 50, 0
archetype = om15_xxxlarge_tunnel02

[Object]
nickname = om13alt_ast_a01_09
pos = 950, -520, 820
rotate = 0, -140, 0
archetype = om15_xxxlarge_door
'''


class AsteroidTwo(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'om13alt_ast_a02'
    TEMPLATE = '''
[Object]
nickname = om13alt_ast_a02
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = om15_xxxlarge_asteroid2

[Object]
nickname = om13alt_ast_a02_01
pos = -420, -550, -1240
rotate = -20, 5, 0
archetype = om15_xxxlarge_door

[Object]
nickname = om13alt_ast_a02_02
pos = -380, -350, -640
rotate = 20, -10, 220
archetype = om15_xxxlarge_tunnel02

[Object]
nickname = om13alt_ast_a02_03
pos = -350, 250, 0
rotate = -50, -50, 0
archetype = om15_xxxlarge_tunnel04

[Object]
nickname = om13alt_ast_a02_05
pos = 550, -220, 370
rotate = 180, 45, 0
archetype = om15_xxxlarge_tunnel02

[Object]
nickname = om13alt_ast_a02_09
pos = 920, -220, 800
rotate = 0, -140, 0
archetype = om15_xxxlarge_door
'''

    EXTRA = '''
[Object]
nickname = om13alt_ast_a02_11
pos = -120, -250, -280
rotate = -20, 26, 0
archetype = om15_xxxlarge_tunnel03

[Object]
nickname = om13alt_ast_a02_12
pos = 240, -180, 70
rotate = 0, -41, -2
archetype = om15_xxxlarge_tunnel06
'''


class AsteroidFour(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'om13alt_ast_a02'
    TEMPLATE = AsteroidTwo.TEMPLATE + AsteroidTwo.EXTRA


class AsteroidThree(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'om13alt_ast_a03'
    TEMPLATE = '''
[Object]
nickname = om13alt_ast_a03_01
pos = -1750, 720, 400
rotate = 0, 110, -20
archetype = om15_xxxlarge_door

[Object]
nickname = om13alt_ast_a03_03
pos = -1046, 356, 179
rotate = -98, 29, -131
archetype = om15_xxxlarge_tunnel01

[Object]
nickname = om13alt_ast_a03_07
pos = -300, -450, -450
rotate = 180, 45, 0
archetype = om15_xxxlarge_tunnel02

[Object]
nickname = om13alt_ast_a03_06
pos = -680, -200, -580
rotate = 180, -20, -40
archetype = om15_xxxlarge_wall

[Object]
nickname = om13alt_ast_a03_08
pos = -50, -450, -150
rotate = -23, 26, -43
archetype = om15_xxxlarge_tunnel05

[Object]
nickname = om13alt_ast_a03_05
pos = 550, -500, 350
rotate = -5, 45, 0
archetype = om15_xxxlarge_tunnel03

[Object]
nickname = om13alt_ast_a03_09
pos = 950, -520, 820
rotate = 0, -140, 0
archetype = om15_xxxlarge_door
'''
