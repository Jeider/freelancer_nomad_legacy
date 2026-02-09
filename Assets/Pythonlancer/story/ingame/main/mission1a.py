from universe import sirius as S
from universe.systems import sig13, rh_ber
from story.ingame import ingame_mission
from story import actors

from story.ingame import objectives as O
from story.ingame.tools import Point, Obj, Conn, NNObj, Ship, SaveState, MultiText, MultiLine, TextDialog, DIALOG_YES_NO
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT

from world.npc import NPC, EqMap
from world import ship
from universe import faction

from text.strings import MultiString as MS

NPCSHIPS = '''

[NPCShipArch]
nickname = intro_armored_default
loadout = intro_armored_default
level = d5
ship_archetype = ge_armored
pilot = transport_hard
state_graph = TRANSPORT
npc_class = lawful, class_armored, d20

[NPCShipArch]
nickname = intro_armored_fast_start
loadout = intro_armored_fast_start
level = d5
ship_archetype = ge_armored
pilot = transport_hard
state_graph = TRANSPORT
npc_class = lawful, class_armored, d20


[NPCShipArch]
nickname = rh_grp_cruiser_m1
loadout = rh_grp_cruiser_sat
level = d22
ship_archetype = rh_cruiser
pilot = cruiser_sat
state_graph = CRUISER
npc_class = lawful, CRUISER

[NPCShipArch]
nickname = co_elite2_m1
loadout = lod_m1_co_elite2
level = d20
ship_archetype = or_elite
pilot = pilot_MSN01_torpedo
state_graph = FIGHTER
npc_class = lawful, class_fighter,  d20
'''



