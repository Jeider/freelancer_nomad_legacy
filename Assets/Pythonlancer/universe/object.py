from text.dividers import SINGLE_DIVIDER, DIVIDER
from random import randint

TOP = 'top'
BOTTOM = 'bottom'
LEFT = 'left'
RIGHT = 'right'

DIRECTIONS = (TOP, BOTTOM, LEFT, RIGHT)
X_AXIS = (LEFT, RIGHT)
Z_AXIS = (TOP, BOTTOM)
POS_Y_FORCE_VALUE = 0

MIN_REL_APPEND = 500
TRADELANE_ZONE_SIZE = 2500

POS_KEY = 'pos'
ROT_KEY = 'rotate'
SIZE_KEY = 'size'

TLR_DISTANCE = 7000

TLR_HUGE_SIZE_RINGS_COUNT = 5
TLR_SMALL_SIZE_RINGS_COUNT = 4


def get_reversed_direction(direction):
    if direction == TOP:
        return BOTTOM

    if direction == BOTTOM:
        return TOP

    if direction == LEFT:
        return RIGHT

    if direction == RIGHT:
        return LEFT

    raise Exception('unknown direction %s' % direction)


class SystemObject(object):
    POS = None
    REL = None

    IDS_NAME = 1  # TEMPORARY

    REL_APPEND = 3000  # distance between object and tradelane
    REL_DRIFT = 0  # move initial pos for tradelane start point


    @classmethod
    def get_position(cls):
        if not cls.POS:
            raise Exception('POS is not defined')

        try:
            if not isinstance(cls.POS[0], int) or not isinstance(cls.POS[1], int) or not isinstance(cls.POS[2], int):
                raise Exception('POS must containt only integers')
        except IndexError:
            raise Exception('Not enough items in POS')

        return cls.POS

    @classmethod
    def get_rel(cls):
        if not cls.REL:
            raise Exception('REL is required')

        if cls.REL not in DIRECTIONS:
            raise Exception('REL %s is not correct direction' % cls.REL)

        return cls.REL

    @classmethod
    def get_rel_drift(cls):
        return cls.REL_DRIFT

    @classmethod
    def get_rel_append(cls):
        if cls.REL_APPEND < MIN_REL_APPEND:
            raise Exception('Too small REL_APPEND')
        return cls.REL_APPEND

    @classmethod
    def get_tradelane_props(cls, tradelane_side):
        tradelane_side = get_reversed_direction(tradelane_side)

        pos_x, _, pos_z = cls.get_position()

        rel_append = cls.get_rel_append()
        rel_drift = cls.get_rel_drift()
        rel = cls.get_rel()

        if rel_drift > 0:
            if rel == LEFT:
                pos_x += rel_drift
            if rel == RIGHT:
                pos_x -= rel_drift
            if rel == TOP:
                pos_z += rel_drift
            if rel == BOTTOM:
                pos_z -= rel_drift

        if tradelane_side == LEFT:
            pos_x -= rel_append
        if tradelane_side == RIGHT:
            pos_x += rel_append
        if tradelane_side == TOP:
            pos_z -= rel_append
        if tradelane_side == BOTTOM:
            pos_z += rel_append

        return pos_x, POS_Y_FORCE_VALUE, pos_z, cls.IDS_NAME

    def __init__(self, system):
        self.system = system


class AppearableObject(SystemObject):
    SPACE_OBJECT_TEMPLATE = None
    SPACE_OBJECT_NAME = None

    def has_appearance(self):
        return self.SPACE_OBJECT_TEMPLATE is not None

    def get_system_content(self):
        if not self.POS:
            raise Exception('POS is required for getting object instance when it has appaerance')

        return self.SPACE_OBJECT_TEMPLATE().get_instance(
            new_space_object_name=self.SPACE_OBJECT_NAME,
            move_to=self.POS,
        )


class StaticObject(AppearableObject):
    ABSTRACT = True

    @classmethod
    def is_abstract(cls):
        return cls.ABSTRACT


class JumpableObject(StaticObject):
    pass


class Jumpgate(JumpableObject):
    ABSTRACT = False

    REL_DRIFT = 500
    REL_APPEND = 2000


