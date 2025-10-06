import random

from universe import sirius as S
from universe.systems import ku_tgk, sig42
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

[NPCShipArch]
nickname = ms9_br_destroyer_torpedo
loadout = m09_br_torp_destroyer
level = d10
ship_archetype = br_destroyer
pilot = cruiser_antisolar
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

[NPCShipArch]
nickname = ms9_br_gunboat
loadout = br_grp_gunboat
level = d19
ship_archetype = br_gunboat
pilot = gunboat_default
state_graph = GUNBOAT
npc_class = lawful, class_gunboat

[NPCShipArch]
nickname = ms9_li_dread
loadout = li_dreadnought_01
level = d10
ship_archetype = li_dreadnought
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

[NPCShipArch]
nickname = ms9_br_battleship
loadout = br_grp_battleship
level = d10
ship_archetype = br_battleship
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

[NPCShipArch]
nickname = m09_train
loadout = m09_train
level = d10
ship_archetype = ge_super_large_train
pilot = MSN01a_Large_Transport
state_graph = TRANSPORT
npc_class = lawful, transport_large

[NPCShipArch]
nickname = m09_repair
level = d10
ship_archetype = ge_repair
loadout = co_ge_repair_loadout01
pilot = MSN01a_Large_Transport
state_graph = TRANSPORT
npc_class = lawful, TRANSPORT 

[NPCShipArch]
nickname = m09_lifter
level = d10
ship_archetype = ge_lifter
loadout = co_ge_lifter_loadout01
ship_archetype = ge_lifter
pilot = MSN01a_Large_Transport
state_graph = TRANSPORT
npc_class = lawful, TRANSPORT

