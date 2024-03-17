from random import randint

from fx.space import Dust

from universe.content.system_object import SystemObject, TOP, BOTTOM, LEFT, RIGHT, DIRECTIONS, POS_KEY, ROT_KEY, SIZE_KEY
from universe.content.zones import DynamicZone, DynamicSphereZone, RawZone
from universe.content import interior
from universe.content.locked_dock_key import LockedDockKey
from universe.content import faction
from universe.content.space_voice import SpaceVoice, SpaceCostume
from universe.content.loadout import Loadout

from text.dividers import SINGLE_DIVIDER, DIVIDER


TRADELANE_ZONE_SIZE = 2500

TLR_DISTANCE = 7000

TLR_HUGE_SIZE_RINGS_COUNT = 5
TLR_SMALL_SIZE_RINGS_COUNT = 4

DEFENCE_SIMPLE = 'simple'
DEFENCE_MEDIUM = 'medium'
DEFENCE_HIGH = 'high'


class AppearableObject(SystemObject):
    SPACE_OBJECT_TEMPLATE = None
    SPACE_OBJECT_NAME = None
    RELATED_OBJECT = None
    RELATED_OBJECT_INDEX = 0
    ARCHETYPE = None
    LOADOUT = None

    LOCKED_DOCK = False

    ARCHETYPE_TEMPLATE = '''[Object]
nickname = {nickname}
ids_name = {ids_name}
ids_info = {ids_info}
pos = {pos}
rotate = {rotate}
archetype = {archetype}'''

    def has_appearance(self):
        return self.ARCHETYPE or self.SPACE_OBJECT_TEMPLATE

    def get_system_content(self):
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

    def get_templated_content(self):
        position = self.get_position()
        if not position:
            raise Exception('POS is required for getting object instance when it has appaerance')

        return self.SPACE_OBJECT_TEMPLATE().get_instance(
            root_props=self.get_root_props(),
            dock_props=self.get_dock_props(),
            new_space_object_name=self.get_space_object_name(),
            move_to=position,
        )

    def get_archetype(self):
        return self.ARCHETYPE

    def get_single_object_content(self):
        content = [
            self.ARCHETYPE_TEMPLATE.format(
                nickname=self.get_inspace_nickname(),
                archetype=self.get_archetype(),
                ids_name=self.IDS_NAME,
                ids_info=self.IDS_INFO,
                pos='{}, {}, {}'.format(*self.get_position()),
                rotate='{}, {}, {}'.format(*self.get_rotate()),
            )
        ]

        if self.LOADOUT:
            content.append('loadout = {}'.format(self.LOADOUT))

        content.append(self.get_dock_props())

        for key, value in self.get_inspace_parameters().items():
            content.append('{} = {}'.format(key, value))

        item = SINGLE_DIVIDER.join(content)

        sattelites = self.get_sattelites()

        return DIVIDER.join([item] + sattelites)

    def get_sattelites(self):
        return []

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
    AST_ZONE_NAME_TEMPLATE = 'Zone_{space_name}_ast_exclusion'
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

    def get_ast_exclusion_zone_name(self):
        return self.AST_ZONE_NAME_TEMPLATE.format(
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

    def get_lawful_defence_zone_params(self):
        population_class = self.get_lawful_population_class()
        if self.DEFENCE_LEVEL == DEFENCE_SIMPLE:
            return population_class.get_simple_defence_params()
        elif self.DEFENCE_LEVEL == DEFENCE_MEDIUM:
            return population_class.get_medium_defence_params()
        elif self.DEFENCE_LEVEL == DEFENCE_HIGH:
            return population_class.get_high_defence_params()

        raise Exception('Unknown defence class for object %s' % self.__class__.__name__)

    def get_unlawful_defence_zone_params(self):
        raise Exception('unlawful not supported at this moment %s' % self.__class__.__name__)

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
        if len(self.ASTEROID_ZONES) != 0:
            zones.append(
                DynamicSphereZone(
                    system=self.system,
                    space_nickname=self.get_ast_exclusion_zone_name(),
                    alias=self.ALIAS,
                    index=self.INDEX,
                    size=self.AST_EXCLUSION_ZONE_SIZE,
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

        if self.DEFENCE_LEVEL and self.system.ENABLE_POPULATION:
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
        is_lawful = self.FACTION in self.system.LAWFUL_FACTIONS
        if not is_lawful and self.FACTION not in self.system.UNLAWFUL_FACTIONS:
            raise Exception('Faction isnt defined in a system for object %s' % self.__class__.__name__)
        return is_lawful


class VirtualDepot(StaticObject):
    ALIAS = 'virtual'

    def get_system_content(self):
        return ''

    def get_inspace_nickname(self):
        return '{system_name}_virtual_{index}'.format(system_name=self.system.NAME, index=self.INDEX)


class RawText(SystemObject):
    SPACE_CONTENT = ''

    def get_system_content(self):
        return self.SPACE_CONTENT


class JumpableObject(StaticObject):
    pass


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


class Planet(GenericSphere):
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

    IDS_NAME = 1
    IDS_INFO = 1

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

    def get_inspace_parameters(self):
        params = super().get_inspace_parameters()
        params['atmosphere_range'] = self.get_atmosphere_range()
        spin_data = self.get_spin()
        if spin_data:
            params['spin'] = spin_data

        if self.RELATED_DOCK_RING is not None:
            params.update(self.system.get_static_by_class(self.RELATED_DOCK_RING).get_raw_root_props())

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


class Jumpgate(JumpableObject):
    ALIAS = 'jg'
    REL_DRIFT = 500
    REL_APPEND = 2000

    IDS_NAME = 196658
    IDS_INFO = 65551
    ARCHETYPE = 'jumpgate'

    JUMP_EFFECT = 'jump_effect_edge'
    REPUTATION = 'rh_grp'
    GOTO = 'sig8, sig8_to_ber, gate_tunnel_edge'
    LOADOUT = 'jumpgate_rh'

    Y_ROTATE_PER_REL = {
        LEFT: -90,
        RIGHT: 90,
        TOP: 180,
        BOTTOM: 0,
    }

    DEFENCE_ZONE_SIZE = 4000
    DEFENCE_LEVEL = DEFENCE_SIMPLE

    def get_inspace_parameters(self):
        params = super().get_inspace_parameters()
        params.update({
            'jump_effect': self.JUMP_EFFECT,
            'reputation': self.REPUTATION,
            'goto': self.GOTO,
            'loadout': self.LOADOUT,
        })
        return params

    def get_rotate(self):
        return (0, self.Y_ROTATE_PER_REL[self.REL], 0)

    def get_inspace_nickname(self):
        return '{system_name}_jg{index}_test'.format(system_name=self.system.NAME, index=self.INDEX)


class Sattelite(StaticObject):
    pass


class NotDockableObject(StaticObject):
    DEFENCE_LEVEL = None

    def get_inspace_nickname(self):
        return '{system_name}_{alias}_{index}'.format(
            system_name=self.system.NAME,
            alias=self.ALIAS,
            index=self.INDEX
        )


class DockableObject(StaticObject):
    ARCHETYPE = 'depot'
    INTERIOR_CLASS = interior.CustomFileInterior  # custom interior
    INTERIORS_FOLDER = 'GENERATED_INTERIORS'
    DEALERS = None

    INTERIOR_BG1 = None
    INTERIOR_BG2 = None
    BG1_KEY = 'terrain_tiny'
    BG2_KEY = 'terrain_sml'

    ROOM_SUBFOLDER = None

    INTERIOR_DEFINITION_TEMPLATE = '''[Base]
nickname = {base_name}
system = {system_name}
strid_name = {ids_name}
file = {file_location}.ini
BGCS_base_run_by = W02bF44'''

    INTERIOR_LOCATION_GENERATED_TEMPLATE = 'Universe\\{interiors_folder}\\{interior_file_name}'
    INTERIOR_LOCATION_CUSTOM_TEMPLATE = 'Universe\\Systems_MOD\\{system_folder}\\{interior_file_name}'

    AUDIO_PREFIX = None
    SPACE_VOICE = None
    SPACE_COSTUME = None
    RANDOM_ROBOT = False
    ALLOW_SPACE_COSTUME = True

    DEFENCE_LEVEL = DEFENCE_MEDIUM

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.interior = None
        if self.INTERIOR_CLASS:
            subfolder = self.ROOM_SUBFOLDER if self.ROOM_SUBFOLDER else self.system.ROOM_SUBFOLDER
            self.interior = self.INTERIOR_CLASS(self, subfolder)

        self.key = None
        if self.LOCKED_DOCK:
            self.key = LockedDockKey(self)

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
                ids_name=self.IDS_NAME,
                file_location=file_location,
            )
        ]
        if self.INTERIOR_BG1:
            definition.append('{} = {}'.format(self.BG1_KEY, self.INTERIOR_BG1))
        if self.INTERIOR_BG2:
            definition.append('{} = {}'.format(self.BG2_KEY, self.INTERIOR_BG2))
        return SINGLE_DIVIDER.join(definition)

    def get_mbases_content(self):
        if not self.interior:
            raise Exception('%s have not interior' % self.__class__.__name__)
        return self.interior.get_mbase()

    def get_audio_prefix(self):
        if not self.AUDIO_PREFIX:
            raise Exception('unknown audio prefix for %s' % self.__class__.__name__)
        return self.AUDIO_PREFIX

    def get_raw_root_props(self):
        base_name = self.get_base_nickname()
        return {
            'ids_name': self.IDS_NAME,
            'ids_info': self.IDS_INFO,
            'base': base_name,
            'reputation': self.get_faction(),
            'behavior': 'NOTHING',
        }

    def get_root_props(self):
        return SINGLE_DIVIDER.join(['{} = {}'.format(key, value) for key, value in self.get_raw_root_props().items()])

    def get_dock_props(self):
        base_name = self.get_base_nickname()
        props = {
            'ids_name': self.IDS_NAME,
            'ids_info': self.IDS_INFO,
            'base': base_name,
            'dock_with': base_name,
            'reputation': self.get_faction(),
            'behavior': 'NOTHING',
        }

        if self.ALLOW_SPACE_COSTUME:
            if self.RANDOM_ROBOT and not self.SPACE_VOICE and not self.SPACE_COSTUME:
                props['voice'] = SpaceVoice.VOICE_ROBOT
                props['space_costume'] = SpaceCostume.random_robot()
            else:
                props['voice'] = self.SPACE_VOICE if self.SPACE_VOICE else SpaceVoice.DEFAULT
                props['space_costume'] = self.SPACE_COSTUME if self.SPACE_COSTUME else SpaceCostume.DEFAULT

        return SINGLE_DIVIDER.join(['{} = {}'.format(key, value) for key, value in props.items()])


class Dockring(DockableObject):
    ALIAS = 'dockring'
    ARCHETYPE = 'dock_ring'
    REL_DRIFT = 1000
    REL_APPEND = 3000

    INTERIOR_CLASS = None  # should be overrided

    AUDIO_PREFIX = None  # should be overrided

    Y_ROTATE_PER_REL = {
        LEFT: 90,
        RIGHT: -90,
        TOP: 0,
        BOTTOM: 180,
    }

    DEFENCE_ZONE_SIZE = 5000
    DEFENCE_LEVEL = DEFENCE_HIGH
    DEFENCE_ZONE_BACKDRIFT = 2000

    def get_rotate(self):
        return (0, self.Y_ROTATE_PER_REL[self.REL], 0)

    def get_interior_content(self):
        raise Exception('Interior for dock ring planets should be only manual created')


class Station(DockableObject):
    ALIAS = 'station'
    AUDIO_PREFIX = SpaceVoice.STATION


class AbandonedAsteroid(DockableObject):
    AUDIO_PREFIX = SpaceVoice.STATION
    RANDOM_ROBOT = True


class GasMinerOld(Station):
    RANDOM_ROBOT = True

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
            faction=self.get_faction(),
        )

    def get_sattelites(self):
        return [self.get_cargo_pods()]


