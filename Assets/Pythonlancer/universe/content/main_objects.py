import random
from random import randint

from fx.space import Dust
import fx.neuralnet as nn

from world.names import *
from universe import markets

from universe.content import meta
from universe.content.system_object import SystemObject, TOP, BOTTOM, LEFT, RIGHT, DIRECTIONS, POS_KEY, ROT_KEY, SIZE_KEY
from universe.content.zones import DynamicZone, DynamicSphereZone, RawZone
from universe.content import interior
from universe.content.locked_dock_key import LockedDockKey
from universe.audio.space_voice import SpaceVoice, SpaceCostume
from universe.content.loadout import Loadout
from universe import connection
from universe import faction
from universe.content import descriptions
from universe.content import diversion

from tools.system_template import ObjectTemplateLoader
from templates.space_object_template import SpaceObjectTemplate
from story.math import rotate_point, relocate_point
from text.dividers import SINGLE_DIVIDER, DIVIDER
from text.strings import MultiString as MS

TLR_HUGE_SIZE_RINGS_COUNT = 5
TLR_SMALL_SIZE_RINGS_COUNT = 4

DEFENCE_SIMPLE = 'simple'
DEFENCE_MEDIUM = 'medium'
DEFENCE_HIGH = 'high'

VISIT_SUPRISE = 16

AST_TYPES = ['om15', 'ku_tgk', 'co_cur', 'li_cal', 'tau37', 'green']


def merge_props(props: dict):
    return SINGLE_DIVIDER.join(['{} = {}'.format(key, value) for key, value in props.items()])


class Sattelite:
    ALIAS = None
    ARCHETYPE = None
    LOADOUT = None
    OFFSET = [0, 0, 0]
    ROTATE = [0, 0, 0]
    ORIENT_TOGETHER = False
    ROTATE_RANDOM = False
    VISIT = None

    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        super().__init__(*args, **kwargs)
        if not self.ALIAS:
            raise Exception(f'Related obj {self} should have alias')
        if not self.ARCHETYPE:
            raise Exception(f'Related obj {self} have not archetype')

    def get_space_content(self):
        parent_pos = self.parent.get_position()
        satt_pos = self.OFFSET.copy()
        satt_rot = (
            [randint(0, 360), randint(0, 360), randint(0, 360)]
            if self.ROTATE_RANDOM
            else self.ROTATE.copy()
        )
        if self.ORIENT_TOGETHER:
            parent_rot = self.parent.get_rotate()[1]
            satt_pos = relocate_point(satt_pos, rotate_y=-parent_rot)
            satt_rot[1] += parent_rot

        satt_pos = [
            parent_pos[0] + satt_pos[0],
            parent_pos[1] + satt_pos[1],
            parent_pos[2] + satt_pos[2]
        ]

        params = [
            '[Object]',
            f'nickname = {self.parent.get_inspace_nickname()}_related_{self.ALIAS}',
            f'pos = {satt_pos[0]:0.3f}, {satt_pos[1]:0.3f}, {satt_pos[2]:0.3f}',
            f'rotate = {satt_rot[0]:0.3f}, {satt_rot[1]:0.3f}, {satt_rot[2]:0.3f}',
            f'archetype = {self.ARCHETYPE}',
        ]
        if self.LOADOUT:
            params.append(f'loadout = {self.LOADOUT}')
        if self.VISIT:
            params.append(f'visit = {self.VISIT}')
        return SINGLE_DIVIDER.join(params)


class SupriseSattelite(Sattelite):
    VISIT = VISIT_SUPRISE


