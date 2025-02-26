from story.ingame.tools import Nag, Script, Trigger, Cond, Direct, Patrol

from text.dividers import DIVIDER


class IngameMission(object):
    JINJA_TEMPLATE = None
    FOLDER = None
    FILE = None
    NPC_FILE = 'npcships'
    STATIC_NPCSHIPS = None
    SCRIPT_INDEX = None
    DIRECT_SYSTEMS = []

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def __init__(self, full_script, universe_root):
        self.capital_groups = {}
        self.full_script = full_script
        self.universe_root = universe_root
        self.points: dict = self.get_all_points()
        self.nn_objectives = self.get_nn_objectives()
        self.nag = Nag()

        self.script = None
        if self.full_script and self.SCRIPT_INDEX:
            self.script = Script(
                msn_script=self.full_script.get_mission_by_index(self.SCRIPT_INDEX)
            )

        self.ingame_thorns = self.get_ingame_thorns()
        if not self.FOLDER:
            raise Exception('Folder should be defined for %s' % self.__class__.__name__)
        if not self.FILE:
            raise Exception('File name should be defined for %s' % self.__class__.__name__)

    def get_template(self):
        if not self.JINJA_TEMPLATE:
            raise Exception('template not found for mission %s' % self.__class__.__name__)
        return self.JINJA_TEMPLATE

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

    def get_static_points(self):
        return []

    def get_static_points_content(self):
        return {p.alias: p for p in self.get_static_points()}

    def get_all_points(self):
        points = self.get_static_points_content()
        points.update(self.get_real_objects())
        points.update(self.get_capital_ships_content())
        return points

    def get_ships(self):
        return []

    def get_ships_with_npc(self):
        return [ship for ship in self.get_ships() if ship.npc is not None]

    def get_ships_for_context(self):
        return {ship.name: ship for ship in self.get_ships()}

    def get_npcs(self):
        return [ship.npc for ship in self.get_ships() if ship.npc]

    def get_nn_objectives(self):
        return []

    def get_nn_objectives_context(self):
        return {nn.get_name(): nn for nn in self.nn_objectives}

    def get_all_nn_objectives_content(self):
        return DIVIDER.join([nn.get_definition() for nn in self.nn_objectives])

    def get_initial_context(self) -> dict:
        context = {
            'nag': self.nag,
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
        trigger = Trigger()
        context['trigger'] = trigger
        context['cond'] = Cond()
        direct = Direct(self, systems=self.DIRECT_SYSTEMS)
        context['direct'] = direct
        context['patrol'] = Patrol(direct=direct, trigger=trigger)
        # print(context.keys())
        return context

    def add_capital_group(self, group_name, members):
        self.capital_groups[group_name] = members

    def get_capital_group(self, group_name):
        if group_name not in self.capital_groups:
            raise Exception(f'Capital group {group_name} not defined in {self.__class__.__name__}')
        return self.capital_groups[group_name]


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
