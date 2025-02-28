from templates.space_object_template import SpaceObjectTemplate


class TradingDoors(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rmbase02'
    TEMPLATE = '''

[Object]
nickname = rmbase02_ROOT
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_industrial01e

[Object]
nickname = rmbase02_ring01
pos = 0, 0, 0
rotate = 90, 0, 0
archetype = smallest_ring

[Object]
nickname = rmbase02_ring02
pos = 0, 30, 0
rotate = 90, 0, 0
archetype = smallest_ring

[Object]
nickname = rmbase02_ring03
pos = 0, -30, 0
rotate = 90, 0, 0
archetype = smallest_ring

[Object]
nickname = rmbase02_gider01
pos = 0, 0, 0
rotate = 90, 0, 0
archetype = space_girderc

[Object]
nickname = rmbase02_door01
pos = 2, 0.5, 320
rotate = 90, 0, 0
archetype = space_door_half

[Object]
nickname = rmbase02_door02
pos = -2, -0.5, -320
rotate = -90, 0, 0
archetype = space_door_half

[Object]
nickname = rmbase02_door03
pos = 2, -0.5, 320
rotate = -90, 180, 0
archetype = space_door_half

[Object]
nickname = rmbase02_door04
pos = -2, 0.5, -320
rotate = 90, 180, 0
archetype = space_door_half

[Object]
nickname = rmbase02_panel01
pos = 0, 90, 225
rotate = 105, 0, 0
archetype = space_station_panelb

[Object]
nickname = rmbase02_panel02
pos = 0, -90, 225
rotate = 75, 0, 0
archetype = space_station_panelb

[Object]
nickname = rmbase02_panel03
pos = 90, 0, 225
rotate = 75, 0, 90
archetype = space_station_panelb

[Object]
nickname = rmbase02_panel04
pos = -90, 0, 225
rotate = 105, 0, 90
archetype = space_station_panelb

[Object]
nickname = rmbase02_panel05
pos = 0, 90, -225
rotate = -105, 0, 0
archetype = space_station_panelb

[Object]
nickname = rmbase02_panel06
pos = 0, -90, -225
rotate = -75, 0, 0
archetype = space_station_panelb

[Object]
nickname = rmbase02_panel07
pos = 90, 0, -225
rotate = -75, 0, 90
archetype = space_station_panelb

[Object]
nickname = rmbase02_panel08
pos = -90, 0, -225
rotate = -105, 0, 90
archetype = space_station_panelb

[Object]
nickname = rmbase02_airlock01
pos = 0, 275, 0
rotate = 90, 0, 0
archetype = space_airlock_dummy

[Object]
nickname = rmbase02_airlock02
pos = 0, -275, 0
rotate = -90, 0, 0
archetype = space_airlock_dummy

[Object]
nickname = rmbase02_habitat01
pos = 0, 390, 0
rotate = 0, 0, 0
archetype = space_small_control_block

[Object]
nickname = rmbase02_habitat02
pos = 0, -390, 0
rotate = 180, 0, 0
archetype = space_small_control_block

[Object]
nickname = rmbase02_control_tower01
pos = 0, 125, 0
rotate = 0, 0, 0
archetype = space_control_tower

[Object]
nickname = rmbase02_control_tower02
pos = 0, -125, 0
rotate = 0, 0, 0
archetype = space_control_tower

[Object]
nickname = rmbase02_control_tower03
pos = 0, 175, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower

[Object]
nickname = rmbase02_control_tower04
pos = 0, 330, 0
rotate = 0, 0, 0
archetype = space_small_control_tower

[Object]
nickname = rmbase02_control_tower05
pos = 0, -175, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower

[Object]
nickname = rmbase02_control_tower06
pos = 0, -330, 0
rotate = 0, 0, 0
archetype = space_small_control_tower

[Object]
nickname = rmbase02_industrial01
pos = 175, 0, 0
rotate = 0, 90, 90
archetype = space_industriala

[Object]
nickname = rmbase02_industrial02
pos = 148, 2, 85
rotate = 90, 60, 0
archetype = space_industrial02d

[Object]
nickname = rmbase02_industrial03
pos = 148, 2, -85
rotate = 90, -60, 0
archetype = space_industrial02d

[Object]
nickname = rmbase02_industrial04
pos = -175, 0, 0
rotate = 0, 90, 90
archetype = space_industriala

[Object]
nickname = rmbase02_industrial05
pos = -148, 2, 85
rotate = 90, -60, 0
archetype = space_industrial02d

[Object]
nickname = rmbase02_industrial06
pos = -148, 2, -85
rotate = 90, 60, 0
archetype = space_industrial02d
    '''


class XenosOutpostPanels(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rmbase01'
    TEMPLATE = '''[Object]
nickname = rmbase01_door
pos = 0, 0, -115
rotate = 0, 0, 0
archetype = space_door_lock2_destroyable

[Object]
nickname = rmbase01
pos = 0, 0, 110
rotate = 90, 0, 0
archetype = space_medium_control_tower

[Object]
nickname = rmbase01_ring
pos = 0, 0, -115
rotate = 0, 0, 0
archetype = small_ring
parent = rmbase01

[Object]
nickname = rmbase01_control_tower03
pos = 0, -180, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = rmbase01

[Object]
nickname = rmbase01_ind01
pos = 0, 110, 0
rotate = 0, 0, 0
archetype = space_industrial02d
parent = rmbase01

[Object]
nickname = rmbase01_ind02
pos = 60, -100, 0
rotate = 0, 0, 30
archetype = space_industrial02d
parent = rmbase01

[Object]
nickname = rmbase01_ind03
pos = -60, -100, 0
rotate = 0, 0, -30
archetype = space_industrial02d
parent = rmbase01

[Object]
nickname = rmbase01_ind04
pos = 130, -50, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rmbase01

[Object]
nickname = rmbase01_ind05
pos = -130, -50, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rmbase01

[Object]
nickname = rmbase01_ind06
pos = 0, -120, 0
rotate = 0, 0, 90
archetype = space_industrial02d
parent = rmbase01

[Object]
nickname = rmbase01_habitat01
pos = 0, 180, 0
rotate = 0, 0, 0
archetype = space_pirate_control_block
parent = rmbase01

[Object]
nickname = rmbase01_habitat02
pos = 0, -240, 0
rotate = 180, 0, 0
archetype = space_pirate_control_block
parent = rmbase01

[Object]
nickname = rmbase01_panel01
pos = -100, 50, 0
rotate = 0, 0, 0
archetype = space_debris_panel
parent = rmbase01

[Object]
nickname = rmbase01_panel02
pos = 100, 50, 0
rotate = 0, 180, 0
archetype = space_debris_panel
parent = rmbase01
'''