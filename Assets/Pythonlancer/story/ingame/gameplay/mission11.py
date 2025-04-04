import random

from universe import sirius as S
from universe.systems import om7, or_hq, rh_vien, sig42
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors

from universe.content import main_objects

from story.ingame import names as N
from story.ingame import objectives as O
from story.ingame.tools import (
    Point, Obj, Conn, NNObj, Ship, Solar, DockableBattleshipSolar, StaticJumpgate, Capital, SaveState
)
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT, GENERIC_MOUNTED_ROTATABLE, GENERIC_TWO_POINT_MOVE

from world.npc import NPC, EqMap
from world import ship
from universe import faction

NPCSHIPS = '''

[NPCShipArch]
nickname = ms11_ku_destroyer
loadout = ku_grp_destroyer
level = d5
ship_archetype = ku_destroyer
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER

[NPCShipArch]
nickname = ms11_rh_cruiser
loadout = rh_grp_cruiser
level = d5
ship_archetype = rh_cruiser
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER

[NPCShipArch]
nickname = ms11_rh_battleship
loadout = rh_battleship_01
level = d5
ship_archetype = rh_battleship_m11
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER

[NPCShipArch]
nickname = ms11_ku_battleship
loadout = ku_grp_battleship
level = d10
ship_archetype = ku_battleship
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

[NPCShipArch]
nickname = ms11_rockford
loadout = m11_rockford
level = d10
ship_archetype = ge_fighter6
pilot = story_rtc_dummy_attacker
state_graph = CRUISER
npc_class = lawful

[NPCShipArch]
nickname = m11_wilham
loadout = m11_wilham
level = d6
ship_archetype = rh_elite
pilot = story_rtc_dummy
state_graph = CRUISER
npc_class = lawful

'''


