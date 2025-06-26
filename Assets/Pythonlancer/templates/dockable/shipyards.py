from templates.space_object_template import SpaceObjectTemplate


class CambridgeShipyard(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'br_cam_02'
    TEMPLATE = '''[Object]
nickname = br_cam_02
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = space_police01
{dock_props}

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
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_factory02
{dock_props}

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
    SPACE_OBJECT_NAME = 'rh_stut_02'
    TEMPLATE = '''[Object]
nickname = rh_stut_02
pos = 0, 0, 0
rotate = 0, -90, 0
archetype = space_factory02
{dock_props}

[Object]
nickname = rh_stut_02_industrial01
pos = 250, 245, 810
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_stut_02

[Object]
nickname = rh_stut_02_industrial02
pos = 0, 245, 810
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_stut_02

[Object]
nickname = rh_stut_02_industrial03
pos = -250, 245, 810
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_stut_02

[Object]
nickname = rh_stut_02_industrial04
pos = 250, -245, 810
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_stut_02

[Object]
nickname = rh_stut_02_industrial05
pos = 0, -245, 810
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_stut_02

[Object]
nickname = rh_stut_02_industrial06
pos = -250, -245, 810
rotate = 0, 0, 0
archetype = space_industrial02a
parent = rh_stut_02

[Object]
nickname = rh_stut_02_girder01
pos = 250, -148, 580
rotate = 45, 0, 0
archetype = space_girder
parent = rh_stut_02

[Object]
nickname = rh_stut_02_girder02
pos = 0, -148, 580
rotate = 45, 0, 0
archetype = space_girder
parent = rh_stut_02

[Object]
nickname = rh_stut_02_girder03
pos = -250, -148, 580
rotate = 45, 0, 0
archetype = space_girder
parent = rh_stut_02

[Object]
nickname = rh_stut_02_girder04
pos = 250, 147, 580
rotate = -45, 0, 0
archetype = space_girder
parent = rh_stut_02

[Object]
nickname = rh_stut_02_girder05
pos = 0, 147, 580
rotate = -45, 0, 0
archetype = space_girder
parent = rh_stut_02

[Object]
nickname = rh_stut_02_girder06
pos = -250, 147, 580
rotate = -45, 0, 0
archetype = space_girder
parent = rh_stut_02

[Object]
nickname = rh_stut_02_girder07
pos = 250, -80, 670
rotate = 35, 0, 0
archetype = space_girder
parent = rh_stut_02

[Object]
nickname = rh_stut_02_girder08
pos = 0, -80, 670
rotate = 35, 0, 0
archetype = space_girder
parent = rh_stut_02

[Object]
nickname = rh_stut_02_girder09
pos = -250, -80, 670
rotate = 35, 0, 0
archetype = space_girder
parent = rh_stut_02

[Object]
nickname = rh_stut_02_girder10
pos = 250, 80, 670
rotate = -35, 0, 0
archetype = space_girder
parent = rh_stut_02

[Object]
nickname = rh_stut_02_girder11
pos = 0, 80, 670
rotate = -35, 0, 0
archetype = space_girder
parent = rh_stut_02

[Object]
nickname = rh_stut_02_girder12
pos = -250, 80, 670
rotate = -35, 0, 0
archetype = space_girder
parent = rh_stut_02

[Object]
nickname = rh_stut_02_shipyard01
pos = 250, 465, 990
rotate = 0, 0, 180
archetype = shipyard
parent = rh_stut_02

[Object]
nickname = rh_stut_02_shipyard02
pos = 0, 465, 990
rotate = 0, 0, 180
archetype = shipyard
parent = rh_stut_02

[Object]
nickname = rh_stut_02_shipyard03
pos = -250, 465, 990
rotate = 0, 0, 180
archetype = shipyard
parent = rh_stut_02

[Object]
nickname = rh_stut_02_shipyard04
pos = 250, -465, 990
rotate = 0, 0, 0
archetype = shipyard
parent = rh_stut_02

[Object]
nickname = rh_stut_02_shipyard05
pos = 0, -465, 990
rotate = 0, 0, 0
archetype = shipyard
parent = rh_stut_02

[Object]
nickname = rh_stut_02_shipyard06
pos = -250, -465, 990
rotate = 0, 0, 0
archetype = shipyard
parent = rh_stut_02

[Object]
nickname = rh_stut_02_industrial07
pos = 600, 0, 495
rotate = 0, -90, 0
archetype = space_industrial
parent = rh_stut_02

[Object]
nickname = rh_stut_02_industrial08
pos = -600, 0, 495
rotate = 0, 90, 0
archetype = space_industrial
parent = rh_stut_02

[Object]
nickname = rh_stut_02_habitat01
pos = -600, 290, 495
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = rh_stut_02

[Object]
nickname = rh_stut_02_habitat02
pos = 600, 205, 495
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = rh_stut_02

[Object]
nickname = rh_stut_02_habitat03
pos = -600, 140, 495
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_02

[Object]
nickname = rh_stut_02_tankl01
pos = 250, 245, 1050
rotate = -90, 0, 0
archetype = space_tanklx4
parent = rh_stut_02

[Object]
nickname = rh_stut_02_tankl02
pos = 0, 245, 1050
rotate = -90, 0, 0
archetype = space_tanklx4
parent = rh_stut_02

[Object]
nickname = rh_stut_02_tankl03
pos = -250, 245, 1050
rotate = -90, 0, 0
archetype = space_tanklx4
parent = rh_stut_02

[Object]
nickname = rh_stut_02_tankl04
pos = 250, -245, 1050
rotate = -90, 0, 0
archetype = space_tanklx4
parent = rh_stut_02

[Object]
nickname = rh_stut_02_tankl05
pos = 0, -245, 1050
rotate = -90, 0, 0
archetype = space_tanklx4
parent = rh_stut_02

[Object]
nickname = rh_stut_02_tankl06
pos = -250, -245, 1050
rotate = -90, 0, 0
archetype = space_tanklx4
parent = rh_stut_02

[Object]
nickname = rh_stut_02_tankl07
pos = 250, 0, 360
rotate = 0, 0, 90
archetype = space_tankl2x2
parent = rh_stut_02

[Object]
nickname = rh_stut_02_tankl08
pos = -250, 0, 360
rotate = 0, 0, 90
archetype = space_tankl2x2
parent = rh_stut_02
'''


class ForbesShipyard(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_for_03'
    TEMPLATE = '''[Object]
nickname = li_for_03
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_mining01
{dock_props}

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


class UlsterShipyardDestroyed(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'br_uls_03'
    TEMPLATE = '''[Object]
nickname = br_uls_03
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_industrial_dmg_root
{root_props}

[Object]
nickname = br_uls_03_tube01
pos = 0, 750, 0
rotate = 90, 0, 0
archetype = space_tube_fix
parent = br_uls_03

[Object]
nickname = br_uls_03_tube02
pos = 0, 275, -275
rotate = 45, 0, 0
archetype = space_short_tube
parent = br_uls_03

[Object]
nickname = br_uls_03_tube03
pos = 0, -275, -275
rotate = -45, 0, 0
archetype = space_short_tube
parent = br_uls_03

[Object]
nickname = br_uls_03_girder01
pos = 400, 0, 0
rotate = 90, 0, -10
archetype = space_beamx_dmg
parent = br_uls_03

[Object]
nickname = br_uls_03_girder02
pos = -400, 0, 0
rotate = 90, 0, 0
archetype = space_girder
parent = br_uls_03

[Object]
nickname = br_uls_03_girder03
pos = -120, 504, 0
rotate = 40, -90, 0
archetype = space_girdera
parent = br_uls_03

[Object]
nickname = br_uls_03_girder04
pos = 380, 380, 0
rotate = -40, -90, 180
archetype = space_beaml_dmg
parent = br_uls_03

[Object]
nickname = br_uls_03_girder05
pos = -120, -504, 0
rotate = -40, -90, 0
archetype = space_girdera
parent = br_uls_03

[Object]
nickname = br_uls_03_girder06
pos = 220, -404, 0
rotate = -40, 90, 0
archetype = space_beaml_dmg
parent = br_uls_03

[Object]
nickname = br_uls_03_ind01
pos = -400, 150, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_uls_03

[Object]
nickname = br_uls_03_ind02
pos = -400, -150, 0
rotate = -90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor_dmg
parent = br_uls_03

[Object]
nickname = br_uls_03_ind03
pos = 430, 150, 0
rotate = 90, 0, -10
archetype = space_industrial01a
loadout = space_ind01_reactor_dmg
parent = br_uls_03

[Object]
nickname = br_uls_03_ind05
pos = 0, 520, 0
rotate = 0, 90, 5
archetype = space_industriala
parent = br_uls_03

[Object]
nickname = br_uls_03_ind06
pos = 0, -500, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = br_uls_03

[Object]
nickname = br_uls_03_ind07
pos = 0, 275, -300
rotate = 90, 0, 90
archetype = space_industrial02d
parent = br_uls_03

[Object]
nickname = br_uls_03_ind08
pos = 0, -275, -300
rotate = 90, 0, 90
archetype = space_industrial02d
parent = br_uls_03

[Object]
nickname = br_uls_03_ind09
pos = 0, 275, 300
rotate = 90, 0, 90
archetype = space_industrial02d
parent = br_uls_03

[Object]
nickname = br_uls_03_ind10
pos = 0, -275, 300
rotate = 90, 0, 90
archetype = space_industrial02d
parent = br_uls_03

[Object]
nickname = br_uls_03_shipyard01
pos = 0, 275, -400
rotate = -90, 0, 90
archetype = shipyard_dmgA
parent = br_uls_03

[Object]
nickname = br_uls_03_shipyard02
pos = 0, -275, -400
rotate = -90, 0, 90
archetype = shipyard
parent = br_uls_03

[Object]
nickname = br_uls_03_shipyard03
pos = 0, 275, 400
rotate = 90, 0, 90
archetype = shipyard_dmgA
parent = br_uls_03

[Object]
nickname = br_uls_03_shipyard04
pos = -100, -275, 600
rotate = 120, 30, -50
archetype = shipyard_dmgB
parent = br_uls_03

[Object]
nickname = br_uls_03_twr01
pos = 15, 590, 0
rotate = 0, 0, 10
archetype = space_medium_control_tower
parent = br_uls_03

[Object]
nickname = br_uls_03_twr02
pos = 0, -600, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = br_uls_03

[Object]
nickname = br_uls_03_tank01
pos = -10, -250, 0
rotate = 90, 90, 0
archetype = space_tankl4_dmg
parent = br_uls_03

[Object]
nickname = br_uls_03_tank02
pos = -10, 250, 0
rotate = 90, 90, 0
archetype = space_tankl4x4_dmg
parent = br_uls_03

[Object]
nickname = br_uls_03_tank03
pos = 10, -250, 0
rotate = 90, -50, 0
archetype = space_tankl4x4_dmg
parent = br_uls_03

[Object]
nickname = br_uls_03_tank04
pos = 10, 250, 0
rotate = 90, -90, 0
archetype = space_tankl4_dmg
parent = br_uls_03

[Object]
nickname = br_uls_03_airlock01
pos = 0, 700, 0
rotate = 90, 0, 10
archetype = space_airlock_dummy
parent = br_uls_03

[Object]
nickname = br_uls_03_airlock02
pos = 0, -700, 0
rotate = -90, 0, 0
archetype = space_airlock_dummy
parent = br_uls_03

[Object]
nickname = br_uls_03_hab_dmg01
pos = 0, 750, 0
rotate = 0, 0, 0
archetype = space_habitat_dmg
parent = br_uls_03

[Object]
nickname = br_uls_03_hab_dmg02
pos = 0, -825, 0
rotate = 0, 0, 0
archetype = space_habitat_dmg
parent = br_uls_03
'''


class UlsterShipyardAlive(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'br_uls_03'
    TEMPLATE = '''[Object]
nickname = br_uls_03
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_police01
{dock_props}

[Object]
nickname = br_uls_03_ind20
pos = 0, -1000, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = br_uls_03

[Object]
nickname = br_uls_03_tube01
pos = 0, -250, 0
rotate = 90, 0, 0
archetype = space_tube_fix
parent = br_uls_03

[Object]
nickname = br_uls_03_tube02
pos = 0, -725, -275
rotate = 45, 0, 0
archetype = space_short_tube
parent = br_uls_03

[Object]
nickname = br_uls_03_tube03
pos = 0, -1275, -275
rotate = -45, 0, 0
archetype = space_short_tube
parent = br_uls_03

[Object]
nickname = br_uls_03_girder01
pos = 400, -1000, 0
rotate = 90, 0, 0
archetype = space_girder
parent = br_uls_03

[Object]
nickname = br_uls_03_girder02
pos = -400, -1000, 0
rotate = 90, 0, 0
archetype = space_girder
parent = br_uls_03

[Object]
nickname = br_uls_03_girder03
pos = -120, -496, 0
rotate = 40, -90, 0
archetype = space_girdera
parent = br_uls_03

[Object]
nickname = br_uls_03_girder04
pos = 120, -496, 0
rotate = 40, 90, 0
archetype = space_girdera
parent = br_uls_03

[Object]
nickname = br_uls_03_girder05
pos = -120, -1504, 0
rotate = -40, -90, 0
archetype = space_girdera
parent = br_uls_03

[Object]
nickname = br_uls_03_girder06
pos = 120, -1504, 0
rotate = -40, 90, 0
archetype = space_girdera
parent = br_uls_03

[Object]
nickname = br_uls_03_girder07
pos = 50, -1000, 0
rotate = 0, 90, 0
archetype = space_girdera
parent = br_uls_03

[Object]
nickname = br_uls_03_girder08
pos = -50, -1000, 0
rotate = 0, -90, 0
archetype = space_girdera
parent = br_uls_03

[Object]
nickname = br_uls_03_ind01
pos = -400, -850, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_uls_03

[Object]
nickname = br_uls_03_ind02
pos = -400, -1150, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_uls_03

[Object]
nickname = br_uls_03_ind03
pos = 400, -850, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_uls_03

[Object]
nickname = br_uls_03_ind04
pos = 400, -1150, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = br_uls_03

[Object]
nickname = br_uls_03_ind05
pos = 0, -500, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = br_uls_03

[Object]
nickname = br_uls_03_ind06
pos = 0, -1500, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = br_uls_03

[Object]
nickname = br_uls_03_ind07
pos = 0, -725, -300
rotate = 90, 0, 90
archetype = space_industrial02d
parent = br_uls_03

[Object]
nickname = br_uls_03_ind08
pos = 0, -1275, -300
rotate = 90, 0, 90
archetype = space_industrial02d
parent = br_uls_03

[Object]
nickname = br_uls_03_ind09
pos = 0, -725, 300
rotate = 90, 0, 90
archetype = space_industrial02d
parent = br_uls_03

[Object]
nickname = br_uls_03_ind10
pos = 0, -1275, 300
rotate = 90, 0, 90
archetype = space_industrial02d
parent = br_uls_03

[Object]
nickname = br_uls_03_shipyard01
pos = 0, -725, -400
rotate = -90, 0, 90
archetype = shipyard
parent = br_uls_03

[Object]
nickname = br_uls_03_shipyard02
pos = 0, -1275, -400
rotate = -90, 0, 90
archetype = shipyard
parent = br_uls_03

[Object]
nickname = br_uls_03_shipyard03
pos = 0, -725, 400
rotate = 90, 0, 90
archetype = shipyard
parent = br_uls_03

[Object]
nickname = br_uls_03_shipyard04
pos = 0, -1275, 400
rotate = -90, 180, -90
archetype = shipyard
parent = br_uls_03

[Object]
nickname = br_uls_03_twr01
pos = 0, -400, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = br_uls_03

[Object]
nickname = br_uls_03_twr02
pos = 0, -1600, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = br_uls_03

[Object]
nickname = br_uls_03_airlock01
pos = 0, -300, 0
rotate = 90, 0, 0
archetype = space_airlock_dummy
parent = br_uls_03

[Object]
nickname = br_uls_03_airlock02
pos = 0, -1700, 0
rotate = -90, 0, 0
archetype = space_airlock_dummy
parent = br_uls_03

[Object]
nickname = br_uls_03_hab_dmg01
pos = 0, -200, 0
rotate = 90, 0, 0
archetype = space_girder
parent = br_uls_03

[Object]
nickname = br_uls_03_hab_dmg02
pos = 0, -1840, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = br_uls_03
'''


class HeavyBarrelShipyard(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'br_hbr_02'
    TEMPLATE = '''[Object]
nickname = br_hbr_02
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_police01
{dock_props}

[Object]
nickname = br_hbr_02_prison1
pos = 135, -650, 0
rotate = 0, 90, 0
archetype = space_prison_dummy
parent = br_hbr_02

[Object]
nickname = br_hbr_02_prison2
pos = -135, -650, 0
rotate = 0, 90, 0
archetype = space_prison_dummy
parent = br_hbr_02

[Object]
nickname = br_hbr_02_shipyard01
pos = 135, -700, -600
rotate = 0, 180, 0
archetype = shipyard
parent = br_hbr_02

[Object]
nickname = br_hbr_02_shipyard02
pos = -135, -700, -600
rotate = 0, 180, 0
archetype = shipyard
parent = br_hbr_02

[Object]
nickname = br_hbr_02_shipyard03
pos = 135, -700, 600
rotate = 0, 0, 0
archetype = shipyard
parent = br_hbr_02

[Object]
nickname = br_hbr_02_shipyard04
pos = -135, -700, 600
rotate = 0, 0, 0
archetype = shipyard
parent = br_hbr_02

[Object]
nickname = br_hbr_02_shipyard05
pos = 0, -400, 0
rotate = 180, 0, 0
archetype = shipyard
parent = br_hbr_02

[Object]
nickname = br_hbr_02_control_tower01
pos = 0, -335, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = br_hbr_02

[Object]
nickname = br_hbr_02_control_tower02
pos = 0, -790, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = br_hbr_02

[Object]
nickname = br_hbr_02_girder01
pos = 0, -100, 0
rotate = 90, 0, 0
archetype = space_girderc
parent = br_hbr_02

[Object]
nickname = br_hbr_02_habitat01
pos = 0, -240, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = br_hbr_02

[Object]
nickname = br_hbr_02_tanks01
pos = 0, -1150, 0
rotate = 90, 90, 0
archetype = space_tankl2x2
parent = br_hbr_02

[Object]
nickname = br_hbr_02_tanks02
pos = 0, -950, 0
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = br_hbr_02

[Object]
nickname = br_hbr_02_tanks03
pos = 0, -940, -100
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = br_hbr_02

[Object]
nickname = br_hbr_02_tanks04
pos = 0, -940, 100
rotate = 90, 90, 0
archetype = space_tankl4x4
parent = br_hbr_02
'''
