from text.dividers import SINGLE_DIVIDER

SHAPES_ROCK = 'file = solar\\asteroids\\rock_shapes.ini'
SHAPES_MINES = 'file = solar\\asteroids\\mine_shapes.ini'
SHAPES_DEBRIS = 'file = solar\\asteroids\\debris_shapes.ini'
SHAPES_OM15 = 'file = solar\\asteroids_mod\\om15\\shapes.ini'
SHAPES_LI_CAL = 'file = solar\\asteroids_mod\\li_cal\\shapes.ini'
SHAPES_KU_TGK = 'file = solar\\asteroids_mod\\ku_tgk\\shapes.ini'
SHAPES_TAU37 = 'file = solar\\asteroids_mod\\tau37\\shapes.ini'
SHAPES_CO_CUR = 'file = solar\\asteroids_mod\\co_cur\\shapes.ini'
SHAPES_TAU29 = 'file = solar\\asteroids_mod\\tau29\\shapes.ini'
SHAPES_LAVA = 'file = solar\\asteroids_mod\\lava\\shapes.ini'

LOOT_BERYL = 'lootcrate_ast_loot_beryl'
LOOT_ORGANISMS = 'lootcrate_ast_loot_organisms'
LOOT_DIAMONDS = 'lootcrate_ast_loot_diamonds'
LOOT_COPPER = 'lootcrate_ast_loot_copper'
LOOT_COBALT = 'lootcrate_ast_loot_cobalt'
LOOT_ARTIFACTS = 'lootcrate_ast_loot_artifacts'
LOOT_SILVER = 'lootcrate_ast_loot_silver'
LOOT_COAL = 'lootcrate_ast_loot_coal'
LOOT_GOLD = 'lootcrate_ast_loot_gold'
LOOT_METAL = 'lootcrate_ast_loot_metal'
LOOT_NIOBIUM = 'lootcrate_ast_loot_niobium'
LOOT_OXYGEN = 'lootcrate_ast_loot_oxygen'
LOOT_WATER = 'lootcrate_ast_loot_water'

BELT_HEIGHT_DEFAULT = 4000

AST_TEMPLATE = '''
[TexturePanels]
{shapes}

[Field]
{field}

[properties]

[Exclusion Zones]
{exclusions}

[Cube]
{cube}

{dynasteroids}

{belt}

{billboards}

{loot_props}
'''

DYNAST_OM15 = '''
[DynamicAsteroids]
asteroid = ast_om15_normal_a
count = 30
placement_radius = 1000.000000
placement_offset = 200.000000
max_velocity = 20.000000
max_angular_velocity = 0.300000
color_shift = 1.000000, 1.000000, 1.000000

[DynamicAsteroids]
asteroid = ast_om15_normal_b
count = 30
placement_radius = 1000.000000
placement_offset = 200.000000
max_velocity = 20.000000
max_angular_velocity = 0.300000
color_shift = 1.000000, 1.000000, 1.000000

[DynamicAsteroids]
asteroid = ast_om15_normal_c
count = 30
placement_radius = 1000.000000
placement_offset = 200.000000
max_velocity = 20.000000
max_angular_velocity = 0.300000
color_shift = 1.000000, 1.000000, 1.000000
'''

DYNAST_LI_CAL = '''
[DynamicAsteroids]
asteroid = ast_li_cal_normal_a
count = 30
placement_radius = 1000.000000
placement_offset = 200.000000
max_velocity = 20.000000
max_angular_velocity = 0.300000
color_shift = 1.000000, 1.000000, 1.000000

[DynamicAsteroids]
asteroid = ast_li_cal_normal_b
count = 30
placement_radius = 1000.000000
placement_offset = 200.000000
max_velocity = 20.000000
max_angular_velocity = 0.300000
color_shift = 1.000000, 1.000000, 1.000000

[DynamicAsteroids]
asteroid = ast_li_cal_normal_c
count = 30
placement_radius = 1000.000000
placement_offset = 200.000000
max_velocity = 20.000000
max_angular_velocity = 0.300000
color_shift = 1.000000, 1.000000, 1.000000
'''

