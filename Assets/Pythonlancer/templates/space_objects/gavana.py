from templates.space_object_template import SpaceObjectTemplate


class Gavana(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'co_cad_02'
    TEMPLATE = '''[Object]
nickname = co_cad_02
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = gavana_core
base = co_cad_02_base
behavior = NOTHING
reputation = co_grp
ids_name = 203864
ids_info = 065776

[Object]
nickname = co_cad_02_dock
pos = 0, 270, 523
rotate = 0, 0, 0
archetype = space_police01_front_dock
dock_with = co_cad_02_base
base = co_cad_02_base
behavior = NOTHING
reputation = co_grp
ids_name = 196722
ids_info = 065739
voice = atc_leg_f01
space_costume = br_karina_head_gen, pl_female2_journeyman_body, prop_neuralnet_a

[Object]
nickname = co_cad_02_space_arch01
pos = 0, -480, 0
rotate = 90, 0, 0
archetype = space_short_large_arch
parent = co_cad_02

[Object]
nickname = co_cad_02_space_arch02
pos = 0, 480, 0
rotate = -90, 0, 0
archetype = space_short_large_arch
parent = co_cad_02

[Object]
nickname = co_cad_02_space_arch03
pos = 470, 0, 0
rotate = 90, 0, 90
archetype = space_long_large_arch
parent = co_cad_02

[Object]
nickname = co_cad_02_space_arch04
pos = -470, 0, 0
rotate = -90, 0, 90
archetype = space_long_large_arch
parent = co_cad_02

[Object]
nickname = co_cad_02_space_arch05
pos = 0, 203, 523
rotate = 0, 0, 0
archetype = space_arch_chunk_closed
parent = co_cad_02

[Object]
nickname = co_cad_02_space_arch06
pos = 0, -1500, -523
rotate = 0, 180, 0
archetype = space_arch_closed
parent = co_cad_02

[Object]
nickname = co_cad_02_space_arch07
pos = 0, 1500, 523
rotate = 180, 180, 0
archetype = space_arch_closed
parent = co_cad_02

[Object]
nickname = co_cad_02_space_arch08
pos = 0, 1500, -523
rotate = 180, 0, 0
archetype = space_arch_closed
parent = co_cad_02

[Object]
nickname = co_cad_02_space_arch09
pos = 150, 0, 523
rotate = 0, 0, 90
archetype = space_small_arch
parent = co_cad_02

[Object]
nickname = co_cad_02_space_arch10
pos = 150, 0, -523
rotate = 0, 0, 90
archetype = space_small_arch
parent = co_cad_02

[Object]
nickname = co_cad_02_space_arch11
pos = -150, 0, 523
rotate = 0, 0, -90
archetype = space_small_arch
parent = co_cad_02

[Object]
nickname = co_cad_02_space_arch12
pos = -150, 0, -523
rotate = 0, 0, -90
archetype = space_small_arch
parent = co_cad_02

[Object]
nickname = co_cad_02_space_indX01
pos = 60, 290, 523
rotate = 0, 0, 0
archetype = space_industrial02b
parent = co_cad_02

[Object]
nickname = co_cad_02_space_indX02
pos = 60, 250, 523
rotate = 0, 0, 0
archetype = space_industrial02b
parent = co_cad_02

[Object]
nickname = co_cad_02_space_indX03
pos = -60, 290, 523
rotate = 0, 0, 0
archetype = space_industrial02b
parent = co_cad_02

[Object]
nickname = co_cad_02_space_indX04
pos = -60, 250, 523
rotate = 0, 0, 0
archetype = space_industrial02b
parent = co_cad_02

[Object]
nickname = co_cad_02_control_towerA01
pos = 270, 0, 530
rotate = -90, 0, 0
archetype = space_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_towerA02
pos = 270, 0, -530
rotate = 90, 0, 0
archetype = space_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_towerA03
pos = -270, 0, 530
rotate = -90, 0, 0
archetype = space_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_towerA04
pos = -270, 0, -530
rotate = 90, 0, 0
archetype = space_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_towerA05
pos = 270, 0, 0
rotate = -90, 0, 0
archetype = space_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_towerA06
pos = -270, 0, 0
rotate = 90, 0, 0
archetype = space_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_towerA07
pos = 0, 280, 0
rotate = -90, 0, 0
archetype = space_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_towerA08
pos = 0, 280, 345
rotate = -105, 0, 0
archetype = space_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_towerA09
pos = 0, 280, -345
rotate = 105, 0, 0
archetype = space_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_towerA10
pos = 0, -280, 0
rotate = 90, 0, 0
archetype = space_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_towerA11
pos = 0, -280, 345
rotate = -75, 0, 0
archetype = space_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_towerA12
pos = 0, -280, -345
rotate = 75, 0, 0
archetype = space_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_indA01
pos = 270, 0, 530
rotate = 0, 180, 0
archetype = space_industrialc
parent = co_cad_02

[Object]
nickname = co_cad_02_indA02
pos = 270, 0, -530
rotate = 0, 0, 0
archetype = space_industrialc
parent = co_cad_02

[Object]
nickname = co_cad_02_indA03
pos = -270, 0, 530
rotate = 0, 180, 0
archetype = space_industrialc
parent = co_cad_02

[Object]
nickname = co_cad_02_indA04
pos = -270, 0, -530
rotate = 0, 0, 0
archetype = space_industrialc
parent = co_cad_02

[Object]
nickname = co_cad_02_indA05
pos = 270, 0, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = co_cad_02

[Object]
nickname = co_cad_02_indA06
pos = -270, 0, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = co_cad_02

[Object]
nickname = co_cad_02_indA07
pos = 0, 280, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = co_cad_02

[Object]
nickname = co_cad_02_indA08
pos = 0, 280, 345
rotate = 0, 180, 0
archetype = space_industrialc
parent = co_cad_02

[Object]
nickname = co_cad_02_indA09
pos = 0, 280, -345
rotate = 0, 0, 0
archetype = space_industrialc
parent = co_cad_02

[Object]
nickname = co_cad_02_indA10
pos = 0, -280, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = co_cad_02

[Object]
nickname = co_cad_02_indA11
pos = 0, -280, 345
rotate = 0, 180, 0
archetype = space_industrialc
parent = co_cad_02

[Object]
nickname = co_cad_02_indA12
pos = 0, -280, -345
rotate = 0, 0, 0
archetype = space_industrialc
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_A01
pos = 0, 280, 172.5
rotate = 0, 0, 0
archetype = space_girder
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_A02
pos = 0, 280, -172.5
rotate = 0, 0, 0
archetype = space_girder
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_A03
pos = 0, -280, 172.5
rotate = 0, 0, 0
archetype = space_girder
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_A04
pos = 0, -280, -172.5
rotate = 0, 0, 0
archetype = space_girder
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_A05
pos = 0, 280, 172.5
rotate = 0, 90, 0
archetype = space_girder
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_A06
pos = 0, 280, -172.5
rotate = 0, 90, 0
archetype = space_girder
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_A07
pos = 0, -280, 172.5
rotate = 0, 90, 0
archetype = space_girder
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_A08
pos = 0, -280, -172.5
rotate = 0, 90, 0
archetype = space_girder
parent = co_cad_02

[Object]
nickname = co_cad_02_control_tower_B01
pos = 0, 280, 172.5
rotate = 90, 0, 0
archetype = space_small_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_tower_B02
pos = 0, 280, -172.5
rotate = 90, 0, 0
archetype = space_small_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_tower_B03
pos = 0, -280, 172.5
rotate = 90, 0, 0
archetype = space_small_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_tower_B04
pos = 0, -280, -172.5
rotate = 90, 0, 0
archetype = space_small_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_dome_A01
pos = 0, 375, 172.5
rotate = 0, 0, 0
archetype = space_domea
parent = co_cad_02

[Object]
nickname = co_cad_02_dome_A02
pos = 0, 375, -172.5
rotate = 0, 0, 0
archetype = space_domea
parent = co_cad_02

[Object]
nickname = co_cad_02_dome_A03
pos = 0, -375, 172.5
rotate = 180, 0, 0
archetype = space_domea
parent = co_cad_02

[Object]
nickname = co_cad_02_dome_A04
pos = 0, -375, -172.5
rotate = 180, 0, 0
archetype = space_domea
parent = co_cad_02

[Object]
nickname = co_cad_02_indB01
pos = 325, 195, 542
rotate = 0, 90, 60
archetype = space_industrial02b
parent = co_cad_02

[Object]
nickname = co_cad_02_indB02
pos = 325, 195, 504
rotate = 0, 90, 60
archetype = space_industrial02b
parent = co_cad_02

[Object]
nickname = co_cad_02_indB03
pos = -325, 195, 542
rotate = 0, 90, -60
archetype = space_industrial02b
parent = co_cad_02

[Object]
nickname = co_cad_02_indB04
pos = 325, 195, -504
rotate = 0, 90, 60
archetype = space_industrial02b
parent = co_cad_02

[Object]
nickname = co_cad_02_indB05
pos = 325, 195, -542
rotate = 0, 90, 60
archetype = space_industrial02b
parent = co_cad_02

[Object]
nickname = co_cad_02_indB06
pos = -325, 195, 504
rotate = 0, 90, -60
archetype = space_industrial02b
parent = co_cad_02

[Object]
nickname = co_cad_02_indB07
pos = -325, 195, -542
rotate = 0, 90, -60
archetype = space_industrial02b
parent = co_cad_02

[Object]
nickname = co_cad_02_indB08
pos = -325, 195, -504
rotate = 0, 90, -60
archetype = space_industrial02b
parent = co_cad_02

[Object]
nickname = co_cad_02_indC01
pos = 325, -195, 542
rotate = 0, 90, -60
archetype = space_industrial02b
parent = co_cad_02

[Object]
nickname = co_cad_02_indC02
pos = 325, -195, 504
rotate = 0, 90, -60
archetype = space_industrial02b
parent = co_cad_02

[Object]
nickname = co_cad_02_indC03
pos = -325, -195, 542
rotate = 0, 90, 60
archetype = space_industrial02b
parent = co_cad_02

[Object]
nickname = co_cad_02_indC04
pos = 325, -195, -504
rotate = 0, 90, -60
archetype = space_industrial02b
parent = co_cad_02

[Object]
nickname = co_cad_02_indC05
pos = 325, -195, -542
rotate = 0, 90, -60
archetype = space_industrial02b
parent = co_cad_02

[Object]
nickname = co_cad_02_indC06
pos = -325, -195, 504
rotate = 0, 90, 60
archetype = space_industrial02b
parent = co_cad_02

[Object]
nickname = co_cad_02_indC07
pos = -325, -195, -542
rotate = 0, 90, 60
archetype = space_industrial02b
parent = co_cad_02

[Object]
nickname = co_cad_02_indC08
pos = -325, -195, -504
rotate = 0, 90, 60
archetype = space_industrial02b
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_A01
pos = 160, 280, 90
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_A02
pos = 100, 280, 90
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_A03
pos = 160, 280, 256
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_A04
pos = 100, 280, 256
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_A05
pos = -160, 280, 90
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_A06
pos = -100, 280, 90
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_A07
pos = -160, 280, 256
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_A08
pos = -100, 280, 225256
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_B01
pos = 160, 280, -90
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_B02
pos = 100, 280, -90
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_B03
pos = 160, 280, -256
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_B04
pos = 100, 280, -256
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_B05
pos = -160, 280, -90
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_B06
pos = -100, 280, -90
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_B07
pos = -160, 280, -256
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_B08
pos = -100, 280, -256
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_C01
pos = 160, -280, 90
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_C02
pos = 100, -280, 90
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_C03
pos = 160, -280, 256
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_C04
pos = 100, -280, 256
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_C05
pos = -160, -280, 90
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_C06
pos = -100, -280, 90
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_C07
pos = -160, -280, 256
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_C08
pos = -100, -280, 256
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_D01
pos = 160, -280, -90
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_D02
pos = 100, -280, -90
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_D03
pos = 160, -280, -256
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_D04
pos = 100, -280, -256
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_D05
pos = -160, -280, -90
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_D06
pos = -100, -280, -90
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_D07
pos = -160, -280, -256
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_D08
pos = -100, -280, -256
rotate = 90, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_tanks_A01
pos = 462, 65, 395
rotate = 0, 0, -70
archetype = space_tankl4
parent = co_cad_02

[Object]
nickname = co_cad_02_tanks_A02
pos = 462, -65, 395
rotate = 0, 0, -110
archetype = space_tankl4
parent = co_cad_02

[Object]
nickname = co_cad_02_tanks_A03
pos = 462, 65, 130
rotate = 0, 0, -70
archetype = space_tankl4
parent = co_cad_02

[Object]
nickname = co_cad_02_tanks_A04
pos = 462, -65, 130
rotate = 0, 0, -110
archetype = space_tankl4
parent = co_cad_02

[Object]
nickname = co_cad_02_tanks_A05
pos = -462, 65, 395
rotate = 180, 0, -110
archetype = space_tankl4
parent = co_cad_02

[Object]
nickname = co_cad_02_tanks_A06
pos = -462, -65, 395
rotate = 180, 0, -70
archetype = space_tankl4
parent = co_cad_02

[Object]
nickname = co_cad_02_tanks_A07
pos = -462, 65, 130
rotate = 180, 0, -110
archetype = space_tankl4
parent = co_cad_02

[Object]
nickname = co_cad_02_tanks_A08
pos = -462, -65, 130
rotate = 180, 0, -70
archetype = space_tankl4
parent = co_cad_02

[Object]
nickname = co_cad_02_tanks_B01
pos = 462, 65, -395
rotate = 0, 0, -70
archetype = space_tankl4
parent = co_cad_02

[Object]
nickname = co_cad_02_tanks_B02
pos = 462, -65, -395
rotate = 0, 0, -110
archetype = space_tankl4
parent = co_cad_02

[Object]
nickname = co_cad_02_tanks_B03
pos = 462, 65, -130
rotate = 0, 0, -70
archetype = space_tankl4
parent = co_cad_02

[Object]
nickname = co_cad_02_tanks_B04
pos = 462, -65, -130
rotate = 0, 0, -110
archetype = space_tankl4
parent = co_cad_02

[Object]
nickname = co_cad_02_tanks_B05
pos = -462, 65, -395
rotate = 180, 0, -110
archetype = space_tankl4
parent = co_cad_02

[Object]
nickname = co_cad_02_tanks_B06
pos = -462, -65, -395
rotate = 180, 0, -70
archetype = space_tankl4
parent = co_cad_02

[Object]
nickname = co_cad_02_tanks_B07
pos = -462, 65, -130
rotate = 180, 0, -110
archetype = space_tankl4
parent = co_cad_02

[Object]
nickname = co_cad_02_tanks_B08
pos = -462, -65, -130
rotate = 180, 0, -70
archetype = space_tankl4
parent = co_cad_02

[Object]
nickname = co_cad_02_indD01
pos = 160, 0, 380
rotate = 0, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_cad_02

[Object]
nickname = co_cad_02_indD02
pos = 160, 0, 95
rotate = 0, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_cad_02

[Object]
nickname = co_cad_02_indD03
pos = -160, 0, 380
rotate = 0, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_cad_02

[Object]
nickname = co_cad_02_indD04
pos = -160, 0, 95
rotate = 0, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_cad_02

[Object]
nickname = co_cad_02_indD05
pos = 160, 0, -380
rotate = 0, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_cad_02

[Object]
nickname = co_cad_02_indD06
pos = 160, 0, -95
rotate = 0, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_cad_02

[Object]
nickname = co_cad_02_indD07
pos = -160, 0, -380
rotate = 0, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_cad_02

[Object]
nickname = co_cad_02_indD08
pos = -160, 0, -95
rotate = 0, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_B01
pos = 270, 0, 60
rotate = 0, 0, 0
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_B02
pos = 270, 0, -60
rotate = 0, 180, 0
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_B03
pos = -270, 0, 60
rotate = 0, 0, 0
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_B04
pos = -270, 0, -60
rotate = 0, 180, 0
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_B05
pos = 260, 160, 155
rotate = 0, -97, 0
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_B06
pos = 260, 160, -155
rotate = 0, -82, 0
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_B07
pos = -260, 160, 155
rotate = 0, 97, 0
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_B08
pos = -260, 160, -155
rotate = 0, 82, 0
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_B09
pos = 0, 160, 25
rotate = 0, 0, 0
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_B10
pos = 0, 160, -25
rotate = 0, 180, 0
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_B11
pos = 0, -160, 25
rotate = 0, 0, 0
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_B12
pos = 0, -160, -25
rotate = 0, 180, 0
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_B13
pos = 260, -160, 155
rotate = 0, -97, 0
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_B14
pos = 260, -160, -155
rotate = 0, -82, 0
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_B15
pos = -260, -160, 155
rotate = 0, 97, 0
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_B16
pos = -260, -160, -155
rotate = 0, 82, 0
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_E01
pos = 260, 90, 315
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_E02
pos = 260, 90, 155
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_E03
pos = -260, 90, 315
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_E04
pos = -260, 90, 155
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_E05
pos = 260, 90, -315
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_E06
pos = 260, 90, -155
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_E07
pos = -260, 90, -315
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_E08
pos = -260, 90, -155
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_F01
pos = 260, -90, 315
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_F02
pos = 260, -90, 155
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_F03
pos = -260, -90, 315
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_F04
pos = -260, -90, 155
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_F05
pos = 260, -90, -315
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_F06
pos = 260, -90, -155
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_F07
pos = -260, -90, -315
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_F08
pos = -260, -90, -155
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = co_cad_02

[Object]
nickname = co_cad_02_indE01
pos = 0, 160, 130
rotate = 0, 0, 0
archetype = space_industrial02a
parent = co_cad_02

[Object]
nickname = co_cad_02_indE02
pos = 0, 160, -130
rotate = 0, 0, 0
archetype = space_industrial02a
parent = co_cad_02

[Object]
nickname = co_cad_02_indE03
pos = 0, -160, 130
rotate = 0, 0, 0
archetype = space_industrial02a
parent = co_cad_02

[Object]
nickname = co_cad_02_indE04
pos = 0, -160, -130
rotate = 0, 0, 0
archetype = space_industrial02a
parent = co_cad_02

[Object]
nickname = co_cad_02_shipyard01
pos = 0, 40, 195
rotate = 0, 0, 0
archetype = shipyard_medium
parent = co_cad_02

[Object]
nickname = co_cad_02_shipyard02
pos = 0, -40, 195
rotate = 0, 0, 180
archetype = shipyard_medium
parent = co_cad_02

[Object]
nickname = co_cad_02_shipyard03
pos = 0, 40, -195
rotate = 0, 0, 0
archetype = shipyard_medium
parent = co_cad_02

[Object]
nickname = co_cad_02_shipyard04
pos = 0, -40, -195
rotate = 0, 0, 180
archetype = shipyard_medium
parent = co_cad_02

[Object]
nickname = co_cad_02_control_block_A01
pos = 0, 360, -523
rotate = 0, 0, 0
archetype = space_small_control_block
parent = co_cad_02

[Object]
nickname = co_cad_02_control_block_A02
pos = 0, -360, -523
rotate = 180, -90, 0
archetype = space_small_control_block
parent = co_cad_02

[Object]
nickname = co_cad_02_control_block_A03
pos = 0, -360, 523
rotate = 180, 90, 0
archetype = space_small_control_block
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_G01
pos = 260, 160, 450
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_G02
pos = -260, 160, 450
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_G03
pos = 260, 160, -450
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_G04
pos = -260, 160, -450
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_G05
pos = 260, 160, 50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_G06
pos = 260, 160, -50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_G07
pos = -260, 160, 50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_G08
pos = -260, 160, -50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_H01
pos = 260, -160, 450
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_H02
pos = -260, -160, 450
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_H03
pos = 260, -160, -450
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_H04
pos = -260, -160, -450
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_H05
pos = 260, -160, 50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_H06
pos = 260, -160, -50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_H07
pos = -260, -160, 50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_habitat_H08
pos = -260, -160, -50
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_C01
pos = 160, 0, 238
rotate = 0, -90, -50
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_C02
pos = 160, 0, 238
rotate = 0, -90, 50
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_C03
pos = 160, 0, -238
rotate = 0, -90, -50
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_C04
pos = 160, 0, -238
rotate = 0, -90, 50
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_C05
pos = -160, 0, 238
rotate = 0, 90, 50
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_C06
pos = -160, 0, 238
rotate = 0, 90, -50
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_C07
pos = -160, 0, -238
rotate = 0, 90, 50
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_girder_C08
pos = -160, 0, -238
rotate = 0, 90, -50
archetype = space_girdera
parent = co_cad_02

[Object]
nickname = co_cad_02_control_tower_C01
pos = 260, 70, 450
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_tower_C02
pos = -260, 70, 450
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_tower_C03
pos = 260, 70, -450
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_tower_C04
pos = -260, 70, -450
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_tower_C05
pos = 260, 70, 50
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_tower_C06
pos = 260, 70, -50
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_tower_C07
pos = -260, 70, 50
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_tower_C08
pos = -260, 70, -50
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_tower_D01
pos = 260, -70, 450
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_tower_D02
pos = -260, -70, 450
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_tower_D03
pos = 260, -70, -450
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_tower_D04
pos = -260, -70, -450
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_tower_D05
pos = 260, -70, 50
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_tower_D06
pos = 260, -70, -50
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_tower_D07
pos = -260, -70, 50
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cad_02

[Object]
nickname = co_cad_02_control_tower_D08
pos = -260, -70, -50
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_cad_02
'''