class Misson01A(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m01/m01a.ini'
    FOLDER = 'M01A'
    FILE = 'm01a'
    SCRIPT_INDEX = 1
    START_SAVE_ID = 32000
    START_SAVE_RU_NAME = MS('Сигма-13. Газодобытчик Магдебург', 'Sigma-13. Gas miner Magdeburg')
    STATIC_NPCSHIPS = NPCSHIPS
    RTC = ['alaric_sig13']
    INIT_OFFER = MultiLine(
        ru_lines=[
            'ЗАДАЧА:',
            'Сопроводить рейнландский торговый конвой.',
            '',
            'СЛОЖНОСТЬ:',
            'Лёгкая.',
            '',
            'НАГРАДА:',
            '5 000 кредитов.',
        ],
        en_lines=[
            'OBJECTIVE:',
            'Escort Rheinland trade convoy.',
            '',
            'DIFFICULTY:',
            'Easy.',
            '',
            'REWARD:',
            '5 000 credits.',
        ]
    ).get_content()

    def get_save_states(self):
        return [
            SaveState(self, 'brandenburg', MS('Берлин, Аванпост Бранденбург', 'Berlin, Outpost Brandnburg')),
        ]

    def get_offers(self):
        return

    def get_dialogs(self):
        return [
            TextDialog(
                self, 'intro_select', MS('От автора', 'From author'),
                dialog_type=DIALOG_YES_NO,
                ru_content=MultiText([
                    'Добро пожаловать в Наследие Номадов!',

                    'Нажмите Да, чтобы начать кампанию.',

                    'Нажмите Нет, чтобы начать кампанию и пропустить титры.',
                ],[
                    'Greetings! Welcome to mod The Nomad Legacy!',

                    'Press Yes to start the campaign.',

                    'Press No to start the campaign and skip intro titles.',
                ]),
            ),
            TextDialog(
                self, 'engine_controls', MS('От автора', 'From author'),
                ru_content=MultiText([
                    'Добро пожаловать в мод Наследие Номадов!',

                    'Если вы до этого не играли во Freelancer, то научиться играть будет не сложно. В основном игра управляется мышью, '
                    'кнопка W - это увеличить скорость, X - реверс, Tab - форсаж. A D - стрейфы. Q E - крен. Z - выключенный двигатель, активирует '
                    'движение по инерции. Shift+W - полёт в круизе',

                    'Чтобы активировать действия автопилота вы должны нажимать или на кнопки на верхней панели или '
                    'нажимать кнопки: F2 - это двигаться к указанной цели, F3 - стыковка с целью, F4 войти в формацию '
                    'с целью.',

                    'Удачных полётов!',
                ],[
                    'Greetings! Welcome to mod The Nomad Legacy!',

                    "If you don't player in Freelancer, you can learn it very fast. Game mostly controller by your mouse, also with buttons: "
                    "W - increase throttle, X - reverse, Tab - afterburn, A D - strafes, Q E - rotate corkscrew (a.k.a. do a barrel roll), "
                    "Z - kill engine, activates motion by inertia."

                    "To activate maneuvers of your autopilot you should use top bar or press keys: F2 - go to target, "
                    "F3 - dock with target, F4 - join formation with target.",

                    "Good flights!"
                ]),
            ),
        ]

    def get_ingame_thorns(self):
        return [
            IngameThorn(
                self,
                system_class=S.sig13,
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
            Point(self, S.sig13, 'm1_alaric1'),
            Point(self, S.rh_ber, 'rh_cruiser'),
            Point(self, S.rh_ber, 'rh_wing1'),
            Point(self, S.rh_ber, 'rh_wing2'),
            Point(self, S.rh_ber, 'co_wingA'),
            Point(self, S.rh_ber, 'co_wingB'),
            Point(self, S.rh_ber, 'co_wingX'),
            Point(self, S.rh_ber, 'co_wingX_target'),
            Point(self, S.rh_ber, 'player_outpost_autosave'),
            Point(self, S.rh_ber, 'player_cruiser_dead'),
            Point(self, S.rh_ber, 'alaric_outpost'),
        ]


    def get_ships(self):
        return [
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
                'RHwingA',
                count=2,
                affiliation=faction.RheinlandMain.CODE,
                system_class=S.rh_ber,
                labels=[
                    'outpost_defend',
                    'friend'
                ],
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D3,
                    equip_map=EqMap(base_level=2),
                    have_afterburn1=False,
                    have_afterburn2=False,
                )
            ),
            Ship(
                self,
                'RHwingB',
                count=2,
                affiliation=faction.RheinlandMain.CODE,
                system_class=S.rh_ber,
                labels=[
                    'outpost_defend',
                    'friend'
                ],
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D3,
                    equip_map=EqMap(base_level=2),
                    have_afterburn1=False,
                    have_afterburn2=False,
                )
            ),
            Ship(
                self,
                'COwingA',
                count=6,
                affiliation=faction.Corsairs.CODE,
                system_class=S.rh_ber,
                labels=[
                    'outpost_attack',
                    'enemy'
                ],
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Bloodhound,
                    level=NPC.D1,
                    equip_map=EqMap(base_level=1),
                    have_afterburn1=False,
                    have_afterburn2=False,
                    # gen_armor=False,
                    # extra_equip=[
                    #     'equip = npc_armor_2',
                    # ]
                )
            ),
            Ship(
                self,
                'COwingB',
                count=3,
                affiliation=faction.Corsairs.CODE,
                system_class=S.rh_ber,
                labels=[
                    'outpost_attack',
                    'enemy'
                ],
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Bloodhound,
                    level=NPC.D1,
                    equip_map=EqMap(base_level=1),
                    have_afterburn1=False,
                    have_afterburn2=False,
                    # gen_armor=False,
                    # extra_equip=[
                    #     'equip = npc_armor_2',
                    # ]
                )
            ),
            Ship(
                self,
                'COwingC',
                count=3,
                affiliation=faction.Corsairs.CODE,
                system_class=S.rh_ber,
                relative_pos=True,
                relative_range=700,
                labels=[
                    'outpost_attack',
                    'enemy'
                ],
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Bloodhound,
                    level=NPC.D1,
                    equip_map=EqMap(base_level=1),
                    have_afterburn1=False,
                    have_afterburn2=False,
                    # gen_armor=False,
                    # extra_equip=[
                    #     'equip = npc_armor_2',
                    # ]
                )
            ),
        ]

    def get_nn_objectives(self):
        return [
            NNObj(self, MS('Поговорите с Алариком в баре', 'Talk with Alaric in bar'), name='find_job'),
            NNObj(self, O.LAUNCH, name='launch'),
            NNObj(self, O.TLR, target='s13_tlr'),
            NNObj(self, O.JUMPGATE, target='s13_to_ber'),
            NNObj(self, O.TLR, target='tlr_to_outpost'),
            NNObj(self, MS('Ожидайте прохождения проверки', 'Wait for the inspection to pass'), target='ber_outpost'),
            NNObj(self, O.DESTROY_CORSAIRS, name='defend_cruiser'),
            NNObj(self, O.TLR, target='tlr_to_planet'),
            NNObj(self, O.DOCKRING, target='ber_dockring'),
        ]


