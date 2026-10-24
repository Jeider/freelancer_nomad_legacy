from world.names import *

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

{field_dust}

{far_rocks}

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

DYNAST_TAU29 = '''
[DynamicAsteroids]
asteroid = ast_tau29_normal_a
count = 30
placement_radius = 1000.000000
placement_offset = 200.000000
max_velocity = 20.000000
max_angular_velocity = 0.300000
color_shift = 1.000000, 1.000000, 1.000000

[DynamicAsteroids]
asteroid = ast_tau29_normal_b
count = 30
placement_radius = 1000.000000
placement_offset = 200.000000
max_velocity = 20.000000
max_angular_velocity = 0.300000
color_shift = 1.000000, 1.000000, 1.000000

[DynamicAsteroids]
asteroid = ast_tau29_normal_c
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
height = {belt_height}
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

BELT_TAU29 = '''
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

BILLBOARD_TAU29 = '''
[AsteroidBillboards]
count = 300
start_dist = 1100
fade_dist_percent = 0.500000
shape = tau29_billboards
color_shift = 0.6, 0.6, 0.6
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

DYNAST_NOMAD = '''
[DynamicAsteroids]
asteroid = mod_nomad_large
count = 40
placement_radius = 1200.000000
placement_offset = 500.000000
max_velocity = 3.000000
max_angular_velocity = 0.05000000
color_shift = 1.000000, 1.000000, 1.000000