class AppearableObject(SystemObject):
    SPACE_OBJECT_TEMPLATE = None
    SPACE_OBJECT_NAME = None
    RELATED_OBJECT = None
    RELATED_OBJECT_INDEX = 0
    ARCHETYPE = None
    LOADOUT = None
    STORY = False
    SPACE_NAME = None
    TEMPLATE_ARCHETYPE = False
    TEMPLATE_ROTATE = False
    TEMPLATE_LOADOUT = False

    SATTELITES = []

    LOCKED_DOCK = False
    KEY_COLLECT_FX = None

    ARCHETYPE_TEMPLATE = '''[Object]
nickname = {nickname}
pos = {pos}
rotate = {rotate}
archetype = {archetype}'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connections = []

    def add_connection(self, the_conn):
        self.connections.append(the_conn)

    def has_appearance(self):
        return (self.ARCHETYPE or self.SPACE_OBJECT_TEMPLATE or self.TEMPLATE_ARCHETYPE) and not self.is_story()

    def is_story(self):
        return self.STORY

    def get_system_content(self):
        if self.is_story():
            return ''  # hide story content

        if self.SPACE_OBJECT_TEMPLATE is not None:
            return self.get_templated_content()
        else:
            return self.get_single_object_content()

    def get_space_object_name(self):
        if self.SPACE_OBJECT_NAME:
            return self.SPACE_OBJECT_NAME
        else:
            return self.get_inspace_nickname()

    def get_root_props(self):
        return ''

    def get_dock_props(self):
        return ''

    def get_simple_root_props(self):
        return {
            'ids_name': self.get_ids_name(),
            'ids_info': self.get_ids_info(),
        }

    def get_templated_content(self):
        position = self.get_position()
        if not position:
            raise Exception('POS is required for getting object instance when it has appaerance')

        content = self.SPACE_OBJECT_TEMPLATE().get_instance(
            root_props=self.get_root_props(),
            dock_props=self.get_dock_props(),
            new_space_object_name=self.get_space_object_name(),
            move_to=position,
        )
        sattelites = self.get_sattelites()
        if len(sattelites):
            content += DIVIDER + DIVIDER.join(sattelites)

        return content

    def get_archetype(self):
        if self.TEMPLATE_ARCHETYPE:
            return self.system.template.get_item_archetype(self.get_full_alias())
        return self.ARCHETYPE

    def get_loadout(self):
        if self.TEMPLATE_LOADOUT:
            return self.system.template.get_item_loadout(self.get_full_alias())
        return self.LOADOUT

    def get_ids_name(self):
        return 1

    def get_ids_info(self):
        return 1

    def get_single_object_content(self):
        content = [
            self.ARCHETYPE_TEMPLATE.format(
                nickname=self.get_inspace_nickname(),
                archetype=self.get_archetype(),
                pos='{}, {}, {}'.format(*self.get_position()),
                rotate='{}, {}, {}'.format(*self.get_rotate()),
            )
        ]

        if loadout := self.get_loadout():
            content.append('loadout = {}'.format(loadout))

        content.append(self.get_dock_props())

        for key, value in self.get_inspace_parameters().items():
            content.append('{} = {}'.format(key, value))

        item = SINGLE_DIVIDER.join(content)

        sattelites = self.get_sattelites() + self.get_root_sattelites()

        return DIVIDER.join([item] + sattelites)

    def get_sattelites(self):
        return []

    def get_root_sattelites(self):
        sattelites = []
        for satt in self.SATTELITES:
            sattelites.append(
                satt(parent=self).get_space_content()
            )
        return sattelites

    def get_inspace_nickname(self):
        print(self.__class__.__name__)
        raise NotImplementedError

    def get_inspace_parameters(self):
        return {}

    def get_extra_params(self):
        return {}


class StaticObject(AppearableObject):
    ASTEROID_ZONES = []
    AST_EXCLUSION_ZONE_SIZE = 3000
    AST_ZONE_NAME_TEMPLATE = 'Zone_{space_name}_ast_{zone_code}_exclusion'
    AST_EXCLUSION_ZONE_PARAMS = {}

    NEBULA_ZONES = []
    NEBULA_EXCLUSION_ZONE_SIZE = 3000
    NEBULA_ZONE_NAME_TEMPLATE = 'Zone_{space_name}_nebula_exclusion'
    EXCLUSION_PARAMS = {}
    NEBULA_EXCLUSION_EDGE_FRACTION = 0.2
    NEBULA_EXCLUSION_ZONE_PARAMS = {}

    RING_ZONE_NAME_TEMPLATE = 'Zone_{space_name}_ring'
    RING_FILE_TEMPLATE = 'solar\\rings\\{ring_file_name}.ini'
    RING = False
    RING_ZONE_ALIAS = None
    RING_ZONE_INDEX = None
    RING_FILE_NAME = None

    DEFENCE_ZONE_SIZE = 5000
    DEFENCE_LEVEL = None
    DEFENCE_ZONE_BACKDRIFT = 0
    DEFENCE_ZONE_NAME_TEMPLATE = 'Zone_{space_name}_pop_defence'

    LLIGHT_CLOUD_ZONE_NAME_TEMPLATE = 'Zone_{space_name}_llight_cloud'
    LLIGHT_CLOUD = False
    LLIGHT_CLOUD_NAME = None
    LLIGHT_CLOUD_FILE_TEMPLATE = 'solar\\nebula_mod\\{llight_cloud_name}.ini'
    LLIGHT_CLOUD_RANGE = 600000

    USE_LIFTER = False

    FORCE_CONNECTIONS = []

    def get_base(self):
        return None

    def get_force_connections(self):
        return self.FORCE_CONNECTIONS

    def get_ast_exclusion_zone_name(self, ast_zone):
        return self.AST_ZONE_NAME_TEMPLATE.format(
            zone_code=ast_zone.get_zone_alias(),
            space_name=self.get_inspace_nickname(),
        )
    
    def get_nebula_exclusion_zone_name(self):
        return self.NEBULA_ZONE_NAME_TEMPLATE.format(
            space_name=self.get_inspace_nickname(),
        )
    
    def get_ring_zone_name(self):
        return self.RING_ZONE_NAME_TEMPLATE.format(
            space_name=self.get_inspace_nickname(),
        )
    
    def get_defence_zone_name(self):
        return self.DEFENCE_ZONE_NAME_TEMPLATE.format(
            space_name=self.get_inspace_nickname(),
        )

    def get_llight_cloud_zone_name(self):
        return self.LLIGHT_CLOUD_ZONE_NAME_TEMPLATE.format(
            space_name=self.get_inspace_nickname(),
        )

    def get_defence_zone_position(self):
        pos_x, pos_y, pos_z = self.get_position()
        if self.REL == LEFT:
            pos_x += self.DEFENCE_ZONE_BACKDRIFT
        if self.REL == RIGHT:
            pos_x -= self.DEFENCE_ZONE_BACKDRIFT
        if self.REL == TOP:
            pos_z += self.DEFENCE_ZONE_BACKDRIFT
        if self.REL == BOTTOM:
            pos_z -= self.DEFENCE_ZONE_BACKDRIFT
        return (pos_x, pos_y, pos_z)

    def has_lifter(self):
        return self.USE_LIFTER

    def get_lawful_defence_zone_params(self):
        population_class = self.get_lawful_population_class()
        if self.DEFENCE_LEVEL == DEFENCE_SIMPLE:
            return population_class.get_simple_defence_params()
        elif self.DEFENCE_LEVEL == DEFENCE_MEDIUM:
            return population_class.get_medium_defence_params(use_lifter=self.has_lifter())
        elif self.DEFENCE_LEVEL == DEFENCE_HIGH:
            return population_class.get_high_defence_params(use_lifter=self.has_lifter())

        raise Exception('Unknown defence class for object %s' % self.__class__.__name__)

    def get_unlawful_defence_zone_params(self):
        population_class = self.get_unlawful_population_class()
        return population_class.get_pirate_defence_params(self.get_faction())

    def get_defence_zone(self):
        return DynamicSphereZone(
            system=self.system,
            space_nickname=self.get_defence_zone_name(),
            alias=self.ALIAS,
            index=self.INDEX,
            position=self.get_defence_zone_position(),
            size=self.DEFENCE_ZONE_SIZE,
            merged_params=(
                self.get_lawful_defence_zone_params()
                if self.is_lawful() else
                self.get_unlawful_defence_zone_params()
            )
        )

    def get_dynamic_zones(self):
        zones = []
        for ast_zone in self.ASTEROID_ZONES:
            zones.append(
                DynamicSphereZone(
                    system=self.system,
                    space_nickname=self.get_ast_exclusion_zone_name(ast_zone),
                    alias=self.ALIAS,
                    index=self.INDEX,
                    size=(ast_zone.ASTEROID_DEFINITION_CLASS.EXCLUSION_SIZE_OVERRIDE
                          if ast_zone.ASTEROID_DEFINITION_CLASS.EXCLUSION_SIZE_OVERRIDE > 0 else
                            self.AST_EXCLUSION_ZONE_SIZE),
                    **self.AST_EXCLUSION_ZONE_PARAMS,
                )
            )
        if len(self.NEBULA_ZONES) != 0:
            zones.append(
                DynamicSphereZone(
                    system=self.system,
                    space_nickname=self.get_nebula_exclusion_zone_name(),
                    alias=self.ALIAS,
                    index=self.INDEX,
                    size=self.NEBULA_EXCLUSION_ZONE_SIZE,
                    edge_fraction=self.NEBULA_EXCLUSION_EDGE_FRACTION,
                    **self.NEBULA_EXCLUSION_ZONE_PARAMS,
                )
            )
        if self.RING:
            if not self.RING_ZONE_ALIAS and not self.RING_ZONE_INDEX:
                raise Exception('ring for object %s have not enough data' % self.__class__.__name__)
            zones.append(
                DynamicZone(
                    system=self.system,
                    space_nickname=self.get_ring_zone_name(),
                    alias=self.RING_ZONE_ALIAS,
                    index=self.RING_ZONE_INDEX,
                )
            )
        if self.LLIGHT_CLOUD:
            zones.append(
                RawZone(
                    system=self.system,
                    zone_params={
                        'nickname': self.get_llight_cloud_zone_name(),
                        'size': '{}, {}, {}'.format(self.LLIGHT_CLOUD_RANGE, 0, self.LLIGHT_CLOUD_RANGE),
                        'position': '{}, {}, {}'.format(0, 0, 0),
                        'shape': 'RING',
                    }
                )
            )

        if self.DEFENCE_LEVEL and self.system.have_population() and not self.STORY:
            zones.append(
                self.get_defence_zone(),
            )
        return zones

    def get_inspace_parameters(self):
        params = super().get_inspace_parameters()
        if self.RING:
            if not self.RING_FILE_NAME:
                raise Exception('unknown file for ring %s' % self.__class__.__name__)

            params['ring'] = '{zone}, {ring_file}'.format(
                zone=self.get_ring_zone_name(),
                ring_file=self.RING_FILE_TEMPLATE.format(ring_file_name=self.RING_FILE_NAME),
            )
        elif self.LLIGHT_CLOUD:
            if not self.LLIGHT_CLOUD_NAME:
                raise Exception('unknown file for llight cloud ring %s' % self.__class__.__name__)

            params['ring'] = '{zone}, {llight_cloud}'.format(
                zone=self.get_llight_cloud_zone_name(),
                llight_cloud=self.LLIGHT_CLOUD_FILE_TEMPLATE.format(llight_cloud_name=self.LLIGHT_CLOUD_NAME),
            )


        return params

    def is_lawful(self):
        is_lawful = self.get_faction() in self.system.get_lawful_factions()
        if not is_lawful and self.get_faction() not in self.system.get_unlawful_factions():
            raise Exception('Faction %s isnt defined in system for object %s' % (self.get_faction(), self.__class__.__name__))
        return is_lawful


class AutoStaticObject(StaticObject):
    ALIAS = 'static'
    TEMPLATE_ARCHETYPE = True
    TEMPLATE_LOADOUT = True  # Enable when you want it

    def get_inspace_nickname(self):
        return '{system_name}_staticobj_{index}'.format(system_name=self.system.NAME, index=self.INDEX)


class NamedObject(StaticObject):
    LAZY_NAME = False

    RU_NAME = None
    RU_FIRST_DESCRIPTION = None
    RU_SECOND_DESCRIPTION = None
    DOUBLE_INFO = False
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.LAZY_NAME:
            self.set_space_name()

        self.ids_info1 = self.system.ids.new_name(
            self.get_first_description()
        )
        if self.have_double_info():
            self.ids_info2 = self.system.ids.new_name(
                self.get_second_description()
            )

    def have_double_info(self):
        return self.DOUBLE_INFO is not None

    def get_first_description(self):
        if self.RU_FIRST_DESCRIPTION:
            return MS(
                "\\n" + self.RU_FIRST_DESCRIPTION.get_ru(),
                "\\n" + self.RU_FIRST_DESCRIPTION.get_en()
            )
        return MS(' ', ' ')  # empty

    def get_second_description(self):
        return MS(' ', ' ')  # empty

    def set_space_name(self):
        space_name = self.get_space_name()

        if not space_name:
            raise Exception(f'System object {self} have no name')

        self.ids_name = self.system.ids.new_name(space_name)

    def get_name(self):
        return self.RU_NAME

    def get_space_name(self):
        return self.get_name()

    def get_base_string_id(self):
        return self.get_ids_name()

    def get_ids_name(self):
        return self.ids_name.id

    def get_tradelane_ids_name(self):
        return self.get_ids_name()

    def get_ids_info(self):
        return self.ids_info1.id

    def get_ids_info1(self):
        return self.ids_info1.id

    def get_ids_info2(self):
        if not self.have_double_info():
            raise Exception(f'{self} is not double info object')
        return self.ids_info2.id

    def get_infocard_map(self):
        return f'Map = {self.get_ids_info1()}, {self.get_ids_info2() if self.have_double_info() else "1"}'


class VirtualDepot(NamedObject):
    ALIAS = 'virtual'

    def get_system_content(self):
        return ''

    def get_inspace_nickname(self):
        return '{system_name}_virtual_{index}'.format(system_name=self.system.NAME, index=self.INDEX)


class RawText(SystemObject):
    SPACE_CONTENT = ''

    def get_system_content(self):
        return self.SPACE_CONTENT


class JumpableObject(NamedObject):
    TARGET_SYSTEM_NAME = None
    CONNECTION_KIND = connection.CONNECTION_LAWFUL
    FORCE_INSPACE_NAME = None
    FORCE_TARGET_NAME = None
    LAZY_NAME = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_system = None

        if self.TARGET_SYSTEM_NAME is None:
            raise Exception('Jumpgate %s have no target system' % self.__class__.__name__)

    def init_connection(self):
        self.target_system = self.system.get_universe_root().get_system_by_name(self.TARGET_SYSTEM_NAME)
        self.set_space_name()

    def get_target_system(self):
        if not self.target_system:
            raise Exception('Jumpgate %s have no initiated connection with system' % self.__class__.__name__)

        return self.target_system

    def get_jump_effect(self):
        raise Exception('unknown jump effect')

    def get_inspace_nickname(self):
        if self.FORCE_INSPACE_NAME:
            return self.FORCE_INSPACE_NAME

        return '{system_name}_{alias}_to_{target_system_name}'.format(
            alias=self.ALIAS,
            system_name=self.system.NAME,
            target_system_name=self.TARGET_SYSTEM_NAME,
        )

    def get_target_jump_object_nickname(self):
        if self.FORCE_TARGET_NAME:
            return self.FORCE_TARGET_NAME

        return '{target_system_name}_{alias}_to_{system_name}'.format(
            alias=self.ALIAS,
            system_name=self.system.NAME,
            target_system_name=self.TARGET_SYSTEM_NAME,  # Should not be initialized
        )

    def get_goto(self):
        return '{target_system_nickname}, {target_jumpgate_name}, {gate_tunnel}'.format(
            target_system_nickname=self.get_target_system().NAME,  # Should be initialized
            target_jumpgate_name=self.get_target_jump_object_nickname(),
            gate_tunnel=self.system.JUMP_EFFECT.GATE_TUNNEL
        )

    def get_target_jumpgate(self):
        # Should be initialized
        return self.get_target_system().get_jumpgate_instance(self.system.NAME)

    def get_msg_id_prefix(self):
        return self.get_target_system().get_system_msg()

    def get_inspace_parameters(self):
        params = super().get_inspace_parameters()
        params.update({
            'ids_name': self.get_ids_name(),
            'ids_info': self.get_ids_info(),
            'jump_effect': self.get_jump_effect(),
            'reputation': self.get_faction().get_code(),
            'goto': self.get_goto(),
            'msg_id_prefix': self.get_msg_id_prefix(),
        })
        return params

    def get_name(self):
        return MS(
            f'{self.system.get_ru_name()} > {self.get_target_system().get_ru_name()}',
            f'{self.system.get_en_name()} > {self.get_target_system().get_en_name()}'
        )


class Jumpgate(JumpableObject):
    ALIAS = 'jg'
    REL_DRIFT = 500
    REL_APPEND = 2000

    IDS_INFO = 65551
    ARCHETYPE = 'jumpgate'

    LOADOUT = 'jumpgate_rh'

    Y_ROTATE_PER_REL = {
        LEFT: -90,
        RIGHT: 90,
        TOP: 180,
        BOTTOM: 0,
    }
    ROTATE_BY_TEMPLATE = False

    DEFENCE_ZONE_SIZE = 4000
    DEFENCE_LEVEL = DEFENCE_SIMPLE

    CONNECTION_KIND = connection.CONNECTION_LAWFUL

    def get_y_rotate(self):
        return (
            self.system.template.get_item_rotate(self.get_full_alias())[1]
            if self.ROTATE_BY_TEMPLATE
            else self.Y_ROTATE_PER_REL[self.REL]
        )

    def get_rotate(self):
        return 0, self.get_y_rotate(), 0

    def get_jump_effect(self):
        return self.system.JUMP_EFFECT.JUMP_EFFECT

    def get_ids_info(self):
        return self.IDS_INFO


class Jumphole(JumpableObject):
    ALIAS = 'jh'
    REL_DRIFT = 500
    REL_APPEND = 2000

    IDS_NAME = 196718
    IDS_INFO = 65551
    ARCHETYPE = 'jumphole'
    LOADOUT = 'hole_effect_edge'

    DEFENCE_LEVEL = None

    CONNECTION_KIND = connection.CONNECTION_UNLAWFUL

    def get_jump_effect(self):
        return self.system.JUMP_EFFECT.HOLE_EFFECT

    def get_ids_info(self):
        return self.IDS_INFO


class JumpgateAlt(Jumpgate):
    LOADOUT = 'jumpgate_special'

    def get_jump_effect(self):
        return self.system.JUMP_EFFECT.JUMP_EFFECT_ALT


class GenericSphere(StaticObject):
    SPHERE_RADIUS = None

    DRAG_ZONE_NAME_TEMPLATE = 'Zone_{parent}_drag'
    DEATH_ZONE_NAME_TEMPLATE = 'Zone_{parent}_death'

    ATMOSPHERE_SPACEDUST = None
    ATMOSPHERE_SPACEDUST_MAXPARTICLES = None

    DRAG_ZONE_INTERFERENCE = 0.001
    DAMAGE_ZONE_DAMAGE = 200000000
    DAMAGE_ZONE_SORT = 99.5

    DRAG_MODIFIER = 1

    def get_sphere_radius(self):
        if not self.SPHERE_RADIUS:
            raise Exception('sphere radius isnt defined %s' % self.__class__.__name__)
        return self.SPHERE_RADIUS

    def get_atmosphere_range(self):
        raise NotImplementedError

    def get_drag_zone_size(self):
        raise NotImplementedError

    def get_death_zone_size(self):
        raise NotImplementedError

    def get_zones_force_position(self):
        return None
    
    def get_sphere_damage_zones(self):
        parent_name = self.get_inspace_nickname()
        drag_zone = DynamicSphereZone(
            system=self.system,
            space_nickname=self.DRAG_ZONE_NAME_TEMPLATE.format(parent=parent_name),
            position=self.get_zones_force_position(),
            alias=self.ALIAS,
            index=self.INDEX,
            size=self.get_drag_zone_size(),
            interference=self.DRAG_ZONE_INTERFERENCE,
            drag_modifier=self.DRAG_MODIFIER,
            spacedust=self.ATMOSPHERE_SPACEDUST,
            spacedust_maxparticles=self.ATMOSPHERE_SPACEDUST_MAXPARTICLES,
            sort=self.DAMAGE_ZONE_SORT,
        )
        damage_zone = DynamicSphereZone(
            system=self.system,
            space_nickname=self.DEATH_ZONE_NAME_TEMPLATE.format(parent=parent_name),
            position=self.get_zones_force_position(),
            alias=self.ALIAS,
            index=self.INDEX,
            size=self.get_death_zone_size(),
            damage=self.DAMAGE_ZONE_DAMAGE,
        )
        return [drag_zone, damage_zone]
    
    def get_dynamic_zones(self):
        dynamic_zones = super().get_dynamic_zones()
        return dynamic_zones + self.get_sphere_damage_zones()


class Sun(GenericSphere):
    ALIAS = 'sun'

    ARCHETYPE = 'sun_2000'

    IDS_NAME = 253954
    IDS_INFO = 65541

    LOADOUT = None
    STAR = None
    ATMOSHPERE_RANGE = 11000
    DEATH_ZONE_SIZE = 7000
    DEATH_ZONE_DAMAGE = 200000000
    DRAG_ZONE_SIZE = 10500
    DRAG_MODIFIER = 5

    def get_atmosphere_range(self):
        return self.ATMOSHPERE_RANGE

    def get_drag_zone_size(self):
        return self.DRAG_ZONE_SIZE

    def get_death_zone_size(self):
        return self.DEATH_ZONE_SIZE

    def get_inspace_parameters(self):
        params = super().get_inspace_parameters()
        params.update({
            'star': self.STAR,
            'atmosphere_range': self.get_atmosphere_range(),
        })
        return params

    def get_inspace_nickname(self):
        return '{system_name}_sun_{index}'.format(system_name=self.system.NAME, index=self.INDEX)


class SunSmall(Sun):
    ARCHETYPE = 'sun_1000'

    ATMOSHPERE_RANGE = 5000
    DEATH_ZONE_SIZE = 4000
    DEATH_ZONE_DAMAGE = 200000000
    DRAG_ZONE_SIZE = 6000
    DRAG_MODIFIER = 4


class Planet(GenericSphere, NamedObject):
    ALIAS = 'planet'

    PLANET_RADIUSES = (1500, 2000, 2500, 3000, 4000, 5000)
    PLANET_CIRCLE_ARCHETYPE_TEMPLATE = 'planet_{radius}_circle'
    PLANET_CIRCLE_TEMPLATE = '''[Object]
