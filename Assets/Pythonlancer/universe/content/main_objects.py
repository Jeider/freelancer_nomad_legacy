from random import randint

from universe.content.system_object import SystemObject, TOP, BOTTOM, LEFT, RIGHT, DIRECTIONS, POS_KEY, ROT_KEY, SIZE_KEY
from text.dividers import SINGLE_DIVIDER, DIVIDER


TRADELANE_ZONE_SIZE = 2500

TLR_DISTANCE = 7000

TLR_HUGE_SIZE_RINGS_COUNT = 5
TLR_SMALL_SIZE_RINGS_COUNT = 4


PLANET_CIRCLE_1500 = 'planet_1500_circle'
PLANET_CIRCLE_2000 = 'planet_2000_circle'
PLANET_CIRCLE_2500 = 'planet_2500_circle'
PLANET_CIRCLE_3000 = 'planet_3000_circle'
PLANET_CIRCLE_4000 = 'planet_4000_circle'
PLANET_CIRCLE_5000 = 'planet_5000_circle'

BASIC_Y_ROTATE_PER_REL = {
    LEFT: -90,
    RIGHT: 90,
    TOP: 180,
    BOTTOM: 0,
}


class AppearableObject(SystemObject):
    SPACE_OBJECT_TEMPLATE = None
    SPACE_OBJECT_NAME = None
    ARCHETYPE = None

    ARCHETYPE_TEMPLATE = '''[Object]
nickname = {nickname}
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

    def get_templated_content(self):
        position = self.get_position()
        if not position:
            raise Exception('POS is required for getting object instance when it has appaerance')

        return self.SPACE_OBJECT_TEMPLATE().get_instance(
            new_space_object_name=self.get_space_object_name(),
            move_to=position,
        )

    def get_single_object_content(self):
        content = [
            self.ARCHETYPE_TEMPLATE.format(
                nickname=self.get_inspace_nickname(),
                archetype=self.ARCHETYPE,
                ids_name=self.IDS_NAME,
                ids_info=self.IDS_INFO,
                pos='{}, {}, {}'.format(*self.get_position()),
                rotate='{}, {}, {}'.format(*self.get_rotate()),
            )
        ]
        for key, value in self.get_inspace_parameters().items():
            content.append('{} = {}'.format(key, value))

        return SINGLE_DIVIDER.join(content)

    def get_rotate(self):
        return (0, 0, 0)

    def get_inspace_nickname(self):
        print(self.__class__.__name__)
        raise NotImplementedError

    def get_inspace_parameters(self):
        return {}

    def get_extra_params(self):
        return {}


class StaticObject(AppearableObject):
    ABSTRACT = True

    @classmethod
    def is_abstract(cls):
        return cls.ABSTRACT


class JumpableObject(StaticObject):
    pass


class Sun(StaticObject):
    ALIAS = 'sun'

    ARCHETYPE = 'sun_2000'

    IDS_NAME = 253954
    IDS_INFO = 65541

    SUN_FX = None
    STAR = None
    ATMOSHPERE_RANGE = 11000
    DEATH_ZONE = 7000
    DEATH_DAMAGE = 200000000
    DRAG_ZONE = 10500
    DRAG_MODIFIER = 5

    def get_inspace_parameters(self):
        return {
            'loadout': self.SUN_FX,
            'star': self.STAR,
            'atmosphere_range': self.ATMOSHPERE_RANGE,
        }

    def get_outer_zones(self):
        pass

    def get_inspace_nickname(self):
        return '{system_name}_sun_{index}'.format(system_name=self.system.NAME, index=self.INDEX)



class Planet(StaticObject):
    ALIAS = 'planet'

    PLANET_CIRCLE = None
    ATMOSPHERE_RANGE_APPEND = 200
    DEATH_ZONE_APPEND = 150
    DRAG_ZONE_DAMAGE = 0.1
    DRAG_ZONE_INTERFERENCE = 0.001
    PLANET_CIRCLE_Y_DRIFT = 10


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

    def get_inspace_parameters(self):
        return {
            'jump_effect': self.JUMP_EFFECT,
            'reputation': self.REPUTATION,
            'goto': self.GOTO,
            'loadout': self.LOADOUT,
        }

    def get_rotate(self):
        return (0, BASIC_Y_ROTATE_PER_REL[self.REL], 0)

    def get_inspace_nickname(self):
        return '{system_name}_jg{index}_test'.format(system_name=self.system.NAME, index=self.INDEX)


class Sattelite(StaticObject):
    pass


class DockableObject(StaticObject):
    # debug

    ARCHETYPE = 'depot'

    def get_inspace_nickname(self):
        return '{system_name}_{base_index:02d}'.format(system_name=self.system.NAME, base_index=self.BASE_INDEX)


class Dockring(DockableObject):
    ALIAS = 'dockring'
    ARCHETYPE = 'dock_ring'
    REL_DRIFT = 1000
    REL_APPEND = 3000

    def get_rotate(self):
        return (0, BASIC_Y_ROTATE_PER_REL[self.REL], 0)


class Station(DockableObject):
    ALIAS = 'station'


class Outpost(DockableObject):
    ALIAS = 'outpost'


class Prison(DockableObject):
    ALIAS = 'prison'


class Shipyard(DockableObject):
    ALIAS = 'shipyard'


class TradingBase(DockableObject):
    ALIAS = 'trading'


class JunkerBase(DockableObject):
    ALIAS = 'junker'


class PirateBase(DockableObject):
    ALIAS = 'pirate'


class Refinery(DockableObject):
    ALIAS = 'alg'


class PatrolObjective(SystemObject):
    PATROL_NAME = None

    TRACKS_PATROL_HEADING = '[Path]'
    TRACKS_PATROL_NAME = 'name = {name}, {index}'
    TRACKS_PATROL_ITEM = 'pos = {pos}'

    SPACE_PARAMS = '''
