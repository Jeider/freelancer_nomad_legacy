import random

from universe import sirius as S
from universe.systems import sig42
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors
from story.ingame import names as N

from story.ingame import objectives as O
from story.ingame.tools import (Point, Obj, Conn, NNObj, Ship, Solar, Capital, DockableBattleshipSolar, SaveState,
                                MultiLine)
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT

from world.npc import NPC, EqMap
from world import ship
from universe import faction

from text.strings import MultiString as MS

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
loadout = li_dreadnought_03
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
    START_SAVE_ID = 33200
    START_SAVE_RU_NAME = MS('Сириус. Планета Спрага', 'Sirius. Planet Sprague')
    SCRIPT_INDEX = 12
    DIRECT_SYSTEMS = [S.sig42, S.asf_hq, S.asf_prom]
    STATIC_NPCSHIPS = NPCSHIPS
    RTC = ['sprague']
    INIT_OFFER = MultiLine(
        [
            'ЗАДАЧА:',
            'Не допустить уничтожение станции Энтерпрайз и штаба СБА.',
            '',
            'СЛОЖНОСТЬ:',
            'Спасти человечество.',
            '',
            'Награда:',
            'Выживание',
        ],
        [
            'OBJECTIVE:',
            'Don not let Order destroy Station Enterprise and ASF Headquarters.',
            '',
            'DIFFICULTY:',
            'Save the mankind.',
            '',
            'REWARD:',
            'Survival',
        ]
    ).get_content()

    def get_save_states(self):
        return [
            SaveState(self, 'bush_battle', MS('Штаб СБА. Битва в секторе форта Буш', "ASF's HQ. Battle in sector of Fort Bush")),
            SaveState(self, 'logos_battle', MS('Прометей. Нейтрализация линкора Логос', 'Proemetheus. Neutralization of the battleship Logos')),
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
            ('ku_miner01', MS('Инженерное судно Кохая', 'Engineer vessel Cochaya')),
            ('ku_miner02', MS('Инженерное судно Сюинсэн', 'Engineer vessel Sinsene')),
            ('ku_miner03', MS('Инженерное судно Урал', 'Engineer vessel Ural')),
            ('fort_bush', MS('Форт Буш', 'Fort Bush')),
            ('fort1', MS('Форт Джефферсон', 'Fort Jefferson')),
            ('fort2', MS('Форт Аламо', 'Fort Alamo')),
            ('fort3', MS('Форт Стармер', 'Fort Starmer')),
            ('fort4', MS('Форт Росс', 'Fort Ross')),
            ('fort5', MS('Форт Нокс', 'Fort Nox')),

            ('counter_relative_obj', MS('счётчик', 'counter')),
            ('counter_assault', MS('счётчик', 'counter')),

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
            ('prom_osiris_emi', MS('ЭМИ Осириса', "Osiris' EMI gun")),
        ]
        for sol, name in prom_solars:
            defined_points.append(
                Solar(self, S.asf_prom, sol, ru_name=name),
            )

        defined_points.append(
            DockableBattleshipSolar(
                self, S.asf_prom, 'logos',
                ru_name=MS('Линкор Логос', 'Battleship Logos'), base='asf_prom_99_base',
                labels=['enemy', 'or_b', 'logos']),
        )
        defined_points.append(
            DockableBattleshipSolar(
                self, S.asf_prom, 'prom_osiris', faction='asf_grp',
                ru_name=N.OSIRIS, base='asf_prom_99_base',
                labels=['friend', 'asf', 'osiris']),
        )

        logos_segments = [
            ('logos_shieldgen', MS('Генератор щита Логоса', "Logos' Shield Generator")),
            ('logos_shieldgen_dmg', MS('Генератор щита Логоса', "Logos' Shield Generator")),
            ('logos_control_tower', MS('Рубка Логоса', "Logos' Control Tower")),
            ('logos_control_tower_dmg', MS('Рубка Логоса', "Logos' Control Tower")),
            ('logos_reactor', MS('Реактор Логоса', "Logos' Reactor")),
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
            Capital(self, 'road_ku_bship', ru_name=MS('Линкор Муцу', 'Battleship Mutsu'), **ku_bship),
            Capital(self, 'road_li_dread', ru_name=MS('Линкор Коннектикут', "Battleship Connecticut"), **li_dread),
            Capital(self, 'road_ku_destroyer1', ru_name=MS('Эсминец Амаги', "Amagi Destroyer"), **ku_destroyer),
            Capital(self, 'road_ku_destroyer2', ru_name=MS('Эсминец Конго', 'Congo Destroyer'), **ku_destroyer),
            Capital(self, 'omaha1', ru_name=MS('Крейсер Омаха', "Omaha Cruiser"), **omaha),
            Capital(self, 'omaha2', ru_name=MS('Крейсер Делавэр', 'Delaware Cruiser'), **omaha),
            Capital(self, 'omaha3', ru_name=MS('Крейсер Юта', 'Utah Cruiser'), **omaha),

            Capital(self, 'nagato', ru_name=MS('Линкор Нагато', 'Battleship Nagato'), **ku_bship),

            Capital(self, 'to_bush_ku_bship', ru_name=MS('Линкор Кавати', 'Battleship Kawachi'), **ku_bship),
            Capital(self, 'to_bush_li_dread', ru_name=MS('Линкор Вермонт', 'Battleship Vermont'), **li_dread),

            Capital(self, 'ku_assault1', ru_name=MS('Линкор Ямато', 'Battleship Yamato'), **ku_bship_assault),
            Capital(self, 'ku_assault2', ru_name=MS('Линкор Тоса', 'Battleship Tosa'), **ku_bship_assault),
            Capital(self, 'ku_assault3', ru_name=MS('Линкор Исэ', 'Battleship Ise'), **ku_bship_assault),

            Capital(self, 'ku_cr_assault1', ru_name=MS('Эсминец Катори', 'Katori Destroyer'), **ku_destroyer),
            Capital(self, 'ku_cr_assault2', ru_name=MS('Эсминец Сикисима', 'Shikishima Destroyer'), **ku_destroyer),
            Capital(self, 'ku_cr_assault3', ru_name=MS('Эсминец Фудзи', 'Fuji Destroyer'), **ku_destroyer),
            Capital(self, 'ku_cr_assault4', ru_name=MS('Эсминец Чин-Иен', 'Chin Yen Destroyer'), **ku_destroyer),

            Capital(self, 'li_cr_defend1', ru_name=MS('Крейсер Теннесси', 'Tennessee Cruiser'), **li_cruiser),
            Capital(self, 'li_cr_defend2', ru_name=MS('Крейсер Монтана', 'Montana Cruiser'), **li_cruiser),

            Capital(self, 'osiris_on_assault', ru_name=N.OSIRIS, **asf_osiris),
        ]

        OR_PROM_A = [
            ('prom_A_order_01', MS('Линкор Навухудоносор', 'Battleship Nebuchadnezzar')),
            ('prom_A_order_02', MS('Линкор Брахма', 'Battleship Brahma')),
            ('prom_A_order_03', MS('Линкор Кадуцеус', 'Battleship Caduceus')),
            ('prom_A_order_04', MS('Линкор Вигилант', 'Battleship Vigilant')),
        ]
        OR_PROM_B = [
            ('prom_B_order_02', MS('Линкор Ганеша', 'Battleship Ganesha')),
            ('prom_B_order_03', MS('Линкор Икарус', 'Battleship Ikarus')),
            ('prom_B_order_04', MS('Линкор Артаксеркс', 'Battleship Artaxerxes')),
            ('prom_B_order_05', MS('Линкор Хаммер', 'Battleship Hammer')),
        ]
        prom_or_ships = []

        ASF_PROM_A = [
            ('prom_A_asf_01', MS('Линкор Орегон', 'Battleship Oregon')),
            ('prom_A_asf_02', MS('Линкор Кентукки', 'Battleship Kentucky')),
        ]
        ASF_PROM_B = [
            ('prom_B_asf_01', MS('Линкор Цинцинатти', 'Battleship Cincinnati')),
            ('prom_B_asf_02', MS('Линкор Рио-Гранде', 'Battleship Rio-Grande')),
        ]
        prom_asf_ships = []

        for cap, name in OR_PROM_A:
            the_cap = Capital(self, cap, ru_name=name, **order_osiris_a)
            caps.append(the_cap)
            prom_or_ships.append(the_cap)

        for cap, name in OR_PROM_B:
            the_cap = Capital(self, cap, ru_name=name, **order_osiris_b)
            caps.append(the_cap)
            prom_or_ships.append(the_cap)

        for cap, name in ASF_PROM_A:
            the_cap = Capital(self, cap, ru_name=name, **li_dread_a)
            caps.append(the_cap)
            prom_asf_ships.append(the_cap)

        for cap, name in ASF_PROM_B:
            the_cap = Capital(self, cap, ru_name=name, **li_dread_b)
            caps.append(the_cap)
            prom_asf_ships.append(the_cap)

        self.add_capital_group('PROM_ORDER', prom_or_ships)
        self.add_capital_group('PROM_ASF', prom_asf_ships)

        caps.append(
            Capital(self, 'armored', ru_name=N.ARMORED, **armored_ship)
        )
        caps.append(
            Capital(self, 'armored_out', ru_name=N.ARMORED, **armored_ship_out)
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

            NNObj(self, MS('Уничтожьте инженерные судна', "Destroy engineering vessels"), name='destroy_miners'),

            NNObj(self, O.GOTO, name='to_bush01', target='to_bush01'),
            NNObj(self, O.GOTO, name='to_bush02', target='to_bush02'),
            NNObj(self, O.GOTO, name='to_bush03', target='to_bush03'),
            NNObj(self, O.GOTO, name='to_bush04', target='to_bush04'),
            NNObj(self, O.GOTO, name='to_bush05', target='to_bush05'),
            NNObj(self, O.GOTO, name='to_bush06', target='to_bush06'),

            NNObj(self, MS('Уничтожьте двигатели линкоров Кусари', "Destroy engines of Kusari battleships"),
                  name='stop_assault_battleships'),

            NNObj(self, MS('Влетите внутрь сферы станции Энтерпрайз',
                           'Enter inside blue sphere of station Enterprise'), name='jump_to_prom', target='m13_asf_hq_01'),

            NNObj(self,  O.GOTO, name='prom_goinsde1', target='prom_goinsde1'),
            NNObj(self,  O.GOTO, name='prom_goinsde2', target='prom_goinsde2'),
            NNObj(self,  O.GOTO, name='prom_goinsde3', target='prom_goinsde3'),

            NNObj(self, MS('Доберитесь до Логоса', 'Go to Battleship Logos'), name='goto_logos', target='logos', towards=True),

            NNObj(self, MS('Ожидайте прибытия линкора Осирис', 'Wait for arrive of Battleship Osiris'), name='wait_osiris'),

            NNObj(self, MS('Уничтожьте генератор щита Логоса', "Destroy Logos' shield generator"), name='logos_shieldgen', target='logos_shieldgen'),
            NNObj(self, MS('Уничтожьте командный мостик Логоса', "Destroy Logos' control tower"), name='logos_control_tower', target='logos_control_tower'),
            NNObj(self, MS('Уничтожьте реактор Логоса', "Destroy Logos' reactor"), name='logos_reactor', target='logos_reactor'),

            NNObj(self, MS('Обеспечьте безопасность десантного судна', 'Defend friendly landing craft'), name='defend_armored'),
            NNObj(self, MS('Ожидайте пленения Ямамото', 'Wait for capture of Yamamoto'), name='wait_for_armored'),
            NNObj(self, MS('Ожидайте доставки Ямамото на Осирис',
                           'Wait for delivery of Yamamoto on Osiris'), name='wait_for_armored_osiris'),

            NNObj(self, MS('Сядьте на линкор Осирис', 'Dock with Osiris'), name='dock_osiris', target='prom_osiris'),
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
                    level=NPC.D12,
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
                    level=NPC.D12,
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
                    level=NPC.D12,
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
                    ship=ship.Crusader,
                    level=NPC.D15,
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
                    level=NPC.D15,
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
                    level=NPC.D12,
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
                    level=NPC.D12,
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
                    level=NPC.D12,
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
                    level=NPC.D12,
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
                    ship=ship.DefenderJuni,
                    level=NPC.D12,
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
                    ship=ship.DefenderJuni,
                    level=NPC.D12,
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
                    level=NPC.D12,
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
                    ship=ship.DefenderJuni,
                    level=NPC.D12,
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
                    level=NPC.D13,
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
                    level=NPC.D13,
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
                    ship=ship.DefenderJuni,
                    level=NPC.D12,
                    equip_map=EqMap(base_level=6),
                )
            ),
        ]
