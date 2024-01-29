from templates.space_object_template import SpaceObjectTemplate


class StuttgartMegabase(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_stut_04'
    TEMPLATE = '''[Object]
nickname = rh_stut_04
pos = 0, -1650, 0
rotate = 0, 0, 0
archetype = manhaim_core
base = rh_stut_04_base
reputation = rc_grp
behavior = NOTHING
ids_name = 203620
ids_info = 065558

[Object]
nickname = rh_stut_04_dock
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_port_dmg_dock
base = rh_stut_04_base
dock_with = rh_stut_04_base
reputation = rc_grp
behavior = NOTHING
ids_name = 196722
ids_info = 065739
voice = atc_leg_m01
space_costume = rh_bartender_head, rh_shipdealer_body, prop_neuralnet_e

;RIGHT FACTORIES

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_ind01
pos = 500, -1650, 0
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_ind02
pos = 500, -1250, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_ind03
pos = 500, -2050, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_ind04
pos = 500, -1450, 350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_ind05
pos = 500, -1850, 350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_ind06
pos = 500, -1650, 270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_ind07
pos = 500, -1450, -350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_ind08
pos = 500, -1850, -350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_ind09
pos = 500, -1650, -270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_conn01
pos = 580, -1535, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_conn02
pos = 420, -1535, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_conn03
pos = 580, -1765, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_conn04
pos = 420, -1765, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_conn05
pos = 580, -1535, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_conn06
pos = 420, -1535, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_conn07
pos = 580, -1765, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_conn08
pos = 420, -1765, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_prod01
pos = 500, -1610, 130
rotate = 0, 180, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_prod02
pos = 500, -1690, 130
rotate = 180, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_prod03
pos = 500, -1610, -130
rotate = 0, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_prod04
pos = 500, -1690, -130
rotate = 0, 0, 180
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_gird01
pos = 500, -1450, 350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_gird02
pos = 500, -1450, 350
rotate = -41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_gird03
pos = 500, -1850, 350
rotate = 41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_gird04
pos = 500, -1450, -350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_gird05
pos = 500, -1450, -350
rotate = -41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_gird06
pos = 500, -1850, -350
rotate = 41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_tube01
pos = 500, -1250, 0
rotate = 90, 0, 0
archetype = space_short_tube
parent = rh_stut_04


[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_ind01
pos = 900, -1650, 0
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_ind02
pos = 900, -1250, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_ind03
pos = 900, -2050, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_ind04
pos = 900, -1450, 350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_ind05
pos = 900, -1850, 350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_ind06
pos = 900, -1650, 270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_ind07
pos = 900, -1450, -350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_ind08
pos = 900, -1850, -350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_ind09
pos = 900, -1650, -270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_conn01
pos = 980, -1535, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_conn02
pos = 820, -1535, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_conn03
pos = 980, -1765, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_conn04
pos = 820, -1765, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_conn05
pos = 980, -1535, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_conn06
pos = 820, -1535, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_conn07
pos = 980, -1765, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_conn08
pos = 820, -1765, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_prod01
pos = 900, -1610, 130
rotate = 0, 180, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_prod02
pos = 900, -1690, 130
rotate = 180, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_prod03
pos = 900, -1610, -130
rotate = 0, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_prod04
pos = 900, -1690, -130
rotate = 0, 0, 180
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_gird01
pos = 900, -1450, 350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_gird02
pos = 900, -1450, 350
rotate = -41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_gird03
pos = 900, -1850, 350
rotate = 41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_gird04
pos = 900, -1450, -350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_gird05
pos = 900, -1450, -350
rotate = -41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_gird06
pos = 900, -1850, -350
rotate = 41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_tube01
pos = 900, -1250, 0
rotate = 90, 0, 0
archetype = space_short_tube
parent = rh_stut_04


[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_ind01
pos = 1300, -1650, 0
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_ind02
pos = 1300, -1250, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_ind03
pos = 1300, -2050, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_ind04
pos = 1300, -1450, 350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_ind05
pos = 1300, -1850, 350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_ind06
pos = 1300, -1650, 270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_ind07
pos = 1300, -1450, -350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_ind08
pos = 1300, -1850, -350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_ind09
pos = 1300, -1650, -270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_conn01
pos = 1380, -1535, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_conn02
pos = 1220, -1535, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_conn03
pos = 1380, -1765, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_conn04
pos = 1220, -1765, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_conn05
pos = 1380, -1535, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_conn06
pos = 1220, -1535, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_conn07
pos = 1380, -1765, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_conn08
pos = 1220, -1765, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_prod01
pos = 1300, -1610, 130
rotate = 0, 180, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_prod02
pos = 1300, -1690, 130
rotate = 180, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_prod03
pos = 1300, -1610, -130
rotate = 0, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_prod04
pos = 1300, -1690, -130
rotate = 0, 0, 180
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_gird01
pos = 1300, -1450, 350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_gird02
pos = 1300, -1450, 350
rotate = -41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_gird03
pos = 1300, -1850, 350
rotate = 41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_gird04
pos = 1300, -1450, -350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_gird05
pos = 1300, -1450, -350
rotate = -41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_gird06
pos = 1300, -1850, -350
rotate = 41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_tube01
pos = 1300, -1250, 0
rotate = 90, 0, 0
archetype = space_short_tube
parent = rh_stut_04


[Object]
nickname = rh_stut_04_RIGHT_MINER_ind01
pos = 1720, -1650, 0
rotate = 90, 0, 90
archetype = space_industrial02d
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_MINER_ind02
pos = 1590, -1560, 0
rotate = 90, 0, 90
archetype = space_industrial01b
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_MINER_ind03
pos = 1590, -1740, 0
rotate = 90, 0, 90
archetype = space_industrial01b
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_MINER_ind04
pos = 1470, -1578, 0
rotate = -12, 90, 90
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_MINER_ind05
pos = 1470, -1722, 0
rotate = -12, -90, 90
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_MINER_miner01
pos = 1720, -1510, 0
rotate = 0, 90, 0
archetype = gas_miner_core
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_MINER_miner02
pos = 1720, -1790, 0
rotate = 0, 90, 180
archetype = gas_miner_core
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_gird01
pos = 1300, -1450, 350
rotate = -90, 45, 90
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_gird02
pos = 900, -1450, 350
rotate = -90, 45, 90
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_gird03
pos = 1300, -1450, -350
rotate = -90, 45, 90
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_gird04
pos = 900, -1450, -350
rotate = -90, 45, 90
archetype = space_girdera
parent = rh_stut_04

;LEFT FACTORIES 

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind01
pos = -500, -1650, 0
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind02
pos = -500, -1250, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind03
pos = -500, -2050, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind04
pos = -500, -1450, 350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind05
pos = -500, -1850, 350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind06
pos = -500, -1650, 270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind07
pos = -500, -1450, -350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind08
pos = -500, -1850, -350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind09
pos = -500, -1650, -270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn01
pos = -420, -1535, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn02
pos = -580, -1535, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn03
pos = -420, -1765, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn04
pos = -580, -1765, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn05
pos = -420, -1535, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn06
pos = -580, -1535, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn07
pos = -420, -1765, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn08
pos = -580, -1765, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_prod01
pos = -500, -1610, 130
rotate = 0, 180, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_prod02
pos = -500, -1690, 130
rotate = 180, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_prod03
pos = -500, -1610, -130
rotate = 0, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_prod04
pos = -500, -1690, -130
rotate = 0, 0, 180
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird01
pos = -500, -1450, 350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird02
pos = -500, -1450, 350
rotate = -41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird03
pos = -500, -1850, 350
rotate = 41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird04
pos = -500, -1450, -350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird05
pos = -500, -1450, -350
rotate = -41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird06
pos = -500, -1850, -350
rotate = 41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_tube01
pos = -500, -1250, 0
rotate = 90, 0, 0
archetype = space_short_tube
parent = rh_stut_04


[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind01
pos = -900, -1650, 0
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind02
pos = -900, -1250, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind03
pos = -900, -2050, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind04
pos = -900, -1450, 350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind05
pos = -900, -1850, 350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind06
pos = -900, -1650, 270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind07
pos = -900, -1450, -350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind08
pos = -900, -1850, -350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind09
pos = -900, -1650, -270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn01
pos = -820, -1535, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn02
pos = -980, -1535, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn03
pos = -820, -1765, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn04
pos = -980, -1765, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn05
pos = -820, -1535, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn06
pos = -980, -1535, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn07
pos = -820, -1765, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn08
pos = -980, -1765, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_prod01
pos = -900, -1610, 130
rotate = 0, 180, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_prod02
pos = -900, -1690, 130
rotate = 180, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_prod03
pos = -900, -1610, -130
rotate = 0, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_prod04
pos = -900, -1690, -130
rotate = 0, 0, 180
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_gird01
pos = -900, -1450, 350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_gird02
pos = -900, -1450, 350
rotate = -41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_gird03
pos = -900, -1850, 350
rotate = 41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_gird04
pos = -900, -1450, -350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_gird05
pos = -900, -1450, -350
rotate = -41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_gird06
pos = -900, -1850, -350
rotate = 41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_tube01
pos = -900, -1250, 0
rotate = 90, 0, 0
archetype = space_short_tube
parent = rh_stut_04


[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind01
pos = -1300, -1650, 0
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind02
pos = -1300, -1250, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind03
pos = -1300, -2050, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind04
pos = -1300, -1450, 350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind05
pos = -1300, -1850, 350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind06
pos = -1300, -1650, 270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind07
pos = -1300, -1450, -350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind08
pos = -1300, -1850, -350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind09
pos = -1300, -1650, -270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn01
pos = -1220, -1535, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn02
pos = -1380, -1535, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn03
pos = -1220, -1765, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn04
pos = -1380, -1765, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn05
pos = -1220, -1535, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn06
pos = -1380, -1535, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn07
pos = -1220, -1765, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn08
pos = -1380, -1765, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_prod01
pos = -1300, -1610, 130
rotate = 0, 180, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_prod02
pos = -1300, -1690, 130
rotate = 180, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_prod03
pos = -1300, -1610, -130
rotate = 0, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_prod04
pos = -1300, -1690, -130
rotate = 0, 0, 180
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird01
pos = -1300, -1450, 350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird02
pos = -1300, -1450, 350
rotate = -41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird03
pos = -1300, -1850, 350
rotate = 41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird04
pos = -1300, -1450, -350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird05
pos = -1300, -1450, -350
rotate = -41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird06
pos = -1300, -1850, -350
rotate = 41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_tube01
pos = -1300, -1250, 0
rotate = 90, 0, 0
archetype = space_short_tube
parent = rh_stut_04


[Object]
nickname = rh_stut_04_LEFT_MINER_ind01
pos = -1720, -1650, 0
rotate = 90, 0, 90
archetype = space_industrial02d
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_MINER_ind02
pos = -1590, -1560, 0
rotate = 90, 0, 90
archetype = space_industrial01b
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_MINER_ind03
pos = -1590, -1740, 0
rotate = 90, 0, 90
archetype = space_industrial01b
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_MINER_ind04
pos = -1470, -1578, 0
rotate = -12, -90, -90
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_MINER_ind05
pos = -1470, -1722, 0
rotate = -12, 90, -90
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_MINER_miner01
pos = -1720, -1510, 0
rotate = 0, 90, 0
archetype = gas_miner_core
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_MINER_miner02
pos = -1720, -1790, 0
rotate = 0, 90, 180
archetype = gas_miner_core
parent = rh_stut_04


[Object]
nickname = rh_stut_04_LEFT_gird01
pos = -1300, -1450, 350
rotate = 90, 45, 90
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_gird02
pos = -900, -1450, 350
rotate = 90, 45, 90
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_gird03
pos = -1300, -1450, -350
rotate = 90, 45, 90
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_gird04
pos = -900, -1450, -350
rotate = 90, 45, 90
archetype = space_girdera
parent = rh_stut_04


;STATION CORE

[Object]
nickname = rh_stut_04_CORE_the
pos = 0, -1650, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_tube01
pos = 0, -2050, 0
rotate = 90, 0, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_tube02
pos = 50, -1650, 0
rotate = 0, 90, 0
archetype = space_tube_fix
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_tube03
pos = 0, -1250, 0
rotate = -90, 0, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_tube04
pos = -50, -1650, 0
rotate = 0, -90, 0
archetype = space_tube_fix
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_tube05
pos = 0, -1650, 375
rotate = 0, 180, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_ind01
pos = 250, -1650, 250
rotate = 90, 45, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_ind02
pos = -250, -1650, 250
rotate = 90, 45, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_ind03
pos = 250, -1650, -250
rotate = 90, 45, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_ind04
pos = -250, -1650, -250
rotate = 90, 45, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_ind05
pos = 125, -1350, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_ind06
pos = 0, -1350, 125
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_ind07
pos = -125, -1350, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_ind08
pos = 0, -1350, -125
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_ind09
pos = 125, -1950, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_ind10
pos = 0, -1950, 125
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_ind11
pos = -125, -1950, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_ind12
pos = 0, -1950, -125
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_girder01
pos = 250, -1500, 250
rotate = 0, -135, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_girder02
pos = -250, -1500, 250
rotate = 0, 135, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_girder03
pos = 250, -1500, -250
rotate = 0, -45, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_girder04
pos = -250, -1500, -250
rotate = 0, 45, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_girder05
pos = 250, -1800, 250
rotate = 0, -135, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_girder06
pos = -250, -1800, 250
rotate = 0, 135, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_girder07
pos = 250, -1800, -250
rotate = 0, -45, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_girder08
pos = -250, -1800, -250
rotate = 0, 45, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_girder09
pos = 500, -1250, 0
rotate = 0, -90, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_girder10
pos = -500, -1250, 0
rotate = 0, 90, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_girder11
pos = 500, -2050, 0
rotate = 0, -90, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_girder12
pos = -500, -2050, 0
rotate = 0, 90, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_twr01
pos = 0, -1500, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_twr02
pos = 0, -1800, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_twr03
pos = 0, -1210, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_twr04
pos = 0, -2100, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_twr05
pos = 250, -1500, 250
rotate = 0, 45, 0
archetype = space_small_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_twr06
pos = 250, -1800, 250
rotate = 0, 45, 0
archetype = space_small_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_twr07
pos = -250, -1500, 250
rotate = 0, -45, 0
archetype = space_small_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_twr08
pos = -250, -1800, 250
rotate = 0, -45, 0
archetype = space_small_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_twr09
pos = 250, -1500, -250
rotate = 0, -45, 0
archetype = space_small_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_twr10
pos = 250, -1800, -250
rotate = 0, -45, 0
archetype = space_small_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_twr11
pos = -250, -1500, -250
rotate = 0, 45, 0
archetype = space_small_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_twr12
pos = -250, -1800, -250
rotate = 0, 45, 0
archetype = space_small_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_twr13
pos = 300, -1250, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_twr14
pos = -300, -1250, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_twr15
pos = 300, -2050, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_twr16
pos = -300, -2050, 0
rotate = 0, 90, 0
archetype = space_small_control_tower
parent = rh_stut_04

;FRONT

[Object]
nickname = rh_stut_04_FRONT_ind01
pos = 1, -1250, 250
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_FRONT_ind02
pos = 0, -1450, 350
rotate = 90, 20, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_FRONT_ind03
pos = 0, -1850, 350
rotate = 90, -20, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_FRONT_ind04
pos = 1, -2050, 250
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_FRONT_ind05
pos = 0, -1650, 400
rotate = 90, 0, 90
archetype = space_industrial02d
parent = rh_stut_04

[Object]
nickname = rh_stut_04_FRONT_tube01
pos = -400, -1450, 350
rotate = 0, 90, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_FRONT_tube02
pos = -400, -1850, 350
rotate = 0, 90, 0
archetype = space_short_tube
parent = rh_stut_04


[Object]
nickname = rh_stut_04_FRONT_girder01
pos = 0, -1450, 350
rotate = 70, 0, 0
archetype = space_girder
parent = rh_stut_04

[Object]
nickname = rh_stut_04_FRONT_girder02
pos = 0, -1850, 350
rotate = -70, 0, 0
archetype = space_girder
parent = rh_stut_04

[Object]
nickname = rh_stut_04_FRONT_girder03
pos = -300, -1250, 0
rotate = 0, 36, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_FRONT_girder04
pos = 300, -1250, 0
rotate = 0, -36, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_FRONT_shipyard01
pos = 0, -1130, 250
rotate = 0, 90, 0
archetype = shipyard
parent = rh_stut_04

[Object]
nickname = rh_stut_04_FRONT_shipyard02
pos = 0, -1650, 500
rotate = 90, 0, 90
archetype = shipyard
parent = rh_stut_04

[Object]
nickname = rh_stut_04_FRONT_shipyard03
pos = 0, -2170, 250
rotate = 180, 90, 0
archetype = shipyard
parent = rh_stut_04

;BACK

[Object]
nickname = rh_stut_04_BACK_ind01
pos = 1, -1250, -250
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BACK_ind02
pos = 0, -1450, -350
rotate = 90, -20, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BACK_ind03
pos = 0, -1850, -350
rotate = 90, 20, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BACK_ind04
pos = 1, -2050, -250
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BACK_ind05
pos = 0, -1650, -400
rotate = 90, 0, 90
archetype = space_industrial02d
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BACK_tube01
pos = -400, -1450, -350
rotate = 0, 90, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BACK_tube02
pos = -400, -1850, -350
rotate = 0, 90, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BACK_girder01
pos = 0, -1450, -350
rotate = -70, 0, 0
archetype = space_girder
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BACK_girder02
pos = 0, -1850, -350
rotate = 70, 0, 0
archetype = space_girder
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BACK_girder03
pos = -300, -1250, 0
rotate = 0, 144, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BACK_girder04
pos = 300, -1250, 0
rotate = 0, -144, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BACK_shipyard01
pos = 0, -1130, -250
rotate = 0, -90, 0
archetype = shipyard
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BACK_shipyard02
pos = 0, -1650, -500
rotate = -90, 0, 90
archetype = shipyard
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BACK_shipyard03
pos = 0, -2170, -250
rotate = 180, -90, 0
archetype = shipyard
parent = rh_stut_04

;TOP DOCK AND HILL

[Object]
nickname = rh_stut_04_TOP_airlock
pos = 0, -165, 0
rotate = 90, 45, 0
archetype = space_airlock_dummy
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_tube01
pos = 150, -1250, 0
rotate = -90, 0, 11
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_tube02
pos = -150, -1250, 0
rotate = -90, 0, -11
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_ind01
pos = 0, -550, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_ind02
pos = 0, -350, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_twr01
pos = 0, -640, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_twr02
pos = 0, -550, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_twr03
pos = 0, -460, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_twr04
pos = 0, -295, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_habitatA01
pos = 150, -550, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_habitatA02
pos = 0, -550, 150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_habitatA03
pos = -150, -550, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_habitatA04
pos = 0, -550, -150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_habitatA05
pos = 100, -550, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_habitatA06
pos = 100, -550, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_habitatA07
pos = -100, -550, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_habitatA08
pos = -100, -550, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_habitatB01
pos = 100, -380, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_habitatB02
pos = 0, -380, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_habitatB03
pos = -100, -380, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_habitatB04
pos = 0, -380, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_habitatB05
pos = 70, -380, 70
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_habitatB06
pos = -70, -380, 70
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_habitatB07
pos = 70, -380, -70
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_habitatB08
pos = -70, -380, -70
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

;BOTTOM HILL


[Object]
nickname = rh_stut_04_BOTTOM_airlock
pos = 0, -3135, 0
rotate = -90, 45, 0
archetype = space_airlock_dummy
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_tube01
pos = 150, -2050, 0
rotate = 90, 0, -11
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_tube02
pos = -150, -2050, 0
rotate = 90, 0, 11
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_ind01
pos = 0, -2750, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_ind02
pos = 0, -2950, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_twr01
pos = 0, -2660, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_twr02
pos = 0, -2750, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_twr03
pos = 0, -2840, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_twr04
pos = 0, -3005, 0
rotate = 0, 0, 0
archetype = space_medium_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_ctrl01
pos = 0, -3255, 0
rotate = 180, 0, 0
archetype = space_small_control_block
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_twr05
pos = 0, -3190, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_habitatA01
pos = 150, -2750, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_habitatA02
pos = 0, -2750, 150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_habitatA03
pos = -150, -2750, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_habitatA04
pos = 0, -2750, -150
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_habitatA05
pos = 100, -2750, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_habitatA06
pos = 100, -2750, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_habitatA07
pos = -100, -2750, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_habitatA08
pos = -100, -2750, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_habitatB01
pos = 100, -2920, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_habitatB02
pos = 0, -2920, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_habitatB03
pos = -100, -2920, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_habitatB04
pos = 0, -2920, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_habitatB05
pos = 70, -2920, 70
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_habitatB06
pos = -70, -2920, 70
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_habitatB07
pos = 70, -2920, -70
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_habitatB08
pos = -70, -2920, -70
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = rh_stut_04
'''