toughness = 1
density = 1
repop_time = 90
max_battle_size = 3
pop_type = lane_patrol
relief_time = 30
attack_ids = 10
tradelane_attack = 50
mission_eligible = true
faction_weight = rx_grp, 10
density_restriction = 1, patroller
density_restriction = 1, police_patroller
density_restriction = 1, pirate_patroller
density_restriction = 4, lawfuls
density_restriction = 4, unlawfuls
encounter = patrol_tlr, 1, 0.330000
faction = rx_grp, 1.000000
'''
    
    def __init__(self, index, positions):
        self.index = index
        self.positions = positions
        self.raw_paths = []

    def get_tracks_request_content(self):
        items = [
            self.TRACKS_PATROL_HEADING,
            self.TRACKS_PATROL_NAME.format(name=self.PATROL_NAME, index=self.index),
        ]

        for pos_item in self.positions:
            items.append(
                self.TRACKS_PATROL_ITEM.format(pos='{0}, {1}, {2}'.format(*pos_item))
            )

        return SINGLE_DIVIDER.join(items)

    def add_raw_path(self, tracks_raw_zone):
        self.raw_paths.append(tracks_raw_zone)

    def get_path_label(self):
        return '{0}{1}'.format(self.PATROL_NAME, self.index)

    def get_system_content(self):
        system_content = []
        for path in self.raw_paths:
            lines = ['[Zone]'] + path.raw_lines
            zone_item = SINGLE_DIVIDER.join(lines) + self.SPACE_PARAMS
            system_content.append(zone_item)

        return DIVIDER.join(system_content)


class PolicePatrol(PatrolObjective):
    PATROL_NAME = 'police'


class HuntersPatrol(PatrolObjective):
    PATROL_NAME = 'bounty_hunter'


class PiratePatrol(PatrolObjective):
    PATROL_NAME = 'pirate'


class Tradelane(object):

    RING_TEMPLATE = '''[Object]