class Misson11(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m11/m11.ini'
    FOLDER = 'M11'
    FILE = 'm11'
    SCRIPT_INDEX = 11
    DIRECT_SYSTEMS = [S.om7, S.or_hq, S.rh_vien, S.sig42]
    STATIC_NPCSHIPS = NPCSHIPS
    INIT_TITLE = ''
    INIT_OFFER = ''
    ACCEPT_TITLE = 'Миссия 11. Засада на Рокфорда'
    ACCEPT_OFFER = 'Предложение миссии'
    RTC = ['rescued', 'alaric', 'ambush', 'drink', 'harajuku_launch_rtc']

    def get_save_states(self):
        return [
            SaveState(self, 'hq_battle', 'Штаб Ордена. Битва у Вавилона'),
        ]

    def get_static_points(self):
        defined_points = []

        # Omega 7

        om7_points = [
            'rockford_chase1',
            'rockford_chase2',
            'rockford_chase3',
            'rockford_chase4',
        ]
        for p in om7_points:
            defined_points.append(
                Point(self, S.om7, p)
            )

        defined_points.append(
            Solar(self, S.om7, 'om7_musashi1',
                  ru_name='Линкор Мусаси', base='om7_99_base'),
        )
        defined_points.append(
            Solar(self, S.rh_vien, 'vien_flagship_solar',
                  ru_name='Линкор Гнейзенау',
                  labels=['enemy', 'rh_battleship', 'rheinland', 'vienna_defend']),
        )
        defined_points.append(
            DockableBattleshipSolar(
                self, S.rh_vien, 'vien_musashi1',
                ru_name='Линкор Мусаси', base='rh_vien_99_base',
                labels=['enemy', 'ku_battleship', 'ku', 'order', 'vienna_assault']),
        )

        # Order Headquarters

        hq_points = [
            'terra1',
            'terra2',
            'terra3',
            'to_vien1',
            'to_vien2',
            'to_sirius1',
            'to_sirius2',
        ]
        for p in hq_points:
            defined_points.append(
                Point(self, S.or_hq, p)
            )

        defined_points.append(
            StaticJumpgate(self, S.or_hq, 'jg_or_hq_to_rh_vienna', ru_name='Гиперврата в Вену'),
        )
        defined_points.append(
            StaticJumpgate(self, S.or_hq, 'jg_or_hq_to_sirius', ru_name='Гиперврата в Сириус'),
        )

        defined_points.append(
            Solar(self, S.or_hq, 'or_hq_musashi1',
                  ru_name='Линкор Мусаси', base='or_hq_99_base'),
        )

        # Vienna

        boxes = 16
        vienn_solars = [f'BOX{i:02d}' for i in range(1, boxes+1)]
        for sol in vienn_solars:
            defined_points.append(
                Solar(self, S.rh_vien, sol, ru_name='Исследовательский контейнер'),
            )

        vien_points = [
            'vienna_battle_zone',
        ]
        for p in vien_points:
            defined_points.append(
                Point(self, S.rh_vien, p)
            )

        defined_points.append(
            Solar(self, S.rh_vien, 'lair_power_cell', ru_name='Энергоядро Номадов'),
        )

        return defined_points

    def get_capital_ships(self):
        hq_rcr = {
            'npc_ship_arch': 'ms11_rh_cruiser',
            'faction': 'rh_grp',
            'labels': ['enemy', 'rh_cruiser', 'rheinland', 'hq_attack'],
            'ru_name': N.RH_CRUISER,
        }
        hq_kd = {
            'npc_ship_arch': 'ms11_ku_destroyer',
            'faction': 'or_grp',
            'labels': ['friend', 'ku_destroyer', 'ku', 'order'],
            'ru_name': N.KU_DESTROYER,
        }

        vien_rcr = {
            'npc_ship_arch': 'ms11_rh_cruiser',
            'faction': 'rh_grp',
            'labels': ['enemy', 'rh_cruiser', 'rheinland', 'vienna_defend'],
            'ru_name': N.RH_CRUISER,
        }
        vien_kd = {
            'npc_ship_arch': 'ms11_ku_destroyer',
            'faction': 'or_grp',
            'labels': ['friend', 'ku_destroyer', 'ku', 'order', 'vienna_assault'],
            'ru_name': N.KU_DESTROYER,
        }

        vien_rbs = {
            'npc_ship_arch': 'ms11_rh_battleship',
            'faction': 'rh_grp',
            'labels': ['enemy', 'rh_battleship', 'rheinland', 'vienna_defend'],
        }

        rockford = {
            'npc_ship_arch': 'ms11_rockford',
            'faction': 'fc_uk_grp',
            'labels': ['rtc'],
        }
        wilham = {
            'npc_ship_arch': 'm11_wilham',
            'faction': 'fc_uk_grp',
            'labels': ['rtc'],
        }

        caps = []
        hq_rcrs = []
        hq_kds = []
        vien_rcrs = []
        vien_kds = []

        hq_caps = 4
        vien_rcrs_count = 3
        vien_ku_caps = 2

        for index in range(1, hq_caps+1):
            cap = f'hq_rcr{index}'
            the_cap = Capital(self, cap, **hq_rcr)
            caps.append(the_cap)
            hq_rcrs.append(the_cap)

        self.add_capital_group('HQ_RCR', hq_rcrs)

        for index in range(1, hq_caps+1):
            cap = f'hq_kd{index}'
            the_cap = Capital(self, cap, **hq_kd)
            caps.append(the_cap)
            hq_kds.append(the_cap)

        self.add_capital_group('HQ_KD', hq_kds)

        for index in range(1, vien_rcrs_count+1):
            cap = f'vien_rcr{index}'
            the_cap = Capital(self, cap, **vien_rcr)
            caps.append(the_cap)
            vien_rcrs.append(the_cap)

        self.add_capital_group('VIEN_RCR', vien_rcrs)

        for index in range(1, vien_ku_caps+1):
            cap = f'vien_kd{index}'
            the_cap = Capital(self, cap, **vien_kd)
            caps.append(the_cap)
            vien_kds.append(the_cap)

        self.add_capital_group('VIEN_KD', vien_kds)

        caps.append(
            Capital(self, 'rockford', ru_name='Рокфорд', **rockford)
        )

        caps.append(
            Capital(self, 'wilham', ru_name='Вильгельм', **wilham)
        )

        caps.append(
            Capital(self, 'vien_flagship', ru_name='Линкор Гнейзенау', **vien_rbs)
        )

        return caps

    def get_ingame_thorns(self):
        return [
            IngameThorn(
                self,
                system_class=S.rh_vien,
                template=GENERIC_MOUNTED_ROTATABLE,
                name='m11_wilham_run',
                params={
                    'cam_pos_x': 50,
                    'cam_pos_y': -10,
                    'cam_pos_z': 10,
                    'rotate_duration': 30,
                    'rotate_angle': -30,
                    'remove_smooth': True,
                },
                duration=60,
                target='wilham',
            ),
            IngameThorn(
                self,
                system_class=S.rh_vien,
                template=GENERIC_TWO_POINT,
                name='m11_wilham_death',
                points={
                    'camera': 'death_cam',
                    'marker': 'death_marker',
                },
                duration=12,
            ),
            IngameThorn(
                self,
                system_class=S.rh_vien,
                template=GENERIC_TWO_POINT_MOVE,
                name='m11_cell_tractor',
                points={
                    'camera': 'cell_cam',
                    'marker': 'lair_power_cell',
                    'marker_two': 'lair_power_cell_mrk2',
                },
                params={
                    'move_duration': 40,
                },
                duration=12,
            ),
            IngameThorn(
                self,
                system_class=S.rh_vien,
                template=GENERIC_TWO_POINT,
                name='m11_rockford_flee',
                points={
                    'camera': 'rockford_cam',
                    'marker': 'rockford_cam_flee',
                },
                duration=12,
            ),
            IngameThorn(
                self,
                system_class=S.or_hq,
                template=GENERIC_MOUNTED_ROTATABLE,
                name='m11_hq_road_cam1',
                params={
                    'cam_pos_x': 50,
                    'cam_pos_y': -10,
                    'cam_pos_z': 10,
                    'rotate_duration': 60,
                    'rotate_angle': -720,
                    'remove_smooth': True,
                },
                duration=60,
                target='edison_trent',
            ),


        ]

    def get_real_objects(self):
        return {
            'om7_tlr_1': Conn(self, om7.Om7KusariStationConn1, om7.Om7HokkaidoJumpgate),
            'harajuku': Obj(self, om7.Om7KusariStation),

            'order_hq_jump': Obj(self, om7.Om7OrderJumpgate),

            'sig42_tlr_1': Conn(self, sig42.Sig42KusariStationConn3, sig42.Sig42KusariStation),
            'sprague': Obj(self, sig42.Sig42Dockring),
        }

    def get_nn_objectives(self):
        return [
            NNObj(self, O.LAUNCH, name='launch'),

            NNObj(self, O.TLR, target='om7_tlr_1'),
            NNObj(self, 'Сядьте на Харадзюку', target='harajuku'),

            NNObj(self, O.CHASE_ROCKFORD, name='rockford_chase1', target='rockford_chase1'),
            NNObj(self, O.CHASE_ROCKFORD, name='rockford_chase2', target='rockford_chase2'),
            NNObj(self, O.CHASE_ROCKFORD, name='rockford_chase3', target='rockford_chase3'),
            NNObj(self, O.CHASE_ROCKFORD, name='rockford_chase4', target='rockford_chase4'),

            NNObj(self, O.GOTO_JUMPGATE, name='order_hq_jump_fly', target='order_hq_jump', towards=True),
            NNObj(self, O.JUMPGATE, target='order_hq_jump'),

            NNObj(self, O.GOTO, name='terra1', target='terra1'),
            NNObj(self, O.GOTO, name='terra2', target='terra2'),
            NNObj(self, O.GOTO, name='terra3', target='terra3'),

            NNObj(self, 'Уничтожьте рейнландские корабли', name='hq_fight'),

            NNObj(self, O.GOTO, name='to_vien1', target='to_vien1'),
            NNObj(self, O.GOTO, name='to_vien2', target='to_vien2'),

            NNObj(self, O.JUMPGATE, name='jump_vienna', target='jg_or_hq_to_rh_vienna'),

            NNObj(self, O.GOTO, name='to_the_vienna', target='vienna_battle_zone'),

            NNObj(self, 'Уничтожьте исследовательские контейнеры', name='vienna_destroy_scient'),
            NNObj(self, 'Уничтожьте рейнландский флагман', name='vienna_destroy_flagship'),

            NNObj(self, 'Сядьте на линкор Мусаси', name='dock_vien_musashi', target='vien_musashi1'),

            NNObj(self, 'Подберите артефакт', name='get_the_loot'),

            NNObj(self, O.GOTO, name='to_sirius1', target='to_sirius1'),
            NNObj(self, O.GOTO, name='to_sirius2', target='to_sirius2'),

            NNObj(self, O.JUMPGATE, name='jump_into_sirius', target='jg_or_hq_to_sirius'),

            NNObj(self, O.TLR, target='sig42_tlr_1'),
            NNObj(self, 'Сядьте на планету Спрага', target='sprague'),

        ]

    def get_ships(self):
        return [
            Ship(
                self,
                'kim',
                jumper=False,
                hero=True,
                actor=actors.Kim,
                labels=[
                    'friend',
                    'order',
                ],
                npc=NPC(
                    faction=faction.OrderMain,
                    ship=ship.Dragon,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=6),
                )
            ),
            Ship(
                self,
                'killer',
                count=3,
                system_class=S.om7,
                labels=[
                    'friend',
                    'order',
                ],
                slide_x=100,
                unique_npc_entry=True,
                base_name='Лямбда',
                npc=NPC(
                    faction=faction.KusariMain,
                    ship=ship.Dragon,
                    level=NPC.D6,
                    equip_map=EqMap(base_level=6),
                )
            ),
            # HQ
            Ship(
                self,
                'hq_ku1',
                count=4,
                affiliation=faction.OrderMain.CODE,
                system_class=S.or_hq,
                slide_x=50,
                slide_z=50,
                labels=[
                    'hq_defence',
                    'order',
                    'friend',
                ],
                npc=NPC(
                    faction=faction.KusariMain,
                    ship=ship.Dragon,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'hq_ku2',
                count=4,
                affiliation=faction.OrderMain.CODE,
                system_class=S.or_hq,
                slide_x=-50,
                slide_z=50,
                labels=[
                    'hq_defence',
                    'order',
                    'friend',
                ],
                npc=NPC(
                    faction=faction.KusariMain,
                    ship=ship.Dragon,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'hq_rh1',
                count=5,
                affiliation=faction.RheinlandMain.CODE,
                system_class=S.or_hq,
                slide_z=50,
                labels=[
                    'hq_attack',
                    'rheinland',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'hq_rh2',
                count=5,
                affiliation=faction.RheinlandMain.CODE,
                system_class=S.or_hq,
                slide_z=50,
                labels=[
                    'hq_attack',
                    'rheinland',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            # VIEN
            Ship(
                self,
                'vien_kf1',
                count=3,
                affiliation=faction.OrderMain.CODE,
                system_class=S.rh_vien,
                slide_x=100,
                slide_z=100,
                labels=[
                    'vien_assault',
                    'order',
                    'friend',
                ],
                npc=NPC(
                    faction=faction.KusariMain,
                    ship=ship.Dragon,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'vien_kf2',
                count=3,
                affiliation=faction.OrderMain.CODE,
                system_class=S.rh_vien,
                slide_x=100,
                slide_z=100,
                labels=[
                    'vien_assault',
                    'order',
                    'friend',
                ],
                npc=NPC(
                    faction=faction.KusariMain,
                    ship=ship.Dragon,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'vien_rf1',
                count=4,
                affiliation=faction.RheinlandMain.CODE,
                system_class=S.rh_vien,
                slide_z=200,
                labels=[
                    'vien_defence',
                    'rheinland',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'vien_rf2',
                count=4,
                affiliation=faction.RheinlandMain.CODE,
                system_class=S.rh_vien,
                slide_z=200,
                labels=[
                    'vien_defence',
                    'rheinland',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'vien_rf3',
                count=4,
                affiliation=faction.RheinlandMain.CODE,
                system_class=S.rh_vien,
                slide_z=200,
                labels=[
                    'vien_defence',
                    'rheinland',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'edison_trent',
                actor=actors.EdisonTrent,
                labels=[
                    'friend',
                ],
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Titan,
                    level=NPC.D19,
                    equip_map=EqMap(base_level=6),
                )
            ),


        ]
