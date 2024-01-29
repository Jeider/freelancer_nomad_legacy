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


class StuttgartShipyard(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = '203622'
    TEMPLATE = '''[Object]
nickname = Rh_stut_02
ids_name = 203622
pos = 0, 0, 0
rotate = 0, -90, 0
archetype = space_factory02
ids_info = 065559
dock_with = Rh_stut_02_base
base = Rh_stut_02_base
reputation = rh_grp
behavior = NOTHING
voice = atc_leg_m01
space_costume = rh_wilham_head, rh_male_guard_body, prop_hat_male_rh_grd_visor, prop_neuralnet_c
difficulty_level = 11
loadout = space_factory02_rh
pilot = pilot_solar_hard

[Object]
nickname = rh_stut_02_industrial01
pos = 250, 245, 810
rotate = 0, 0, 0
archetype = space_industrial02a
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_industrial02
pos = 0, 245, 810
rotate = 0, 0, 0
archetype = space_industrial02a
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_industrial03
pos = -250, 245, 810
rotate = 0, 0, 0
archetype = space_industrial02a
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_industrial04
pos = 250, -245, 810
rotate = 0, 0, 0
archetype = space_industrial02a
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_industrial05
pos = 0, -245, 810
rotate = 0, 0, 0
archetype = space_industrial02a
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_industrial06
pos = -250, -245, 810
rotate = 0, 0, 0
archetype = space_industrial02a
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_girder01
pos = 250, -148, 580
rotate = 45, 0, 0
archetype = space_girder
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_girder02
pos = 0, -148, 580
rotate = 45, 0, 0
archetype = space_girder
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_girder03
pos = -250, -148, 580
rotate = 45, 0, 0
archetype = space_girder
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_girder04
pos = 250, 147, 580
rotate = -45, 0, 0
archetype = space_girder
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_girder05
pos = 0, 147, 580
rotate = -45, 0, 0
archetype = space_girder
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_girder06
pos = -250, 147, 580
rotate = -45, 0, 0
archetype = space_girder
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_girder07
pos = 250, -80, 670
rotate = 35, 0, 0
archetype = space_girder
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_girder08
pos = 0, -80, 670
rotate = 35, 0, 0
archetype = space_girder
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_girder09
pos = -250, -80, 670
rotate = 35, 0, 0
archetype = space_girder
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_girder10
pos = 250, 80, 670
rotate = -35, 0, 0
archetype = space_girder
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_girder11
pos = 0, 80, 670
rotate = -35, 0, 0
archetype = space_girder
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_girder12
pos = -250, 80, 670
rotate = -35, 0, 0
archetype = space_girder
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_shipyard01
pos = 250, 465, 990
rotate = 0, 0, 180
archetype = shipyard
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_shipyard02
pos = 0, 465, 990
rotate = 0, 0, 180
archetype = shipyard
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_shipyard03
pos = -250, 465, 990
rotate = 0, 0, 180
archetype = shipyard
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_shipyard04
pos = 250, -465, 990
rotate = 0, 0, 0
archetype = shipyard
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_shipyard05
pos = 0, -465, 990
rotate = 0, 0, 0
archetype = shipyard
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_shipyard06
pos = -250, -465, 990
rotate = 0, 0, 0
archetype = shipyard
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_industrial07
pos = 600, 0, 495
rotate = 0, -90, 0
archetype = space_industrial
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_industrial08
pos = -600, 0, 495
rotate = 0, 90, 0
archetype = space_industrial
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_habitat01
pos = -600, 290, 495
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_habitat02
pos = 600, 205, 495
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_habitat03
pos = -600, 140, 495
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_tankl01
pos = 250, 245, 1050
rotate = -90, 0, 0
archetype = space_tanklx4
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_tankl02
pos = 0, 245, 1050
rotate = -90, 0, 0
archetype = space_tanklx4
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_tankl03
pos = -250, 245, 1050
rotate = -90, 0, 0
archetype = space_tanklx4
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_tankl04
pos = 250, -245, 1050
rotate = -90, 0, 0
archetype = space_tanklx4
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_tankl05
pos = 0, -245, 1050
rotate = -90, 0, 0
archetype = space_tanklx4
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_tankl06
pos = -250, -245, 1050
rotate = -90, 0, 0
archetype = space_tanklx4
parent = Rh_stut_02

[Object]
nickname = rh_stut_02_tankl07
pos = 250, 0, 360
rotate = 0, 0, 90
archetype = space_tankl2x2
parent = Rh_stut_02

[Object]
nickname = Rh_stut_02_tankl08
pos = -250, 0, 360
rotate = 0, 0, 90
archetype = space_tankl2x2
parent = Rh_stut_02
'''


class ForbesShipyard(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_for_03'
    TEMPLATE = '''[Object]
nickname = li_for_03
ids_name = 203666
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_mining01
ids_info = 065586
dock_with = li_for_03_Base
base = li_for_03_Base
reputation = li_grp
behavior = NOTHING
voice = atc_leg_f01
space_costume = br_newscaster_head_gen_hat, li_hatcher_body, prop_hat_female_li_elite
difficulty_level = 12
loadout = space_mining01_li
pilot = pilot_solar_hardest

[Object]
nickname = li_for_03_industrial01
pos = 242, -460, 376
rotate = 0, 0, 0
archetype = space_industriala
parent = li_for_03

[Object]
nickname = li_for_03_industrial02
pos = 600, -460, 376
rotate = 0, 0, 0
archetype = space_industriala
parent = li_for_03

[Object]
nickname = li_for_03_industrial03
pos = 295, -156, 376
rotate = 0, 0, 0
archetype = space_industriala
parent = li_for_03

[Object]
nickname = li_for_03_industrial04
pos = -242, -460, 628
rotate = 0, 0, 0
archetype = space_industriala
parent = li_for_03

[Object]
nickname = li_for_03_industrial05
pos = -600, -460, 628
rotate = 0, 0, 0
archetype = space_industriala
parent = li_for_03

[Object]
nickname = li_for_03_industrial06
pos = -295, -156, 628
rotate = 0, 0, 0
archetype = space_industriala
parent = li_for_03

[Object]
nickname = li_for_03_industrial07
pos = 0, 230, 640
rotate = 0, 0, 0
archetype = space_industriala
parent = li_for_03

[Object]
nickname = li_for_03_industrial08
pos = 0, 230, 890
rotate = 0, 0, 0
archetype = space_industriala
parent = li_for_03

[Object]
nickname = li_for_03_tankl01
pos = 242, -460, 630
rotate = 0, 0, 180
archetype = space_tankl4
parent = li_for_03

[Object]
nickname = li_for_03_tankl02
pos = 600, -460, 630
rotate = 0, 0, 180
archetype = space_tankl4
parent = li_for_03

[Object]
nickname = li_for_03_tankl03
pos = 295, -156, 630
rotate = 0, 0, 0
archetype = space_tankl4
parent = li_for_03

[Object]
nickname = li_for_03_tankl04
pos = -242, -460, 370
rotate = 0, 0, 180
archetype = space_tankl4
parent = li_for_03

[Object]
nickname = li_for_03_tankl05
pos = -600, -460, 370
rotate = 0, 0, 180
archetype = space_tankl4
parent = li_for_03

[Object]
nickname = li_for_03_tankl06
pos = -295, -156, 370
rotate = 0, 0, 0
archetype = space_tankl4
parent = li_for_03

[Object]
nickname = li_for_03_girder01
pos = 140, -155, 376
rotate = 0, 90, 0
archetype = space_girder
parent = li_for_03

[Object]
nickname = li_for_03_girder02
pos = 95, -296, 376
rotate = 62, 90, 0
archetype = space_girder
parent = li_for_03

[Object]
nickname = li_for_03_girder03
pos = 400, -460, 376
rotate = 0, 90, 0
archetype = space_girder
parent = li_for_03

[Object]
nickname = li_for_03_girder04
pos = 466, -265, 376
rotate = 45, 90, 0
archetype = space_girder
parent = li_for_03

[Object]
nickname = li_for_03_girder05
pos = 270, -300, 376
rotate = -75, 90, 0
archetype = space_girder
parent = li_for_03

[Object]
nickname = li_for_03_girder06
pos = -140, -155, 628
rotate = 0, 90, 0
archetype = space_girder
parent = li_for_03

[Object]
nickname = li_for_03_girder07
pos = -95, -296, 628
rotate = -62, 90, 0
archetype = space_girder
parent = li_for_03

[Object]
nickname = li_for_03_girder08
pos = -270, -300, 628
rotate = 75, 90, 0
archetype = space_girder
parent = li_for_03

[Object]
nickname = li_for_03_girder09
pos = -400, -460, 628
rotate = 0, 90, 0
archetype = space_girder
parent = li_for_03

[Object]
nickname = li_for_03_girder10
pos = -466, -265, 628
rotate = -45, 90, 0
archetype = space_girder
parent = li_for_03

[Object]
nickname = li_for_03_girder11
pos = 0, 35, 505
rotate = -45, 0, 0
archetype = space_girder
parent = li_for_03

[Object]
nickname = li_for_03_girder12
pos = 0, 35, 755
rotate = -45, 0, 0
archetype = space_girder
parent = li_for_03

[Object]
nickname = li_for_03_shipyard01
pos = 242, -675, 520
rotate = 0, 0, 0
archetype = shipyard
parent = li_for_03

[Object]
nickname = li_for_03_shipyard02
pos = 600, -675, 520
rotate = 0, 0, 0
archetype = shipyard
parent = li_for_03

[Object]
nickname = li_for_03_shipyard03
pos = -242, -675, 480
rotate = 0, 180, 0
archetype = shipyard
parent = li_for_03

[Object]
nickname = li_for_03_shipyard04
pos = 295, 57, 600
rotate = 0, 0, 180
archetype = shipyard
parent = li_for_03

[Object]
nickname = li_for_03_shipyard05
pos = -600, -675, 480
rotate = 0, 180, 0
archetype = shipyard
parent = li_for_03

[Object]
nickname = li_for_03_dome01
pos = 0, 260, 340
rotate = 0, 0, 0
archetype = space_dome
parent = li_for_03

[Object]
nickname = li_for_03_habitat01
pos = 0, 374, 640
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_for_03

[Object]
nickname = li_for_03_habitat02
pos = 0, 435, 890
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = li_for_03

[Object]
nickname = li_for_03_habitat03
pos = 0, 550, 640
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = li_for_03

[Object]
nickname = li_for_03_panel01
pos = -295, -96, 628
rotate = 0, -60, 0
archetype = space_solar_pnl
parent = li_for_03
'''
