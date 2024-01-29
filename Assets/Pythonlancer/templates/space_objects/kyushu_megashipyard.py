from templates.space_object_template import SpaceObjectTemplate


class KyushuMegashipyard(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_ksu_02'
    TEMPLATE = '''[Object]
nickname = ku_ksu_02
ids_name = 203745
pos = -30000, -8000, -25000
rotate = 0, 45, 0
archetype = kyushu_core
ids_info = 065660
base = ku_ksu_02_base
reputation = ku_grp
behavior = NOTHING

[Object]
nickname = ku_ksu_02_dock
pos = -30000, -7150, -25000
rotate = 0, 135, 0
archetype = space_freeport01
dock_with = ku_ksu_02_base
base = ku_ksu_02_base
reputation = ku_grp
behavior = NOTHING
voice = atc_leg_f01
space_costume = ku_kym_head_gen, ku_female_guard_body, prop_hat_female_ku_grd_visor
difficulty_level = 10
pilot = pilot_solar_hardest
visit = 16
ids_name = 196722
ids_info = 065739

;ROOT

[Object]
nickname = ku_ksu_02_ROOT_tanks01
pos = -30000, -8720, -25000
rotate = 180, 135, 0
archetype = space_tanklx4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_ROOT_habitat01
pos = -30000, -8838, -25000
rotate = 180, 45, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_ROOT_habitat02
pos = -30000, -8955, -25000
rotate = 180, 45, 0
archetype = space_habitat_tall
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_ROOT_research01
pos = -30000, -7225, -25000
rotate = 90, 45, 0
archetype = space_tube
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_ROOT_shipyard01
pos = -29780, -8000, -25220
rotate = 90, -225, 0
archetype = shipyard_2x
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_ROOT_shipyard02
pos = -30220, -8000, -24780
rotate = 90, -45, 0
archetype = shipyard_2x
parent = ku_ksu_02

;BLOCK A

[Object]
nickname = ku_ksu_02_A_control_tower01
pos = -30000, -7918, -25000
rotate = 180, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_A_control_tower02
pos = -30000, -8000, -25000
rotate = 180, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_A_control_tower03
pos = -30000, -8082, -25000
rotate = 0, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_A_habitat_wide01
pos = -30000, -8000, -25160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_A_habitat_wide02
pos = -30160, -8000, -25000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_A_habitat_wide03
pos = -30000, -8000, -24840
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_A_habitat_wide04
pos = -29840, -8000, -25000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

;BLOCK B

[Object]
nickname = ku_ksu_02_B_control_tower01
pos = -30000, -7750, -25000
rotate = 180, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_control_tower02
pos = -30000, -7460, -25000
rotate = 180, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_control_tower03
pos = -30000, -7372, -25000
rotate = 180, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_control_tower04
pos = -30000, -7290, -25000
rotate = 180, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_habitat_wide01
pos = -30000, -7372, -25160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_habitat_wide02
pos = -30160, -7372, -25000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_habitat_wide03
pos = -30000, -7372, -24840
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_habitat_wide04
pos = -29840, -7372, -25000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_tanks01
pos = -30160, -7835, -25000
rotate = 90, 90, 0
archetype = space_tanks4x4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_tanks02
pos = -29860, -7835, -25000
rotate = 90, 90, 0
archetype = space_tanks4x4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_tanks03
pos = -30000, -7835, -25160
rotate = 90, 0, 0
archetype = space_tanks4x4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_tanks04
pos = -30000, -7835, -24880
rotate = 90, 0, 0
archetype = space_tanks4x4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_tanks05
pos = -30160, -7835, -25041
rotate = 90, 0, 0
archetype = space_tanks4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_tanks06
pos = -29860, -7835, -24959
rotate = 90, 180, 0
archetype = space_tanks4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_tanks07
pos = -30041, -7835, -25160
rotate = 90, 90, 0
archetype = space_tanks4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_tanks08
pos = -29959, -7835, -24880
rotate = 90, -90, 0
archetype = space_tanks4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_industrial01
pos = -30140, -7605, -25000
rotate = 90, 45, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_industrial02
pos = -29860, -7605, -25000
rotate = 90, 45, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_industrial03
pos = -30000, -7605, -25140
rotate = 90, 45, 0
archetype = space_industrial02a
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_industrial04
pos = -30000, -7605, -24860
rotate = 90, 45, 0
archetype = space_industrial02a
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_dome01
pos = -30140, -7270, -25000
rotate = 0, 0, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_dome02
pos = -29860, -7270, -25000
rotate = 0, 0, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_dome03
pos = -30000, -7270, -25140
rotate = 0, 90, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_dome04
pos = -30000, -7270, -24860
rotate = 0, 90, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_dome05
pos = -30100, -7270, -25100
rotate = 0, -45, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_dome06
pos = -29900, -7270, -25100
rotate = 0, 45, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_dome07
pos = -29900, -7270, -24900
rotate = 0, -45, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_B_dome08
pos = -30100, -7270, -24900
rotate = 0, 45, 0
archetype = space_domeb
parent = ku_ksu_02

;BLOCK C

[Object]
nickname = ku_ksu_02_C_control_tower01
pos = -30000, -8250, -25000
rotate = 0, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_control_tower02
pos = -30000, -8540, -25000
rotate = 0, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_control_tower03
pos = -30000, -8628, -25000
rotate = 0, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_control_tower04
pos = -30000, -8710, -25000
rotate = 0, 0, 0
archetype = space_control_tower
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_habitat_wide01
pos = -30000, -8628, -25160
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_habitat_wide02
pos = -30160, -8628, -25000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_habitat_wide03
pos = -30000, -8628, -24840
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_habitat_wide04
pos = -29840, -8628, -25000
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_tanks01
pos = -30160, -8165, -25000
rotate = 90, 90, 0
archetype = space_tanks4x4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_tanks02
pos = -29860, -8165, -25000
rotate = 90, 90, 0
archetype = space_tanks4x4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_tanks03
pos = -30000, -8165, -25160
rotate = 90, 0, 0
archetype = space_tanks4x4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_tanks04
pos = -30000, -8165, -24880
rotate = 90, 0, 0
archetype = space_tanks4x4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_tanks05
pos = -30160, -8165, -25041
rotate = 90, 0, 0
archetype = space_tanks4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_tanks06
pos = -29860, -8165, -24959
rotate = 90, 180, 0
archetype = space_tanks4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_tanks07
pos = -30041, -8165, -25160
rotate = 90, 90, 0
archetype = space_tanks4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_tanks08
pos = -29959, -8165, -24880
rotate = 90, -90, 0
archetype = space_tanks4
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_industrial01
pos = -30140, -8395, -25000
rotate = 90, 45, 0
archetype = space_industrial02a
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_industrial02
pos = -29860, -8395, -25000
rotate = 90, 45, 0
archetype = space_industrial02a
loadout = space_ind01_reactor
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_industrial03
pos = -30000, -8395, -25140
rotate = 90, 45, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_industrial04
pos = -30000, -8395, -24860
rotate = 90, 45, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_dome01
pos = -30140, -8730, -25000
rotate = 180, 0, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_dome02
pos = -29860, -8730, -25000
rotate = 180, 0, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_dome03
pos = -30000, -8730, -25140
rotate = 180, 90, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_dome04
pos = -30000, -8730, -24860
rotate = 180, 90, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_dome05
pos = -30100, -8730, -25100
rotate = 180, -45, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_dome06
pos = -29900, -8730, -25100
rotate = 180, 45, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_dome07
pos = -29900, -8730, -24900
rotate = 180, -45, 0
archetype = space_domeb
parent = ku_ksu_02

[Object]
nickname = ku_ksu_02_C_dome08
pos = -30100, -8730, -24900
rotate = 180, 45, 0
archetype = space_domeb
parent = ku_ksu_02
'''