DYNAST_TAU37 = '''
[DynamicAsteroids]
asteroid = ast_tau37_normal_a
count = 30
placement_radius = 1000.000000
placement_offset = 200.000000
max_velocity = 20.000000
max_angular_velocity = 0.300000
color_shift = 1.000000, 1.000000, 1.000000

[DynamicAsteroids]
asteroid = ast_tau37_normal_b
count = 30
placement_radius = 1000.000000
placement_offset = 200.000000
max_velocity = 20.000000
max_angular_velocity = 0.300000
color_shift = 1.000000, 1.000000, 1.000000

[DynamicAsteroids]
asteroid = ast_tau37_normal_c
count = 30
placement_radius = 1000.000000
placement_offset = 200.000000
max_velocity = 20.000000
max_angular_velocity = 0.300000
color_shift = 1.000000, 1.000000, 1.000000
'''

DYNAST_KU_TGK = '''
[DynamicAsteroids]
asteroid = ast_ku_tgk_normal_a
count = 30
placement_radius = 1000.000000
placement_offset = 200.000000
max_velocity = 20.000000
max_angular_velocity = 0.300000
color_shift = 1.000000, 1.000000, 1.000000

[DynamicAsteroids]
asteroid = ast_ku_tgk_normal_b
count = 30
placement_radius = 1000.000000
placement_offset = 200.000000
max_velocity = 20.000000
max_angular_velocity = 0.300000
color_shift = 1.000000, 1.000000, 1.000000

[DynamicAsteroids]
asteroid = ast_ku_tgk_normal_c
count = 30
placement_radius = 1000.000000
placement_offset = 200.000000
max_velocity = 20.000000
max_angular_velocity = 0.300000
color_shift = 1.000000, 1.000000, 1.000000
'''

DYNAST_CO_CUR = '''
[DynamicAsteroids]
asteroid = ast_co_cur_normal_a
count = 30
placement_radius = 1000.000000
placement_offset = 200.000000
max_velocity = 20.000000
max_angular_velocity = 0.300000
color_shift = 1.000000, 1.000000, 1.000000

[DynamicAsteroids]
asteroid = ast_co_cur_normal_b
count = 30
placement_radius = 1000.000000
placement_offset = 200.000000
max_velocity = 20.000000
max_angular_velocity = 0.300000
color_shift = 1.000000, 1.000000, 1.000000

[DynamicAsteroids]
asteroid = ast_co_cur_normal_c
count = 30
placement_radius = 1000.000000
placement_offset = 200.000000
max_velocity = 20.000000
max_angular_velocity = 0.300000
color_shift = 1.000000, 1.000000, 1.000000
'''

DYNAST_DEBRIS = '''
[DynamicAsteroids]
asteroid = din_debris_xlarge_A
count = 20
placement_radius = 2000.000000
placement_offset = 600.000000
max_velocity = 10.000000
max_angular_velocity = 0.100000
color_shift = 1.000000, 1.000000, 1.000000

[DynamicAsteroids]
asteroid = din_debris_xlarge_B
count = 20
placement_radius = 2000.000000
placement_offset = 600.000000
max_velocity = 10.000000
max_angular_velocity = 0.100000
color_shift = 1.000000, 1.000000, 1.000000

[DynamicAsteroids]
asteroid = din_debris_xlarge_C
count = 20
placement_radius = 2000.000000
placement_offset = 600.000000
max_velocity = 10.000000
max_angular_velocity = 0.100000
color_shift = 1.000000, 1.000000, 1.000000

[DynamicAsteroids]
asteroid = din_debris_xlarge_D
count = 8
placement_radius = 2000.000000
placement_offset = 600.000000
max_velocity = 10.000000
max_angular_velocity = 0.100000
color_shift = 1.000000, 1.000000, 1.000000
'''

BELT_OM15 = '''
[Band]
render_parts = 6
shape = asteroid_belt_06
height = 4000
offset_dist = 2000
fade = 0.800000, 1.250000, 15, 17
texture_aspect = 1.000000
ambient_intensity = 0.400000
vert_increase = 2
color_shift = 1, 0.85, 0.8
'''