class SolarPlant(Station):
    ALIAS = 'solar'
    RANDOM_ROBOT = True


class RoidMiner(Station):
    RANDOM_ROBOT = True
    ROTATE_RANDOM = False

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
            faction=self.get_faction(),
            loadout=self.CARGO_PODS_LOADOUT,
        )

    def get_sattelites(self):
        return [self.get_cargo_pods(), self.get_asteroid()]

    def get_rotate(self):
        return 0, 0, 0


class DebrisManufactoring(Station):
    AUDIO_PREFIX = SpaceVoice.FACTORY
    RANDOM_ROBOT = True


class Outpost(DockableObject):
    ALIAS = 'outpost'
    AUDIO_PREFIX = SpaceVoice.OUTPOST


class Prison(DockableObject):
    ALIAS = 'prison'
    AUDIO_PREFIX = SpaceVoice.PRISON


class Shipyard(DockableObject):
    ALIAS = 'shipyard'
    AUDIO_PREFIX = SpaceVoice.SHIPYARD


class TradingBase(DockableObject):
    ALIAS = 'trading'
    AUDIO_PREFIX = SpaceVoice.OUTPOST


class Battleship(DockableObject):
    ALIAS = 'bship'
    AUDIO_PREFIX = SpaceVoice.BATTLESHIP


