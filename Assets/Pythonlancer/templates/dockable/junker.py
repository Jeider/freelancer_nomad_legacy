from templates.space_object_template import SpaceObjectTemplate


class HonshuJunker(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_hns_04'
    TEMPLATE = '''[Object]
nickname = ku_hns_04
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = space_police01
{dock_props}

[Object]
nickname = ku_hns_04_industrial01
pos = 0, 210, 0
rotate = 90, 0, 0
archetype = space_industrial02a
parent = ku_hns_04

[Object]
nickname = ku_hns_04_industrial02
pos = 0, 210, 190
rotate = 0, 0, 45
archetype = space_industriala
parent = ku_hns_04

[Object]
nickname = ku_hns_04_industrial03
pos = 0, 210, -190
rotate = 0, 0, 45
archetype = space_industriala
parent = ku_hns_04

[Object]
nickname = ku_hns_04_industrial04
pos = -140, 200, 0
rotate = 0, 90, 30
archetype = space_industriala
parent = ku_hns_04

[Object]
nickname = ku_hns_04_industrial05
pos = 140, 200, 0
rotate = 0, 90, -30
archetype = space_industrial_dmg
parent = ku_hns_04

[Object]
nickname = ku_hns_04_tanks01
pos = -50, 160, -180
rotate = 0, 0, -90
archetype = space_tankl4
parent = ku_hns_04

[Object]
nickname = ku_hns_04_tanks02
pos = 50, 160, -180
rotate = 0, 0, 90
archetype = space_tankl4
parent = ku_hns_04

[Object]
nickname = ku_hns_04_tanks03
pos = -50, 160, 190
rotate = 0, 0, -90
archetype = space_tankl4
parent = ku_hns_04

[Object]
nickname = ku_hns_04_tanks04
pos = 50, 160, 190
rotate = 0, 0, 90
archetype = space_tankl4
parent = ku_hns_04

[Object]
nickname = ku_hns_04_panel01
pos = 110, 225, -180
rotate = 0, 180, 15
archetype = space_debris_panel
parent = ku_hns_04

[Object]
nickname = ku_hns_04_panel02
pos = -110, 225, -180
rotate = 0, 0, -15
archetype = space_debris_panel
parent = ku_hns_04

[Object]
nickname = ku_hns_04_panel03
pos = 110, 225, 180
rotate = 0, 180, 15
archetype = space_debris_panel
parent = ku_hns_04

[Object]
nickname = ku_hns_04_panel04
pos = -110, 225, 180
rotate = 0, 0, -15
archetype = space_debris_panel
parent = ku_hns_04

[Object]
nickname = ku_hns_04_tower01
pos = 0, 360, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = ku_hns_04

[Object]
nickname = ku_hns_04_control01
pos = 0, 425, 0
rotate = 0, 0, 0
archetype = space_pirate_control_block
parent = ku_hns_04
'''


class SigmaEightJunker(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'sig8_02'
    TEMPLATE = '''[Object]
nickname = sig8_02
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_port_dmg_production
{dock_props}

[Object]
nickname = sig8_02_space_girder01
pos = 0, 0, 150
rotate = 0, 0, 0
archetype = space_girder
parent = sig8_02

[Object]
nickname = sig8_02_space_girder02
pos = 0, 0, -150
rotate = 0, 0, 0
archetype = space_girder
parent = sig8_02

[Object]
nickname = sig8_02_space_dome01
pos = 0, 0, -350
rotate = 0, 0, 0
archetype = space_domea
parent = sig8_02

[Object]
nickname = sig8_02_space_habitat01
pos = 0, -10, -420
rotate = 0, 22, 90
archetype = space_habitat_wide
parent = sig8_02

[Object]
nickname = sig8_02_space_habitat02
pos = 60, -10, -320
rotate = 70, 0, 90
archetype = space_habitat_wide
parent = sig8_02

[Object]
nickname = sig8_02_space_habitat03
pos = -60, -10, -320
rotate = -70, 0, 90
archetype = space_habitat_wide
parent = sig8_02

[Object]
nickname = sig8_02_space_industrial01
pos = 0, 0, 350
rotate = 0, 0, 0
archetype = space_industriala
parent = sig8_02

[Object]
nickname = sig8_02_space_tanks01
pos = 0, 130, 350
rotate = 90, 0, 0
archetype = space_tanks4x4
parent = sig8_02

[Object]
nickname = sig8_02_space_tanks02
pos = 0, -130, 350
rotate = 90, 0, 0
archetype = space_tanks4x4
parent = sig8_02

[Object]
nickname = sig8_02_space_tanks03
pos = 130, 0, 350
rotate = 90, 0, 90
archetype = space_tanks4x4
parent = sig8_02

[Object]
nickname = sig8_02_space_tanks04
pos = -130, 0, 350
rotate = 90, 0, 90
archetype = space_tanks4x4
parent = sig8_02

[Object]
nickname = sig8_02_space_tanks05
pos = 85, 85, 350
rotate = 90, 0, -45
archetype = space_tanks4x4
parent = sig8_02

[Object]
nickname = sig8_02_space_tanks06
pos = 85, -85, 350
rotate = 90, 0, 45
archetype = space_tanks4x4
parent = sig8_02

[Object]
nickname = sig8_02_space_tanks07
pos = -85, 85, 350
rotate = 90, 0, 45
archetype = space_tanks4x4
parent = sig8_02

[Object]
nickname = sig8_02_space_tanks08
pos = -85, -85, 350
rotate = 90, 0, -45
archetype = space_tanks4x4
parent = sig8_02
'''


class StuttgartJunker(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_stut_05'
    TEMPLATE = '''[Object]
nickname = rh_stut_05
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_port_dmg_front_dock
{dock_props}

[Object]
nickname = rh_stut_05_ind01
pos = 0, 0, -200
rotate = 0, 0, 0
archetype = space_industriala
parent = Rh_stut_05

[Object]
nickname = rh_stut_05_ind02
pos = 0, 0, -470
rotate = 0, 0, 0
archetype = space_industriala
parent = Rh_stut_05

[Object]
nickname = rh_stut_05_ind03
pos = 110, 0, 0
rotate = 0, 90, 0
archetype = space_industrial01b
parent = Rh_stut_05

[Object]
nickname = rh_stut_05_ind04
pos = 285, 0, 0
rotate = 0, 90, 0
archetype = space_industriala
parent = Rh_stut_05

[Object]
nickname = rh_stut_05_ind05
pos = 285, 0, -300
rotate = 0, 0, 0
archetype = space_industrial_dmg
parent = Rh_stut_05

[Object]
nickname = rh_stut_05_tanks01
pos = 75, 0, -200
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = Rh_stut_05

[Object]
nickname = rh_stut_05_tanks02
pos = 75, 0, -470
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = Rh_stut_05

[Object]
nickname = rh_stut_05_tanks03
pos = 580, 0, -100
rotate = 30, 120, 30
archetype = space_tankl4x4_dmg
parent = Rh_stut_05

[Object]
nickname = rh_stut_05_habitat01
pos = 0, -110, -470
rotate = 180, 0, 0
archetype = space_small_control_block
parent = Rh_stut_05

[Object]
nickname = rh_stut_05_habitat02
pos = 0, -80, -200
rotate = 180, 0, 0
archetype = space_habitat_dmg
parent = Rh_stut_05

[Object]
nickname = rh_stut_05_habitat03
pos = 285, -105, 0
rotate = 0, 0, 0
archetype = space_habitat_dmg
parent = Rh_stut_05

[Object]
nickname = rh_stut_05_habitat04
pos = 285, 100, 0
rotate = 0, 0, 0
archetype = space_habitat_dmg
parent = Rh_stut_05

[Object]
nickname = rh_stut_05_panel01
pos = 180, 40, 40
rotate = 0, 90, 0
archetype = space_panel45
parent = Rh_stut_05

[Object]
nickname = rh_stut_05_panel02
pos = 390, 40, 40
rotate = 0, 90, 0
archetype = space_panel45
parent = Rh_stut_05

[Object]
nickname = rh_stut_05_panel03
pos = -40, -40, -335
rotate = 180, 0, 0
archetype = space_panel45
parent = Rh_stut_05

[Object]
nickname = rh_stut_05_debris01
pos = -10, 80, -470
rotate = 0, 0, 0
archetype = space_debris_panel
parent = Rh_stut_05

[Object]
nickname = rh_stut_05_debris02
pos = -10, 80, -200
rotate = 0, 0, 0
archetype = space_debris_panel
parent = Rh_stut_05

[Object]
nickname = rh_stut_05_girder01
pos = 0, 0, -350
rotate = 0, 0, 0
archetype = space_girderc
parent = Rh_stut_05

[Object]
nickname = rh_stut_05_girder02
pos = 500, 0, 0
rotate = -1, 88, 0
archetype = space_beaml_dmg
parent = Rh_stut_05
'''


class BerlinJunker(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_ber_08'
    TEMPLATE = '''[Object]
nickname = rh_ber_08
pos = 0, 0, 0
rotate = 0, 180, 0
archetype = space_port_dmg_front_dock
{dock_props}

[Object]
nickname = rh_ber_08_girder01
pos = 0, -44, 816
rotate = 90, 0, 0
archetype = space_girderc
parent = rh_ber_08

[Object]
nickname = rh_ber_08_debris_panel01
pos = -50, -100, 253
rotate = 0, 0, 45
archetype = space_debris_panel
parent = rh_ber_08

[Object]
nickname = rh_ber_08_debris_panel02
pos = 50, -150, 303
rotate = 0, 0, -135
archetype = space_debris_panel
parent = rh_ber_08

[Object]
nickname = rh_ber_08_debris_panel03
pos = -50, -120, 493
rotate = 0, 0, 45
archetype = space_debris_panel
parent = rh_ber_08

[Object]
nickname = rh_ber_08_debris_panel04
pos = 50, -100, 553
rotate = 0, 0, -135
archetype = space_debris_panel
parent = rh_ber_08

[Object]
nickname = rh_ber_08_industrial01
pos = 0, 15, 273
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_ber_08

[Object]
nickname = rh_ber_08_industrial02
pos = 0, -90, 273
rotate = 0, 0, 90
archetype = space_industrial02d
parent = rh_ber_08

[Object]
nickname = rh_ber_08_industrial03
pos = 0, 15, 523
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_ber_08

[Object]
nickname = rh_ber_08_industrial04
pos = 0, -90, 523
rotate = 0, 0, 90
archetype = space_industrial02d
parent = rh_ber_08

[Object]
nickname = rh_ber_08_industrial05
pos = 0, 0, 816
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_ber_08

[Object]
nickname = rh_ber_08_industrial06
pos = 0, 5, 133
rotate = -15, 0, 0
archetype = space_industrial01d
parent = rh_ber_08

[Object]
nickname = rh_ber_08_industrial07
pos = 0, 5, 673
rotate = 15, 0, 0
archetype = space_industrial01d
parent = rh_ber_08

[Object]
nickname = rh_ber_08_industrial08
pos = 0, 15, 348
rotate = 0, 0, 0
archetype = space_industrial01d
parent = rh_ber_08

[Object]
nickname = rh_ber_08_tank01
pos = 0, -150, 263
rotate = 0, 0, 0
archetype = space_tankl4
parent = rh_ber_08

[Object]
nickname = rh_ber_08_tank02
pos = 0, -150, 528
rotate = 0, 0, 0
archetype = space_tankl4
parent = rh_ber_08

[Object]
nickname = rh_ber_08_tank03
pos = 0, -220, 816
rotate = 0, 0, 0
archetype = space_tankl2
parent = rh_ber_08

[Object]
nickname = rh_ber_08_habitat01
pos = 0, 129, 743
rotate = 0, 90, 0
archetype = space_habitat_tall
parent = rh_ber_08

[Object]
nickname = rh_ber_08_habitat02
pos = 0, 68, 743
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_ber_08

[Object]
nickname = rh_ber_08_habitat03
pos = 0, 166, 816
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = rh_ber_08

[Object]
nickname = rh_ber_08_habitat04
pos = 0, 94, 893
rotate = 0, 0, 0
archetype = space_small_control_block
parent = rh_ber_08

[Object]
nickname = rh_ber_08_panel01
pos = -46, 70, 198
rotate = 0, 0, -20
archetype = space_panel
parent = rh_ber_08

[Object]
nickname = rh_ber_08_panel02
pos = 46, 70, 198
rotate = 0, 0, 20
archetype = space_panel
parent = rh_ber_08

[Object]
nickname = rh_ber_08_panel03
pos = -35, 100, 398
rotate = 0, 0, -20
archetype = space_panel
parent = rh_ber_08

[Object]
nickname = rh_ber_08_panel04
pos = 35, 100, 398
rotate = 0, 0, 20
archetype = space_panel
parent = rh_ber_08

[Object]
nickname = rh_ber_08_panel05
pos = -46, 70, 598
rotate = 0, 0, -20
archetype = space_panel
parent = rh_ber_08

[Object]
nickname = rh_ber_08_panel06
pos = 46, 70, 598
rotate = 0, 0, 20
archetype = space_panel
parent = rh_ber_08
'''


class OmegaSmelter(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'om15_03'
    TEMPLATE = '''[Object]
nickname = om15_03
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_port_dmg
{dock_props}

[Object]
nickname = om15_03_mplatform
pos = -230, -25, 0
rotate = 0, 90, 0
archetype = mplatform_satellite
parent = om15_03

[Object]
nickname = om15_03_tanks01
pos = -160, 22, -80
rotate = 0, 45, 0
archetype = space_tanks2x2
parent = om15_03

[Object]
nickname = om15_03_tanks02
pos = -220, 22, -80
rotate = 0, -45, 0
archetype = space_tanks2x2
parent = om15_03

[Object]
nickname = om15_03_panel01
pos = 40, 0, 0
rotate = 90, 90, 0
archetype = space_solar_pnl
parent = om15_03
'''


class ForbesJunker(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_for_06'
    TEMPLATE = '''[Object]
nickname = li_for_06
pos = 0, 0, 0
rotate = 0, 90, 0
archetype = space_port_dmg
{dock_props}

[Object]
nickname = li_for_06_industrial01
pos = 0, -300, 0
rotate = 90, 45, 90
archetype = space_industrial02a
parent = li_for_06

[Object]
nickname = li_for_06_industrial02
pos = 0, -450, 0
rotate = 90, 90, 90
archetype = space_industrial02d
parent = li_for_06

[Object]
nickname = li_for_06_industrial03
pos = 0, -390, -90
rotate = 90, -45, 90
archetype = space_industrial02a
parent = li_for_06

[Object]
nickname = li_for_06_industrial04
pos = 0, -390, 90
rotate = 90, 45, 90
archetype = space_industrial02a
parent = li_for_06

[Object]
nickname = li_for_06_girder01
pos = 0, -380, 0
rotate = -90, 0, 0
archetype = space_girderc
parent = li_for_06

[Object]
nickname = li_for_06_tank01
pos = 0, -490, 0
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_for_06

[Object]
nickname = li_for_06_tank02
pos = 0, -450, 80
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_for_06

[Object]
nickname = li_for_06_tank03
pos = 0, -450, -80
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_for_06

[Object]
nickname = li_for_06_tank04
pos = 0, -410, 150
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_for_06

[Object]
nickname = li_for_06_tank05
pos = 0, -410, -150
rotate = 0, 90, 0
archetype = space_tankl4
parent = li_for_06

[Object]
nickname = li_for_06_panel01
pos = 0, -320, 120
rotate = 0, 90, 0
archetype = space_debris_panel
parent = li_for_06

[Object]
nickname = li_for_06_panel02
pos = 0, -320, -125
rotate = 0, -90, 0
archetype = space_debris_panel
parent = li_for_06
'''