BELT_LI_CAL = '''
[Band]
render_parts = 6
shape = asteroid_belt_06
height = {belt_height}
offset_dist = 2000
fade = 0.800000, 1.250000, 15, 17
texture_aspect = 1.000000
ambient_intensity = 0.400000
vert_increase = 2
color_shift = 0.8, 0.8, 0.8
'''

BELT_KU_TGK = '''
[Band]
render_parts = 6
shape = asteroid_belt_06
height = {belt_height}
offset_dist = 2000
fade = 0.800000, 1.250000, 15, 17
texture_aspect = 1.000000
ambient_intensity = 0.400000
vert_increase = 2
color_shift = 0.8, 0.9, 1
'''

BELT_TAU37 = '''
[Band]
render_parts = 6
shape = asteroid_belt_06
height = {belt_height}
offset_dist = 2000
fade = 0.800000, 1.250000, 15, 17
texture_aspect = 1.000000
ambient_intensity = 0.400000
vert_increase = 2
color_shift = 0.9, 0.95, 1
'''

BELT_CO_CUR = '''
[Band]
render_parts = 6
shape = asteroid_belt_06
height = {belt_height}
offset_dist = 2000
fade = 0.800000, 1.250000, 15, 17
texture_aspect = 1.000000
ambient_intensity = 0.400000
vert_increase = 2
color_shift = 1, 1, 0.9
'''

BELT_DEBRIS = '''
[Band]
render_parts = 10
shape = debris_belt_04
height = 5000
offset_dist = 2500
fade = 1.100000, 1.450000, 10, 11
texture_aspect = 1.000000
color_shift = 0.800000, 0.800000, 0.800000
ambient_intensity = 1.000000
vert_increase = 1
'''

BILLBOARD_OM15 = '''
[AsteroidBillboards]
count = 300
start_dist = 1100
fade_dist_percent = 0.500000
shape = background_om15
color_shift = 0.800000, 0.750000, 0.750000
ambient_intensity = 1
size = 40, 150
'''

BILLBOARD_LI_CAL = '''
[AsteroidBillboards]
count = 300
start_dist = 1100
fade_dist_percent = 0.500000
shape = background_li_cal
color_shift = 0.8, 0.8, 0.8
ambient_intensity = 1
size = 40, 150
'''

BILLBOARD_TAU37 = '''
[AsteroidBillboards]
count = 300
start_dist = 1100
fade_dist_percent = 0.500000
shape = background_tau37
color_shift = 1, 1, 1
ambient_intensity = 1
size = 40, 150
'''

BILLBOARD_KU_TGK = '''
[AsteroidBillboards]
count = 300
start_dist = 1100
fade_dist_percent = 0.500000
shape = background_ku_tgk
color_shift = 1, 1, 1
ambient_intensity = 1
size = 40, 150
'''

BILLBOARD_CO_CUR = '''
[AsteroidBillboards]
count = 300
start_dist = 1100
fade_dist_percent = 0.500000
shape = background_co_cur
color_shift = 1, 1, 1
ambient_intensity = 1
size = 40, 150
'''

BILLBOARD_DEBRIS = '''
[AsteroidBillboards]
count = 500
start_dist = 1500
fade_dist_percent = 0.800000
shape = debris_tri
color_shift = 1, 1, 1
ambient_intensity = 1.000000
size = 100, 250
'''

LOOT_PROPS = '''
[LootableZone]
dynamic_loot_container = {loot_container}
dynamic_loot_commodity = {loot_commodity}
dynamic_loot_count = {loot_min}, {loot_max}
dynamic_loot_difficulty = {loot_difficulty}
'''

EXCLUSION_NAME_TEMPLATE = 'exclusion = {zone_name}'
EXCLUDE_DYNAST = 'exclude_dynamic_asteroids = 1'
EXCLUDE_BILLBOARDS = 'exclude_billboards = 1'

