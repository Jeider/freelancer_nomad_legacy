import random

from universe import sirius as S
from universe.systems import sig42
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors

from story.ingame import objectives as O
from story.ingame.tools import Point, Obj, Conn, NNObj, Ship, Solar, Capital, DockableBattleshipSolar, SaveState
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT

from world.npc import NPC, EqMap
from world import ship
from universe import faction

NPCSHIPS = '''
nickname = ms12_ku_gunboat
loadout = ku_grp_gunboat
level = d10
ship_archetype = ku_gunboat
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

[NPCShipArch]
nickname = ms12_ku_destroyer
loadout = ku_grp_destroyer
level = d10
ship_archetype = ku_destroyer
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

[NPCShipArch]
nickname = ms12_ku_battleship
loadout = ku_grp_battleship
level = d10
ship_archetype = ku_battleship
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

[NPCShipArch]
nickname = ms12_ku_battleship_assault
loadout = ku_battleship_m13_assault
level = d10
ship_archetype = ku_battleship_m13_assault
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5



[NPCShipArch]
nickname = ms12_li_dread
loadout = li_dreadnought_03_surv1_evil
level = d10
ship_archetype = li_dreadnought
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

[NPCShipArch]
nickname = ms12_li_cruiser
loadout = li_grp_cruiser
level = d10
ship_archetype = li_cruiser
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

[NPCShipArch]
nickname = ms12_osiris
loadout = li_battleship_02
level = d10
ship_archetype = or_osiris
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

[NPCShipArch]
nickname = ms12_logos
loadout = logos
level = d10
ship_archetype = or_logos
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

[NPCShipArch]
nickname = ms12_armored
loadout = m12_armored
level = d10
ship_archetype = ge_armored
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5


'''


