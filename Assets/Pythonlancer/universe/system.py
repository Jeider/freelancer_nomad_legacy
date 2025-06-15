import pathlib

from universe.content.system_object import SystemObject
from universe.content.main_objects import RawText, TradeConnection, JumpableObject, DockableObject, StaticObject
from universe.content import zones
from universe.content.mineable import Mineable, RewardsGroup
from universe.content import interior
from universe.content import population
from universe import connection
from universe.base import Base

from text.dividers import SINGLE_DIVIDER, DIVIDER

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

SYSTEM_TEMPLATE = '''[system]
nickname = {nickname}
file = {systems_root}\{folder}\{nickname}.ini
pos = {navmap_pos}
msg_id_prefix = {msg_prefix}
visit = 0
strid_name = {ids_name}
ids_info = {ids_info}
NavMapScale = {navmap_scale}
'''

MULTI_VIGNETTE_ZONE_DRIFT = 6000
VISIT_DEFAULT = 0
VISIT_STORY = 128

STORY_CONTENT_DIVIDER = 'nickname = divider'


class SiriusSystem:
    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)


class System:
    NAME = ''
    RU_NAME = ''
    CONTENT = None
    TEMPLATE_NAME = None
    ALLOW_SYNC = False
    NAVMAP_POS = '0, 0'
    NAVMAP_SCALE = 1.0
    SYSTEM_FOLDER = None
    SYSTEMS_ROOT = 'SYSTEMS_MOD'
    IS_STORY = False
    VISIT = 0
    SCAN_JUMP = True
    SPACE_FARCLIP = 100000

    INTERIOR_DEFAULT_SUBFOLDER = None

    TRACKS_SYSTEM_TEMPLATE = '''[Settings]
system = {system_name}
distance = {tlr_distance}
'''

    FACTION_CODE = None
    ROOM_SUBFOLDER = None

    LAWFUL_FACTIONS = []
    UNLAWFUL_FACTIONS = []

    FIRST_LAWFUL_POPULATION_CLASS = None
    FIRST_UNLAWFUL_POPULATION_CLASS = None

    SECOND_LAWFUL_POPULATION_CLASS = None
    SECOND_UNLAWFUL_POPULATION_CLASS = None

    JUMP_EFFECT = None

    ENABLE_POPULATION = True

    def __init__(self, core, universe, ids):
        self.core = core
        self.universe_manager = universe
        self.ids = ids
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

        self.trade_letters = []

        self.trade_connections = []
        self.trade_connections_db = {}

        self.raw_texts = []
        self.statics_list = []
        self.statics_db = {}
        self.mineable = []

        self.jumpable = []
        self.jumpgates_db = {}
        self.lawful_connections = []

        self.keys = []

        self.ids_name = ids.new_name(self.RU_NAME)
        self.ids_info = ids.new_name(self.RU_NAME)  # TODO: change

        self.bases_db = {}
        self.bases_list = []

        self.process_content()

    def process_content(self):
        if self.have_dynamic_content():
            self.process_template()
            self.init_dynamic_content()
            self.post_process_dynamic_content()

    def have_dynamic_content(self):
        return self.CONTENT is not None

    def init_dynamic_content(self):
        for item in self.CONTENT.__dict__.values():
            if not isinstance(item, type):
                continue

            if not issubclass(item, RewardsGroup) and not issubclass(item, SystemObject):
                continue

            if item.ABSTRACT:
                continue

            item.SYSTEM_NAME = self.NAME

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
            elif issubclass(item, zones.Zone):
                self.add_static_zone(item)

        self.process_reward_groups()

    def post_process_dynamic_content(self):
        for the_connect in self.trade_connections:
            destinations = the_connect.get_destination_objects()
            destinations[0].add_connection(the_connect)
            destinations[1].add_connection(the_connect)
            for attacker in the_connect.get_attacker_objects():
                attacker.add_connection(the_connect)
        #
        # for static in self.get_dockable_objects():
        #     for connect in static.get_force_connections():
        #         static.add_connection(connect)

    def init_jumpgates(self):
        for jumpable_item in self.jumpable:
            jumpable_item.init_connection()
            if jumpable_item.CONNECTION_KIND == connection.CONNECTION_LAWFUL:
                self.lawful_connections.append(jumpable_item.target_system)
                self.jumpgates_db[jumpable_item.TARGET_SYSTEM_NAME] = jumpable_item

    def get_jumpgate_instance(self, system_name):
        return self.jumpgates_db[system_name]

    def load_trade_connections(self):
        if len(self.trade_connections) > 0:
            self.generate_tradelanes()

            for item in self.trade_connections:
                item.init_patrols()

    def get_dynamic_content(self):
        system_content = []

        for raw_text in self.raw_texts:
            system_content.append(raw_text.get_system_content())

        system_content.append(self.get_encounters_definitions())

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
            for item in self.trade_connections:
                system_content.append(item.get_system_content())

        self.generate_patrols()

        if self.ENABLE_POPULATION:
            for patrol in self.get_patrols_list():
                system_content.append(patrol.get_system_content())

        system_content.extend(self.get_mission_vignettes())

        return DIVIDER.join(system_content)

    def get_content(self):
        return self.get_dynamic_content()

    def get_ids_name(self):
        return self.ids_name.id

    def get_ids_info(self):
        return self.ids_info.id

    def get_universe_definition(self):
        return SYSTEM_TEMPLATE.format(
            nickname=self.NAME,
            systems_root=self.SYSTEMS_ROOT,
            folder=self.SYSTEM_FOLDER,
            msg_prefix=self.get_system_msg(),
            navmap_pos=self.NAVMAP_POS,
            navmap_scale=self.NAVMAP_SCALE,
            ids_name=self.get_ids_name(),
            ids_info=self.get_ids_info(),
        )

    def get_random_hacker_panel(self):
        return self.universe_manager.get_random_hacker_panel()

    def get_universe_root(self):
        return self.universe_manager.get_universe_root()

    def add_trade_connection(self, item):
        trade_conn = item(self)
        if trade_conn.TRADELANE_LETTER in self.trade_letters:
            raise Exception(f'{self} already have letter {trade_conn.TRADELANE_LETTER}')
        self.trade_letters.append(trade_conn.TRADELANE_LETTER)
        self.trade_connections.append(trade_conn)
        self.trade_connections_db[item.__name__]  = trade_conn

    def add_raw_text(self, item):
        self.raw_texts.append(item(self))

    def add_static_object(self, item):
        static = item(self)
        self.statics_list.append(static)
        self.statics_db[static.get_full_alias()] = static
        self.loadouts += static.get_loadouts()

        if len(static.ASTEROID_ZONES) > 0:
            ast_exclusion_zone_name = static.get_ast_exclusion_zone_name()
            for ast_zone in static.ASTEROID_ZONES:
                self.asteroid_definitions_db[ast_zone.get_full_alias()].add_exclusion(ast_exclusion_zone_name)

        if len(static.NEBULA_ZONES) > 0:
            nebula_exclusion_zone_name = static.get_nebula_exclusion_zone_name()
            for neb_zone in static.NEBULA_ZONES:
                self.templated_nebulas_db[neb_zone.get_full_alias()].add_exclusion(nebula_exclusion_zone_name, static.EXCLUSION_PARAMS)

        self.dynamic_zones.extend(static.get_dynamic_zones())

        if issubclass(static.__class__, DockableObject) and static.LOCKED_DOCK:
            self.keys.append(static.key)

        if issubclass(static.__class__, JumpableObject):
            self.jumpable.append(static)

    def get_static_by_class(self, item_class):
        return self.statics_db[item_class.get_full_alias()]

    def get_trade_connection_by_class(self, item_class):
        return self.trade_connections_db[item_class.__name__]

    def add_mineable(self, item):
        self.mineable.append(item(self))

    def add_static_zone(self, item):
        zone = item(self)
        if issubclass(item, zones.BaseAsteroidZone):
            self.asteroid_zones.append(zone)
            if item.ASTEROID_DEFINITION_CLASS is not None:
                definition = item.ASTEROID_DEFINITION_CLASS(self, zone)
                self.asteroid_definitions.append(definition)
                self.asteroid_definitions_db[zone.get_full_alias()] = definition

        elif issubclass(item, zones.NebulaZone):
            self.nebula_zones.append(zone)
            self.templated_nebulas.append(zone)
            self.templated_nebulas_db[zone.get_full_alias()] = zone

        self.static_zones.append(zone)

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

    def get_faction(self):
        if self.FACTION_CODE is None:
            raise Exception('unknown faction for system %s' % self.__class__.__name__)
        return self.FACTION_CODE

    def get_lawful_factions(self):
        factions = self.FIRST_LAWFUL_POPULATION_CLASS.get_lawful_factions()
        if self.SECOND_LAWFUL_POPULATION_CLASS:
            factions += self.SECOND_LAWFUL_POPULATION_CLASS.get_lawful_factions()
        return factions

    def get_unlawful_factions(self):
        factions = self.FIRST_UNLAWFUL_POPULATION_CLASS.get_unlawful_factions()
        if self.SECOND_LAWFUL_POPULATION_CLASS:
            factions += self.SECOND_UNLAWFUL_POPULATION_CLASS.get_unlawful_factions()
        return factions

    def get_encounters_definitions(self):
        pop_classes = [
            self.FIRST_LAWFUL_POPULATION_CLASS,
            self.FIRST_UNLAWFUL_POPULATION_CLASS,
            self.SECOND_LAWFUL_POPULATION_CLASS,
            self.SECOND_UNLAWFUL_POPULATION_CLASS,
        ]

        encounters = []
        encounter_names = set()

        for pop in pop_classes:
            if not pop:
                continue
            for pop_enc in pop.get_encounter_definitions():
                enc_name = pop_enc.get_nickname()
                if enc_name not in encounter_names:
                    encounters.append(pop_enc)
                    encounter_names.add(enc_name)

        return DIVIDER.join([enc.get_definition() for enc in encounters])

    def get_point_pos(self, name):
        return self.template.get_item_pos(name)

    def get_point_rotate(self, name):
        return self.template.get_item_rotate(name)

    @classmethod
    def get_system_msg(cls):
        return f'gcs_refer_system_{cls.NAME}'

    @classmethod
    def get_system_msg_relative(cls):
        return f'gcs_refer_system_{cls.NAME}-'

    def add_base(self, system_object):
        the_base = Base(
            self.core,
            self,
            system_object=system_object,
        )

        base_name = system_object.get_base_nickname()

        self.bases_db[base_name] = the_base
        self.bases_list.append(the_base)

        self.universe_manager.bases_db[base_name] = the_base
        self.universe_manager.bases_list.append(the_base)

        system_object.set_base(the_base)


