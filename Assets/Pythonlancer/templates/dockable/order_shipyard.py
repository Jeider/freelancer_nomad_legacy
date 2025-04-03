from templates.space_object_template import SpaceObjectTemplate


class OrderShipyard(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'or_ship_01'
    TEMPLATE = '''[Object]
nickname = or_ship_01
pos = 0, 1120, 0
rotate = 0, 0, 0
archetype = space_small_control_block_station_root
{root_props}

[Object]
nickname = or_ship_01_S1_ind01
pos = 0, 1000, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_ind02
pos = 0, 1000, 1820
rotate = 0, 0, 0
archetype = space_industrial02a
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_ind03
pos = 0, 1000, -1820
rotate = 0, 0, 0
archetype = space_industrial02a
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_ind04
pos = 0, 1000, 3630
rotate = 0, 0, 0
archetype = space_industrial02a
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_ind05
pos = 0, 1000, -3630
rotate = 0, 0, 0
archetype = space_industrial02a
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_ind06
pos = 0, -1000, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_ind07
pos = 0, -1000, 1820
rotate = 0, 0, 0
archetype = space_industrial02a
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_ind08
pos = 0, -1000, -1820
rotate = 0, 0, 0
archetype = space_industrial02a
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_ind09
pos = 0, -1000, 3630
rotate = 0, 0, 0
archetype = space_industrial02a
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_ind10
pos = 0, -1000, -3630
rotate = 0, 0, 0
archetype = space_industrial02a
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_conn01
pos = 0, 1000, 135
rotate = 0, 0, 0
archetype = space_tube_fix
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_conn02
pos = 0, 1000, -135
rotate = 0, 180, 0
archetype = space_tube_fix
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_conn03
pos = 0, 1000, 1950
rotate = 0, 0, 0
archetype = space_tube_fix
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_conn04
pos = 0, 1000, -1950
rotate = 0, 180, 0
archetype = space_tube_fix
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_conn05
pos = 0, -1000, 135
rotate = 0, 0, 0
archetype = space_tube_fix
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_conn06
pos = 0, -1000, -135
rotate = 0, 180, 0
archetype = space_tube_fix
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_conn07
pos = 0, -1000, 1950
rotate = 0, 0, 0
archetype = space_tube_fix
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_conn08
pos = 0, -1000, -1950
rotate = 0, 180, 0
archetype = space_tube_fix
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_tube01
pos = 50, 1000, 0
rotate = 90, 0, 60
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_tube02
pos = 50, -1000, 0
rotate = 90, 0, 120
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_tube03
pos = 1175, 480, 0
rotate = 90, 0, 60
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_tube04
pos = 1175, -480, 0
rotate = 90, 0, 120
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_tube05
pos = -50, 1000, 0
rotate = 90, 0, -60
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_tube06
pos = -50, -1000, 0
rotate = 90, 0, -120
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_tube07
pos = -1175, 480, 0
rotate = 90, 0, -60
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_tube08
pos = -1175, -480, 0
rotate = 90, 0, -120
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_shipyard01
pos = 0, 870, 0
rotate = 0, 0, 180
archetype = shipyard
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_shipyard02
pos = 0, -870, 0
rotate = 0, 0, 0
archetype = shipyard
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_shipyard01
pos = 950, 500, 0
rotate = 0, 0, 0
archetype = shipyard_2x
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_shipyard02
pos = 950, -500, 0
rotate = 0, 0, 180
archetype = shipyard_2x
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_shipyard03
pos = 2040, 50, 0
rotate = 0, 0, 180
archetype = shipyard_2x
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_shipyard04
pos = -950, 500, 0
rotate = 0, 0, 0
archetype = shipyard_2x
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_shipyard05
pos = -950, -500, 0
rotate = 0, 0, 180
archetype = shipyard_2x
parent = or_ship_01

[Object]
nickname = or_ship_01_S1_shipyard06
pos = -2040, 50, 0
rotate = 0, 0, 180
archetype = shipyard_2x
parent = or_ship_01

[Object]
nickname = or_ship_01_S2_tube01
pos = 50, 1000, 3630
rotate = 90, 0, 60
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S2_tube02
pos = 50, -1000, 3630
rotate = 90, 0, 120
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S2_tube03
pos = 1175, 480, 3630
rotate = 90, 0, 60
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S2_tube04
pos = 1175, -480, 3630
rotate = 90, 0, 120
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S2_tube05
pos = -50, 1000, 3630
rotate = 90, 0, -60
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S2_tube06
pos = -50, -1000, 3630
rotate = 90, 0, -120
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S2_tube07
pos = -1175, 480, 3630
rotate = 90, 0, -60
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S2_tube08
pos = -1175, -480, 3630
rotate = 90, 0, -120
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S2_shipyard01
pos = 0, 870, 3630
rotate = 0, 0, 180
archetype = shipyard
parent = or_ship_01

[Object]
nickname = or_ship_01_S2_shipyard02
pos = 0, -870, 3630
rotate = 0, 0, 0
archetype = shipyard
parent = or_ship_01

[Object]
nickname = or_ship_01_S2_shipyard01
pos = 950, 500, 3630
rotate = 0, 0, 0
archetype = shipyard_2x
parent = or_ship_01

[Object]
nickname = or_ship_01_S2_shipyard02
pos = 950, -500, 3630
rotate = 0, 0, 180
archetype = shipyard_2x
parent = or_ship_01

[Object]
nickname = or_ship_01_S2_shipyard03
pos = 2040, 50, 3630
rotate = 0, 0, 180
archetype = shipyard_2x
parent = or_ship_01

[Object]
nickname = or_ship_01_S2_shipyard04
pos = -950, 500, 3630
rotate = 0, 0, 0
archetype = shipyard_2x
parent = or_ship_01

[Object]
nickname = or_ship_01_S2_shipyard05
pos = -950, -500, 3630
rotate = 0, 0, 180
archetype = shipyard_2x
parent = or_ship_01

[Object]
nickname = or_ship_01_S2_shipyard06
pos = -2040, 50, 3630
rotate = 0, 0, 180
archetype = shipyard_2x
parent = or_ship_01

[Object]
nickname = or_ship_01_S3_tube01
pos = 50, 1000, -3630
rotate = 90, 0, 60
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S3_tube02
pos = 50, -1000, -3630
rotate = 90, 0, 120
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S3_tube03
pos = 1175, 480, -3630
rotate = 90, 0, 60
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S3_tube04
pos = 1175, -480, -3630
rotate = 90, 0, 120
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S3_tube05
pos = -50, 1000, -3630
rotate = 90, 0, -60
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S3_tube06
pos = -50, -1000, -3630
rotate = 90, 0, -120
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S3_tube07
pos = -1175, 480, -3630
rotate = 90, 0, -60
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S3_tube08
pos = -1175, -480, -3630
rotate = 90, 0, -120
archetype = space_short_tube
parent = or_ship_01

[Object]
nickname = or_ship_01_S3_shipyard01
pos = 0, 870, -3630
rotate = 0, 0, 180
archetype = shipyard
parent = or_ship_01

[Object]
nickname = or_ship_01_S3_shipyard02
pos = 0, -870, -3630
rotate = 0, 0, 0
archetype = shipyard
parent = or_ship_01

[Object]
nickname = or_ship_01_S3_shipyard01
pos = 950, 500, -3630
rotate = 0, 0, 0
archetype = shipyard_2x
parent = or_ship_01

[Object]
nickname = or_ship_01_S3_shipyard02
pos = 950, -500, -3630
rotate = 0, 0, 180
archetype = shipyard_2x
parent = or_ship_01

[Object]
nickname = or_ship_01_S3_shipyard03
pos = 2040, 50, -3630
rotate = 0, 0, 180
archetype = shipyard_2x
parent = or_ship_01

[Object]
nickname = or_ship_01_S3_shipyard04
pos = -950, 500, -3630
rotate = 0, 0, 0
archetype = shipyard_2x
parent = or_ship_01

[Object]
nickname = or_ship_01_S3_shipyard05
pos = -950, -500, -3630
rotate = 0, 0, 180
archetype = shipyard_2x
parent = or_ship_01

[Object]
nickname = or_ship_01_S3_shipyard06
pos = -2040, 50, -3630
rotate = 0, 0, 180
archetype = shipyard_2x
parent = or_ship_01
'''