nickname = {parent_planet}_planet_circle
pos = {position}
rotate = {rotate}
archetype = {circle_archetype}
{planet_spin}
parent = {parent_planet}'''

    PLANET_CIRCLE = True
    PLANET_CIRCLE_DEFAULT_ROTATE = (0, 30, 0)
    ATMOSPHERE_RANGE_APPEND = 350
    ATMOSPHERE_SPACEDUST = Dust.ATMOSPHERE
    ATMOSPHERE_SPACEDUST_MAXPARTICLES = 500
    DOCK_RING_OFFSET = 300
    DEATH_ZONE_APPEND = 150
    DRAG_ZONE_APPEND = 300
    PLANET_CIRCLE_Y_DRIFT = 10
    SPIN = 0.02
    DRAG_MODIFIER = 3

    RELATED_DOCK_RING = None
    DOUBLE_INFO = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if related_dock_ring := self.get_related_ring_obj():
            related_dock_ring.set_related_planet(self)

    def get_spin(self):
        if self.SPIN > 0:
            return f'0, {self.SPIN}, 0'
        return None

    def get_planet_circle(self):
        if not self.PLANET_CIRCLE:
            return

        if self.get_sphere_radius() not in self.PLANET_RADIUSES:
            raise Exception('planet %s have invalid radius' % self.__class__.__name__)

        pos_x, pos_y, pos_z = self.get_position()
        spin = ''
        spin_data = self.get_spin()
        if spin_data:
            spin = f'spin = {spin_data}'

        rotate = self.get_rotate()
        if sum(rotate) == 0:
            rotate = self.PLANET_CIRCLE_DEFAULT_ROTATE

        return self.PLANET_CIRCLE_TEMPLATE.format(
            parent_planet=self.get_inspace_nickname(),
            position='{}, {}, {}'.format(pos_x, pos_y+self.PLANET_CIRCLE_Y_DRIFT, pos_z),
            rotate='{}, {}, {}'.format(*rotate),
            circle_archetype=self.PLANET_CIRCLE_ARCHETYPE_TEMPLATE.format(radius=self.get_sphere_radius()),
            planet_spin=spin,
        )

    def get_sattelites(self):
        sattelites = []
        circle = self.get_planet_circle()
        if circle:
            sattelites.append(circle)
        return sattelites

    def get_inspace_nickname(self):
        return '{system_name}_planet_{index}'.format(system_name=self.system.NAME, index=self.INDEX)

    def get_related_ring_obj(self):
        if self.RELATED_DOCK_RING:
            return self.system.get_static_by_class(self.RELATED_DOCK_RING)

    def get_inspace_parameters(self):
        params = super().get_inspace_parameters()
        params['atmosphere_range'] = self.get_atmosphere_range()
        spin_data = self.get_spin()
        if spin_data:
            params['spin'] = spin_data

        params.update(self.get_simple_root_props())

        if related_dock_ring := self.get_related_ring_obj():
            params.update(related_dock_ring.get_raw_base_props())

        return params

    def get_atmosphere_range(self):
        return self.get_sphere_radius() + self.ATMOSPHERE_RANGE_APPEND

    def get_drag_zone_size(self):
        return self.get_sphere_radius() + self.DRAG_ZONE_APPEND

    def get_death_zone_size(self):
        return self.get_sphere_radius() + self.DEATH_ZONE_APPEND

    def get_position_for_dock_ring(self):
        pos_x, pos_y, pos_z = self.system.template.get_item_pos(self.RELATED_DOCK_RING.get_full_alias())
        planet_drift = self.SPHERE_RADIUS + self.DOCK_RING_OFFSET
        if self.RELATED_DOCK_RING.REL == LEFT:
            pos_x -= planet_drift 
        elif self.RELATED_DOCK_RING.REL == RIGHT:
            pos_x += planet_drift 
        elif self.RELATED_DOCK_RING.REL == TOP:
            pos_z -= planet_drift
        elif self.RELATED_DOCK_RING.REL == BOTTOM:
            pos_z += planet_drift

        return (pos_x, pos_y, pos_z)

    def get_zones_force_position(self):
        if self.RELATED_DOCK_RING is not None:
            return self.get_position_for_dock_ring()

    def get_position(self):
        if self.RELATED_DOCK_RING is not None:
            return self.get_position_for_dock_ring()
        else:
            return super().get_position()

    def get_space_name(self):
        if related_dock_ring := self.get_related_ring_obj():
            return related_dock_ring.get_name()

        return self.get_name()


class NotDockableObject(StaticObject):
    DEFENCE_LEVEL = None

    def get_root_props(self):
        return merge_props(self.get_simple_root_props())

    def get_inspace_nickname(self):
        return '{system_name}_{alias}_{index}'.format(
            system_name=self.system.NAME,
            alias=self.ALIAS,
            index=self.INDEX
        )


class StationRuins(NotDockableObject, NamedObject):
    RU_FIRST_DESCRIPTION = descriptions.STATION_RUINS


class DockableObject(NamedObject):
    ARCHETYPE = 'depot'
    DOUBLE_INFO = True
    INTERIOR_CLASS = interior.CustomFileInterior  # custom interior
    INTERIOR_EXTRA_ROOMS = []
    INTERIORS_FOLDER = 'GENERATED_INTERIORS'
    DEALERS = None
    IS_BASE = True
    EQUIP_SET = None
    SHIP_SET = None
    BASE_INDEX = None
    WEAPON_FACTION = None
    MISC_EQUIP_TYPE = None
    EQUIP_FACTION = None
    MISC_EQUIP_GEN_TYPE = None
    BASE_PROPS = None
    SELL_AMMO = True
    DOCK_ONLY = False
    MSG_PREFIX = None

    AUTOSAVE_FORBIDDEN = False

    INTERIOR_BG1 = None
    INTERIOR_BG2 = None
    BG1_KEY = 'terrain_tiny'
    BG2_KEY = 'terrain_sml'

    CALC_STORE = True
    HAVE_CHARACTERS = True

    ROOM_SUBFOLDER = None

    INTERIOR_DEFINITION_TEMPLATE = '''[Base]
