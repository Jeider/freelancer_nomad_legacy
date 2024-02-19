from templates.space_object_template import SpaceObjectTemplate


class KyushuMegashipyard(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_ksu_02'
    TEMPLATE = '''[Object]
nickname = ku_ksu_02
pos = 0, 0, 0
rotate = 0, 45, 0
archetype = kyushu_core
{root_props}

[Object]
nickname = ku_ksu_02_dock
pos = 0, 850, 0
rotate = 0, 135, 0
archetype = space_freeport01
{dock_props}

;ROOT

[Object]
nickname = ku_ksu_02_ROOT_tanks01
pos = 0, -720, 0
rotate = 180, 135, 0
archetype = space_tanklx4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_ROOT_habitat01
pos = 0, -838, 0
rotate = 180, 45, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_ROOT_habitat02
pos = 0, -955, 0
rotate = 180, 45, 0
archetype = space_habitat_tall
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_ROOT_research01
pos = 0, 775, 0
rotate = 90, 45, 0
archetype = space_tube
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_ROOT_shipyard01
pos = 220, 0, -220
rotate = 90, -225, 0
archetype = shipyard_2x
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_ROOT_shipyard02
pos = -220, 0, 220
rotate = 90, -45, 0
archetype = shipyard_2x
parent = ku_ksu_02

;BLOCK A

[Object]
nickname = ku_ksu_02_A_control_tower01
pos = 0, 82, 0
rotate = 180, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_A_control_tower02
pos = 0, 0, 0
rotate = 180, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_A_control_tower03
pos = 0, -82, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_A_habitat_wide01
pos = 0, 0, -160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_A_habitat_wide02
pos = -160, 0, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_A_habitat_wide03
pos = 0, 0, 160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_A_habitat_wide04
pos = 160, 0, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

;BLOCK B

[Object]
nickname = ku_ksu_02_B_control_tower01
pos = 0, 250, 0
rotate = 180, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_control_tower02
pos = 0, 540, 0
rotate = 180, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_control_tower03
pos = 0, 628, 0
rotate = 180, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_control_tower04
pos = 0, 710, 0
rotate = 180, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_habitat_wide01
pos = 0, 628, -160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_habitat_wide02
pos = -160, 628, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_habitat_wide03
pos = 0, 628, 160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_habitat_wide04
pos = 160, 628, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_tanks01
pos = -160, 165, 0
rotate = 90, 90, 0
archetype = space_tanks4x4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_tanks02
pos = 140, 165, 0
rotate = 90, 90, 0
archetype = space_tanks4x4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_tanks03
pos = 0, 165, -160
rotate = 90, 0, 0
archetype = space_tanks4x4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_tanks04
pos = 0, 165, 120
rotate = 90, 0, 0
archetype = space_tanks4x4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_tanks05
pos = -160, 165, -41
rotate = 90, 0, 0
archetype = space_tanks4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_tanks06
pos = 140, 165, 41
rotate = 90, 180, 0
archetype = space_tanks4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_tanks07
pos = -41, 165, -160
rotate = 90, 90, 0
archetype = space_tanks4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_tanks08
pos = 41, 165, 120
rotate = 90, -90, 0
archetype = space_tanks4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_industrial01
pos = -140, 395, 0
rotate = 90, 45, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_industrial02
pos = 140, 395, 0
rotate = 90, 45, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_industrial03
pos = 0, 395, -140
rotate = 90, 45, 0
archetype = space_industrial02a
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_industrial04
pos = 0, 395, 140
rotate = 90, 45, 0
archetype = space_industrial02a
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_dome01
pos = -140, 730, 0
rotate = 0, 0, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_dome02
pos = 140, 730, 0
rotate = 0, 0, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_dome03
pos = 0, 730, -140
rotate = 0, 90, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_dome04
pos = 0, 730, 140
rotate = 0, 90, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_dome05
pos = -100, 730, -100
rotate = 0, -45, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_dome06
pos = 100, 730, -100
rotate = 0, 45, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_dome07
pos = 100, 730, 100
rotate = 0, -45, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_dome08
pos = -100, 730, 100
rotate = 0, 45, 0
archetype = space_domeb
parent = ku_ksu_02

;BLOCK C

[Object]
nickname = ku_ksu_02_C_control_tower01
pos = 0, -250, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_control_tower02
pos = 0, -540, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_control_tower03
pos = 0, -628, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_control_tower04
pos = 0, -710, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_habitat_wide01
pos = 0, -628, -160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_habitat_wide02
pos = -160, -628, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_habitat_wide03
pos = 0, -628, 160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_habitat_wide04
pos = 160, -628, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_tanks01
pos = -160, -165, 0
rotate = 90, 90, 0
archetype = space_tanks4x4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_tanks02
pos = 140, -165, 0
rotate = 90, 90, 0
archetype = space_tanks4x4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_tanks03
pos = 0, -165, -160
rotate = 90, 0, 0
archetype = space_tanks4x4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_tanks04
pos = 0, -165, 120
rotate = 90, 0, 0
archetype = space_tanks4x4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_tanks05
pos = -160, -165, -41
rotate = 90, 0, 0
archetype = space_tanks4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_tanks06
pos = 140, -165, 41
rotate = 90, 180, 0
archetype = space_tanks4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_tanks07
pos = -41, -165, -160
rotate = 90, 90, 0
archetype = space_tanks4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_tanks08
pos = 41, -165, 120
rotate = 90, -90, 0
archetype = space_tanks4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_industrial01
pos = -140, -395, 0
rotate = 90, 45, 0
archetype = space_industrial02a
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_industrial02
pos = 140, -395, 0
rotate = 90, 45, 0
archetype = space_industrial02a
loadout = space_ind01_reactor
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_industrial03
pos = 0, -395, -140
rotate = 90, 45, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_industrial04
pos = 0, -395, 140
rotate = 90, 45, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_dome01
pos = -140, -730, 0
rotate = 180, 0, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_dome02
pos = 140, -730, 0
rotate = 180, 0, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_dome03
pos = 0, -730, -140
rotate = 180, 90, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_dome04
pos = 0, -730, 140
rotate = 180, 90, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_dome05
pos = -100, -730, -100
rotate = 180, -45, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_dome06
pos = 100, -730, -100
rotate = 180, 45, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_dome07
pos = 100, -730, 100
rotate = 180, -45, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_dome08
pos = -100, -730, 100
rotate = 180, 45, 0
archetype = space_domeb
parent = ku_ksu_02
'''
