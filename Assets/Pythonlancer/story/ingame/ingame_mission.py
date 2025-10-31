from story.ingame.tools import Nag, Script, Trigger, Cond, Direct, Rtc, Offer, Difficulty

from text.dividers import DIVIDER
from text.strings import MultiString as MS


class IngameMission(object):
    JINJA_TEMPLATE = None
    FOLDER = None
    FILE = None
    NPC_FILE = 'npcships'
    STATIC_NPCSHIPS = None
    SCRIPT_INDEX = None
    DIRECT_SYSTEMS = []
    INIT_OFFER = None
    RTC = []
    START_SAVE_ID = None
    START_SAVE_RU_NAME = None

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def __init__(self, russian, difficulty, ids, ids_save, full_script, universe, history_manager):
        self.russian = russian
        self.difficulty = difficulty
        self.ids = ids
        self.ids_save = ids_save
        self.capital_groups = {}
        self.solar_groups = {}
        self.full_script = full_script
        self.universe = universe
        self.universe_root = self.universe.get_universe_root()
        self.history_manager = history_manager
        self.points: dict = self.get_all_points()
        self.nn_objectives = self.get_nn_objectives()
        self.nag = Nag()
        self.rtc = Rtc(self)
        self.offer = Offer(self)

        self.title = ids.new_name(self.get_mission_title())

        if not self.INIT_OFFER:
            raise Exception(f'Mission {self.__class__.__name__} have no initital offer')
        self.init_offer = ids.new_name(self.INIT_OFFER)

        self.script = None
        if self.full_script and self.SCRIPT_INDEX:
            self.script = Script(
                mission=self,
                msn_script=self.full_script.get_mission_by_index(self.SCRIPT_INDEX)
            )

        self.trigger = Trigger()
        self.cond = Cond()
        self.direct = Direct(self, systems=self.DIRECT_SYSTEMS)

        self.ingame_thorns = self.get_ingame_thorns()
        if not self.FOLDER:
            raise Exception('Folder should be defined for %s' % self.__class__.__name__)
        if not self.FILE:
            raise Exception('File name should be defined for %s' % self.__class__.__name__)

        if not self.START_SAVE_ID or not self.START_SAVE_RU_NAME:
            raise Exception(f'Mission {self.__class__.__name__} have no initial save id or initial save name')

        self.ids_save.add_force(self.START_SAVE_ID, MS(
            f'Миссия {self.SCRIPT_INDEX}. {self.START_SAVE_RU_NAME.get_ru()}',
            f'Mission {self.SCRIPT_INDEX}. {self.START_SAVE_RU_NAME.get_en()}'
        ))

    def get_mission_title(self):
        return MS(f'Миссия {self.SCRIPT_INDEX}', f'Mission {self.SCRIPT_INDEX}')

    def get_init_title(self):
        return self.title.id

    def get_init_offer(self):
        return self.init_offer.id

    def get_template(self):
        if not self.JINJA_TEMPLATE:
            raise Exception('template not found for mission %s' % self.__class__.__name__)
        return self.JINJA_TEMPLATE

    def get_rtc_files(self):
        items = []
        for rtc in self.RTC:
            items.append(
                (rtc, f'missions/{self.FOLDER}/{rtc}.ini')
            )
        return items

    def get_ingame_thorns(self):
        return []

    def get_ingame_thorns_context(self):
        return {f'thorn_{thn.get_name()}': thn for thn in self.ingame_thorns}

    def get_system(self, system_name):
        return self.universe_root.get_all_system_by_name(system_name)

    def get_point(self, point_name):
        return self.points[point_name]

    def get_system_obj_pos(self, system_class, point):
        return '{0}, {1}, {2}'.format(*self.get_system(system_class.NAME).get_point_pos(point))

    def get_capital_ships(self):
        return []

    def get_capital_ships_content(self):
        return {cap.name: cap for cap in self.get_capital_ships()}

    def get_real_objects(self):
        return {}

    def get_save_states(self):
        return []

    def get_dialogs(self):
        return []

    def get_static_points(self):
        return []

    def get_static_points_content(self):
        result = {}
        for point in self.get_static_points():
            try:
                result[point.alias] = point
            except Exception as e:
                print(f'caused on point {point}')
                raise e

        return result

    def get_all_points(self):
        points = self.get_static_points_content()
        points.update(self.get_real_objects())
        points.update(self.get_capital_ships_content())
        return points

    def get_ships(self):
        return []

    def get_ships_with_npc(self):
        return [ship for ship in self.get_ships() if ship.have_npc()]

    def get_ships_for_context(self):
        return {ship.name: ship for ship in self.get_ships()}

    def get_npcs(self):
        return [ship.npc for ship in self.get_ships() if ship.npc]

    def get_nn_objectives(self):
        return []

    def get_nn_objectives_context(self):
        objectives = {}
        keys = []
        for nn in self.nn_objectives:
            name = nn.get_name()
            if name in keys:
                raise Exception(f'{name} already defined as nnobjective')
            keys.append(name)
            objectives[nn.get_name()] = nn

        return objectives

    def get_all_nn_objectives_content(self):
        return DIVIDER.join([nn.get_definition() for nn in self.nn_objectives])

    def get_rtc_context(self) -> dict:
        return {
            'init_offer': self.init_offer,
            'suffix': '' if self.russian else '_en',
        }

    def get_initial_context(self) -> dict:
        context = {
            'mission': self,
            'nag': self.nag,
            'init_offer': self.init_offer,
            'rtc': self.rtc,
            'offer': self.offer,
            'history': self.history_manager,
        }
        if self.script:
            context['script'] = self.script
        return context

    def get_objects_definitions(self):
        """for template"""
        content = []
        ships = self.get_ships_with_npc()
        for ship in ships:
            content.append(ship.get_mission_npcs())
            content.append(ship.get_mission_ships())
        capitals = self.get_capital_ships()
        for capital in capitals:
            content.append(capital.get_definition())
        return DIVIDER.join(content)

    def get_context(self):
        context = self.get_initial_context()
        context.update(self.points)
        context.update(self.get_ships_for_context())
        context.update(self.get_nn_objectives_context())
        context.update(self.get_ingame_thorns_context())
        context['nn_objectives_list'] = self.get_all_nn_objectives_content()
        context['objects_definitions'] = self.get_objects_definitions()
        context['trigger'] = self.trigger
        context['cond'] = self.cond
        context['direct'] = self.direct
        context['diff'] = Difficulty(difficulty_class=self.difficulty)
        # print(context.keys())
        return context

    def add_capital_group(self, group_name, members):
        self.capital_groups[group_name] = members

    def get_capital_group(self, group_name):
        if group_name not in self.capital_groups:
            raise Exception(f'Capital group {group_name} not defined in {self.__class__.__name__}')
        return self.capital_groups[group_name]

    def add_solar_group(self, group_name, members):
        self.solar_groups[group_name] = members

    def get_solar_group(self, group_name):
        if group_name not in self.solar_groups:
            raise Exception(f'Solar group {group_name} not defined in {self.__class__.__name__}')
        return self.solar_groups[group_name]

    def get_solar_group_names(self):
        return self.solar_groups.keys()


class NagVoice(object):
    DEFINITION = '''
[NPC] 
nickname = npc_nnvoice
affiliation = li_n_grp
npc_ship_arch = nnvoice_shiparch
space_costume = , robot_body_E
individual_name = 089999
voice = nn_mod

[MsnShip]
nickname = nag_voice
NPC = npc_nnvoice
jumper = false
label = the_nnvoice
position = 0,-50000,0

'''

    def get_definition(self):
        return self.DEFINITION