nickname = {ring_nickname}
ids_name = 260920
ids_info = 66170
pos = {pos}
rotate = {rotate}
Archetype = Trade_Lane_Ring_F
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

    OBJ_FROM_EXTRA_DRIFT = 0
    OBJ_TO_EXTRA_DRIFT = 0

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
    ZONE_TEMPLATE = ''

    ZONE_TEMPLATEX = '''[zone]
nickname = Zone_{system_name}_tlr_{tlr_letter}
pos = {pos}
rotate = {rotate}
shape = BOX
size = {size}
sort = 6
toughness = 1
density = 6
repop_time = 15
max_battle_size = 4
pop_type = major_tradelane
relief_time = 15
encounter = tr_grp_rh_transport_tlr, 5, 0.5
faction = tr_grp, 1.00000
encounter = rh_grp_main_trade_tlr, 5, 0.7
faction = rh_grp, 0.50000
faction = rc_grp, 0.50000
encounter = bh_grp_rh_trade_tlr, 5, 0.5
faction = bh_grp, 1.00000
'''

    def __init__(self, system):
        self.system = system
        if not self.TRADELANE_LETTER:
            raise Exception('Tradelane should have a letter')
        self.last_tradelane_index = 1
        self.tradelanes = []
        self.tracks_raw_outer_zone = None
        self.police_patrol = self.get_police_patrol()
        self.system.add_patrol(self.police_patrol)
        self.bounty_hunter_patrol = self.get_bountry_hunter_patrol()
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

        start_tradelane_props = obj_from.get_tradelane_props(side_from, self.OBJ_FROM_EXTRA_DRIFT)
        end_tradelane_props = obj_to.get_tradelane_props(side_to, self.OBJ_TO_EXTRA_DRIFT)

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
        self.tradelanes.append(Tradelane(self, tracks_raw_tradelane, self.last_tradelane_index))
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
        return self.ZONE_TEMPLATE.format(
            system_name=self.system.NAME.upper(),
            tlr_letter=self.TRADELANE_LETTER,
            pos='{0}, {1}, {2}'.format(*self.tracks_raw_outer_zone.lines[POS_KEY]),
            rotate='{0}, {1}, {2}'.format(*self.tracks_raw_outer_zone.lines[ROT_KEY]),
            size='{0}, {1}, {2}'.format(*self.tracks_raw_outer_zone.lines[SIZE_KEY]),
        )

    def get_system_content(self):
        system_content = []
        for tlr in self.tradelanes:
            system_content.append(tlr.get_system_object())

        if self.tracks_raw_outer_zone:
            system_content.append(self.get_tradelane_zone())

        return DIVIDER.join(system_content)

    def get_police_patrol(self):
        obj_from, obj_to = self.get_destination_objects()
        obj_from_pos = self.system.get_object_position(obj_from)
        obj_to_pos = self.system.get_object_position(obj_to)
        return PolicePatrol(
            index=self.system.get_next_police_patrol_id(),
            positions=[
                (obj_from_pos[0], 0, obj_from_pos[2]),
                (obj_to_pos[0], 0, obj_to_pos[2]),
            ]
        ) 

    def get_bountry_hunter_patrol(self):
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
        obj_from, obj_to = self.get_destination_objects()

        tlrs_len = len(self.tradelanes)

        if tlrs_len <= TLR_SMALL_SIZE_RINGS_COUNT:
            first_tradelane_index = 1
        else:
            first_tradelane_index = randint(1, tlrs_len-2)


        lane1_pos = self.tradelanes[first_tradelane_index].get_tradelane_pos()
        lane2_pos = self.tradelanes[first_tradelane_index+1].get_tradelane_pos()
        attacker_base_pos = self.system.get_object_position(attacker_base)

        return PiratePatrol(
            index=self.system.get_next_police_patrol_id(),
            positions=[
                (attacker_base_pos[0], 0, attacker_base_pos[2]),
                (lane1_pos[0], 0, lane1_pos[2]),
                (lane2_pos[0], 0, lane2_pos[2]),
                (attacker_base_pos[0], 0, attacker_base_pos[2]),
            ]
        )







