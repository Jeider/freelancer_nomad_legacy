from universe import sirius
from universe.systems import sig13, rh_ber
from story.ingame import ingame_mission
from story.ingame import tools
from story.ingame import triggers as trig

from story.ingame.tools import Point, Obj, Conn, NNObj, Ship, Nag
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT

from text.dividers import DIVIDER




class Misson01A(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m01/m01a.ini'

    def __init__(self, universe_root):
        self.universe_root = universe_root
        self.points: dict = self.get_points()
        self.nn_objectives = self.get_nn_objectives()
        self.nag = Nag()
        self.ingame_thorns = self.get_ingame_thorns()

        # mrk -18300, 600, 29300
        # static -17950, 665, 29655

    def get_ingame_thorns(self):
        return [
            IngameThorn(
                self,
                system_class=sirius.sig13,
                template=GENERIC_TWO_POINT,
                name='m01_s13_launch',
                points={
                    'camera': 'm1_cam',
                    'marker': 'm1_cam_marker',
                }
            )
        ]

    def get_ingame_thorns_context(self):
        return {f'thorn_{thn.get_name()}': thn for thn in self.ingame_thorns}

    def get_system(self, system_name):
        return self.universe_root.get_system_by_name(system_name)

    def get_point(self, point_name):
        return self.points[point_name]

    def get_system_obj_pos(self, system_class, point):
        return '{0}, {1}, {2}'.format(*self.get_system(system_class.NAME).get_point_pos(point))

    def get_points(self):
        return {
            's13_tlr': Conn(self, sig13.Sig13ConnRheinlandGas2, sig13.Sig13RheinlandStation),
            's13_to_ber': Obj(self, sig13.Sig13BerlinJumpgate),
            'ber_outpost': Obj(self, rh_ber.BerlinOutpost),
            'tlr_to_outpost': Conn(self, rh_ber.BerConnOutpost1, rh_ber.BerlinSigma13Jumpgate),
            'tlr_to_planet': Conn(self, rh_ber.BerConnOutpost3, rh_ber.BerlinDockring),
            'ber_dockring': Obj(self, rh_ber.BerlinDockring),

            'alaric_s13': Point(self, sirius.sig13, 'm1_alaric1'),
        }

    def get_ships(self):
        return {
            'alaric': Ship('MSN01_Alaric'),
        }

    def get_nn_objectives(self):
        return [
            NNObj(self, 91002, name='find_job'),
            NNObj(self, 91003, name='launch'),
            NNObj(self, 91004, target='s13_tlr'),
            NNObj(self, 91005, target='s13_to_ber'),
            NNObj(self, 91006, target='tlr_to_outpost'),
            NNObj(self, 91006, target='ber_outpost'),
            NNObj(self, 91007, name='defend_cruiser'),
            NNObj(self, 91008, target='tlr_to_planet'),
            NNObj(self, 91008, target='ber_dockring'),
        ]

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
