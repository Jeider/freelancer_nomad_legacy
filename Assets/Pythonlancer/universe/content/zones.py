from fx.space import Dust
from fx.sound import Ambience

from universe.content.system_object import SystemObject, NamedDynamicSystemObject

from text.dividers import SINGLE_DIVIDER, DIVIDER

SHAPE_SPHERE = 'SPHERE'


class RawZone(SystemObject):
    ABSTRACT = True

    ZONE_NICKNAME_TEMPLATE = 'Zone_{base_alias}'
    ZONE_TEMPLATE = '''[Zone]
{params}'''

    def __init__(self, *args, **kwargs):
        self.zone_params = kwargs.get('zone_params')
        super().__init__(*args, **kwargs)

    def get_system_content(self):
        content = ['{} = {}'.format(key, value) for key, value in self.zone_params.items()]
        return self.ZONE_TEMPLATE.format(params=SINGLE_DIVIDER.join(content))


class Zone(SystemObject):
    ABSTRACT = True

    ZONE_NICKNAME_TEMPLATE = 'Zone_{base_alias}'
    ZONE_TEMPLATE = '''[Zone]
{params}'''

    def get_zone_main_params(self):
        shape = self.get_shape().upper()
        if shape == SHAPE_SPHERE:
            size = '{}'.format(self.get_size()[0])
        else:
            size = '{}, {}, {}'.format(*self.get_size())

        return {
            'nickname': self.get_zone_nickame(),
            'pos': '{}, {}, {}'.format(*self.get_zone_position()),
            'rotate': '{}, {}, {}'.format(*self.get_rotate()),
            'shape': shape,
            'size': size,
        }

    def get_zone_merged_params(self):
        return ''

    def get_system_content(self):
        params = self.get_zone_main_params()
        params.update(self.get_zone_extra_parameters())
        content = ['{} = {}'.format(key, value) for key, value in params.items()]
        content.append(self.get_zone_merged_params())
        return self.ZONE_TEMPLATE.format(params=SINGLE_DIVIDER.join(content))

    def get_zone_extra_parameters(self):
        return {}

    def get_zone_nickame(self):
        return self.ZONE_NICKNAME_TEMPLATE.format(
            base_alias=self.get_zone_base_alias()
        )

    def get_zone_base_alias(self):
        print(self.__class__.__name__)
        raise NotImplementedError()

    def get_zone_position(self):
        return self.get_position()


class DynamicZone(NamedDynamicSystemObject, Zone):

    def __init__(self, *args, **kwargs):
        self.interference = kwargs.get('interference')
        self.damage = kwargs.get('damage')
        self.sort = kwargs.get('sort')
        self.spacedust = kwargs.get('spacedust')
        self.spacedust_maxparticles = kwargs.get('spacedust_maxparticles')
        self.position = kwargs.get('position')
        self.music = kwargs.get('music')
        self.edge_fraction = kwargs.get('edge_fraction')
        self.merged_params = kwargs.get('merged_params')
        self.drag_modifier = kwargs.get('drag_modifier')
        super().__init__(*args, **kwargs)

    def get_zone_nickame(self):
        return self.space_nickname

    def get_zone_position(self):
        if self.position:
            return self.position
        else:
            return super().get_zone_position()

    def get_zone_extra_parameters(self):
        params = {}
        if self.music:
            params['music'] = self.music
        if self.interference:
            params['interference'] = self.interference
        if self.damage:
            params['damage'] = self.damage
        if self.sort:
            params['sort'] = self.sort
        if self.spacedust:
            params['spacedust'] = self.spacedust
        if self.spacedust_maxparticles:
            params['spacedust_maxparticles'] = self.spacedust_maxparticles
        if self.edge_fraction:
            params['edge_fraction'] = self.edge_fraction
        if self.drag_modifier:
            params['drag_modifier'] = self.drag_modifier
        return params

    def get_zone_merged_params(self):
        if self.merged_params:
            return self.merged_params
        return ''


class SphereZone(Zone):
    def get_zone_main_params(self):
        return {
            'nickname': self.get_zone_nickame(),
            'pos': '{}, {}, {}'.format(*self.get_zone_position()),
            'shape': 'SPHERE',
            'size': self.get_single_size(),
        }

    def get_single_size(self):
        raise NotImplementedError


class DynamicSphereZone(SphereZone, DynamicZone):

    def __init__(self, *args, **kwargs):
        self.size = kwargs.get('size')
        super().__init__(*args, **kwargs)

    def get_single_size(self):
        return self.size


