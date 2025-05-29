from universe import sirius as S
from universe.systems import sig13, rh_ber
from story.ingame import ingame_mission
from story import actors

from story.ingame import objectives as O
from story.ingame.tools import Point, Obj, Conn, NNObj, Ship, SaveState, MultiText, TextDialog
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT

from world.npc import NPC, EqMap
from world import ship
from universe import faction

NPCSHIPS = '''

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
    STATIC_NPCSHIPS = NPCSHIPS

    def get_save_states(self):
        return [
            SaveState(self, 'brandenburg', 'Берлин, Аванпост Бранденбург'),
        ]

    def get_dialogs(self):
        return [
            TextDialog(
                self, 'engine_controls', 'От автора',
                ru_content=MultiText([
                    'Добро пожаловать в мод Наследие Номадов!',

                    'Хочу обратить ваше внимание, что ваш корабль имеет гораздо более гибкую систему оборудования. '
                    'Вы можете менять и постепенно улучшать двигатели, генераторы, форсажи и прочее.',

                    'По этой причине ваш первый двигатель обладаем совсем слабой скоростью. Но не волнуйтесь, '
                    'в будущем вы сможете ставить более лучшее оборудование, которое позволит вам развивать '
                    'более внушительную скорость.',

                    'Удачных полётов!',
                ])
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
                    level=NPC.D1,
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
                    level=NPC.D1,
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
                    level=NPC.D1,
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
                    gen_armor=False,
                    extra_equip=[
                        'equip = npc_armor_2',
                    ]
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
                    gen_armor=False,
                    extra_equip=[
                        'equip = npc_armor_2',
                    ]
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
                    gen_armor=False,
                    extra_equip=[
                        'equip = npc_armor_2',
                    ]
                )
            ),
        ]

    def get_nn_objectives(self):
        return [
            NNObj(self, 'Поговорите с Алариком в баре', name='find_job'),
            NNObj(self, O.LAUNCH, name='launch'),
            NNObj(self, O.TLR, target='s13_tlr'),
            NNObj(self, O.JUMPGATE, target='s13_to_ber'),
            NNObj(self, O.TLR, target='tlr_to_outpost'),
            NNObj(self, 'Ожидайте прохождения проверки', target='ber_outpost'),
            NNObj(self, 'Уничтожьте корсаров', name='defend_cruiser'),
            NNObj(self, O.TLR, target='tlr_to_planet'),
            NNObj(self, O.DOCKRING, target='ber_dockring'),
        ]


