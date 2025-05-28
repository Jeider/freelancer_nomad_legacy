from universe import sirius
from universe.systems import sig13, rh_ber
from story.ingame import ingame_mission

from story.ingame import objectives as O
from story.ingame.tools import Point, Obj, Conn, NNObj, Ship
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT


class Misson01A(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m01/m01a.ini'
    FOLDER = 'M01A'
    FILE = 'm01a'
    SCRIPT_INDEX = 1
    START_SAVE_ID = 32000

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
        return [
            Ship(self, 'alaric'),
        ]

    def get_nn_objectives(self):
        return [
            NNObj(self, 'Поговорите с Алариком в баре', name='find_job'),
            NNObj(self, O.LAUNCH, name='launch'),
            NNObj(self, O.TLR, target='s13_tlr'),
            NNObj(self, O.JUMPGATE, target='s13_to_ber'),
            NNObj(self, O.TLR, target='tlr_to_outpost'),
            NNObj(self, 'Ожидайте прохождение проверки', target='ber_outpost'),
            NNObj(self, 'Уничтожьте корсаров', name='defend_cruiser'),
            NNObj(self, O.TLR, target='tlr_to_planet'),
            NNObj(self, O.DOCKRING, target='ber_dockring'),
        ]
