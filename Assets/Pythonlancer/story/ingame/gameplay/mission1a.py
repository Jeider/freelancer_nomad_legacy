from universe import sirius
from universe.systems import sig13, rh_ber
from story.ingame import ingame_mission

from story.ingame.tools import Point, Obj, Conn, NNObj, Ship
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT


class Misson01A(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m01/m01a.ini'
    FOLDER = 'M01A'
    FILE = 'm01a'

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

    def get_real_objects(self):
        return {
            's13_tlr': Conn(self, sig13.Sig13ConnRheinlandGas2, sig13.Sig13RheinlandStation),
            's13_to_ber': Obj(self, sig13.Sig13BerlinJumpgate),
            'ber_outpost': Obj(self, rh_ber.BerlinOutpost),
            'tlr_to_outpost': Conn(self, rh_ber.BerConnOutpost1, rh_ber.BerlinSigma13Jumpgate),
            'tlr_to_planet': Conn(self, rh_ber.BerConnOutpost3, rh_ber.BerlinOutpost),
            'ber_dockring': Obj(self, rh_ber.BerlinDockring),
        }

    def get_static_points(self):
        return [
            Point(self, sirius.sig13, 'm1_alaric1'),
            Point(self, sirius.rh_ber, 'rh_cruiser'),
            Point(self, sirius.rh_ber, 'rh_wing1'),
            Point(self, sirius.rh_ber, 'rh_wing2'),
            Point(self, sirius.rh_ber, 'co_wingA'),
            Point(self, sirius.rh_ber, 'co_wingB'),
            Point(self, sirius.rh_ber, 'co_wingX'),
            Point(self, sirius.rh_ber, 'co_wingX_target'),
            Point(self, sirius.rh_ber, 'player_outpost_autosave'),
            Point(self, sirius.rh_ber, 'player_cruiser_dead'),
            Point(self, sirius.rh_ber, 'alaric_outpost'),
        ]


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