nickname = {base_name}
system = {system_name}
strid_name = {ids_name}
file = {file_location}.ini
BGCS_base_run_by = W02bF44'''

    INTERIOR_LOCATION_GENERATED_TEMPLATE = 'Universe\\{interiors_folder}\\{interior_file_name}'
    INTERIOR_LOCATION_CUSTOM_TEMPLATE = 'Universe\\{system_root}\\{system_folder}\\{interior_file_name}'

    AUDIO_PREFIX = None
    SPACE_VOICE = None
    SPACE_COSTUME = None
    RANDOM_ROBOT = False
    ALLOW_SPACE_COSTUME = True

    DEFENCE_LEVEL = DEFENCE_MEDIUM

    TRADE_DEPOT_ARCHETYPES = []
    TRADE_POINT_ARCHETYPE: diversion.TradingFixture = diversion.TradingFixture

    TRADE_POINTS_OFFSETS = []
    TRADE_POINT_Y = -500
    TRADE_POINT_Z = 1000
    TRADE_POINT_ORIENTS = []
    TRADE_POINT_EMPTY_ARCHETYPE = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.BASE_INDEX:
            raise Exception('Dockable base have no base index %s' % self.__class__.__name__)

        self.base = None

        self.interior = None
        if self.INTERIOR_CLASS:
            subfolder = self.ROOM_SUBFOLDER if self.ROOM_SUBFOLDER else self.system.ROOM_SUBFOLDER
            self.interior = self.INTERIOR_CLASS(self, subfolder)

        self.key = None
        if self.LOCKED_DOCK:
            if not self.KEY_COLLECT_FX:
                raise Exception('Dockable locked base have no fx for key %s' % self.__class__.__name__)
            self.key = LockedDockKey(self, key_fx=self.KEY_COLLECT_FX, key_name=self.get_key_loot_name())

    def get_key_loot_name(self):
        return MS(
            f'Ключ для {self.get_name().get_ru()}',
            f'Key for {self.get_name().get_en()}'
        )

    def get_weapon_faction(self):
        return self.WEAPON_FACTION

    def get_equip_type(self):
        if self.MISC_EQUIP_TYPE:
            return self.MISC_EQUIP_TYPE
        elif self.MISC_EQUIP_GEN_TYPE:
            if not self.EQUIP_FACTION:
                raise Exception(f'base {self.get_base_nickname()} have no equip set')

            return TYPE_PER_GEN_TYPE[self.EQUIP_FACTION][self.MISC_EQUIP_GEN_TYPE]

        raise Exception(f'base {self.get_base_nickname()} have no any equip type')

    def set_base(self, base):
        self.base = base

    def get_base(self):
        return self.base

    def get_refer_msg(self):
        return self.MSG_PREFIX if self.MSG_PREFIX else self.get_base_nickname()

    def get_audio_prefix(self):
        return self.AUDIO_PREFIX if self.AUDIO_PREFIX else self.get_base_msg()

    def get_base_msg(self):
        return f'gcs_refer_base_{self.get_refer_msg()}'

    def get_base_msg_relative(self):
        return f'gcs_refer_base_{self.get_refer_msg()}-'

    def get_ru_name(self):
        return self.RU_NAME

    def get_key_name(self):
        if not self.key:
            raise Exception('this base could not be locked')

        return self.key.get_equip_name()

    def get_inspace_nickname(self):
        return '{system_name}_{base_index:02d}'.format(system_name=self.system.NAME, base_index=self.BASE_INDEX)

    def get_base_nickname(self):
        return '{system_name}_{base_index:02d}_base'.format(system_name=self.system.NAME, base_index=self.BASE_INDEX)

    def get_interior_file_name(self):
        return 'gen_{base_nickname}'.format(base_nickname=self.get_base_nickname())

    def get_interior_content(self):
        if not self.interior:
            raise Exception('Impossible to load interior for dockable base %s' % self.__class__.__name__)

        return self.interior.get_base_info()

    def get_interior_definition(self):
        file_location = (
            self.INTERIOR_LOCATION_CUSTOM_TEMPLATE.format(
                system_root=self.system.SYSTEMS_ROOT,
                system_folder=self.system.SYSTEM_FOLDER,
                interior_file_name=self.get_base_nickname(),
            )
            if self.interior.CUSTOM_INTERIOR_FILE else
            self.INTERIOR_LOCATION_GENERATED_TEMPLATE.format(
                interiors_folder=self.INTERIORS_FOLDER,
                interior_file_name=self.get_interior_file_name(),
            )
        )

        definition = [
            self.INTERIOR_DEFINITION_TEMPLATE.format(
                base_name=self.get_base_nickname(),
                system_name=self.system.NAME,
                ids_name=self.get_base_string_id(),
                file_location=file_location,
            )
        ]
        if self.INTERIOR_BG1:
            definition.append('{} = {}'.format(self.BG1_KEY, self.INTERIOR_BG1))
        if self.INTERIOR_BG2:
            definition.append('{} = {}'.format(self.BG2_KEY, self.INTERIOR_BG2))
        if self.AUTOSAVE_FORBIDDEN is True:
            definition.append('autosave_forbidden = true')

        return SINGLE_DIVIDER.join(definition)

    def get_mbases_content(self):
        if not self.interior:
            raise Exception('%s have not interior' % self.__class__.__name__)
        return self.interior.get_mbase()

    def get_raw_root_props(self):
        base_name = self.get_base_nickname()
        return {
            'ids_name': self.get_ids_name(),
            'ids_info': self.get_ids_info(),
            'base': base_name,
            'reputation': self.get_faction().get_code(),
            'behavior': 'NOTHING',
        }

    def get_raw_base_props(self):
        base_name = self.get_base_nickname()
        return {
            'base': base_name,
            'reputation': self.get_faction().get_code(),
            'behavior': 'NOTHING',
        }

    def get_root_props(self):
        return merge_props(self.get_raw_root_props())

    def get_dock_props(self):
        base_name = self.get_base_nickname()
        props = {
            'ids_name': self.get_ids_name(),
            'ids_info': self.get_ids_info(),
            'dock_with': base_name,
            'reputation': self.get_faction().get_code(),
            'behavior': 'NOTHING',
        }
        if not self.DOCK_ONLY:
            props['base'] = base_name

        if self.ALLOW_SPACE_COSTUME:
            if self.RANDOM_ROBOT and not self.SPACE_VOICE and not self.SPACE_COSTUME:
                props['voice'] = SpaceVoice.VOICE_ROBOT_RU if self.system.core.russian else SpaceVoice.VOICE_ROBOT_EN
                props['space_costume'] = SpaceCostume.random_robot()
            else:
                if self.system.core.russian:
                    props['voice'] = self.SPACE_VOICE if self.SPACE_VOICE else SpaceVoice.DEFAULT_RU
                else:
                    props['voice'] = self.SPACE_VOICE if self.SPACE_VOICE else SpaceVoice.DEFAULT_EN
                props['space_costume'] = self.SPACE_COSTUME if self.SPACE_COSTUME else SpaceCostume.DEFAULT

        return SINGLE_DIVIDER.join(['{} = {}'.format(key, value) for key, value in props.items()])

    def have_bar(self):
        return self.interior.have_bar()

    def have_equip_dealer(self):
        if not self.interior.have_equip():
            return False

        if not self.EQUIP_SET:
            raise Exception('Base %s have no equip set for equip dealer' % self.__class__.__name__)

        return True

    def have_trader(self):
        if not self.interior.have_trader():
            return False

        if not self.BASE_PROPS:
            raise Exception('Base %s have no defined economics base props' % self.__class__.__name__)

        return True

    def have_shipdealer(self):
        if not self.interior.have_shipdealer():
            return False

        if not self.SHIP_SET:
            raise Exception('Base %s have no ship set for ship dealer' % self.__class__.__name__)

        return True

    def get_main_rotate(self):
        raise NotImplementedError

    def get_trade_points_front(self):
        space_objects = []
        root_name = self.get_space_object_name()
        root_pos = self.get_position()
        main_rotate = self.get_main_rotate()

        i = 1
        for fixture_offset in self.TRADE_POINTS_OFFSETS:
            if main_rotate != 0:
                fixture_offset = relocate_point(fixture_offset, rotate_y=main_rotate)

            fixture_pos = [
                root_pos[0] + fixture_offset[0],
                root_pos[1] + fixture_offset[1],
                root_pos[2] + fixture_offset[2],
            ]

            space_objects.append(f'''[Object]
nickname = {root_name}_tr_point{i}
pos = {fixture_pos[0]:0.7f}, {fixture_pos[1]:0.7f}, {fixture_pos[2]:0.7f} 
rotate = 0, {main_rotate}, 0
archetype = {self.TRADE_POINT_ARCHETYPE.ARCHETYPE}
behavior = NOTHING
reputation = {self.get_faction_code()}
dock_with = {self.get_base_nickname()}
''')

            empty_point_index = random.randint(1, len(self.TRADE_POINT_ARCHETYPE.TRANSPORT_POINTS))

            j = 1
            for fixture_point in self.TRADE_POINT_ARCHETYPE.TRANSPORT_POINTS:
                depot_archetype: diversion.TradingTrain = (
                    self.TRADE_POINT_EMPTY_ARCHETYPE
                    if j == empty_point_index else
                    random.choice(self.TRADE_DEPOT_ARCHETYPES)
                )

                if depot_archetype is not None:

                    point_init_pos = [
                        fixture_point,
                        0,
                        depot_archetype.FRONT_OFFSET
                    ]
                    if main_rotate != 0:
                        point_init_pos = relocate_point(point_init_pos, rotate_y=-main_rotate)

                    point_pos = [
                        point_init_pos[0] + fixture_pos[0],
                        point_init_pos[1] + fixture_pos[1],
                        point_init_pos[2] + fixture_pos[2],
                    ]

                    space_objects.append(f'''[Object]
nickname = {root_name}_tr_point{i}_moor_obj{j}
pos = {point_pos[0]:0.7f}, {point_pos[1]:0.7f}, {point_pos[2]:0.7f} 
rotate = 0, {main_rotate}, 0
archetype = {depot_archetype.ARCHETYPE}
loadout = {depot_archetype.LOADOUT}
reputation = {self.get_faction_code()}
ids_name = 261161
behavior = NOTHING
''')
                j += 1

            i += 1

        return space_objects

    def get_trade_points_orient(self):
        space_objects = []
        root_name = self.get_space_object_name()
        root_pos = self.get_position()

        i = 1
        for fixture_orient in self.TRADE_POINT_ORIENTS:
            fixture_offset = [
                0, self.TRADE_POINT_Y, self.TRADE_POINT_Z
            ]
            fixture_offset = relocate_point(fixture_offset, rotate_y=fixture_orient)

            fixture_pos = [
                root_pos[0] + fixture_offset[0],
                root_pos[1] + fixture_offset[1],
                root_pos[2] + fixture_offset[2],
            ]

            space_objects.append(f'''[Object]
nickname = {root_name}_tr_point{i}
pos = {fixture_pos[0]:0.2f}, {fixture_pos[1]:0.2f}, {fixture_pos[2]:0.2f} 
rotate = 0, {-fixture_orient}, 0
archetype = {self.TRADE_POINT_ARCHETYPE.ARCHETYPE}
behavior = NOTHING
reputation = {self.get_faction_code()}
dock_with = {self.get_base_nickname()}
''')

            empty_point_index = random.randint(1, len(self.TRADE_POINT_ARCHETYPE.TRANSPORT_POINTS))

            j = 1
            for fixture_point in self.TRADE_POINT_ARCHETYPE.TRANSPORT_POINTS:
                depot_archetype: diversion.TradingTrain = (
                    self.TRADE_POINT_EMPTY_ARCHETYPE
                    if j == empty_point_index else
                    random.choice(self.TRADE_DEPOT_ARCHETYPES)
                )

                if depot_archetype is not None:

                    point_init_pos = [
                        fixture_point,
                        0,
                        depot_archetype.FRONT_OFFSET
                    ]
                    point_init_pos = relocate_point(point_init_pos, rotate_y=fixture_orient)

                    point_pos = [
                        point_init_pos[0] + fixture_pos[0],
                        point_init_pos[1] + fixture_pos[1],
                        point_init_pos[2] + fixture_pos[2],
                    ]

                    space_objects.append(f'''[Object]
nickname = {root_name}_tr_point{i}_moor_obj{j}
pos = {point_pos[0]:0.7f}, {point_pos[1]:0.7f}, {point_pos[2]:0.7f}
rotate = 0, {-fixture_orient}, 0
archetype = {depot_archetype.ARCHETYPE}
loadout = {depot_archetype.LOADOUT}
reputation = {self.get_faction_code()}
ids_name = 261161
behavior = NOTHING
''')
                j += 1

            i += 1

        return space_objects


class Dockring(DockableObject):
    ALIAS = 'dockring'
    ARCHETYPE = 'dock_ring'
    REL_DRIFT = 1000
    REL_APPEND = 3000
    DOCK_ONLY = True
    DOUBLE_INFO = True

    DOCKING_FIXTURE_TEMPLATE = '''[Object]
