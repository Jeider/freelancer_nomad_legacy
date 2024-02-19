from templates.space_object_template import SpaceObjectTemplate


# NEED A DOCK
class SphereMegabase(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'sph_base01'
    TEMPLATE = '''[Object]
nickname = sph_base01
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_industriala
{root_props}

[Object]
nickname = sph_base01_control_twr01
pos = 0, 125, 0
rotate = 180, 0, 0
archetype = space_control_tower
parent = sph_base01

[Object]
nickname = sph_base01_control_twr02
pos = 0, 40, 0
rotate = 0, 7.5, 0
archetype = space_control_tower
parent = sph_base01

[Object]
nickname = sph_base01_control_twr03
pos = 0, -40, 0
rotate = 0, 6, 0
archetype = space_control_tower
parent = sph_base01

[Object]
nickname = sph_base01_control_twr04
pos = 0, -125, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = sph_base01

[Object]
nickname = sph_base01_control_twr05
pos = 0, 325, 0
rotate = -180, 45, 0
archetype = space_control_tower
parent = sph_base01

[Object]
nickname = sph_base01_control_twr06
pos = 0, 630, 0
rotate = -180, 45, 0
archetype = space_medium_control_tower
parent = sph_base01

[Object]
nickname = sph_base01_control_twr07
pos = 0, 930, 0
rotate = -180, 45, 0
archetype = space_medium_control_tower
parent = sph_base01

[Object]
nickname = sph_base01_control_twr08
pos = 0, 1120, 0
rotate = -180, 45, 0
archetype = space_control_tower
parent = sph_base01

[Object]
nickname = sph_base01_control_twr09
pos = 0, 1300, 0
rotate = -180, 0, 0
archetype = space_small_control_tower
parent = sph_base01

[Object]
nickname = sph_base01_control_twr10
pos = 0, 1620, 0
rotate = -180, 0, 0
archetype = space_small_control_tower
parent = sph_base01

[Object]
nickname = sph_base01_prison01
pos = 600, 0, 155
rotate = 0, 180, 0
archetype = space_prison
parent = sph_base01

[Object]
nickname = sph_base01_prison02
pos = 600, 0, -155
rotate = 0, 180, 0
archetype = space_prison
parent = sph_base01

[Object]
nickname = sph_base01_prison03
pos = -600, 0, 155
rotate = 0, 0, 0
archetype = space_prison
parent = sph_base01

[Object]
nickname = sph_base01_prison04
pos = -600, 0, -155
rotate = 0, 0, 0
archetype = space_prison
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris01
pos = 275, 60, 70
rotate = 0, 80, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris02
pos = 275, -60, 70
rotate = 0, 80, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris03
pos = 335, 0, 215
rotate = 90, 0, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris04
pos = 175, 60, 185
rotate = 0, 75, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris05
pos = 175, -60, 185
rotate = 0, 75, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris06
pos = -275, 60, 70
rotate = 0, -80, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris07
pos = -275, -60, 70
rotate = 0, -80, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris08
pos = -335, 0, 215
rotate = 90, 0, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris09
pos = -175, 60, 185
rotate = 0, -75, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris10
pos = -175, -60, 185
rotate = 0, -75, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris11
pos = 275, 60, -70
rotate = 0, -80, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris12
pos = 275, -60, -70
rotate = 0, -80, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris13
pos = 335, 0, -215
rotate = 90, 0, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris14
pos = 175, 60, -185
rotate = 0, -75, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris15
pos = 175, -60, -185
rotate = 0, -75, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris16
pos = -275, 60, -70
rotate = 0, 80, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris17
pos = -275, -60, -70
rotate = 0, 80, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris18
pos = -335, 0, -215
rotate = 90, 0, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris19
pos = -175, 60, -185
rotate = 0, 75, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris20
pos = -175, -60, -185
rotate = 0, 75, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core01
pos = 0, 0, 180
rotate = 90, 0, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core02
pos = 180, 0, 0
rotate = 90, 90, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core03
pos = -180, 0, 0
rotate = 90, 90, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core04
pos = 0, 0, -180
rotate = 90, 0, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core05
pos = 90, 0, 155
rotate = 90, 30, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core06
pos = 155, 0, 90
rotate = 90, 60, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core07
pos = -90, 0, 155
rotate = 90, -30, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core08
pos = -155, 0, 90
rotate = 90, -60, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core09
pos = 90, 0, -155
rotate = 90, -30, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core10
pos = 155, 0, -90
rotate = 90, -60, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core11
pos = -90, 0, -155
rotate = 90, 30, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core12
pos = -155, 0, -90
rotate = 90, 60, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_shipyard01
pos = 0, 0, 600
rotate = 180, 90, 0
archetype = shipyard_2x
parent = sph_base01

[Object]
nickname = sph_base01_shipyard02
pos = 0, 0, -600
rotate = 180, 90, 0
archetype = shipyard_2x
parent = sph_base01

[Object]
nickname = sph_base01_shipyard03
pos = 0, -50, 1150
rotate = 180, 90, 0
archetype = shipyard
parent = sph_base01

[Object]
nickname = sph_base01_shipyard04
pos = 0, -50, 1550
rotate = 180, 90, 0
archetype = shipyard
parent = sph_base01

[Object]
nickname = sph_base01_shipyard05
pos = 0, -50, -1150
rotate = 180, 90, 0
archetype = shipyard
parent = sph_base01

[Object]
nickname = sph_base01_shipyard06
pos = 0, -50, -1550
rotate = 180, 90, 0
archetype = shipyard
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect01
pos = 100, 250, 110
rotate = 0, 0, 0
archetype = space_industriala
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect02
pos = 100, 250, -110
rotate = 0, 0, 0
archetype = space_industriala
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect03
pos = -100, 250, 110
rotate = 0, 0, 0
archetype = space_industriala
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect04
pos = -100, 250, -110
rotate = 0, 0, 0
archetype = space_industriala
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect05
pos = 100, 100, 110
rotate = -90, 45, 0
archetype = space_industrialc
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect06
pos = 100, 100, -110
rotate = -90, 45, 0
archetype = space_industrialc
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect07
pos = -100, 100, 110
rotate = -90, 45, 0
archetype = space_industrialc
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect08
pos = -100, 100, -110
rotate = -90, 45, 0
archetype = space_industrialc
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect09
pos = 100, -260, 155
rotate = 0, 0, 0
archetype = space_industriala
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect10
pos = 100, -260, -155
rotate = 0, 0, 0
archetype = space_industriala
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect11
pos = -100, -260, 155
rotate = 0, 0, 0
archetype = space_industriala
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect12
pos = -100, -260, -155
rotate = 0, 0, 0
archetype = space_industriala
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect13
pos = 100, -100, 110
rotate = 90, 45, 0
archetype = space_industrialc
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect14
pos = 100, -100, -110
rotate = 90, 45, 0
archetype = space_industrialc
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect15
pos = -100, -100, 110
rotate = 90, 45, 0
archetype = space_industrialc
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect16
pos = -100, -100, -110
rotate = 90, 45, 0
archetype = space_industrialc
parent = sph_base01

[Object]
nickname = sph_base01_ind_shprd01
pos = 100, 35, 1850
rotate = 0, 0, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_shprd02
pos = -100, 35, 1850
rotate = 0, 0, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_shprd03
pos = 100, 35, -1850
rotate = 0, 0, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_shprd04
pos = -100, 35, -1850
rotate = 0, 0, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_shprd05
pos = 0, -260, 800
rotate = 0, 90, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_shprd06
pos = 0, -250, 600
rotate = 0, 90, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_ind_shprd07
pos = 0, -260, -800
rotate = 0, 90, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_shprd08
pos = 0, -250, -600
rotate = 0, 90, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_ind_shprd09
pos = 0, 175, 600
rotate = 0, 90, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_shprd10
pos = 0, 175, -600
rotate = 0, 90, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_tube01
pos = 100, 250, 200
rotate = 8, 0, 0
archetype = space_tube_fix
parent = sph_base01

[Object]
nickname = sph_base01_tube02
pos = -100, 250, 200
rotate = 8, 0, 0
archetype = space_tube_fix
parent = sph_base01

[Object]
nickname = sph_base01_tube03
pos = 100, 35, 1730
rotate = 0, 180, 0
archetype = space_short_tube
parent = sph_base01

[Object]
nickname = sph_base01_tube04
pos = -100, 35, 1730
rotate = 0, 180, 0
archetype = space_short_tube
parent = sph_base01

[Object]
nickname = sph_base01_tube05
pos = 100, 250, -200
rotate = 8, 180, 0
archetype = space_tube_fix
parent = sph_base01

[Object]
nickname = sph_base01_tube06
pos = -100, 250, -200
rotate = 8, 180, 0
archetype = space_tube_fix
parent = sph_base01

[Object]
nickname = sph_base01_tube07
pos = 100, 35, -1730
rotate = 0, 0, 0
archetype = space_short_tube
parent = sph_base01

[Object]
nickname = sph_base01_tube08
pos = -100, 35, -1730
rotate = 0, 0, 0
archetype = space_short_tube
parent = sph_base01

[Object]
nickname = sph_base01_tube09
pos = 100, -260, -775
rotate = 0, 0, 0
archetype = space_tube_fix
parent = sph_base01

[Object]
nickname = sph_base01_tube10
pos = -100, -260, -775
rotate = 0, 0, 0
archetype = space_tube_fix
parent = sph_base01

[Object]
nickname = sph_base01_girder01
pos = 100, 35, 960
rotate = -25, 180, 0
archetype = space_girdera
parent = sph_base01

[Object]
nickname = sph_base01_girder02
pos = -100, 35, 960
rotate = -25, 180, 0
archetype = space_girdera
parent = sph_base01

[Object]
nickname = sph_base01_girder03
pos = 100, 85, 965
rotate = -90, 180, 0
archetype = space_girderb
parent = sph_base01

[Object]
nickname = sph_base01_girder04
pos = -100, 85, 965
rotate = -90, 180, 0
archetype = space_girderb
parent = sph_base01

[Object]
nickname = sph_base01_girder05
pos = 100, 35, -960
rotate = -25, 0, 0
archetype = space_girdera
parent = sph_base01

[Object]
nickname = sph_base01_girder06
pos = -100, 35, -960
rotate = -25, 0, 0
archetype = space_girdera
parent = sph_base01

[Object]
nickname = sph_base01_girder07
pos = 100, 85, -965
rotate = 90, 0, 0
archetype = space_girderb
parent = sph_base01

[Object]
nickname = sph_base01_girder08
pos = -100, 85, -965
rotate = -90, 0, 0
archetype = space_girderb
parent = sph_base01

[Object]
nickname = sph_base01_girder09
pos = 0, -850, 150
rotate = 0, 90, 0
archetype = space_girderc
parent = sph_base01

[Object]
nickname = sph_base01_girder10
pos = 0, -850, -150
rotate = 0, 90, 0
archetype = space_girderc
parent = sph_base01

[Object]
nickname = sph_base01_girder11
pos = 0, -500, 150
rotate = 0, 90, 0
archetype = space_girderc
parent = sph_base01

[Object]
nickname = sph_base01_girder12
pos = 0, -500, -150
rotate = 0, 90, 0
archetype = space_girderc
parent = sph_base01

[Object]
nickname = sph_base01_girder13
pos = 0, -260, -155
rotate = 0, 90, 0
archetype = space_girderc
parent = sph_base01

[Object]
nickname = sph_base01_girder14
pos = 0, -260, 155
rotate = 0, 90, 0
archetype = space_girderc
parent = sph_base01

[Object]
nickname = sph_base01_girder15
pos = 0, 250, 110
rotate = 0, 90, 0
archetype = space_girderc
parent = sph_base01

[Object]
nickname = sph_base01_girder16
pos = 0, 250, 110
rotate = 0, 90, 0
archetype = space_girderc
parent = sph_base01

[Object]
nickname = sph_base01_girder17
pos = 100, -545, 730
rotate = -72, 0, 0
archetype = space_girdera
parent = sph_base01

[Object]
nickname = sph_base01_girder18
pos = -100, -545, 730
rotate = -72, 0, 0
archetype = space_girdera
parent = sph_base01

[Object]
nickname = sph_base01_girder19
pos = 100, -545, -730
rotate = -72, 180, 0
archetype = space_girdera
parent = sph_base01

[Object]
nickname = sph_base01_girder20
pos = -100, -545, -730
rotate = -72, 180, 0
archetype = space_girdera
parent = sph_base01

[Object]
nickname = sph_base01_girder21
pos = 0, -840, 455
rotate = 0, 90, 0
archetype = space_girderc
parent = sph_base01

[Object]
nickname = sph_base01_girder22
pos = 0, -850, -455
rotate = 0, 90, 0
archetype = space_girderc
parent = sph_base01

[Object]
nickname = sph_base01_girder23
pos = 0, -525, 455
rotate = 0, 90, 0
archetype = space_girderc
parent = sph_base01

[Object]
nickname = sph_base01_girder24
pos = 0, -525, -455
rotate = 0, 90, 0
archetype = space_girderc
parent = sph_base01

[Object]
nickname = sph_base01_girder25
pos = 0, -525, 735
rotate = 0, 90, 0
archetype = space_girderc
parent = sph_base01

[Object]
nickname = sph_base01_girder24
pos = 0, -525, -725
rotate = 0, 90, 0
archetype = space_girderc
parent = sph_base01

[Object]
nickname = sph_base01_girder25
pos = 0, -1080, 150
rotate = 0, 90, 0
archetype = space_girderc
parent = sph_base01

[Object]
nickname = sph_base01_girder26
pos = 0, -1080, -150
rotate = 0, 90, 0
archetype = space_girderc
parent = sph_base01

[Object]
nickname = sph_base01_habitat01
pos = 100, 410, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat02
pos = -100, 410, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat03
pos = 0, 410, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat04
pos = 0, 410, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat05
pos = 0, 410, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat06
pos = 100, 550, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat07
pos = -100, 550, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat08
pos = 0, 550, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat09
pos = 0, 550, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat10
pos = 0, 550, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat11
pos = 100, 710, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat12
pos = -100, 710, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat13
pos = 0, 710, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat14
pos = 0, 710, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat15
pos = 0, 710, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat16
pos = 100, 850, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat17
pos = -100, 850, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat18
pos = 0, 850, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat19
pos = 0, 850, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat20
pos = 0, 850, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat21
pos = 60, 1025, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat22
pos = -60, 1025, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat23
pos = 0, 1025, 60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat24
pos = 0, 1025, -60
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat25
pos = 40, 1215, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat26
pos = -40, 1215, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat27
pos = 0, 1215, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat28
pos = 0, 1215, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat29
pos = 40, 1570, 0
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = sph_base01

[Object]
nickname = sph_base01_habitat30
pos = -40, 1570, 0
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = sph_base01

[Object]
nickname = sph_base01_habitat31
pos = 0, 1570, 40
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = sph_base01

[Object]
nickname = sph_base01_habitat32
pos = 0, 1570, -40
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = sph_base01

[Object]
nickname = sph_base01_habitat33
pos = 40, 1385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat34
pos = -40, 1385, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat35
pos = 0, 1385, 40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat36
pos = 0, 1385, -40
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = sph_base01

[Object]
nickname = sph_base01_habitat37
pos = 0, 180, -100
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = sph_base01

[Object]
nickname = sph_base01_habitat38
pos = 0, 180, 0
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = sph_base01

[Object]
nickname = sph_base01_habitat39
pos = 0, 180, 100
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = sph_base01

[Object]
nickname = sph_base01_habitat40
pos = 0, 1770, 0
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = sph_base01

[Object]
nickname = sph_base01_control_block01
pos = 0, 1890, 0
rotate = 0, 0, 0
archetype = space_small_control_block
parent = sph_base01

[Object]
nickname = sph_base01_control_block02
pos = 0, -260, -920
rotate = -90, 0, 0
archetype = space_small_control_block
parent = sph_base01

[Object]
nickname = sph_base01_control_block03
pos = 0, -260, 920
rotate = 90, 0, 0
archetype = space_small_control_block
parent = sph_base01

[Object]
nickname = sph_base01_bottom_tube01
pos = 100, -325, 155
rotate = 90, 0, 0
archetype = space_short_tube
parent = sph_base01

[Object]
nickname = sph_base01_bottom_tube02
pos = -100, -325, 155
rotate = 90, 0, 0
archetype = space_short_tube
parent = sph_base01

[Object]
nickname = sph_base01_bottom_tube03
pos = 100, -325, -155
rotate = 90, 0, 0
archetype = space_short_tube
parent = sph_base01

[Object]
nickname = sph_base01_bottom_tube04
pos = -100, -325, -155
rotate = 90, 0, 0
archetype = space_short_tube
parent = sph_base01

[Object]
nickname = sph_base01_bottom_tube05
pos = 100, -250, 455
rotate = 90, 0, 0
archetype = space_short_tube
parent = sph_base01

[Object]
nickname = sph_base01_bottom_tube06
pos = -100, -250, 455
rotate = 90, 0, 0
archetype = space_short_tube
parent = sph_base01

[Object]
nickname = sph_base01_bottom_tube07
pos = 100, -250, -455
rotate = 90, 0, 0
archetype = space_short_tube
parent = sph_base01

[Object]
nickname = sph_base01_bottom_tube05
pos = -100, -250, -455
rotate = 90, 0, 0
archetype = space_short_tube
parent = sph_base01

[Object]
nickname = sph_base01_tanks01
pos = 100, -500, 300
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = sph_base01

[Object]
nickname = sph_base01_tanks02
pos = 100, -840, 300
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = sph_base01

[Object]
nickname = sph_base01_tanks04
pos = -100, -500, 300
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = sph_base01

[Object]
nickname = sph_base01_tanks05
pos = -100, -850, 300
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = sph_base01

[Object]
nickname = sph_base01_tanks06
pos = 100, -500, -300
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = sph_base01

[Object]
nickname = sph_base01_tanks07
pos = 100, -850, -300
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = sph_base01

[Object]
nickname = sph_base01_tanks08
pos = -100, -500, -300
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = sph_base01

[Object]
nickname = sph_base01_tanks09
pos = -100, -850, -300
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = sph_base01

[Object]
nickname = sph_base01_tanks10
pos = 100, -775, 0
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = sph_base01

[Object]
nickname = sph_base01_tanks11
pos = 100, -1075, 0
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = sph_base01

[Object]
nickname = sph_base01_tanks12
pos = -100, -775, 0
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = sph_base01

[Object]
nickname = sph_base01_tanks13
pos = -100, -1075, 0
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = sph_base01

[Object]
nickname = sph_base01_tanks14
pos = -100, -475, 0
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = sph_base01

[Object]
nickname = sph_base01_tanks15
pos = 100, -475, 0
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = sph_base01

[Object]
nickname = sph_base01_tanks16
pos = 100, -525, 610
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = sph_base01

[Object]
nickname = sph_base01_tanks16
pos = 100, -525, 610
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = sph_base01

[Object]
nickname = sph_base01_tanks17
pos = -100, -525, 610
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = sph_base01

[Object]
nickname = sph_base01_tanks18
pos = 100, -525, -610
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = sph_base01

[Object]
nickname = sph_base01_tanks19
pos = -100, -525, -610
rotate = 0, 0, 0
archetype = space_tankl4x4
parent = sph_base01
'''


class SphereMegabaseShort(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'sph_base01'
    TEMPLATE = '''[Object]
nickname = sph_base01
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = hamburg_core
{root_props}

[Object]
nickname = sph_base01_control_twr01
pos = 0, 125, 0
rotate = 180, 0, 0
archetype = space_control_tower
parent = sph_base01

[Object]
nickname = sph_base01_control_twr02
pos = 0, 40, 0
rotate = 0, 7.5, 0
archetype = space_control_tower
parent = sph_base01

[Object]
nickname = sph_base01_control_twr03
pos = 0, -40, 0
rotate = 0, 6, 0
archetype = space_control_tower
parent = sph_base01

[Object]
nickname = sph_base01_control_twr04
pos = 0, -125, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = sph_base01

[Object]
nickname = sph_base01_control_twr05
pos = 0, 325, 0
rotate = -180, 45, 0
archetype = space_control_tower
parent = sph_base01

[Object]
nickname = sph_base01_prison01
pos = 600, 0, 155
rotate = 0, 180, 0
archetype = space_prison
parent = sph_base01

[Object]
nickname = sph_base01_prison02
pos = 600, 0, -155
rotate = 0, 180, 0
archetype = space_prison
parent = sph_base01

[Object]
nickname = sph_base01_prison03
pos = -600, 0, 155
rotate = 0, 0, 0
archetype = space_prison
parent = sph_base01

[Object]
nickname = sph_base01_prison04
pos = -600, 0, -155
rotate = 0, 0, 0
archetype = space_prison
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris01
pos = 275, 60, 70
rotate = 0, 80, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris02
pos = 275, -60, 70
rotate = 0, 80, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris03
pos = 335, 0, 215
rotate = 90, 0, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris04
pos = 175, 60, 185
rotate = 0, 75, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris05
pos = 175, -60, 185
rotate = 0, 75, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris06
pos = -275, 60, 70
rotate = 0, -80, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris07
pos = -275, -60, 70
rotate = 0, -80, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris08
pos = -335, 0, 215
rotate = 90, 0, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris09
pos = -175, 60, 185
rotate = 0, -75, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris10
pos = -175, -60, 185
rotate = 0, -75, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris11
pos = 275, 60, -70
rotate = 0, -80, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris12
pos = 275, -60, -70
rotate = 0, -80, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris13
pos = 335, 0, -215
rotate = 90, 0, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris14
pos = 175, 60, -185
rotate = 0, -75, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris15
pos = 175, -60, -185
rotate = 0, -75, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris16
pos = -275, 60, -70
rotate = 0, 80, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris17
pos = -275, -60, -70
rotate = 0, 80, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris18
pos = -335, 0, -215
rotate = 90, 0, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris19
pos = -175, 60, -185
rotate = 0, 75, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_pris20
pos = -175, -60, -185
rotate = 0, 75, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core01
pos = 0, 0, 180
rotate = 90, 0, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core02
pos = 180, 0, 0
rotate = 90, 90, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core03
pos = -180, 0, 0
rotate = 90, 90, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core04
pos = 0, 0, -180
rotate = 90, 0, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core05
pos = 90, 0, 155
rotate = 90, 30, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core06
pos = 155, 0, 90
rotate = 90, 60, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core07
pos = -90, 0, 155
rotate = 90, -30, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core08
pos = -155, 0, 90
rotate = 90, -60, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core09
pos = 90, 0, -155
rotate = 90, -30, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core10
pos = 155, 0, -90
rotate = 90, -60, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core11
pos = -90, 0, -155
rotate = 90, 30, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_industrial_core12
pos = -155, 0, -90
rotate = 90, 60, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_shipyard01
pos = 0, 0, 600
rotate = 180, 90, 0
archetype = shipyard_2x
parent = sph_base01

[Object]
nickname = sph_base01_shipyard02
pos = 0, 0, -600
rotate = 180, 90, 0
archetype = shipyard_2x
parent = sph_base01

[Object]
nickname = sph_base01_shipyard03
pos = 0, -50, 1150
rotate = 180, 90, 0
archetype = shipyard
parent = sph_base01

[Object]
nickname = sph_base01_shipyard04
pos = 0, -50, 1550
rotate = 180, 90, 0
archetype = shipyard
parent = sph_base01

[Object]
nickname = sph_base01_shipyard05
pos = 0, -50, -1150
rotate = 180, 90, 0
archetype = shipyard
parent = sph_base01

[Object]
nickname = sph_base01_shipyard06
pos = 0, -50, -1550
rotate = 180, 90, 0
archetype = shipyard
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect01
pos = 100, 250, 110
rotate = 0, 0, 0
archetype = space_industriala
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect02
pos = 100, 250, -110
rotate = 0, 0, 0
archetype = space_industriala
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect03
pos = -100, 250, 110
rotate = 0, 0, 0
archetype = space_industriala
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect04
pos = -100, 250, -110
rotate = 0, 0, 0
archetype = space_industriala
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect05
pos = 100, 100, 110
rotate = -90, 45, 0
archetype = space_industrialc
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect06
pos = 100, 100, -110
rotate = -90, 45, 0
archetype = space_industrialc
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect07
pos = -100, 100, 110
rotate = -90, 45, 0
archetype = space_industrialc
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect08
pos = -100, 100, -110
rotate = -90, 45, 0
archetype = space_industrialc
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect09
pos = 100, -260, 155
rotate = 0, 0, 0
archetype = space_industriala
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect10
pos = 100, -260, -155
rotate = 0, 0, 0
archetype = space_industriala
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect11
pos = -100, -260, 155
rotate = 0, 0, 0
archetype = space_industriala
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect12
pos = -100, -260, -155
rotate = 0, 0, 0
archetype = space_industriala
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect13
pos = 100, -100, 110
rotate = 90, 45, 0
archetype = space_industrialc
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect14
pos = 100, -100, -110
rotate = 90, 45, 0
archetype = space_industrialc
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect15
pos = -100, -100, 110
rotate = 90, 45, 0
archetype = space_industrialc
parent = sph_base01

[Object]
nickname = sph_base01_ind_connect16
pos = -100, -100, -110
rotate = 90, 45, 0
archetype = space_industrialc
parent = sph_base01

[Object]
nickname = sph_base01_ind_shprd01
pos = 100, 35, 1850
rotate = 0, 0, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_shprd02
pos = -100, 35, 1850
rotate = 0, 0, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_shprd03
pos = 100, 35, -1850
rotate = 0, 0, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_shprd04
pos = -100, 35, -1850
rotate = 0, 0, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_shprd05
pos = 0, -260, 800
rotate = 0, 90, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_shprd06
pos = 0, -250, 600
rotate = 0, 90, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_ind_shprd07
pos = 0, -260, -800
rotate = 0, 90, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_shprd08
pos = 0, -250, -600
rotate = 0, 90, 0
archetype = space_industrial02d
parent = sph_base01

[Object]
nickname = sph_base01_ind_shprd09
pos = 0, 175, 600
rotate = 0, 90, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_ind_shprd10
pos = 0, 175, -600
rotate = 0, 90, 0
archetype = space_industrial02a
parent = sph_base01

[Object]
nickname = sph_base01_tube01
pos = 100, 250, 200
rotate = 8, 0, 0
archetype = space_tube_fix
parent = sph_base01

[Object]
nickname = sph_base01_tube02
pos = -100, 250, 200
rotate = 8, 0, 0
archetype = space_tube_fix
parent = sph_base01

[Object]
nickname = sph_base01_tube03
pos = 100, 35, 1730
rotate = 0, 180, 0
archetype = space_short_tube
parent = sph_base01

[Object]
nickname = sph_base01_tube04
pos = -100, 35, 1730
rotate = 0, 180, 0
archetype = space_short_tube
parent = sph_base01

[Object]
nickname = sph_base01_tube05
pos = 100, 250, -200
rotate = 8, 180, 0
archetype = space_tube_fix
parent = sph_base01

[Object]
nickname = sph_base01_tube06
pos = -100, 250, -200
rotate = 8, 180, 0
archetype = space_tube_fix
parent = sph_base01

[Object]
nickname = sph_base01_tube07
pos = 100, 35, -1730
rotate = 0, 0, 0
archetype = space_short_tube
parent = sph_base01

[Object]
nickname = sph_base01_tube08
pos = -100, 35, -1730
rotate = 0, 0, 0
archetype = space_short_tube
parent = sph_base01

[Object]
nickname = sph_base01_tube09
pos = 100, -260, -775
rotate = 0, 0, 0
archetype = space_tube_fix
parent = sph_base01

[Object]
nickname = sph_base01_tube10
pos = -100, -260, -775
rotate = 0, 0, 0
archetype = space_tube_fix
parent = sph_base01

[Object]
nickname = sph_base01_girder01
pos = 100, 35, 960
rotate = -25, 180, 0
archetype = space_girdera
parent = sph_base01

[Object]
nickname = sph_base01_girder02
pos = -100, 35, 960
rotate = -25, 180, 0
archetype = space_girdera
parent = sph_base01

[Object]
nickname = sph_base01_girder03
pos = 100, 85, 965
rotate = -90, 180, 0
archetype = space_girderb
parent = sph_base01

[Object]
nickname = sph_base01_girder04
pos = -100, 85, 965
rotate = -90, 180, 0
archetype = space_girderb
parent = sph_base01

[Object]
nickname = sph_base01_girder05
pos = 100, 35, -960
rotate = -25, 0, 0
archetype = space_girdera
parent = sph_base01

[Object]
nickname = sph_base01_girder06
pos = -100, 35, -960
rotate = -25, 0, 0
archetype = space_girdera
parent = sph_base01

[Object]
nickname = sph_base01_girder07
pos = 100, 85, -965
rotate = 90, 0, 0
archetype = space_girderb
parent = sph_base01

[Object]
nickname = sph_base01_girder08
pos = -100, 85, -965
rotate = -90, 0, 0
archetype = space_girderb
parent = sph_base01

[Object]
nickname = sph_base01_girder09
pos = 0, -260, -155
rotate = 0, 90, 0
archetype = space_girderc
parent = sph_base01

[Object]
nickname = sph_base01_girder10
pos = 0, -260, 155
rotate = 0, 90, 0
archetype = space_girderc
parent = sph_base01
'''
