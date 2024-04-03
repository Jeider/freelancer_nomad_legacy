from templates.space_object_template import SpaceObjectTemplate


class ColumbiaProduction(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_col_03'
    TEMPLATE = '''[Object]
nickname = li_col_03
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_police02
{dock_props}

[Object]
nickname = li_col_03_airlock01
pos = 0, 0, 1110
rotate = 0, 180, 0
archetype = space_airlock_dummy
parent = li_col_03

[Object]
nickname = li_col_03_airlock02
pos = 0, 0, 10
rotate = 0, 0, 0
archetype = space_airlock_dummy
parent = li_col_03

[Object]
nickname = li_col_03_control01
pos = 0, 0, 1150
rotate = 90, 0, 0
archetype = space_small_control_tower
parent = li_col_03

[Object]
nickname = li_col_03_control02
pos = 0, 0, 1150
rotate = 0, 0, 0
archetype = space_industrialc
parent = li_col_03

[Object]
nickname = li_col_03_control_tower01
pos = 0, 65, 560
rotate = 90, 0, 0
archetype = space_control_tower
parent = li_col_03

[Object]
nickname = li_col_03_control_tower02
pos = 0, 0, 1010
rotate = -90, 0, 0
archetype = space_medium_control_tower
parent = li_col_03

[Object]
nickname = li_col_03_control_tower03
pos = 0, 0, 110
rotate = 90, 0, 0
archetype = space_medium_control_tower
parent = li_col_03

[Object]
nickname = li_col_03_factoryA01
pos = -100, 110, 345
rotate = 0, 0, 0
archetype = space_large_production
loadout = mplatform_module_red
parent = li_col_03

[Object]
nickname = li_col_03_factoryA02
pos = -200, -15, 345
rotate = 0, 0, 0
archetype = space_large_production
loadout = mplatform_module_red
parent = li_col_03

[Object]
nickname = li_col_03_factoryA03
pos = 100, 110, 345
rotate = 0, 0, 0
archetype = space_large_production
loadout = mplatform_module_red
parent = li_col_03

[Object]
nickname = li_col_03_factoryA04
pos = 200, -15, 345
rotate = 0, 0, 0
archetype = space_large_production
loadout = mplatform_module_red
parent = li_col_03

[Object]
nickname = li_col_03_station_pnlA01
pos = 0, 285, 410
rotate = 0, 90, 0
archetype = space_station_panelb
parent = li_col_03

[Object]
nickname = li_col_03_station_pnlA02
pos = 0, 185, 260
rotate = 0, 90, 0
archetype = space_station_panelb
parent = li_col_03

[Object]
nickname = li_col_03_indA01
pos = 100, 0, 240
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_03

[Object]
nickname = li_col_03_indA02
pos = 100, 0, 440
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_03

[Object]
nickname = li_col_03_indA03
pos = -100, 0, 240
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_03

[Object]
nickname = li_col_03_indA04
pos = -100, 0, 440
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_03

[Object]
nickname = li_col_03_indA05
pos = 0, 63, 240
rotate = 0, 0, 45
archetype = space_industriala
parent = li_col_03

[Object]
nickname = li_col_03_indA06
pos = 0, 63, 440
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_03

[Object]
nickname = li_col_03_indA07
pos = 0, -65, 340
rotate = 0, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_col_03

[Object]
nickname = li_col_03_indA08
pos = 0, -65, 440
rotate = 0, 0, 0
archetype = space_industrialc
parent = li_col_03

[Object]
nickname = li_col_03_indA09
pos = 0, -65, 240
rotate = 0, 180, 0
archetype = space_industrialc
parent = li_col_03

[Object]
nickname = li_col_03_indA10
pos = 0, 145, 410
rotate = 0, 0, 90
archetype = space_industrial02d
parent = li_col_03

[Object]
nickname = li_col_03_panelA01
pos = 0, 185, 560
rotate = 0, 0, 0
archetype = space_solar_pnl
parent = li_col_03

[Object]
nickname = li_col_03_panelA02
pos = 0, 285, 410
rotate = 0, 0, 0
archetype = space_solar_pnl
parent = li_col_03

[Object]
nickname = li_col_03_panelA03
pos = 0, 185, 260
rotate = 0, 0, 0
archetype = space_solar_pnl
parent = li_col_03

[Object]
nickname = li_col_03_factoryB01
pos = -100, 110, 775
rotate = 0, 180, 0
archetype = space_large_production
loadout = mplatform_module_red
parent = li_col_03

[Object]
nickname = li_col_03_factoryB02
pos = -200, -15, 775
rotate = 0, 180, 0
archetype = space_large_production
loadout = mplatform_module_red
parent = li_col_03

[Object]
nickname = li_col_03_factoryB03
pos = 100, 110, 775
rotate = 0, 180, 0
archetype = space_large_production
loadout = mplatform_module_red
parent = li_col_03

[Object]
nickname = li_col_03_factoryB04
pos = 200, -15, 775
rotate = 0, 180, 0
archetype = space_large_production
loadout = mplatform_module_red
parent = li_col_03

[Object]
nickname = li_col_03_station_pnlB01
pos = 0, 285, 710
rotate = 0, 90, 0
archetype = space_station_panelb
parent = li_col_03

[Object]
nickname = li_col_03_station_pnlB02
pos = 0, 185, 860
rotate = 0, 90, 0
archetype = space_station_panelb
parent = li_col_03

[Object]
nickname = li_col_03_indB01
pos = 100, 0, 880
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_03

[Object]
nickname = li_col_03_indB02
pos = 100, 0, 680
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_03

[Object]
nickname = li_col_03_indB03
pos = -100, 0, 880
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_03

[Object]
nickname = li_col_03_indB04
pos = -100, 0, 680
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_03

[Object]
nickname = li_col_03_indB05
pos = 0, 63, 880
rotate = 0, 0, 45
archetype = space_industriala
parent = li_col_03

[Object]
nickname = li_col_03_indB06
pos = 0, 63, 680
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_03

[Object]
nickname = li_col_03_indB07
pos = 0, -65, 780
rotate = 0, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_col_03

[Object]
nickname = li_col_03_indB08
pos = 0, -65, 680
rotate = 0, 180, 0
archetype = space_industrialc
parent = li_col_03

[Object]
nickname = li_col_03_indB09
pos = 0, -65, 880
rotate = 0, 0, 0
archetype = space_industrialc
parent = li_col_03

[Object]
nickname = li_col_03_indB10
pos = 0, 145, 710
rotate = 0, 0, 90
archetype = space_industrial02d
parent = li_col_03

[Object]
nickname = li_col_03_panelB02
pos = 0, 285, 710
rotate = 0, 0, 0
archetype = space_solar_pnl
parent = li_col_03

[Object]
nickname = li_col_03_panelB03
pos = 0, 185, 860
rotate = 0, 0, 0
archetype = space_solar_pnl
parent = li_col_03
'''


class ColumbiaSmallProduction(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_col_03'
    TEMPLATE = '''[Object]
nickname = li_col_03
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_police02

[Object]
nickname = li_col_03_airlock01
pos = 0, 0, 680
rotate = 0, 180, 0
archetype = space_airlock_dummy
parent = li_col_03

[Object]
nickname = li_col_03_airlock02
pos = 0, 0, 10
rotate = 0, 0, 0
archetype = space_airlock_dummy
parent = li_col_03

[Object]
nickname = li_col_03_control01
pos = 0, 0, 730
rotate = 90, 0, 0
archetype = space_small_control_tower
parent = li_col_03

[Object]
nickname = li_col_03_control_tower02
pos = 0, 0, 565
rotate = 90, 0, 0
archetype = space_medium_control_tower
parent = li_col_03

[Object]
nickname = li_col_03_control_tower03
pos = 0, 0, 110
rotate = 90, 0, 0
archetype = space_medium_control_tower
parent = li_col_03

[Object]
nickname = li_col_03_factoryA01
pos = -100, 110, 345
rotate = 0, 0, 0
archetype = space_large_production
loadout = mplatform_module_red
parent = li_col_03

[Object]
nickname = li_col_03_factoryA02
pos = -200, -15, 345
rotate = 0, 0, 0
archetype = space_large_production
loadout = mplatform_module_red
parent = li_col_03

[Object]
nickname = li_col_03_factoryA03
pos = 100, 110, 345
rotate = 0, 0, 0
archetype = space_large_production
loadout = mplatform_module_red
parent = li_col_03

[Object]
nickname = li_col_03_factoryA04
pos = 200, -15, 345
rotate = 0, 0, 0
archetype = space_large_production
loadout = mplatform_module_red
parent = li_col_03

[Object]
nickname = li_col_03_station_pnlA01
pos = 2, 285, 350
rotate = 0, 90, 0
archetype = space_station_panelb
parent = li_col_03

[Object]
nickname = li_col_03_station_pnlA02
pos = 0, 185, 170
rotate = 0, 90, 0
archetype = space_station_panelb
parent = li_col_03

[Object]
nickname = li_col_03_station_pnlA03
pos = 0, 185, 520
rotate = 0, 90, 0
archetype = space_station_panelb
parent = li_col_03

[Object]
nickname = li_col_03_indA01
pos = 100, 0, 240
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_03

[Object]
nickname = li_col_03_indA02
pos = 100, 0, 440
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_03

[Object]
nickname = li_col_03_indA03
pos = -100, 0, 240
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_03

[Object]
nickname = li_col_03_indA04
pos = -100, 0, 440
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_03

[Object]
nickname = li_col_03_indA05
pos = 0, 63, 240
rotate = 0, 0, 45
archetype = space_industriala
parent = li_col_03

[Object]
nickname = li_col_03_indA06
pos = 0, 63, 440
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_03

[Object]
nickname = li_col_03_indA07
pos = 0, -65, 340
rotate = 0, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = li_col_03

[Object]
nickname = li_col_03_indA08
pos = 0, -65, 440
rotate = 0, 0, 0
archetype = space_industrialc
parent = li_col_03

[Object]
nickname = li_col_03_indA09
pos = 0, -65, 240
rotate = 0, 180, 0
archetype = space_industrialc
parent = li_col_03

[Object]
nickname = li_col_03_indA10
pos = 0, 145, 410
rotate = 0, 0, 90
archetype = space_industrial02d
parent = li_col_03

[Object]
nickname = li_col_03_panelA01
pos = 0, 185, 520
rotate = 0, 0, 0
archetype = space_solar_pnl
parent = li_col_03

[Object]
nickname = li_col_03_panelA02
pos = 0, 285, 350
rotate = 0, 0, 0
archetype = space_solar_pnl
parent = li_col_03

[Object]
nickname = li_col_03_panelA03
pos = 0, 185, 170
rotate = 0, 0, 0
archetype = space_solar_pnl
parent = li_col_03
'''
