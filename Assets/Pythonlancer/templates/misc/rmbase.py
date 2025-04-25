from templates.space_object_template import SpaceObjectTemplate


class RmbasePanels(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rmbase01'
    TEMPLATE = '''
[Object]
nickname = rmbase01
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_industrial01d

[Object]
nickname = rmbase01_ring01
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = smallest_ring
loadout = space_ind01_reactor

[Object]
nickname = rmbase01_ring02
pos = 0, 0, 30
rotate = 0, 0, 0
archetype = smallest_ring
loadout = space_ind01_reactor

[Object]
nickname = rmbase01_ring03
pos = 0, 0, -30
rotate = 0, 0, 0
archetype = smallest_ring
loadout = space_ind01_reactor

[Object]
nickname = rmbase01_control_tower01
pos = 0, 0, 110
rotate = 90, 0, 0
archetype = space_medium_control_tower

[Object]
nickname = rmbase01_control_tower02
pos = 0, 0, -110
rotate = 90, 0, 0
archetype = space_medium_control_tower

[Object]
nickname = rmbase01_control_tower03
pos = 0, -180, 0
rotate = 0, 0, 0
archetype = space_small_control_tower

[Object]
nickname = rmbase01_ind01
pos = 0, 110, 0
rotate = 0, 0, 0
archetype = space_industrial02d

[Object]
nickname = rmbase01_ind02
pos = 60, -100, 0
rotate = 0, 0, 30
archetype = space_industrial02d

[Object]
nickname = rmbase01_ind03
pos = -60, -100, 0
rotate = 0, 0, -30
archetype = space_industrial02d

[Object]
nickname = rmbase01_ind04
pos = 130, -50, 0
rotate = 0, 0, 0
archetype = space_industriala

[Object]
nickname = rmbase01_ind05
pos = -130, -50, 0
rotate = 0, 0, 0
archetype = space_industriala

[Object]
nickname = rmbase01_ind06
pos = 0, -120, 0
rotate = 0, 0, 90
archetype = space_industrial02d

[Object]
nickname = rmbase01_habitat01
pos = 0, 180, 0
rotate = 0, 0, 0
archetype = space_pirate_control_block

[Object]
nickname = rmbase01_habitat02
pos = 0, -240, 0
rotate = 180, 0, 0
archetype = space_pirate_control_block

[Object]
nickname = rmbase01_panel01
pos = -100, 50, 0
rotate = 0, 0, 0
archetype = space_debris_panel

[Object]
nickname = rmbase01_panel02
pos = 100, 50, 0
rotate = 0, 180, 0
archetype = space_debris_panel
    '''


class RmbaseDoors(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rmbase02'
    TEMPLATE = '''

[Object]
nickname = rmbase02_ROOT
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_industrial01e

[Object]
nickname = rmbase02_root01
pos = 0, 82, 0
rotate = -90, 0, 0
archetype = space_industrial01c

[Object]
nickname = rmbase02_root02
pos = 0, -82, 0
rotate = 90, 0, 0
archetype = space_industrial01c

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


class RmbaseSmugglers(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rmbase03'
    TEMPLATE = '''
[Object]
nickname = rmbase03_root
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_industrial01f

[Object]
nickname = rmbase03_tunnel01
pos = 0, 0, -180
rotate = 0, 0, 0
archetype = space_tunnel

[Object]
nickname = rmbase03_tunnel02
pos = 0, 0, 180
rotate = 0, 180, 0
archetype = space_tunnel

[Object]
nickname = rmbase03_door01
pos = 0, 0, 120
rotate = 0, 0, 0
archetype = space_small_door

[Object]
nickname = rmbase03_door02
pos = 0, 0, 180
rotate = 0, 0, 0
archetype = space_small_door

[Object]
nickname = rmbase03_door03
pos = 0, 0, 280
rotate = 0, 0, 0
archetype = space_small_door

[Object]
nickname = rmbase03_door04
pos = 0, 0, -120
rotate = 0, 180, 0
archetype = space_small_door

[Object]
nickname = rmbase03_door05
pos = 0, 0, -180
rotate = 0, 180, 0
archetype = space_small_door

[Object]
nickname = rmbase03_door06
pos = 0, 0, -280
rotate = 0, 180, 0
archetype = space_small_door

[Object]
nickname = rmbase03_ind01
pos = 0, 100, 0
rotate = 0, 0, 90
archetype = space_industrial02d

[Object]
nickname = rmbase03_ind02
pos = 60, 60, 0
rotate = 0, 0, -45
archetype = space_industrial02d

[Object]
nickname = rmbase03_ind03
pos = -60, 60, 0
rotate = 0, 0, 45
archetype = space_industrial02d

[Object]
nickname = rmbase03_ind04
pos = 110, 0, 0
rotate = 0, 0, 0
archetype = space_industriala

[Object]
nickname = rmbase03_ind05
pos = 60, -60, 0
rotate = 0, 0, 45
archetype = space_industrial02d

[Object]
nickname = rmbase03_ind06
pos = -60, -60, 0
rotate = 0, 0, -45
archetype = space_industrial02d

[Object]
nickname = rmbase03_ind07
pos = 0, -100, 0
rotate = 0, 0, 90
archetype = space_industrial02d

[Object]
nickname = rmbase03_ind08
pos = -110, 0, 0
rotate = 0, 0, 0
archetype = space_industriala

[Object]
nickname = rmbase03_habitat01
pos = 0, 190, 75
rotate = 0, 0, 0
archetype = space_pirate_control_block

[Object]
nickname = rmbase03_habitat02
pos = 0, 190, -75
rotate = 0, 90, 0
archetype = space_pirate_control_block

[Object]
nickname = rmbase03_habitat03
pos = 0, 260, 0
rotate = 0, 180, 0
archetype = space_pirate_control_block

[Object]
nickname = rmbase03_habitat04
pos = 0, 170, 0
rotate = 0, 0, 0
archetype = space_habitat_wide

[Object]
nickname = rmbase03_ring01
pos = 0, 0, 100
rotate = 0, 0, 0
archetype = smallest_ring

[Object]
nickname = rmbase03_ring02
pos = 0, 0, -100
rotate = 0, 0, 0
archetype = smallest_ring

[Object]
nickname = rmbase03_tanks01
pos = 0, -150, 0
rotate = 0, 0, 0
archetype = space_tankl4

[Object]
nickname = rmbase03_tanks02
pos = 110, -60, 0
rotate = 0, 0, 0
archetype = space_tankl4

[Object]
nickname = rmbase03_tanks03
pos = -110, -60, 0
rotate = 0, 0, 0
archetype = space_tankl4

[Object]
nickname = rmbase03_girder01
pos = 0, 85, 150
rotate = 30, 0, 0
archetype = space_girderc

[Object]
nickname = rmbase03_girder02
pos = 0, -85, 150
rotate = -30, 0, 0
archetype = space_girderc

[Object]
nickname = rmbase03_girder03
pos = 0, 85, -150
rotate = -30, 0, 0
archetype = space_girderc

[Object]
nickname = rmbase03_girder04
pos = 0, -85, -150
rotate = 30, 0, 0
archetype = space_girderc

[Object]
nickname = rmbase03_girder05
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_girderb

[Object]
nickname = rmbase03_girder06
pos = 0, 0, 0
rotate = 90, 0, 0
archetype = space_girderb
    '''


class RmbaseTraders(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rmbase04'
    TEMPLATE = '''

[Object]
nickname = rmbase04_root
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_industrial01f

[Object]
nickname = rmbase04_airlock01
pos = 0, 200, 0
rotate = 90, 0, 0
archetype = space_airlock_tunnel

[Object]
nickname = rmbase04_airlock02
pos = 0, -200, 0
rotate = -90, 0, 0
archetype = space_airlock_tunnel

[Object]
nickname = rmbase04_door01
pos = 0, 230, 0
rotate = 90, 0, 0
archetype = space_airlock_door

[Object]
nickname = rmbase04_door02
pos = 0, 120, 0
rotate = 90, 0, 0
archetype = space_airlock_door

[Object]
nickname = rmbase04_door03
pos = 0, -230, 0
rotate = 90, 0, 0
archetype = space_airlock_door

[Object]
nickname = rmbase04_door04
pos = 0, -120, 0
rotate = 90, 0, 0
archetype = space_airlock_door

[Object]
nickname = rmbase04_ring01
pos = 0, 120, 0
rotate = 90, -15, 0
archetype = small_ring

[Object]
nickname = rmbase04_ring02
pos = 0, -120, 0
rotate = 90, -15, 0
archetype = small_ring

[Object]
nickname = rmbase04_ind01
pos = 0, 0, 110
rotate = -90, 0, 0
archetype = space_industrial02d

[Object]
nickname = rmbase04_ind02
pos = 0, 0, -110
rotate = 90, 0, 0
archetype = space_industrial02d

[Object]
nickname = rmbase04_ind03
pos = 110, 0, 0
rotate = 90, 90, 0
archetype = space_industrial02d

[Object]
nickname = rmbase04_ind04
pos = -110, 0, 0
rotate = 90, 90, 0
archetype = space_industrial02d

[Object]
nickname = rmbase04_ind05
pos = 85, 0, 85
rotate = 90, 0, 0
archetype = space_industriala

[Object]
nickname = rmbase04_ind06
pos = 85, 0, -85
rotate = 90, 0, 0
archetype = space_industriala

[Object]
nickname = rmbase04_ind07
pos = -85, 0, 85
rotate = 90, 0, 0
archetype = space_industriala

[Object]
nickname = rmbase04_ind08
pos = -85, 0, -85
rotate = 90, 0, 0
archetype = space_industriala

[Object]
nickname = rmbase04_tanks01
pos = 0, 0, 280
rotate = 0, 0, 90
archetype = space_tankl4x4

[Object]
nickname = rmbase04_tanks02
pos = 0, 0, 480
rotate = 0, 0, 90
archetype = space_tankl2x2

[Object]
nickname = rmbase04_tanks03
pos = 0, 0, -280
rotate = 0, 0, 90
archetype = space_tankl4x4

[Object]
nickname = rmbase04_tanks04
pos = 0, 0, -480
rotate = 0, 0, 90
archetype = space_tankl2x2


[Object]
nickname = rmbase04_girder01
pos = 0, 0, -450
rotate = 15, 0, 0
archetype = space_girdera

[Object]
nickname = rmbase04_girder02
pos = 0, 0, -450
rotate = -15, 0, 0
archetype = space_girdera

[Object]
nickname = rmbase04_girder03
pos = 0, 0, 450
rotate = -15, 180, 0
archetype = space_girdera

[Object]
nickname = rmbase04_girder04
pos = 0, 0, 450
rotate = 15, 180, 0
archetype = space_girdera

[Object]
nickname = rmbase04_girder05
pos = 180, 80, 0
rotate = 30, 90, 0
archetype = space_girderb

[Object]
nickname = rmbase04_girder06
pos = 175, 70, -50
rotate = 25, 90, 0
archetype = space_girderb

[Object]
nickname = rmbase04_girder07
pos = 175, 70, 50
rotate = 25, 90, 0
archetype = space_girderb

[Object]
nickname = rmbase04_girder08
pos = 192, -80, 0
rotate = -30, 90, 0
archetype = space_girderb

[Object]
nickname = rmbase04_girder09
pos = 175, -80, -50
rotate = -25, 90, 0
archetype = space_girderb

[Object]
nickname = rmbase04_girder10
pos = 175, -80, 50
rotate = -25, 90, 0
archetype = space_girderb

[Object]
nickname = rmbase04_shipyard01
pos = 220, -18, 0
rotate = 0, 180, 0
archetype = shipyard_medium

[Object]
nickname = rmbase04_shipyard02
pos = -220, -18, 0
rotate = 0, 0, 0
archetype = shipyard_medium

[Object]
nickname = rmbase04_transport01
pos = 250, 0, 0
rotate = 0, 0, 0
archetype = large_transport

[Object]
nickname = rmbase04_transport02
pos = -250, 0, 0
rotate = 0, 0, 0
archetype = large_transport
    '''


class RmbaseShipyard(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rmbase05'
    TEMPLATE = '''
[Object]
nickname = rmbase05_root
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_industrial01d

[Object]
nickname = rmbase05_shield
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_medium_shield
loadout = rmbase_military_shipyard_demo_fx

[Object]
nickname = rmbase05_ring01
pos = 0, 0, 0
rotate = 0, 0, 90
archetype = large_ring

[Object]
nickname = rmbase05_ring02
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = smallest_ring

[Object]
nickname = rmbase05_ring03
pos = 0, 0, -30
rotate = 0, 0, 0
archetype = smallest_ring

[Object]
nickname = rmbase05_ring04
pos = 0, 0, 30
rotate = 0, 0, 0
archetype = smallest_ring

[Object]
nickname = rmbase05_ring05
pos = 0, 0, 500
rotate = 90, 0, 0
archetype = small_ring

[Object]
nickname = rmbase05_ring06
pos = 0, 0, -500
rotate = 90, 0, 0
archetype = small_ring

[Object]
nickname = rmbase05_ring07
pos = 0, 0, -500
rotate = 0, 0, 0
archetype = smallest_ring

[Object]
nickname = rmbase05_ring08
pos = 0, 0, -530
rotate = 0, 0, 0
archetype = smallest_ring

[Object]
nickname = rmbase05_ring09
pos = 0, 0, -470
rotate = 0, 0, 0
archetype = smallest_ring

[Object]
nickname = rmbase05_ring10
pos = 0, 0, 470
rotate = 0, 0, 0
archetype = smallest_ring

[Object]
nickname = rmbase05_ring11
pos = 0, 0, 500
rotate = 0, 0, 0
archetype = smallest_ring

[Object]
nickname = rmbase05_ring12
pos = 0, 0, 530
rotate = 0, 0, 0
archetype = smallest_ring

[Object]
nickname = rmbase05_ind01
pos = 0, 0, 240
rotate = 0, 0, 0
archetype = space_industriala

[Object]
nickname = rmbase05_ind02
pos = 0, 0, -240
rotate = 0, 0, 0
archetype = space_industriala

[Object]
nickname = rmbase05_ind03
pos = 0, 0, 500
rotate = 0, 0, 0
archetype = space_industrial01d

[Object]
nickname = rmbase05_ind04
pos = 0, 0, -500
rotate = 0, 0, 0
archetype = space_industrial01d

[Object]
nickname = rmbase05_girder01
pos = 0, 0, 110
rotate = 90, 0, 0
archetype = space_girderc

[Object]
nickname = rmbase05_girder02
pos = 0, 0, -110
rotate = 90, 0, 0
archetype = space_girderc

[Object]
nickname = rmbase05_girder03
pos = 110, 0, 0
rotate = 90, 0, 0
archetype = space_girderc

[Object]
nickname = rmbase05_girder04
pos = -110, 0, 0
rotate = 90, 0, 0
archetype = space_girderc

[Object]
nickname = rmbase05_girder05
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_girder

[Object]
nickname = rmbase05_girder06
pos = 0, 0, 600
rotate = 180, 0, 0
archetype = space_girdera

[Object]
nickname = rmbase05_girder07
pos = 0, 0, -600
rotate = 0, 0, 0
archetype = space_girdera

[Object]
nickname = rmbase05_ctrl_twr01
pos = 0, 100, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower

[Object]
nickname = rmbase05_ctrl_twr02
pos = 0, -100, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower

[Object]
nickname = rmbase05_ctrl_twr03
pos = 0, 280, 0
rotate = 180, 0, 0
archetype = space_medium_control_tower

[Object]
nickname = rmbase05_ctrl_twr04
pos = 0, -280, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower

[Object]
nickname = rmbase05_hab01
pos = 50, 190, 50
rotate = 0, 45, 0
archetype = space_habitat_wide

[Object]
nickname = rmbase05_hab02
pos = 50, 190, -50
rotate = 0, 45, 0
archetype = space_habitat_wide

[Object]
nickname = rmbase05_hab03
pos = -50, 190, 50
rotate = 0, 45, 0
archetype = space_habitat_wide

[Object]
nickname = rmbase05_hab04
pos = -50, 190, -50
rotate = 0, 45, 0
archetype = space_habitat_wide

[Object]
nickname = rmbase05_hab05
pos = 0, 190, 0
rotate = 0, 0, 0
archetype = space_habitat_wide

[Object]
nickname = rmbase05_hab06
pos = 50, -190, 50
rotate = 0, 45, 0
archetype = space_habitat_wide

[Object]
nickname = rmbase05_hab07
pos = 50, -190, -50
rotate = 0, 45, 0
archetype = space_habitat_wide

[Object]
nickname = rmbase05_hab08
pos = -50, -190, 50
rotate = 0, 45, 0
archetype = space_habitat_wide

[Object]
nickname = rmbase05_hab09
pos = -50, -190, -50
rotate = 0, 45, 0
archetype = space_habitat_wide

[Object]
nickname = rmbase05_hab10
pos = 0, -190, 0
rotate = 0, 0, 0
archetype = space_habitat_wide

[Object]
nickname = rmbase05_shipyard01
pos = 160, 0, 0
rotate = 0, 0, -90
archetype = shipyard_medium

[Object]
nickname = rmbase05_shipyard02
pos = -160, 0, 0
rotate = 0, 0, 90
archetype = shipyard_medium
    '''


class RmbaseNewGasminer(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rmbase08'
    TEMPLATE = '''
[Object]
nickname = rmbase08_ROOT
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_industrial01j

[Object]
nickname = rmbase08_door01
pos = 0, 9, 165
rotate = 0, 0, 0
archetype = space_circle_door

[Object]
nickname = rmbase08_door02
pos = 0, 9, 100
rotate = 0, 0, 0
archetype = space_circle_door

[Object]
nickname = rmbase08_door03
pos = 0, 9, -165
rotate = 0, 0, 0
archetype = space_circle_door

[Object]
nickname = rmbase08_door04
pos = 0, 9, -100
rotate = 0, 0, 0
archetype = space_circle_door

[Object]
nickname = rmbase08_miner01
pos = 0, 150, 0
rotate = 0, 0, 0
archetype = gas_miner_core

[Object]
nickname = rmbase08_tunnel01
pos = 0, 15, 132
rotate = 180, 0, 0
archetype = gas_miner_tunnel

[Object]
nickname = rmbase08_tunnel02
pos = 0, 15, -132
rotate = 0, 0, 180
archetype = gas_miner_tunnel

[Object]
nickname = rmbase08_panel01
pos = 0, 45, -125
rotate = 0, 0, 0
archetype = space_short_station_panel

[Object]
nickname = rmbase08_panel02
pos = 0, 45, 125
rotate = 0, 180, 0
archetype = space_short_station_panel

[Object]
nickname = rmbase08_control01
pos = 0, 280, 0
rotate = 0, 90, 0
archetype = space_pirate_control_block

[Object]
nickname = rmbase08_ind01
pos = 0, -75, 0
rotate = 0, 0, 0
archetype = space_industrial02d

[Object]
nickname = rmbase08_ind02
pos = 75, -25, 0.1
rotate = 0, 0, 60
archetype = space_industrial02d

[Object]
nickname = rmbase08_ind03
pos = -75, -25, -0.1
rotate = 0, 0, -60
archetype = space_industrial02d

[Object]
nickname = rmbase08_ind04
pos = -50, 50, 0.1
rotate = 0, 0, 10
archetype = space_industrial02d

[Object]
nickname = rmbase08_ind05
pos = 50, 50, -0.1
rotate = 0, 0, -10
archetype = space_industrial02d

[Object]
nickname = rmbase08_ring01
pos = 0, 0, 41
rotate = 0, 0, 0
archetype = small_ring

[Object]
nickname = rmbase08_ring02
pos = 0, 0, -41
rotate = 0, 0, 0
archetype = small_ring

[Object]
nickname = rmbase08_tank01
pos = 45, -95, 0
rotate = 0, 0, 0
archetype = space_tankl4

[Object]
nickname = rmbase08_tank02
pos = -45, -95, 0
rotate = 0, 0, 0
archetype = space_tankl4

[Object]
nickname = rmbase08_tank03
pos = 110, -40, 0
rotate = 0, 0, 0
archetype = space_tankl4

[Object]
nickname = rmbase08_tank04
pos = -110, -40, 0
rotate = 0, 0, 0
archetype = space_tankl4
    '''


class WeaponPlatformLargeGun(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'wplatform01'
    TEMPLATE = '''[Object]
nickname = wplatform01_ROOT
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_wplatform_core02

[Object]
nickname = wplatform01_pad01
pos = 90, -32, 0
rotate = 0, 0, 0
archetype = space_pad
loadout = rh_weapon_platform_one_turret
faction = rx_grp
reputation = rx_grp
behavior = NOTHING
difficulty_level = 5 ;12
pilot = pilot_solar_hardest

[Object]
nickname = wplatform01_pad02
pos = -90, -32, 0
rotate = 0, 180, 0
archetype = space_pad
loadout = rh_weapon_platform_one_turret
faction = rx_grp
reputation = rx_grp
behavior = NOTHING
difficulty_level = 5 ;12
pilot = pilot_solar_hardest

[Object]
nickname = wplatform01_pad03
pos = 0, -32, 90
rotate = 0, -90, 0
archetype = space_pad
loadout = rh_weapon_platform_one_turret
faction = rx_grp
reputation = rx_grp
behavior = NOTHING
difficulty_level = 5 ;12
pilot = pilot_solar_hardest

[Object]
nickname = wplatform01_pad04
pos = 0, -32, -90
rotate = 0, 90, 0
archetype = space_pad
loadout = rh_weapon_platform_one_turret
faction = rx_grp
reputation = rx_grp
behavior = NOTHING
difficulty_level = 5 ;12
pilot = pilot_solar_hardest

[Object]
nickname = wplatform01_pad05
pos = 0, -100, 0
rotate = -180, 0, 0
archetype = space_turret_pad
loadout = rh_weapon_platform_one_turret
faction = rx_grp
reputation = rx_grp
behavior = NOTHING
difficulty_level = 5 ;12
pilot = pilot_solar_hardest

[Object]
nickname = wplatform01_ctrl_twr01
pos = 0, 43, 0
rotate = 0, 0, 0
archetype = space_turret_pad

[Object]
nickname = wplatform01_ctrl_block01
pos = 0, 40, 0
rotate = 0, 0, 0
archetype = space_small_control_block

[Object]
nickname = wplatform01_shieldgen01
pos = 0, 20, 0
rotate = 0, 0, 0
archetype = space_shieldgen
loadout = rh_weapon_platform_many_turret
faction = rx_grp
reputation = rx_grp
behavior = NOTHING
difficulty_level = 5 ;12
pilot = pilot_solar_hardest
    '''


