from templates.space_object_template import SpaceObjectTemplate


class TekagiDebris(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_tgk_06'
    TEMPLATE = '''[Object]
nickname = ku_tgk_06_space_arch_chunk1a_2
pos = 0, -400, -500
rotate = 0, -70, 0
archetype = space_arch_chunk1a

[Object]
nickname = ku_tgk_06
pos = 0, 0, 0
rotate = 90, 0, 0
archetype = space_industrial01_station_root
{root_props}

[Object]
nickname = ku_tgk_06_SHIELDGEN_gird01
pos = 0, 360, -60
rotate = 45, 0, 0
archetype = space_girderb
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_SHIELDGEN_gird02
pos = 0, 460, -60
rotate = -45, 0, 0
archetype = space_girderb
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_SHIELDGEN_gird03
pos = 0, 360, 60
rotate = -45, 0, 0
archetype = space_girderb
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_SHIELDGEN_gird04
pos = 0, 460, 60
rotate = 45, 0, 0
archetype = space_girderb
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_SHIELDGEN_gird05
pos = 60, 360, 0
rotate = -45, 90, 0
archetype = space_girderb
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_SHIELDGEN_gird06
pos = 60, 460, 0
rotate = 45, 90, 0
archetype = space_girderb
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_SHIELDGEN_gird07
pos = -60, 360, 0
rotate = 45, 90, 0
archetype = space_girderb
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_SHIELDGEN_gird08
pos = -60, 460, 0
rotate = 45, -90, 0
archetype = space_girderb
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_SHIELDGEN_ring01
pos = 0, 410, 0
rotate = 90, 0, 0
archetype = small_ring
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_SHIELDGEN_ring02
pos = 0, 460, 0
rotate = 90, 0, 0
archetype = smallest_ring
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_SHIELDGEN_ring03
pos = 0, 360, 0
rotate = 90, 0, 0
archetype = smallest_ring
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_REACTOR_ind01
pos = 0, 0, 175
rotate = 90, 0, 0
archetype = space_industrial01
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_REACTOR_ind02
pos = 0, 0, -175
rotate = 90, 0, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_REACTOR_ind03
pos = 100, 0, -100
rotate = 90, 45, 0
archetype = space_industrial01
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_REACTOR_ind04
pos = 175, 0, 0
rotate = 90, 0, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_REACTOR_ind05
pos = -100, 0, -100
rotate = 90, 45, 0
archetype = space_industrial01
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_REACTOR_ind06
pos = -175, 0, 0
rotate = 90, 0, 0
archetype = space_industrial01
loadout = space_ind01_reactor
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_REACTOR_ind07
pos = -100, 0, 100
rotate = 90, 45, 0
archetype = space_industrial01
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_REACTOR_ind08
pos = 100, 0, 100
rotate = 90, 45, 0
archetype = space_industrial01
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_REACTOR_ind08
pos = 0, 210, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_REACTOR_twr01
pos = 0, 130, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_PRODUCTION_tube01
pos = 0, 175, -300
rotate = 11, 180, 0
archetype = space_short_tube
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_PRODUCTION_ind01
pos = 0, 175, -180
rotate = 0, 0, 0
archetype = space_industrial02a
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_PRODUCTION_ind02
pos = 0, -100, -1052
rotate = 90, 0, 0
archetype = space_industrial01a
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_PRODUCTION_ind03
pos = -231, -310, -768
rotate = -90, -30, 0
archetype = space_industrialc
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_PRODUCTION_tanks01
pos = 360, -170, -1052
rotate = 185, 90, 0
archetype = space_tankl4
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_PRODUCTION_tanks02
pos = 490, -215, -920
rotate = 195, 90, 0
archetype = space_tankl4
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_PRODUCTION_factory01
pos = -90, -250, -768
rotate = 0, -90, 0
archetype = space_production
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_PRODUCTION_factory02
pos = -380, -280, -760
rotate = 0, 90, 0
archetype = space_production
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_PRODUCTION_girder01
pos = 150, -130, -1052
rotate = 20, 90, 0
archetype = space_girderc
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_PRODUCTION_girder02
pos = 300, -170, -985
rotate = 5, 45, 0
archetype = space_girderc
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_PRODUCTION_girder03
pos = -65, -100, -1056
rotate = 15, -30, 0
archetype = space_girdera
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_HILL_tube01
pos = -250, 210, 0
rotate = 30, -90, 0
archetype = space_short_tube
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_HILL_ind01
pos = -180, 175, 0
rotate = 0, 90, 0
archetype = space_industrial02a
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_HILL_ind02
pos = -910, -290, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_HILL_ind03
pos = -910, -240, 400
rotate = 90, 0, 0
archetype = space_industrial_dmg
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_HILL_ind04
pos = -910, -240, -400
rotate = 90, 0, 0
archetype = space_industriala
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_HILL_twr02
pos = -910, 40, 0
rotate = 10, 0, 10
archetype = space_medium_Control_tower
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_HILL_twr01
pos = -910, -160, 0
rotate = 0, 0, 0
archetype = space_medium_Control_tower
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_HILL_habitat01
pos = -910, -50, -60
rotate = 0, 0, 0
archetype = space_habitat_dmg
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_HILL_habitat02
pos = -910, -50, 70
rotate = 170, 0, 0
archetype = space_habitat_dmg
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_HILL_habitat03
pos = -970, -50, 0
rotate = 0, 0, -20
archetype = space_habitat_dmg
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_HILL_habitat04
pos = -850, -80, -20
rotate = 200, 0, 0
archetype = space_habitat_dmg
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_HILL_habitat05
pos = -920, 100, 10
rotate = 10, 0, 10
archetype = space_habitat_dmg
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_HILL_girder01
pos = -910, -300, 0
rotate = -10, 0, 0
archetype = space_girdera
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_HILL_girder02
pos = -910, -300, 0
rotate = -10, 180, 0
archetype = space_girdera
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_HILL_girder03
pos = -910, -100, -400
rotate = -90, 0, 0
archetype = space_beaml_dmg
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_HILL_dock01
pos = -905, 0, 405
rotate = 10, 90, 0
archetype = space_police_dmg
parent = ku_tgk_06

[Object]
nickname = ku_tgk_06_HILL_dock02
pos = -910, 50, -415
rotate = 95, 80, 95
archetype = space_police_dmg
parent = ku_tgk_06
'''


class MunchenBattleStationDebris(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_mnh_05'
    TEMPLATE = '''[Object]
nickname = rh_mnh_05
pos = 0, 0, 0
rotate = -90, 45, 5
archetype = space_industrial_dmg_root
{root_props}

[Object]
nickname = rh_mnh_05_dockA
pos = -10, -5, -270
rotate = 0, 0, -10
archetype = munchen_dmg01
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_dockB
pos = -40, 2, 220
rotate = 0, -195, 0
archetype = munchen_dmg02
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_docklock01
pos = -125, 0, -150
rotate = 0, 160, 0
archetype = space_industrial01c
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_docklock02
pos = 105, -25, -150
rotate = 10, 180, 5
archetype = space_industrial01c
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_docklock03
pos = -67, 0, -150
rotate = 5, 180, 0
archetype = space_industrial01c
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_docklock06
pos = 105, -15, 150
rotate = 20, 0, -10
archetype = space_industrial01c
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_docklock08
pos = 48, -10, 150
rotate = 10, 0, 0
archetype = space_industrial01c
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_COREgird01
pos = 50, 0, -70
rotate = -15, -40, 0
archetype = space_girderc
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_COREgird02
pos = -10, 0, 0
rotate = 5, 40, 5
archetype = space_girder
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_COREgird04
pos = -10, 0, 0
rotate = 0, 23, -5
archetype = space_girder
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_ringIN01
pos = -280, 20, -30
rotate = 60, 34,20
archetype = smallest_ring
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_ringIN02
pos = -150, -70, 0
rotate = 70, 35, -5
archetype = smallest_ring
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_ringIN04
pos = 230, 0, 20
rotate = 60, 25, 60
archetype = smallest_ring
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_ringIN05
pos = 160, 0, 7
rotate = 75, 35, 75
archetype = smallest_ring
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_ringIN06
pos = 95, 0, 0
rotate = 80, 40, 80
archetype = smallest_ring
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_NRGgird01
pos = -110, 60, 0
rotate = 10, 90, 0
archetype = space_beaml_dmg
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_NRGgird01a
pos = 90, 60, 0
rotate = 0, 80, 0
archetype = space_girderc
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_NRGgird02a
pos = 90, -70, 0
rotate = -10, -90, 0
archetype = space_beaml_dmg
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_NRGgird03
pos = -10, 130, -60
rotate = 35, 0, 0
archetype = space_girderb
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_NRGgird05
pos = -10, 110, 60
rotate = -10, 0, 0
archetype = space_girderb
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_NRGgird07
pos = 50, 130, 0
rotate = -30, 90, 0
archetype = space_girderb
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_NRGgird09
pos = -70, 120, 0
rotate = 30, 90, 0
archetype = space_girderb
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_NRGgird11
pos = -10, -245, -65
rotate = 55, 0, 0
archetype = space_girderb
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_NRGgird12
pos = -10, -150, -45
rotate = -35, 0, 0
archetype = space_girderb
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_NRGgird13
pos = -10, -260, 50
rotate = -40, 0, 0
archetype = space_girderb
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_NRGgird14
pos = -10, -150, 65
rotate = 55, 0, 0
archetype = space_girderb
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_NRGgird15
pos = 35, -260, 0
rotate = -35, 90, 0
archetype = space_girderb
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_NRGgird16
pos = 45, -150, 0
rotate = 60, 90, 0
archetype = space_girderb
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_NRGgird17
pos = -70, -240, 0
rotate = 50, 90, 0
archetype = space_girderb
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_NRGgird18
pos = -50, -140, 0
rotate = 35, -90, 0
archetype = space_girderb
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_ringOUT03
pos = 0, 120, 0
rotate = 100, 10, 20
archetype = smallest_ring
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_ringOUT04
pos = -10, -150, 0
rotate = 80, 0, 0
archetype = smallest_ring
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_ringOUT05
pos = -10, -200, 0
rotate = 95, 0, -10
archetype = small_ring
parent = rh_mnh_05

[Object]
nickname = rh_mnh_05_ringOUT06
pos = -10, -250, 0
rotate = 90, 0, -10
archetype = smallest_ring
parent = rh_mnh_05
'''


class MunchenCivilianStationDebris(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_mnh_06'
    TEMPLATE = '''[Object]
nickname = rh_mnh_06
pos = 0, 0, 0
rotate = 90, 0, 0
archetype = space_industrial01a_station_root
{root_props}

[Object]
nickname = rh_mnh_06_industrial01
pos = 0, 245, -300
rotate = -2, 0, 0
archetype = space_industriala
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_industrial02
pos = 0, 245, 300
rotate = -5, 0, 0
archetype = space_industriala
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_industrial03
pos = -10, -245, -300
rotate = -3, 2, 0
archetype = space_industriala
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_industrial04
pos = 0, -245, 300
rotate = -3, 0, 0
archetype = space_industriala
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_industrial05
pos = 440, 0, 0
rotate = 0, 90, 0
archetype = space_industrial02a
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_industrial06
pos = 440, 0, -150
rotate = 0, 90, 0
archetype = space_industrial02a
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_industrial07
pos = 440, 0, -300
rotate = 0, 90, 0
archetype = space_industrial02a
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_industrial08
pos = 440, 0, 150
rotate = 0, 90, 0
archetype = space_industrial02a
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_industrial09
pos = 440, 0, 300
rotate = 0, 90, 0
archetype = space_industrial02a
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_industrial10
pos = -440, 0, 0
rotate = 0, 90, 0
archetype = space_industrial02a
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_industrial11
pos = -440, 0, -150
rotate = 0, 90, 0
archetype = space_industrial02a
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_industrial12
pos = -440, 0, -300
rotate = 0, 90, 0
archetype = space_industrial02a
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_industrial13
pos = -440, 0, 150
rotate = 0, 90, 0
archetype = space_industrial02a
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_industrial14
pos = -440, 0, 300
rotate = 0, 90, 0
archetype = space_industrial02a
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_industrial15
pos = 0, 245, 0
rotate = 0, 0, 0
archetype = space_industrial_dmg
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_industrial16
pos = 0, -245, 0
rotate = 0, 0, 0
archetype = space_industrial_dmg
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_industrial17
pos = 0, 0, -300
rotate = 90, 0, 0
archetype = space_industrial01a
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_industrial18
pos = 0, 0, 300
rotate = 90, 0, 0
archetype = space_industrial01a
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_girder01
pos = 60, 245, -300
rotate = 45, 90, 0
archetype = space_girdera
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_girder02
pos = -60, 245, -300
rotate = 45, -90, 0
archetype = space_girdera
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_girder03
pos = 60, -245, -300
rotate = -45, 90, 0
archetype = space_girdera
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_girder04
pos = -60, -245, -300
rotate = -45, -90, 0
archetype = space_girdera
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_girder05
pos = 60, 245, 300
rotate = 45, 90, 0
archetype = space_girdera
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_girder06
pos = -60, 245, 300
rotate = 45, -90, 0
archetype = space_girdera
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_girder07
pos = 60, -245, 300
rotate = -45, 90, 0
archetype = space_girdera
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_girder08
pos = -60, -245, 300
rotate = -45, -90, 0
archetype = space_girdera
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_girder09
pos = 0, 0, 0
rotate = 90,  0, 0
archetype = space_girder
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_girder10
pos = 0, 0, -300
rotate = 90,  0, 0
archetype = space_girder
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_girder11
pos = 0, 0, 300
rotate = 90,  0, 0
archetype = space_girder
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_girder12
pos = 0, 375, 0
rotate = 90, 0, 0
archetype = space_girderc
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_girder13
pos = 0, -350, 0
rotate = 90, 0, 0
archetype = space_girderc
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_shipyard01
pos = 440, 150, 0
rotate = 0, 0, 0
archetype = shipyard_dmgA
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_shipyard02
pos = 440, -200, 0
rotate = -30, -10, 180
archetype = shipyard_dmgB
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_shipyard03
pos = -460, 150, 0
rotate = 0, 180, 0
archetype = shipyard_dmgA
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_shipyard04
pos = -460, -150, 0
rotate = 0, 180, 180
archetype = shipyard_dmgA
parent = rh_mnh_06

[Object]
nickname = rh_mnh_06_tunnel01
pos = 0, -500, 0
rotate = 0, 0, 0
archetype = space_tunnel
parent = rh_mnh_06
'''


class OmegaDanzigDebris(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'om15_02'
    TEMPLATE = '''[Object]
nickname = om15_02
pos = 0, 0, 0
rotate = 7, 3, -5
archetype = space_control_tower_root
{root_props}

[Object]
nickname = om15_02_bottom
pos = 0, 90, 0
rotate = -5, 0, -10
archetype = space_control_tower
parent = om15_02

[Object]
nickname = om15_02_middle
pos = 0, -80, -820
rotate = 0, 0, 0
archetype = space_tube_fix
parent = om15_02

[Object]
nickname = om15_02_middle_ind01
pos = 0, -80, 750
rotate = 0, 0, 0
archetype = space_industrial01d
parent = om15_02

[Object]
nickname = om15_02_bottom_beamx01
pos = 0, -230, 0
rotate = 0, 0, 0
archetype = space_beamx_dmg
parent = om15_02

[Object]
nickname = om15_02_beaml01
pos = 0, 70, 0
rotate = 90, 180, 5
archetype = space_beaml_dmg
parent = om15_02

[Object]
nickname = om15_02_beaml02
pos = 200, -80, 900
rotate = 0, 90, 0
archetype = space_beaml_dmg
parent = om15_02

[Object]
nickname = om15_02_beaml03
pos = -195, -80, 900
rotate = 180, -90, 12
archetype = space_beaml_dmg
parent = om15_02

[Object]
nickname = om15_02_shipyard01
pos = 0, -210, -900
rotate = 12, 102, 200
archetype = shipyard
parent = om15_02

[Object]
nickname = om15_02_shipyard02
pos = 0, -210, 900
rotate = -20, 80, 170
archetype = shipyard
parent = om15_02

[Object]
nickname = om15_02_cruiser_debris01
pos = -200, -280, -900
rotate = 0, 50, 0
archetype = rh_cruiser_debris
parent = om15_02

[Object]
nickname = om15_02_cruiser_debris02
pos = -400, -280, 0
rotate = 0, 50, 30
archetype = rh_cruiser_debris
parent = om15_02

[Object]
nickname = om15_02_miner_debris01
pos = 355, -150, 775
rotate = 0, 30, 0
archetype = mining_debris_satellite_non_targetable
parent = om15_02

[Object]
nickname = om15_02_industrial_dmg01
pos = 0, -80, 0
rotate = 0, 90, 0
archetype = space_industrial_dmg
parent = om15_02

[Object]
nickname = om15_02_industrial_dmg02
pos = 0, -80, -150
rotate = 15, -90, 0
archetype = space_industrial_dmg
parent = om15_02

[Object]
nickname = om15_02_industrial_dmg03
pos = 0, 220, 0
rotate = 0, 10, 0
archetype = space_industrial_dmg
parent = om15_02

[Object]
nickname = om15_02_dmg_tanks01
pos = -190, -35, -900
rotate = 0, -90, -20
archetype = space_tankl4_dmg
parent = om15_02

[Object]
nickname = om15_02_dmg_tanks02
pos = 0, -280, 0
rotate = -20, 0, 0
archetype = space_tankl4_dmg
parent = om15_02

[Object]
nickname = om15_02_dmg_tanks03
pos = 200, -30, -900
rotate = 90, 0, 98
archetype = space_tankl4x4_dmg
parent = om15_02

[Object]
nickname = om15_02_dmg_tanks04
pos = 500, -80, 0
rotate = 50, 30, 0
archetype = space_tankl4x4_dmg
parent = om15_02

[Object]
nickname = om15_02_dmg_tanks05
pos = 0, -230, -230
rotate = 40, 0, -10
archetype = space_tanklx4_dmg
parent = om15_02

[Object]
nickname = om15_02_dmg_habitat01
pos = 0, 69, 150
rotate = 180, 180, 0
archetype = space_habitat_dmg
parent = om15_02

[Object]
nickname = om15_02_dmg_habitat02
pos = -140, 140, 0
rotate = 0, 0, 0
archetype = space_habitat_dmg
parent = om15_02

[Object]
nickname = om15_02_dmg_habitat03
pos = 150, 140, -50
rotate = 180, 30, -15
archetype = space_habitat_dmg
parent = om15_02

[Object]
nickname = om15_02_dmg_dock01
pos = 200, -71, -400
rotate = 10, 45, -20
archetype = space_police_dmg
parent = om15_02

[Object]
nickname = om15_02_dmg_dock02
pos = -500, -130, 0
rotate = 0, 15, 30
archetype = space_police_dmg
parent = om15_02

[Object]
nickname = om15_02_dmg_dock03
pos = -295, 103, 6
rotate = -10, 180, -5
archetype = space_police_dmg
parent = om15_02

[Object]
nickname = om15_02_dmg_dock04
pos = -300, -71, 0
rotate = 0, 180, 0
archetype = space_police_dmg
parent = om15_02

[Object]
nickname = om15_02_tunnel01
pos = 0, -80, -900
rotate = 0, 0, 0
archetype = space_tunnel
parent = om15_02

[Object]
nickname = om15_02_tunnel02
pos = 0, -80, 900
rotate = 0, 180, 0
archetype = space_tunnel
parent = om15_02
'''


class StuttgartDestroyedOutpost(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_stut_07'
    TEMPLATE = '''[Object]
nickname = rh_stut_07
pos = 0, 0, 0
rotate = 30, 0, 0
archetype = space_police_dmg_visible
{root_props}

[Object]
nickname = rh_stut_07_industrial01
pos = 0, -400, -40
rotate = 80, 0, 0
archetype = space_industrial02a
parent = rh_stut_07

[Object]
nickname = rh_stut_07_industrial02
pos = 240, -400, 10
rotate = 80, -20, 0
archetype = space_industrial02a
parent = rh_stut_07

[Object]
nickname = rh_stut_07_industrial03
pos = -207, -390, -60
rotate = 90, 15, 15
archetype = space_industrial02a
parent = rh_stut_07

[Object]
nickname = rh_stut_07_girder01
pos = 250, -270, -10
rotate = -45, -90, 0
archetype = space_girdera
parent = rh_stut_07

[Object]
nickname = rh_stut_07_girder02
pos = -250, -270, -60
rotate = -45, 80, 0
archetype = space_girdera
parent = rh_stut_07

[Object]
nickname = rh_stut_07_girder03
pos = 0, -200, -40
rotate = 100, 0, 0
archetype = space_girder
parent = rh_stut_07
'''


class ForbesDebris(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_for_07'
    TEMPLATE = '''[Object]
nickname = li_for_07
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_police_dmg_visible
{root_props}

[Object]
nickname = li_for_07_beam01
pos = 0, -165, 0
rotate = 0, 0, 0
archetype = space_beamx_dmg
parent = li_for_07

[Object]
nickname = li_for_07_industrial01
pos = -165, -112, 0
rotate = 0, 90, -10
archetype = space_industrial01d
parent = li_for_07

[Object]
nickname = li_for_07_industrial02
pos = 200, -180, 0
rotate = -80, 60, -100
archetype = space_industrial01d
parent = li_for_07

[Object]
nickname = li_for_07_industrial03
pos = 0, -112, -170
rotate = 10, 0, 0
archetype = space_industrial01d
parent = li_for_07

[Object]
nickname = li_for_07_industrial04
pos = 0, -135, 150
rotate = 2, 0, 15
archetype = space_industrial01d
parent = li_for_07

[Object]
nickname = li_for_07_shipyard01
pos = 0, -250, -200
rotate = 30, 60, 30
archetype = shipyard_dmgB
parent = li_for_07

[Object]
nickname = li_for_07_shipyard02
pos = 100, -250, 300
rotate = 30, -60, -30
archetype = shipyard_dmgB
parent = li_for_07
'''


class ColumbiaDebris(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_col_05'
    TEMPLATE = '''[Object]
nickname = li_col_05
pos = 0, 0, 0
rotate = 0, -90, 0
archetype = space_police_dmg_clickable
{root_props}

[Object]
nickname = li_col_05_industrial_A01
pos = 187.5, 105, -1035
rotate = 0, 1, 45
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A02
pos = 62.5, 105, -1035
rotate = 0, 0, 45.5
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A03
pos = -62.5, 105, -1035
rotate = 0, 0, 45.5
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A04
pos = -187.5, 105, -1035
rotate = 0, 0, 45.34
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A05
pos = 125, 0, -1035
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A06
pos = 0, 0, -1035
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A07
pos = -125, 0, -1035
rotate = 0, 0.5, 0
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A08
pos = 187.5, -105, -1035
rotate = 0, -0.6, 45
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A09
pos = 62.5, -105, -1035
rotate = 0, 0, 45
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A10
pos = -62.5, -105, -1035
rotate = 0, 0.2, 45
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A11
pos = -187.5, -105, -1035
rotate = 0.2, 0.134, 45
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_B01
pos = 0, 0, -685
rotate = 0, 90, 0
archetype = space_industrial02a
parent = li_col_05

[Object]
nickname = li_col_05_industrial_B02
pos = 0, 0, -535
rotate = 0, 90, 0
archetype = space_industrial02a
parent = li_col_05

[Object]
nickname = li_col_05_industrial_B03
pos = 85, 0, -610
rotate = 0, 1, 0
archetype = space_industrial01a
parent = li_col_05

[Object]
nickname = li_col_05_industrial_B04
pos = -88, 0, -610
rotate = -2, 0, 0
archetype = space_industrial01a
parent = li_col_05

[Object]
nickname = li_col_05_industrial_B05
pos = 0, 0, -145
rotate = 1, 90, 0
archetype = space_industrial02a
parent = li_col_05

[Object]
nickname = li_col_05_girder_A01
pos = 62.5, 105, -915
rotate = 20, -10, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_A02
pos = -62.5, 105, -915
rotate = 20, 10, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_A03
pos = -187.5, 105, -915
rotate = 20, 35, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_A04
pos = 187.5, 105, -915
rotate = 20, -35, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_A05
pos = 62.5, -105, -915
rotate = -20, -10, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_A06
pos = -62.5, -105, -915
rotate = -20, 10, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_A07
pos = -187.5, -105, -915
rotate = -20, 35, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_A08
pos = 187.5, -105, -915
rotate = -20, -35, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_A09
pos = 125, 0, -915
rotate = 0, -20, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_A10
pos = 0, 0, -915
rotate = 0, 0, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_A11
pos = -125, 0, -915
rotate = 0, 20, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A01
pos = 55.5, -32, -405
rotate = -2, 0, -45
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A02
pos = 55.5, 26, -405
rotate = 0, 0, -135
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A03
pos = -59.5, -32, -405
rotate = 0, 2, 45
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A04
pos = -59.5, 26, -405
rotate = 0, 0, 135
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A05
pos = 55.5, -32, -265
rotate = 0, 0, -45
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A06
pos = 55.5, 26, -265
rotate = 5, 0, -135
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A07
pos = -59.5, -32, -265
rotate = 0, 0, 45
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A08
pos = -59.5, 26, -265
rotate = 1, 0, 135
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A09
pos = 0, -41, -405
rotate = 3, 0, 0
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A10
pos = 0, 41, -405
rotate = 0, 0, 180
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A11
pos = 0, -41, -265
rotate = 0, 0, 0
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A12
pos = 0, 41, -265
rotate = 5, 2, 180
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_habitat01
pos = 0, 65, -610
rotate = 0, 0, 0
archetype = space_habitat_dmg
parent = li_col_05
'''


class CaliforniaDebris(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_cal_10'
    TEMPLATE = '''[Object]
nickname = li_cal_10
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_industriala_base_root
{root_props}

[Object]
nickname = li_cal_10_ctrl_twr01
pos = 0, 80, 0
rotate = 0, 0, 5
archetype = space_medium_control_tower
parent = li_cal_10

[Object]
nickname = li_cal_10_ctrl_twr02
pos = 0, 110, 0
rotate = 0, 0, 10
archetype = space_control_tower
parent = li_cal_10

[Object]
nickname = li_cal_10_ctrl_twr03
pos = 0, 275, 0
rotate = 0, 0, 10
archetype = space_small_control_tower
parent = li_cal_10

[Object]
nickname = li_cal_10_industrial01
pos = 0, 0, -220
rotate = 0, 0, 0
archetype = space_industriala
parent = li_cal_10

[Object]
nickname = li_cal_10_industrial02
pos = 0, 0, 220
rotate = 0, 0, 0
archetype = space_industriala
parent = li_cal_10

[Object]
nickname = li_cal_10_industrial03
pos = -125, 0, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = li_cal_10

[Object]
nickname = li_cal_10_industrial04
pos = 180, 0, -20
rotate = 0, 30, 0
archetype = space_industrial_dmg
parent = li_cal_10

[Object]
nickname = li_cal_10_industrial05
pos = 0, -150, 0
rotate = -10, 0, 0
archetype = space_industriala
parent = li_cal_10

[Object]
nickname = li_cal_10_tunnel01
pos = 0, 0, -423
rotate = 0, 0, 0
archetype = space_tunnel
parent = li_cal_10

[Object]
nickname = li_cal_10_tunnel02
pos = 0, 0, 420
rotate = 0, 180, 0
archetype = space_tunnel
parent = li_cal_10

[Object]
nickname = li_cal_10_girder01
pos = 0, 200, -120
rotate = -55, 0, 0
archetype = space_girderc
parent = li_cal_10

[Object]
nickname = li_cal_10_girder02
pos = 0, 200, 120
rotate = 55, 0, 0
archetype = space_girderc
parent = li_cal_10

[Object]
nickname = li_cal_10_girder03
pos = -120, 200, 0
rotate = 140, 90, 0
archetype = space_beaml_dmg
parent = li_cal_10

[Object]
nickname = li_cal_10_girder04
pos = 120, 210, 0
rotate = 55, 90, 0
archetype = space_girderc
parent = li_cal_10

[Object]
nickname = li_cal_10_girder05
pos = 0, 200, 0
rotate = 90, 0, 0
archetype = space_girderc
parent = li_cal_10

[Object]
nickname = li_cal_10_girder07
pos = 0, -90, 172
rotate = -35, 0, 0
archetype = space_girderc
parent = li_cal_10

[Object]
nickname = li_cal_10_girder08
pos = -90, 0, -172
rotate = 0, -35, 0
archetype = space_girderc
parent = li_cal_10

[Object]
nickname = li_cal_10_girder10
pos = -90, 0, 172
rotate = 0, 35, 0
archetype = space_girderc
parent = li_cal_10

[Object]
nickname = li_cal_10_habitat01
pos = 0, 360, 0
rotate = 180, 0, 0
archetype = space_habitat_dmg
parent = li_cal_10

[Object]
nickname = li_cal_10_shipyard01
pos = -600, -50, 0
rotate = 0, 30, 0
archetype = shipyard_dmgA
parent = li_cal_10

[Object]
nickname = li_cal_10_shipyard02
pos = 300, -250, -300
rotate = -30, 0, 0
archetype = shipyard_dmgB
parent = li_cal_10

[Object]
nickname = li_cal_10_mining01
pos = 300, 100, 500
rotate = -20, 60, 0
archetype = mining_debris_satellite_non_targetable
parent = li_cal_10

[Object]
nickname = li_cal_10_control_panel01
pos = 0, 55, 485
rotate = 0, 0, 90
archetype = space_control_panel
parent = li_cal_10

[Object]
nickname = li_cal_10_control_panel02
pos = -55, 0, 500
rotate = 0, 180, 0
archetype = space_control_panel
parent = li_cal_10

[Object]
nickname = li_cal_10_control_panel03
pos = 0, 55, -490
rotate = 0, 0, 90
archetype = space_control_panel
parent = li_cal_10

[Object]
nickname = li_cal_10_control_panel04
pos = 55, 0, -505
rotate = 0, 0, 0
archetype = space_control_panel
parent = li_cal_10
'''


class SigmaEightFreeport(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'sig8_03'
    LOCKED_OBJECT_OFFSET = (100, 13, 60)
    TEMPLATE = '''[Object]
nickname = sig8_03
pos = -250, -25, 60
rotate = 0, 0, 0
archetype = space_industrial_dmg_root
reputation = fc_uk_grp
behavior = NOTHING

[Object]
nickname = sig8_03_space_dome_dmg01
pos = -600, -29, 60
rotate = 0, 0, 0
archetype = space_dome_dmg2
parent = sig8_03

[Object]
nickname = sig8_03_space_solar_panel_dmg01
pos = -250, -45, 60
rotate = 0, 90, 0
archetype = space_panel_damaged_01
parent = sig8_03

[Object]
nickname = sig8_03_space_tanks01
pos = -250, -185, 60
rotate = 0, 0, 0
archetype = space_tanklx4_dmg
parent = sig8_03

[Object]
nickname = sig8_03_space_beam_dmg01
pos = -55, -25, 60
rotate = 0, 90, 0
archetype = space_beaml_dmg
parent = sig8_03

[Object]
nickname = sig8_03_space_habitat_dmg01
pos = -80, -35, 160
rotate = -200, 90, 30
archetype = space_habitat_dmg
parent = sig8_03

[Object]
nickname = sig8_03_tunnel01
pos = -250, -35, 360
rotate = 0, -90, 0
archetype = space_tunnel
parent = sig8_03

[Object]
nickname = sig8_03_tunnel02
pos = -251, -18, -236
rotate = 0, 90, 0
archetype = space_tunnel
parent = sig8_03
'''