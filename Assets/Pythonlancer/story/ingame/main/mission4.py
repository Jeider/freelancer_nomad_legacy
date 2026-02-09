import random

from universe import sirius as S
from universe.systems import rh_mnh, rh_biz, sig8, li_for
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors

from story.ingame import names as N
from story.ingame import objectives as O
from story.ingame.tools import (Point, Obj, Conn, NNObj, Ship, Solar, Capital, SaveState,
                                MultiText, MultiLine, TextDialog)
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT

from world.npc import NPC, EqMap
from world import ship
from universe import faction

from text.strings import MultiString as MS

NPCSHIPS = '''

[NPCShipArch]
nickname = ms4_rh_battleship_ship
loadout = rh_battleship_01
level = d10
ship_archetype = rh_battleship_ms4
pilot = cruiser_default_lowgun
state_graph = CRUISER
npc_class = lawful, CRUISER

[NPCShipArch]
nickname = ms4_rh_cruiser_ship
loadout = rh_grp_cruiser
level = d10
ship_archetype = rh_cruiser
pilot = cruiser_default_lowgun
state_graph = CRUISER
npc_class = lawful, CRUISER

[NPCShipArch]
nickname = ms4_rh_gunboat_ship
loadout = rh_grp_gunboat_no_torpedoes
level = d10
ship_archetype = rh_gunboat
pilot = cruiser_default_lowgun
state_graph = CRUISER
npc_class = lawful, CRUISER, d22
'''