nickname = {parent_object}_docking_fixture_1
ids_name = 253953
pos = {pos}
rotate = {rotate}
archetype = docking_fixture
ids_info = 065540
dock_with = {parent_base}
reputation = {reputation}
behavior = NOTHING
'''

    INTERIOR_CLASS = None  # should be overrided

    AUDIO_PREFIX = None  # should be overrided

    Y_ROTATE_PER_REL = {
        LEFT: 90,
        RIGHT: -90,
        TOP: 0,
        BOTTOM: 180,
    }

    FIXTURE_POSITION_APPEND = (0, 350, 0)
    HAVE_FIXTURE = True

    DEFENCE_ZONE_SIZE = 5000
    DEFENCE_LEVEL = DEFENCE_HIGH
    DEFENCE_ZONE_BACKDRIFT = 2000
    USE_LIFTER = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.related_planet = None

    def get_related_planet(self):
        return self.related_planet

    def set_related_planet(self, planet):
        self.related_planet = planet

    def get_infocard_map(self):
        if self.related_planet:
            return f'Map = {self.related_planet.get_ids_info1()}, {self.get_ids_info2()}'

    def get_main_rotate(self):
        return self.Y_ROTATE_PER_REL[self.REL]

    def get_rotate(self):
        return (0, self.get_main_rotate(), 0)

    def get_interior_content(self):
        raise Exception('Interior for dock ring planets should be only manual created')

    def get_sattelites(self):
        position = self.get_position()

        sattelites = []

        # DOCKING FIXTURE

        fixture_position = (
            self.FIXTURE_POSITION_APPEND[0] + position[0],
            self.FIXTURE_POSITION_APPEND[1] + position[1],
            self.FIXTURE_POSITION_APPEND[2] + position[2],
        )

        sattelites.append(
            self.DOCKING_FIXTURE_TEMPLATE.format(
                parent_object=self.get_space_object_name(),
                pos='{}, {}, {}'.format(*fixture_position),
                rotate='{}, {}, {}'.format(*self.get_rotate()),
                parent_base=self.get_base_nickname(),
                reputation=self.get_faction_code(),
            )
        )

        sattelites.extend(
            self.get_trade_points_front()
        )

        return sattelites

    def get_space_name(self):
        return MS('Стыковочное кольцо', 'Docking ring')

    def get_tradelane_ids_name(self):
        return self.related_planet.get_ids_name()

    def get_base_string_id(self):
        if self.related_planet:
            return self.related_planet.get_ids_name()
        return self.get_ids_name()


class LargePlanetDockring(Dockring):
    BASE_PROPS = meta.LargePlanet()
    MISC_EQUIP_GEN_TYPE = GEN_PIRATE
    EQUIP_SET = markets.MainPlanetSet

    TRADE_POINTS_OFFSETS = [
        [500, 200, 0],
        [-500, 200, 0],
        [500, -200, 0],
        [-500, -200, 0],
    ]
    TRADE_DEPOT_ARCHETYPES = [diversion.TradingTrain,
                              diversion.TradingLargeTransport,
                              diversion.TradingTrainCargo]
    TRADE_POINT_EMPTY_ARCHETYPE = diversion.TradingTrainCargoEmpty


class MiningPlanetDockring(Dockring):
    BASE_PROPS = meta.MiningPlanet()
    EQUIP_SET = markets.CivPlanetSet
    MISC_EQUIP_GEN_TYPE = GEN_CIV

    TRADE_POINTS_OFFSETS = [
        [500, 200, 0],
        [-500, 200, 0],
        [500, -200, 0],
        [-500, -200, 0],
    ]
    TRADE_DEPOT_ARCHETYPES = [diversion.TradingLargeTransport, diversion.TradingSmallTransport]


class ResortPlanetDockring(Dockring):
    BASE_PROPS = meta.ResortPlanet()
    EQUIP_SET = markets.CivPlanetSet
    MISC_EQUIP_GEN_TYPE = GEN_CIV

    TRADE_POINTS_OFFSETS = [
        [-500, 200, 0],
        [-500, -200, 0],
    ]
    TRADE_DEPOT_ARCHETYPES = [diversion.TradingSmallTransport]


class WaterPlanetDockring(Dockring):
    BASE_PROPS = meta.WaterPlanet()
    EQUIP_SET = markets.CivPlanetSet
    MISC_EQUIP_GEN_TYPE = GEN_CIV

    TRADE_POINTS_OFFSETS = [
        [500, 200, 0],
        [500, -200, 0],
    ]
    TRADE_DEPOT_ARCHETYPES = [diversion.TradingSmallTransport]


class Station(DockableObject):
    ALIAS = 'station'
    BASE_PROPS = meta.SpaceStation()
    EQUIP_SET = markets.StationSet
    MISC_EQUIP_GEN_TYPE = GEN_CIV


class LargeStation(Station):
    EQUIP_SET = markets.LargeStationSet
    MISC_EQUIP_GEN_TYPE = GEN_MAIN


class TradelaneSupportStation(Station):
    BASE_PROPS = meta.TradelaneSupportStation()


class ResearchStation(Station):
    BASE_PROPS = meta.Research()
    EQUIP_SET = markets.ResearchSet
    MISC_EQUIP_GEN_TYPE = GEN_CIV


class GasMiningStation(Station):
    BASE_PROPS = meta.GasMiningStation()


class RoidMinerStation(Station):
    BASE_PROPS = meta.RoidMiningStation()


class AbandonedAsteroid(DockableObject):
    AUDIO_PREFIX = SpaceVoice.RESEARCH_BASE
    RANDOM_ROBOT = True
    BASE_PROPS = meta.LockedAsteroid()
    EQUIP_SET = None
    SELL_AMMO = False
    KEY_COLLECT_FX = nn.FX_GOT_KEY_ASTEROID
    RU_FIRST_DESCRIPTION = descriptions.ASTEROID_ROCK
    FORCE_FACTION = faction.Unknown


class AbandonedAsteroidIce(DockableObject):
    AUDIO_PREFIX = SpaceVoice.RESEARCH_BASE
    RANDOM_ROBOT = True
    BASE_PROPS = meta.LockedAsteroid()
    SELL_AMMO = False
    EQUIP_SET = None
    KEY_COLLECT_FX = nn.FX_GOT_KEY_ASTEROID
    RU_FIRST_DESCRIPTION = descriptions.ASTEROID_ICE
    FORCE_FACTION = faction.Unknown


class GasMinerOld(Station):
    RANDOM_ROBOT = True
    SELL_AMMO = False
    EQUIP_SET = None
    AUDIO_PREFIX = SpaceVoice.GAS_MINER
    KEY_COLLECT_FX = nn.FX_GOT_KEY_GAS_MINER
    RU_FIRST_DESCRIPTION = descriptions.GAS_MINER_OLD

    CARGO_PODS_POSITION_Y_DRIFT = -60

    CARGO_PODS_TEMPLATE = '''[Object]
nickname = {parent_gasminer}_cargo
pos = {position}
rotate = {rotate}
archetype = gas_mining_cargo
reputation = {faction}
behavior = NOTHING'''

    def get_cargo_pods(self):
        pos_x, pos_y, pos_z = self.get_position()
        
        return self.CARGO_PODS_TEMPLATE.format(
            parent_gasminer=self.get_inspace_nickname(),
            position='{}, {}, {}'.format(pos_x, pos_y+self.CARGO_PODS_POSITION_Y_DRIFT, pos_z),
            rotate='{}, {}, {}'.format(*self.get_rotate()),
            faction=self.get_faction().get_code(),
        )

    def get_sattelites(self):
        return [self.get_cargo_pods()]


class SolarPlant(Station):
    ALIAS = 'solar'
    RANDOM_ROBOT = True
    BASE_PROPS = meta.LockedSolarPlant()
    SELL_AMMO = False
    KEY_COLLECT_FX = nn.FX_GOT_KEY_STATION
    RU_FIRST_DESCRIPTION = descriptions.SOLAR_PLANT
    FORCE_FACTION = faction.Unknown
    AUDIO_PREFIX = SpaceVoice.SOLAR_PLANT


class RoidMiner(Station):
    RANDOM_ROBOT = True
    ROTATE_RANDOM = False
    BASE_PROPS = meta.LockedRoidMiner()
    SELL_AMMO = False
    EQUIP_SET = None
    KEY_COLLECT_FX = nn.FX_GOT_KEY_ROID_MINER
    RU_FIRST_DESCRIPTION = descriptions.ROID_MINER
    AUDIO_PREFIX = SpaceVoice.ROID_MINER

    ASTEROID_OFFSET = (0, 5, -235)
    ASTEROID_ROTATE = (145, -30, 34)
    ASTEROID_ARCHETYPE = 'om15_mining_asteroid'

    ASTEROID_TEMPLATE = '''[Object]
nickname = {parent_roidminer}_ast
pos = {position}
rotate = {rotate}
archetype = {archetype}
visit = 128'''

    CARGO_PODS_POSITION_Y_DRIFT = 5
    CARGO_PODS_LOADOUT = ''

    CARGO_PODS_TEMPLATE = '''[Object]
nickname = {parent_roidminer}_cargo
pos = {position}
rotate = {rotate}
archetype = mining_cargo
reputation = {faction}
loadout = {loadout}
behavior = NOTHING
ids_name = 261161
ids_info = 66150'''

    def get_asteroid(self):
        pos_x, pos_y, pos_z = self.get_position()
        offset_x, offset_y, offset_z = self.ASTEROID_OFFSET

        return self.ASTEROID_TEMPLATE.format(
            parent_roidminer=self.get_inspace_nickname(),
            position='{}, {}, {}'.format(pos_x+offset_x, pos_y+offset_y, pos_z+offset_z),
            rotate='{}, {}, {}'.format(*self.ASTEROID_ROTATE),
            archetype=self.ASTEROID_ARCHETYPE,
        )

    def get_cargo_pods(self):
        pos_x, pos_y, pos_z = self.get_position()

        return self.CARGO_PODS_TEMPLATE.format(
            parent_roidminer=self.get_inspace_nickname(),
            position='{}, {}, {}'.format(pos_x, pos_y+self.CARGO_PODS_POSITION_Y_DRIFT, pos_z),
            rotate='{}, {}, {}'.format(*self.get_rotate()),
            faction=self.get_faction().get_code(),
            loadout=self.CARGO_PODS_LOADOUT,
        )

    def get_sattelites(self):
        return [self.get_cargo_pods(), self.get_asteroid()]

    def get_rotate(self):
        return 0, 0, 0


class DebrisManufactoring(Station):
    AUDIO_PREFIX = SpaceVoice.FACTORY
    RANDOM_ROBOT = True
    BASE_PROPS = meta.LockedSmelter()
    SELL_AMMO = False
    EQUIP_SET = None
    KEY_COLLECT_FX = nn.FX_GOT_KEY_FACTORY
    RU_FIRST_DESCRIPTION = descriptions.DEBRIS_MANUFACTORING


class Outpost(DockableObject):
    ALIAS = 'outpost'
    BASE_PROPS = meta.Outpost()
    EQUIP_SET = markets.PoliceOutpostSet
    MISC_EQUIP_GEN_TYPE = GEN_PIRATE


class Prison(DockableObject):
    ALIAS = 'prison'
    BASE_PROPS = meta.Prison()
    EQUIP_SET = markets.PrisonSet
    MISC_EQUIP_GEN_TYPE = GEN_PIRATE


class Shipyard(DockableObject):
    ALIAS = 'shipyard'
    BASE_PROPS = meta.Shipyard()
    EQUIP_SET = markets.ShipyardSet
    MISC_EQUIP_GEN_TYPE = GEN_PIRATE


class LargeShipyard(Shipyard):
    EQUIP_SET = markets.LargeStationSet
    MISC_EQUIP_GEN_TYPE = GEN_PIRATE


class TradingBase(DockableObject):
    ALIAS = 'trading'
    BASE_PROPS = meta.TradingBase()
    EQUIP_SET = markets.StationSet
    MISC_EQUIP_GEN_TYPE = GEN_CIV

    TRADE_POINT_Y = -500
    TRADE_POINT_Z = 1000
    TRADE_POINT_ORIENTS = [45, 135, 225, 315]
    TRADE_DEPOT_ARCHETYPES = [diversion.TradingTrain, diversion.TradingLargeTransport]
    TRADE_POINT_ARCHETYPE = diversion.TradingFixture

    def get_sattelites(self):
        return self.get_trade_points_orient()


class Battleship(DockableObject):
    ALIAS = 'bship'
    BASE_PROPS = meta.Battleship()
    EQUIP_SET = markets.BattleshipSet
    MISC_EQUIP_GEN_TYPE = GEN_MAIN


class RheinlandBattleship(Battleship):
    ARCHETYPE = 'r_battleship'
    LOADOUT = 'rh_battleship_station'


class LibertyBattleship(Battleship):
    ARCHETYPE = 'l_dreadnought'
    LOADOUT = 'li_dreadnought_station'


class BretoniaBattleship(Battleship):
    ARCHETYPE = 'b_battleship'
    LOADOUT = 'br_battleship_station'


class KusariBattleship(Battleship):
    ARCHETYPE = 'k_battleship'
    LOADOUT = 'ku_battleship_station'


class LuxuryLiner(Battleship):
    ARCHETYPE = 'luxury_liner'
    LOADOUT = 'ge_liner_co_01'
    BASE_PROPS = meta.LuxuryLiner()
    EQUIP_SET = markets.StationSet
    MISC_EQUIP_GEN_TYPE = GEN_CIV


class Freeport(DockableObject):
    ALIAS = 'freeport'
    BASE_PROPS = meta.Freeport()
    EQUIP_SET = markets.StationSet
    MISC_EQUIP_GEN_TYPE = GEN_PIRATE


class JunkerBase(DockableObject):
    ALIAS = 'junker'
    BASE_PROPS = meta.JunkerBase()
    EQUIP_SET = markets.PirateSet
    MISC_EQUIP_GEN_TYPE = GEN_PIRATE


class PirateBase(DockableObject):
    ALIAS = 'pirate'
    EQUIP_SET = markets.PirateSet
    MISC_EQUIP_GEN_TYPE = GEN_PIRATE


class PirateStation(PirateBase):
    BASE_PROPS = meta.PirateStation()


class PirateGasMiner(PirateBase):
    BASE_PROPS = meta.PirateGasMiner()


class PirateAsteroid(PirateBase):
    BASE_PROPS = meta.PirateAsteroid()


class Refinery(DockableObject):
    ALIAS = 'alg'
    BASE_PROPS = meta.Refinery()
    EQUIP_SET = markets.StationSet
    MISC_EQUIP_GEN_TYPE = GEN_CIV


class Hackable(DockableObject):
    HACKABLE_SOLAR_CLASS = None
    LOCKED_DOCK = True
    DEFENCE_LEVEL = None
    RANDOM_ROBOT = True
    BASE_PROPS = meta.LockedHackableOutpost()
    CALC_STORE = False
    SELL_AMMO = False
    EQUIP_SET = None
    FORCE_FACTION = faction.Unknown

    def get_position(self):
        if self.RELATED_OBJECT:
            if not self.RELATED_OBJECT.SPACE_OBJECT_TEMPLATE:
                raise Exception('Related object must have template')
            offset = self.RELATED_OBJECT.SPACE_OBJECT_TEMPLATE.get_locked_object_offset(self.RELATED_OBJECT_INDEX)
            position = self.system.get_object_position(self.RELATED_OBJECT)
            return offset[0]+position[0], offset[1]+position[1], offset[2]+position[2]
        else:
            return super().get_position()

    def get_archetype(self):
        return self.HACKABLE_SOLAR_CLASS.ARCHETYPE

    def get_hacker_panel_position(self):
        pos_x, pos_y, pos_z = self.get_position()
        offset_x, offset_y, offset_z = self.HACKABLE_SOLAR_CLASS.OFFSET
        return (pos_x+offset_x, pos_y+offset_y, pos_z+offset_z)

    def get_rotate(self):
        return self.HACKABLE_SOLAR_CLASS.ROTATE

    def get_hacker_name(self):
        return f'{self.get_base_nickname()}_hacker_panel'

    def get_hacker_panel(self):
        panel = self.system.get_random_hacker_panel()
        hacker_name = self.get_hacker_name()
        hacker_position = self.get_hacker_panel_position()

        space_panel = panel.get_space_content(
            space_name=hacker_name,
            reputation=self.get_faction().get_code(),
            position=hacker_position,
            relation=self.HACKABLE_SOLAR_CLASS.PANEL_RELATION,
            success_loadout=hacker_name,
        )

#         space_zone = f'''
# [Zone]
# nickname = {hacker_name}_help_zone
# pos = {hacker_position[0]}, {hacker_position[1]}, {hacker_position[2]}
# shape = SPHERE
# size = 50
# spacedust = gf_hacker_help
# spacedust_maxparticles = 1
#         '''

        return DIVIDER.join([space_panel])

    def get_sattelites(self):
        return [self.get_hacker_panel()]

    def get_hacker_loadout(self):
        loadout = Loadout(loadout_nickname=self.get_hacker_name())
        base_key = self.get_key_name()
        loadout.add_cargo(base_key)
        return loadout

    def get_loadouts(self):
        return [self.get_hacker_loadout()]