class RheinlandFirst:
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_RH

    FIRST_LAWFUL_POPULATION_CLASS = population.RheinlandLegalPopulation
    FIRST_UNLAWFUL_POPULATION_CLASS = population.RheinlandPiratePopulation


class RheinlandSecond:
    SECOND_LAWFUL_POPULATION_CLASS = population.RheinlandLegalPopulation
    SECOND_UNLAWFUL_POPULATION_CLASS = population.RheinlandPiratePopulation


class LibertyFirst:
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_LI

    FIRST_LAWFUL_POPULATION_CLASS = population.LibertyLegalPopulation
    FIRST_UNLAWFUL_POPULATION_CLASS = population.LibertyPiratePopulation


class LibertySecond:
    SECOND_LAWFUL_POPULATION_CLASS = population.LibertyLegalPopulation
    SECOND_UNLAWFUL_POPULATION_CLASS = population.LibertyPiratePopulation


class BretoniaFirst:
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_BR

    FIRST_LAWFUL_POPULATION_CLASS = population.BretoniaLegalPopulation
    FIRST_UNLAWFUL_POPULATION_CLASS = population.BretoniaPiratePopulation


class BretoniaSecond:
    SECOND_LAWFUL_POPULATION_CLASS = population.BretoniaLegalPopulation
    SECOND_UNLAWFUL_POPULATION_CLASS = population.BretoniaPiratePopulation


