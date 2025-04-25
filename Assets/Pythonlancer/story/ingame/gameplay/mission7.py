import random

from universe import sirius as S
from universe.systems import br_avl
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors

from story.ingame import names as N
from story.ingame import objectives as O
from story.ingame.tools import Point, Obj, Conn, NNObj, Ship, Solar, StaticJumpgate, Capital, SaveState
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT

from world.npc import NPC, EqMap
from world import ship
from universe import faction

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
    SCRIPT_INDEX = 7
    DIRECT_SYSTEMS = [S.omicron2, S.co_cad, S.om13, S.br_avl]
    STATIC_NPCSHIPS = NPCSHIPS
    RTC = ['cadiz']

    def get_save_states(self):
        return [
            SaveState(self, 'ironside', 'Кадиз. Билл Айронсайд найден'),
            SaveState(self, 'diversion', 'Малый Омикрон. Перед диверсией'),
            SaveState(self, 'armored', 'Малый Омикрон. Перехват транспорта'),
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
                Solar(self, S.co_cad, sol, ru_name='_'),
            )

        defined_points.append(
            StaticJumpgate(self, S.co_cad, 'cad_to_omicron2', ru_name='_'),
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
            Solar(self, S.omicron2, 'repair1', ru_name='Ремонтник', labels=['comm_defence']),
            Solar(self, S.omicron2, 'repair2', ru_name='Ремонтник', labels=['comm_defence']),

            Solar(self, S.omicron2, 'transport1', ru_name='Транспорт', labels=['comm_defence']),
            Solar(self, S.omicron2, 'transport2', ru_name='Транспорт', labels=['comm_defence']),
        ])

        defined_points.append(
            StaticJumpgate(self, S.omicron2, 'omicron2_to_om13', ru_name='_'),
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
            NNObj(self, 'Уничтожьте корабли банды Старлайна', name='kill_starline'),
            NNObj(self, 'Убейте Билла Айронсайда', name='kill_starline_leader'),
            NNObj(self, O.GOTO, name='return_to_freeport', target='co_cad_03'),
            NNObj(self, O.TLR, name='tlr_to_cadiz', target='co_cad_CO_TLR_L1_03'),
            NNObj(self, O.TLR, name='dock_with_cadiz', target='co_cad_01_dock_ring'),
            NNObj(self, 'Уничтожьте истребители Ордена', name='destroy_order_ship'),
            NNObj(self, O.TLR, name='escape_tlr_1', target='co_cad_CO_TLR_L2_01'),
            NNObj(self, O.TLR, name='escape_tlr_2', target='co_cad_CO_TLR_L3_01'),
            NNObj(self, O.JUMPGATE, name='jump_omicron2', target='cad_to_omicron2'),
            NNObj(self, O.GOTO, name='goto_near_tortuga', target='to_tortuga_road'),
            NNObj(self, 'Подберите бомбы', name='pick_up_bombs'),
            NNObj(self, O.GOTO, name='goto_near_tortuga', target='to_tortuga_road'),
            NNObj(self, 'Доберитесь до коммуникатора',
                  name='goto_communicator', target='communicator', towards=True),
            NNObj(self, 'Уничтожьте ядро коммуникатора, сбросив бомбы и сдетонировав их',
                  name='destroy_communicator', target='communicator'),
            NNObj(self, 'Покиньте Тортугу', name='fly_away_from_tortuga', target='fly_away_tortuga'),
            NNObj(self, 'Доберитесь до точки засады',
                  name='goto_possible_ambush_place', target='possible_ambush_place'),
            NNObj(self, 'Доберитесь места перехвата',
                  name='goto_real_ambush_place', target='real_ambush_place'),
            NNObj(self, 'Атакуйте бронированный транспорт', name='attack_transport'),
            NNObj(self, 'Приблизьтесь к транспорту, чтобы перегрузить генератор', name='overdose_generator'),
            NNObj(self, 'Уничтожьте бронированный транспорт', name='destroy_transport'),
            NNObj(self, 'Подберите артефакты', name='pick_up_artifacts'),
            NNObj(self, O.GOTO_JUMPHOLE, name='goto_jump_om13', target='omicron2_to_om13', towards=True),
            NNObj(self, O.JUMPHOLE, name='jump_om13', target='omicron2_to_om13'),
        ]


    '''
[NNObjective]
nickname = NN_go_to_battleship
state = HIDDEN
type = rep_inst, tau23, 097026, 097026, 16000, 0, 0, tau23_03

[NNObjective]
nickname = NN_buy_things_and_launch_to_space
state = HIDDEN
type = ids, 097027

[NNObjective]
nickname = NN_use_tlr_to_gasminer
state = HIDDEN
type = rep_inst, tau23, 097028, 097028, 15793, -6, -1064, TAU23_F_Trade_Lane_Ring_L2_04

[NNObjective]
nickname = NN_dock_with_avalon
state = HIDDEN
type = rep_inst, tau23, 097029, 097029, 10000, -380, -30000, tau23_01

[NNObjective]
nickname = NN_destroy_bandits
state = HIDDEN
type = ids, 097030

[NNObjective]
nickname = NN_dock_with_avalon_again
state = HIDDEN
type = rep_inst, tau23, 097031, 097031, 10000, -380, -30000, tau23_01
    
    '''

    def get_capital_ships(self):
        armored_ship = {
            'npc_ship_arch': 'm07_armored',
            'faction': 'fc_uk_grp',
            'labels': ['order'],
        }

        caps = [
            Capital(self, 'armored', ru_name='Бронированный транспорт', **armored_ship),
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
        ]