class Sattelite(StaticObject):
    ABSTRACT = False


class DockableObject(AppearableObject):
    pass


class Dockring(DockableObject):
    ABSTRACT = False

    REL_DRIFT = 1000
    REL_APPEND = 5000



class Station(DockableObject):
    ABSTRACT = False


class TradeStation(DockableObject):
    ABSTRACT = False


class PirateBase(DockableObject):
    ABSTRACT = False


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

    @classmethod
    def get_destination_objects(cls):
        if not cls.OBJ_FROM and not cls.OBJ_TO:
            raise Exception('OBJ_FROM and OBJ_TO is required')

        if not issubclass(cls.OBJ_FROM, SystemObject):
            raise Exception('OBJ_FROM %s is not SystemObject' % cls.OBJ_FROM)

        if not issubclass(cls.OBJ_TO, SystemObject):
            raise Exception('OBJ_TO %s is not SystemObject' % cls.OBJ_TO)

        return (cls.OBJ_FROM, cls.OBJ_TO)

    @classmethod
    def get_sides(cls):
        if not cls.SIDE_FROM or not cls.SIDE_TO:
            raise Exception('SIDE_FROM and SIDE_TO is required')

        if cls.SIDE_FROM not in DIRECTIONS:
            raise Exception('SIDE_FROM %s isnt correct direction' % cls.SIDE_FROM)

        if cls.SIDE_TO not in DIRECTIONS:
            raise Exception('SIDE_TO %s isnt correct direction' % cls.SIDE_TO)

        return (cls.SIDE_FROM, cls.SIDE_TO)

    @classmethod
    def get_side_tradelanes_props(cls):
        obj_from, obj_to = cls.get_destination_objects()
        side_from, side_to = cls.get_sides()

        start_tradelane_props = obj_from.get_tradelane_props(side_from)
        end_tradelane_props = obj_to.get_tradelane_props(side_to)

        return start_tradelane_props, end_tradelane_props

    @classmethod
    def get_tracks_request_content(cls, zone_index=1):
        start_tradelane_props, end_tradelane_props = cls.get_side_tradelanes_props()
        return cls.TRACKS_TLR_TEMPLATE.format(
            first_tlr_props='{0}, {1}, {2}, {3}'.format(*start_tradelane_props),
            last_tlr_props='{0}, {1}, {2}, {3}'.format(*end_tradelane_props),
            tlr_zone_size=TRADELANE_ZONE_SIZE,
            tlr_zone_index=zone_index,
            tlr_distance=TLR_DISTANCE,
        )

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
        return PolicePatrol(
            index=self.system.get_next_police_patrol_id(),
            positions=[
                (obj_from.POS[0], 0, obj_from.POS[2]),
                (obj_to.POS[0], 0, obj_to.POS[2]),
            ]
        ) 

    def get_bountry_hunter_patrol(self):
        patrol_rel = self.HUNTER_DEFENCE_REL
        if patrol_rel is None:
            return

        obj_from, obj_to = self.get_destination_objects()
        obj_from_pos2_x = obj_from.POS[0]
        obj_from_pos2_z = obj_from.POS[2]
        obj_to_pos2_x = obj_to.POS[0]
        obj_to_pos2_z = obj_to.POS[2]

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
                (obj_from.POS[0], 0, obj_from.POS[2]),
                (obj_from_pos2_x, 0, obj_from_pos2_z),
                (obj_to_pos2_x, 0, obj_to_pos2_z),
                (obj_to.POS[0], 0, obj_to.POS[2]),
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

        return PiratePatrol(
            index=self.system.get_next_police_patrol_id(),
            positions=[
                (attacker_base.POS[0], 0, attacker_base.POS[2]),
                (lane1_pos[0], 0, lane1_pos[2]),
                (lane2_pos[0], 0, lane2_pos[2]),
                (attacker_base.POS[0], 0, attacker_base.POS[2]),
            ]
        )






class AsteroidField(SystemObject):
    CORE_EXCLUSION_SIZE = 500
    OUTER_SIZE = 2000
    ASTEROID_ARCHETYPE = 'om15_mineast_super'
    