class KusariFirst:
    ROOM_SUBFOLDER = interior.ROOM_FOLDER_KU

    FIRST_LAWFUL_POPULATION_CLASS = population.KusariLegalPopulation
    FIRST_UNLAWFUL_POPULATION_CLASS = population.KusariPiratePopulation


class KusariSecond:
    SECOND_LAWFUL_POPULATION_CLASS = population.KusariLegalPopulation
    SECOND_UNLAWFUL_POPULATION_CLASS = population.KusariPiratePopulation


class StorySystem(System):
    DIRECT_TEMPLATE_NAME = None
    SYSTEMS_ROOT = 'SPECIAL'

    ENABLE_POPULATION = False

    VISIT = VISIT_STORY
    IS_STORY = True
    SCAN_JUMP = False

    def get_direct_template_source(self):
        current_path = pathlib.Path().resolve()
        return current_path.parent.parent / 'DATA' / 'UNIVERSE' / self.SYSTEMS_ROOT / self.SYSTEM_FOLDER

    def process_template(self):
        if self.DIRECT_TEMPLATE_NAME is None:
            raise Exception('unknown direct template')

        self.template = SystemTemplateLoader.get_template(
            self.DIRECT_TEMPLATE_NAME,
            source_path=self.get_direct_template_source(),
        )

    def get_static_content(self):
        content = SystemTemplateLoader.get_template_text_content(
            self.DIRECT_TEMPLATE_NAME,
            source_path=self.get_direct_template_source(),
        )

        new_lines = []

        for line in content:
            clean_line = line.strip()
            if clean_line == STORY_CONTENT_DIVIDER:
                break
            new_lines.append(line)
            if clean_line == '[SystemInfo]':
                new_lines.append(f'space_farclip = {self.SPACE_FARCLIP}\n')

        del new_lines[-1]

        return ''.join(new_lines)

    def get_content(self):
        return self.get_static_content()

    def process_content(self):
        if self.have_dynamic_content():
            self.init_dynamic_content()
        self.process_template()
