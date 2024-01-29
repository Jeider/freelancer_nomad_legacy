from templates.space_object_template import SpaceObjectTemplate


class CambridgeShipyard(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'br_cam_02'
    TEMPLATE = '''[Object]
nickname = br_cam_02
ids_name = 203725
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = space_police01
ids_info = 065640
dock_with = br_cam_02_base
base = br_cam_02_base
reputation = br_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = br_quigly_head, br_quigly_body, prop_neuralnet_b_right
difficulty_level = 11
loadout = br_space_police01
pilot = pilot_solar_hard

[Object]
nickname = br_cam_02_industrial01
pos = -500, 0, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = br_cam_02

[Object]
nickname = br_cam_02_industrial02
pos = -658, 0, -586
rotate = 0, 30, 0
archetype = space_industriala
parent = br_cam_02
loadout = space_ind_tanks

[Object]
nickname = br_cam_02_industrial03
pos = -658, 0, 586
rotate = 0, -30, 0
archetype = space_industriala
parent = br_cam_02
loadout = space_ind_tanks

[Object]
nickname = br_cam_02_industrial04
pos = -1095, 0, -1024
rotate = 0, 60, 0
archetype = space_industriala
parent = br_cam_02
loadout = space_ind_tanks

[Object]
nickname = br_cam_02_industrial05
pos = -1095, 0, 1024
rotate = 0, -60, 0
archetype = space_industriala
parent = br_cam_02
loadout = space_ind_tanks

[Object]
nickname = br_cam_02_industrial06
pos = -1000, 0, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = br_cam_02

[Object]
nickname = br_cam_02_girder01
pos = -260, 0, 0
rotate = 0, 90, 0
archetype = space_girder
parent = br_cam_02

[Object]
nickname = br_cam_02_girder02
pos = -547, 0, -300
rotate = 0, 15, 0
archetype = space_girder
parent = br_cam_02

[Object]
nickname = br_cam_02_girder03
pos = -547, 0, 300
rotate = 180, -15, 0
archetype = space_girder
parent = br_cam_02

[Object]
nickname = br_cam_02_girder04
pos = -855, 0, -828
rotate = 0, 45, 0
archetype = space_girder
parent = br_cam_02

[Object]
nickname = br_cam_02_girder05
pos = -855, 0, 828
rotate = 0, -45, 0
archetype = space_girder
parent = br_cam_02

[Object]
nickname = br_cam_02_girder06
pos = -750, 0, 0
rotate = 0, 90, 0
archetype = space_girder
parent = br_cam_02

[Object]
nickname = br_cam_02_research01
pos = -1000, 900, 0
rotate = 90, -30, 0
archetype = space_research
parent = br_cam_02

[Object]
nickname = br_cam_02_solar_plant01
pos = -912, 900, 50
rotate = 0, -30, 0
archetype = space_solar_plant
spin = 0.1, 0, 0
parent = br_cam_02

[Object]
nickname = br_cam_02_solar_plant02
pos = -912, -900, 50
rotate = 0, -30, 0
archetype = space_solar_plant
spin = 0.1, 0, 0
parent = br_cam_02

[Object]
nickname = br_cam_02_shipyard01
pos = -930, 190, -430
rotate = 180, 120, 0
archetype = shipyard
parent = br_cam_02

[Object]
nickname = br_cam_02_shipyard02
pos = -930, -190, -430
rotate = 0, -60, 0
archetype = shipyard
parent = br_cam_02

[Object]
nickname = br_cam_02_shipyard03
pos = -1250, 190, -750
rotate = 180, 150, 0
archetype = shipyard
parent = br_cam_02

[Object]
nickname = br_cam_02_shipyard04
pos = -1250, -190, -750
rotate = 0, -30, 0
archetype = shipyard
parent = br_cam_02

[Object]
nickname = br_cam_02_shipyard05
pos = -930, 190, 430
rotate = 180, 60, 0
archetype = shipyard
parent = br_cam_02

[Object]
nickname = br_cam_02_shipyard06
pos = -930, -190, 430
rotate = 0, -120, 0
archetype = shipyard
parent = br_cam_02

[Object]
nickname = br_cam_02_shipyard07
pos = -1250, 190, 750
rotate = 180, 30, 0
archetype = shipyard
parent = br_cam_02

[Object]
nickname = br_cam_02_shipyard08
pos = -1250, -190, 750
rotate = 0, -150, 0
archetype = shipyard
parent = br_cam_02

[Object]
nickname = br_cam_02_habitat01
pos = -500, 140, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_cam_02

[Object]
nickname = br_cam_02_habitat02
pos = -500, -140, 0
rotate = 180, 0, 0
archetype = space_habitat_wide
parent = br_cam_02

[Object]
nickname = br_cam_02_habitat03
pos = -500, 345, 0
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = br_cam_02

[Object]
nickname = br_cam_02_habitat04
pos = -500, -345, 0
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = br_cam_02
'''


class HokkaidoShipyard(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'Ku_hkd_03'
    TEMPLATE = '''[Object]
nickname = Ku_hkd_03
ids_name = 203758
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_factory02
ids_info = 065673
base = Ku_hkd_03_base
dock_with = Ku_hkd_03_base
reputation = ku_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = ku_bartender_head_hat, ku_male_elite_body, prop_hat_male_ku_elite
difficulty_level = 11
loadout = space_factory02_ku
pilot = pilot_solar_hard

[Object]
nickname = ku_hkd_03_girder01
pos = -250, -149, -580
rotate = -45, 0, 0
archetype = space_girder
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_girder02
pos = -250, -55, -635
rotate = -35, 0, 0
archetype = space_girder
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_girder03
pos = 0, -149, -580
rotate = -45, 0, 0
archetype = space_girder
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_girder04
pos = 0, -55, -635
rotate = -35, 0, 0
archetype = space_girder
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_girder05
pos = 250, -149, -580
rotate = -45, 0, 0
archetype = space_girder
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_girder06
pos = 250, -55, -635
rotate = -35, 0, 0
archetype = space_girder
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_industrial01
pos = -250, -257, -757
rotate = 90, 0, 0
archetype = space_industrial02a
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_industrial02
pos = 0, -257, -757
rotate = 90, 0, 0
archetype = space_industrial02a
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_industrial03
pos = 250, -257, -757
rotate = 90, 0, 0
archetype = space_industrial02a
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_shipyard01
pos = -250, -400, -978
rotate = 90, 0, 0
archetype = shipyard
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_shipyard02
pos = 0, -400, -978
rotate = 90, 0, 0
archetype = shipyard
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_shipyard03
pos = 250, -400, -978
rotate = 90, 0, 0
archetype = shipyard
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_girder07
pos = -250, 149, -580
rotate = 45, 0, 0
archetype = space_girder
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_girder08
pos = -250, 55, -635
rotate = 35, 0, 0
archetype = space_girder
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_girder09
pos = 0, 149, -580
rotate = 45, 0, 0
archetype = space_girder
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_girder10
pos = 0, 55, -635
rotate = 35, 0, 0
archetype = space_girder
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_girder11
pos = 250, 149, -580
rotate = 45, 0, 0
archetype = space_girder
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_girder12
pos = 250, 55, -635
rotate = 35, 0, 0
archetype = space_girder
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_industrial04
pos = -250, 257, -757
rotate = 90, 0, 0
archetype = space_industrial02a
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_industrial05
pos = 0, 257, -757
rotate = 90, 0, 0
archetype = space_industrial02a
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_industrial06
pos = 250, 257, -757
rotate = 90, 0, 0
archetype = space_industrial02a
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_shipyard04
pos = -250, 400, -980
rotate = -90, 180, 0
archetype = shipyard
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_shipyard05
pos = 0, 400, -980
rotate = -90, 180, 0
archetype = shipyard
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_shipyard06
pos = 250, 400, -980
rotate = -90, 180, 0
archetype = shipyard
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_reactor01
pos = 0, -226.5, -161
rotate = 0, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_reactor02
pos = 0, -226.5, -430
rotate = 0, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_tanks01
pos = -250, 520, -757
rotate = 90, 60, 0
archetype = space_tankl4x4
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_tanks02
pos = 0, 520, -757
rotate = 0, 90, 90
archetype = space_tankl4x4
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_tanks03
pos = 250, 520, -757
rotate = 90, -60, 0
archetype = space_tankl4x4
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_tanks04
pos = -250, -520, -757
rotate = 90, 60, 0
archetype = space_tankl4x4
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_tanks05
pos = 0, -520, -757
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = ku_hkd_03

[Object]
nickname = ku_hkd_03_tanks06
pos = 250, -520, -757
rotate = 90, -60, 0
archetype = space_tankl4x4
parent = ku_hkd_03

'''
