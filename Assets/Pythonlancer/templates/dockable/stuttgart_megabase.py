from templates.space_object_template import SpaceObjectTemplate


class StuttgartMegabaseOriginal(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_stut_04'
    TEMPLATE = '''[Object]
nickname = rh_stut_04
pos = 0, -1650, 0
rotate = 0, 0, 0
archetype = manhaim_core
{root_props}

[Object]
nickname = rh_stut_04_dock
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_port_dmg_dock
{dock_props}

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


class MannhaimShort(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_stut_04'
    TEMPLATE = '''[Object]
nickname = rh_stut_04
pos = 0, 0, 1230
rotate = 0, 90, 0
archetype = space_shipping01
{dock_props}

[Object]
nickname = rh_stut_04_RIGHT_MINER_ind01
pos = 820, 0, 0
rotate = 90, 0, 90
archetype = space_industrial02d
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_MINER_ind02
pos = 690, 90, 0
rotate = 90, 0, 90
archetype = space_industrial01b
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_MINER_ind03
pos = 690, -90, 0
rotate = 90, 0, 90
archetype = space_industrial01b
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_MINER_ind04
pos = 570, 72, 0
rotate = -12, 90, 90
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_MINER_ind05
pos = 570, -72, 0
rotate = -12, -90, 90
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_MINER_miner01
pos = 820, 140, 0
rotate = 0, 90, 0
archetype = gas_miner_core
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_MINER_miner02
pos = 820, -140, 0
rotate = 0, 90, 180
archetype = gas_miner_core
parent = rh_stut_04

[Object]
nickname = rh_stut_04_ind01
pos = 0, 0, 440
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_ind02
pos = 0, 0, -440
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_ind03
pos = 0, 0, -600
rotate = 90, 0, 90
archetype = space_industrial02d
parent = rh_stut_04

[Object]
nickname = rh_stut_04_ind03
pos = 0, 0, -955
rotate = 0, 90, 0
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_shipyard01
pos = 0, -30, -760
rotate = 0, 90, 0
archetype = shipyard
parent = rh_stut_04

[Object]
nickname = rh_stut_04_shipyard01
pos = 0, -30, -1150
rotate = 0, 90, 0
archetype = shipyard
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_tube04
pos = 400, 0, 0
rotate = 0, -90, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_tube04
pos = 400, 400, 0
rotate = 0, -90, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_tube04
pos = 400, -400, 0
rotate = 0, -90, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind01
pos = 400, 0, 0
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind02
pos = 400, 400, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind03
pos = 400, -400, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind04
pos = 400, 200, 350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind05
pos = 400, -200, 350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind06
pos = 400, 0, 270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind07
pos = 400, 200, -350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind08
pos = 400, -200, -350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind09
pos = 400, 0, -270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn01
pos = 480, 115, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn02
pos = 320, 115, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn03
pos = 480, -115, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn04
pos = 320, -115, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn05
pos = 480, 115, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn06
pos = 320, 115, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn07
pos = 480, -115, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn08
pos = 320, -115, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_prod01
pos = 400, 40, 130
rotate = 0, 180, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_prod02
pos = 400, -40, 130
rotate = 180, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_prod03
pos = 400, 40, -130
rotate = 0, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_prod04
pos = 400, -40, -130
rotate = 0, 0, 180
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird01
pos = 400, 200, 350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird02
pos = 400, 200, 350
rotate = -41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird03
pos = 400, -200, 350
rotate = 41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird04
pos = 400, 200, -350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird05
pos = 400, 200, -350
rotate = -41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird06
pos = 400, -200, -350
rotate = 41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_tube01
pos = 400, 400, 0
rotate = 90, 0, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind01
pos = 0, 0, 0
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind02
pos = 0, 400, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind03
pos = 0, -400, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind04
pos = 0, 200, 350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind05
pos = 0, -200, 350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind06
pos = 0, 0, 270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind07
pos = 0, 200, -350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind08
pos = 0, -200, -350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind09
pos = 0, 0, -270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn01
pos = 80, 115, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn02
pos = -80, 115, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn03
pos = 80, -115, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn04
pos = -80, -115, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn05
pos = 80, 115, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn06
pos = -80, 115, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn07
pos = 80, -115, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn08
pos = -80, -115, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_prod01
pos = 0, 40, 130
rotate = 0, 180, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_prod02
pos = 0, -40, 130
rotate = 180, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_prod03
pos = 0, 40, -130
rotate = 0, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_prod04
pos = 0, -40, -130
rotate = 0, 0, 180
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_gird02
pos = 0, 200, 350
rotate = -41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_gird03
pos = 0, -200, 350
rotate = 41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_gird05
pos = 0, 200, -350
rotate = -41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_gird06
pos = 0, -200, -350
rotate = 41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_tube01
pos = 0, 400, 0
rotate = 90, 0, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind01
pos = -400, 0, 0
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind02
pos = -400, 400, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind03
pos = -400, -400, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind04
pos = -400, 200, 350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind05
pos = -400, -200, 350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind06
pos = -400, 0, 270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind07
pos = -400, 200, -350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind08
pos = -400, -200, -350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind09
pos = -400, 0, -270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn01
pos = -320, 115, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn02
pos = -480, 115, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn03
pos = -320, -115, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn04
pos = -480, -115, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn05
pos = -320, 115, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn06
pos = -480, 115, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn07
pos = -320, -115, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn08
pos = -480, -115, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_prod01
pos = -400, 40, 130
rotate = 0, 180, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_prod02
pos = -400, -40, 130
rotate = 180, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_prod03
pos = -400, 40, -130
rotate = 0, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_prod04
pos = -400, -40, -130
rotate = 0, 0, 180
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird01
pos = -400, 200, 350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird02
pos = -400, 200, 350
rotate = -41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird03
pos = -400, -200, 350
rotate = 41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird04
pos = -400, 200, -350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird05
pos = -400, 200, -350
rotate = -41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird06
pos = -400, -200, -350
rotate = 41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_tube01
pos = -400, 400, 0
rotate = 90, 0, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_MINER_ind01
pos = -820, 0, 0
rotate = 90, 0, 90
archetype = space_industrial02d
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_MINER_ind02
pos = -690, 90, 0
rotate = 90, 0, 90
archetype = space_industrial01b
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_MINER_ind03
pos = -690, -90, 0
rotate = 90, 0, 90
archetype = space_industrial01b
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_MINER_ind04
pos = -570, 72, 0
rotate = -12, -90, -90
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_MINER_ind05
pos = -570, -72, 0
rotate = -12, 90, -90
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_MINER_miner01
pos = -820, 140, 0
rotate = 0, 90, 0
archetype = gas_miner_core
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_MINER_miner02
pos = -820, -140, 0
rotate = 0, 90, 180
archetype = gas_miner_core
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_gird01
pos = -400, 200, 350
rotate = 90, 45, 90
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_gird02
pos = 0, 200, 350
rotate = 90, 45, 90
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_gird03
pos = -400, 200, -350
rotate = 90, 45, 90
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_gird04
pos = 0, 200, -350
rotate = 90, 45, 90
archetype = space_girdera
parent = rh_stut_04
'''


class MannhaimShort(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_stut_04'
    TEMPLATE = '''[Object]
nickname = rh_stut_04
pos = 0, 0, 1230
rotate = 0, 90, 0
archetype = space_shipping01
{dock_props}

[Object]
nickname = rh_stut_04_RIGHT_MINER_ind01
pos = 820, 0, 0
rotate = 90, 0, 90
archetype = space_industrial02d
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_MINER_ind02
pos = 690, 90, 0
rotate = 90, 0, 90
archetype = space_industrial01b
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_MINER_ind03
pos = 690, -90, 0
rotate = 90, 0, 90
archetype = space_industrial01b
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_MINER_ind04
pos = 570, 72, 0
rotate = -12, 90, 90
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_MINER_ind05
pos = 570, -72, 0
rotate = -12, -90, 90
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_MINER_miner01
pos = 820, 140, 0
rotate = 0, 90, 0
archetype = gas_miner_core
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_MINER_miner02
pos = 820, -140, 0
rotate = 0, 90, 180
archetype = gas_miner_core
parent = rh_stut_04

[Object]
nickname = rh_stut_04_ind01
pos = 0, 0, 440
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_ind02
pos = 0, 0, -440
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_ind03
pos = 0, 0, -600
rotate = 90, 0, 90
archetype = space_industrial02d
parent = rh_stut_04

[Object]
nickname = rh_stut_04_ind03
pos = 0, 0, -955
rotate = 0, 90, 0
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_shipyard01
pos = 0, -30, -760
rotate = 0, 90, 0
archetype = shipyard
parent = rh_stut_04

[Object]
nickname = rh_stut_04_shipyard01
pos = 0, -30, -1150
rotate = 0, 90, 0
archetype = shipyard
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_tube04
pos = 400, 0, 0
rotate = 0, -90, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_tube04
pos = 400, 400, 0
rotate = 0, -90, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_tube04
pos = 400, -400, 0
rotate = 0, -90, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind01
pos = 400, 0, 0
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind02
pos = 400, 400, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind03
pos = 400, -400, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind04
pos = 400, 200, 350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind05
pos = 400, -200, 350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind06
pos = 400, 0, 270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind07
pos = 400, 200, -350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind08
pos = 400, -200, -350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind09
pos = 400, 0, -270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn01
pos = 480, 115, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn02
pos = 320, 115, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn03
pos = 480, -115, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn04
pos = 320, -115, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn05
pos = 480, 115, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn06
pos = 320, 115, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn07
pos = 480, -115, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn08
pos = 320, -115, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_prod01
pos = 400, 40, 130
rotate = 0, 180, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_prod02
pos = 400, -40, 130
rotate = 180, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_prod03
pos = 400, 40, -130
rotate = 0, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_prod04
pos = 400, -40, -130
rotate = 0, 0, 180
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird01
pos = 400, 200, 350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird02
pos = 400, 200, 350
rotate = -41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird03
pos = 400, -200, 350
rotate = 41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird04
pos = 400, 200, -350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird05
pos = 400, 200, -350
rotate = -41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird06
pos = 400, -200, -350
rotate = 41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_tube01
pos = 400, 400, 0
rotate = 90, 0, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind01
pos = 0, 0, 0
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind02
pos = 0, 400, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind03
pos = 0, -400, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind04
pos = 0, 200, 350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind05
pos = 0, -200, 350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind06
pos = 0, 0, 270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind07
pos = 0, 200, -350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind08
pos = 0, -200, -350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind09
pos = 0, 0, -270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn01
pos = 80, 115, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn02
pos = -80, 115, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn03
pos = 80, -115, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn04
pos = -80, -115, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn05
pos = 80, 115, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn06
pos = -80, 115, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn07
pos = 80, -115, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn08
pos = -80, -115, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_prod01
pos = 0, 40, 130
rotate = 0, 180, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_prod02
pos = 0, -40, 130
rotate = 180, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_prod03
pos = 0, 40, -130
rotate = 0, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_prod04
pos = 0, -40, -130
rotate = 0, 0, 180
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_gird02
pos = 0, 200, 350
rotate = -41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_gird03
pos = 0, -200, 350
rotate = 41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_gird05
pos = 0, 200, -350
rotate = -41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_gird06
pos = 0, -200, -350
rotate = 41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_tube01
pos = 0, 400, 0
rotate = 90, 0, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind01
pos = -400, 0, 0
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind02
pos = -400, 400, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind03
pos = -400, -400, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind04
pos = -400, 200, 350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind05
pos = -400, -200, 350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind06
pos = -400, 0, 270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind07
pos = -400, 200, -350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind08
pos = -400, -200, -350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind09
pos = -400, 0, -270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn01
pos = -320, 115, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn02
pos = -480, 115, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn03
pos = -320, -115, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn04
pos = -480, -115, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn05
pos = -320, 115, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn06
pos = -480, 115, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn07
pos = -320, -115, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn08
pos = -480, -115, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_prod01
pos = -400, 40, 130
rotate = 0, 180, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_prod02
pos = -400, -40, 130
rotate = 180, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_prod03
pos = -400, 40, -130
rotate = 0, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_prod04
pos = -400, -40, -130
rotate = 0, 0, 180
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird01
pos = -400, 200, 350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird02
pos = -400, 200, 350
rotate = -41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird03
pos = -400, -200, 350
rotate = 41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird04
pos = -400, 200, -350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird05
pos = -400, 200, -350
rotate = -41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird06
pos = -400, -200, -350
rotate = 41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_tube01
pos = -400, 400, 0
rotate = 90, 0, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_MINER_ind01
pos = -820, 0, 0
rotate = 90, 0, 90
archetype = space_industrial02d
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_MINER_ind02
pos = -690, 90, 0
rotate = 90, 0, 90
archetype = space_industrial01b
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_MINER_ind03
pos = -690, -90, 0
rotate = 90, 0, 90
archetype = space_industrial01b
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_MINER_ind04
pos = -570, 72, 0
rotate = -12, -90, -90
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_MINER_ind05
pos = -570, -72, 0
rotate = -12, 90, -90
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_MINER_miner01
pos = -820, 140, 0
rotate = 0, 90, 0
archetype = gas_miner_core
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_MINER_miner02
pos = -820, -140, 0
rotate = 0, 90, 180
archetype = gas_miner_core
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_gird01
pos = -400, 200, 350
rotate = 90, 45, 90
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_gird02
pos = 0, 200, 350
rotate = 90, 45, 90
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_gird03
pos = -400, 200, -350
rotate = 90, 45, 90
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_gird04
pos = 0, 200, -350
rotate = 90, 45, 90
archetype = space_girdera
parent = rh_stut_04
'''


class MannhaimShortGaslessOriginal(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'rh_stut_04'
    TEMPLATE = '''[Object]
nickname = rh_stut_04
pos = 0, 0, 1230
rotate = 0, 90, 0
archetype = space_shipping01
{dock_props}

[Object]
nickname = rh_stut_04_ind01
pos = 0, 0, 440
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_ind02
pos = 0, 0, -440
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_ind03
pos = 0, 0, -600
rotate = 90, 0, 90
archetype = space_industrial02d
parent = rh_stut_04

[Object]
nickname = rh_stut_04_ind03
pos = 0, 0, -955
rotate = 0, 90, 0
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_shipyard01
pos = 0, -30, -760
rotate = 0, 90, 0
archetype = shipyard
parent = rh_stut_04

[Object]
nickname = rh_stut_04_shipyard01
pos = 0, -30, -1150
rotate = 0, 90, 0
archetype = shipyard
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_tube04
pos = 400, 0, 0
rotate = 0, -90, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_tube04
pos = 400, 400, 0
rotate = 0, -90, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_tube04
pos = 400, -400, 0
rotate = 0, -90, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind01
pos = 400, 0, 0
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind02
pos = 400, 400, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind03
pos = 400, -400, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind04
pos = 400, 200, 350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind05
pos = 400, -200, 350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind06
pos = 400, 0, 270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind07
pos = 400, 200, -350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind08
pos = 400, -200, -350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind09
pos = 400, 0, -270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn01
pos = 480, 115, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn02
pos = 320, 115, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn03
pos = 480, -115, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn04
pos = 320, -115, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn05
pos = 480, 115, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn06
pos = 320, 115, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn07
pos = 480, -115, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_conn08
pos = 320, -115, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_prod01
pos = 400, 40, 130
rotate = 0, 180, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_prod02
pos = 400, -40, 130
rotate = 180, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_prod03
pos = 400, 40, -130
rotate = 0, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_prod04
pos = 400, -40, -130
rotate = 0, 0, 180
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird01
pos = 400, 200, 350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird02
pos = 400, 200, 350
rotate = -41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird03
pos = 400, -200, 350
rotate = 41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird04
pos = 400, 200, -350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird05
pos = 400, 200, -350
rotate = -41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_gird06
pos = 400, -200, -350
rotate = 41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_tube01
pos = 400, 400, 0
rotate = 90, 0, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind01
pos = 0, 0, 0
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind02
pos = 0, 400, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind03
pos = 0, -400, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind04
pos = 0, 200, 350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind05
pos = 0, -200, 350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind06
pos = 0, 0, 270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind07
pos = 0, 200, -350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind08
pos = 0, -200, -350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind09
pos = 0, 0, -270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn01
pos = 80, 115, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn02
pos = -80, 115, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn03
pos = 80, -115, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn04
pos = -80, -115, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn05
pos = 80, 115, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn06
pos = -80, 115, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn07
pos = 80, -115, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_conn08
pos = -80, -115, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_prod01
pos = 0, 40, 130
rotate = 0, 180, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_prod02
pos = 0, -40, 130
rotate = 180, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_prod03
pos = 0, 40, -130
rotate = 0, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_prod04
pos = 0, -40, -130
rotate = 0, 0, 180
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_gird02
pos = 0, 200, 350
rotate = -41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_gird03
pos = 0, -200, 350
rotate = 41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_gird05
pos = 0, 200, -350
rotate = -41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_gird06
pos = 0, -200, -350
rotate = 41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_tube01
pos = 0, 400, 0
rotate = 90, 0, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind01
pos = -400, 0, 0
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind02
pos = -400, 400, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind03
pos = -400, -400, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind04
pos = -400, 200, 350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind05
pos = -400, -200, 350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind06
pos = -400, 0, 270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind07
pos = -400, 200, -350
rotate = 90, 41, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind08
pos = -400, -200, -350
rotate = 90, 49, 90
archetype = space_industrial02a
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind09
pos = -400, 0, -270
rotate = 90, 45, 90
archetype = space_industriala
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn01
pos = -320, 115, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn02
pos = -480, 115, 270
rotate = 0, 180, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn03
pos = -320, -115, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn04
pos = -480, -115, 270
rotate = 180, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn05
pos = -320, 115, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn06
pos = -480, 115, -270
rotate = 0, 0, 0
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn07
pos = -320, -115, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_conn08
pos = -480, -115, -270
rotate = 0, 0, 180
archetype = space_industrial03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_prod01
pos = -400, 40, 130
rotate = 0, 180, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_prod02
pos = -400, -40, 130
rotate = 180, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_prod03
pos = -400, 40, -130
rotate = 0, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_prod04
pos = -400, -40, -130
rotate = 0, 0, 180
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird01
pos = -400, 200, 350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird02
pos = -400, 200, 350
rotate = -41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird03
pos = -400, -200, 350
rotate = 41, 180, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird04
pos = -400, 200, -350
rotate = 90, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird05
pos = -400, 200, -350
rotate = -41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_gird06
pos = -400, -200, -350
rotate = 41, 0, 0
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_tube01
pos = -400, 400, 0
rotate = 90, 0, 0
archetype = space_short_tube
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_gird01
pos = -400, 200, 350
rotate = 90, 45, 90
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_gird02
pos = 0, 200, 350
rotate = 90, 45, 90
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_gird03
pos = -400, 200, -350
rotate = 90, 45, 90
archetype = space_girdera
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_gird04
pos = 0, 200, -350
rotate = 90, 45, 90
archetype = space_girdera
parent = rh_stut_04
'''



class StuttgartMegabase(StuttgartMegabaseOriginal):
    TEMPLATE = '''[Object]
nickname = rh_stut_04
pos = 0, -1650, 0
rotate = 0, 0, 0
archetype = manhaim_core
{root_props}

[Object]
nickname = rh_stut_04_dock
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_port_dmg_dock
{dock_props}

;RIGHT FACTORIES

[Object]
nickname = rh_stut_04_RIGHT_FACTORY1_ind01
pos = 500, -1650, 0
rotate = 0, 0, 0
archetype = stuttgart_mega_right_factory1
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY2_ind01
pos = 900, -1650, 0
rotate = 0, 0, 0
archetype = stuttgart_mega_right_factory2
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_FACTORY3_ind01
pos = 1300, -1650, 0
rotate = 0, 0, 0
archetype = stuttgart_mega_right_factory3
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_MINER_ind01
pos = 1595, -1650, 0
rotate = 0, 0, 0
archetype = stuttgart_mega_right_miner
parent = rh_stut_04

[Object]
nickname = rh_stut_04_RIGHT_gird01
pos = 1100, -1450, 0
rotate = 0, 0, 0
archetype = stuttgart_mega_right
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind01
pos = -500, -1650, 0
rotate = 0, 0, 0
archetype = stuttgart_mega_left_factory1
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_ind01
pos = -900, -1650, 0
rotate = 0, 0, 0
archetype = stuttgart_mega_left_factory2
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_ind01
pos = -1300, -1650, 0
rotate = 0, 0, 0
archetype = stuttgart_mega_left_factory3
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_MINER_ind01
pos = -1595, -1650, 0
rotate = 0, 0, 0
archetype = stuttgart_mega_left_miner
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_gird01
pos = -1100, -1450, 0
rotate = 0, 0, 0
archetype = stuttgart_mega_left
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_the
pos = 0, -1655, 62.5
rotate = 0, 0, 0
archetype = stuttgart_mega_core
parent = rh_stut_04

[Object]
nickname = rh_stut_04_FRONT_ind01
pos = -50, -1650, 250
rotate = 0, 0, 0
archetype = stuttgart_mega_front
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BACK_ind01
pos = -50, -1650, -250
rotate = 0, 0, 0
archetype = stuttgart_mega_back
parent = rh_stut_04

[Object]
nickname = rh_stut_04_TOP_airlock
pos = 0, -707.5, 0
rotate = 0, 0, 0
archetype = stuttgart_mega_top
parent = rh_stut_04

[Object]
nickname = rh_stut_04_BOTTOM_airlock
pos = 0, -2652.5, 0
rotate = 0, 0, 0
archetype = stuttgart_mega_bottom
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_factory1_collision00
pos = 501.764, -1649.78, 1.76408
rotate = 0, 0, 0
archetype = stuttgart_mega_right_factory1_collision00
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_factory1_collision01
pos = 499.499, -1650.13, 324.122
rotate = 0, 0, 0
archetype = stuttgart_mega_right_factory1_collision01
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_factory1_collision02
pos = 499.499, -1650.13, -68.1164
rotate = 0, 0, 0
archetype = stuttgart_mega_right_factory1_collision02
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_factory1_collision03
pos = 500, -1650, 2.97584e-06
rotate = 0, 0, 0
archetype = stuttgart_mega_right_factory1_collision03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_factory1_collision04
pos = 462.971, -1650, -3.8932e-05
rotate = 0, 0, 0
archetype = stuttgart_mega_right_factory1_collision04
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_factory2_collision00
pos = 901.764, -1649.78, 1.76408
rotate = 0, 0, 0
archetype = stuttgart_mega_right_factory2_collision00
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_factory2_collision01
pos = 899.499, -1650.13, 324.122
rotate = 0, 0, 0
archetype = stuttgart_mega_right_factory2_collision01
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_factory2_collision02
pos = 899.499, -1650.13, -68.1164
rotate = 0, 0, 0
archetype = stuttgart_mega_right_factory2_collision02
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_factory2_collision03
pos = 900, -1650, 2.97584e-06
rotate = 0, 0, 0
archetype = stuttgart_mega_right_factory2_collision03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_factory2_collision04
pos = 862.971, -1650, -3.8932e-05
rotate = 0, 0, 0
archetype = stuttgart_mega_right_factory2_collision04
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_factory3_collision00
pos = 1301.76, -1649.78, 1.76408
rotate = 0, 0, 0
archetype = stuttgart_mega_right_factory3_collision00
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_factory3_collision01
pos = 1299.5, -1650.13, 324.122
rotate = 0, 0, 0
archetype = stuttgart_mega_right_factory3_collision01
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_factory3_collision02
pos = 1299.5, -1650.13, -68.1164
rotate = 0, 0, 0
archetype = stuttgart_mega_right_factory3_collision02
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_factory3_collision03
pos = 1300, -1650, 2.97584e-06
rotate = 0, 0, 0
archetype = stuttgart_mega_right_factory3_collision03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_factory3_collision04
pos = 1262.97, -1650, -3.8932e-05
rotate = 0, 0, 0
archetype = stuttgart_mega_right_factory3_collision04
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_miner_collision00
pos = 1619.94, -1650.14, -0.350796
rotate = 0, 0, 0
archetype = stuttgart_mega_right_miner_collision00
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_miner_collision01
pos = 1657.91, -1549.69, 0.0201282
rotate = 0, 0, 0
archetype = stuttgart_mega_right_miner_collision01
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_miner_collision02
pos = 1663.14, -1471.24, 0.0403919
rotate = 0, 0, 0
archetype = stuttgart_mega_right_miner_collision02
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_miner_collision03
pos = 1782.53, -1546.44, 0.0201283
rotate = 0, 0, 0
archetype = stuttgart_mega_right_miner_collision03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_miner_collision04
pos = 1774.33, -1471.24, 0.0403958
rotate = 0, 0, 0
archetype = stuttgart_mega_right_miner_collision04
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_miner_collision05
pos = 1665.67, -1828.76, 0.0403958
rotate = 0, 0, 0
archetype = stuttgart_mega_right_miner_collision05
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_miner_collision06
pos = 1657.47, -1753.56, 0.0201283
rotate = 0, 0, 0
archetype = stuttgart_mega_right_miner_collision06
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_miner_collision07
pos = 1776.86, -1828.76, 0.0403919
rotate = 0, 0, 0
archetype = stuttgart_mega_right_miner_collision07
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_miner_collision08
pos = 1782.09, -1750.31, 0.0201282
rotate = 0, 0, 0
archetype = stuttgart_mega_right_miner_collision08
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_right_collision00
pos = 924.486, -1450.17, 0.174046
rotate = 0, 0, 0
archetype = stuttgart_mega_right_collision00
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_factory1_collision00
pos = -498.236, -1649.78, 1.76408
rotate = 0, 0, 0
archetype = stuttgart_mega_left_factory1_collision00
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_factory1_collision01
pos = -500.501, -1650.13, 324.122
rotate = 0, 0, 0
archetype = stuttgart_mega_left_factory1_collision01
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_factory1_collision02
pos = -500.501, -1650.13, -68.1164
rotate = 0, 0, 0
archetype = stuttgart_mega_left_factory1_collision02
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_factory1_collision03
pos = -500, -1650, 2.97584e-06
rotate = 0, 0, 0
archetype = stuttgart_mega_left_factory1_collision03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_factory1_collision04
pos = -537.029, -1650, -3.8932e-05
rotate = 0, 0, 0
archetype = stuttgart_mega_left_factory1_collision04
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_factory2_collision00
pos = -898.236, -1649.78, 1.76408
rotate = 0, 0, 0
archetype = stuttgart_mega_left_factory2_collision00
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_factory2_collision01
pos = -900.501, -1650.13, 324.122
rotate = 0, 0, 0
archetype = stuttgart_mega_left_factory2_collision01
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_factory2_collision02
pos = -900.501, -1650.13, -68.1164
rotate = 0, 0, 0
archetype = stuttgart_mega_left_factory2_collision02
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_factory2_collision03
pos = -900, -1650, 2.97584e-06
rotate = 0, 0, 0
archetype = stuttgart_mega_left_factory2_collision03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_factory2_collision04
pos = -937.029, -1650, -3.8932e-05
rotate = 0, 0, 0
archetype = stuttgart_mega_left_factory2_collision04
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_factory3_collision00
pos = -1298.24, -1649.78, 1.76408
rotate = 0, 0, 0
archetype = stuttgart_mega_left_factory3_collision00
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_factory3_collision01
pos = -1300.5, -1650.13, 324.122
rotate = 0, 0, 0
archetype = stuttgart_mega_left_factory3_collision01
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_factory3_collision02
pos = -1300.5, -1650.13, -68.1164
rotate = 0, 0, 0
archetype = stuttgart_mega_left_factory3_collision02
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_factory3_collision03
pos = -1300, -1650, 2.97584e-06
rotate = 0, 0, 0
archetype = stuttgart_mega_left_factory3_collision03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_factory3_collision04
pos = -1337.03, -1650, -3.8932e-05
rotate = 0, 0, 0
archetype = stuttgart_mega_left_factory3_collision04
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_miner_collision00
pos = -1618.28, -1650.14, -0.350796
rotate = 0, 0, 0
archetype = stuttgart_mega_left_miner_collision00
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_miner_collision01
pos = -1782.09, -1549.69, 0.0201282
rotate = 0, 0, 0
archetype = stuttgart_mega_left_miner_collision01
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_miner_collision02
pos = -1776.86, -1471.24, 0.0403919
rotate = 0, 0, 0
archetype = stuttgart_mega_left_miner_collision02
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_miner_collision03
pos = -1657.47, -1546.44, 0.0201283
rotate = 0, 0, 0
archetype = stuttgart_mega_left_miner_collision03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_miner_collision04
pos = -1665.67, -1471.24, 0.0403958
rotate = 0, 0, 0
archetype = stuttgart_mega_left_miner_collision04
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_miner_collision05
pos = -1774.33, -1828.76, 0.0403958
rotate = 0, 0, 0
archetype = stuttgart_mega_left_miner_collision05
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_miner_collision06
pos = -1782.53, -1753.56, 0.0201283
rotate = 0, 0, 0
archetype = stuttgart_mega_left_miner_collision06
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_miner_collision07
pos = -1663.14, -1828.76, 0.0403919
rotate = 0, 0, 0
archetype = stuttgart_mega_left_miner_collision07
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_miner_collision08
pos = -1657.91, -1750.31, 0.0201282
rotate = 0, 0, 0
archetype = stuttgart_mega_left_miner_collision08
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_left_collision00
pos = -924.486, -1450.17, 0.173979
rotate = 0, 0, 0
archetype = stuttgart_mega_left_collision00
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_core_collision00
pos = -2.22838e-09, -1650, -12.3856
rotate = 0, 0, 0
archetype = stuttgart_mega_core_collision00
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_core_collision01
pos = 249.906, -1649.83, 250.164
rotate = 0, 0, 0
archetype = stuttgart_mega_core_collision01
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_core_collision02
pos = -250.094, -1649.83, 250.164
rotate = 0, 0, 0
archetype = stuttgart_mega_core_collision02
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_core_collision03
pos = 249.906, -1649.83, -249.836
rotate = 0, 0, 0
archetype = stuttgart_mega_core_collision03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_core_collision04
pos = -250.094, -1649.83, -249.836
rotate = 0, 0, 0
archetype = stuttgart_mega_core_collision04
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_core_collision05
pos = 124.818, -1349.83, 0.0493584
rotate = 0, 0, 0
archetype = stuttgart_mega_core_collision05
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_core_collision06
pos = -0.182491, -1349.83, 125.049
rotate = 0, 0, 0
archetype = stuttgart_mega_core_collision06
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_core_collision07
pos = -125.182, -1349.83, 0.0493584
rotate = 0, 0, 0
archetype = stuttgart_mega_core_collision07
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_core_collision08
pos = -0.182491, -1349.83, -124.951
rotate = 0, 0, 0
archetype = stuttgart_mega_core_collision08
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_core_collision09
pos = 124.818, -1949.83, 0.0493584
rotate = 0, 0, 0
archetype = stuttgart_mega_core_collision09
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_core_collision10
pos = -0.182491, -1949.83, 125.049
rotate = 0, 0, 0
archetype = stuttgart_mega_core_collision10
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_core_collision11
pos = -125.182, -1949.83, 0.0493584
rotate = 0, 0, 0
archetype = stuttgart_mega_core_collision11
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_core_collision12
pos = -4.00162e-07, -1664.08, 2.82416e-07
rotate = 0, 0, 0
archetype = stuttgart_mega_core_collision12
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_core_collision13
pos = -0.0679779, -1500.15, 0.0143051
rotate = 0, 0, 0
archetype = stuttgart_mega_core_collision13
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_core_collision14
pos = -0.0679779, -1800.15, 0.0143051
rotate = 0, 0, 0
archetype = stuttgart_mega_core_collision14
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_core_collision15
pos = -0.0679779, -1210.15, 0.0143051
rotate = 0, 0, 0
archetype = stuttgart_mega_core_collision15
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_core_collision16
pos = 61.7978, -1804.52, 62.036
rotate = 0, 0, 0
archetype = stuttgart_mega_core_collision16
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_core_collision17
pos = -0.184332, -1649.78, -0.00779548
rotate = 0, 0, 0
archetype = stuttgart_mega_core_collision17
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_core_collision18
pos = 27.5997, -1524.78, -124.509
rotate = 0, 0, 0
archetype = stuttgart_mega_core_collision18
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_core_collision19
pos = 1.30706, -1649.78, 0.27169
rotate = 0, 0, 0
archetype = stuttgart_mega_core_collision19
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_front_collision00
pos = 2.26408, -1556.23, 306.354
rotate = 0, 0, 0
archetype = stuttgart_mega_front_collision00
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_front_collision01
pos = -6.85009, -1650, 321.445
rotate = 0, 0, 0
archetype = stuttgart_mega_front_collision01
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_back_collision00
pos = 2.26408, -1556.25, -306.143
rotate = 0, 0, 0
archetype = stuttgart_mega_back_collision00
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_back_collision01
pos = -6.85009, -1650, -321.445
rotate = 0, 0, 0
archetype = stuttgart_mega_back_collision01
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_top_collision00
pos = -0.191306, -680.309, 2.06077e-05
rotate = 0, 0, 0
archetype = stuttgart_mega_top_collision00
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_top_collision01
pos = -0.0679779, -640.15, 0.0143051
rotate = 0, 0, 0
archetype = stuttgart_mega_top_collision01
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_top_collision02
pos = -0.0679779, -550.15, 0.0143051
rotate = 0, 0, 0
archetype = stuttgart_mega_top_collision02
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_top_collision03
pos = -0.0679779, -460.15, 0.0143051
rotate = 0, 0, 0
archetype = stuttgart_mega_top_collision03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_top_collision04
pos = -0.0671797, -447.958, 0.0919695
rotate = 0, 0, 0
archetype = stuttgart_mega_top_collision04
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_bottom_collision00
pos = -0.191306, -2619.69, -3.8111e-06
rotate = 0, 0, 0
archetype = stuttgart_mega_bottom_collision00
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_bottom_collision01
pos = -0.0679779, -2660.15, 0.0143051
rotate = 0, 0, 0
archetype = stuttgart_mega_bottom_collision01
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_bottom_collision02
pos = -0.0679779, -2750.15, 0.0143051
rotate = 0, 0, 0
archetype = stuttgart_mega_bottom_collision02
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_bottom_collision03
pos = -0.0679779, -2840.15, 0.0143051
rotate = 0, 0, 0
archetype = stuttgart_mega_bottom_collision03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_bottom_collision04
pos = -0.0435104, -3005.15, 0.00915527
rotate = 0, 0, 0
archetype = stuttgart_mega_bottom_collision04
parent = rh_stut_04

[Object]
nickname = rh_stut_04_stuttgart_mega_bottom_collision05
pos = -0.0671797, -3038.45, 0.0919695
rotate = 0, 0, 0
archetype = stuttgart_mega_bottom_collision05
parent = rh_stut_04

'''


class MannhaimShortGasless(MannhaimShortGaslessOriginal):
    TEMPLATE = '''[Object]
nickname = rh_stut_04
pos = 0, 0, 1230
rotate = 0, 90, 0
archetype = space_shipping01
{dock_props}

[Object]
nickname = rh_stut_04_ind01
pos = 0, -15, -355
rotate = 0, 0, 0
archetype = batch_mannhaim__06c8cdd6_structure0
parent = rh_stut_04

[Object]
nickname = rh_stut_04_CORE_tube04
pos = 400, 0, 0
rotate = 0, 0, 0
archetype = batch_mannhaim__06c8cdd6_core0
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_ind01
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = batch_mannhaim__06c8cdd6_left0
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_prod02
pos = 400, -40, 130
rotate = 180, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_prod03
pos = 400, 40, -130
rotate = 0, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY1_prod04
pos = 400, -40, -130
rotate = 0, 0, 180
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_prod02
pos = 0, -40, 130
rotate = 180, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_prod03
pos = 0, 40, -130
rotate = 0, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY2_prod04
pos = 0, -40, -130
rotate = 0, 0, 180
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_prod01
pos = -400, 40, 130
rotate = 0, 180, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_prod02
pos = -400, -40, 130
rotate = 180, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_prod03
pos = -400, 40, -130
rotate = 0, 0, 0
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04

[Object]
nickname = rh_stut_04_LEFT_FACTORY3_prod04
pos = -400, -40, -130
rotate = 0, 0, 180
archetype = space_production
loadout = mplatform_module_white
parent = rh_stut_04



[Object]
nickname = rh_stut_04_col_structure0_collision00
pos = 0.772064203, 1.21369171, -359.70554
rotate = 0, 0, 0
archetype = batch_mannhaim__06c8cdd6_structure0_collision00
parent = rh_stut_04

[Object]
nickname = rh_stut_04_col_core0_collision00
pos = 12.6144185, 0.176393509, -0.200215584
rotate = 0, 0, 0
archetype = batch_mannhaim__06c8cdd6_core0_collision00
parent = rh_stut_04

[Object]
nickname = rh_stut_04_col_left0_collision00
pos = 399.498649, 0.222499847, 153.637139
rotate = 0, 0, 0
archetype = batch_mannhaim__06c8cdd6_left0_collision00
parent = rh_stut_04

[Object]
nickname = rh_stut_04_col_left0_collision01
pos = 399.498649, -0.12858586, -54.0902217
rotate = 0, 0, 0
archetype = batch_mannhaim__06c8cdd6_left0_collision01
parent = rh_stut_04

[Object]
nickname = rh_stut_04_col_left0_collision02
pos = 190.673208, -6.33377504e-05, -3.89319741e-05
rotate = 0, 0, 0
archetype = batch_mannhaim__06c8cdd6_left0_collision02
parent = rh_stut_04

[Object]
nickname = rh_stut_04_col_left0_collision03
pos = -0.501350564, 0.222499847, 153.637139
rotate = 0, 0, 0
archetype = batch_mannhaim__06c8cdd6_left0_collision03
parent = rh_stut_04

[Object]
nickname = rh_stut_04_col_left0_collision04
pos = -0.501350564, -0.12858586, -68.1163928
rotate = 0, 0, 0
archetype = batch_mannhaim__06c8cdd6_left0_collision04
parent = rh_stut_04

[Object]
nickname = rh_stut_04_col_left0_collision05
pos = -209.326792, 15.2489891, 4.00161611e-07
rotate = 0, 0, 0
archetype = batch_mannhaim__06c8cdd6_left0_collision05
parent = rh_stut_04

[Object]
nickname = rh_stut_04_col_left0_collision06
pos = -400.501351, -92.7306984, 0.00910165411
rotate = 0, 0, 0
archetype = batch_mannhaim__06c8cdd6_left0_collision06
parent = rh_stut_04

[Object]
nickname = rh_stut_04_col_left0_collision07
pos = -400.501351, -42.8182532, -68.1074012
rotate = 0, 0, 0
archetype = batch_mannhaim__06c8cdd6_left0_collision07
parent = rh_stut_04

[Object]
nickname = rh_stut_04_col_left0_collision08
pos = -77.1590318, -6.33377504e-05, 0.173979271
rotate = 0, 0, 0
archetype = batch_mannhaim__06c8cdd6_left0_collision08
parent = rh_stut_04

'''