class PropertyZone(Zone):
    ZONE_FIELD_TYPE = None

    ROOT_FOLDER = 'ASTEROIDS_MOD'
    MUSIC = None
    PROPERTY_FLAGS = None
    PROPERTY_FOG_COLOR = None

    SPACEDUST = None
    SPACEDUST_MAXPARTICLES = None

    INTERFERENCE = None
    DRAG_MODIFIER = None

    def get_zone_base_alias(self):
        return '{system_name}_{alias}_{zone_field_type}'.format(
            system_name=self.system.NAME,
            alias=self.get_full_alias(),
            zone_field_type=self.ZONE_FIELD_TYPE,
        )

    def get_zone_extra_parameters(self):
        params = {}
        if self.MUSIC:
            params['music'] = self.MUSIC
        if self.PROPERTY_FLAGS:
            params['property_flags'] = self.PROPERTY_FLAGS
        if self.PROPERTY_FOG_COLOR:
            params['property_fog_color'] = self.PROPERTY_FOG_COLOR
        if self.SPACEDUST:
            params['spacedust'] = self.SPACEDUST
        if self.SPACEDUST_MAXPARTICLES:
            params['spacedust_maxparticles'] = self.SPACEDUST_MAXPARTICLES
        if self.INTERFERENCE:
            params['interference'] = self.INTERFERENCE
        if self.DRAG_MODIFIER:
            params['drag_modifier'] = self.DRAG_MODIFIER
        return params


class BaseFileAppearanceZone(PropertyZone):
    ROOT_FOLDER = 'ASTEROIDS_MOD'

    def get_file_name(self):
        return f'gen_{self.get_zone_base_alias()}'


class BaseAsteroidZone(BaseFileAppearanceZone):
    ZONE_FIELD_TYPE = 'asteroids'

    ASTEROID_DEFINITION_CLASS = None
    ROOT_FOLDER = 'ASTEROIDS_MOD'
    SUBFOLDER = 'GENERATED'

    ASTEROID_DEFINITION_TEMPLATE = '''[Asteroids]
file = solar\\{root_folder}\\{subfolder}\\{file_name}.ini
zone = {zone}'''

    def __init__(self, *args, **kwargs):
        if self.ASTEROID_DEFINITION_CLASS is None:
            raise Exception('Asteroid definition class is mandatory for zone %s' % self.__class__.__name__)
        super().__init__(*args, **kwargs)

    def get_asteroid_definition_header(self):
        return self.ASTEROID_DEFINITION_TEMPLATE.format(
            root_folder=self.ROOT_FOLDER,
            subfolder=self.SUBFOLDER,
            file_name=self.get_file_name(),
            zone=self.get_zone_nickame(),
        )

    def get_file_name(self):
        return self.get_zone_base_alias()


class AsteroidZone(BaseAsteroidZone):
    ALIAS = 'ast'
    ZONE_FIELD_TYPE = 'asteroids'

    ROOT_FOLDER = 'ASTEROIDS_MOD'

    ASTEROID_DEFINITION_CLASS = None


class DebrisZone(BaseAsteroidZone):
    ALIAS = 'deb'
    ZONE_FIELD_TYPE = 'debris'

    MUSIC = Ambience.DEBRIS

    SPACEDUST = Dust.DEBRIS
    SPACEDUST_MAXPARTICLES = 50


class NebulaZone(BaseFileAppearanceZone):
    ZONE_FIELD_TYPE = 'nebula'
    ALIAS = 'neb'
    ROOT_FOLDER = 'NEBULA_MOD'
    CONTENT_TEMPLATE = None
    GENERATED_NEBULA_SUBFOLDER = 'GENERATED'

    NEBULA_DEFINITION_TEMPLATE = '''[Nebula]
file = solar\\{root_folder}\\{subfolder}\\{file_name}.ini
zone = {zone}'''

    def __init__(self, *args, **kwargs):
        self.exclusions = {}
        if self.CONTENT_TEMPLATE is None:
            raise Exception('Content template is mandatory for zone %s' % self.__class__.__name__)
        super().__init__(*args, **kwargs)

    def get_nebula_definition_header(self):
        return self.NEBULA_DEFINITION_TEMPLATE.format(
            root_folder=self.ROOT_FOLDER,
            file_name=self.get_file_name(),
            subfolder=self.GENERATED_NEBULA_SUBFOLDER,
            zone=self.get_zone_nickame(),
        )

    def get_file_name(self):
        return f'gen_{self.get_zone_base_alias()}'

    def add_exclusion(self, name, params):
        self.exclusions[name] = params

    def get_exclusions_content(self):
        entries = []
        for name, params in self.exclusions.items():
            excl_params = {'exclusion': name}
            excl_params.update(params)
            entry = SINGLE_DIVIDER.join(['{} = {}'.format(key, value) for key, value in excl_params.items()])
            entries.append(entry)

        return DIVIDER.join(entries)

    def get_file_content(self):
        return self.CONTENT_TEMPLATE().format(params={'exclusions': self.get_exclusions_content()})
