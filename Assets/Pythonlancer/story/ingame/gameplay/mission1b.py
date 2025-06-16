from universe import sirius as S
from universe.systems import rh_ber, sig8, rh_biz
from story.ingame import ingame_mission
from story import actors

from story.ingame import objectives as O
from story.ingame.tools import Point, Obj, Conn, NNObj, Ship, Capital, SaveState, MultiLine
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT

from world.npc import NPC, EqMap
from world import ship
from universe import faction

NPCSHIPS = '''

[NPCShipArch]
nickname = armored_m1
loadout = lod_MSN01_armored
level = d10
ship_archetype = ge_armored
pilot = cruiser_default
state_graph = TRANSPORT
npc_class = lawful, CRUISER

'''


class Misson01B(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m01/m01b.ini'
    FOLDER = 'M01B'
    FILE = 'm01b'
    SCRIPT_INDEX = 1
    START_SAVE_ID = 32100
    START_SAVE_RU_NAME = 'Планета Берлин'
    STATIC_NPCSHIPS = NPCSHIPS
    INIT_OFFER = MultiLine(
        'ЗАДАЧА:',
        'Сопроводить рейнландский торговый конвой.'
        ''
        'СЛОЖНОСТЬ:'
        'Низкая.'
        ''
        'Награда:'
        '5 000 кредитов.'
    ).get_content()

    def get_save_states(self):
        return [
            SaveState(self, 's8_battle', 'Сигма-8, Астероидное поле'),
        ]

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
            Point(self, S.rh_ber, 'ber_armored'),

            Point(self, S.sig8, 'point_first_regroup'),
            Point(self, S.sig8, 'point_to_starke'),
            Point(self, S.sig8, 'point_a'),
            Point(self, S.sig8, 'point_b'),
            Point(self, S.sig8, 'point_near_outpost'),
            Point(self, S.sig8, 'point_near_outpost2'),
            Point(self, S.sig8, 'point_escort_outpost'),
            Point(self, S.sig8, 'player_battle_autosave'),

            Point(self, S.rh_biz, 'biz_m1_first_regroup'),
        ]

    def get_capital_ships(self):
        armored_ship = {
            'npc_ship_arch': 'armored_m1',
            'faction': 'fc_uk_grp',
            'labels': ['m1_friend'],
            'jumper': 'true',
        }

        caps = [
            Capital(self, 'armored', ru_name='Аделмар', **armored_ship),
        ]

        return caps

    def get_ships(self):
        return [
            Ship(
                self,
                'escort',
                jumper=True,
                hero=True,
                actor=actors.Luc,
                labels=[
                    'm1_friend',
                    'friend',
                ],
                npc=NPC(
                    faction=faction.RheinlandCivilians,
                    ship=ship.Banshee,
                    level=NPC.D3,
                    equip_map=EqMap(base_level=1),
                )
            ),
            Ship(
                self,
                'alaric',
                jumper=True,
                hero=True,
                actor=actors.Alaric,
                labels=[
                    'm1_friend',
                    'friend',
                ],
                npc=NPC(
                    faction=faction.LibertyPirate,
                    ship=ship.Piranha,
                    level=NPC.D3,
                    equip_map=EqMap(base_level=2),
                )
            ),
            Ship(
                self,
                'pir_f_A',
                count=3,
                affiliation=faction.WorkaroundPirate.CODE,
                system_class=S.sig8,
                labels=[
                    'pi_assault',
                    'enemy'
                ],
                relative_pos=True,
                relative_range=1600,
                npc=NPC(
                    faction=faction.RheinlandPirate,
                    ship=ship.Dagger,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=1),
                    have_afterburn2=False,
                    # gen_armor=False,
                    # extra_equip=[
                    #     'equip = npc_armor_1',
                    # ]
                )
            ),
            Ship(
                self,
                'pir_e_A',
                count=2,
                affiliation=faction.WorkaroundPirate.CODE,
                system_class=S.sig8,
                labels=[
                    'pi_assault',
                    'enemy'
                ],
                relative_pos=True,
                relative_range=1800,
                npc=NPC(
                    faction=faction.RheinlandPirate,
                    ship=ship.Stiletto,
                    level=NPC.D2,
                    equip_map=EqMap(base_level=1),
                    have_afterburn2=False,
                    # gen_armor=False,
                    # extra_equip=[
                    #     'equip = npc_armor_1',
                    # ]
                )
            ),
            Ship(
                self,
                'pir_f_B',
                count=2,
                affiliation=faction.WorkaroundPirate.CODE,
                system_class=S.sig8,
                labels=[
                    'pi_assault',
                    'enemy'
                ],
                relative_pos=True,
                relative_range=1500,
                npc=NPC(
                    faction=faction.RheinlandPirate,
                    ship=ship.Dagger,
                    level=NPC.D2,
                    equip_map=EqMap(base_level=1),
                    have_afterburn2=False,
                    # gen_armor=False,
                    # extra_equip=[
                    #     'equip = npc_armor_1',
                    # ]
                )
            ),
            Ship(
                self,
                'pir_e_B',
                count=2,
                affiliation=faction.WorkaroundPirate.CODE,
                system_class=S.sig8,
                labels=[
                    'pi_assault',
                    'enemy'
                ],
                relative_pos=True,
                relative_range=1500,
                npc=NPC(
                    faction=faction.RheinlandPirate,
                    ship=ship.Stiletto,
                    level=NPC.D2,
                    equip_map=EqMap(base_level=1),
                    have_afterburn2=False,
                    # gen_armor=False,
                    # extra_equip=[
                    #     'equip = npc_armor_1',
                    # ]
                )
            ),
        ]

    #

    def get_nn_objectives(self):
        return [
            NNObj(self, O.LAUNCH, name='launch'),
            NNObj(self, 'Направляйтесь к Аделмару', name='goto_adelmar', target='point_b'),
            NNObj(self, O.DESTROY_ENEMY, name='destroy_enemy'),
            NNObj(self, 'Войдите в формацию с Аделмаром', name='join_formation'),
            NNObj(self, 'Следуйте за Аделмаром', name='follow_adelmar'),
            NNObj(self, O.DOCKRING, target='biz_dockring'),
        ]
