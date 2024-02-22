from text.dividers import SINGLE_DIVIDER

SHAPES_ROCK = 'file = solar\\asteroids\\rock_shapes.ini'
SHAPES_DEBRIS = 'file = solar\\asteroids\\debris_shapes.ini'
SHAPES_OM15 = 'file = solar\\asteroids_mod\\om15\\shapes.ini'

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

AST_TEMPLATE = '''
[TexturePanels]
{shapes}

[Field]

[properties]

[Exclusion Zones]
{exclusions}

[Cube]

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

EXCLUSION_ITEM = '''
exclusion = {zone_name}
exclude_dynamic_asteroids = 1
'''


class AsteroidDefinition(object):
    ABSTRACT = True

    SHAPES = []
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

    NAME = None
    SUBFOLDER = 'GENERATED'

    def __init__(self, system):
        self.system = system
        self.exclusions = []
        if not self.NAME:
            raise Exception('NAME is mandatory for asteroid definition %s' % self.__class__.__name__)

    def add_exclusion(self, zone_name):
        self.exclusions.append(zone_name)

    def get_file_content(self):
        params = {
            'shapes': SINGLE_DIVIDER.join(self.SHAPES),
            'exclusions': SINGLE_DIVIDER.join([EXCLUSION_ITEM.format(zone_name=exclusion) for exclusion in self.exclusions]),
            'belt': '',
            'dynasteroids': '',
            'billboards': '',
            'loot_props': '',
        }
        if self.BELT:
            params['belt'] = self.BELT_TEMPLATE
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