MINES_FIELD_TEMPLATE = '''
cube_size = 500
fill_dist = 1500
diffuse_color = 200, 200, 200
ambient_color = 110, 110, 110
ambient_increase = 80, 80, 80
empty_cube_frequency = 0.0
'''

MINES_CUBE_TEMPLATE = '''
asteroid = mine_spike_minedout, 0.200000, 0.800000, 0.300000, 45, 20, 0, mine
asteroid = mine_spike_minedout, 0.600000, 0.200000, -0.200000, 35, 10, 20, mine
asteroid = mine_spike_minedout, 0.400000, -0.700000, -0.200000, 15, 90, 120, mine
asteroid = mine_spike_minedout, -0.200000, -0.100000, -0.600000, 105, 160, 25, mine
asteroid = mine_spike_minedout, 0.500000, -0.200000, -0.600000, 75, 30, 70, mine
asteroid = mine_spike_minedout, -0.700000, 0.400000, -0.400000, 75, 30, 70, mine
asteroid = mine_spike_minedout, -0.200000, 0.600000, 0.600000, 105, 160, 25, mine
asteroid = mine_spike_minedout, -0.500000, -0.200000, 0.600000, 75, 30, 70, mine
'''

MINES_BILLBOARD_TEMPLATE = '''
[AsteroidBillboards]
count = 600
start_dist = 2500
fade_dist_percent = 0.900000
shape = spike_mine_tri_minedout
size = 300, 300
'''

DYNAST_BADLANDS = '''
[DynamicAsteroids]
asteroid = mod_dbadlands_large
count = 40
placement_radius = 1200.000000
placement_offset = 500.000000
max_velocity = 3.000000
max_angular_velocity = 0.05000000
color_shift = 1.000000, 1.000000, 1.000000

[DynamicAsteroids]
asteroid = mod_dbadlands_large
count = 40
placement_radius = 1500.000000
placement_offset = 800.000000
max_velocity = 5.000000
max_angular_velocity = 0.05000000
color_shift = 1.000000, 1.000000, 1.000000
'''


class AsteroidDefinition(object):
    SHAPES = []
    FIELD_TEMPLATE = None
    FIELD = False
    CUBE_TEMPLATE = None
    CUBE = False
    BELT_TEMPLATE = None
    BELT = False
    DYNAST_TEMPLATE = None
    DYNAST = False
    BILLBOARD_TEMPLATE = None
    BILLBOARDS = False
    LOOT = False
    LOOT_MIN = 1
    LOOT_MAX = 2
    LOOT_DIFFICULTY = 2
    LOOT_CONTAINER = LOOT_WATER
    LOOT_COMMODITY = None
    BELT_HEIGHT = BELT_HEIGHT_DEFAULT
    EXCLUDE_BILLBOARDS = True

    def __init__(self, system, zone):
        self.system = system
        self.zone = zone
        self.exclusions = []

    def get_file_name(self):
        return self.zone.get_file_name()

    def add_exclusion(self, zone_name):
        self.exclusions.append(zone_name)

    def get_file_content(self):
        exclusion_params = [
            EXCLUSION_NAME_TEMPLATE,
            EXCLUDE_DYNAST,
        ]
        if self.EXCLUDE_BILLBOARDS:
            exclusion_params.append(EXCLUDE_BILLBOARDS)
        exclusion_template = SINGLE_DIVIDER.join(exclusion_params)

        params = {
            'shapes': SINGLE_DIVIDER.join(self.SHAPES),
            'exclusions': SINGLE_DIVIDER.join([exclusion_template.format(zone_name=exclusion) for exclusion in self.exclusions]),
            'belt': '',
            'dynasteroids': '',
            'billboards': '',
            'loot_props': '',
            'field': '',
            'cube': '',
        }
        if self.FIELD:
            params['field'] = self.FIELD_TEMPLATE
        if self.CUBE:
            params['cube'] = self.CUBE_TEMPLATE
        if self.BELT:
            params['belt'] = self.BELT_TEMPLATE.format(belt_height=self.BELT_HEIGHT)
        if self.DYNAST:
            params['dynasteroids'] = self.DYNAST_TEMPLATE
        if self.BILLBOARDS:
            params['billboards'] = self.BILLBOARD_TEMPLATE
        if self.LOOT:
            params['loot_props'] = LOOT_PROPS.format(
                loot_container=self.LOOT_CONTAINER,
                loot_commodity=self.LOOT_COMMODITY,
                loot_min=self.LOOT_MIN,
                loot_max=self.LOOT_MAX,
                loot_difficulty=self.LOOT_DIFFICULTY,
            )
        return AST_TEMPLATE.format(**params)