[DynamicAsteroids]
asteroid = mod_nomad_large
count = 40
placement_radius = 1500.000000
placement_offset = 800.000000
max_velocity = 5.000000
max_angular_velocity = 0.05000000
color_shift = 1.000000, 1.000000, 1.000000
'''

LARGE_AST_FIELD_TEMPLATE = '''
cube_size = 1500
fill_dist = 5000
diffuse_color = 255, 255, 255
ambient_color = 255, 255, 255
ambient_increase = 0, 0, 0
empty_cube_frequency = 0
'''

LARGE_AST_CUBE_TEMPLATE = '''
asteroid = ast_{ast}_xlarge04, 0.600000, 0.200000, -0.200000, 1, 2, 5
asteroid = ast_{ast}_xlarge02, 0.200000, 0.800000, 0.300000, -5, -155, 3
asteroid = ast_{ast}_xlarge01, 0.400000, -0.700000, -0.200000, 2, 124, -4
asteroid = ast_{ast}_xlarge02, -0.300000, -0.300000, 0.800000, 7, -5, -8
asteroid = ast_{ast}_xlarge04, -0.200000, -0.100000, -0.600000, 0, 4, 5
asteroid = ast_{ast}_xlarge01, -0.600000, -0.800000, 0.700000, 1, 192, 5
'''



FIELD_DUST_TEMPLATE = '''[FieldDust]
opacity = 0.22
max_opacity = 0.35
brightness = 0.8
ambient = 0.12
forward = 0.55
forward_weight = 0.5
back = 0.25
noise_scale = 4000
coverage = 0.45
softness = 0.25
clump = 0.7
steps = 6'''

FAR_ROCKS_TEMPLATE = '''[FarRocks]
replace_band = 1'''


# BEGIN ordinary-world mesh Band profiles v1
ORDINARY_WORLD_MESH_FAR_ROCKS = """[FarRocks]
type = mesh
count = 1000
model_scale = 3
start_dist = 4500
start_fade = 700
replace_band = 1"""

ORDINARY_WORLD_DEBRIS_FAR_ROCKS = """[FarRocks]
type = debris
count = 1000
model_scale = 2
size_power = 2.3
edge_softness = 1.2
clump_size = 3200
clump_coverage = 0.45
clump_softness = 0.2
clump_amount = 0.65
start_dist = 4500
start_fade = 700
far_dist = 55000
far_fade = 18000
color = 255, 255, 255
brightness = 1.0
ambient = 1.0
min_pixels = 1
solid_pixels = 5
replace_band = 1"""

ORDINARY_WORLD_DEBRIS_FIELD_DUST = """[FieldDust]
opacity = 0.06
max_opacity = 0.10
color = 110, 115, 120
brightness = 0.65
ambient = 0.18
forward = 0.35
forward_weight = 0.3
back = 0.1
noise_scale = 3200
coverage = 0.5
softness = 0.2
clump = 0.65
edge_softness = 1.2
clear_radius = 1000
steps = 8
lod_distance = 100000
far_dist = 55000
far_fade = 18000
exclude_zones = 1"""


def _ordinary_world_mesh_band(field, params):
    system = field.system
    name = str(getattr(system, 'NAME', '')).lower()
    if (getattr(system, 'SYSTEMS_ROOT', None) != 'SYSTEMS_MOD'
            or getattr(system, 'IS_STORY', False)
            or not name or name in ('om11', 'tau44', 'm8_tau44')
            or name.startswith('sphere')
            or not field.BELT or not field.DYNAST or not field.FAR_ROCKS):
        return
    # Even a non-asteroid Cube directive is conservatively considered filled.
    def active_lines(value):
        return [line.split(';', 1)[0].split('#', 1)[0].strip()
                for line in value.splitlines()
                if line.split(';', 1)[0].split('#', 1)[0].strip()]
    if active_lines(params['cube']):
        return
    if '[band]' not in [line.lower() for line in active_lines(params['belt'])]:
        return
    models = []
    section = ''
    for line in active_lines(params['dynasteroids']):
        if line.startswith('['):
            section = line.lower()
        elif section == '[dynamicasteroids]' and '=' in line:
            key, value = line.split('=', 1)
            if key.strip().lower() == 'asteroid' and value.strip():
                models.append(value.strip().split(',', 1)[0].strip())
    if not models or any(not model or '{' in model or '}' in model for model in models):
        return
    debris = isinstance(field, DebrisDefinition) or all(
        model.lower().startswith('din_debris_') for model in models)
    params['far_rocks'] = (ORDINARY_WORLD_DEBRIS_FAR_ROCKS if debris
                           else ORDINARY_WORLD_MESH_FAR_ROCKS)
    if debris and field.FIELD_DUST:
        params['field_dust'] = ORDINARY_WORLD_DEBRIS_FIELD_DUST
# END ordinary-world mesh Band profiles v1


class AsteroidDefinition(object):
    NAME = 'ast'
    SHAPES = []
    FIELD_TEMPLATE = None
    FIELD = False
    CUBE_TEMPLATE = None
    CUBE_PARAMS = {}
    CUBE = False
    BELT_TEMPLATE = None
    BELT = False
    FAR_ROCKS_TEMPLATE = FAR_ROCKS_TEMPLATE
    FAR_ROCKS = True  # with a BELT: far rock shells replace the band
    FIELD_DUST_TEMPLATE = FIELD_DUST_TEMPLATE
    FIELD_DUST = True  # with a BELT: the field's dust volume
    DYNAST_TEMPLATE = None
    DYNAST = False
    BILLBOARD_TEMPLATE = None
    BILLBOARDS = False
    LOOT = False
    LOOT_MIN = 1
    LOOT_MAX = 1
    LOOT_DIFFICULTY = 10
    LOOT_CONTAINER = LOOT_WATER
    LOOT_COMMODITY = None
    BELT_HEIGHT = BELT_HEIGHT_DEFAULT
    EXCLUDE_BILLBOARDS = True
    EXCLUSION_SIZE_OVERRIDE = 0

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
            'far_rocks': '',
            'field_dust': '',
            'dynasteroids': '',
            'billboards': '',
            'loot_props': '',
            'field': '',
            'cube': '',
        }
        if self.FIELD:
            params['field'] = self.FIELD_TEMPLATE
        if self.CUBE:
            params['cube'] = self.CUBE_TEMPLATE.format(**self.CUBE_PARAMS)
        if self.BELT:
            params['belt'] = self.BELT_TEMPLATE.format(belt_height=self.BELT_HEIGHT)
        if self.FAR_ROCKS and self.BELT:
            params['far_rocks'] = self.FAR_ROCKS_TEMPLATE
        if self.FIELD_DUST and self.BELT:
            params['field_dust'] = self.FIELD_DUST_TEMPLATE
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
        _ordinary_world_mesh_band(self, params)
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


class Tau29AsteroidDefinition(AsteroidDefinition):
    BELT_TEMPLATE = BELT_TAU29
    DYNAST_TEMPLATE = DYNAST_TAU29
    BILLBOARD_TEMPLATE = BILLBOARD_TAU29
    SHAPES = [
        SHAPES_ROCK,
        SHAPES_TAU29,
    ]


class DebrisDefinition(AsteroidDefinition):
    NAME = 'debris'
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

# OM15 - niobium
# TAU29 - diamond
#
# LI_CAL - berilium
# CO_CUR - nicollum
#
# KU_TGK - gold
# LI_CAL - SILVER
#
# TAU37 - URANIUM
#
# CO_CUR - PLUMBUM


class Omega15NiobiumAsteroidDefinition(Omega15AsteroidDefinition):
    BELT = False
    BILLBOARDS = False
    DYNAST = True
    LOOT = True
    LOOT_CONTAINER = LOOT_NIOBIUM
    LOOT_COMMODITY = roid(NIOBIUM)


class Tau29DiamondAsteroidDefinition(Tau29AsteroidDefinition):
    BELT = False
    BILLBOARDS = False
    DYNAST = True
    LOOT = True
    LOOT_CONTAINER = LOOT_NIOBIUM
    LOOT_COMMODITY = roid(DIAMONDS)


class CaliforniaBeriliumAsteroidDefinition(CaliforniaAsteroidDefinition):
    BELT = False
    BILLBOARDS = False
    DYNAST = True
    LOOT = True
    LOOT_CONTAINER = LOOT_BERYL
    LOOT_COMMODITY = roid(BERILIUM)


class CuracaoPlumbumAsteroidDefinition(CuracaoAsteroidDefinition):
    BELT = False
    BILLBOARDS = False
    DYNAST = True
    LOOT = True
    LOOT_CONTAINER = LOOT_BERYL
    LOOT_COMMODITY = roid(PLUMBUM)


class Tau37UraniumAsteroidDefinition(Tau37AsteroidDefinition):
    BELT = False
    BILLBOARDS = False
    DYNAST = True
    LOOT = True
    LOOT_CONTAINER = LOOT_COBALT
    LOOT_COMMODITY = roid(URANIUM)


class TekagiSilverAsteroidDefinition(TekagiAsteroidDefinition):
    BELT = False
    BILLBOARDS = False
    DYNAST = True
    LOOT = True
    LOOT_CONTAINER = LOOT_SILVER
    LOOT_COMMODITY = roid(SILVER)


class TekagiGoldAsteroidDefinition(TekagiAsteroidDefinition):
    BELT = False
    BILLBOARDS = False
    DYNAST = True
    LOOT = True
    LOOT_CONTAINER = LOOT_GOLD
    LOOT_COMMODITY = roid(GOLD)


class SpaceMines(AsteroidDefinition):
    NAME = 'space_mines'
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
    NAME = 'badland'
    DYNAST = True
    DYNAST_TEMPLATE = DYNAST_BADLANDS


class NomadDynasteroids(AsteroidDefinition):
    DYNAST = True
    DYNAST_TEMPLATE = DYNAST_NOMAD


class Tau37LargeAsteroids(Tau37AsteroidDefinition):
    FIELD_TEMPLATE = LARGE_AST_FIELD_TEMPLATE
    CUBE_TEMPLATE = LARGE_AST_CUBE_TEMPLATE
    CUBE_PARAMS = {'ast': 'tau37'}
    FIELD = True
    CUBE = True
