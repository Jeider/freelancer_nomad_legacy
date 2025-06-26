from templates.space_object_template import SpaceObjectTemplate


class TekagiMegabase(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'ku_tgk_01'
    TEMPLATE = '''[Object]
nickname = ku_tgk_01
pos = 0, 0, 0
rotate = 0, -90, 0
archetype = smallstation1
loadout = smallstation1_nosound
{dock_props}

[Object]
nickname = ku_tgk_01_station_center
pos = 0, -520, 0
archetype = sw_center_500
rotate = 0, 45, 0
atmosphere_range = 100
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_lod
pos = 0, -521, 0
archetype = space_trade_station_full_lod
parent = ku_tgk_01
rotate = 0, 90, 0

;center connections

[Object]
nickname = ku_tgk_01_PIPELINE_girder01
pos = 980, -520, 0
rotate = 0, 90, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINE_girder02
pos = 868, -378, 0
rotate = -60, 90, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINE_girder03
pos = 868, -662, 0
rotate = 60, 90, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINE_girder04
pos = 680, -520, 0
rotate = 0, 90, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINE_girder05
pos = 670, -500, 0
rotate = 0, 90, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINE_girder06
pos = 670, -540, 0
rotate = 0, 90, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINE_girder07
pos = 485, -375, 0
rotate = 78, 90, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINE_girder08
pos = 485, -665, 0
rotate = -78, 90, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINE_industrial01
pos = 820, -520, 0
rotate = 0, 0, 0
archetype = space_industriala_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINE_industrial02
pos = 500, -520, 0
rotate = 0, 90, 0
archetype = space_industrial01a_low_detail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINE_industrial03
pos = 320, -220, 0
rotate = -10, 90, 0
archetype = space_industrial01a_low_detail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINE_industrial04
pos = 320, -820, 0
rotate = 10, 90, 0
archetype = space_industrial01a_low_detail
parent = ku_tgk_01


[Object]
nickname = ku_tgk_01_PIPELINEB_girder01
pos = -980, -520, 0
rotate = 0, -90, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEB_girder02
pos = -868, -378, 0
rotate = -60, -90, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEB_girder03
pos = -868, -662, 0
rotate = 60, -90, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEB_girder04
pos = -680, -520, 0
rotate = 0, -90, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEB_girder05
pos = -670, -500, 0
rotate = 0, -90, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEB_girder06
pos = -670, -540, 0
rotate = 0, -90, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEB_girder07
pos = -485, -375, 0
rotate = 78, -90, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEB_girder08
pos = -485, -665, 0
rotate = -78, -90, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEB_industrial01
pos = -820, -520, 0
rotate = 0, 0, 0
archetype = space_industriala_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEB_industrial02
pos = -500, -520, 0
rotate = 0, -90, 0
archetype = space_industrial01a_low_detail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEB_industrial03
pos = -320, -220, 0
rotate = -10, -90, 0
archetype = space_industrial01a_low_detail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEB_industrial04
pos = -320, -820, 0
rotate = 10, -90, 0
archetype = space_industrial01a_low_detail
parent = ku_tgk_01


[Object]
nickname = ku_tgk_01_PIPELINEC_girder01
pos = 0, -520, -980
rotate = 0, 180, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEC_girder02
pos = 0, -378, -868
rotate = -60, 180, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEC_girder03
pos = 0, -662, -868
rotate = 60, 180, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEC_girder04
pos = 0, -520, -680
rotate = 0, 180, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEC_girder05
pos = 0, -500, -670
rotate = 0, 180, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEC_girder06
pos = 0, -540, -670
rotate = 0, 180, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEC_girder07
pos = 0, -375, -485
rotate = 78, 180, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEC_girder08
pos = 0, -665, -485
rotate = -78, 180, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEC_industrial01
pos = 0, -520, -820
rotate = 0, 90, 0
archetype = space_industriala_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEC_industrial02
pos = 0, -520, -500
rotate = 0, 180, 0
archetype = space_industrial01a_low_detail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEC_industrial03
pos = 0, -220, -320
rotate = -10, 180, 0
archetype = space_industrial01a_low_detail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINEC_industrial04
pos = 0, -820, -320
rotate = 10, 180, 0
archetype = space_industrial01a_low_detail
parent = ku_tgk_01


[Object]
nickname = ku_tgk_01_PIPELINED_girder01
pos = 0, -520, 980
rotate = 0, -0, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINED_girder02
pos = 0, -378, 868
rotate = -60, -0, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINED_girder03
pos = 0, -662, 868
rotate = 60, -0, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINED_girder04
pos = 0, -520, 680
rotate = 0, -0, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINED_girder05
pos = 0, -500, 670
rotate = 0, -0, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINED_girder06
pos = 0, -540, 670
rotate = 0, -0, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINED_girder07
pos = 0, -375, 485
rotate = 78, -0, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINED_girder08
pos = 0, -665, 485
rotate = -78, -0, 0
archetype = space_girder_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINED_industrial01
pos = 0, -520, 820
rotate = 0, 90, 0
archetype = space_industriala_lowdetail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINED_industrial02
pos = 0, -520, 500
rotate = 0, -0, 0
archetype = space_industrial01a_low_detail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINED_industrial03
pos = 0, -220, 320
rotate = -10, -0, 0
archetype = space_industrial01a_low_detail
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_PIPELINED_industrial04
pos = 0, -820, 320
rotate = 10, -0, 0
archetype = space_industrial01a_low_detail
parent = ku_tgk_01



[Object]
nickname = ku_tgk_01_CONTROL_habitat01
pos = 0, -1240, 60
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = ku_tgk_01


[Object]
nickname = ku_tgk_01_CONTROL_habitat02
pos = 0, -1325, 0
rotate = 180, -0, 0
archetype = space_habitat_tall
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_CONTROL_habitat03
pos = 0, -1185, -60
rotate = 180, -0, 0
archetype = space_habitat_tall
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_CONTROL_habitat04
pos = 60, -1120, 0
rotate = 180, -0, 0
archetype = space_habitat_tall
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_CONTROL_habitat05
pos = 0, -1090, 60
rotate = 0, -0, 0
archetype = space_habitat_wide
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_CONTROL_habitat06
pos = 0, -1115, 0
rotate = 0, -0, 0
archetype = space_habitat_wide
parent = ku_tgk_01

[Object]
nickname = ku_tgk_01_CONTROL_control_tower01
pos = 0, -1020, 0
rotate = 0, -0, 0
archetype = space_control_tower
parent = ku_tgk_01





[Object]
nickname = ku_tgk_01_CENTER_industrial01
pos = 0, -520, 1100
rotate = 0, 90, 0
archetype = space_trade_station_part
parent = ku_tgk_01
loadout = space_trade_part_attacher
reputation = ku_grp
pilot = pilot_solar_hardest
behavior = NOTHING

[Object]
nickname = ku_tgk_01_CENTER_industrial02
pos = 425, -520, 1015
rotate = 0, 112.5, 0
archetype = space_trade_station_part
parent = ku_tgk_01
loadout = space_trade_part_attacher2
reputation = ku_grp
pilot = pilot_solar_hardest
behavior = NOTHING

[Object]
nickname = ku_tgk_01_CENTER_industrial03
pos = 792, -520, 795
rotate = 0, 135, 0
archetype = space_trade_station_part
parent = ku_tgk_01
loadout = space_trade_part_attacher
reputation = ku_grp
pilot = pilot_solar_hardest
behavior = NOTHING

[Object]
nickname = ku_tgk_01_CENTER_industrial04
pos = 1015, -520, 420
rotate = 0, 157.5, 0
archetype = space_trade_station_part
parent = ku_tgk_01
loadout = space_trade_part_attacher2
reputation = ku_grp
pilot = pilot_solar_hardest
behavior = NOTHING

[Object]
nickname = ku_tgk_01_CENTER_industrial05
pos = 1100, -520, 0
rotate = 0, 180, 0
archetype = space_trade_station_part
parent = ku_tgk_01
loadout = space_trade_part_attacher
reputation = ku_grp
pilot = pilot_solar_hardest
behavior = NOTHING

[Object]
nickname = ku_tgk_01_CENTER_industrial06
pos = -1100, -520, 0
rotate = 0, 0, 0
archetype = space_trade_station_part
parent = ku_tgk_01
loadout = space_trade_part_attacher
reputation = ku_grp
pilot = pilot_solar_hardest
behavior = NOTHING

[Object]
nickname = ku_tgk_01_CENTER_industrial07
pos = -1015, -520, 420
rotate = 0, -337.5, 0
archetype = space_trade_station_part
parent = ku_tgk_01
loadout = space_trade_part_attacher2
reputation = ku_grp
pilot = pilot_solar_hardest
behavior = NOTHING

[Object]
nickname = ku_tgk_01_CENTER_industrial08
pos = -798, -520, 795
rotate = 0, -315, 0
archetype = space_trade_station_part
parent = ku_tgk_01
loadout = space_trade_part_attacher
reputation = ku_grp
pilot = pilot_solar_hardest
behavior = NOTHING

[Object]
nickname = ku_tgk_01_CENTER_industrial09
pos = -425, -520, 1015
rotate = 0, -292.5, 0
archetype = space_trade_station_part
parent = ku_tgk_01
loadout = space_trade_part_attacher2
reputation = ku_grp
pilot = pilot_solar_hardest
behavior = NOTHING

[Object]
nickname = ku_tgk_01_CENTER_industrial10
pos = 1015, -520, -420
rotate = 0, -157.5, 0
archetype = space_trade_station_part
parent = ku_tgk_01
loadout = space_trade_part_attacher2
reputation = ku_grp
pilot = pilot_solar_hardest
behavior = NOTHING

[Object]
nickname = ku_tgk_01_CENTER_industrial11
pos = 792, -520, -795
rotate = 0, -135, 0
archetype = space_trade_station_part
parent = ku_tgk_01
loadout = space_trade_part_attacher
reputation = ku_grp
pilot = pilot_solar_hardest
behavior = NOTHING

[Object]
nickname = ku_tgk_01_CENTER_industrial12
pos = 425, -520, -1015
rotate = 0, -112.5, 0
archetype = space_trade_station_part
parent = ku_tgk_01
loadout = space_trade_part_attacher2
reputation = ku_grp
pilot = pilot_solar_hardest
behavior = NOTHING

[Object]
nickname = ku_tgk_01_CENTER_industrial13
pos = 0, -520, -1100
rotate = 0, 270, 0
archetype = space_trade_station_part
parent = ku_tgk_01
loadout = space_trade_part_attacher
reputation = ku_grp
pilot = pilot_solar_hardest
behavior = NOTHING

[Object]
nickname = ku_tgk_01_CENTER_industrial14
pos = -425, -520, -1015
rotate = 0, 292.5, 0
archetype = space_trade_station_part
parent = ku_tgk_01
loadout = space_trade_part_attacher2
reputation = ku_grp
pilot = pilot_solar_hardest
behavior = NOTHING

[Object]
nickname = ku_tgk_01_CENTER_industrial15
pos = -792, -520, -795
rotate = 0, 315, 0
archetype = space_trade_station_part
parent = ku_tgk_01
loadout = space_trade_part_attacher
reputation = ku_grp
pilot = pilot_solar_hardest
behavior = NOTHING

[Object]
nickname = ku_tgk_01_CENTER_industrial16
pos = -1015, -520, -420
rotate = 0, 337.5, 0
archetype = space_trade_station_part
parent = ku_tgk_01
loadout = space_trade_part_attacher2
reputation = ku_grp
pilot = pilot_solar_hardest
behavior = NOTHING
'''
