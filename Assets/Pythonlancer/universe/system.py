from universe.content.system_object import SystemObject
from universe.content.main_objects import RawText, TradeConnection, JumpableObject, DockableObject, StaticObject
from universe.content.zones import Zone, BaseAsteroidZone, NebulaZone, TemplatedNebulaZone
from universe.content.asteroid_definition import AsteroidDefinition
from universe.content.mineable import Mineable, RewardField, Field, RewardsGroup
from universe.content import interior
from universe.content import faction
from universe.content import population

from universe.systems import br_wrw as br_wrw_objects
from universe.systems import rh_ber as rh_ber_content
from universe.systems import sig13 as sig13_content
from universe.systems import rh_biz as rh_biz_content

from text.dividers import DIVIDER

from tools.tracks import Tracks
from tools.system_template import SystemTemplateLoader


TLR_DISTANCE = 7000

VIGNETTE_ZONE_TEMPLATE = '''[Zone]
nickname = Zone_{system_name}_destroy_vignette_{index:02d}
pos = {position}
shape = SPHERE
size = 10000
mission_type = unlawful, lawful
sort = 99.500000
vignette_type = open'''

MULTI_VIGNETTE_ZONE_DRIFT = 6000


class System(object):
    NAME = ''
    CONTENT = None
    TEMPLATE_NAME = None
    ALLOW_SYNC = False

    INTERIOR_DEFAULT_SUBFOLDER = None

    TRACKS_SYSTEM_TEMPLATE = '''[Settings]
system = {system_name}
distance = {tlr_distance}
'''

    FACTION_CODE = None
    ROOM_SUBFOLDER = None

    LAWFUL_FACTIONS = []
    UNLAWFUL_FACTIONS = []

    LAWFUL_POPULATION_CLASS = None
    UNLAWFUL_POPULATION_CLASS = None

    ENABLE_POPULATION = True

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def __init__(self):
        self.template = None

        self.last_police_patrol_id = 0
        self.last_bounty_hunter_patrol_id = 0
        self.last_pirate_patrol_id = 0
        self.police_patrols_list = []
        self.bounty_hunters_patrols_list = []
        self.pirate_patrols_list = []
        self.patrols_db = {}

        self.rewards_groups_list = []
        self.rewards_groups_db = {}
        self.loadouts = []

        self.asteroid_definitions = []
        self.asteroid_definitions_db = {}
        self.templated_nebulas = []
        self.templated_nebulas_db = {}

        self.static_zones = []
        self.asteroid_zones = []
        self.nebula_zones = []
        self.dynamic_zones = []

        self.trade_connections = []

        self.raw_texts = []
        self.statics_list = []
        self.statics_db = {}
        self.mineable = []

        self.keys = []

        if self.CONTENT is not None:
            self.init_content()

    def init_content(self):
        self.process_template()

        for item in self.CONTENT.__dict__.values():
            if not isinstance(item, type):
                continue

            if issubclass(item, AsteroidDefinition) and not item.ABSTRACT:
                self.add_asteroid_definition(item)
                continue

            if not issubclass(item, RewardsGroup) and not issubclass(item, SystemObject):
                continue

            if (item.ABSTRACT and item != br_wrw_objects.WarwickSysObject) or item == br_wrw_objects.WarwickSysObject:
                continue

            if issubclass(item, RewardsGroup):
                reward_group_instance = item(self)
                self.rewards_groups_list.append(reward_group_instance)
                self.rewards_groups_db[item.__name__] = reward_group_instance
                continue

            if not isinstance(item, type) or not issubclass(item, SystemObject):
                continue

            if item in (TradeConnection, DockableObject, TradeConnection):
                continue

            if issubclass(item, RawText):
                self.add_raw_text(item)
            elif issubclass(item, StaticObject):
                self.add_static_object(item)
            elif issubclass(item, Mineable):
                self.add_mineable(item)
            elif issubclass(item, TradeConnection):
                self.add_trade_connection(item)
            elif issubclass(item, Zone):
                self.add_static_zone(item)

        self.process_reward_groups()

        system_content = []

        for raw_text in self.raw_texts:
            system_content.append(raw_text.get_system_content())

        for asteroid_zone in self.asteroid_zones:
            system_content.append(asteroid_zone.get_asteroid_definition_header())

        for nebula_zone in self.nebula_zones:
            system_content.append(nebula_zone.get_nebula_definition_header())

        for app_obj in self.get_appearable_objects():
            system_content.append(app_obj.get_system_content())

        for mineable_obj in self.get_mineable_objects():
            system_content.append(mineable_obj.get_system_content())

        for static_zone in self.static_zones:
            system_content.append(static_zone.get_system_content())

        for dynamic_zone in self.dynamic_zones:
            system_content.append(dynamic_zone.get_system_content())

        if len(self.trade_connections) > 0:
            self.generate_tradelanes()
            self.define_attacker_patrols()

            for item in self.trade_connections:
                system_content.append(item.get_system_content())

        self.generate_patrols()

        if self.ENABLE_POPULATION:
            for patrol in self.get_patrols_list():
                system_content.append(patrol.get_system_content())

        system_content.extend(self.get_mission_vignettes())

        self.system_content_str = DIVIDER.join(system_content)

    def add_trade_connection(self, item):
        self.trade_connections.append(item(self))

    def add_raw_text(self, item):
        self.raw_texts.append(item(self))

    def add_static_object(self, item):
        static = item(self)
        self.statics_list.append(static)
        self.statics_db[static.get_full_alias()] = static

        if len(static.ASTEROID_ZONES) > 0:
            ast_exclusion_zone_name = static.get_ast_exclusion_zone_name()
            for ast_zone in static.ASTEROID_ZONES:
                self.asteroid_definitions_db[ast_zone.ASTEROID_DEFINITION_CLASS.NAME].add_exclusion(ast_exclusion_zone_name)

        if len(static.NEBULA_ZONES) > 0:
            nebula_exclusion_zone_name = static.get_nebula_exclusion_zone_name()
            for neb_zone in static.NEBULA_ZONES:
                self.templated_nebulas_db[neb_zone.FILE_NAME].add_exclusion(nebula_exclusion_zone_name, static.EXCLUSION_PARAMS)

        self.dynamic_zones.extend(static.get_dynamic_zones())

        if issubclass(static.__class__, DockableObject) and static.LOCKED_DOCK:
            self.keys.append(static.key)

    def get_static_by_class(self, item_class):
        return self.statics_db[item_class.get_full_alias()]

    def add_mineable(self, item):
        self.mineable.append(item(self))

    def add_static_zone(self, item):
        zone = item(self)
        if issubclass(item, BaseAsteroidZone):
            self.asteroid_zones.append(zone)
        elif issubclass(item, NebulaZone):
            self.nebula_zones.append(zone)
            if issubclass(item, TemplatedNebulaZone):
                self.templated_nebulas.append(zone)
                self.templated_nebulas_db[zone.FILE_NAME] = zone

        self.static_zones.append(zone)

    def add_asteroid_definition(self, item):
        definition = item(self)
        self.asteroid_definitions.append(definition)
        self.asteroid_definitions_db[definition.NAME] = definition

    def get_dockable_objects(self):
        return [static for static in self.statics_list if issubclass(static.__class__, DockableObject)]

    def get_interiors_data(self):
        interior_definitions = []
        interior_files = {}
        mbases_content = []

        for static in self.get_dockable_objects():
            mbases_content.append(static.get_mbases_content())
            interior_definitions.append(static.get_interior_definition())
            if not static.INTERIOR_CLASS.CUSTOM_INTERIOR_FILE:
                interior_files[static.get_interior_file_name()] = static.get_interior_content()

        return interior_definitions, interior_files, mbases_content

    def process_template(self):
        if self.TEMPLATE_NAME is None:
            raise Exception('unknown template')

        self.template = SystemTemplateLoader.get_template(self.TEMPLATE_NAME)

    def get_object_position(self, system_object_class):
        return self.template.get_item_pos(system_object_class.get_full_alias())

    def get_system_object_instance(self, system_object_class):
        return self.statics_db[system_object_class.get_full_alias()]

    def process_reward_groups(self):
        for rewards_group in self.rewards_groups_list:
            self.loadouts += rewards_group.get_loadouts()

    def get_rewards_group_by_class(self, reward_group_class):
        return self.rewards_groups_db[reward_group_class.__name__]

    def get_next_police_patrol_id(self):
        self.last_police_patrol_id += 1
        return self.last_police_patrol_id

    def get_next_bounty_hunter_patrol_id(self):
        self.last_bounty_hunter_patrol_id += 1
        return self.last_bounty_hunter_patrol_id

    def get_next_pirate_patrol_id(self):
        self.last_pirate_patrol_id += 1
        return self.last_pirate_patrol_id

    def add_patrol(self, patrol):
        self.patrols_db[patrol.get_path_label()] = patrol

    def get_patrols_list(self):
        return self.patrols_db.values()

    def get_appearable_objects(self):
        return [item for item in self.statics_list if item.has_appearance()]

    def get_mineable_objects(self):
        return self.mineable

    @classmethod
    def get_tracks_request_content(cls):
        return cls.TRACKS_SYSTEM_TEMPLATE.format(
            system_name=cls.NAME,
            tlr_distance=TLR_DISTANCE,
        )

    def get_tradelane_creation_request(self):
        request_items = [self.get_tracks_request_content()] + [item.get_tracks_request_content() for item in self.trade_connections]
        return DIVIDER.join(request_items)

    def get_tradelane_creation_response(self):
        tradelanes_request = self.get_tradelane_creation_request()
        return Tracks.get_tracks(tradelanes_request)

    def get_path_creation_request(self):
        request_items = [self.get_tracks_request_content()] + [patrol.get_tracks_request_content() for patrol in self.get_patrols_list()]
        return DIVIDER.join(request_items)

    def get_path_creation_response(self):
        path_request = self.get_path_creation_request()
        return Tracks.get_tracks(path_request)

    def generate_tradelanes(self):
        tlr_response = self.get_tradelane_creation_response()

        trade_connection_index = 0
        for response_item in tlr_response:
            if response_item.is_object():
                self.trade_connections[trade_connection_index].add_tradelane(response_item)
            if response_item.is_tlr_zone():
                self.trade_connections[trade_connection_index].set_tradelane_zone(response_item)
                trade_connection_index += 1

    def define_attacker_patrols(self):
        for item in self.trade_connections:
            item.define_attacker_patrols()

    def generate_patrols(self):
        if len(self.patrols_db) == 0:
            return

        patrols_response = self.get_path_creation_response()

        for response_item in patrols_response:
            self.patrols_db[response_item.get_path_label()].add_raw_path(response_item)

    def get_police_faction(self):
        raise NotImplementedError

    def get_bounty_hunter_encounter(self):
        raise NotImplementedError
    
    def get_pirate_faction(self):
        raise NotImplementedError

    def get_mission_vignettes(self):
        entries = []
        index = 1

        for position in self.template.get_single_mission_vignettes_positions():
            entries.append(
                VIGNETTE_ZONE_TEMPLATE.format(
                    system_name=self.NAME,
                    index=index,
                    position='{}, {}, {}'.format(*position),
                )
            )
            index += 1

        drift = abs(MULTI_VIGNETTE_ZONE_DRIFT)

        multi_drift_map = [
            (-drift, 0),
            (drift, 0),
            (0, -drift),
            (0, drift),
        ]

        for pos_x, pos_y, pos_z in self.template.get_multiple_mission_vignettes_positions():
            for drift_x, drift_z in multi_drift_map:
                entries.append(
                    VIGNETTE_ZONE_TEMPLATE.format(
                        system_name=self.NAME,
                        index=index,
                        position='{}, {}, {}'.format(pos_x + drift_x, pos_y, pos_z + drift_z),
                    )
                )
                index += 1

        return entries


