from text.dividers import SINGLE_DIVIDER

SHAPES_ROCK = 'file = solar\\asteroids\\rock_shapes.ini'
SHAPES_OM15 = 'file = solar\\asteroids_mod\\om15\\shapes.ini'

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
    LOOT_CONTAINER = 'lootcrate_ast_loot_niobium'
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


class Omega15NiobiumAsteroidDefinition(Omega15AsteroidDefinition):
    BELT = False
    BILLBOARD = False
    DYNAST = True
    LOOT = True
    LOOT_CONTAINER = 'lootcrate_ast_loot_niobium'
    LOOT_COMMODITY = 'comm_roid_niobium'
