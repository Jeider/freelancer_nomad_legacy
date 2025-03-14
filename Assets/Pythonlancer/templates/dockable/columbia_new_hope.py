from templates.space_object_template import SpaceObjectTemplate


class ColumbiaNewHope(SpaceObjectTemplate):
    SPACE_OBJECT_NAME = 'li_col_05'
    TEMPLATE = '''[Object]
nickname = li_col_05
pos = 0, 0, 0
rotate = 0, 0, 0
archetype = space_shipping01_no_moor
{dock_props}

[Object]
nickname = li_col_05_ctrl_twr01
pos = 980, 170, 0
rotate = 0, 0, 0
archetype = space_control_tower
parent = li_col_05

[Object]
nickname = li_col_05_ctrl_block01
pos = 1100, 170, 0
rotate = 0, 90, 0
archetype = space_control_block
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A01
pos = 1167.5, 105, 0
rotate = 0, 0, 45
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A02
pos = 1042.5, 105, 0
rotate = 0, 0, 45
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A03
pos = 917.5, 105, 0
rotate = 0, 0, 45
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A04
pos = 792.5, 105, 0
rotate = 0, 0, 45
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A05
pos = 1105, 0, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A06
pos = 980, 0, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A07
pos = 855, 0, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A08
pos = 1167.5, -105, 0
rotate = 0, 0, 45
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A09
pos = 1042.5, -105, 0
rotate = 0, 0, 45
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A10
pos = 917.5, -105, 0
rotate = 0, 0, 45
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A11
pos = 792.5, -105, 0
rotate = 0, 0, 45
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A12
pos = 730, 0, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A13
pos = 1230, 0, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A20
pos = 1105, -210, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A21
pos = 980, -210, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A22
pos = 855, -210, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A23
pos = 1042.5, -315, 0
rotate = 0, 0, 45
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A24
pos = 917.5, -315, 0
rotate = 0, 0, 45
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A25
pos = 980, -420, 0
rotate = 0, 0, 0
archetype = space_industriala
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A26
pos = 980, -420, 110
rotate = -10, 0, 0
archetype = space_short_tube
parent = li_col_05

[Object]
nickname = li_col_05_industrial_A27
pos = 980, -420, -110
rotate = -10, 180, 0
archetype = space_short_tube
parent = li_col_05

[Object]
nickname = li_col_05_industrial_B01
pos = 980, 0, 350
rotate = 0, 90, 0
archetype = space_industrial02a
parent = li_col_05

[Object]
nickname = li_col_05_industrial_B02
pos = 980, 0, 500
rotate = 0, 90, 0
archetype = space_industrial02a
parent = li_col_05

[Object]
nickname = li_col_05_industrial_B03
pos = 1065, 0, 425
rotate = 0, 0, 0
archetype = space_industrial01a
parent = li_col_05

[Object]
nickname = li_col_05_industrial_B04
pos = 892, 0, 425
rotate = 0, 0, 0
archetype = space_industrial01a
parent = li_col_05

[Object]
nickname = li_col_05_industrial_B05
pos = 980, 0, 890
rotate = 0, 90, 0
archetype = space_industrial02a
parent = li_col_05

[Object]
nickname = li_col_05_industrial_B06
pos = 980, -200, 890
rotate = 90, 90, 0
archetype = space_industrial02a
parent = li_col_05

[Object]
nickname = li_col_05_industrial_B07
pos = 980, -200, -890
rotate = 90, 90, 0
archetype = space_industrial02a
parent = li_col_05

[Object]
nickname = li_col_05_dome01
pos = 980, 31, 1250
rotate = 0, 180, 0
archetype = space_dome
parent = li_col_05

[Object]
nickname = li_col_05_dome02
pos = 980, 31, -1250
rotate = 0, 0, 0
archetype = space_dome
parent = li_col_05

[Object]
nickname = li_col_05_girder_A01
pos = 1042.5, 105, 120
rotate = 20, -10, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_A02
pos = 917.5, 105, 120
rotate = 20, 10, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_A03
pos = 792.5, 105, 120
rotate = 20, 35, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_A04
pos = 1167.5, 105, 120
rotate = 20, -35, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_A05
pos = 1042.5, -105, 120
rotate = -20, -10, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_A06
pos = 917.5, -105, 120
rotate = -20, 10, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_A07
pos = 792.5, -105, 120
rotate = -20, 35, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_A08
pos = 1167.5, -105, 120
rotate = -20, -35, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_A09
pos = 1105, 0, 120
rotate = 0, -20, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_A10
pos = 980, 0, 120
rotate = 0, 0, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_A11
pos = 855, 0, 120
rotate = 0, 20, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A01
pos = 1035.5, -32, 630
rotate = 0, 0, -45
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A02
pos = 1035.5, 26, 630
rotate = 0, 0, -135
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A03
pos = 920.5, -32, 630
rotate = 0, 0, 45
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A04
pos = 920.5, 26, 630
rotate = 0, 0, 135
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A05
pos = 1035.5, -32, 770
rotate = 0, 0, -45
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A06
pos = 1035.5, 26, 770
rotate = 0, 0, -135
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A07
pos = 920.5, -32, 770
rotate = 0, 0, 45
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A08
pos = 920.5, 26, 770
rotate = 0, 0, 135
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A09
pos = 980, -41, 630
rotate = 0, 0, 0
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A10
pos = 980, 41, 630
rotate = 0, 0, 180
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A11
pos = 980, -41, 770
rotate = 0, 0, 0
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_A12
pos = 980, 41, 770
rotate = 0, 0, 180
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_habitat01
pos = 892, 210, 425
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = li_col_05

[Object]
nickname = li_col_05_habitat02
pos = 1065, 210, 425
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = li_col_05

[Object]
nickname = li_col_05_habitat03
pos = 892, 210, -425
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = li_col_05

[Object]
nickname = li_col_05_habitat04
pos = 1065, 210, -425
rotate = 0, 0, 0
archetype = space_habitat_tall
parent = li_col_05

[Object]
nickname = li_col_05_girder_B01
pos = 1042.5, 105, -120
rotate = 20, -170, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_B02
pos = 917.5, 105, -120
rotate = 20, 170, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_B03
pos = 792.5, 105, -120
rotate = 20, 155, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_B04
pos = 1167.5, 105, -120
rotate = 20, -155, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_B05
pos = 1042.5, -105, -120
rotate = -20, -170, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_B06
pos = 917.5, -105, -120
rotate = -20, 170, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_B07
pos = 792.5, -105, -120
rotate = -20, 155, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_B08
pos = 1167.5, -105, -120
rotate = -20, -155, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_B09
pos = 1105, 0, -120
rotate = 0, -160, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_B10
pos = 980, 0, -120
rotate = 0, 180, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_girder_B11
pos = 855, 0, -120
rotate = 0, 160, 0
archetype = space_girdera
parent = li_col_05

[Object]
nickname = li_col_05_industrial_C01
pos = 980, 0, -350
rotate = 0, 90, 0
archetype = space_industrial02a
parent = li_col_05

[Object]
nickname = li_col_05_industrial_C02
pos = 980, 0, -500
rotate = 0, 90, 0
archetype = space_industrial02a
parent = li_col_05

[Object]
nickname = li_col_05_industrial_C03
pos = 1065, 0, -425
rotate = 0, 1, 0
archetype = space_industrial01a
parent = li_col_05

[Object]
nickname = li_col_05_industrial_C04
pos = 892, 0, -425
rotate = 0, 0, 0
archetype = space_industrial01a
parent = li_col_05

[Object]
nickname = li_col_05_industrial_C05
pos = 980, 0, -890
rotate = 1, 90, 0
archetype = space_industrial02a
parent = li_col_05

[Object]
nickname = li_col_05_tanks_B01
pos = 1035.5, -32, -630
rotate = 0, 0, -45
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_B02
pos = 1035.5, 26, -630
rotate = 0, 0, -135
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_B03
pos = 920.5, -32, -630
rotate = 0, 0, 45
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_B04
pos = 920.5, 26, -630
rotate = 0, 0, 135
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_B05
pos = 1035.5, -32, -770
rotate = 0, 0, -45
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_B06
pos = 1035.5, 26, -770
rotate = 0, 0, -135
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_B07
pos = 920.5, -32, -770
rotate = 0, 0, 45
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_B08
pos = 920.5, 26, -770
rotate = 0, 0, 135
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_B09
pos = 980, -41, -630
rotate = 0, 0, 0
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_B10
pos = 980, 41, -630
rotate = 0, 0, 180
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_B11
pos = 980, -41, -770
rotate = 0, 0, 0
archetype = space_tanks4
parent = li_col_05

[Object]
nickname = li_col_05_tanks_B12
pos = 980, 41, -770
rotate = 0, 0, 180
archetype = space_tanks4
parent = li_col_05
'''