class BretoniaSystem(object):

    FACTION_CODE = None

    def get_faction(self):
        if self.FACTION_CODE is None:
            raise Exception('unknown faction for system %s' % self.NAME)
        return self.FACTION_CODE



class RheinlandSystem(object):

    FACTION_CODE = None
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_RH

    LAWFUL_FACTIONS = [
        faction.RH_GRP,
        faction.BH_GRP,
        faction.RC_GRP,
        faction.TR_GRP,
    ]
    UNLAWFUL_FACTIONS = [
        faction.RX_GRP,
        faction.PI_GRP,
        faction.JUNK_GRP,
    ]

    LAWFUL_POPULATION_CLASS = population.RheinlandLegalPopulation
    UNLAWFUL_POPULATION_CLASS = None

    def get_faction(self):
        if self.FACTION_CODE is None:
            raise Exception('unknown faction for system %s' % self.NAME)
        return self.FACTION_CODE

    def get_police_faction(self):
        return faction.RH_GRP

    def get_bounty_hunter_encounter(self):
        return 'bh_grp_rh_patrol'
    
    def get_pirate_faction(self):
        return faction.RX_GRP


class rh_mnh(System):
    NAME = 'Rh_Mnh'


class rh_biz(RheinlandSystem, System):
    NAME = 'rh_biz'
    TEMPLATE_NAME = 'rh_biz'
    FACTION_CODE = faction.RH_GRP
    CONTENT = rh_biz_content

    SYSTEM_FOLDER = 'RH_BIZMARK'
    ALLOW_SYNC = True