class Misson04(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m04/m04.ini'
    FOLDER = 'M04'
    FILE = 'm04'
    START_SAVE_ID = 32400
    START_SAVE_RU_NAME = MS('Мюнхен, Планета Норторф', 'Munich, Planet Nortorf')
    STATIC_NPCSHIPS = NPCSHIPS
    SCRIPT_INDEX = 4
    DIRECT_SYSTEMS = [S.sig8, S.rh_biz, S.li_for]
    RTC = ['vendor_msn']
    INIT_OFFER = MultiLine(
        [
            'ЗАДАЧА:',
            'Сопроводить Джакобо в систему Форбс',
            '',
            'СЛОЖНОСТЬ:',
            'Неизвестно.',
            '',
            'Награда:',
            'Неизвестно (предположительно высокая).',
        ],
        [
            'OBJECTIVE:',
            'Escort Jacobo to the Forbes system',
            '',
            'DIFFICULTY:',
            'Unknown.',
            '',
            'REWARD:',
            'Unknown (theoretically high).',
        ]
    ).get_content()

    def get_save_states(self):
        return [
            SaveState(self, 'keln', MS('Берлин, станция Кёльн', 'Berlin, Station Kologne')),
            SaveState(self, 'forbes_jh', MS('Сигма-8, гипердыра в Форбс', 'Sigma-8, jumphole to Forbes')),
        ]

    def get_dialogs(self):
        return [
            TextDialog(
                self, 'capital', MS('Уязвимые точки', 'Vulnerable points'),
                ru_content=MultiText([
                    'Вражеский крейсер очень тяжело уничтожить, атакуя в лоб. Но вы можете атаковать его уязвимые точки!',

                    'Уязвимые точки выделены отдельным цветом. Уничтожив уязвимую точку вы нанесёте крейсеру '
                    'дополнительные повреждения.',

                    'Выбирайте элементы корабля противника с помощью вашего интерфейса, чтобы навести прицел на '
                    'указанную точку. Ваши ракеты тоже будут лететь в наведенную точку корабля противника.',
                ],[
                    "It's very difficulty to destroy cruiser by direct attacks. But you can attact vulnerable points!",

                    "Vulnerable points have special colors: by default it's orange. Cruiser will get extra damage "
                    "after loosing of vulnerable point.",

                    "You can also select vulnerable point by clicking on interface. If will set your crosshair on "
                    "this point. Your missiles also will be targeted on this point."
                ]),
            ),
        ]

    def get_real_objects(self):
        return {
            'vendor_planet': Obj(self, rh_mnh.MunchDockring),
            'mnh_tlr_1': Conn(self, rh_mnh.MunchCivRuinsConn2, rh_mnh.MunchDockring),
            'mnh_tlr_2': Conn(self, rh_mnh.MunchCivRuinsConn1, rh_mnh.MunchCivilianStationRuins),
            'mnh_to_biz': Obj(self, rh_mnh.MunchBizmarkJumpgate),

            'keln': Obj(self, rh_biz.BizmarkMilitary),
            'biz_to_sig8': Obj(self, rh_biz.BizmarkSigma8Jumphole),

            'sig8_to_for': Obj(self, sig8.Sig8ForbesJumphole),

            'shipyard': Obj(self, li_for.ForbesShipyard),
            'for_tlr_1': Conn(self, li_for.ForbesPlanetConn2, li_for.ForbesShipyard),
            'final_planet': Obj(self, li_for.ForbesDockring),
        }

    def get_nn_objectives(self):
        return [
            NNObj(self, MS('Встретьтесь с Джакобо в баре планеты Норторф',
                           'Meet Jacobo in bar of Planet Nortorf'), name='meet_vendor', target='vendor_planet'),

            NNObj(self, O.LAUNCH, name='launch'),

            NNObj(self, O.TLR, target='mnh_tlr_1'),
            NNObj(self, O.TLR, target='mnh_tlr_2'),
            NNObj(self, O.JUMPGATE, target='mnh_to_biz'),

            NNObj(self, MS('Следуйте за офицером', 'Follow officer'), name='follow_officer'),
            NNObj(self, MS('Сражайтесь!', 'Fight!'), name='destroy_keln_enemy'),

            NNObj(self, MS('Уничтожьте боковую панель реактора',
                           'Destroy side panel of battleship'), name='destroy_reactor', target='bs_reactor', nag=False),

            NNObj(self, O.GOTO_JUMPHOLE, name='biz_to_sig8_fly', target='biz_to_sig8', towards=True),
            NNObj(self, O.JUMPHOLE, target='biz_to_sig8'),

            NNObj(self, MS('Уничтожьте крейсер', 'Destroy the cruiser'), name='attack_cruiser'),
            NNObj(self, O.DESTROY_FIGHTERS, name='destroy_fighters'),

            NNObj(self, O.GOTO, name='goto_escape_point1', target='point_escape1', towards=True, reach_range=2000),
            NNObj(self, O.GOTO, name='goto_escape_point2', target='point_escape2', towards=True, reach_range=2000),
            NNObj(self, O.GOTO, name='goto_escape_point3', target='point_escape3', towards=True, reach_range=2000),

            NNObj(self, O.DESTROY_CORSAIRS, name='destroy_corsairs'),
            NNObj(self, O.GOTO_JUMPHOLE, name='sig8_to_for_fly', target='sig8_to_for', towards=True),
            NNObj(self, O.JUMPHOLE, target='sig8_to_for'),
            NNObj(self, MS('Ожидайте активации дыры', 'Wait for activation'), name='wait_for_activation'),

            NNObj(self, MS('Доберитесь до ближайшей базы', 'Reach nearest base'), target='shipyard', towards=True),
            NNObj(self, O.TLR, target='for_tlr_1'),
            NNObj(self, O.DOCKRING, target='final_planet'),
        ]

    def get_static_points(self):
        biz_points = [
            'officer_init',
            'arrest_player',
            'arrest_jacobo',
            'officer_flyback',
            'officer_flyback1',
            'officer_flyback2',
            'officer_flyback3',
            'officer_flyback4',
            'to_keln1',
            'to_keln2',
            'gb1',
            'gb2',
            'gb3',
            'cr1',
            'cr2',
            'keln_hassler',
            'keln_alaric',
            'keln_player',
            'keln_jacobo',
            'keln_officer'
        ]

        sig8_points = [
            'point_escape1',
            'point_escape2',
            'point_escape3',
        ]

        defined_points = [
            Point(self, S.rh_mnh, 'jacobo_init'),
        ]
        for p in biz_points:
            defined_points.append(
                Point(self, S.rh_biz, p)
            )
        for p in sig8_points:
            defined_points.append(
                Point(self, S.sig8, p)
            )

        defined_points.extend([
            Solar(self, S.rh_biz, 'bs', ru_name=MS('Линкор Вотан', 'Battleship Wotan'),
                  faction='rh_grp', archetype='rh_battleship_ms4_solar', loadout='rh_battleship_01_no_guns',
                  labels=['keln_capship']),
            Solar(self, S.rh_biz, 'bs_reactor', ru_name=MS('Реактор линкора', 'Battleship\'s Reactor'),
                  faction='rh_grp', archetype='msn4_rh_battleship_shield'),
        ])

        return defined_points

    def get_capital_ships(self):
        keln_rcr = {
            'npc_ship_arch': 'ms4_rh_cruiser_ship',
            'faction': 'rh_grp',
            'labels': ['keln_capship'],
            'ru_name': N.RH_CRUISER,
        }
        keln_gb = {
            'npc_ship_arch': 'ms4_rh_gunboat_ship',
            'faction': 'rh_grp',
            'labels': ['keln_capship'],
            'ru_name': N.RH_GUNBOAT,
        }
        s8_rcr = {
            'npc_ship_arch': 'ms4_rh_cruiser_ship',
            'faction': 'rh_grp',
            'labels': ['s8_cap', 'fleet'],
            'ru_name': N.RH_CRUISER,
        }

        caps = []
        keln_caps = []

        keln_cr_count = 2
        keln_gb_count = 2

        for index in range(1, keln_cr_count+1):
            cap = f'cr{index}'
            the_cap = Capital(self, cap, **keln_rcr)
            caps.append(the_cap)
            keln_caps.append(the_cap)

        for index in range(1, keln_gb_count+1):
            cap = f'gb{index}'
            the_cap = Capital(self, cap, **keln_gb)
            caps.append(the_cap)
            keln_caps.append(the_cap)

        self.add_capital_group('KELN_CAP', keln_caps)

        caps.append(
            Capital(self, 's8_cruiser', **s8_rcr)
        )

        return caps

    def get_ships(self):
        return [
            Ship(
                self,
                'jacobo',
                jumper=True,
                labels=[
                    'friend',
                ],
                actor=actors.Jacobo,
                npc=NPC(
                    faction=faction.Outcasts,
                    ship=ship.Dromader,
                    level=NPC.D4,
                    equip_map=EqMap(base_level=3),
                )
            ),
            Ship(
                self,
                'hassler',
                jumper=True,
                hero=True,
                actor=actors.Hassler,
                labels=[
                    'friend',
                    'friend_fighter',
                ],
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D4,
                    equip_map=EqMap(base_level=4),
                )
            ),
            Ship(
                self,
                'alaric',
                jumper=True,
                hero=True,
                actor=actors.Alaric,
                labels=[
                    'friend',
                    'friend_fighter',
                ],
                npc=NPC(
                    faction=faction.AlaricLike,
                    ship=ship.Barracuda,
                    level=NPC.D4,
                    equip_map=EqMap(base_level=4),
                )
            ),
            Ship(
                self,
                'officer_leader',
                actor=actors.Kreitmaier,
                labels=[
                    'officer',
                    'rheinland',
                ],
                affiliation=faction.RheinlandMain.CODE,
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D4,
                    equip_map=EqMap(base_level=4),
                )
            ),
            Ship(
                self,
                'officer_wing',
                count=4,
                labels=[
                    'officer',
                    'rheinland',
                ],
                affiliation=faction.RheinlandMain.CODE,
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D4,
                    equip_map=EqMap(base_level=4),
                )
            ),
            Ship(
                self,
                'keln_reinforcement',
                count=6,
                relative_pos=True,
                relative_range=1500,
                labels=[
                    'keln',
                    'rheinland',
                ],
                affiliation=faction.RheinlandMain.CODE,
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D4,
                    equip_map=EqMap(base_level=4),
                )
            ),
            Ship(
                self,
                'ms4_f1',
                count=3,
                labels=[
                    'fleet',
                    'fleet_fighter',
                ],
                slide_z=-50,
                slide_x=-50,
                system_class=S.sig8,
                affiliation=faction.RheinlandMain.CODE,
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Banshee,
                    level=NPC.D4,
                    equip_map=EqMap(base_level=3),
                )
            ),
            Ship(
                self,
                'ms4_f2',
                count=3,
                labels=[
                    'fleet',
                    'fleet_fighter',
                ],
                slide_z=-50,
                slide_x=-50,
                system_class=S.sig8,
                affiliation=faction.RheinlandMain.CODE,
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Banshee,
                    level=NPC.D4,
                    equip_map=EqMap(base_level=3),
                )
            ),
            Ship(
                self,
                's8_reinforcement',
                count=3,
                relative_pos=True,
                relative_range=2000,
                labels=[
                    'fleet',
                    'fleet_fighter',
                ],
                affiliation=faction.RheinlandMain.CODE,
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D4,
                    equip_map=EqMap(base_level=4),
                )
            ),

            Ship(
                self,
                'corsair',
                count=6,
                relative_pos=True,
                relative_range=2300,
                affiliation=faction.Corsairs.CODE,
                labels=[
                    'corsairs',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Bloodhound,
                    level=NPC.D5,
                    equip_map=EqMap(base_level=3),
                )
            ),
        ]
