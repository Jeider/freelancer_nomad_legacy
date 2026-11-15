from templates.space_object_template import SpaceObjectTemplate


class ColumbiaProductionOriginal(SpaceObjectTemplate):
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
{dock_props}

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


class ColumbiaProduction(ColumbiaProductionOriginal):
    TEMPLATE = '''[Object]
nickname = li_col_03
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_police02
{dock_props}

[Object]
nickname = li_col_03_airlock01
pos = 0, 110, 580
rotate = 0, 0, 0
archetype = batch_columbia_production_structure0
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
nickname = li_col_03_batch_columbia_production_structure0_collision00
pos = 4.14702868e-06, 1.90734863e-05, 615.770041
rotate = 0, 0, 0
archetype = batch_columbia_production_structure0_collision00
parent = li_col_03

[Object]
nickname = li_col_03_batch_columbia_production_structure0_collision01
pos = -0.0679779053, 64.9856942, 785
rotate = 0, 0, 0
archetype = batch_columbia_production_structure0_collision01
parent = li_col_03

[Object]
nickname = li_col_03_batch_columbia_production_structure0_collision02
pos = 19.6742134, 135.387146, 324.705443
rotate = 0, 0, 0
archetype = batch_columbia_production_structure0_collision02
parent = li_col_03

[Object]
nickname = li_col_03_batch_columbia_production_structure0_collision03
pos = -50.0127678, 31.7224998, 341.764076
rotate = 0, 0, 0
archetype = batch_columbia_production_structure0_collision03
parent = li_col_03

[Object]
nickname = li_col_03_batch_columbia_production_structure0_collision04
pos = -0.182491302, 221.166191, 540.605572
rotate = 0, 0, 0
archetype = batch_columbia_production_structure0_collision04
parent = li_col_03

[Object]
nickname = li_col_03_batch_columbia_production_structure0_collision05
pos = -0.0127677917, 24.7348461, 781.764076
rotate = 0, 0, 0
archetype = batch_columbia_production_structure0_collision05
parent = li_col_03

[Object]
nickname = li_col_03_batch_columbia_production_structure0_collision06
pos = -0.182491302, 221.166191, 780
rotate = 0, 0, 0
archetype = batch_columbia_production_structure0_collision06
parent = li_col_03

'''
