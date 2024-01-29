from templates.space_object_template import SpaceObjectTemplate


class KyushuResearch(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_ksu_04'
    TEMPLATE = '''[Object]
nickname = ku_ksu_04
ids_name = 203744
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_police02
ids_info = 065659
base = ku_ksu_04_base
dock_with = ku_ksu_04_base
visit = 16
reputation = ku_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = sc_scientist2_head, sc_scientist3_body, prop_neuralnet_d
difficulty_level = 10
pilot = pilot_solar_hardest

[Object]
nickname = ku_ksu_04_lightpanel01
pos = 563, 0, 0
rotate = 0, 90, 0
archetype = space_industriala
loadout = lightpanels_x3
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_lightpanel02
pos = 308, 0, 0
rotate = 90, 45, 90
archetype = space_industriala
loadout = lightpanels_x3
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_ind01
pos = 73, 0, 0
rotate = 0, -90, 0
archetype = space_industrialc
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_ctrl_twr01
pos = 148, 0, 0
rotate = 90, 90, 0
archetype = space_control_tower
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_ctrl_twr02
pos = 78, 0, 0
rotate = 90, 90, 0
archetype = space_control_tower
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_ctrl_twr03
pos = 8, 0, 0
rotate = 90, 90, 0
archetype = space_control_tower
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatA01
pos = 113, -162, 0
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatA02
pos = 113, 162, 0
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatA03
pos = 113, 0, -162
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatA04
pos = 113, 0, 162
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatA05
pos = 113, -115, 115
rotate = 45, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatA06
pos = 113, -115, -115
rotate = -45, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatA07
pos = 113, 115, -115
rotate = 45, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatA08
pos = 113, 115, 115
rotate = -45, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatB01
pos = 43, -162, 0
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatB02
pos = 43, 162, 0
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatB03
pos = 43, 0, -162
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatB04
pos = 43, 0, 162
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatB05
pos = 43, -115, 115
rotate = 45, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatB06
pos = 43, -115, -115
rotate = -45, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatB07
pos = 43, 115, -115
rotate = 45, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_habitatB08
pos = 43, 115, 115
rotate = -45, 0, 0
archetype = space_habitat_wide
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_tank01
pos = -47, 100, 0
rotate = 0, 90, 180
archetype = space_tanks2
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_tank02
pos = -47, -100, 0
rotate = 0, 90, 0
archetype = space_tanks2
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_tank03
pos = -47, 0, 100
rotate = -90, 0, 90
archetype = space_tanks2
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_tank04
pos = -47, 0, -100
rotate = 90, 0, -90
archetype = space_tanks2
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_tank05
pos = -47, -75, 75
rotate = 90, 135, 90
archetype = space_tanks2
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_tank06
pos = -47, -75, -75
rotate = 90, 45, 90
archetype = space_tanks2
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_tank07
pos = -47, 75, 75
rotate = 90, -135, 90
archetype = space_tanks2
parent = ku_ksu_04

[Object]
nickname = ku_ksu_04_tank08
pos = -47, 75, -75
rotate = 90, -45, 90
archetype = space_tanks2
parent = ku_ksu_04
'''