class RheinlandBattleship(Battleship):
    ARCHETYPE = 'r_battleship'
    LOADOUT = 'rh_battleship_station'


class Freeport(DockableObject):
    ALIAS = 'freeport'
    AUDIO_PREFIX = SpaceVoice.FREEPORT


class JunkerBase(DockableObject):
    ALIAS = 'junker'
    AUDIO_PREFIX = SpaceVoice.OUTPOST


class PirateBase(DockableObject):
    ALIAS = 'pirate'
    AUDIO_PREFIX = SpaceVoice.OUTPOST


class Refinery(DockableObject):
    ALIAS = 'alg'
    AUDIO_PREFIX = SpaceVoice.FACTORY


class Hackable(DockableObject):
    HACKABLE_SOLAR_CLASS = None
    LOCKED_DOCK = True
    DEFENCE_LEVEL = None
    RANDOM_ROBOT = True

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

        return panel.get_space_content(
            space_name=self.get_hacker_name(),
            reputation=self.FACTION,
            position=self.get_hacker_panel_position(),
            relation=self.HACKABLE_SOLAR_CLASS.PANEL_RELATION,
            success_loadout=hacker_name,
        )

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


class HackableBattleship(Hackable):
    AUDIO_PREFIX = SpaceVoice.BATTLESHIP


