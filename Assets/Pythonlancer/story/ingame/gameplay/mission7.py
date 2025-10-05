import random

from universe import sirius as S
from universe.systems import br_avl
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors

from story.ingame import names as N
from story.ingame import objectives as O
from story.ingame.tools import (Point, Obj, Conn, NNObj, Ship, Solar, StaticJumpgate, Capital, SaveState,
                                DockableBattleshipSolar, MultiLine)
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT

from world.npc import NPC, EqMap
from world import ship
from universe import faction

from text.strings import MultiString as MS

NPCSHIPS = '''

[NPCShipArch]
nickname = m07_armored
loadout = ms7_armored_loadout
level = d10
ship_archetype = ge_armored
pilot = mod_fighter_version_a
state_graph = GUNBOAT
npc_class = lawful, CRUISER

'''


class Misson07(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m07/m07.ini'
    FOLDER = 'M07'
    FILE = 'm07'
    START_SAVE_ID = 32700
    START_SAVE_RU_NAME = MS('Мальта, фрипорт Тринидад', 'Malta, Freeport Trinidad')
    SCRIPT_INDEX = 7
    DIRECT_SYSTEMS = [S.omicron2, S.co_cad, S.om13, S.br_avl]
    STATIC_NPCSHIPS = NPCSHIPS
    RTC = ['cadiz']
    INIT_OFFER = MultiLine(
        [
            'ЗАДАЧА:',
            'Найти способ восстановить связь с СБА и вызволить артефакты',
            '',
            'СЛОЖНОСТЬ:',
            'Рискованная.',
            '',
            'НАГРАДА:',
            'Обещанные 250 000 кредитов',
        ],[
            'OBJECTIVE:',
            'Find way to get contact with ASF and get artifacts back.',
            '',
            'DIFFICULTY:',
            'Risky.',
            '',
            'REWARD:',
            'Promised 250 000 credits',
        ]
    ).get_content()

    def get_save_states(self):
        return [
            SaveState(self, 'ironside', MS('Мальта. Билл Айронсайд найден', 'Malta. Battle with Ironside')),
            SaveState(self, 'diversion', MS('Малый Омикрон. Перед диверсией', 'Omicron Minor. Before Diversion')),
            SaveState(self, 'armored', MS('Малый Омикрон. Перехват транспорта', 'Omicron Minor. Catching of Transport')),
        ]

    def get_ingame_thorns(self):
        return [
            IngameThorn(
                self,
                system_class=S.br_avl,
                template=GENERIC_TWO_POINT,
                name='m7_bandit_cam',
                points={
                    'camera': 'bandit_cam',
                    'marker': 'bandit_mrk',
                },
                duration=120,
            ),
            IngameThorn(
                self,
                system_class=S.br_avl,
                template=GENERIC_TWO_POINT,
                name='m7_supercop_cam',
                points={
                    'camera': 'bandit_darcy_cam',
                    'marker': 'bandit_darcy_mrk',
                },
                duration=120,
            ),
        ]

    def get_static_points(self):
        defined_points = []

        # CADIZ

        cad_points = [
            'starline1',
            'starline2',
        ]
        for p in cad_points:
            defined_points.append(
                Point(self, S.co_cad, p)
            )

        cad_solars = [
            'co_cad_CO_TLR_L1_03',
            'co_cad_01_dock_ring',
            'co_cad_03',

            'co_cad_CO_TLR_L2_01',
            'co_cad_CO_TLR_L3_01',
        ]
        for sol in cad_solars:
            defined_points.append(
                Solar(self, S.co_cad, sol, ru_name=MS('_', '_')),
            )

        defined_points.append(
            StaticJumpgate(self, S.co_cad, 'cad_to_omicron2', ru_name=MS('_', '_')),
        )

        cad_points = [
            'to_tortuga_road',
            'fly_away_tortuga',
            'possible_ambush_place',
            'real_ambush_place',
        ]
        for p in cad_points:
            defined_points.append(
                Point(self, S.omicron2, p)
            )

        omicron_solars = [
            ('communicator', 'Коммуникатор'),
        ]
        for sol, ru_name in omicron_solars:
            defined_points.append(
                Solar(self, S.omicron2, sol, ru_name=ru_name),
            )

        defined_points.extend([
            Solar(self, S.omicron2, 'repair1', ru_name=MS('Ремонтник', "Repair Ship"), labels=['comm_defence']),
            Solar(self, S.omicron2, 'repair2', ru_name=MS('Ремонтник', "Repair Ship"), labels=['comm_defence']),

            Solar(self, S.omicron2, 'transport1', ru_name=MS('Транспорт', 'Transport'), labels=['comm_defence']),
            Solar(self, S.omicron2, 'transport2', ru_name=MS('Транспорт', 'Transport'), labels=['comm_defence']),
        ])

        defined_points.append(
            StaticJumpgate(self, S.omicron2, 'omicron2_to_om13', ru_name=MS('_', '_')),
        )

        defined_points.append(
            DockableBattleshipSolar(
                self, S.br_avl, 'm7_bship1', ru_name=MS('Линкор Принц Уэльсский', 'Battleship Prince of Wales'), base='br_avl_99_base',
                archetype='b_battleship', loadout='br_battleship_station'),
        )
        return defined_points

    def get_real_objects(self):
        return {
            'battleship': Obj(self, br_avl.AvalStoryBattleship),
            'aval_tlr': Conn(self, br_avl.AvalPoliceConn1, br_avl.AvalPolice),
            'dock_ring': Obj(self, br_avl.AvalDockring),
        }

    def get_nn_objectives(self):
        return [
            NNObj(self, O.LAUNCH, name='launch'),
            NNObj(self, O.GOTO, name='goto_starline1', target='starline1'),
            NNObj(self, O.GOTO, name='goto_starline2', target='starline2'),
            NNObj(self, MS('Уничтожьте корабли банды Старлайна', 'Destroy Starline band ships'), name='kill_starline'),
            NNObj(self, MS('Убейте Билла Айронсайда', 'Kill Bill Ironside'), name='kill_starline_leader'),
            NNObj(self, O.GOTO, name='return_to_freeport', target='co_cad_03'),
            NNObj(self, O.TLR, name='tlr_to_cadiz', target='co_cad_CO_TLR_L1_03'),
            NNObj(self, O.TLR, name='dock_with_cadiz', target='co_cad_01_dock_ring'),
            NNObj(self, MS('Уничтожьте истребители Ордена', 'Destroy Order ships'), name='destroy_order_ship'),
            NNObj(self, O.TLR, name='escape_tlr_1', target='co_cad_CO_TLR_L2_01'),
            NNObj(self, O.TLR, name='escape_tlr_2', target='co_cad_CO_TLR_L3_01'),
            NNObj(self, O.JUMPGATE, name='jump_omicron2', target='cad_to_omicron2'),
            NNObj(self, O.GOTO, name='goto_near_tortuga', target='to_tortuga_road'),
            NNObj(self, MS('Подберите бомбы', 'Collect bombs'), name='pick_up_bombs'),
            NNObj(self, MS('Доберитесь до коммуникатора', 'Reach the communicator'),
                  name='goto_communicator', target='communicator', towards=True),
            NNObj(self, 'Уничтожьте ядро коммуникатора, сбросив бомбы и сдетонировав их',
                  name='destroy_communicator', target='communicator'),
            NNObj(self, MS('Покиньте Тортугу', 'Left Tortuga space'), name='fly_away_from_tortuga', target='fly_away_tortuga'),
            NNObj(self, MS('Доберитесь до точки засады', 'Reach ambush place'),
                  name='goto_possible_ambush_place', target='possible_ambush_place'),
            NNObj(self, MS('Доберитесь места перехвата', 'Go to catched transport'),
                  name='goto_real_ambush_place', target='real_ambush_place'),
            NNObj(self, MS('Атакуйте бронированный транспорт', 'Attack armored transport'), name='attack_transport'),
            NNObj(self, MS('Приблизьтесь к транспорту, чтобы перегрузить генератор',
                           'Stay near transport to overload it\'s generator'), name='overdose_generator'),
            NNObj(self, MS('Уничтожьте бронированный транспорт', 'Destroy armored transport'), name='destroy_transport'),
            NNObj(self, MS('Подберите артефакты', 'Collect artifacts'), name='pick_up_artifacts'),
            NNObj(self, O.GOTO_JUMPHOLE, name='goto_jump_om13', target='omicron2_to_om13', towards=True),
            NNObj(self, O.JUMPHOLE, name='jump_om13', target='omicron2_to_om13'),
            NNObj(self, O.GOTO, name='goto_bship', target='m7_bship1', towards=True),
            NNObj(self, O.DOCK_BATTLESHIP, name='dock_bship', target='m7_bship1'),
            NNObj(self, MS('Улучшите свой корабль и вылетайте в космос', 'Upgrade your ship and launch to space'),
                  name='buy_things_and_launch_to_space'),
            NNObj(self, O.TLR, target='aval_tlr'),
            NNObj(self, O.DOCKRING, target='dock_ring'),
            NNObj(self, MS('Уничтожьте бандитов', 'Destroy bandits'), name='destroy_bandits'),
        ]

    def get_capital_ships(self):
        armored_ship = {
            'npc_ship_arch': 'm07_armored',
            'faction': 'fc_uk_grp',
            'labels': ['order'],
        }

        caps = [
            Capital(self, 'armored', ru_name=MS('Бронированный транспорт', 'Armored transport'), **armored_ship),
        ]

        return caps

    def get_ships(self):
        return [
            Ship(
                self,
                'rockford',
                hero=True,
                jumper=True,
                actor=actors.Rockford,
                labels=[
                    'friend',
                ],
                npc=NPC(
                    faction=faction.LibertyHunters,
                    ship=ship.Eagle,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'point_a',
                count=4,
                affiliation=faction.Starline.CODE,
                system_class=S.co_cad,
                slide_z=-200,
                labels=['point_a', 'starline'],
                npc=NPC(
                    faction=faction.Starline,
                    ship=ship.Barracuda,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=4),
                )
            ),
            Ship(
                self,
                'point_b',
                count=4,
                affiliation=faction.Starline.CODE,
                system_class=S.co_cad,
                slide_z=-200,
                labels=['point_b', 'starline'],
                npc=NPC(
                    faction=faction.Starline,
                    ship=ship.Barracuda,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'ironside',
                count=1,
                affiliation=faction.Starline.CODE,
                system_class=S.co_cad,
                labels=['point_b', 'starline'],
                npc=NPC(
                    faction=faction.Starline,
                    ship=ship.Defender,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'cadiz_order',
                count=6,
                affiliation=faction.OrderMain.CODE,
                system_class=S.co_cad,
                slide_z=200,
                labels=['cadiz_attack', 'order'],
                npc=NPC(
                    faction=faction.OrderMain,
                    ship=ship.Anubis,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'escort_a',
                count=3,
                affiliation=faction.OrderMain.CODE,
                system_class=S.omicron2,
                slide_x=200,
                labels=['armored_defend', 'order'],
                npc=NPC(
                    faction=faction.OrderMain,
                    ship=ship.Anubis,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'escort_b',
                count=3,
                affiliation=faction.OrderMain.CODE,
                system_class=S.omicron2,
                slide_z=200,
                labels=['armored_defend', 'order'],
                npc=NPC(
                    faction=faction.OrderMain,
                    ship=ship.Anubis,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'darcy',
                hero=True,
                actor=actors.Darcy,
                labels=[
                    'friend',
                ],
                npc=NPC(
                    faction=faction.BretoniaMain,
                    ship=ship.Cavalier,
                    level=NPC.D19,
                    equip_map=EqMap(base_level=6),
                )
            ),
            Ship(
                self,
                'bandit',
                count=5,
                system_class=S.br_avl,
                slide_z=-60,
                labels=[
                    'bandit',
                    'enemy',
                ],
                base_name='Бандит',
                npc=NPC(
                    faction=faction.BretoniaPirate,
                    ship=ship.Crusader,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=5),
                ),
            ),
        ]