class HackableStation(Hackable):
    AUDIO_PREFIX = SpaceVoice.STATION
    KEY_COLLECT_FX = nn.FX_GOT_KEY_STATION
    RU_FIRST_DESCRIPTION = descriptions.HACKABLE_STATION


class HackableSolarPlant(Hackable):
    AUDIO_PREFIX = SpaceVoice.SOLAR_PLANT
    KEY_COLLECT_FX = nn.FX_GOT_KEY_STATION
    RU_FIRST_DESCRIPTION = descriptions.HACKABLE_SOLAR_PLANT


class HackableBattleship(Hackable):
    AUDIO_PREFIX = SpaceVoice.BATTLESHIP
    KEY_COLLECT_FX = nn.FX_GOT_KEY_BATTLESHIP
    RU_FIRST_DESCRIPTION = descriptions.BATTLESHIP_HACKABLE


class HackableLuxury(Hackable):
    AUDIO_PREFIX = SpaceVoice.LINER
    KEY_COLLECT_FX = nn.FX_GOT_KEY_BATTLESHIP
    RU_FIRST_DESCRIPTION = descriptions.HACKABLE_LUXURY


class LockedBattleship(Station):
    AUDIO_PREFIX = SpaceVoice.BATTLESHIP
    LOCKED_DOCK = True
    ROTATE_RANDOM = True
    RANDOM_ROBOT = True
    DEFENCE_LEVEL = None
    BASE_PROPS = meta.LockedBattleship()
    KEY_COLLECT_FX = nn.FX_GOT_KEY_BATTLESHIP
    RU_FIRST_DESCRIPTION = descriptions.BATTLESHIP_LOCKED
    FORCE_FACTION = faction.Unknown


class LockedLuxury(Station):
    AUDIO_PREFIX = SpaceVoice.LINER
    LOCKED_DOCK = True
    ROTATE_RANDOM = True
    RANDOM_ROBOT = True
    DEFENCE_LEVEL = None
    BASE_PROPS = meta.LockedBattleship()
    KEY_COLLECT_FX = nn.FX_GOT_KEY_BATTLESHIP
    RU_FIRST_DESCRIPTION = descriptions.LUXURY_LOCKED
    FORCE_FACTION = faction.Unknown
    EQUIP_SET = None
    SELL_AMMO = False


class PatrolObjective(SystemObject):
    PATROL_ALIAS = None

    TRACKS_PATROL_HEADING = '[Path]'
    TRACKS_PATROL_NAME = 'name = {name}, {index}'
    TRACKS_PATROL_ITEM = 'pos = {pos}'
    
    def __init__(self, system, population_kind, index, positions):
        self.system = system
        self.population_kind = population_kind
        self.index = index
        self.positions = positions
        self.raw_paths = []

    def get_population_kind(self):
        return self.population_kind

    def get_tracks_request_content(self):
        items = [
            self.TRACKS_PATROL_HEADING,
            self.TRACKS_PATROL_NAME.format(name=self.PATROL_ALIAS, index=self.index),
        ]

        for pos_item in self.positions:
            items.append(
                self.TRACKS_PATROL_ITEM.format(pos='{0}, {1}, {2}'.format(*pos_item))
            )

        return SINGLE_DIVIDER.join(items)

    def add_raw_path(self, tracks_raw_zone):
        self.raw_paths.append(tracks_raw_zone)

    def get_path_label(self):
        return '{0}{1}'.format(self.PATROL_ALIAS, self.index)

    def get_zone_params(self):
        raise NotImplementedError

    def get_system_content(self):
        system_content = []
        for path in self.raw_paths:
            lines = ['[Zone]'] + path.raw_lines
            lines.append(self.get_zone_params())
            zone_item = SINGLE_DIVIDER.join(lines)
            system_content.append(zone_item)

        return DIVIDER.join(system_content)


class PolicePatrol(PatrolObjective):
    PATROL_ALIAS = 'police'

    ZONE_PARAMS = '''toughness = 1
density = 1
repop_time = 90
max_battle_size = 3
pop_type = lane_patrol
relief_time = 30
usage = patrol
mission_eligible = true
density_restriction = 1, patroller
density_restriction = 1, police_patroller
density_restriction = 1, pirate_patroller
density_restriction = 4, lawfuls
density_restriction = 4, unlawfuls
encounter = {police_encounter}, 1, 0.330000
faction = {police_faction}, 1.000000'''

    def get_zone_params(self):
        lawful_population = self.get_lawful_population_class()
        return self.ZONE_PARAMS.format(
            police_encounter=lawful_population.get_police_encounter(),
            police_faction=lawful_population.get_police_faction().get_code(),
        )


class HuntersPatrol(PatrolObjective):
    PATROL_ALIAS = 'bounty_hunter'

    ZONE_PARAMS = '''toughness = 4
density = 3
repop_time = 90
max_battle_size = 4
pop_type = field_patrol
relief_time = 30
usage = patrol
mission_eligible = true
density_restriction = 1, patroller
density_restriction = 1, police_patroller
density_restriction = 1, pirate_patroller
density_restriction = 4, lawfuls
density_restriction = 4, unlawfuls
encounter = {bh_encounter}, 1, 0.330000
faction = {bh_faction}, 1.000000'''

    def get_zone_params(self):
        lawful_population = self.get_lawful_population_class()
        return self.ZONE_PARAMS.format(
            bh_encounter=lawful_population.get_bounty_hunter_encounter(),
            bh_faction=lawful_population.get_bounty_hunter_faction().get_code(),
        )


class PiratePatrol(PatrolObjective):
    PATROL_ALIAS = 'pirate'

    ZONE_PARAMS = '''toughness = 1
density = 1
repop_time = 90
max_battle_size = 3
pop_type = attack_patrol
relief_time = 30
attack_ids = 10
tradelane_attack = 50
mission_eligible = true
density_restriction = 1, patroller
density_restriction = 1, police_patroller
density_restriction = 1, pirate_patroller
density_restriction = 4, lawfuls
density_restriction = 4, unlawfuls
encounter = {attack_tlr_encounter}, 1, 0.330000
faction = {pirate_faction}, 1.000000'''

    def get_zone_params(self):
        unlawful_population = self.get_unlawful_population_class()
        return self.ZONE_PARAMS.format(
            attack_tlr_encounter=unlawful_population.get_tlr_attackers_encounter(),
            pirate_faction=unlawful_population.get_tlr_attackers_faction().get_code(),
        )