class LockedBattleship(Station):
    AUDIO_PREFIX = SpaceVoice.BATTLESHIP
    LOCKED_DOCK = True
    ROTATE_RANDOM = True
    RANDOM_ROBOT = True
    DEFENCE_LEVEL = None


class PatrolObjective(SystemObject):
    PATROL_ALIAS = None

    TRACKS_PATROL_HEADING = '[Path]'
    TRACKS_PATROL_NAME = 'name = {name}, {index}'
    TRACKS_PATROL_ITEM = 'pos = {pos}'
    
    def __init__(self, system, index, positions):
        self.system = system
        self.index = index
        self.positions = positions
        self.raw_paths = []

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

    PATROL_ENCOUNTER = 'patrol_police'
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
encounter = {encounter}, 1, 0.330000
faction = {police_faction}, 1.000000'''

    def get_zone_params(self):
        return self.ZONE_PARAMS.format(
            encounter=self.PATROL_ENCOUNTER,
            police_faction=self.system.get_police_faction(),
        )


class HuntersPatrol(PatrolObjective):
    PATROL_ALIAS = 'bounty_hunter'

    HUNTERS_FACTION = faction.BH_GRP
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
        return self.ZONE_PARAMS.format(
            bh_encounter=self.system.get_bounty_hunter_encounter(),
            bh_faction=self.HUNTERS_FACTION,
        )


class PiratePatrol(PatrolObjective):
    PATROL_ALIAS = 'pirate'

    PATROL_TLR_ENCOUNTER = 'patrol_tlr'
    ZONE_PARAMS = '''toughness = 1
density = 1
repop_time = 90
max_battle_size = 3
pop_type = lane_patrol
relief_time = 30
attack_ids = 10
tradelane_attack = 50
mission_eligible = true
density_restriction = 1, patroller
density_restriction = 1, police_patroller
density_restriction = 1, pirate_patroller
density_restriction = 4, lawfuls
density_restriction = 4, unlawfuls
encounter = {patrol_tlr_encounter}, 1, 0.330000
faction = {pirate_faction}, 1.000000'''

    def get_zone_params(self):
        return self.ZONE_PARAMS.format(
            patrol_tlr_encounter=self.PATROL_TLR_ENCOUNTER,
            pirate_faction=self.system.get_pirate_faction(),
        )


class Tradelane(object):

    RING_TEMPLATE = '''[Object]
