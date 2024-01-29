from templates.space_object_template import SpaceObjectTemplate


class PirateBaseBizmark(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_biz_06'
    TEMPLATE = '''[Object]
nickname = rh_biz_06
ids_name = 203885
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_police01
ids_info = 1
base = rh_biz_06_base
dock_with = rh_biz_06_base
reputation = rx_grp
behavior = NOTHING
voice = atc_leg_f01
space_costume = rh_gruenwald_head_gen, pl_female2_journeyman_body
difficulty_level = 5
loadout = rh_space_police01
pilot = pilot_solar_hardest

[Object]
nickname = rh_biz_06_industrial01
pos = 0, -200, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_biz_06

[Object]
nickname = rh_biz_06_industrial02
pos = 0, -450, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_biz_06

[Object]
nickname = rh_biz_06_industrial03
pos = 0, -725, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_biz_06

[Object]
nickname = rh_biz_06_industrial04
pos = -175, -490, 0
rotate = 0, 0, -60
archetype = space_industriala
parent = rh_biz_06

[Object]
nickname = rh_biz_06_industrial05
pos = 175, -490, 0
rotate = 0, 0, 60
archetype = space_industriala
parent = rh_biz_06

[Object]
nickname = rh_biz_06_industrial06
pos = -315, -250, 0
rotate = 0, 0, -60
archetype = space_industriala
parent = rh_biz_06

[Object]
nickname = rh_biz_06_industrial07
pos = 315, -250, 0
rotate = 0, 0, 60
archetype = space_industriala
parent = rh_biz_06

[Object]
nickname = rh_biz_06_girder01
pos = 0, -200, 0
rotate = 90, 0, 0
archetype = space_girder
parent = rh_biz_06

[Object]
nickname = rh_biz_06_girder02
pos = 0, -600, 0
rotate = 90, 0, 0
archetype = space_girder
parent = rh_biz_06

[Object]
nickname = rh_biz_06_girder03
pos = -25, -750, 0
rotate = -60, -90, 0
archetype = space_girdera
parent = rh_biz_06

[Object]
nickname = rh_biz_06_girder04
pos = 25, -750, 0
rotate = -60, 90, 0
archetype = space_girdera
parent = rh_biz_06

[Object]
nickname = rh_biz_06_girder05
pos = -160, -520, 0
rotate = -60, -90, 0
archetype = space_girdera
parent = rh_biz_06

[Object]
nickname = rh_biz_06_girder06
pos = 160, -520, 0
rotate = -60, 90, 0
archetype = space_girdera
parent = rh_biz_06

[Object]
nickname = rh_biz_06_girder07
pos = 100, -455, 0
rotate = 10, 90, 0
archetype = space_girderc
parent = rh_biz_06

[Object]
nickname = rh_biz_06_girder08
pos = -100, -455, 0
rotate = -10, 90, 0
archetype = space_girderc
parent = rh_biz_06

[Object]
nickname = rh_biz_06_girder09
pos = 150, -208, 0
rotate = 5, 90, 0
archetype = space_girder
parent = rh_biz_06

[Object]
nickname = rh_biz_06_girder10
pos = -150, -208, 0
rotate = -5, 90, 0
archetype = space_girder
parent = rh_biz_06

[Object]
nickname = rh_biz_06_habitat01
pos = 0, -840, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = rh_biz_06
'''


class PirateBaseHokkaido(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_hkd_06'
    TEMPLATE = '''[Object]
nickname = ku_hkd_06
ids_name = 208624
pos = 0, 0, 0
rotate = 0, -90, 0
archetype = space_police02
ids_info = 067024
base = ku_hkd_06_base
dock_with = ku_hkd_06_base
visit = 16
reputation = kx_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = ge_male2_head, pi_pirate2_body, prop_neuralnet_d

[Object]
nickname = ku_hkd_06_ind01
pos = -30, 0, 0
rotate = 90, 0, 0
archetype = space_industrial02a
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_ind02
pos = -30, -130, -100
rotate = 0, 0, 0
archetype = space_industrial02d
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_ind03
pos = -120, -200, -100
rotate = 0, 90, 90
archetype = space_industrial02d
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_ind04
pos = 60, -200, -100
rotate = -90, 90, 0
archetype = space_industrial02d
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_dome01
pos = -30, -70, -150
rotate = 0, 0, 0
archetype = space_domea
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_twr01
pos = -30, -100, -100
rotate = 0, 0, 0
archetype = space_control_tower
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_twr02
pos = -130, 50, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_twr03
pos = -30, -320, -100
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_block01
pos = -130, 110, 0
rotate = 0, 0, 0
archetype = space_pirate_control_block
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_block02
pos = -30, -380, -100
rotate = 180, 0, 0
archetype = space_pirate_control_block
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_habitat01
pos = -130, -40, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_girder01
pos = -30, -210, -100
rotate = 90, 0, 0
archetype = space_girderc
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_tank01
pos = -30, -170, -100
rotate = 90, 0, 90
archetype = space_tanks4x4
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_tank02
pos = -30, -210, -100
rotate = 90, 0, 90
archetype = space_tanks4x4
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_tank03
pos = -30, -250, -100
rotate = 90, 0, 90
archetype = space_tanks4x4
parent = ku_hkd_06

[Object]
nickname = ku_hkd_06_tank04
pos = -30, -290, -100
rotate = 90, 0, 90
archetype = space_tanks4x4
parent = ku_hkd_06
'''