class Tradelane:
    TLR_NAME_ID = 260920
    TLR_INFO_ID = 66170
    ARCHETYPE = 'Trade_Lane_Ring'
    MIDDLE_RING_LOADOUT = 'trade_lane_ring_main'
    LAST_RING_LOADOUT = MIDDLE_RING_LOADOUT
    START_RING_LOADOUT = MIDDLE_RING_LOADOUT
    TLR_Y_OFFSET = 0

    RING_TEMPLATE = '''[Object]
nickname = {ring_nickname}
ids_name = {ids_name}
ids_info = {ids_info}
pos = {pos}
rotate = {rotate}
archetype = {archetype}
behavior = NOTHING
reputation = {faction}
loadout = {loadout}
pilot = pilot_solar_hard
{extra}
'''
    PREV_RING_TEMPLATE = 'prev_ring = {prev_ring}'
    NEXT_RING_TEMPLATE = 'next_ring = {next_ring}'
    RING_SPACE_NAME_TEMPLATE = 'tradelane_space_name = {ids_name}'

    def __init__(self, trade_connection, tracks_raw_tradelane, tradelane_index):
        self.trade_connection = trade_connection
        self.tracks_raw_tradelane = tracks_raw_tradelane
        self.tradelane_index = tradelane_index
        if not self.tracks_raw_tradelane.is_object():
            raise Exception('object is not tradelane')

    def get_ring_nickname(self):
        return '{system_name}_F_Trade_Lane_Ring_{letter}0{index}'.format(
            system_name=self.trade_connection.system.NAME.upper(),
            letter=self.trade_connection.TRADELANE_LETTER,
            index=self.tradelane_index,
        )

    def get_tradelane_pos(self):
        tlr_pos = self.tracks_raw_tradelane.lines[POS_KEY]
        return tlr_pos[0], tlr_pos[1] + self.TLR_Y_OFFSET, tlr_pos[2]

    def get_tradelane_rotate(self):
        return self.tracks_raw_tradelane.lines[ROT_KEY]

    def get_system_object(self):
        template_params = {
            'ids_name': self.TLR_NAME_ID,
            'ids_info': self.TLR_INFO_ID,
            'ring_nickname': self.get_ring_nickname(),
            'pos': '{0}, {1}, {2}'.format(*self.get_tradelane_pos()),
            'rotate': '{0}, {1}, {2}'.format(*self.get_tradelane_rotate()),
            'faction': self.trade_connection.FACTION.get_code(),
            'archetype': self.ARCHETYPE,
        }

        prev_ring = self.trade_connection.get_prev_ring(self.tradelane_index)
        next_ring = self.trade_connection.get_next_ring(self.tradelane_index)

        extra = []
        if prev_ring:
            extra.append(self.PREV_RING_TEMPLATE.format(prev_ring=prev_ring.get_ring_nickname()))
        if next_ring:
            extra.append(self.NEXT_RING_TEMPLATE.format(next_ring=next_ring.get_ring_nickname()))

        if not prev_ring:
            template_params['loadout'] = self.START_RING_LOADOUT
            extra.append(self.RING_SPACE_NAME_TEMPLATE.format(
                ids_name=self.trade_connection.get_obj_from().get_tradelane_ids_name()))
        elif not next_ring:
            template_params['loadout'] = self.LAST_RING_LOADOUT
            extra.append(self.RING_SPACE_NAME_TEMPLATE.format(
                ids_name=self.trade_connection.get_obj_to().get_tradelane_ids_name()))
        else:
            template_params['loadout'] = self.MIDDLE_RING_LOADOUT

        template_params['extra'] = SINGLE_DIVIDER.join(extra)

        return self.RING_TEMPLATE.format(**template_params)


class TradeConnection(SystemObject):
    OBJ_FROM = None
    OBJ_TO = None
    SIDE_FROM = None
    SIDE_TO = None
    TRADELANE_LETTER = None
    HUNTER_DEFENCE_REL = None
    ATTACKED_BY = []

    TRADELANE_CLASS = Tradelane
    POLICE_PATROL = True
    TLR_OUTER_ZONE = True

    OBJ_FROM_EXTRA_DRIFT = 0
    OBJ_FROM_EXTRA_DRIFT_ALT_AXIS = 0
    OBJ_FROM_TLR_FORCE_OFFSET = None
    OBJ_TO_EXTRA_DRIFT = 0
    OBJ_TO_EXTRA_DRIFT_ALT_AXIS = 0
    OBJ_TO_TLR_FORCE_OFFSET = None

    HUNTER_PATROL_OFFSET = 10000
    HUNTER_PATROL_DRIFT = 3000

    TRADELANE_ZONE_SIZE = 2500
    TLR_DISTANCE = 7000

    TRACKS_TLR_TEMPLATE = '''[TradeLane]
number = 1
count = 1
distance = {tlr_distance}

first = {first_tlr_props}
last = {last_tlr_props}

zone = {tlr_zone_size}, {tlr_zone_index}
'''
    ZONE_TEMPLATE = '''[zone]
nickname = Zone_{system_name}_tlr_{tlr_letter}
pos = {pos}
rotate = {rotate}
shape = BOX
size = {size}'''

    def __init__(self, system):
        self.system = system
        if not self.TRADELANE_LETTER:
            raise Exception('Tradelane should have a letter')
        self.last_tradelane_index = 1
        self.tradelanes = []
        self.tracks_raw_outer_zone = None
        self.police_patrol = None
        self.bounty_hunter_patrol = None
        self.attacker_patrols = []

    def init_patrols(self):
        self.police_patrol = self.get_police_patrol()
        if self.police_patrol:
            self.system.add_patrol(self.police_patrol)
        self.bounty_hunter_patrol = self.get_bounty_hunter_patrol()
        if self.bounty_hunter_patrol:
            self.system.add_patrol(self.bounty_hunter_patrol)
        for attacker_base in self.ATTACKED_BY:
            attacker_patrol = self.get_pirate_attacker_patrol(attacker_base)
            self.attacker_patrols.append(attacker_patrol)
            self.system.add_patrol(attacker_patrol)

    def get_destination_objects(self):
        if not self.OBJ_FROM and not self.OBJ_TO:
            raise Exception('OBJ_FROM and OBJ_TO is required')

        if not issubclass(self.OBJ_FROM, SystemObject):
            raise Exception('OBJ_FROM %s is not SystemObject' % self.OBJ_FROM)

        if not issubclass(self.OBJ_TO, SystemObject):
            raise Exception('OBJ_TO %s is not SystemObject' % self.OBJ_TO)

        return (self.system.get_system_object_instance(self.OBJ_FROM), self.system.get_system_object_instance(self.OBJ_TO))

    def get_obj_from(self):
        return self.system.get_system_object_instance(self.OBJ_FROM)

    def get_obj_to(self):
        return self.system.get_system_object_instance(self.OBJ_TO)

    def get_attacker_objects(self):
        return [self.system.get_system_object_instance(att) for att in self.ATTACKED_BY]

    def get_edge_objects(self):
        return list(self.get_destination_objects()) + self.get_attacker_objects()

    def get_sides(self):
        if not self.SIDE_FROM or not self.SIDE_TO:
            raise Exception('SIDE_FROM and SIDE_TO is required')

        if self.SIDE_FROM not in DIRECTIONS:
            raise Exception('SIDE_FROM %s isnt correct direction' % self.SIDE_FROM)

        if self.SIDE_TO not in DIRECTIONS:
            raise Exception('SIDE_TO %s isnt correct direction' % self.SIDE_TO)

        return (self.SIDE_FROM, self.SIDE_TO)

    def get_side_tradelanes_props(self):
        obj_from, obj_to = self.get_destination_objects()
        side_from, side_to = self.get_sides()

        start_tradelane_props = obj_from.get_tradelane_props(side_from, self.OBJ_FROM_EXTRA_DRIFT, self.OBJ_FROM_EXTRA_DRIFT_ALT_AXIS, force_offset=self.OBJ_FROM_TLR_FORCE_OFFSET)
        end_tradelane_props = obj_to.get_tradelane_props(side_to, self.OBJ_TO_EXTRA_DRIFT, self.OBJ_TO_EXTRA_DRIFT_ALT_AXIS, force_offset=self.OBJ_TO_TLR_FORCE_OFFSET)

        return start_tradelane_props, end_tradelane_props

    def get_tracks_request_content(self, zone_index=1):
        start_tradelane_props, end_tradelane_props = self.get_side_tradelanes_props()
        return self.TRACKS_TLR_TEMPLATE.format(
            first_tlr_props='{0}, {1}, {2}, {3}'.format(*start_tradelane_props),
            last_tlr_props='{0}, {1}, {2}, {3}'.format(*end_tradelane_props),
            tlr_zone_size=self.TRADELANE_ZONE_SIZE,
            tlr_zone_index=zone_index,
            tlr_distance=self.TLR_DISTANCE,
        )

    def add_tradelane(self, tracks_raw_tradelane):
        self.tradelanes.append(self.TRADELANE_CLASS(self, tracks_raw_tradelane, self.last_tradelane_index))
        self.last_tradelane_index += 1

    def set_tradelane_zone(self, tracks_raw_tlr_zone):
        self.tracks_raw_outer_zone = tracks_raw_tlr_zone

    def get_prev_ring(self, index):
        prev_index = index - 1 
        if prev_index < 1:
            return None

        for tlr in self.tradelanes:
            if tlr.tradelane_index == prev_index:
                return tlr

        return None        

    def get_next_ring(self, index):
        next_index = index + 1

        for tlr in self.tradelanes:
            if tlr.tradelane_index == next_index:
                return tlr

        return None

    def get_tradelane_zone(self):
        if not self.system.have_population() or not self.TLR_OUTER_ZONE:
            return ''

        lawful_population = self.get_lawful_population_class()

        obj_from, obj_to = self.get_destination_objects()

        if base_from := obj_from.get_base():
            base_from.add_faction(lawful_population.MAIN_TRADERS)
        if base_to := obj_to.get_base():
            base_to.add_faction(lawful_population.MAIN_TRADERS)

        return SINGLE_DIVIDER.join([
            self.ZONE_TEMPLATE.format(
                system_name=self.system.NAME.upper(),
                tlr_letter=self.TRADELANE_LETTER,
                pos='{0}, {1}, {2}'.format(*self.tracks_raw_outer_zone.lines[POS_KEY]),
                rotate='{0}, {1}, {2}'.format(*self.tracks_raw_outer_zone.lines[ROT_KEY]),
                size='{0}, {1}, {2}'.format(*self.tracks_raw_outer_zone.lines[SIZE_KEY]),
            ),
            lawful_population.get_tradelane_arriaval_traders_params(),
        ])

    def get_system_content(self):
        system_content = []
        for tlr in self.tradelanes:
            system_content.append(tlr.get_system_object())

        if self.tracks_raw_outer_zone:
            system_content.append(self.get_tradelane_zone())

        return DIVIDER.join(system_content)

    def get_police_patrol(self):
        if not self.POLICE_PATROL:
            return
        obj_from, obj_to = self.get_destination_objects()
        obj_from_pos = self.system.get_object_position(obj_from)
        obj_to_pos = self.system.get_object_position(obj_to)

        patrol_faction = self.get_lawful_population_class().get_police_faction()
        if base_from := obj_from.get_base():
            base_from.add_faction(patrol_faction)
        if base_to := obj_to.get_base():
            base_to.add_faction(patrol_faction)

        return PolicePatrol(
            system=self.system,
            population_kind=self.get_population_kind(),
            index=self.system.get_next_police_patrol_id(),
            positions=[
                (obj_from_pos[0], 0, obj_from_pos[2]),
                (obj_to_pos[0], 0, obj_to_pos[2]),
            ]
        ) 

    def get_bounty_hunter_patrol(self):
        patrol_rel = self.HUNTER_DEFENCE_REL
        if patrol_rel is None:
            return

        obj_from, obj_to = self.get_destination_objects()
        obj_from_pos = self.system.get_object_position(obj_from)
        obj_to_pos = self.system.get_object_position(obj_to)

        patrol_faction = self.get_lawful_population_class().get_bounty_hunter_faction()
        if base_from := obj_from.get_base():
            base_from.add_faction(patrol_faction)
        if base_to := obj_to.get_base():
            base_to.add_faction(patrol_faction)

        obj_from_pos2_x = obj_from_pos[0]
        obj_from_pos2_z = obj_from_pos[2]
        obj_to_pos2_x = obj_to_pos[0]
        obj_to_pos2_z = obj_to_pos[2]

        if patrol_rel == LEFT:
            obj_from_pos2_x -= self.HUNTER_PATROL_OFFSET
            obj_from_pos2_z += self.HUNTER_PATROL_DRIFT
            obj_to_pos2_x -= self.HUNTER_PATROL_OFFSET
            obj_to_pos2_z -= self.HUNTER_PATROL_DRIFT
        
        if patrol_rel == RIGHT:
            obj_from_pos2_x += self.HUNTER_PATROL_OFFSET
            obj_from_pos2_z += self.HUNTER_PATROL_DRIFT
            obj_to_pos2_x += self.HUNTER_PATROL_OFFSET
            obj_to_pos2_z -= self.HUNTER_PATROL_DRIFT

        if patrol_rel == TOP:
            obj_from_pos2_x += self.HUNTER_PATROL_DRIFT
            obj_from_pos2_z -= self.HUNTER_PATROL_OFFSET
            obj_to_pos2_x -= self.HUNTER_PATROL_DRIFT
            obj_to_pos2_z -= self.HUNTER_PATROL_OFFSET

        if patrol_rel == BOTTOM:
            obj_from_pos2_x += self.HUNTER_PATROL_DRIFT
            obj_from_pos2_z += self.HUNTER_PATROL_OFFSET
            obj_to_pos2_x -= self.HUNTER_PATROL_DRIFT
            obj_to_pos2_z += self.HUNTER_PATROL_OFFSET

        return HuntersPatrol(
            system=self.system,
            population_kind=self.get_population_kind(),
            index=self.system.get_next_bounty_hunter_patrol_id(),
            positions=[
                (obj_from_pos[0], 0, obj_from_pos[2]),
                (obj_from_pos2_x, 0, obj_from_pos2_z),
                (obj_to_pos2_x, 0, obj_to_pos2_z),
                (obj_to_pos[0], 0, obj_to_pos[2]),
            ]
        )

    def get_pirate_attacker_patrol(self, attacker_base):
        tlrs_len = len(self.tradelanes)

        if tlrs_len <= TLR_SMALL_SIZE_RINGS_COUNT:
            first_tradelane_index = 1
        else:
            first_tradelane_index = randint(1, tlrs_len-2)

        lane1_pos = self.tradelanes[first_tradelane_index].get_tradelane_pos()
        lane2_pos = self.tradelanes[first_tradelane_index+1].get_tradelane_pos()
        attacker_base_pos = self.system.get_object_position(attacker_base)

        attacker_base_instance = self.system.get_static_by_class(attacker_base)
        attacker_base_instance.get_base().add_faction(
            self.get_unlawful_population_class().get_tlr_attackers_faction()
        )

        return PiratePatrol(
            system=self.system,
            population_kind=self.get_population_kind(),
            index=self.system.get_next_pirate_patrol_id(),
            positions=[
                (attacker_base_pos[0], 0, attacker_base_pos[2]),
                (lane1_pos[0], 0, lane1_pos[2]),
                (lane2_pos[0], 0, lane2_pos[2]),
                (attacker_base_pos[0], 0, attacker_base_pos[2]),
            ]
        )


