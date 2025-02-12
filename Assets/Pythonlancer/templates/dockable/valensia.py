from templates.space_object_template import SpaceObjectTemplate


# NEED TO REVISIT THIS BASE
class ValensiaOutside(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'co_mad_02'
    TEMPLATE = '''[Object]
nickname = co_mad_02
pos = 0, 0, 0
archetype = valensia_core
ids_name = 203811
ids_info = 065718
reputation = co_grp
base = co_val_01_base

[Object]
nickname = co_mad_02_core
pos = 0, 0, 0
rotate = 0, 55, 0
archetype = sw_center_750
parent = co_mad_02

[Object]
nickname = co_mad_ROOT_LEFT
pos = 0, 0, 800
rotate = 0, 0, 0
archetype = sw_center_450
parent = co_mad_02

[Object]
nickname = co_mad_ROOT_RIGHT
pos = 0, 0, -800
rotate = 0, 0, 0
archetype = sw_center_450
parent = co_mad_02

[;Object]
nickname = co_mad_ROOT_FRONT
pos = 350, 0, 0
rotate = 0, 0, 0
archetype = sw_center_450
parent = co_mad_02

[;Object]
nickname = co_mad_ROOT_BACK
pos = -350, 0, 0
rotate = 0, 0, 0
archetype = sw_center_450
parent = co_mad_02


[Object]
nickname = co_mad_cntrl_twr01
pos = 0, 0, 1250
rotate = -90, 0, 0
archetype = space_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_cntrl_twr02
pos = 0, 0, -1250
rotate = 90, 0, 0
archetype = space_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_cntrl_twr03
pos = 800, 0, 0
rotate = 0, 0, 90
archetype = space_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_cntrl_twr04
pos = -800, 0, 0
rotate = 0, 0, -90
archetype = space_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_airlock01
pos = 0, 0, 1370
rotate = 0, 180, 0
archetype = space_airlock
jump_effect = jump_effect_airlock
goto = co_val, co_val_airlock01, gate_tunnel_airlock
ids_name = 203812
ids_info = 065739
reputation = co_grp
behavior = NOTHING

[Object]
nickname = co_mad_airlock02
pos = 0, 0, -1370
rotate = 0, 0, 0
archetype = space_airlock
jump_effect = jump_effect_airlock
goto = co_val, co_val_airlock02, gate_tunnel_airlock
ids_name = 203812
ids_info = 065739
reputation = co_grp
behavior = NOTHING

[Object]
nickname = co_mad_airlock03
pos = 920, 0, 0
rotate = 0, -90, 0
archetype = space_airlock
jump_effect = jump_effect_airlock
goto = co_val, co_val_airlock03, gate_tunnel_airlock
ids_name = 203812
ids_info = 065739
reputation = co_grp
behavior = NOTHING

[Object]
nickname = co_mad_airlock04
pos = -920, 0, 0
rotate = 0, 90, 0
archetype = space_airlock
jump_effect = jump_effect_airlock
goto = co_val, co_val_airlock04, gate_tunnel_airlock
ids_name = 203812
ids_info = 065739
reputation = co_grp
behavior = NOTHING

[Object]
nickname = co_mad_TOP_cntrl_twr01
pos = 0, 750, 0
rotate = 180, 0, 0
archetype = space_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_TOP_cntrl_twr02
pos = 0, 1050, 0
rotate = 180, 0, 0
archetype = space_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_TOP_cntrl_twr03
pos = 0, 1165, -1.5
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_TOP_industrial01
pos = 0, 900, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_TOP_industrial02
pos = 140, 900, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_mad_02

[Object]
nickname = co_mad_TOP_industrial03
pos = -140, 900, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_mad_02

[Object]
nickname = co_mad_TOP_industrial04
pos = 0, 900, 140
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_mad_02

[Object]
nickname = co_mad_TOP_industrial05
pos = 0, 900, -140
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_mad_02

[Object]
nickname = co_mad_TOP_habitat01
pos = 0, 1110, -100
rotate = 0, 22, 0
archetype = space_habitat_wide
parent = co_mad_02

[Object]
nickname = co_mad_TOP_habitat02
pos = 0, 1250, -100
rotate = 0, 22, 0
archetype = space_habitat_tall
parent = co_mad_02

[Object]
nickname = co_mad_TOP_habitat03
pos = 0, 1135, 100
rotate = 0, -22, 0
archetype = space_habitat_wide
parent = co_mad_02

[Object]
nickname = co_mad_TOP_habitat04
pos = 0, 1220, 100
rotate = 0, -22, 0
archetype = space_habitat_tall
parent = co_mad_02

[Object]
nickname = co_mad_TOP_habitat05
pos = 0, 1085, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A01
pos = 0.1, 700.1, -0.09999999999854481
rotate = 0, 0, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A02
pos = 0.2, 700.2, -0.2000000000007276
rotate = 0, 30, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A03
pos = 0.3, 700.3, -0.2999999999992724
rotate = 0, 60, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A04
pos = 0.4, 700.4, -0.4000000000014552
rotate = 0, 90, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A05
pos = -0.1, 700.15, -0.09999999999854481
rotate = 0, 120, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A06
pos = -0.2, 700.25, -0.2000000000007276
rotate = 0, 150, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A07
pos = -0.3, 700.35, -0.2999999999992724
rotate = 0, 180, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A08
pos = -0.4, 700.4, -0.4000000000014552
rotate = 0, 210, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A09
pos = 0.15, 700.1, -0.1500000000014552
rotate = 0, 240, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A10
pos = 0.25, 700.2, -0.25
rotate = 0, 270, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A11
pos = -0.15, 700.3, -0.1500000000014552
rotate = 0, 300, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A12
pos = 0.25, 700.5, -0.25
rotate = 0, 330, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B01
pos = 0.1, 698.1, -0.09999999999854481
rotate = 0, 15, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B02
pos = 0.2, 698.2, -0.2000000000007276
rotate = 0, 45, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B03
pos = 0.3, 698.3, -0.2999999999992724
rotate = 0, 75, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B04
pos = 0.4, 698.4, -0.4000000000014552
rotate = 0, 105, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B05
pos = -0.1, 698.15, -0.09999999999854481
rotate = 0, 135, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B06
pos = -0.2, 698.25, -0.2000000000007276
rotate = 0, 165, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B07
pos = -0.3, 698.35, -0.2999999999992724
rotate = 0, 195, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B08
pos = -0.4, 698.4, -0.4000000000014552
rotate = 0, 225, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B09
pos = 0.15, 698.1, -0.1500000000014552
rotate = 0, 255, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B10
pos = 0.25, 698.2, -0.25
rotate = 0, 285, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B11
pos = -0.15, 698.3, -0.1500000000014552
rotate = 0, 315, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B12
pos = 0.25, 698.5, -0.25
rotate = 0, 345, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_cntrl_twr01
pos = 0, -750, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_cntrl_twr02
pos = 0, -1050, 0
rotate = 0, 45, 0
archetype = space_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_cntrl_twr03
pos = 0, -1225, 0
rotate = 180, 0, 0
archetype = space_medium_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_cntrl_twr04
pos = 0, -1375, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_industrial01
pos = 0, -900, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_industrial02
pos = 140, -900, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_industrial03
pos = -140, -900, 0
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_industrial04
pos = 0, -900, 140
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_industrial05
pos = 0, -900, -140
rotate = 90, 0, 0
archetype = space_industrial01a
loadout = space_ind01_reactor
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_habitat01
pos = 100, -1140, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_habitat02
pos = -100, -1140, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_habitat03
pos = 0, -1140, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_habitat04
pos = 0, -1140, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_habitat05
pos = 0, -1140, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_habitat06
pos = 55, -1290, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_habitat07
pos = -55, -1290, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_habitat08
pos = 0, -1530, 0
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A01
pos = 0.1, -700.1, -0.09999999999854481
rotate = 180, 0, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A02
pos = 0.2, -700.2, -0.2000000000007276
rotate = 180, 30, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A03
pos = 0.3, -700.3, -0.2999999999992724
rotate = 180, 60, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A04
pos = 0.4, -700.4, -0.4000000000014552
rotate = 180, 90, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A05
pos = -0.1, -700.15, -0.09999999999854481
rotate = 180, 120, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A06
pos = -0.2, -700.25, -0.2000000000007276
rotate = 180, 150, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A07
pos = -0.3, -700.35, -0.2999999999992724
rotate = 180, 180, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A08
pos = -0.4, -700.4, -0.4000000000014552
rotate = 180, 210, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A09
pos = 0.15, -700.1, -0.1500000000014552
rotate = 180, 240, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A10
pos = 0.25, -700.2, -0.25
rotate = 180, 270, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A11
pos = -0.15, -700.3, -0.1500000000014552
rotate = 180, 300, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A12
pos = 0.25, -700.5, -0.25
rotate = 180, 330, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B01
pos = 0.1, -698.1, -0.09999999999854481
rotate = 180, 15, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B02
pos = 0.2, -698.2, -0.2000000000007276
rotate = 180, 45, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B03
pos = 0.3, -698.3, -0.2999999999992724
rotate = 180, 75, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B04
pos = 0.4, -698.4, -0.4000000000014552
rotate = 180, 105, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B05
pos = -0.1, -698.15, -0.09999999999854481
rotate = 180, 135, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B06
pos = -0.2, -698.25, -0.2000000000007276
rotate = 180, 165, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B07
pos = -0.3, -698.35, -0.2999999999992724
rotate = 180, 195, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B08
pos = -0.4, -698.4, -0.4000000000014552
rotate = 180, 225, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B09
pos = 0.15, -698.1, -0.1500000000014552
rotate = 180, 255, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B10
pos = 0.25, -698.2, -0.25
rotate = 180, 285, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B11
pos = -0.15, -698.3, -0.1500000000014552
rotate = 180, 315, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B12
pos = 0.25, -698.5, -0.25
rotate = 180, 345, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_A01
pos = 0, 418, 600
rotate = 0, 90, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_A02
pos = 209, 362, 600
rotate = 0, 90, -30
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_A03
pos = -209, 362, 600
rotate = 0, 90, 30
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_A04
pos = 362, 209, 600
rotate = 0, 90, -60
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_A05
pos = -362, 209, 600
rotate = 0, 90, 60
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_A06
pos = 418, 0, 600
rotate = 90, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_A07
pos = -418, 0, 600
rotate = 90, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_A08
pos = 362, -209, 600
rotate = 0, 90, 60
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_A09
pos = -362, -209, 600
rotate = 0, 90, -60
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_A10
pos = 209, -362, 600
rotate = 0, 90, 30
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_A11
pos = -209, -362, 600
rotate = 0, 90, -30
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_A12
pos = 0, -418, 600
rotate = 0, 90, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B01
pos = 0, 438.9, 700
rotate = 0, 90, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B02
pos = 219.45, 380.1, 700
rotate = 0, 90, -30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B03
pos = -219.45, 380.1, 700
rotate = 0, 90, 30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B04
pos = 380.1, 219.45, 700
rotate = 0, 90, -60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B05
pos = -380.1, 219.45, 700
rotate = 0, 90, 60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B06
pos = 438.9, 0, 700
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B07
pos = -438.9, 0, 700
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B08
pos = 380.1, -219.45, 700
rotate = 0, 90, 60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B09
pos = -380.1, -219.45, 700
rotate = 0, 90, -60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B10
pos = 219.45, -380.1, 700
rotate = 0, 90, 30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B11
pos = -219.45, -380.1, 700
rotate = 0, 90, -30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B12
pos = 0, -438.9, 700
rotate = 0, 90, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C01
pos = 0, 459.8, 820
rotate = 0, 90, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C02
pos = 229.9, 398.2, 820
rotate = 0, 90, -30
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C03
pos = -229.9, 398.2, 820
rotate = 0, 90, 30
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C04
pos = 398.2, 229.9, 820
rotate = 0, 90, -60
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C05
pos = -398.2, 229.9, 820
rotate = 0, 90, 60
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C06
pos = 459.8, 0, 820
rotate = 90, 0, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C07
pos = -459.8, 0, 820
rotate = 90, 0, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C08
pos = 398.2, -229.9, 820
rotate = 0, 90, 60
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C09
pos = -398.2, -229.9, 820
rotate = 0, 90, -60
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C10
pos = 229.9, -398.2, 820
rotate = 0, 90, 30
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C11
pos = -229.9, -398.2, 820
rotate = 0, 90, -30
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C12
pos = 0, -459.8, 820
rotate = 0, 90, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D01
pos = 0, 438.9, 940
rotate = 0, 90, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D02
pos = 219.45, 380.1, 940
rotate = 0, 90, -30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D03
pos = -219.45, 380.1, 940
rotate = 0, 90, 30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D04
pos = 380.1, 219.45, 940
rotate = 0, 90, -60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D05
pos = -380.1, 219.45, 940
rotate = 0, 90, 60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D06
pos = 438.9, 0, 940
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D07
pos = -438.9, 0, 940
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D08
pos = 380.1, -219.45, 940
rotate = 0, 90, 60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D09
pos = -380.1, -219.45, 940
rotate = 0, 90, -60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D10
pos = 219.45, -380.1, 940
rotate = 0, 90, 30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D11
pos = -219.45, -380.1, 940
rotate = 0, 90, -30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D12
pos = 0, -438.9, 940
rotate = 0, 90, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_E01
pos = 0, 418, 1040
rotate = 0, 90, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_E02
pos = 209, 362, 1040
rotate = 0, 90, -30
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_E03
pos = -209, 362, 1040
rotate = 0, 90, 30
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_E04
pos = 362, 209, 1040
rotate = 0, 90, -60
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_E05
pos = -362, 209, 1040
rotate = 0, 90, 60
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_E06
pos = 418, 0, 1040
rotate = 90, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_E07
pos = -418, 0, 1040
rotate = 90, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_E08
pos = 362, -209, 1040
rotate = 0, 90, 60
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_E09
pos = -362, -209, 1040
rotate = 0, 90, -60
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_E10
pos = 209, -362, 1040
rotate = 0, 90, 30
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_E11
pos = -209, -362, 1040
rotate = 0, 90, -30
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_E12
pos = 0, -418, 1040
rotate = 0, 90, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F01
pos = 0, 355.3, 1120
rotate = 0, 90, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F02
pos = 177.65, 307.7, 1120
rotate = 0, 90, -30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F03
pos = -177.65, 307.7, 1120
rotate = 0, 90, 30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F04
pos = 307.7, 177.65, 1120
rotate = 0, 90, -60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F05
pos = -307.7, 177.65, 1120
rotate = 0, 90, 60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F06
pos = 355.3, 0, 1120
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F07
pos = -355.3, 0, 1120
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F08
pos = 307.7, -177.65, 1120
rotate = 0, 90, 60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F09
pos = -307.7, -177.65, 1120
rotate = 0, 90, -60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F10
pos = 177.65, -307.7, 1120
rotate = 0, 90, 30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F11
pos = -177.65, -307.7, 1120
rotate = 0, 90, -30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F12
pos = 0, -355.3, 1120
rotate = 0, 90, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_G01
pos = 0, 292.6, 1180
rotate = 0, 90, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_G02
pos = 146.3, 253.4, 1180
rotate = 0, 90, -30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_G03
pos = -146.3, 253.4, 1180
rotate = 0, 90, 30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_G04
pos = 253.4, 146.3, 1180
rotate = 0, 90, -60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_G05
pos = -253.4, 146.3, 1180
rotate = 0, 90, 60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_G06
pos = 292.6, 0, 1180
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_G07
pos = -292.6, 0, 1180
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_G08
pos = 253.4, -146.3, 1180
rotate = 0, 90, 60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_G09
pos = -253.4, -146.3, 1180
rotate = 0, 90, -60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_G10
pos = 146.3, -253.4, 1180
rotate = 0, 90, 30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_G11
pos = -146.3, -253.4, 1180
rotate = 0, 90, -30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_G12
pos = 0, -292.6, 1180
rotate = 0, 90, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_H01
pos = 228, 0, 1250
rotate = 90, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_H02
pos = -228, 0, 1250
rotate = 90, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_H03
pos = 0, 228, 1250
rotate = 0, 90, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_H04
pos = 160.8, 160.8, 1250
rotate = 0, 90, -45
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_H05
pos = 0, -228, 1250
rotate = 0, 90, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_H06
pos = -160.8, -160.8, 1250
rotate = 0, 90, -45
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_H07
pos = 160.8, -160.8, 1250
rotate = 0, 90, 45
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_H08
pos = -160.8, 160.8, 1250
rotate = 0, 90, 45
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_A01
pos = 0, 418, -600
rotate = 0, 90, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_A02
pos = 209, 362, -600
rotate = 0, 90, -30
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_A03
pos = -209, 362, -600
rotate = 0, 90, 30
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_A04
pos = 362, 209, -600
rotate = 0, 90, -60
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_A05
pos = -362, 209, -600
rotate = 0, 90, 60
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_A06
pos = 418, 0, -600
rotate = 90, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_A07
pos = -418, 0, -600
rotate = 90, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_A08
pos = 362, -209, -600
rotate = 0, 90, 60
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_A09
pos = -362, -209, -600
rotate = 0, 90, -60
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_A10
pos = 209, -362, -600
rotate = 0, 90, 30
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_A11
pos = -209, -362, -600
rotate = 0, 90, -30
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_A12
pos = 0, -418, -600
rotate = 0, 90, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B01
pos = 0, 438.9, -700
rotate = 0, 90, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B02
pos = 219.45, 380.1, -700
rotate = 0, 90, -30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B03
pos = -219.45, 380.1, -700
rotate = 0, 90, 30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B04
pos = 380.1, 219.45, -700
rotate = 0, 90, -60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B05
pos = -380.1, 219.45, -700
rotate = 0, 90, 60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B06
pos = 438.9, 0, -700
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B07
pos = -438.9, 0, -700
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B08
pos = 380.1, -219.45, -700
rotate = 0, 90, 60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B09
pos = -380.1, -219.45, -700
rotate = 0, 90, -60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B10
pos = 219.45, -380.1, -700
rotate = 0, 90, 30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B11
pos = -219.45, -380.1, -700
rotate = 0, 90, -30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B12
pos = 0, -438.9, -700
rotate = 0, 90, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C01
pos = 0, 459.8, -820
rotate = 0, 90, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C02
pos = 229.9, 398.2, -820
rotate = 0, 90, -30
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C03
pos = -229.9, 398.2, -820
rotate = 0, 90, 30
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C04
pos = 398.2, 229.9, -820
rotate = 0, 90, -60
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C05
pos = -398.2, 229.9, -820
rotate = 0, 90, 60
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C06
pos = 459.8, 0, -820
rotate = 90, 0, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C07
pos = -459.8, 0, -820
rotate = 90, 0, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C08
pos = 398.2, -229.9, -820
rotate = 0, 90, 60
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C09
pos = -398.2, -229.9, -820
rotate = 0, 90, -60
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C10
pos = 229.9, -398.2, -820
rotate = 0, 90, 30
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C11
pos = -229.9, -398.2, -820
rotate = 0, 90, -30
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C12
pos = 0, -459.8, -820
rotate = 0, 90, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D01
pos = 0, 438.9, -940
rotate = 0, 90, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D02
pos = 219.45, 380.1, -940
rotate = 0, 90, -30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D03
pos = -219.45, 380.1, -940
rotate = 0, 90, 30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D04
pos = 380.1, 219.45, -940
rotate = 0, 90, -60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D05
pos = -380.1, 219.45, -940
rotate = 0, 90, 60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D06
pos = 438.9, 0, -940
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D07
pos = -438.9, 0, -940
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D08
pos = 380.1, -219.45, -940
rotate = 0, 90, 60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D09
pos = -380.1, -219.45, -940
rotate = 0, 90, -60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D10
pos = 219.45, -380.1, -940
rotate = 0, 90, 30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D11
pos = -219.45, -380.1, -940
rotate = 0, 90, -30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D12
pos = 0, -438.9, -940
rotate = 0, 90, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_E01
pos = 0, 418, -1040
rotate = 0, 90, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_E02
pos = 209, 362, -1040
rotate = 0, 90, -30
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_E03
pos = -209, 362, -1040
rotate = 0, 90, 30
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_E04
pos = 362, 209, -1040
rotate = 0, 90, -60
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_E05
pos = -362, 209, -1040
rotate = 0, 90, 60
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_E06
pos = 418, 0, -1040
rotate = 90, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_E07
pos = -418, 0, -1040
rotate = 90, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_E08
pos = 362, -209, -1040
rotate = 0, 90, 60
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_E09
pos = -362, -209, -1040
rotate = 0, 90, -60
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_E10
pos = 209, -362, -1040
rotate = 0, 90, 30
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_E11
pos = -209, -362, -1040
rotate = 0, 90, -30
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_E12
pos = 0, -418, -1040
rotate = 0, 90, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F01
pos = 0, 355.3, -1120
rotate = 0, 90, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F02
pos = 177.65, 307.7, -1120
rotate = 0, 90, -30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F03
pos = -177.65, 307.7, -1120
rotate = 0, 90, 30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F04
pos = 307.7, 177.65, -1120
rotate = 0, 90, -60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F05
pos = -307.7, 177.65, -1120
rotate = 0, 90, 60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F06
pos = 355.3, 0, -1120
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F07
pos = -355.3, 0, -1120
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F08
pos = 307.7, -177.65, -1120
rotate = 0, 90, 60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F09
pos = -307.7, -177.65, -1120
rotate = 0, 90, -60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F10
pos = 177.65, -307.7, -1120
rotate = 0, 90, 30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F11
pos = -177.65, -307.7, -1120
rotate = 0, 90, -30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F12
pos = 0, -355.3, -1120
rotate = 0, 90, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_G01
pos = 0, 292.6, -1180
rotate = 0, 90, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_G02
pos = 146.3, 253.4, -1180
rotate = 0, 90, -30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_G03
pos = -146.3, 253.4, -1180
rotate = 0, 90, 30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_G04
pos = 253.4, 146.3, -1180
rotate = 0, 90, -60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_G05
pos = -253.4, 146.3, -1180
rotate = 0, 90, 60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_G06
pos = 292.6, 0, -1180
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_G07
pos = -292.6, 0, -1180
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_G08
pos = 253.4, -146.3, -1180
rotate = 0, 90, 60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_G09
pos = -253.4, -146.3, -1180
rotate = 0, 90, -60
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_G10
pos = 146.3, -253.4, -1180
rotate = 0, 90, 30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_G11
pos = -146.3, -253.4, -1180
rotate = 0, 90, -30
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_G12
pos = 0, -292.6, -1180
rotate = 0, 90, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_H01
pos = 228, 0, -1250
rotate = 90, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_H02
pos = -228, 0, -1250
rotate = 90, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_H03
pos = 0, 228, -1250
rotate = 0, 90, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_H04
pos = 160.8, 160.8, -1250
rotate = 0, 90, -45
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_H05
pos = 0, -228, -1250
rotate = 0, 90, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_H06
pos = -160.8, -160.8, -1250
rotate = 0, 90, -45
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_H07
pos = 160.8, -160.8, -1250
rotate = 0, 90, 45
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_H08
pos = -160.8, 160.8, -1250
rotate = 0, 90, 45
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_A01
pos = 590, 418, 0
rotate = 0, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_A02
pos = 590, 362, 209
rotate = 30, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_A03
pos = 590, 362, -209
rotate = -30, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_A04
pos = 590, 209, 362
rotate = 60, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_A05
pos = 590, 209, -362
rotate = -60, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_A06
pos = 590, 0, 418
rotate = 90, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_A07
pos = 590, 0, -418
rotate = 90, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_A08
pos = 590, -209, 362
rotate = -60, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_A09
pos = 590, -209, -362
rotate = 60, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_A10
pos = 590, -362, 209
rotate = -30, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_A11
pos = 590, -362, -209
rotate = 30, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_A12
pos = 590, -418, 0
rotate = 0, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B01
pos = 670, 355.3, 0
rotate = 0, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B02
pos = 670, 307.7, 177.65000000000146
rotate = 30, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B03
pos = 670, 307.7, -177.65000000000146
rotate = -30, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B04
pos = 670, 177.65, 307.7000000000007
rotate = 60, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B05
pos = 670, 177.65, -307.7000000000007
rotate = -60, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B06
pos = 670, 0, 355.2999999999993
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B07
pos = 670, 0, -355.2999999999993
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B08
pos = 670, -177.65, 307.7000000000007
rotate = -60, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B09
pos = 670, -177.65, -307.7000000000007
rotate = 60, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B10
pos = 670, -307.7, 177.65000000000146
rotate = -30, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B11
pos = 670, -307.7, -177.65000000000146
rotate = 30, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B12
pos = 670, -355.3, 0
rotate = 0, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_C01
pos = 730, 292.6, 0
rotate = 0, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_C02
pos = 730, 253.4, 146.29999999999927
rotate = 30, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_C03
pos = 730, 253.4, -146.29999999999927
rotate = -30, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_C04
pos = 730, 146.3, 253.40000000000146
rotate = 60, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_C05
pos = 730, 146.3, -253.40000000000146
rotate = -60, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_C06
pos = 730, 0, 292.59999999999854
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_C07
pos = 730, 0, -292.59999999999854
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_C08
pos = 730, -146.3, 253.40000000000146
rotate = -60, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_C09
pos = 730, -146.3, -253.40000000000146
rotate = 60, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_C10
pos = 730, -253.4, 146.29999999999927
rotate = -30, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_C11
pos = 730, -253.4, -146.29999999999927
rotate = 30, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_C12
pos = 730, -292.6, 0
rotate = 0, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_D01
pos = 800, 0, 228
rotate = 90, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_D02
pos = 800, 0, -228
rotate = 90, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_D03
pos = 800, 228, 0
rotate = 0, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_D04
pos = 800, 160.8, 160.79999999999927
rotate = 45, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_D05
pos = 800, -228, 0
rotate = 0, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_D06
pos = 800, -160.8, -160.79999999999927
rotate = 45, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_D07
pos = 800, -160.8, 160.79999999999927
rotate = -45, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_D08
pos = 800, 160.8, -160.79999999999927
rotate = -45, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_A01
pos = -590, 418, 0
rotate = 0, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_A02
pos = -590, 362, 209
rotate = 30, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_A03
pos = -590, 362, -209
rotate = -30, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_A04
pos = -590, 209, 362
rotate = 60, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_A05
pos = -590, 209, -362
rotate = -60, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_A06
pos = -590, 0, 418
rotate = 90, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_A07
pos = -590, 0, -418
rotate = 90, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_A08
pos = -590, -209, 362
rotate = -60, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_A09
pos = -590, -209, -362
rotate = 60, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_A10
pos = -590, -362, 209
rotate = -30, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_A11
pos = -590, -362, -209
rotate = 30, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_A12
pos = -590, -418, 0
rotate = 0, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B01
pos = -670, 355.3, 0
rotate = 0, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B02
pos = -670, 307.7, 177.65000000000146
rotate = 30, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B03
pos = -670, 307.7, -177.65000000000146
rotate = -30, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B04
pos = -670, 177.65, 307.7000000000007
rotate = 60, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B05
pos = -670, 177.65, -307.7000000000007
rotate = -60, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B06
pos = -670, 0, 355.2999999999993
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B07
pos = -670, 0, -355.2999999999993
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B08
pos = -670, -177.65, 307.7000000000007
rotate = -60, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B09
pos = -670, -177.65, -307.7000000000007
rotate = 60, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B10
pos = -670, -307.7, 177.65000000000146
rotate = -30, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B11
pos = -670, -307.7, -177.65000000000146
rotate = 30, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B12
pos = -670, -355.3, 0
rotate = 0, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_C01
pos = -730, 292.6, 0
rotate = 0, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_C02
pos = -730, 253.4, 146.29999999999927
rotate = 30, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_C03
pos = -730, 253.4, -146.29999999999927
rotate = -30, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_C04
pos = -730, 146.3, 253.40000000000146
rotate = 60, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_C05
pos = -730, 146.3, -253.40000000000146
rotate = -60, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_C06
pos = -730, 0, 292.59999999999854
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_C07
pos = -730, 0, -292.59999999999854
rotate = 90, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_C08
pos = -730, -146.3, 253.40000000000146
rotate = -60, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_C09
pos = -730, -146.3, -253.40000000000146
rotate = 60, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_C10
pos = -730, -253.4, 146.29999999999927
rotate = -30, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_C11
pos = -730, -253.4, -146.29999999999927
rotate = 30, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_C12
pos = -730, -292.6, 0
rotate = 0, 0, 0
archetype = space_industrial01a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_D01
pos = -800, 0, 228
rotate = 90, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_D02
pos = -800, 0, -228
rotate = 90, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_D03
pos = -800, 228, 0
rotate = 0, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_D04
pos = -800, 160.8, 160.79999999999927
rotate = 45, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_D05
pos = -800, -228, 0
rotate = 0, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_D06
pos = -800, -160.8, -160.79999999999927
rotate = 45, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_D07
pos = -800, -160.8, 160.79999999999927
rotate = -45, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_D08
pos = -800, 160.8, -160.79999999999927
rotate = -45, 0, 0
archetype = space_industriala_low_detail
parent = co_mad_02


[Object]
nickname = co_mad_industrial_L5_A01
pos = 0, 590, 459.7999999999993
rotate = 0, 90, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A02
pos = 229.9, 590, 398.2000000000007
rotate = 0, -60, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A03
pos = -229.9, 590, 398.2000000000007
rotate = 0, 60, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A04
pos = 398.2, 590, 229.90000000000146
rotate = 0, -30, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A05
pos = -398.2, 590, 229.90000000000146
rotate = 0, 30, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A06
pos = 459.8, 590, 0
rotate = 0, 0, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A07
pos = -459.8, 590, 0
rotate = 0, 0, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A08
pos = 398.2, 590, -229.90000000000146
rotate = 0, 30, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A09
pos = -398.2, 590, -229.90000000000146
rotate = 0, -30, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A10
pos = 229.9, 590, -398.2000000000007
rotate = 0, 60, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A11
pos = -229.9, 590, -398.2000000000007
rotate = 0, -60, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A12
pos = 0, 590, -459.7999999999993
rotate = 0, 90, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02


[Object]
nickname = co_mad_industrial_L6_A01
pos = 0, -590, 459.7999999999993
rotate = 0, 90, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A02
pos = 229.9, -590, 398.2000000000007
rotate = 0, -60, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A03
pos = -229.9, -590, 398.2000000000007
rotate = 0, 60, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A04
pos = 398.2, -590, 229.90000000000146
rotate = 0, -30, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A05
pos = -398.2, -590, 229.90000000000146
rotate = 0, 30, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A06
pos = 459.8, -590, 0
rotate = 0, 0, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A07
pos = -459.8, -590, 0
rotate = 0, 0, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A08
pos = 398.2, -590, -229.90000000000146
rotate = 0, 30, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A09
pos = -398.2, -590, -229.90000000000146
rotate = 0, -30, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A10
pos = 229.9, -590, -398.2000000000007
rotate = 0, 60, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A11
pos = -229.9, -590, -398.2000000000007
rotate = 0, -60, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A12
pos = 0, -590, -459.7999999999993
rotate = 0, 90, 0
archetype = space_industrial02a_low_detail
parent = co_mad_02



[Object]
nickname = co_mad_industrial_L7_A02
pos = 806, 60, 257
rotate = 0, -18, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_A03
pos = 686, 60, 498
rotate = 0, -36, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_A04
pos = 498, 60, 686
rotate = 0, -54, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_B02
pos = -806, 60, 257
rotate = 0, 18, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_B03
pos = -686, 60, 498
rotate = 0, 36, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_B04
pos = -498, 60, 686
rotate = 0, 54, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_C02
pos = 806, 60, -257
rotate = 0, 18, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_C03
pos = 686, 60, -498
rotate = 0, 36, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_C04
pos = 498, 60, -686
rotate = 0, 54, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_D02
pos = -806, 60, -257
rotate = 0, -18, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_D03
pos = -686, 60, -498
rotate = 0, -36, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_D04
pos = -498, 60, -686
rotate = 0, -54, 0
archetype = space_industrial02a
parent = co_mad_02


[Object]
nickname = co_mad_industrial_L8_A02
pos = 806, -60, 257
rotate = 0, -18, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_A03
pos = 686, -60, 498
rotate = 0, -36, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_A04
pos = 498, -60, 686
rotate = 0, -54, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_B02
pos = -806, -60, 257
rotate = 0, 18, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_B03
pos = -686, -60, 498
rotate = 0, 36, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_B04
pos = -498, -60, 686
rotate = 0, 54, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_C02
pos = 806, -60, -257
rotate = 0, 18, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_C03
pos = 686, -60, -498
rotate = 0, 36, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_C04
pos = 498, -60, -686
rotate = 0, 54, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_D02
pos = -806, -60, -257
rotate = 0, -18, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_D03
pos = -686, -60, -498
rotate = 0, -36, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_D04
pos = -498, -60, -686
rotate = 0, -54, 0
archetype = space_industrial02a
parent = co_mad_02
'''


class ValensiaOutsideTwo(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'co_mad_02'
    TEMPLATE = '''[Object]
nickname = co_mad_02
ids_name = 203811
pos = 0, 0, 0
archetype = valensia_core
ids_info = 065718
base = co_val_01_base
reputation = co_grp

[Object]
nickname = co_mad_02_core
pos = 0, 0, 0
rotate = 0, 55, 0
archetype = sw_center_750
parent = co_mad_02

[Object]
nickname = co_mad_ROOT_LEFT
pos = 0, 0, 800
rotate = 0, 0, 0
archetype = sw_center_480
parent = co_mad_02

[Object]
nickname = co_mad_ROOT_RIGHT
pos = 0, 0, -800
rotate = 0, 0, 0
archetype = sw_center_480
parent = co_mad_02

[Object]
nickname = co_mad_ROOT_FRONT
pos = 400, 0, 0
rotate = 0, 0, 0
archetype = sw_center_480
parent = co_mad_02

[Object]
nickname = co_mad_ROOT_BACK
pos = -400, 0, 0
rotate = 0, 0, 0
archetype = sw_center_480
parent = co_mad_02

[Object]
nickname = co_mad_cntrl_twr01
pos = 0, 0, 1270
rotate = -90, 0, 0
archetype = space_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_cntrl_twr02
pos = 0, 0, -1270
rotate = 90, 0, 0
archetype = space_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_cntrl_twr03
pos = 860, 0, 0
rotate = 0, 0, 90
archetype = space_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_cntrl_twr04
pos = -860, 0, 0
rotate = 0, 0, -90
archetype = space_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_airlock01
ids_name = 203812
pos = 0, 0, 1370
rotate = 0, 180, 0
archetype = space_airlock
jump_effect = jump_effect_airlock
ids_info = 065739
reputation = co_grp
behavior = NOTHING
goto = co_val, co_val_airlock01, gate_tunnel_airlock

[Object]
nickname = co_mad_airlock02
ids_name = 203812
pos = 0, 0, -1370
rotate = 0, 0, 0
archetype = space_airlock
jump_effect = jump_effect_airlock
ids_info = 065739
reputation = co_grp
behavior = NOTHING
goto = co_val, co_val_airlock02, gate_tunnel_airlock

[Object]
nickname = co_mad_airlock03
ids_name = 203812
pos = 950, 0, 0
rotate = 0, -90, 0
archetype = space_airlock
jump_effect = jump_effect_airlock
ids_info = 065739
reputation = co_grp
behavior = NOTHING
goto = co_val, co_val_airlock03, gate_tunnel_airlock

[Object]
nickname = co_mad_airlock04
ids_name = 203812
pos = -950, 0, 0
rotate = 0, 90, 0
archetype = space_airlock
jump_effect = jump_effect_airlock
ids_info = 065739
reputation = co_grp
behavior = NOTHING
goto = co_val, co_val_airlock04, gate_tunnel_airlock

[Object]
nickname = co_mad_TOP_cntrl_twr01
pos = 0, 750, 0
rotate = 180, 0, 0
archetype = space_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_TOP_cntrl_twr02
pos = 0, 1050, 0
rotate = 180, 0, 0
archetype = space_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_TOP_cntrl_twr03
pos = 0, 1165, -1.5
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_TOP_industrial01
pos = 0, 900, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_TOP_industrial02
pos = 140, 900, 0
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_TOP_industrial03
pos = -140, 900, 0
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_TOP_industrial04
pos = 0, 900, 140
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_TOP_industrial05
pos = 0, 900, -140
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_TOP_habitat01
pos = 0, 1110, -100
rotate = 0, 22, 0
archetype = space_habitat_wide
parent = co_mad_02

[Object]
nickname = co_mad_TOP_habitat02
pos = 0, 1250, -100
rotate = 0, 22, 0
archetype = space_habitat_tall
parent = co_mad_02

[Object]
nickname = co_mad_TOP_habitat03
pos = 0, 1135, 100
rotate = 0, -22, 0
archetype = space_habitat_wide
parent = co_mad_02

[Object]
nickname = co_mad_TOP_habitat04
pos = 0, 1220, 100
rotate = 0, -22, 0
archetype = space_habitat_tall
parent = co_mad_02

[Object]
nickname = co_mad_TOP_habitat05
pos = 0, 1085, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A01
pos = 0.1, 700.1, -0.09999999999854481
rotate = 0, 0, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A02
pos = 0.2, 700.2, -0.2000000000007276
rotate = 0, 30, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A03
pos = 0.3, 700.3, -0.2999999999992724
rotate = 0, 60, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A04
pos = 0.4, 700.4, -0.4000000000014552
rotate = 0, 90, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A05
pos = -0.1, 700.15, -0.09999999999854481
rotate = 0, 120, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A06
pos = -0.2, 700.25, -0.2000000000007276
rotate = 0, 150, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A07
pos = -0.3, 700.35, -0.2999999999992724
rotate = 0, 180, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A08
pos = -0.4, 700.4, -0.4000000000014552
rotate = 0, 210, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A09
pos = 0.15, 700.1, -0.1500000000014552
rotate = 0, 240, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A10
pos = 0.25, 700.2, -0.25
rotate = 0, 270, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A11
pos = -0.15, 700.3, -0.1500000000014552
rotate = 0, 300, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_A12
pos = 0.25, 700.5, -0.25
rotate = 0, 330, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B01
pos = 0.1, 698.1, -0.09999999999854481
rotate = 0, 15, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B02
pos = 0.2, 698.2, -0.2000000000007276
rotate = 0, 45, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B03
pos = 0.3, 698.3, -0.2999999999992724
rotate = 0, 75, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B04
pos = 0.4, 698.4, -0.4000000000014552
rotate = 0, 105, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B05
pos = -0.1, 698.15, -0.09999999999854481
rotate = 0, 135, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B06
pos = -0.2, 698.25, -0.2000000000007276
rotate = 0, 165, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B07
pos = -0.3, 698.35, -0.2999999999992724
rotate = 0, 195, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B08
pos = -0.4, 698.4, -0.4000000000014552
rotate = 0, 225, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B09
pos = 0.15, 698.1, -0.1500000000014552
rotate = 0, 255, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B10
pos = 0.25, 698.2, -0.25
rotate = 0, 285, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B11
pos = -0.15, 698.3, -0.1500000000014552
rotate = 0, 315, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_TOP_hidden_connect_B12
pos = 0.25, 698.5, -0.25
rotate = 0, 345, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_cntrl_twr01
pos = 0, -750, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_cntrl_twr02
pos = 0, -1050, 0
rotate = 0, 45, 0
archetype = space_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_cntrl_twr03
pos = 0, -1225, 0
rotate = 180, 0, 0
archetype = space_medium_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_cntrl_twr04
pos = 0, -1375, 0
rotate = 0, 0, 0
archetype = space_small_control_tower
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_industrial01
pos = 0, -900, 0
rotate = 90, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_industrial02
pos = 140, -900, 0
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_industrial03
pos = -140, -900, 0
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_industrial04
pos = 0, -900, 140
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_industrial05
pos = 0, -900, -140
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_habitat01
pos = 100, -1140, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_habitat02
pos = -100, -1140, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_habitat03
pos = 0, -1140, 100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_habitat04
pos = 0, -1140, -100
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_habitat05
pos = 0, -1140, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_habitat06
pos = 55, -1290, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_habitat07
pos = -55, -1290, 0
rotate = 0, 0, 0
archetype = space_habitat_wide
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_habitat08
pos = 0, -1530, 0
rotate = 180, 0, 0
archetype = space_habitat_tall
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A01
pos = 0.1, -700.1, -0.09999999999854481
rotate = 180, 0, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A02
pos = 0.2, -700.2, -0.2000000000007276
rotate = 180, 30, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A03
pos = 0.3, -700.3, -0.2999999999992724
rotate = 180, 60, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A04
pos = 0.4, -700.4, -0.4000000000014552
rotate = 180, 90, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A05
pos = -0.1, -700.15, -0.09999999999854481
rotate = 180, 120, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A06
pos = -0.2, -700.25, -0.2000000000007276
rotate = 180, 150, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A07
pos = -0.3, -700.35, -0.2999999999992724
rotate = 180, 180, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A08
pos = -0.4, -700.4, -0.4000000000014552
rotate = 180, 210, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A09
pos = 0.15, -700.1, -0.1500000000014552
rotate = 180, 240, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A10
pos = 0.25, -700.2, -0.25
rotate = 180, 270, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A11
pos = -0.15, -700.3, -0.1500000000014552
rotate = 180, 300, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_A12
pos = 0.25, -700.5, -0.25
rotate = 180, 330, 0
archetype = hidden_connect
loadout = hidden_palace_panels01
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B01
pos = 0.1, -698.1, -0.09999999999854481
rotate = 180, 15, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B02
pos = 0.2, -698.2, -0.2000000000007276
rotate = 180, 45, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B03
pos = 0.3, -698.3, -0.2999999999992724
rotate = 180, 75, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B04
pos = 0.4, -698.4, -0.4000000000014552
rotate = 180, 105, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B05
pos = -0.1, -698.15, -0.09999999999854481
rotate = 180, 135, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B06
pos = -0.2, -698.25, -0.2000000000007276
rotate = 180, 165, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B07
pos = -0.3, -698.35, -0.2999999999992724
rotate = 180, 195, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B08
pos = -0.4, -698.4, -0.4000000000014552
rotate = 180, 225, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B09
pos = 0.15, -698.1, -0.1500000000014552
rotate = 180, 255, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B10
pos = 0.25, -698.2, -0.25
rotate = 180, 285, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B11
pos = -0.15, -698.3, -0.1500000000014552
rotate = 180, 315, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_BOTTOM_hidden_connect_B12
pos = 0.25, -698.5, -0.25
rotate = 180, 345, 0
archetype = hidden_connect
loadout = hidden_palace_panels02
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B01
pos = 0, 438.9, 700
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B02
pos = 219.45, 380.1, 700
rotate = 0, 90, -30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B03
pos = -219.45, 380.1, 700
rotate = 0, 90, 30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B04
pos = 380.1, 219.45, 700
rotate = 0, 90, -60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B05
pos = -380.1, 219.45, 700
rotate = 0, 90, 60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B06
pos = 438.9, 0, 700
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B07
pos = -438.9, 0, 700
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B08
pos = 380.1, -219.45, 700
rotate = 0, 90, 60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B09
pos = -380.1, -219.45, 700
rotate = 0, 90, -60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B10
pos = 219.45, -380.1, 700
rotate = 0, 90, 30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B11
pos = -219.45, -380.1, 700
rotate = 0, 90, -30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_B12
pos = 0, -438.9, 700
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C01
pos = 0, 459.8, 820
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C02
pos = 229.9, 398.2, 820
rotate = 0, 90, -30
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C03
pos = -229.9, 398.2, 820
rotate = 0, 90, 30
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C04
pos = 398.2, 229.9, 820
rotate = 0, 90, -60
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C05
pos = -398.2, 229.9, 820
rotate = 0, 90, 60
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C06
pos = 459.8, 0, 820
rotate = 90, 0, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C07
pos = -459.8, 0, 820
rotate = 90, 0, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C08
pos = 398.2, -229.9, 820
rotate = 0, 90, 60
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C09
pos = -398.2, -229.9, 820
rotate = 0, 90, -60
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C10
pos = 229.9, -398.2, 820
rotate = 0, 90, 30
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C11
pos = -229.9, -398.2, 820
rotate = 0, 90, -30
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_C12
pos = 0, -459.8, 820
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D01
pos = 0, 438.9, 945
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D02
pos = 219.45, 380.1, 942
rotate = 0, 90, -30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D03
pos = -219.45, 380.1, 942
rotate = 0, 90, 30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D04
pos = 380.1, 219.45, 940
rotate = 0, 90, -60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D05
pos = -380.1, 219.45, 940
rotate = 0, 90, 60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D06
pos = 438.9, 0, 945
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D07
pos = -438.9, 0, 945
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D08
pos = 380.1, -219.45, 943
rotate = 0, 90, 60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D09
pos = -380.1, -219.45, 943
rotate = 0, 90, -60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D10
pos = 219.45, -380.1, 940
rotate = 0, 90, 30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D11
pos = -219.45, -380.1, 940
rotate = 0, 90, -30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_D12
pos = 0, -438.9, 945
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F01
pos = 0, 355.3, 1130
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F02
pos = 177.65, 307.7, 1120
rotate = 0, 90, -30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F03
pos = -177.65, 307.7, 1120
rotate = 0, 90, 30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F04
pos = 307.7, 177.65, 1125
rotate = 0, 90, -60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F05
pos = -307.7, 177.65, 1125
rotate = 0, 90, 60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F06
pos = 355.3, 0, 1130
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F07
pos = -355.3, 0, 1130
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F08
pos = 307.7, -177.65, 1120
rotate = 0, 90, 60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F09
pos = -307.7, -177.65, 1125
rotate = 0, 90, -60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F10
pos = 177.65, -307.7, 1125
rotate = 0, 90, 30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F11
pos = -177.65, -307.7, 1120
rotate = 0, 90, -30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_F12
pos = 0, -355.3, 1130
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_H01
pos = 228, 0, 1255
rotate = 90, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_H02
pos = -228, 0, 1255
rotate = 90, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_H03
pos = 0, 228, 1255
rotate = 0, 90, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_H04
pos = 160.8, 160.8, 1250
rotate = 0, 90, -45
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_H05
pos = 0, -228, 1255
rotate = 0, 90, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_H06
pos = -160.8, -160.8, 1250
rotate = 0, 90, -45
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_H07
pos = 160.8, -160.8, 1250
rotate = 0, 90, 45
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L1_H08
pos = -160.8, 160.8, 1250
rotate = 0, 90, 45
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B01
pos = 0, 438.9, -700
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B02
pos = 219.45, 380.1, -700
rotate = 0, 90, -30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B03
pos = -219.45, 380.1, -700
rotate = 0, 90, 30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B04
pos = 380.1, 219.45, -700
rotate = 0, 90, -60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B05
pos = -380.1, 219.45, -700
rotate = 0, 90, 60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B06
pos = 438.9, 0, -700
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B07
pos = -438.9, 0, -700
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B08
pos = 380.1, -219.45, -700
rotate = 0, 90, 60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B09
pos = -380.1, -219.45, -700
rotate = 0, 90, -60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B10
pos = 219.45, -380.1, -700
rotate = 0, 90, 30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B11
pos = -219.45, -380.1, -700
rotate = 0, 90, -30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_B12
pos = 0, -438.9, -700
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C01
pos = 0, 459.8, -820
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C02
pos = 229.9, 398.2, -820
rotate = 0, 90, -30
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C03
pos = -229.9, 398.2, -820
rotate = 0, 90, 30
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C04
pos = 398.2, 229.9, -820
rotate = 0, 90, -60
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C05
pos = -398.2, 229.9, -820
rotate = 0, 90, 60
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C06
pos = 459.8, 0, -820
rotate = 90, 0, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C07
pos = -459.8, 0, -820
rotate = 90, 0, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C08
pos = 398.2, -229.9, -820
rotate = 0, 90, 60
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C09
pos = -398.2, -229.9, -820
rotate = 0, 90, -60
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C10
pos = 229.9, -398.2, -820
rotate = 0, 90, 30
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C11
pos = -229.9, -398.2, -820
rotate = 0, 90, -30
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_C12
pos = 0, -459.8, -820
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D01
pos = 0, 438.9, -945
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D02
pos = 219.45, 380.1, -943
rotate = 0, 90, -30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D03
pos = -219.45, 380.1, -943
rotate = 0, 90, 30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D04
pos = 380.1, 219.45, -940
rotate = 0, 90, -60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D05
pos = -380.1, 219.45, -940
rotate = 0, 90, 60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D06
pos = 438.9, 0, -945
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D07
pos = -438.9, 0, -945
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D08
pos = 380.1, -219.45, -943
rotate = 0, 90, 60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D09
pos = -380.1, -219.45, -943
rotate = 0, 90, -60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D10
pos = 219.45, -380.1, -940
rotate = 0, 90, 30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D11
pos = -219.45, -380.1, -940
rotate = 0, 90, -30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_D12
pos = 0, -438.9, -945
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F01
pos = 0, 355.3, -1130
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F02
pos = 177.65, 307.7, -1125
rotate = 0, 90, -30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F03
pos = -177.65, 307.7, -1125
rotate = 0, 90, 30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F04
pos = 307.7, 177.65, -1120
rotate = 0, 90, -60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F05
pos = -307.7, 177.65, -1120
rotate = 0, 90, 60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F06
pos = 355.3, 0, -1130
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F07
pos = -355.3, 0, -1130
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F08
pos = 307.7, -177.65, -1125
rotate = 0, 90, 60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F09
pos = -307.7, -177.65, -1125
rotate = 0, 90, -60
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F10
pos = 177.65, -307.7, -1120
rotate = 0, 90, 30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F11
pos = -177.65, -307.7, -1120
rotate = 0, 90, -30
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_F12
pos = 0, -355.3, -1130
rotate = 0, 90, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_H01
pos = 228, 0, -1250
rotate = 90, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_H02
pos = -228, 0, -1250
rotate = 90, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_H03
pos = 0, 228, -1250
rotate = 0, 90, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_H04
pos = 160.8, 160.8, -1250
rotate = 0, 90, -45
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_H05
pos = 0, -228, -1250
rotate = 0, 90, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_H06
pos = -160.8, -160.8, -1250
rotate = 0, 90, -45
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_H07
pos = 160.8, -160.8, -1250
rotate = 0, 90, 45
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L2_H08
pos = -160.8, 160.8, -1250
rotate = 0, 90, 45
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B01
pos = 675, 355.3, 0
rotate = 0, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B02
pos = 673, 307.7, 177.65000000000146
rotate = 30, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B03
pos = 673, 307.7, -177.65000000000146
rotate = -30, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B04
pos = 670, 177.65, 307.7000000000007
rotate = 60, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B05
pos = 670, 177.65, -307.7000000000007
rotate = -60, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B06
pos = 675, 0, 355.2999999999993
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B07
pos = 675, 0, -355.2999999999993
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B08
pos = 673, -177.65, 307.7000000000007
rotate = -60, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B09
pos = 673, -177.65, -307.7000000000007
rotate = 60, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B10
pos = 670, -307.7, 177.65000000000146
rotate = -30, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B11
pos = 670, -307.7, -177.65000000000146
rotate = 30, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_B12
pos = 675, -355.3, 0
rotate = 0, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_D01
pos = 800, 0, 228
rotate = 90, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_D02
pos = 800, 0, -228
rotate = 90, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_D03
pos = 800, 228, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_D04
pos = 803, 160.8, 160.79999999999927
rotate = 45, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_D05
pos = 800, -228, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_D06
pos = 803, -160.8, -160.79999999999927
rotate = 45, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_D07
pos = 803, -160.8, 160.79999999999927
rotate = -45, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L3_D08
pos = 803, 160.8, -160.79999999999927
rotate = -45, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B01
pos = -675, 355.3, 0
rotate = 0, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B02
pos = -673, 307.7, 177.65000000000146
rotate = 30, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B03
pos = -673, 307.7, -177.65000000000146
rotate = -30, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B04
pos = -670, 177.65, 307.7000000000007
rotate = 60, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B05
pos = -670, 177.65, -307.7000000000007
rotate = -60, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B06
pos = -675, 0, 355.2999999999993
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B07
pos = -675, 0, -355.2999999999993
rotate = 90, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B08
pos = -673, -177.65, 307.7000000000007
rotate = -60, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B09
pos = -673, -177.65, -307.7000000000007
rotate = 60, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B10
pos = -670, -307.7, 177.65000000000146
rotate = -30, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B11
pos = -670, -307.7, -177.65000000000146
rotate = 30, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_B12
pos = -675, -355.3, 0
rotate = 0, 0, 0
archetype = space_industrial01a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_D01
pos = -800, 0, 228
rotate = 90, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_D02
pos = -800, 0, -228
rotate = 90, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_D03
pos = -800, 228, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_D04
pos = -803, 160.8, 160.79999999999927
rotate = 45, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_D05
pos = -800, -228, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_D06
pos = -803, -160.8, -160.79999999999927
rotate = 45, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_D07
pos = -803, -160.8, 160.79999999999927
rotate = -45, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L4_D08
pos = -803, 160.8, -160.79999999999927
rotate = -45, 0, 0
archetype = space_industriala
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A01
pos = 0, 590, 459.7999999999993
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A02
pos = 229.9, 590, 398.2000000000007
rotate = 0, -60, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A03
pos = -229.9, 590, 398.2000000000007
rotate = 0, 60, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A04
pos = 398.2, 590, 229.90000000000146
rotate = 0, -30, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A05
pos = -398.2, 590, 229.90000000000146
rotate = 0, 30, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A06
pos = 459.8, 590, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A07
pos = -459.8, 590, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A08
pos = 398.2, 590, -229.90000000000146
rotate = 0, 30, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A09
pos = -398.2, 590, -229.90000000000146
rotate = 0, -30, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A10
pos = 229.9, 590, -398.2000000000007
rotate = 0, 60, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A11
pos = -229.9, 590, -398.2000000000007
rotate = 0, -60, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L5_A12
pos = 0, 590, -459.7999999999993
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A01
pos = 0, -590, 459.7999999999993
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A02
pos = 229.9, -590, 398.2000000000007
rotate = 0, -60, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A03
pos = -229.9, -590, 398.2000000000007
rotate = 0, 60, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A04
pos = 398.2, -590, 229.90000000000146
rotate = 0, -30, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A05
pos = -398.2, -590, 229.90000000000146
rotate = 0, 30, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A06
pos = 459.8, -590, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A07
pos = -459.8, -590, 0
rotate = 0, 0, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A08
pos = 398.2, -590, -229.90000000000146
rotate = 0, 30, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A09
pos = -398.2, -590, -229.90000000000146
rotate = 0, -30, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A10
pos = 229.9, -590, -398.2000000000007
rotate = 0, 60, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A11
pos = -229.9, -590, -398.2000000000007
rotate = 0, -60, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L6_A12
pos = 0, -590, -459.7999999999993
rotate = 0, 90, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_A02
pos = 806, 60, 257
rotate = 0, -18, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_A03
pos = 686, 60, 498
rotate = 0, -36, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_A04
pos = 498, 60, 686
rotate = 0, -54, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_B02
pos = -806, 60, 257
rotate = 0, 18, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_B03
pos = -686, 60, 498
rotate = 0, 36, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_B04
pos = -498, 60, 686
rotate = 0, 54, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_C02
pos = 806, 60, -257
rotate = 0, 18, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_C03
pos = 686, 60, -498
rotate = 0, 36, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_C04
pos = 498, 60, -686
rotate = 0, 54, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_D02
pos = -806, 60, -257
rotate = 0, -18, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_D03
pos = -686, 60, -498
rotate = 0, -36, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L7_D04
pos = -498, 60, -686
rotate = 0, -54, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_A02
pos = 806, -60, 257
rotate = 0, -18, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_A03
pos = 686, -60, 498
rotate = 0, -36, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_A04
pos = 498, -60, 686
rotate = 0, -54, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_B02
pos = -806, -60, 257
rotate = 0, 18, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_B03
pos = -686, -60, 498
rotate = 0, 36, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_B04
pos = -498, -60, 686
rotate = 0, 54, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_C02
pos = 806, -60, -257
rotate = 0, 18, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_C03
pos = 686, -60, -498
rotate = 0, 36, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_C04
pos = 498, -60, -686
rotate = 0, 54, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_D02
pos = -806, -60, -257
rotate = 0, -18, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_D03
pos = -686, -60, -498
rotate = 0, -36, 0
archetype = space_industrial02a
parent = co_mad_02

[Object]
nickname = co_mad_industrial_L8_D04
pos = -498, -60, -686
rotate = 0, -54, 0
archetype = space_industrial02a
parent = co_mad_02
'''