class Misson12(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m12/m12.ini'
    FOLDER = 'M12'
    FILE = 'm12'
    SCRIPT_INDEX = 12
    DIRECT_SYSTEMS = [S.sig42, S.asf_hq, S.asf_prom]
    STATIC_NPCSHIPS = NPCSHIPS
    RTC = ['sprague']

    def get_save_states(self):
        return [
            SaveState(self, 'bush_battle', 'Штаб СБА. Битва в секторе форта Буш'),
            SaveState(self, 'logos_battle', 'Прометей. Нейтрализация линкора Логос'),
        ]

    def get_static_points(self):
        defined_points = []

        # ASF

        hq_points = [
            'asf_miner01',
            'asf_miner02',
            'to_bush01',
            'to_bush02',
            'to_bush03',
            'to_bush04',
            'to_bush05',
            'to_bush06',
            'm13_asf_hq_01',
        ]
        for p in hq_points:
            defined_points.append(
                Point(self, S.asf_hq, p)
            )

        hq_solars = [
            ('ku_miner01', 'Добывающее судно Кохая'),
            ('ku_miner02', 'Добывающее судно Сюинсэн'),
            ('ku_miner03', 'Добывающее судно Урал'),
            ('fort_bush', 'Форт Буш'),
            ('fort1', 'Форт Джефферсон'),
            ('fort2', 'Форт Аламо'),
            ('fort3', 'Форт Стармер'),
            ('fort4', 'Форт Росс'),
            ('fort5', 'Форт Нокс'),

            ('counter_relative_obj', 'счётчик'),
            ('counter_assault', 'счётчик'),

        ]
        for sol, name in hq_solars:
            defined_points.append(
                Solar(self, S.asf_hq, sol, ru_name=name),
            )

        # PROM

        prom_points = [
            'prom_goinsde1',
            'prom_goinsde2',
            'prom_goinsde3',

            'prom_logos',
        ]
        for p in prom_points:
            defined_points.append(
                Point(self, S.asf_prom, p)
            )

        prom_solars = [
            ('prom_osiris_emi', 'ЭМИ Осириса'),

            ('logos_checker', 'счетчик'),
            ('logos_dmg_90', '9'),
            ('logos_dmg_80', '8'),
            ('logos_dmg_70', '7'),
            ('logos_dmg_60', '6'),
            ('logos_dmg_50', '5'),
            ('logos_dmg_40', '4'),
            ('logos_dmg_30', '3'),
        ]
        for sol, name in prom_solars:
            defined_points.append(
                Solar(self, S.asf_prom, sol, ru_name=name),
            )

        defined_points.append(
            DockableBattleshipSolar(
                self, S.asf_prom, 'logos',
                ru_name='Линкор Логос', base='rh_vien_99_base',
                labels=['enemy', 'or_b', 'logos']),
        )
        defined_points.append(
            DockableBattleshipSolar(
                self, S.asf_prom, 'prom_osiris',
                ru_name='Линкор Осирис', base='rh_vien_99_base',
                labels=['friend', 'asf', 'osiris']),
        )


        logos_segments = [
            ('logos_shieldgen', 'Генератор щита Логоса'),
            ('logos_shieldgen_dmg', 'Генератор щита Логоса'),
            ('logos_control_tower', 'Рубка Логоса'),
            ('logos_control_tower_dmg', 'Рубка Логоса'),
            ('logos_reactor', 'Реактор Логоса'),
        ]
        for p, name in logos_segments:
            defined_points.append(
                Solar(self, S.asf_prom, p, ru_name=name, labels=['enemy', 'or_b', 'logos'])
            )

        return defined_points

    def get_capital_ships(self):
        ku_bship = {
            'npc_ship_arch': 'ms12_ku_battleship',
            'faction': 'or_grp',
            'labels': ['enemy'],
        }
        ku_destroyer = {
            'npc_ship_arch': 'ms12_ku_destroyer',
            'faction': 'or_grp',
            'labels': ['enemy', 'ku_destroyer'],
        }
        li_dread = {
            'npc_ship_arch': 'ms12_li_dread',
            'faction': 'asf_grp',
            'labels': ['friend', 'asf'],
        }
        omaha = {
            'npc_ship_arch': 'ms12_li_cruiser',
            'faction': 'asf_grp',
            'labels': ['friend', 'omaha', 'asf', 'li_cruiser'],
        }
        li_cruiser = {
            'npc_ship_arch': 'ms12_li_cruiser',
            'faction': 'asf_grp',
            'labels': ['friend', 'asf', 'li_cruiser'],
        }
        ku_bship_assault = {
            'npc_ship_arch': 'ms12_ku_battleship_assault',
            'faction': 'or_grp',
            'labels': ['ku_bship_assault'],
        }
        asf_osiris = {
            'npc_ship_arch': 'ms12_osiris',
            'faction': 'asf_grp',
            'labels': ['friend', 'asf'],
        }

        order_osiris_a = {
            'npc_ship_arch': 'ms12_osiris',
            'faction': 'or_grp',
            'labels': ['or_a', 'or_osiris'],
        }
        order_logos = {
            'npc_ship_arch': 'ms12_logos',
            'faction': 'or_grp',
            'labels': ['enemy', 'or_b', 'logos'],
        }
        order_osiris_b = {
            'npc_ship_arch': 'ms12_osiris',
            'faction': 'or_grp',
            'labels': ['enemy', 'or_b', 'or_osiris'],
        }
        li_dread_a = {
            'npc_ship_arch': 'ms12_li_dread',
            'faction': 'asf_grp',
            'labels': ['friend', 'asf_a', 'asf'],
        }
        li_dread_b = {
            'npc_ship_arch': 'ms12_li_dread',
            'faction': 'asf_grp',
            'labels': ['friend', 'asf_b', 'asf'],
        }
        armored_ship = {
            'npc_ship_arch': 'ms12_armored',
            'faction': 'asf_grp',
            'labels': [],
        }
        armored_ship_out = {
            'npc_ship_arch': 'ms12_armored',
            'faction': 'asf_grp',
            'labels': [],
            'arrival_obj': 'logos',
        }

        caps = [
            Capital(self, 'road_ku_bship', ru_name='Линкор Муцу', **ku_bship),
            Capital(self, 'road_li_dread', ru_name='Линкор Коннектикут', **li_dread),
            Capital(self, 'road_ku_destroyer1', ru_name='Эсминец Амаги', **ku_destroyer),
            Capital(self, 'road_ku_destroyer2', ru_name='Эсминец Конго', **ku_destroyer),
            Capital(self, 'omaha1', ru_name='Крейсер Омаха', **omaha),
            Capital(self, 'omaha2', ru_name='Крейсер Делавэр', **omaha),
            Capital(self, 'omaha3', ru_name='Крейсер Юта', **omaha),

            Capital(self, 'nagato', ru_name='Линкор Нагато', **ku_bship),

            Capital(self, 'to_bush_ku_bship', ru_name='Линкор Кавати', **ku_bship),
            Capital(self, 'to_bush_li_dread', ru_name='Линкор Вермонт', **li_dread),

            Capital(self, 'ku_assault1', ru_name='Линкор Ямато', **ku_bship_assault),
            Capital(self, 'ku_assault2', ru_name='Линкор Тоса', **ku_bship_assault),
            Capital(self, 'ku_assault3', ru_name='Линкор Исэ', **ku_bship_assault),

            Capital(self, 'ku_cr_assault1', ru_name='Эсминец Катори', **ku_destroyer),
            Capital(self, 'ku_cr_assault2', ru_name='Эсминец Сикисима', **ku_destroyer),
            Capital(self, 'ku_cr_assault3', ru_name='Эсминец Фудзи', **ku_destroyer),
            Capital(self, 'ku_cr_assault4', ru_name='Эсминец Чин-Иен', **ku_destroyer),

            Capital(self, 'li_cr_defend1', ru_name='Крейсер Теннесси', **li_cruiser),
            Capital(self, 'li_cr_defend2', ru_name='Крейсер Монтана', **li_cruiser),

            Capital(self, 'osiris_on_assault', ru_name='Линкор Осирис', **asf_osiris),
        ]

        OR_PROM_A = [
            ('prom_A_order_01', 'Навухудоносор'),
            ('prom_A_order_02', 'Брахма'),
            ('prom_A_order_03', 'Кадуцеус'),
            ('prom_A_order_04', 'Вигилант'),
        ]
        OR_PROM_B = [
            ('prom_B_order_02', 'Ганеша'),
            ('prom_B_order_03', 'Икарус'),
            ('prom_B_order_04', 'Артаксеркс'),
            ('prom_B_order_05', 'Хаммер'),
        ]
        prom_or_ships = []

        ASF_PROM_A = [
            ('prom_A_asf_01', 'Орегон'),
            ('prom_A_asf_02', 'Кентукки'),
        ]
        ASF_PROM_B = [
            ('prom_B_asf_01', 'Цинцинатти'),
            ('prom_B_asf_02', 'Рио-Гранде'),
        ]
        prom_asf_ships = []

        for cap, name in OR_PROM_A:
            the_cap = Capital(self, cap, ru_name=f'Линкор {name}', **order_osiris_a)
            caps.append(the_cap)
            prom_or_ships.append(the_cap)

        for cap, name in OR_PROM_B:
            the_cap = Capital(self, cap, ru_name=f'Линкор {name}', **order_osiris_b)
            caps.append(the_cap)
            prom_or_ships.append(the_cap)

        for cap, name in ASF_PROM_A:
            the_cap = Capital(self, cap, ru_name=f'Линкор {name}', **li_dread_a)
            caps.append(the_cap)
            prom_asf_ships.append(the_cap)

        for cap, name in ASF_PROM_B:
            the_cap = Capital(self, cap, ru_name=f'Линкор {name}', **li_dread_b)
            caps.append(the_cap)
            prom_asf_ships.append(the_cap)

        self.add_capital_group('PROM_ORDER', prom_or_ships)
        self.add_capital_group('PROM_ASF', prom_asf_ships)

        caps.append(
            Capital(self, 'armored', ru_name='Бронированный транспорт', **armored_ship)
        )
        caps.append(
            Capital(self, 'armored_out', ru_name='Бронированный транспорт', **armored_ship_out)
        )

        return caps

    def get_real_objects(self):
        return {
            'asf_hq_jump': Obj(self, sig42.Sig42AsfJumpgate),
        }

    def get_nn_objectives(self):
        return [
            NNObj(self, O.LAUNCH, name='launch'),

            NNObj(self, O.GOTO_JUMPGATE, name='goto_jump_asf_hq', target='asf_hq_jump', towards=True),
            NNObj(self, O.JUMPGATE, name='jump_asf_hq', target='asf_hq_jump'),

            NNObj(self, O.GOTO, name='asf_miner01', target='asf_miner01'),
            NNObj(self, O.GOTO, name='asf_miner02', target='asf_miner02'),

            NNObj(self, 'Уничтожьте инженерные судна', name='destroy_miners'),

            NNObj(self, O.GOTO, name='to_bush01', target='to_bush01'),
            NNObj(self, O.GOTO, name='to_bush02', target='to_bush02'),
            NNObj(self, O.GOTO, name='to_bush03', target='to_bush03'),
            NNObj(self, O.GOTO, name='to_bush04', target='to_bush04'),
            NNObj(self, O.GOTO, name='to_bush05', target='to_bush05'),
            NNObj(self, O.GOTO, name='to_bush06', target='to_bush06'),

            NNObj(self, 'Уничтожьте двигатели линкоров Кусари', name='stop_assault_battleships'),

            NNObj(self, 'Влетите внутрь сферы станции Энтерпрайз', name='jump_to_prom', target='m13_asf_hq_01'),

            NNObj(self,  O.GOTO, name='prom_goinsde1', target='prom_goinsde1'),
            NNObj(self,  O.GOTO, name='prom_goinsde2', target='prom_goinsde2'),
            NNObj(self,  O.GOTO, name='prom_goinsde3', target='prom_goinsde3'),

            NNObj(self, 'Доберитесь до Логоса', name='goto_logos', target='logos', towards=True),

            NNObj(self, 'Ожидайте прибытия линкора Осирис', name='wait_osiris'),

            NNObj(self, 'Уничтожьте генератор щита Логоса', name='logos_shieldgen', target='logos_shieldgen'),
            NNObj(self, 'Уничтожьте командный мостик Логоса', name='logos_control_tower', target='logos_control_tower'),
            NNObj(self, 'Уничтожьте реактор Логоса', name='logos_reactor', target='logos_reactor'),

            NNObj(self, 'Обеспечьте безопасность десантного судна', name='defend_armored'),
            NNObj(self, 'Ожидайте пленения Ямамото', name='wait_for_armored'),
            NNObj(self, 'Ожидайте доставки Ямамото на Осирис', name='wait_for_armored_osiris'),

            NNObj(self, 'Сядьте на линкор Осирис', name='dock_osiris', target='prom_osiris'),
        ]

    def get_ships(self):
        return [
            Ship(
                self,
                'ku_miner_defence',
                count=3,
                affiliation=faction.OrderMain.CODE,
                system_class=S.asf_hq,
                slide_z=-100,
                labels=[
                    'miner_defence',
                    'new_order',
                    'enemy',
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
                'ku_miner_defence_resp',
                count=3,
                affiliation=faction.OrderMain.CODE,
                system_class=S.asf_hq,
                slide_x=100,
                labels=[
                    'miner_defence',
                    'new_order',
                    'enemy',
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
                'li_miner_help',
                count=5,
                affiliation=faction.ASF.CODE,
                system_class=S.asf_hq,
                slide_z=-50,
                labels=[
                    'li_miner_help',
                    'asf',
                    'friend',
                ],
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Defender,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'hatcher',
                jumper=True,
                hero=True,
                actor=actors.Hatcher,
                labels=[
                    'asf',
                    'friend',
                    'trent_wing',
                ],
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.DefenderJuni,
                    level=NPC.D12,
                    equip_map=EqMap(base_level=6),
                )
            ),
            Ship(
                self,
                'darcy',
                jumper=True,
                hero=True,
                actor=actors.Darcy,
                labels=[
                    'asf',
                    'friend',
                    'trent_wing',
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
                'alaric',
                jumper=True,
                hero=True,
                actor=actors.Alaric,
                labels=[
                    'asf',
                    'friend',
                    'trent_wing',
                ],
                npc=NPC(
                    faction=faction.LibertyPirate,
                    ship=ship.Hammerhead,
                    level=NPC.D19,
                    equip_map=EqMap(base_level=6),
                )
            ),

            Ship(
                self,
                'ku_f_assault1',
                count=3,
                affiliation=faction.OrderMain.CODE,
                system_class=S.asf_hq,
                slide_x=-50,
                labels=[
                    'assault',
                    'enemy_fighter',
                    'enemy',
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
                'ku_f_assault2',
                count=3,
                affiliation=faction.OrderMain.CODE,
                system_class=S.asf_hq,
                slide_x=-50,
                labels=[
                    'assault',
                    'enemy_fighter',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.KusariMain,
                    ship=ship.Drake,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),

            Ship(
                self,
                'ku_f_resp_assault1',
                count=3,
                affiliation=faction.OrderMain.CODE,
                system_class=S.asf_hq,
                slide_x=-50,
                labels=[
                    'assault',
                    'enemy_fighter',
                    'enemy',
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
                'ku_f_resp_assault2',
                count=3,
                affiliation=faction.OrderMain.CODE,
                system_class=S.asf_hq,
                slide_x=-50,
                labels=[
                    'assault',
                    'enemy_fighter',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.KusariMain,
                    ship=ship.Drake,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),

            Ship(
                self,
                'li_f_defend1',
                count=5,
                affiliation=faction.ASF.CODE,
                system_class=S.asf_hq,
                slide_z=-100,
                slide_x=-50,
                labels=[
                    'li_fighter',
                    'asf',
                    'friend',
                ],
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Defender,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'li_f_defend2',
                count=5,
                affiliation=faction.ASF.CODE,
                system_class=S.asf_hq,
                slide_z=-100,
                slide_x=50,
                labels=[
                    'li_fighter',
                    'asf',
                    'friend',
                ],
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Defender,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),

            # PROMETHEUS

            Ship(
                self,
                'or_prom_A',
                count=8,
                affiliation=faction.OrderMain.CODE,
                system_class=S.asf_prom,
                slide_x=50,
                slide_z=-50,
                labels=[
                    'or_a',
                    'enemy_fighter',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.OrderMain,
                    ship=ship.Anubis,
                    level=NPC.D6,
                    equip_map=EqMap(base_level=6),
                )
            ),

            Ship(
                self,
                'asf_prom_A',
                count=8,
                affiliation=faction.ASF.CODE,
                system_class=S.asf_prom,
                slide_x=50,
                slide_z=-50,
                labels=[
                    'asf_a',
                    'li_fighter',
                    'asf',
                    'friend',
                ],
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Defender,
                    level=NPC.D6,
                    equip_map=EqMap(base_level=6),
                )
            ),

            Ship(
                self,
                'or_prom_B1',
                count=4,
                affiliation=faction.OrderMain.CODE,
                system_class=S.asf_prom,
                slide_x=50,
                slide_z=50,
                labels=[
                    'or_b',
                    'enemy_fighter',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.OrderMain,
                    ship=ship.Anubis,
                    level=NPC.D19,
                    equip_map=EqMap(base_level=6),
                )
            ),
            Ship(
                self,
                'or_prom_B2',
                count=6,
                affiliation=faction.OrderMain.CODE,
                system_class=S.asf_prom,
                slide_x=50,
                slide_z=50,
                labels=[
                    'or_b',
                    'enemy_fighter',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.OrderMain,
                    ship=ship.Anubis,
                    level=NPC.D19,
                    equip_map=EqMap(base_level=6),
                )
            ),

            Ship(
                self,
                'asf_prom_B1',
                count=8,
                affiliation=faction.ASF.CODE,
                system_class=S.asf_prom,
                slide_x=50,
                slide_z=50,
                labels=[
                    'asf_b',
                    'li_fighter',
                    'asf',
                    'friend',
                ],
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Defender,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=6),
                )
            ),
        ]
