from universe.content.system_object import SystemObject
from universe.content.main_objects import TradeConnection, JumpableObject, DockableObject, StaticObject
from universe.content.mineable import Mineable, RewardField, Field, RewardsGroup

from universe.systems import br_wrw as br_wrw_objects
from universe.systems import rh_ber as rh_ber_content





from text.dividers import DIVIDER

from tools.tracks import Tracks
from tools.system_template import SystemTemplateLoader


TLR_DISTANCE = 3000


class System(object):
    NAME = ''
    CONTENT = None
    TEMPLATE_NAME = None

    TRACKS_SYSTEM_TEMPLATE = '''[Settings]
system = {system_name}
distance = {tlr_distance}
'''

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

        self.trade_connections = []

        # self.jumps = []
        self.dockables = []
        self.statics_list = []
        self.statics_db = {}
        self.mineable = []
        # self.pirate_assaults = []
        # self.hunter_patrols = []
        # self.zones = []

        if self.CONTENT is not None:
            self.init_content()

    def init_content(self):
        self.process_template()

        for item in self.CONTENT.__dict__.values():
            if not isinstance(item, type):
                continue

            if not issubclass(item, RewardsGroup) and not issubclass(item, SystemObject):
                continue

            if (item.ABSTRACT and item != br_wrw_objects.WarwickSysObject) or item == br_wrw_objects.WarwickSysObject:
                continue

            if issubclass(item, RewardsGroup):
                reward_group_instance = item()
                self.rewards_groups_list.append(reward_group_instance)
                self.rewards_groups_db[item.__name__] = reward_group_instance
                continue

            if not isinstance(item, type) or not issubclass(item, SystemObject):
                continue

            if item in (TradeConnection, DockableObject, TradeConnection):
                continue

            if issubclass(item, StaticObject):
                self.add_static_object(item)
            elif issubclass(item, Mineable):
                self.add_mineable(item)
            elif issubclass(item, TradeConnection):
                self.add_trade_connection(item)

        self.process_reward_groups()

        system_content = []

        for app_obj in self.get_appearable_objects():
            system_content.append(app_obj.get_system_content())

        for mineable_obj in self.get_mineable_objects():
            system_content.append(mineable_obj.get_system_content())

        if len(self.trade_connections) > 0:
            self.generate_tradelanes()
            self.define_attacker_patrols()

            for item in self.trade_connections:
                system_content.append(item.get_system_content())

        self.generate_patrols()

        for patrol in self.get_patrols_list():
            system_content.append(patrol.get_system_content())

        self.system_content_str = DIVIDER.join(system_content)

    def add_trade_connection(self, item):
        self.trade_connections.append(item(self))

    def add_static_object(self, item):
        static = item(self)
        self.statics_list.append(static)
        self.statics_db[static.get_full_alias()] = static

    def add_mineable(self):
        self.mineable.append(item(self))

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




    # def get_path_creation_request(self):
    #     pass



class BretoniaSystem(object):

    FACTION_CODE = None

    def get_faction(self):
        if self.FACTION_CODE is None:
            raise Exception('unknown faction for system %s' % self.NAME)
        return self.FACTION_CODE



class RheinlandSystem(object):

    FACTION_CODE = None

    def get_faction(self):
        if self.FACTION_CODE is None:
            raise Exception('unknown faction for system %s' % self.NAME)
        return self.FACTION_CODE




class rh_mnh(System):
    NAME = 'Rh_Mnh'


class rh_biz(System):
    NAME = 'Rh_biz'


class rh_stut(System):
    NAME = 'Rh_stut'


class rh_ber(RheinlandSystem, System):
    NAME = 'Rh_ber'
    TEMPLATE_NAME = 'rh_ber'
    FACTION_CODE = 'br_grp'
    CONTENT = rh_ber_content

class sig8(System):
    NAME = 'sig8'


class om15(System):
    NAME = 'om15'


class sig13(System):
    NAME = 'sig13'


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
