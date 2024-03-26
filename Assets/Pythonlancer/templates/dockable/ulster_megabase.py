from templates.space_object_template import SpaceObjectTemplate


class UlsterMegabase(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'br_uls_02'
    TEMPLATE = '''[Object]
nickname = br_uls_02
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = ulster_largestation_core
{root_props}

[Object]
nickname = br_uls_02_dock
pos = 115, 0, 300
rotate = 0, 0, 0
archetype = space_shipping01_front_dock
{dock_props}

[Object]
nickname = br_uls_02_DOCK_ind01
pos = 170, 0, 150
rotate = 0, 0, 0
archetype = space_industrial01d_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_DOCK_ind02
pos = -170, 0, 150
rotate = 0, 0, 0
archetype = space_industrial01d_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_DOCK_ind03
pos = 170, 0, -150
rotate = 0, 0, 0
archetype = space_industrial01d_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_DOCK_ind04
pos = -170, 0, -150
rotate = 0, 0, 0
archetype = space_industrial01d_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_DOCK_shipyard
pos = 0, -30, -350
rotate = 0, 90, 0
archetype = shipyard_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_core
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = sw_center_200
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_LEFT_panels01
pos = -1225, 425, 0
rotate = 0, -90, 0
archetype = space_shield_cut
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_LEFT_panels02
pos = -1225, -425, 0
rotate = 180, -90, 0
archetype = space_shield_cut
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_LEFT_tube01
pos = -460, 100, 0
rotate = 0, -90, 0
archetype = space_tube_fix_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_LEFT_tube02
pos = -460, 700, 0
rotate = 0, -90, 0
archetype = space_tube_fix_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_LEFT_tube03
pos = -460, -100, 0
rotate = 0, -90, 0
archetype = space_tube_fix_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_LEFT_tube04
pos = -460, -700, 0
rotate = 0, -90, 0
archetype = space_tube_fix_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_LEFT_tube05
pos = -350, -59, 0
rotate = -90, 0, 8.75
archetype = space_short_tube
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_LEFT_tube06
pos = -350, 59, 0
rotate = 90, 0, -8.75
archetype = space_short_tube
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_LEFT_tube07
pos = -2120, -59, 0
rotate = -90, 0, -8.75
archetype = space_short_tube
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_LEFT_tube08
pos = -2120, 59, 0
rotate = 90, 0, 8.75
archetype = space_short_tube
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_LEFT_ind01
pos = -380, 0, 0
rotate = 0, 0, 0
archetype = space_industrial02a_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_LEFT_ind02
pos = -380, 100, 0
rotate = 0, 90, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_LEFT_ind03
pos = -380, -100, 0
rotate = 0, 90, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_LEFT_ind04
pos = -2090, 0, 0
rotate = 0, 0, 0
archetype = space_industrial02a_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_LEFT_ind05
pos = -2090, 100, 0
rotate = 0, 90, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_LEFT_ind06
pos = -2090, -100, 0
rotate = 0, 90, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_RIGHT_panels01
pos = 1225, 425, 0
rotate = 0, 90, 0
archetype = space_shield_cut
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_RIGHT_panels02
pos = 1225, -425, 0
rotate = 180, 90, 0
archetype = space_shield_cut
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_RIGHT_tube01
pos = 460, 100, 0
rotate = 0, 90, 0
archetype = space_tube_fix_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_RIGHT_tube02
pos = 460, 700, 0
rotate = 0, 90, 0
archetype = space_tube_fix_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_RIGHT_tube03
pos = 460, -100, 0
rotate = 0, 90, 0
archetype = space_tube_fix_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_RIGHT_tube04
pos = 460, -700, 0
rotate = 0, 90, 0
archetype = space_tube_fix_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_RIGHT_tube05
pos = 350, -59, 0
rotate = -90, 0, -8.75
archetype = space_short_tube
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_RIGHT_tube06
pos = 350, 59, 0
rotate = 90, 0, 8.75
archetype = space_short_tube
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_RIGHT_tube07
pos = 2120, -59, 0
rotate = -90, 0, 8.75
archetype = space_short_tube
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_RIGHT_tube08
pos = 2120, 59, 0
rotate = 90, 0, -8.75
archetype = space_short_tube
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_RIGHT_ind01
pos = 380, 0, 0
rotate = 0, 0, 0
archetype = space_industrial02a_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_RIGHT_ind02
pos = 380, 100, 0
rotate = 0, 90, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_RIGHT_ind03
pos = 380, -100, 0
rotate = 0, 90, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_RIGHT_ind04
pos = 2090, 0, 0
rotate = 0, 0, 0
archetype = space_industrial02a_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_RIGHT_ind05
pos = 2090, 100, 0
rotate = 0, 90, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_PANEL_RIGHT_ind06
pos = 2090, -100, 0
rotate = 0, 90, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_CORE_tower01
pos = -170, 0, 0
rotate = 0, 0, 90
archetype = space_medium_control_tower_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_CORE_tower02
pos = 180, 0, 0
rotate = 0, 0, -90
archetype = space_medium_control_tower_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_CORE_tower03
pos = 0, 170, 0
rotate = 0, 0, 0
archetype = space_control_tower_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_CORE_tower04
pos = 0, -170, 0
rotate = 0, 0, 0
archetype = space_control_tower_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_CORE_airlock01
pos = -280, 0, 0
rotate = 90,45, 90
archetype = space_airlock_dummy_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_CORE_airlock02
pos = 280, 0, 0
rotate = 0, -90, 0
archetype = space_airlock_dummy_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOPLINE_airlock01
pos = 0, 250, 0
rotate = 90, 45, 0
archetype = space_airlock_dummy_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOPLINE_airlock02
pos = 0, 1025, 0
rotate = -90, 0, 0
archetype = space_airlock_dummy_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOPLINE_tube01
pos = 0, 200, 115
rotate = -90, 0, 0
archetype = space_short_tube_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOPLINE_tube02
pos = 0, 200, -115
rotate = -90, 45, 0
archetype = space_short_tube_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOPLINE_ind01
pos = 0, 400, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = br_uls_02

[Object]
nickname = br_uls_02_TOPLINE_ind02
pos = 0, 637.5, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = br_uls_02

[Object]
nickname = br_uls_02_TOPLINE_ind03
pos = 0, 875, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = br_uls_02

[Object]
nickname = br_uls_02_TOPLINE_ind04
pos = 0, 175, 115
rotate = -90, 45, 0
archetype = space_industrialc_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOPLINE_ind05
pos = 0, 175, -115
rotate = -90, 45, 0
archetype = space_industrialc_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOPLINE_ind06
pos = 0, 1100, 115
rotate = 90, 45, 0
archetype = space_industrialc_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOPLINE_ind07
pos = 0, 1100, -115
rotate = 90, 45, 0
archetype = space_industrialc_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOPLINE_girder01
pos = 0, 875, 0
rotate = 0, 0, 0
archetype = space_girderc_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOPLINE_girder02
pos = 0, 637.5, 0
rotate = 0, 0, 0
archetype = space_girderc_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOPLINE_girder03
pos = 0, 400, 0
rotate = 0, 0, 0
archetype = space_girderc_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOPLINE_girder04
pos = -170, 170, 0
rotate = -115, -90, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOPLINE_girder05
pos = 170, 170, 0
rotate = -115, 90, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOPLINE_girder06
pos = -170, 1100, 0
rotate = 115, -90, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOPLINE_girder07
pos = 170, 1100, 0
rotate = 115, 90, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOPLINE_tower01
pos = 0, 1100, 0
rotate = 0, 15, 0
archetype = space_control_tower_lowdetail
loadout = bx_energy_industrials
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOMLINE_airlock01
pos = 0, -250, 0
rotate = -90, 45, 0
archetype = space_airlock_dummy_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOMLINE_airlock02
pos = 0, -1025, 0
rotate = 90, 0, 0
archetype = space_airlock_dummy_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOMLINE_tube01
pos = 0, -200, 115
rotate = 90, 0, 0
archetype = space_short_tube_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOMLINE_tube02
pos = 0, -200, -115
rotate = 90, 45, 0
archetype = space_short_tube_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOMLINE_ind01
pos = 0, -400, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOMLINE_ind02
pos = 0, -637.5, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOMLINE_ind03
pos = 0, -875, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOMLINE_ind04
pos = 0, -175, 115
rotate = 90, 45, 0
archetype = space_industrialc_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOMLINE_ind05
pos = 0, -175, -115
rotate = 90, 45, 0
archetype = space_industrialc_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOMLINE_ind06
pos = 0, -1100, 115
rotate = -90, 45, 0
archetype = space_industrialc_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOMLINE_ind07
pos = 0, -1100, -115
rotate = -90, 45, 0
archetype = space_industrialc_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOMLINE_girder01
pos = 0, -875, 0
rotate = 0, 0, 0
archetype = space_girderc_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOMLINE_girder02
pos = 0, -637.5, 0
rotate = 0, 0, 0
archetype = space_girderc_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOMLINE_girder03
pos = 0, -400, 0
rotate = 0, 0, 0
archetype = space_girderc_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOMLINE_girder04
pos = -170, -170, 0
rotate = 115, -90, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOMLINE_girder05
pos = 170, -170, 0
rotate = 115, 90, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOMLINE_girder06
pos = -170, -1100, 0
rotate = -115, -90, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOMLINE_girder07
pos = 170, -1100, 0
rotate = -115, 90, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOMLINE_tower01
pos = 0, -1100, 0
rotate = 0, 15, 0
archetype = space_control_tower_lowdetail
loadout = bx_energy_industrials
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indA01
pos = 0, 1100, 848
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indA02
pos = 0, 1100, -848
rotate = 0, -90, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indA03
pos = 848, 1100, 0
rotate = 0, 180, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indA04
pos = -848, 1100, 0
rotate = 0, 0, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indA05
pos = 420, 1100, 736
rotate = 0, 120, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indA06
pos = -420, 1100, 736
rotate = 0, 60, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indA07
pos = 420, 1100, -736
rotate = 0, -120, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indA08
pos = -420, 1100, -736
rotate = 0, -60, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indA09
pos = 736, 1100, 420
rotate = 0, 150, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indA10
pos = 736, 1100, -420
rotate = 0, -150, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indA11
pos = -736, 1100, 420
rotate = 0, 30, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indA12
pos = -736, 1100, -420
rotate = 0, -30, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indB01
pos = 0, 900, 424
rotate = 0, 90, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indB02
pos = 0, 900, -424
rotate = 0, 90, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indB03
pos = 424, 900, 0
rotate = 0, 0, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indB04
pos = -424, 900, 0
rotate = 0, 0, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indB05
pos = 210, 900, 368
rotate = 0, 120, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indB06
pos = -210, 900, 368
rotate = 0, 60, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indB07
pos = 210, 900, -368
rotate = 0, 60, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indB08
pos = -210, 900, -368
rotate = 0, 120, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indB09
pos = 368, 900, 210
rotate = 0, 150, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indB10
pos = 368, 900, -210
rotate = 0, 30, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indB11
pos = -368, 900, 210
rotate = 0, 30, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indB12
pos = -368, 900, -210
rotate = 0, 150, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indC01
pos = 0, 1300, 424
rotate = 0, 90, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indC02
pos = 0, 1300, -424
rotate = 0, 90, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indC03
pos = 424, 1300, 0
rotate = 0, 0, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indC04
pos = -424, 1300, 0
rotate = 0, 0, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indC05
pos = 210, 1300, 368
rotate = 0, 120, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indC06
pos = -210, 1300, 368
rotate = 0, 60, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indC07
pos = 210, 1300, -368
rotate = 0, 60, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indC08
pos = -210, 1300, -368
rotate = 0, 120, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indC09
pos = 368, 1300, 210
rotate = 0, 150, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indC10
pos = 368, 1300, -210
rotate = 0, 30, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indC11
pos = -368, 1300, 210
rotate = 0, 30, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indC12
pos = -368, 1300, -210
rotate = 0, 150, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_tube01
pos = 0, 1101, -775
rotate = 0, 0, 0
archetype = space_tube_fix_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_tube02
pos = -674.1, 1100, -381.9
rotate = 0, 60, 0
archetype = space_tube_fix_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_tube03
pos = -674, 1099, 381
rotate = 0, 120, 0
archetype = space_tube_fix_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indD01
pos = 424, 1100, 0
rotate = 0, 90, 0
archetype = space_industrial01_low_detail
loadout = space_ind01_reactor
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indD02
pos = -424, 1100, 0
rotate = 0, -90, 0
archetype = space_industrial01_low_detail
loadout = space_ind01_reactor
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indD03
pos = 210, 1100, 368
rotate = 0, 30, 0
archetype = space_industrial01_low_detail
loadout = space_ind01_reactor
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indD04
pos = -210, 1100, 368
rotate = 0, -30, 0
archetype = space_industrial01_low_detail
loadout = space_ind01_reactor
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indD05
pos = -210, 1100, -368
rotate = 0, -150, 0
archetype = space_industrial01_low_detail
loadout = space_ind01_reactor
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_indD06
pos = 210, 1100, -368
rotate = 0, 150, 0
archetype = space_industrial01_low_detail
loadout = space_ind01_reactor
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_girderA01
pos = 424, 1100, 0
rotate = 0, -90, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_girderA02
pos = -424, 1100, 0
rotate = 0, 90, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_girderA03
pos = 210, 1100, 368
rotate = 0, -150, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_girderA04
pos = -210, 1100, 368
rotate = 0, 150, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_girderA05
pos = -210, 1100, -368
rotate = 0, 30, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_girderA06
pos = 210, 1100, -368
rotate = 0, -30, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_tower01
pos = 0, 1300, 0
rotate = 180, 0, 0
archetype = space_control_tower_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_tower02
pos = 0, 1130, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_tower04
pos = 0, 1450, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_habitatA01
pos = 106, 1210, 0
rotate = 0, 0, 0
archetype = space_habitat_wide_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_habitatA02
pos = -106, 1210, 0
rotate = 0, 0, 0
archetype = space_habitat_wide_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_habitatA03
pos = 52.5, 1210, 92
rotate = 0, 0, 0
archetype = space_habitat_wide_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_habitatA04
pos = 52.5, 1210, -92
rotate = 0, 0, 0
archetype = space_habitat_wide_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_habitatA05
pos = -52.5, 1210, 92
rotate = 0, 0, 0
archetype = space_habitat_wide_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_habitatA06
pos = -52.5, 1210, -92
rotate = 0, 0, 0
archetype = space_habitat_wide_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_habitatA07
pos = 0, 1210, 0
rotate = 0, 0, 0
archetype = space_habitat_wide_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_airlock01
pos = 0, 1400, 0
rotate = 90, 45, 0
archetype = space_airlock_dummy_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_girderB01
pos = 0, 1300, -424
rotate = 0, 0, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_girderB02
pos = 368, 1300, -210
rotate = 0, -60, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_girderB03
pos = 368, 1300, 210
rotate = 0, -120, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_girderB04
pos = 0, 1300, 424
rotate = 0, 180, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_girderB05
pos = -368, 1300, 210
rotate = 0, 120, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_girderB06
pos = -368, 1300, -210
rotate = 0, 60, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_habitatB01
pos = 224, 1300, 0
rotate = 0, 0, 90
archetype = space_habitat_tall_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_habitatB02
pos = -224, 1300, 0
rotate = 0, 0, -90
archetype = space_habitat_tall_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_habitatB03
pos = 110, 1300, 195
rotate = -60, 0, 90
archetype = space_habitat_tall_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_habitatB04
pos = -110, 1300, 195
rotate = -120, 0, 90
archetype = space_habitat_tall_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_habitatB05
pos = 110, 1300, -195
rotate = 60, 0, 90
archetype = space_habitat_tall_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_habitatB06
pos = -110, 1300, -195
rotate = 120, 0, 90
archetype = space_habitat_tall_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_TOP_habitatC01
pos = 0, 1515, 0
rotate = 0, 0, 0
archetype = space_small_control_block
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indA01
pos = 0, -1100, 848
rotate = 0, 90, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indA02
pos = 0, -1100, -848
rotate = 0, -90, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indA03
pos = 848, -1100, 0
rotate = 0, 180, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indA04
pos = -848, -1100, 0
rotate = 0, 0, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indA05
pos = 420, -1100, 736
rotate = 0, 120, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indA06
pos = -420, -1100, 736
rotate = 0, 60, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indA07
pos = 420, -1100, -736
rotate = 0, -120, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indA08
pos = -420, -1100, -736
rotate = 0, -60, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indA09
pos = 736, -1100, 420
rotate = 0, 150, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indA10
pos = 736, -1100, -420
rotate = 0, -150, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indA11
pos = -736, -1100, 420
rotate = 0, 30, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indA12
pos = -736, -1100, -420
rotate = 0, -30, 0
archetype = space_industrial01a
loadout = space_ind01_bx_domes
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indB01
pos = 0, -900, 424
rotate = 0, 90, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indB02
pos = 0, -900, -424
rotate = 0, 90, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indB03
pos = 424, -900, 0
rotate = 0, 0, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indB04
pos = -424, -900, 0
rotate = 0, 0, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indB05
pos = 210, -900, 368
rotate = 0, 120, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indB06
pos = -210, -900, 368
rotate = 0, 60, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indB07
pos = 210, -900, -368
rotate = 0, 60, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indB08
pos = -210, -900, -368
rotate = 0, 120, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indB09
pos = 368, -900, 210
rotate = 0, 150, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indB10
pos = 368, -900, -210
rotate = 0, 30, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indB11
pos = -368, -900, 210
rotate = 0, 30, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indB12
pos = -368, -900, -210
rotate = 0, 150, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indC01
pos = 0, -1300, 424
rotate = 0, 90, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indC02
pos = 0, -1300, -424
rotate = 0, 90, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indC03
pos = 424, -1300, 0
rotate = 0, 0, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indC04
pos = -424, -1300, 0
rotate = 0, 0, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indC05
pos = 210, -1300, 368
rotate = 0, 120, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indC06
pos = -210, -1300, 368
rotate = 0, 60, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indC07
pos = 210, -1300, -368
rotate = 0, 60, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indC08
pos = -210, -1300, -368
rotate = 0, 120, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indC09
pos = 368, -1300, 210
rotate = 0, 150, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indC10
pos = 368, -1300, -210
rotate = 0, 30, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indC11
pos = -368, -1300, 210
rotate = 0, 30, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indC12
pos = -368, -1300, -210
rotate = 0, 150, 0
archetype = space_industriala_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_tube01
pos = 0, -1101, -775
rotate = 0, 0, 0
archetype = space_tube_fix_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_tube02
pos = -674.1, -1100, -381.9
rotate = 0, 60, 0
archetype = space_tube_fix_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_tube03
pos = -674, -1099, 381
rotate = 0, 120, 0
archetype = space_tube_fix_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indD01
pos = 424, -1100, 0
rotate = 0, 90, 0
archetype = space_industrial01_low_detail
loadout = space_ind01_reactor
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indD02
pos = -424, -1100, 0
rotate = 0, -90, 0
archetype = space_industrial01_low_detail
loadout = space_ind01_reactor
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indD03
pos = 210, -1100, 368
rotate = 0, 30, 0
archetype = space_industrial01_low_detail
loadout = space_ind01_reactor
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indD04
pos = -210, -1100, 368
rotate = 0, -30, 0
archetype = space_industrial01_low_detail
loadout = space_ind01_reactor
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indD05
pos = -210, -1100, -368
rotate = 0, -150, 0
archetype = space_industrial01_low_detail
loadout = space_ind01_reactor
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_indD06
pos = 210, -1100, -368
rotate = 0, 150, 0
archetype = space_industrial01_low_detail
loadout = space_ind01_reactor
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_girderA01
pos = 424, -1100, 0
rotate = 0, -90, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_girderA02
pos = -424, -1100, 0
rotate = 0, 90, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_girderA03
pos = 210, -1100, 368
rotate = 0, -150, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_girderA04
pos = -210, -1100, 368
rotate = 0, 150, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_girderA05
pos = -210, -1100, -368
rotate = 0, 30, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_girderA06
pos = 210, -1100, -368
rotate = 0, -30, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_tower01
pos = 0, -1300, 0
rotate = 180, 0, 0
archetype = space_control_tower_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_tower02
pos = 0, -1130, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower_lowdetail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_tower04
pos = 0, -1450, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_habitatA01
pos = 106, -1210, 0
rotate = 0, 0, 0
archetype = space_habitat_wide_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_habitatA02
pos = -106, -1210, 0
rotate = 0, 0, 0
archetype = space_habitat_wide_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_habitatA03
pos = 52.5, -1210, 92
rotate = 0, 0, 0
archetype = space_habitat_wide_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_habitatA04
pos = 52.5, -1210, -92
rotate = 0, 0, 0
archetype = space_habitat_wide_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_habitatA05
pos = -52.5, -1210, 92
rotate = 0, 0, 0
archetype = space_habitat_wide_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_habitatA06
pos = -52.5, -1210, -92
rotate = 0, 0, 0
archetype = space_habitat_wide_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_habitatA07
pos = 0, -1210, 0
rotate = 0, 0, 0
archetype = space_habitat_wide_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_airlock01
pos = 0, -1400, 0
rotate = -90, 45, 0
archetype = space_airlock_dummy_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_girderB01
pos = 0, -1300, -424
rotate = 0, 0, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_girderB02
pos = 368, -1300, -210
rotate = 0, -60, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_girderB03
pos = 368, -1300, 210
rotate = 0, -120, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_girderB04
pos = 0, -1300, 424
rotate = 0, 180, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_girderB05
pos = -368, -1300, 210
rotate = 0, 120, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_girderB06
pos = -368, -1300, -210
rotate = 0, 60, 0
archetype = space_girdera_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_habitatB01
pos = 224, -1300, 0
rotate = 0, 0, 90
archetype = space_habitat_tall_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_habitatB02
pos = -224, -1300, 0
rotate = 0, 0, -90
archetype = space_habitat_tall_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_habitatB03
pos = 110, -1300, 195
rotate = -60, 0, 90
archetype = space_habitat_tall_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_habitatB04
pos = -110, -1300, 195
rotate = -120, 0, 90
archetype = space_habitat_tall_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_habitatB05
pos = 110, -1300, -195
rotate = 60, 0, 90
archetype = space_habitat_tall_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_habitatB06
pos = -110, -1300, -195
rotate = 120, 0, 90
archetype = space_habitat_tall_low_detail
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_habitatC01
pos = 0, -1515, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_girderC01
pos = 424, -1100, 0
rotate = 90, 90, 0
archetype = space_girder
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_girderC02
pos = -424, -1100, 0
rotate = 90, -90, 0
archetype = space_girder
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_girderC03
pos = 210, -1100, 368
rotate = 90, 30, 0
archetype = space_girder
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_girderC04
pos = -210, -1100, 368
rotate = 90, -30, 0
archetype = space_girder
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_girderC05
pos = -210, -1100, -368
rotate = 90, -150, 0
archetype = space_girder
parent = br_uls_02

[Object]
nickname = br_uls_02_BOTTOM_girderC06
pos = 210, -1100, -368
rotate = 90, 150, 0
archetype = space_girder
parent = br_uls_02
'''