nickname = {ring_nickname}
ids_name = 260920
ids_info = 66170
pos = {pos}
rotate = {rotate}
archetype = Trade_Lane_Ring
behavior = NOTHING
reputation = {faction}
loadout = trade_lane_ring_li_01
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
        return self.tracks_raw_tradelane.lines[POS_KEY]

    def get_system_object(self):
        template_params = {
            'ring_nickname': self.get_ring_nickname(),
            'pos': '{0}, {1}, {2}'.format(*self.tracks_raw_tradelane.lines[POS_KEY]),
            'rotate': '{0}, {1}, {2}'.format(*self.tracks_raw_tradelane.lines[ROT_KEY]),
            'faction': self.trade_connection.FACTION,
        }

        prev_ring = self.trade_connection.get_prev_ring(self.tradelane_index)
        next_ring = self.trade_connection.get_next_ring(self.tradelane_index)

        extra = []
        if prev_ring:
            extra.append(self.PREV_RING_TEMPLATE.format(prev_ring=prev_ring.get_ring_nickname()))
        if next_ring:
            extra.append(self.NEXT_RING_TEMPLATE.format(next_ring=next_ring.get_ring_nickname()))

        if not prev_ring:
            extra.append(self.RING_SPACE_NAME_TEMPLATE.format(ids_name=self.trade_connection.OBJ_FROM.IDS_NAME))
        elif not next_ring:
            extra.append(self.RING_SPACE_NAME_TEMPLATE.format(ids_name=self.trade_connection.OBJ_FROM.IDS_NAME))

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
        self.police_patrol = self.get_police_patrol()
        if self.police_patrol:
            self.system.add_patrol(self.police_patrol)
        self.bounty_hunter_patrol = self.get_bounty_hunter_patrol()
        if self.bounty_hunter_patrol:
            self.system.add_patrol(self.bounty_hunter_patrol)
        self.attacker_patrols = []

    def get_destination_objects(self):
        if not self.OBJ_FROM and not self.OBJ_TO:
            raise Exception('OBJ_FROM and OBJ_TO is required')

        if not issubclass(self.OBJ_FROM, SystemObject):
            raise Exception('OBJ_FROM %s is not SystemObject' % self.OBJ_FROM)

        if not issubclass(self.OBJ_TO, SystemObject):
            raise Exception('OBJ_TO %s is not SystemObject' % self.OBJ_TO)

        return (self.system.get_system_object_instance(self.OBJ_FROM), self.system.get_system_object_instance(self.OBJ_TO))

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
            tlr_zone_size=TRADELANE_ZONE_SIZE,
            tlr_zone_index=zone_index,
            tlr_distance=TLR_DISTANCE,
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
        if not self.system.ENABLE_POPULATION or not self.TLR_OUTER_ZONE:
            return ''

        return SINGLE_DIVIDER.join([
            self.ZONE_TEMPLATE.format(
                system_name=self.system.NAME.upper(),
                tlr_letter=self.TRADELANE_LETTER,
                pos='{0}, {1}, {2}'.format(*self.tracks_raw_outer_zone.lines[POS_KEY]),
                rotate='{0}, {1}, {2}'.format(*self.tracks_raw_outer_zone.lines[ROT_KEY]),
                size='{0}, {1}, {2}'.format(*self.tracks_raw_outer_zone.lines[SIZE_KEY]),
            ),
            self.get_lawful_population_class().get_tradelane_arriaval_traders_params(),
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
        return PolicePatrol(
            system=self.system,
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
            index=self.system.get_next_bounty_hunter_patrol_id(),
            positions=[
                (obj_from_pos[0], 0, obj_from_pos[2]),
                (obj_from_pos2_x, 0, obj_from_pos2_z),
                (obj_to_pos2_x, 0, obj_to_pos2_z),
                (obj_to_pos[0], 0, obj_to_pos[2]),
            ]
        ) 

    def define_attacker_patrols(self):
        for attacker_base in self.ATTACKED_BY:
            attacker_patrol = self.get_pirate_attacker_patrol(attacker_base)
            self.attacker_patrols.append(attacker_patrol)
            self.system.add_patrol(attacker_patrol)

    def get_pirate_attacker_patrol(self, attacker_base):
        tlrs_len = len(self.tradelanes)

        if tlrs_len <= TLR_SMALL_SIZE_RINGS_COUNT:
            first_tradelane_index = 1
        else:
            first_tradelane_index = randint(1, tlrs_len-2)

        lane1_pos = self.tradelanes[first_tradelane_index].get_tradelane_pos()
        lane2_pos = self.tradelanes[first_tradelane_index+1].get_tradelane_pos()
        attacker_base_pos = self.system.get_object_position(attacker_base)

        return PiratePatrol(
            system=self.system,
            index=self.system.get_next_police_patrol_id(),
            positions=[
                (attacker_base_pos[0], 0, attacker_base_pos[2]),
                (lane1_pos[0], 0, lane1_pos[2]),
                (lane2_pos[0], 0, lane2_pos[2]),
                (attacker_base_pos[0], 0, attacker_base_pos[2]),
            ]
        )



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
        return '{system_name}_F_Trade_Lane_Ring_{letter}0{index}'.format(
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