class rh_stut(System):
    NAME = 'Rh_stut'


class rh_ber(RheinlandSystem, System):
    NAME = 'rh_ber'
    TEMPLATE_NAME = 'rh_ber'
    FACTION_CODE = faction.RH_GRP
    CONTENT = rh_ber_content

    SYSTEM_FOLDER = 'RH_BERLIN'
    ALLOW_SYNC = True

class sig8(System):
    NAME = 'sig8'


class om15(System):
    NAME = 'om15'


# rheinland -  temporary
class sig13(RheinlandSystem, System): 
    NAME = 'sig13'
    TEMPLATE_NAME = 'sig13'
    FACTION_CODE = 'rh_grp'
    CONTENT = sig13_content

    SYSTEM_FOLDER = 'SIGMA13'
    ALLOW_SYNC = True
    ENABLE_POPULATION = True

    LAWFUL_FACTIONS = [
        faction.RH_GRP,
        faction.LI_GRP,
        faction.BH_GRP,
        faction.RC_GRP,
        faction.LC_GRP,
        faction.TR_GRP,
    ]
    UNLAWFUL_FACTIONS = [
        faction.RX_GRP,
        faction.LX_GRP,
        faction.PI_GRP,
        faction.JUNK_GRP,
    ]


class li_cal(System):
    NAME = 'li_cal'