class LargeTradelane(Tradelane):
    # ARCHETYPE = 'TLR_CORSAIR'
    MIDDLE_RING_LOADOUT = 'large_co_tradelane_loadout'
    LAST_RING_LOADOUT = 'large_co_tradelane_loadout_end'
    START_RING_LOADOUT = 'large_co_tradelane_loadout_start'
    TLR_Y_OFFSET = 500


class LargeTradeConnection(TradeConnection):
    TLR_DISTANCE = 12000
    TRADELANE_CLASS = LargeTradelane
    POLICE_PATROL = False  # Temporary


class DestroyedTradelane(Tradelane):

    RING_TEMPLATE = '''[Object]
nickname = {ring_nickname}
ids_name = 260920
ids_info = 66170
pos = {pos}
rotate = {rotate}
archetype = Trade_Lane_Ring_Damage_A
'''

    def get_ring_nickname(self):
        return '{system_name}_broken_Trade_Lane_Ring_{letter}0{index}'.format(
            system_name=self.trade_connection.system.NAME.upper(),
            letter=self.trade_connection.TRADELANE_LETTER,
            index=self.tradelane_index,
        )

    def get_tradelane_pos(self):
        return self.tracks_raw_tradelane.lines[POS_KEY]

    def get_system_object(self):
        template_params = {
            'ring_nickname': self.get_ring_nickname(),
            'pos': '{0}, {1}, {2}'.format(*self.tracks_raw_tradelane.lines[POS_KEY]),
            'rotate': '{0}, {1}, {2}'.format(*self.tracks_raw_tradelane.lines[ROT_KEY]),
        }
        return self.RING_TEMPLATE.format(**template_params)


class BrokenTradeConnection(TradeConnection):
    TRADELANE_CLASS = DestroyedTradelane
    POLICE_PATROL = False
    TLR_OUTER_ZONE = False


class NavBuoyTradelane(Tradelane):

    RING_TEMPLATE = '''[Object]
nickname = {ring_nickname}
pos = {pos}
rotate = {rotate}
archetype = nav_buoy_non_targetable
visit = 128
'''

    def get_ring_nickname(self):
        return '{system_name}_buoy_{letter}0{index}'.format(
            system_name=self.trade_connection.system.NAME.upper(),
            letter=self.trade_connection.TRADELANE_LETTER,
            index=self.tradelane_index,
        )

    def get_tradelane_pos(self):
        return self.tracks_raw_tradelane.lines[POS_KEY]

    def get_system_object(self):
        template_params = {
            'ring_nickname': self.get_ring_nickname(),
            'pos': '{0}, {1}, {2}'.format(*self.tracks_raw_tradelane.lines[POS_KEY]),
            'rotate': '{0}, {1}, {2}'.format(*self.tracks_raw_tradelane.lines[ROT_KEY]),
        }
        return self.RING_TEMPLATE.format(**template_params)


class BuoyTradeConnection(TradeConnection):
    TRADELANE_CLASS = NavBuoyTradelane
    POLICE_PATROL = True
    TLR_OUTER_ZONE = False

    TLR_DISTANCE = 2000


class AbandonedBuoyTradeConnection(BuoyTradeConnection):
    POLICE_PATROL = False


class StoragePoint(StaticObject):
    ALIAS = 'storage'
    ARCHETYPES = []
    ORIENTS = []
    ORIENT_DRIFT = 3
    ROTATE_MIN = -360
    ROTATE_MAX = 360
    RADIUS = 3000

    def has_appearance(self):
        return True

    def get_inspace_nickname(self):
        return '{system_name}_storage{index:02d}'.format(system_name=self.system.NAME, index=self.INDEX)

    def get_single_rotate(self):
        return random.randint(self.ROTATE_MIN, self.ROTATE_MAX)

    def get_system_content(self):
        space_objects = []
        root_name = self.get_inspace_nickname()
        root_pos = self.get_position()

        i = 1
        for orient in self.ORIENTS:
            storage_archetype = random.choice(self.ARCHETYPES)
            orient += random.randint(-self.ORIENT_DRIFT, self.ORIENT_DRIFT)

            storage_pos = relocate_point([self.RADIUS, 0, 0], rotate_y=orient)

            storage_pos = [
                root_pos[0] + storage_pos[0],
                root_pos[1] + storage_pos[1],
                root_pos[2] + storage_pos[2]
            ]

            space_objects.append(f'''[Object]
nickname = {root_name}_storage{i:02d}
pos = {storage_pos[0]:0.3f}, {storage_pos[1]:0.3f}, {storage_pos[2]:0.3f} 
rotate = 0, {-self.get_single_rotate()}, 0
archetype = {storage_archetype.ARCHETYPE}
loadout = {storage_archetype.LOADOUT}
reputation = {self.get_faction_code()}
ids_name = 261161
behavior = NOTHING''')

            i += 1

        return DIVIDER.join(space_objects)


class SmugglerStoragePoint(StoragePoint):
    ARCHETYPES = [diversion.StorageSmuggler]
    ORIENTS = diversion.ORIENT_HEXAGON


class MetroMiningOne(StaticObject):
    ALIAS = 'metro'
    AST_TYPE = None
    ASTEROID_ARCHETYPE_TEMPLATE = '{ast}_xxxlarge_asteroid3'
    ASTEROID_LOADOUT_TEMPLATE = '{ast}_ast_a03_lock1'
    DRILLER_ARCHETYPE = 'space_co_mining_module_driller'
    DRILLER_LOADOUT = 'co_mining_module_driller'
    DRILLER_OFFSET = [-490, -400, -550]
    DRILLER_ROTATE = [-30, -120, 0]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.AST_TYPE not in AST_TYPES:
            raise Exception(f'Object {self} have invalid AST_TYPE. Actual value: {self.AST_TYPE}')

    def has_appearance(self):
        return True

    def get_inspace_nickname(self):
        return '{system_name}_metro{index:02d}'.format(system_name=self.system.NAME, index=self.INDEX)

    def get_main_rotate(self):
        return self.get_rotate()[1]

    def get_system_content(self):
        space_objects = []
        root_name = self.get_inspace_nickname()
        root_pos = self.get_position()
        root_rotate = self.get_main_rotate()

        driller_pos = relocate_point(self.DRILLER_OFFSET, rotate_y=-root_rotate)
        driller_pos = [
            root_pos[0] + driller_pos[0],
            root_pos[1] + driller_pos[1],
            root_pos[2] + driller_pos[2]
        ]

        driller_rotate = self.DRILLER_ROTATE.copy()
        driller_rotate[1] += root_rotate

        # ASTEROID
        space_objects.append(f'''[Object]
nickname = {root_name}_asteroid
pos = {root_pos[0]:0.3f}, {root_pos[1]:0.3f}, {root_pos[2]:0.3f} 
rotate = 0, {root_rotate}, 0
archetype = {self.ASTEROID_ARCHETYPE_TEMPLATE.format(ast=self.AST_TYPE)}
loadout = {self.ASTEROID_LOADOUT_TEMPLATE.format(ast=self.AST_TYPE)}''')

        # DRILLER
        space_objects.append(f'''[Object]
nickname = {root_name}_driller
pos = {driller_pos[0]:0.3f}, {driller_pos[1]:0.3f}, {driller_pos[2]:0.3f} 
rotate = {driller_rotate[0]:0.3f}, {driller_rotate[1]:0.3f}, {driller_rotate[2]:0.3f}
archetype = {self.DRILLER_ARCHETYPE}
loadout = {self.DRILLER_LOADOUT}
ids_name = 261161
ids_info = 1
reputation = {self.get_faction_code()}
behavior = NOTHING
''')

        return DIVIDER.join(space_objects)


class MetroMiningTwo(MetroMiningOne):
    ASTEROID_ARCHETYPE_TEMPLATE = '{ast}_xxxlarge_asteroid4'
    ASTEROID_LOADOUT_TEMPLATE = '{ast}_ast_a04_lock1'
    DRILLER_OFFSET = [315, -235, -10]
    DRILLER_ROTATE = [-20, 120, 0]


class BackgroundComplexObject(StaticObject):
    WORKSPACE_TEMPLATE_NAME = None
    ARCHETYPE_CHANGE_FROM = None
    ARCHETYPE_CHANGE_TO = None
    ROTATE = 0

    def has_appearance(self):
        return True

    def get_inspace_nickname(self):
        return '{system_name}_bgcmx_{index:02d}'.format(system_name=self.system.NAME, index=self.INDEX)

    def get_template_initial_data(self):
        if self.WORKSPACE_TEMPLATE_NAME is None:
            raise Exception(f'Object {self} have no workspace template')
        return ObjectTemplateLoader.get_template(self.WORKSPACE_TEMPLATE_NAME)

    def get_system_content(self):
        archetype_changes = []
        if self.ARCHETYPE_CHANGE_TO:

            if self.ARCHETYPE_CHANGE_FROM is None:
                raise Exception(f'Object {self} have no configured archetype changes')

            archetype_changes.append(
                [self.ARCHETYPE_CHANGE_FROM, self.ARCHETYPE_CHANGE_TO]
            )

        the_base = SpaceObjectTemplate(
            template=self.get_template_initial_data(),
            space_object_name=self.WORKSPACE_TEMPLATE_NAME,  # should be same inside
        )
        return the_base.get_instance(
            new_space_object_name=self.get_inspace_nickname(),
            archetype_changes=archetype_changes,
            move_to=self.get_position(),
            rotate_core=self.ROTATE
        )


class BackgroundTunnelOmega13(BackgroundComplexObject):
    ALIAS = 'tunnel'
    WORKSPACE_TEMPLATE_NAME = 'om13ast'
    ARCHETYPE_CHANGE_FROM = 'om15'  # it's initially om15 asteroid kind

