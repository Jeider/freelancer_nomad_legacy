from universe import sirius
from universe.systems import rh_ber, sig8, rh_biz
from story.ingame import ingame_mission

from story.ingame import objectives as O
from story.ingame.tools import Point, Obj, Conn, NNObj, Ship
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT


class Misson01B(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m01/m01b.ini'
    FOLDER = 'M01B'
    FILE = 'm01b'
    SCRIPT_INDEX = 1
    START_SAVE_ID = 32100

    def get_ingame_thorns(self):
        return []

    def get_real_objects(self):
        return {
            'ber_tlr_1': Conn(self, rh_ber.BerConnStation1, rh_ber.BerlinDockring),
            'ber_tlr_2': Conn(self, rh_ber.BerConnTrading3, rh_ber.BerlinMegaStation),
            'ber_tlr_3': Conn(self, rh_ber.BerConnTrading2, rh_ber.BerlinTrading),
            'ber_to_sig8': Obj(self, rh_ber.BerlinSigma8Jumpgate),

            'sig8_tlr_1': Conn(self, sig8.Sig8PoliceConn2, sig8.Sig8BorderStation),
            'sig8_to_biz': Obj(self, sig8.Sig8BizmarkJumpgate),
            'sig8_outpost': Obj(self, sig8.Sig8BorderStation),

            'biz_tlr_1': Conn(self, rh_biz.BizmarkConnPlanet1, rh_biz.BizmarkSigma8Jumpgate),
            'biz_dockring': Obj(self, rh_biz.BizmarkDockRing),
        }

    def get_static_points(self):
        return [
            Point(self, sirius.rh_ber, 'ber_armored'),

            Point(self, sirius.sig8, 'point_first_regroup'),
            Point(self, sirius.sig8, 'point_to_starke'),
            Point(self, sirius.sig8, 'point_a'),
            Point(self, sirius.sig8, 'point_b'),
            Point(self, sirius.sig8, 'point_near_outpost'),
            Point(self, sirius.sig8, 'point_escort_outpost'),
            Point(self, sirius.sig8, 'player_battle_autosave'),

            Point(self, sirius.rh_biz, 'biz_m1_first_regroup'),
        ]


    def get_ships(self):
        return [
            Ship(self, 'armored'),
            Ship(self, 'escort'),
        ]

    def get_nn_objectives(self):
        return [
            NNObj(self, O.LAUNCH, name='launch'),
            NNObj(self, 'Направляйтесь к Аделмару', name='goto_adelmar', target='point_b'),
            NNObj(self, O.DESTROY_ENEMY, name='destroy_enemy'),
            NNObj(self, 'Войдите в формацию с Аделмаром', name='join_formation'),
            NNObj(self, 'Следуйте за Аделмаром', name='follow_adelmar'),
            NNObj(self, O.DOCKRING, target='biz_dockring'),
        ]