class sig22(System):
    NAME = 'sig22'


class li_mnh(System):
    NAME = 'li_mnh'


class li_for(System):
    NAME = 'li_for'


class sig17(System):
    NAME = 'sig17'


class li_col(System):
    NAME = 'li_col'


class tau31(System):
    NAME = 'tau31'


class br_wrw(BretoniaSystem, System):
    NAME = 'br_wrw'
    FACTION_CODE = 'br_grp'
    # CONTENT = br_wrw_objects


class tau29(System):
    NAME = 'tau29'


class br_cam(System):
    NAME = 'br_cam'


class tau37(System):
    NAME = 'tau37'


class br_avl(System):
    NAME = 'br_avl'


class sig42(System):
    NAME = 'sig42'


class tau23(System):
    NAME = 'tau23'


class ku_ksu(System):
    NAME = 'ku_ksu'


class tau4(System):
    NAME = 'tau4'


class ku_hns(System):
    NAME = 'ku_hns'


class ku_tgk(System):
    NAME = 'ku_tgk'


class ku_hkd(System):
    NAME = 'ku_hkd'


class om7(System):
    NAME = 'om7'


class co_cur(System):
    NAME = 'co_cur'


class co_mad(System):
    NAME = 'co_mad'


class co_val(System):
    NAME = 'co_val'


class co_och(System):
    NAME = 'co_och'


class co_cad(System):
    NAME = 'co_cad'


class om13(System):
    NAME = 'om13'


class tau26(System):
    NAME = 'tau26'


class om11(System):
    NAME = 'om11'


class br_uls(System):
    NAME = 'br_uls'


class upsilon1(System):
    NAME = 'upsilon1'


class upsilon2(System):
    NAME = 'upsilon2'


class omicron1(System):
    NAME = 'omicron1'


class omicron2(System):
    NAME = 'omicron2'
