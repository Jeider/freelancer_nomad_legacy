from templates.space_object_template import SpaceObjectTemplate


class ForbesMegafactoryOriginal(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_for_02'
    TEMPLATE = '''[Object]
nickname = li_for_02
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = prison_detroit
{dock_props}

[Object]
nickname = li_for_02_tube01
pos = -335, 10, 1635
rotate = 0, 180, 0
archetype = space_tube
parent = li_for_02

[Object]
nickname = li_for_02_tube02
pos = -75, 10, 1635
rotate = 0, 180, 0
archetype = space_tube
parent = li_for_02

[Object]
nickname = li_for_02_tube03
pos = -335, 50, 1635
rotate = 0, 180, 0
archetype = space_tube
parent = li_for_02

[Object]
nickname = li_for_02_tube04
pos = -75, -250, 1635
rotate = 0, 180, 0
archetype = space_tube
parent = li_for_02

;SECTION 1

[Object]
nickname = li_for_02_S1_ind01
pos = -205, -120, 1635
rotate = 0, 0, 45
archetype = space_industriala
parent = li_for_02

[Object]
nickname = li_for_02_S1_ind02
pos = -335, 10, 1635
rotate = 45, 90, 0
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S1_ind03
pos = -75, 10, 1635
rotate = 0, 90, 45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S1_ind04
pos = -335, -250, 1635
rotate = 0, 90, 45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S1_ind05
pos = -75, -250, 1635
rotate = 0, 90, -45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S1_ind06
pos = -505, -120, 1635
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_02

[Object]
nickname = li_for_02_S1_ind07
pos = 95, -120, 1635
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_02

[Object]
nickname = li_for_02_S1_girder01
pos = -205, -120, 1635
rotate = 0, 90, 0
archetype = space_girder
parent = li_for_02

;SECTION 2

[Object]
nickname = li_for_02_S2_ind01
pos = -205, -120, 1385
rotate = 0, 0, 45
archetype = space_industriala
parent = li_for_02

[Object]
nickname = li_for_02_S2_ind02
pos = -335, 10, 1385
rotate = 45, 90, 0
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S2_ind03
pos = -75, 10, 1385
rotate = 0, 90, 45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S2_ind04
pos = -335, -250, 1385
rotate = 0, 90, 45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S2_ind05
pos = -75, -250, 1385
rotate = 0, 90, -45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S2_ind06
pos = -505, -120, 1385
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_02

[Object]
nickname = li_for_02_S2_ind07
pos = 95, -120, 1385
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_02

[Object]
nickname = li_for_02_S2_girder01
pos = -205, -120, 1385
rotate = 0, 90, 0
archetype = space_girder
parent = li_for_02

;SECTION 3

[Object]
nickname = li_for_02_S3_ind01
pos = -205, -120, 1135
rotate = 0, 0, 45
archetype = space_industriala
parent = li_for_02

[Object]
nickname = li_for_02_S3_ind02
pos = -335, 10, 1135
rotate = 45, 90, 0
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S3_ind03
pos = -75, 10, 1135
rotate = 0, 90, 45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S3_ind04
pos = -335, -250, 1135
rotate = 0, 90, 45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S3_ind05
pos = -75, -250, 1135
rotate = 0, 90, -45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S3_ind06
pos = -505, -120, 1135
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_02

[Object]
nickname = li_for_02_S3_ind07
pos = 95, -120, 1135
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_02

[Object]
nickname = li_for_02_S3_girder01
pos = -205, -120, 1135
rotate = 0, 90, 0
archetype = space_girder
parent = li_for_02

;SECTION 4

[Object]
nickname = li_for_02_S4_ind01
pos = -205, -120, 885
rotate = 0, 0, 45
archetype = space_industriala
parent = li_for_02

[Object]
nickname = li_for_02_S4_ind02
pos = -335, 10, 885
rotate = 45, 90, 0
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S4_ind03
pos = -75, 10, 885
rotate = 0, 90, 45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S4_ind04
pos = -335, -250, 885
rotate = 0, 90, 45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S4_ind05
pos = -75, -250, 885
rotate = 0, 90, -45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S4_ind06
pos = -505, -120, 885
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_02

[Object]
nickname = li_for_02_S4_ind07
pos = 95, -120, 885
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_02

[Object]
nickname = li_for_02_S4_girder01
pos = -205, -120, 885
rotate = 0, 90, 0
archetype = space_girder
parent = li_for_02

;SECTION 5

[Object]
nickname = li_for_02_S5_ind01
pos = -205, -120, 635
rotate = 0, 0, 45
archetype = space_industriala
parent = li_for_02

[Object]
nickname = li_for_02_S5_ind02
pos = -335, 10, 635
rotate = 45, 90, 0
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S5_ind03
pos = -75, 10, 635
rotate = 0, 90, 45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S5_ind04
pos = -335, -250, 635
rotate = 0, 90, 45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S5_ind05
pos = -75, -250, 635
rotate = 0, 90, -45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S5_ind06
pos = -505, -120, 635
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_02

[Object]
nickname = li_for_02_S5_ind07
pos = 95, -120, 635
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_02

[Object]
nickname = li_for_02_S5_girder01
pos = -205, -120, 635
rotate = 0, 90, 0
archetype = space_girder
parent = li_for_02

;SECTION 6

[Object]
nickname = li_for_02_S6_ind01
pos = -205, -120, 385
rotate = 0, 0, 45
archetype = space_industriala
parent = li_for_02

[Object]
nickname = li_for_02_S6_ind02
pos = -335, 10, 385
rotate = 45, 90, 0
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S6_ind03
pos = -75, 10, 385
rotate = 0, 90, 45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S6_ind04
pos = -335, -250, 385
rotate = 0, 90, 45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S6_ind05
pos = -75, -250, 385
rotate = 0, 90, -45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S6_ind06
pos = -505, -120, 385
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_02

[Object]
nickname = li_for_02_S6_ind07
pos = 95, -120, 385
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_02

[Object]
nickname = li_for_02_S6_girder01
pos = -205, -120, 385
rotate = 0, 90, 0
archetype = space_girder
parent = li_for_02

;CORE

[zone]
nickname = Zone_LI_FOR_03_inner_features
pos = -205, -120, -120
shape = BOX
size = 810, 450, 450
interference = 0.300000
drag_modifier = 3

[Object]
nickname = li_for_02_prison01
pos = -410, 0, 0
rotate = 0, 180, 0
archetype = space_prison_dummy
parent = li_for_02

[;Object] ;THIS IS ROOT
nickname = li_for_02_prison02
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = space_prison_dummy
parent = li_for_02

[Object]
nickname = li_for_02_prison03
pos = -410, -240, 0
rotate = 0, 180, 0
archetype = space_prison_dummy
parent = li_for_02

[Object]
nickname = li_for_02_prison04
pos = 0, -240, 0
rotate = 0, 0, 0
archetype = space_prison_dummy
parent = li_for_02

[Object]
nickname = li_for_02_prison05
pos = -410, 0, -240
rotate = 0, 180, 0
archetype = space_prison_dummy
parent = li_for_02

[Object]
nickname = li_for_02_prison06
pos = 0, 0, -240
rotate = 0, 0, 0
archetype = space_prison_dummy
parent = li_for_02

[Object]
nickname = li_for_02_prison07
pos = -410, -240, -240
rotate = 0, 180, 0
archetype = space_prison_dummy
parent = li_for_02

[Object]
nickname = li_for_02_prison08
pos = 0, -240, -240
rotate = 0, 0, 0
archetype = space_prison_dummy
parent = li_for_02

;TLR STORAGE SECTION

[Object]
nickname = li_for_02_TLR_cntrl_twr01
pos = 0, 120, -120
rotate = 0, 0, 0
archetype = space_control_tower
parent = li_for_02

[Object]
nickname = li_for_02_TLR_cntrl_twr02
pos = 0, 330, -120
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = li_for_02

[Object]
nickname = li_for_02_TLR_cntrl_block01
pos = 0, 370, -120
rotate = 0, 0, 0
archetype = space_small_control_block
parent = li_for_02

[Object]
nickname = li_for_02_TLR_tlrs01
pos = 0, 150, -220
rotate = 0, 45, 0
archetype = space_tlr_x5
parent = li_for_02

[Object]
nickname = li_for_02_TLR_tlrs02
pos = 0, 150, -20
rotate = 0, -135, 0
archetype = space_tlr_x5
parent = li_for_02

[Object]
nickname = li_for_02_TLR_tlrs03
pos = 100, 150, -120
rotate = 0, -45, 0
archetype = space_tlr_x5
parent = li_for_02

[Object]
nickname = li_for_02_TLR_tlrs04
pos = -100, 150, -120
rotate = 0, 135, 0
archetype = space_tlr_x5
parent = li_for_02

[Object]
nickname = li_for_02_TLR_tlrs05
pos = -115, 150, -218
rotate = 0, -90, 0
archetype = space_tlr_x5
parent = li_for_02

[Object]
nickname = li_for_02_TLR_tlrs06
pos = 85, 150, -223
rotate = 0, 180, 0
archetype = space_tlr_x5
parent = li_for_02

[Object]
nickname = li_for_02_TLR_tlrs07
pos = 105, 150, -33
rotate = 0, 90, 0
archetype = space_tlr_x5
parent = li_for_02

[Object]
nickname = li_for_02_TLR_tlrs08
pos = -85, 150, -18
rotate = 0, 0, 0
archetype = space_tlr_x5
parent = li_for_02

[Object]
nickname = li_for_02_TLR_girder01
pos = 0, -20, -120
rotate = -90, 0, 0
archetype = space_girdera
parent = li_for_02

;TOP SECTION

[Object]
nickname = li_for_02_HILL_cntrl_twr01
pos = -410, 120, -120
rotate = 0, 0, 0
archetype = space_control_tower
parent = li_for_02

[Object]
nickname = li_for_02_HILL_cntrl_twr02
pos = -410, 290, -120
rotate = 0, 0, 0
archetype = space_control_tower
parent = li_for_02

[Object]
nickname = li_for_02_HILL_cntrl_twr03
pos = -410, 205, -120
rotate = 0, 0, 0
archetype = space_control_tower
parent = li_for_02

[Object]
nickname = li_for_02_HILL_cntrl_twr04
pos = -410, 410, -120
rotate = 180, 0, 0
archetype = space_control_tower
parent = li_for_02

[Object]
nickname = li_for_02_HILL_dome01
pos = -410, 450, -120
rotate = 0, 0, 0
archetype = space_domea
parent = li_for_02

[Object]
nickname = li_for_02_HILL_habitat01
pos = -560, 205, -120
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_for_02

[Object]
nickname = li_for_02_HILL_habitat02
pos = -260, 205, -120
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_for_02

[Object]
nickname = li_for_02_HILL_habitat03
pos = -410, 205, -270
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_for_02

[Object]
nickname = li_for_02_HILL_habitat04
pos = -410, 205, 30
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_for_02

[Object]
nickname = li_for_02_HILL_habitat05
pos = -410, 205, -120
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_for_02

[Object]
nickname = li_for_02_HILL_habitat06
pos = -560, 350, -120
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_for_02

[Object]
nickname = li_for_02_HILL_habitat07
pos = -260, 350, -120
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_for_02

[Object]
nickname = li_for_02_HILL_habitat08
pos = -410, 350, -270
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_for_02

[Object]
nickname = li_for_02_HILL_habitat09
pos = -410, 350, 30
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_for_02

[Object]
nickname = li_for_02_HILL_habitat10
pos = -410, 350, -120
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = li_for_02

;FACTORY PRODUCTION

[Object]
nickname = li_for_02_PROD_tlr01
pos = -205, -20, -665
rotate = 0, -90, 0
archetype = space_co_tlr_dummy
loadout = large_co_tradelane_dummy_loadout
parent = li_for_02

[Object]
nickname = li_for_02_PROD_girder01
pos = -205, -20, -545
rotate = 0, 0, 0
archetype = space_girdera
parent = li_for_02

[Object]
nickname = li_for_02_PROD_girder02
pos = -205, -20, -515
rotate = 0, 40, 0
archetype = space_girdera
parent = li_for_02

[Object]
nickname = li_for_02_PROD_girder03
pos = -205, 80, -515
rotate = 0, -30, 0
archetype = space_girdera
parent = li_for_02

[Object]
nickname = li_for_02_PROD_girder04
pos = -205, -85, -545
rotate = 0, 10, 0
archetype = space_girdera
parent = li_for_02

[Object]
nickname = li_for_02_PROD_girder05
pos = 95, -220, -645
rotate = 0, -10, 0
archetype = space_girdera
parent = li_for_02

[Object]
nickname = li_for_02_PROD_girder06
pos = -405, -220, -645
rotate = 10, 0, 0
archetype = space_girdera
parent = li_for_02

;BOTTOM BLOCK

[Object]
nickname = li_for_02_STOR_shipyard01
pos = 0, -510, -115
rotate = 0, 180, 0
archetype = shipyard
parent = li_for_02

[Object]
nickname = li_for_02_STOR_shipyard02
pos = -410, -510, -115
rotate = 0, 0, 0
archetype = shipyard
parent = li_for_02
'''

class ForbesManufactoringOriginal(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_for_02'
    TEMPLATE = '''[Object]
nickname = li_for_02
pos = -205, -120, 0
rotate = 0, -90, 0
archetype = prison
{dock_props}

[Object]
nickname = li_for_02_tube01
pos = -335, 10, 1635
rotate = 0, 180, 0
archetype = space_short_tube
parent = li_for_02

[Object]
nickname = li_for_02_tube02
pos = -75, 10, 1635
rotate = 0, 180, 0
archetype = space_short_tube
parent = li_for_02

[Object]
nickname = li_for_02_tube03
pos = -335, 50, 1635
rotate = 0, 180, 0
archetype = space_short_tube
parent = li_for_02

[Object]
nickname = li_for_02_tube04
pos = -75, -250, 1635
rotate = 0, 180, 0
archetype = space_short_tube
parent = li_for_02

[Object]
nickname = li_for_02_prison01
pos = -205, -120, 440
rotate = 0, -90, 0
archetype = space_prison_dummy
parent = li_for_02

[Object]
nickname = li_for_02_prod01
pos = 110, -170, 600
rotate = 0, -90, 0
archetype = space_large_production
parent = li_for_02

[Object]
nickname = li_for_02_prod02
pos = 110, -170, 400
rotate = 0, -90, 0
archetype = space_large_production
parent = li_for_02

[Object]
nickname = li_for_02_prod03
pos = 110, -170, 200
rotate = 0, -90, 0
archetype = space_large_production
parent = li_for_02

[Object]
nickname = li_for_02_prod04
pos = 110, -170, 0
rotate = 0, -90, 0
archetype = space_large_production
parent = li_for_02

[Object]
nickname = li_for_02_prod01b
pos = -510, -170, 600
rotate = 0, 90, 0
archetype = space_large_production
parent = li_for_02

[Object]
nickname = li_for_02_prod02b
pos = -510, -170, 400
rotate = 0, 90, 0
archetype = space_large_production
parent = li_for_02

[Object]
nickname = li_for_02_prod03b
pos = -510, -170, 200
rotate = 0, 90, 0
archetype = space_large_production
parent = li_for_02

[Object]
nickname = li_for_02_prod04b
pos = -510, -170, 0
rotate = 0, 90, 0
archetype = space_large_production
parent = li_for_02

[Object]
nickname = li_for_02_S1_ind01
pos = -205, -120, 1635
rotate = 0, 0, 45
archetype = space_industriala
parent = li_for_02

[Object]
nickname = li_for_02_S1_ind02
pos = -335, 10, 1635
rotate = 45, 90, 0
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S1_ind03
pos = -75, 10, 1635
rotate = 0, 90, 45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S1_ind04
pos = -335, -250, 1635
rotate = 0, 90, 45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S1_ind05
pos = -75, -250, 1635
rotate = 0, 90, -45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S1_ind06
pos = -505, -120, 1635
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_02

[Object]
nickname = li_for_02_S1_ind07
pos = 95, -120, 1635
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_02

[Object]
nickname = li_for_02_S1_girder01
pos = -205, -120, 1635
rotate = 0, 90, 0
archetype = space_girder
parent = li_for_02

[Object]
nickname = li_for_02_S2_ind01
pos = -205, -120, 1385
rotate = 0, 0, 45
archetype = space_industriala
parent = li_for_02

[Object]
nickname = li_for_02_S2_ind02
pos = -335, 10, 1385
rotate = 45, 90, 0
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S2_ind03
pos = -75, 10, 1385
rotate = 0, 90, 45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S2_ind04
pos = -335, -250, 1385
rotate = 0, 90, 45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S2_ind05
pos = -75, -250, 1385
rotate = 0, 90, -45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S2_ind06
pos = -505, -120, 1385
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_02

[Object]
nickname = li_for_02_S2_ind07
pos = 95, -120, 1385
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_02

[Object]
nickname = li_for_02_S2_girder01
pos = -205, -120, 1385
rotate = 0, 90, 0
archetype = space_girder
parent = li_for_02

[Object]
nickname = li_for_02_S3_ind01
pos = -205, -120, 1135
rotate = 0, 0, 45
archetype = space_industriala
parent = li_for_02

[Object]
nickname = li_for_02_S3_ind02
pos = -335, 10, 1135
rotate = 45, 90, 0
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S3_ind03
pos = -75, 10, 1135
rotate = 0, 90, 45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S3_ind04
pos = -335, -250, 1135
rotate = 0, 90, 45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S3_ind05
pos = -75, -250, 1135
rotate = 0, 90, -45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S3_ind06
pos = -505, -120, 1135
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_02

[Object]
nickname = li_for_02_S3_ind07
pos = 95, -120, 1135
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_02

[Object]
nickname = li_for_02_S3_girder01
pos = -205, -120, 1135
rotate = 0, 90, 0
archetype = space_girder
parent = li_for_02

[Object]
nickname = li_for_02_S4_ind01
pos = -205, -120, 885
rotate = 0, 0, 45
archetype = space_industriala
parent = li_for_02

[Object]
nickname = li_for_02_S4_ind01b
pos = -205, -120, 631
rotate = 0, 0, 45
archetype = space_industrialc
parent = li_for_02

[Object]
nickname = li_for_02_S4_ind02
pos = -335, 10, 885
rotate = 45, 90, 0
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S4_ind03
pos = -75, 10, 885
rotate = 0, 90, 45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S4_ind04
pos = -335, -250, 885
rotate = 0, 90, 45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S4_ind05
pos = -75, -250, 885
rotate = 0, 90, -45
archetype = space_industrial02a
parent = li_for_02

[Object]
nickname = li_for_02_S4_ind06
pos = -505, -120, 885
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_02

[Object]
nickname = li_for_02_S4_ind07
pos = 95, -120, 885
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_for_02

[Object]
nickname = li_for_02_S4_girder01
pos = -205, -120, 885
rotate = 0, 90, 0
archetype = space_girder
parent = li_for_02
'''


class ForbesMegafactory(ForbesMegafactoryOriginal):
    TEMPLATE = '''[Object]
nickname = li_for_02
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = prison_detroit
{dock_props}

[Object]
nickname = li_for_02_tube01
pos = -205, -100, 1635
rotate = 0, 0, 0
archetype = forbes_mega_tubes
parent = li_for_02

[Object]
nickname = li_for_02_S1_ind01
pos = -205, -120, 1635
rotate = 0, 0, 0
archetype = forbes_mega_s1
parent = li_for_02

[Object]
nickname = li_for_02_S2_ind01
pos = -205, -120, 1385
rotate = 0, 0, 0
archetype = forbes_mega_s2
parent = li_for_02

[Object]
nickname = li_for_02_S3_ind01
pos = -205, -120, 1135
rotate = 0, 0, 0
archetype = forbes_mega_s3
parent = li_for_02

[Object]
nickname = li_for_02_S4_ind01
pos = -205, -120, 885
rotate = 0, 0, 0
archetype = forbes_mega_s4
parent = li_for_02

[Object]
nickname = li_for_02_S5_ind01
pos = -205, -120, 635
rotate = 0, 0, 0
archetype = forbes_mega_s5
parent = li_for_02

[Object]
nickname = li_for_02_S6_ind01
pos = -205, -120, 385
rotate = 0, 0, 0
archetype = forbes_mega_s6
parent = li_for_02

[zone]
nickname = Zone_LI_FOR_03_inner_features
pos = -205, -120, -120
shape = BOX
size = 810, 450, 450
interference = 0.300000
drag_modifier = 3

[Object]
nickname = li_for_02_prison01
pos = -205, -120, -120
rotate = 0, 0, 0
archetype = forbes_mega_core
parent = li_for_02

[;Object] ;THIS IS ROOT
nickname = li_for_02_prison02
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = space_prison_dummy
parent = li_for_02

[Object]
nickname = li_for_02_TLR_cntrl_twr01
pos = -5, 175, -120.5
rotate = 0, 0, 0
archetype = forbes_mega_tlr
parent = li_for_02

[Object]
nickname = li_for_02_HILL_cntrl_twr01
pos = -410, 285, -120
rotate = 0, 0, 0
archetype = forbes_mega_hill
parent = li_for_02

[Object]
nickname = li_for_02_PROD_tlr01
pos = -205, -20, -665
rotate = 0, -90, 0
archetype = space_co_tlr_dummy
loadout = large_co_tradelane_dummy_loadout
parent = li_for_02

[Object]
nickname = li_for_02_PROD_girder01
pos = -155, -70, -580
rotate = 0, 0, 0
archetype = forbes_mega_prod
parent = li_for_02

[Object]
nickname = li_for_02_STOR_shipyard01
pos = -205, -510, -115
rotate = 0, 0, 0
archetype = forbes_mega_stor
parent = li_for_02



[Object]
nickname = li_for_02_forbes_mega_tubes_collision00
pos = -204.97855, -99.9869404, 855.367246
rotate = 0, 0, 0
archetype = forbes_mega_tubes_collision00
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_s1_collision00
pos = -205.305969, -120.059889, 1636.76408
rotate = 0, 0, 0
archetype = forbes_mega_s1_collision00
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_s1_collision01
pos = -205.173996, -119.950642, 1635.18249
rotate = 0, 0, 0
archetype = forbes_mega_s1_collision01
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_s2_collision00
pos = -205.305969, -120.059889, 1386.76408
rotate = 0, 0, 0
archetype = forbes_mega_s2_collision00
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_s2_collision01
pos = -205.173996, -119.950642, 1385.18249
rotate = 0, 0, 0
archetype = forbes_mega_s2_collision01
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_s3_collision00
pos = -205.305969, -120.059889, 1136.76408
rotate = 0, 0, 0
archetype = forbes_mega_s3_collision00
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_s3_collision01
pos = -205.173996, -119.950642, 1135.18249
rotate = 0, 0, 0
archetype = forbes_mega_s3_collision01
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_s4_collision00
pos = -205.305969, -120.059889, 886.764076
rotate = 0, 0, 0
archetype = forbes_mega_s4_collision00
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_s4_collision01
pos = -205.173996, -119.950642, 885.182491
rotate = 0, 0, 0
archetype = forbes_mega_s4_collision01
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_s5_collision00
pos = -205.305969, -120.059889, 636.764076
rotate = 0, 0, 0
archetype = forbes_mega_s5_collision00
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_s5_collision01
pos = -205.173996, -119.950642, 635.182491
rotate = 0, 0, 0
archetype = forbes_mega_s5_collision01
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_s6_collision00
pos = -205.305969, -120.059889, 386.764076
rotate = 0, 0, 0
archetype = forbes_mega_s6_collision00
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_s6_collision01
pos = -205.173996, -119.950642, 385.182491
rotate = 0, 0, 0
archetype = forbes_mega_s6_collision01
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_core_collision00
pos = -413.56595, 3.81469727e-05, -7.60493818e-06
rotate = 0, 0, 0
archetype = forbes_mega_core_collision00
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_core_collision01
pos = -413.56595, -239.999962, -7.60493818e-06
rotate = 0, 0, 0
archetype = forbes_mega_core_collision01
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_core_collision02
pos = 3.56595612, -239.999962, 7.62939453e-06
rotate = 0, 0, 0
archetype = forbes_mega_core_collision02
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_core_collision03
pos = -413.56595, 3.81469727e-05, -240.000008
rotate = 0, 0, 0
archetype = forbes_mega_core_collision03
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_core_collision04
pos = 3.56595612, 3.81469727e-05, -239.999992
rotate = 0, 0, 0
archetype = forbes_mega_core_collision04
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_core_collision05
pos = -413.56595, -239.999962, -240.000008
rotate = 0, 0, 0
archetype = forbes_mega_core_collision05
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_core_collision06
pos = 3.56595612, -239.999962, -239.999992
rotate = 0, 0, 0
archetype = forbes_mega_core_collision06
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_tlr_collision00
pos = -0.0679779053, 224.850012, -119.985695
rotate = 0, 0, 0
archetype = forbes_mega_tlr_collision00
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_tlr_collision01
pos = 0.0692892075, 420.981647, -120.065029
rotate = 0, 0, 0
archetype = forbes_mega_tlr_collision01
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_tlr_collision02
pos = -5.69928034, 217.900014, -201.475475
rotate = 0, 0, 0
archetype = forbes_mega_tlr_collision02
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_tlr_collision03
pos = 5.6992801, 217.900014, -38.5245253
rotate = 0, 0, 0
archetype = forbes_mega_tlr_collision03
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_tlr_collision04
pos = 81.4754748, 217.900014, -125.69928
rotate = 0, 0, 0
archetype = forbes_mega_tlr_collision04
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_tlr_collision05
pos = -81.475475, 217.900014, -114.30072
rotate = 0, 0, 0
archetype = forbes_mega_tlr_collision05
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_tlr_collision06
pos = -112.607894, 217.900014, -223.610947
rotate = 0, 0, 0
archetype = forbes_mega_tlr_collision06
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_tlr_collision07
pos = 90.6109461, 217.900014, -220.607886
rotate = 0, 0, 0
archetype = forbes_mega_tlr_collision07
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_tlr_collision08
pos = 102.607889, 217.900014, -27.3890536
rotate = 0, 0, 0
archetype = forbes_mega_tlr_collision08
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_tlr_collision09
pos = -68.7206497, 155.514184, -46.822472
rotate = 0, 0, 0
archetype = forbes_mega_tlr_collision09
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_hill_collision00
pos = -410.067978, 204.850013, -119.985695
rotate = 0, 0, 0
archetype = forbes_mega_hill_collision00
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_hill_collision01
pos = -410.067978, 307.500001, -120.000001
rotate = 0, 0, 0
archetype = forbes_mega_hill_collision01
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_hill_collision02
pos = -410.06718, 321.649456, -119.908031
rotate = 0, 0, 0
archetype = forbes_mega_hill_collision02
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_prod_collision00
pos = -155.267548, -100.416305, -420.22816
rotate = 0, 0, 0
archetype = forbes_mega_prod_collision00
parent = li_for_02

[Object]
nickname = li_for_02_forbes_mega_stor_collision00
pos = -204.999983, -478.786308, -115.000005
rotate = 0, 0, 0
archetype = forbes_mega_stor_collision00
parent = li_for_02

'''


class ForbesManufactoring(ForbesManufactoringOriginal):
    TEMPLATE = '''[Object]
nickname = li_for_02
pos = -205, -120, 0
rotate = 0, -90, 0
archetype = prison
{dock_props}

[Object]
nickname = li_for_02_tube01
pos = -205, -100, 1037.5
rotate = 0, 0, 0
archetype = batch_forbes_ma_018e8df6_structure0
parent = li_for_02

[Object]
nickname = li_for_02_prod01
pos = 110, -170, 600
rotate = 0, -90, 0
archetype = space_large_production
parent = li_for_02

[Object]
nickname = li_for_02_prod02
pos = 110, -170, 400
rotate = 0, -90, 0
archetype = space_large_production
parent = li_for_02

[Object]
nickname = li_for_02_prod03
pos = 110, -170, 200
rotate = 0, -90, 0
archetype = space_large_production
parent = li_for_02

[Object]
nickname = li_for_02_prod04
pos = 110, -170, 0
rotate = 0, -90, 0
archetype = space_large_production
parent = li_for_02

[Object]
nickname = li_for_02_prod01b
pos = -510, -170, 600
rotate = 0, 90, 0
archetype = space_large_production
parent = li_for_02

[Object]
nickname = li_for_02_prod02b
pos = -510, -170, 400
rotate = 0, 90, 0
archetype = space_large_production
parent = li_for_02

[Object]
nickname = li_for_02_prod03b
pos = -510, -170, 200
rotate = 0, 90, 0
archetype = space_large_production
parent = li_for_02

[Object]
nickname = li_for_02_prod04b
pos = -510, -170, 0
rotate = 0, 90, 0
archetype = space_large_production
parent = li_for_02

[Object]
nickname = li_for_02_S1_ind01
pos = -205, -120, 1635
rotate = 0, 0, 0
archetype = batch_forbes_ma_018e8df6_s10
parent = li_for_02

[Object]
nickname = li_for_02_S2_ind01
pos = -205, -120, 1385
rotate = 0, 0, 0
archetype = batch_forbes_ma_018e8df6_s20
parent = li_for_02

[Object]
nickname = li_for_02_S3_ind01
pos = -205, -120, 1135
rotate = 0, 0, 0
archetype = batch_forbes_ma_018e8df6_s30
parent = li_for_02

[Object]
nickname = li_for_02_S4_ind01
pos = -205, -120, 758
rotate = 0, 0, 0
archetype = batch_forbes_ma_018e8df6_s40
parent = li_for_02



[Object]
nickname = li_for_02_batch_forbes_ma_018e8df6_structure0_collision00
pos = -205.000008, -102.296579, 921.838116
rotate = 0, 0, 0
archetype = batch_forbes_ma_018e8df6_structure0_collision00
parent = li_for_02

[Object]
nickname = li_for_02_batch_forbes_ma_018e8df6_s10_collision00
pos = -205.305969, -120.059889, 1636.76408
rotate = 0, 0, 0
archetype = batch_forbes_ma_018e8df6_s10_collision00
parent = li_for_02

[Object]
nickname = li_for_02_batch_forbes_ma_018e8df6_s10_collision01
pos = -205.173996, -119.950642, 1635.18249
rotate = 0, 0, 0
archetype = batch_forbes_ma_018e8df6_s10_collision01
parent = li_for_02

[Object]
nickname = li_for_02_batch_forbes_ma_018e8df6_s20_collision00
pos = -205.305969, -120.059889, 1386.76408
rotate = 0, 0, 0
archetype = batch_forbes_ma_018e8df6_s20_collision00
parent = li_for_02

[Object]
nickname = li_for_02_batch_forbes_ma_018e8df6_s20_collision01
pos = -205.173996, -119.950642, 1385.18249
rotate = 0, 0, 0
archetype = batch_forbes_ma_018e8df6_s20_collision01
parent = li_for_02

[Object]
nickname = li_for_02_batch_forbes_ma_018e8df6_s30_collision00
pos = -205.305969, -120.059889, 1136.76408
rotate = 0, 0, 0
archetype = batch_forbes_ma_018e8df6_s30_collision00
parent = li_for_02

[Object]
nickname = li_for_02_batch_forbes_ma_018e8df6_s30_collision01
pos = -205.173996, -119.950642, 1135.18249
rotate = 0, 0, 0
archetype = batch_forbes_ma_018e8df6_s30_collision01
parent = li_for_02

[Object]
nickname = li_for_02_batch_forbes_ma_018e8df6_s40_collision00
pos = -205.305969, -120.059889, 821.640717
rotate = 0, 0, 0
archetype = batch_forbes_ma_018e8df6_s40_collision00
parent = li_for_02

[Object]
nickname = li_for_02_batch_forbes_ma_018e8df6_s40_collision01
pos = -205.173996, -191.550847, 885.182491
rotate = 0, 0, 0
archetype = batch_forbes_ma_018e8df6_s40_collision01
parent = li_for_02

'''
