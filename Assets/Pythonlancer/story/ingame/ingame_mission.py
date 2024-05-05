from story.ingame.tools import NNObj, Ship, Nag

from text.dividers import DIVIDER


class IngameMission(object):
    JINJA_TEMPLATE = None

    def __init__(self, universe_root):
        self.universe_root = universe_root
        self.points: dict = self.get_all_points()
        self.nn_objectives = self.get_nn_objectives()
        self.nag = Nag()
        self.ingame_thorns = self.get_ingame_thorns()

    def get_template(self):
        if not self.JINJA_TEMPLATE:
            raise Exception('template not found for mission %s' % self.__class__.__name__)
        return self.JINJA_TEMPLATE

    def get_ingame_thorns(self):
        return []

    def get_ingame_thorns_context(self):
        return {f'thorn_{thn.get_name()}': thn for thn in self.ingame_thorns}

    def get_system(self, system_name):
        return self.universe_root.get_system_by_name(system_name)

    def get_point(self, point_name):
        return self.points[point_name]

    def get_system_obj_pos(self, system_class, point):
        return '{0}, {1}, {2}'.format(*self.get_system(system_class.NAME).get_point_pos(point))

    def get_real_objects(self):
        return {}

    def get_static_points(self):
        return []

    def get_static_points_content(self):
        return {p.alias: p for p in self.get_static_points()}

    def get_all_points(self):
        points = self.get_static_points_content()
        points.update(self.get_real_objects())
        return points

    def get_ships(self):
        return {}

    def get_nn_objectives(self):
        return []

    def get_nn_objectives_context(self):
        return {nn.get_name(): nn for nn in self.nn_objectives}

    def get_all_nn_objectives_content(self):
        return DIVIDER.join([nn.get_definition() for nn in self.nn_objectives])

    def get_initial_context(self) -> dict:
        return {
            'nag': self.nag,
        }

    def get_context(self):
        context = self.get_initial_context()
        context.update(self.points)
        context.update(self.get_ships())
        context.update(self.get_nn_objectives_context())
        context.update(self.get_ingame_thorns_context())
        context['nn_objectives_list'] = self.get_all_nn_objectives_content()
        # print(context.keys())
        return context



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


class Ship(object):
    DEFINIION = '''
[NPC]
nickname = alaric_m1
affiliation = fc_uk_grp
npc_ship_arch = MSN01_alaric
space_costume = rh_alaric_head_hat, pi_pirate6_body, comm_rh_alaric
individual_name = 091204
voice = pilot_f_mil_m01

[MsnShip]
nickname = MSN01_Alaric
NPC = alaric_m1
jumper = true
label = m1_friend
label = friend    
'''