class Omega15AsteroidDefinition(AsteroidDefinition):
    BELT_TEMPLATE = BELT_OM15
    DYNAST_TEMPLATE = DYNAST_OM15
    BILLBOARD_TEMPLATE = BILLBOARD_OM15
    SHAPES = [
        SHAPES_ROCK,
        SHAPES_OM15,
    ]


class CaliforniaAsteroidDefinition(AsteroidDefinition):
    BELT_TEMPLATE = BELT_LI_CAL
    DYNAST_TEMPLATE = DYNAST_LI_CAL
    BILLBOARD_TEMPLATE = BILLBOARD_LI_CAL
    SHAPES = [
        SHAPES_ROCK,
        SHAPES_LI_CAL,
    ]


class Tau37AsteroidDefinition(AsteroidDefinition):
    BELT_TEMPLATE = BELT_TAU37
    DYNAST_TEMPLATE = DYNAST_TAU37
    BILLBOARD_TEMPLATE = BILLBOARD_TAU37
    SHAPES = [
        SHAPES_ROCK,
        SHAPES_TAU37,
    ]


class TekagiAsteroidDefinition(AsteroidDefinition):
    BELT_TEMPLATE = BELT_KU_TGK
    DYNAST_TEMPLATE = DYNAST_KU_TGK
    BILLBOARD_TEMPLATE = BILLBOARD_KU_TGK
    SHAPES = [
        SHAPES_ROCK,
        SHAPES_KU_TGK,
    ]


class CuracaoAsteroidDefinition(AsteroidDefinition):
    BELT_TEMPLATE = BELT_CO_CUR
    DYNAST_TEMPLATE = DYNAST_CO_CUR
    BILLBOARD_TEMPLATE = BILLBOARD_CO_CUR
    SHAPES = [
        SHAPES_ROCK,
        SHAPES_CO_CUR,
    ]


class DebrisDefinition(AsteroidDefinition):
    BELT_TEMPLATE = BELT_DEBRIS
    DYNAST_TEMPLATE = DYNAST_DEBRIS
    BILLBOARD_TEMPLATE = BILLBOARD_DEBRIS
    SHAPES = [
        SHAPES_DEBRIS,
    ]
    BELT = True
    BILLBOARDS = True
    DYNAST = True
    LOOT = True
    LOOT_MIN = 1
    LOOT_MAX = 2
    LOOT_DIFFICULTY = 2
    LOOT_CONTAINER = LOOT_METAL
    LOOT_COMMODITY = 'comm_scrap_metal'


class Omega15NiobiumAsteroidDefinition(Omega15AsteroidDefinition):
    BELT = False
    BILLBOARDS = False
    DYNAST = True
    LOOT = True
    LOOT_CONTAINER = 'lootcrate_ast_loot_niobium'
    LOOT_COMMODITY = 'comm_roid_niobium'


class SpaceMines(AsteroidDefinition):
    FIELD = True
    CUBE = True
    BILLBOARDS = True
    FIELD_TEMPLATE = MINES_FIELD_TEMPLATE
    CUBE_TEMPLATE = MINES_CUBE_TEMPLATE
    BILLBOARD_TEMPLATE = MINES_BILLBOARD_TEMPLATE
    SHAPES = [
        SHAPES_MINES,
    ]


class BadlansDynasteroids(AsteroidDefinition):
    DYNAST = True
    DYNAST_TEMPLATE = DYNAST_BADLANDS