'''

BDR_NAMES = [
    MS('Эсминец Сарацин', 'Saracen Destroyer'),
    MS('Эсминец Мохок', 'Mohawk Destroyer'),
    MS('Эсминец Киплинг', 'Kipling Destroyer'),

    MS('Эсминец Маори', 'Maori Destroyer'),
    MS('Эсминец Нубиец', 'Nubian Destroyer'),
    MS('Эсминец Кимберли', 'Kimberley Destroyer'),

    MS('Эсминец Викинг', 'Viking Destroyer'),
    MS('Эсминец Юпитер', 'Jupiter Destroyer'),
    MS('Эсминец Нептун', 'Neptune Destroyer'),

    MS('Эсминец Уран', 'Uranus Destroyer'),
    MS('Эсминец Марс', 'Mars Destroyer'),
    MS('Эсминец Венера', 'Venus Destroyer'),

    MS('Эсминец Плутон', 'Pluto Destroyer'),
    MS('Эсминец Меркурий', 'Mercury Destroyer'),
    MS('Эсминец Сатурн', 'Saturn Destroyer'),

    MS('Эсминец Монтроз', 'Montrose Destroyer'),
    MS('Эсминец Маккей', 'Makkey Destroyer'),
    MS('Эсминец Хэвок', 'Havock Destroyer'),

    MS('Эсминец Нестор', 'Nestor Destroyer'),
    MS('Эсминец Онслоу', 'Onslow Destroyer'),
    MS('Эсминец Джервис', 'Jervis Destroyer'),

    MS('Эсминец Келли', 'Kelly Destroyer'),
    MS('Эсминец Джуно', 'Juno Destroyer'),
    MS('Эсминец Норман', 'Norman Destroyer'),
]



class Misson09(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m09/m09.ini'
    FOLDER = 'M09'
    FILE = 'm09'
    START_SAVE_ID = 32900
    START_SAVE_RU_NAME = MS('Омега-3. Станция Йокогама', 'Omega-3, Station Yokohama')
    SCRIPT_INDEX = 9
    DIRECT_SYSTEMS = [S.ku_tgk, S.sig42]
    STATIC_NPCSHIPS = NPCSHIPS
    RTC = ['deck', 'yokohama', 'order', 'final', 'leave_yoko']
    INIT_OFFER = MultiLine(
        [
            'ЗАДАЧА:',
            'Помочь Ордену получить важные данные об СБА.',
            '',
            'СЛОЖНОСТЬ:',
            'Высокая.',
            '',
            'НАГРАДА:',
            'Выполнение договоренностей со стороны Ордена',
        ],
        [
            'OBJECTIVE:',
            'Help the Order to get important data about ASF.',
            '',
            'DIFFICULTY:',
            'High.',
            '',
            'REWARD:',
            'Implementation of the treaty from The Order\'s side',
        ]
    ).get_content()

    def get_save_states(self):
        return [
            SaveState(self, 'fighter_patrol', MS('Сириус. Патруль истребителей', 'Sirius. Fighter patrol')),
            SaveState(self, 'gunboat_patrol', MS('Сириус. Патруль канонерок', 'Sirius. Gunboat patrol')),
            SaveState(self, 'destroyer_attack', MS('Сириус. Эсминцы', 'Sirius. Destroyers')),
        ]

    def get_static_points(self):
        defined_points = []

        # SIRIUS

        sig42_points = [
            'to_train',
            'ship_patrol',
            'gunboat_patrol',
            'destroyer_patrol',
            'randevoue',
        ]
        for p in sig42_points:
            defined_points.append(
                Point(self, S.sig42, p)
            )

        sig42_solars = [
            ('com_sat', MS('Хризантема', 'Chrysanthemum')),
            ('check1', MS('Датчик', "Sensor")),
        ]
        for sol, ru_name in sig42_solars:
            defined_points.append(
                Solar(self, S.sig42, sol, ru_name=ru_name, labels=['friend']),
            )

        defined_points.extend([
            DockableBattleshipSolar(self, S.sig42, 'torp_musashi',
                                    ru_name=N.MUSASHI, base='sig42_98_base',
                                    archetype='k_battleship', labels=['friend']),
        ])

        return defined_points

    def get_capital_ships(self):
        bdr_torpedo = {
            'npc_ship_arch': 'ms9_br_destroyer_torpedo',
            'faction': 'asf_grp',
            'labels': ['enemy', 'br_destroyer', 'torpedo_attack'],
        }
        br_gunboat = {
            'npc_ship_arch': 'ms9_br_gunboat',
            'faction': 'asf_grp',
            'labels': ['enemy', 'br_gunboat', 'asf', 'bgb'],
        }
        li_dread = {
            'npc_ship_arch': 'ms9_li_dread',
            'faction': 'asf_grp',
            'labels': ['enemy', 'asf'],
        }
        br_bship = {
            'npc_ship_arch': 'ms9_br_battleship',
            'faction': 'asf_grp',
            'labels': ['enemy', 'asf'],
        }

        caps = []
        torp_per_letter = 3
        torp_letters = ['a', 'b', 'c', 'd', 'e', 'f']
        torp_caps = []
        bgb_caps = []
        asf_cap_names = [
            ['ldr1', li_dread],
            ['ldr2', li_dread],
            ['bbs1', br_bship],
            ['bbs2', br_bship],
            ['bbs3', br_bship],
            ['bbs4', br_bship],
        ]
        asf_caps = []

        gunboats_len = 3
        bdr_name_index = 0

        for letter in torp_letters:
            for index in range(1, torp_per_letter+1):
                cap = f'bdr_{letter}{index}'
                the_cap = Capital(self, cap, ru_name=BDR_NAMES[bdr_name_index], **bdr_torpedo)
                caps.append(the_cap)
                torp_caps.append(the_cap)
                bdr_name_index += 1

        self.add_capital_group('BDR_TORP', torp_caps)

        for index in range(1, gunboats_len+1):
            cap = f'bgb{index}'
            the_cap = Capital(self, cap, ru_name=N.BR_GUNBOAT, **br_gunboat)
            caps.append(the_cap)
            bgb_caps.append(the_cap)

        self.add_capital_group('BGB', bgb_caps)

        for cap, arch in asf_cap_names:
            the_cap = Capital(self, cap, ru_name=N.BR_GUNBOAT, **arch)
            caps.append(the_cap)
            asf_caps.append(the_cap)

        self.add_capital_group('ASF_CAP', asf_caps)

        return caps

    def get_real_objects(self):
        return {
            'vendor_station': Obj(self, ku_tgk.TekagiLargeStation),
            'tgk_tlr_1': Conn(self, ku_tgk.TekagiFreeportConn2, ku_tgk.TekagiLargeStation),
            'tgk_tlr_2': Conn(self, ku_tgk.TekagiFreeportConn1, ku_tgk.TekagiFreeport),
            'to_sirius': Obj(self, ku_tgk.TekagiSiriusJumphole),
        }

    def get_nn_objectives(self):
        return [
            NNObj(self,
                  MS('Встретьтесь с информатором на станции Йокогама в Омеге-3',
                     'Meet informer in Yokohama Station in Omega-3 system'),
                  name='meet_vendor', target='vendor_station'),

            NNObj(self, O.LAUNCH, name='launch'),

            NNObj(self, O.TLR, target='tgk_tlr_1'),
            NNObj(self, O.TLR, target='tgk_tlr_2'),

            NNObj(self, O.GOTO_JUMPHOLE, name='goto_sirius', target='to_sirius', towards=True),
            NNObj(self, O.JUMPHOLE, name='jump_sirius', target='to_sirius'),

            NNObj(self, O.GOTO, target='to_train'),

            NNObj(self, MS('Войдите формацию с поездом', 'Join train\'s formation'), name='train_formation'),
            NNObj(self, MS('Следуйте за поездом', 'Follow train'), name='train_follow'),

            NNObj(self, MS('Доберитесь до датчика', 'Reach sensor'), name='to_check', target='check1', towards=True),

            NNObj(self, MS('Находитесь как можно ближе к датчику', "Stay as close to the sensor as possible"), name='stay_near_check_close'),

            NNObj(self, MS('Перехватите вражеский патруль', 'Catch enemy patrol'), target='ship_patrol'),
            NNObj(self, MS('Уничтожьте вражеский патруль', 'Destroy enemy patrol'), name='destroy_ship_patrol'),

            NNObj(self, MS('Перехватите канонерки СБА', 'Catch enemy gunboats'), target='gunboat_patrol'),
            NNObj(self, MS('Уничтожьте корабли СБА', "Destroy ASF ships"), name='destroy_gunboat_patrol'),

            NNObj(self, MS('Перехватите эсминцы СБА', 'Catch Destroyers'), target='destroyer_patrol'),
            NNObj(self, MS('Повредите вражеские эсминцы', 'Hurt enemy destroyers'), name='hit_bdr'),
            NNObj(self, MS('Перехватите торпеды', 'Intercept torpedoes'), name='catch_torpedoes'),
            NNObj(self, MS('Захватите капсулу с Хризантемы', 'Collect capsule from Chrysantemum'), name='collect_chrysatemum'),

            NNObj(self, O.GOTO, target='randevoue'),
            NNObj(self, MS('Сядьте на линкор Мусаси', 'Dock with Musashi'), name='dock_musashi', target='torp_musashi'),
        ]

    def get_ingame_thorns(self):
        return [
            IngameThorn(
                self,
                system_class=S.sig42,
                template=GENERIC_TWO_POINT,
                name='m9_kamikadze',
                points={
                    'camera': 'trap_cam',
                    'marker': 'trap_marker',
                },
                duration=120,
            ),
        ]

    def get_ships(self):
        return [
            Ship(
                self,
                'kim',
                hero=True,
                jumper=True,
                actor=actors.Kim,
                labels=[
                    'friend',
                    'order',
                ],
                npc=NPC(
                    faction=faction.OrderMain,
                    ship=ship.Dragon,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'matome',
                hero=True,
                jumper=True,
                actor=actors.Matome,
                labels=[
                    'friend',
                    'order',
                ],
                npc=NPC(
                    faction=faction.OrderMain,
                    ship=ship.Dron,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'darcy',
                hero=True,
                jumper=True,
                actor=actors.Darcy,
                labels=[
                    'friend',
                    'order',
                ],
                npc=NPC(
                    faction=faction.BretoniaMain,
                    ship=ship.Crusader,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'train',
                hero=True,
                jumper=False,
                affiliation=faction.OrderMain.CODE,
                actor=actors.ChrysanthemumTrain,
                radius=0,
                labels=[
                    'friend',
                    'order',
                ],
                static_npc_shiparch='m09_train'
            ),
            Ship(
                self,
                'lifter',
                hero=True,
                jumper=False,
                affiliation=faction.OrderMain.CODE,
                actor=actors.ChrysanthemumLifter,
                radius=0,
                labels=[
                    'friend',
                    'order',
                ],
                static_npc_shiparch='m09_lifter'
            ),
            Ship(
                self,
                'repair',
                hero=True,
                jumper=False,
                affiliation=faction.OrderMain.CODE,
                actor=actors.ChrysanthemumRepair,
                radius=0,
                labels=[
                    'friend',
                    'order',
                ],
                static_npc_shiparch='m09_repair'
            ),
            Ship(
                self,
                'sakura',
                count=5,
                system_class=S.sig42,
                affiliation=faction.OrderMain.CODE,
                labels=[
                    'friend',
                    'order',
                ],
                slide_x=100,
                unique_npc_entry=True,
                base_name=MS('Сакура', 'Sakura'),
                npc=NPC(
                    faction=faction.KusariMain,
                    ship=ship.Drake,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=6),
                )
            ),
            Ship(
                self,
                'suzuki',
                count=5,
                system_class=S.sig42,
                affiliation=faction.OrderMain.CODE,
                labels=[
                    'friend',
                    'order',
                ],
                radius=0,
                slide_x=100,
                unique_npc_entry=True,
                base_name=MS('Сузуки', "Suzuki"),
                npc=NPC(
                    faction=faction.KusariMain,
                    ship=ship.Dragon,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=6),
                )
            ),
            Ship(
                self,
                'suzuki_bdr',
                count=5,
                system_class=S.sig42,
                affiliation=faction.OrderMain.CODE,
                labels=[
                    'friend',
                    'order',
                ],
                radius=0,
                slide_x=100,
                unique_npc_entry=True,
                base_name=MS('Сузуки', "Suzuki"),
                npc=NPC(
                    faction=faction.KusariMain,
                    ship=ship.Dragon,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=6),
                )
            ),
            Ship(
                self,
                'yanagi_bdr',
                count=5,
                system_class=S.sig42,
                affiliation=faction.OrderMain.CODE,
                labels=[
                    'friend',
                    'order',
                ],
                slide_z=100,
                unique_npc_entry=True,
                base_name=MS('Янаги', 'Yanagi'),
                npc=NPC(
                    faction=faction.KusariMain,
                    ship=ship.Dragon,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=6),
                )
            ),
            Ship(
                self,
                'kamikadze',
                count=5,
                system_class=S.sig42,
                affiliation=faction.OrderMain.CODE,
                labels=[
                    'friend',
                    'order',
                ],
                unique_npc_entry=True,
                base_name=MS('Янаги', 'Yanagi'),
                npc=NPC(
                    faction=faction.KusariMain,
                    ship=ship.Dragon,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=6),
                )
            ),
            Ship(
                self,
                'patroller_a',
                count=4,
                system_class=S.sig42,
                affiliation=faction.ASF.CODE,
                labels=[
                    'enemy',
                    'asf',
                    'ship_patroller',
                ],
                slide_z=100,
                npc=NPC(
                    faction=faction.BretoniaMain,
                    ship=ship.Cavalier,
                    level=NPC.D9,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'patroller_b',
                count=4,
                system_class=S.sig42,
                affiliation=faction.ASF.CODE,
                labels=[
                    'enemy',
                    'asf',
                    'ship_patroller',
                ],
                slide_z=100,
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Patriot,
                    level=NPC.D9,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'bgb_support_a',
                count=5,
                system_class=S.sig42,
                affiliation=faction.ASF.CODE,
                labels=[
                    'enemy',
                    'asf',
                    'bgb_support',
                    'bgb',
                ],
                slide_z=100,
                npc=NPC(
                    faction=faction.BretoniaMain,
                    ship=ship.Crusader,
                    level=NPC.D9,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'bgb_support_b',
                count=5,
                system_class=S.sig42,
                affiliation=faction.ASF.CODE,
                labels=[
                    'enemy',
                    'asf',
                    'bgb_support',
                    'bgb',
                ],
                slide_x=100,
                npc=NPC(
                    faction=faction.BretoniaMain,
                    ship=ship.Cavalier,
                    level=NPC.D9,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'bdr_support_a',
                count=5,
                system_class=S.sig42,
                affiliation=faction.ASF.CODE,
                labels=[
                    'enemy',
                    'asf',
                    'bdr_support',
                    'bdr',
                ],
                slide_x=-100,
                npc=NPC(
                    faction=faction.BretoniaMain,
                    ship=ship.Crusader,
                    level=NPC.D9,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'bdr_support_b',
                count=3,
                system_class=S.sig42,
                affiliation=faction.ASF.CODE,
                labels=[
                    'enemy',
                    'asf',
                    'bdr_support',
                    'bdr',
                ],
                slide_x=100,
                slide_z=100,
                npc=NPC(
                    faction=faction.BretoniaMain,
                    ship=ship.Crusader,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'bdr_support_c',
                count=3,
                system_class=S.sig42,
                affiliation=faction.ASF.CODE,
                labels=[
                    'enemy',
                    'asf',
                    'bdr_support',
                    'bdr',
                ],
                slide_x=100,
                slide_z=100,
                npc=NPC(
                    faction=faction.BretoniaMain,
                    ship=ship.Crusader,
                    level=NPC.D9,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'bdr_support_d',
                count=3,
                system_class=S.sig42,
                affiliation=faction.ASF.CODE,
                labels=[
                    'enemy',
                    'asf',
                    'bdr_support',
                    'bdr',
                ],
                slide_x=100,
                slide_z=100,
                npc=NPC(
                    faction=faction.BretoniaMain,
                    ship=ship.Crusader,
                    level=NPC.D9,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'bdr_support_e',
                count=3,
                system_class=S.sig42,
                affiliation=faction.ASF.CODE,
                labels=[
                    'enemy',
                    'asf',
                    'bdr_support',
                    'bdr',
                ],
                slide_x=100,
                slide_z=100,
                npc=NPC(
                    faction=faction.BretoniaMain,
                    ship=ship.Crusader,
                    level=NPC.D9,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'bdr_support_f',
                count=3,
                system_class=S.sig42,
                affiliation=faction.ASF.CODE,
                labels=[
                    'enemy',
                    'asf',
                    'bdr_support',
                    'bdr',
                ],
                slide_x=100,
                slide_z=100,
                npc=NPC(
                    faction=faction.BretoniaMain,
                    ship=ship.Crusader,
                    level=NPC.D9,
                    equip_map=EqMap(base_level=5),
                )
            ),
        ]
