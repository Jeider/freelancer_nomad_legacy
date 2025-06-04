import random

from universe import sirius as S
from universe.systems import li_for, sig17
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors

from story.ingame import names as N
from story.ingame import objectives as O
from story.ingame.tools import Point, Obj, Conn, NNObj, Ship, Solar, Capital, SaveState, MultiText, TextDialog
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT, GENERIC_MOUNTED_ROTATABLE

from world.npc import NPC, EqMap
from world import ship
from universe import faction

NPCSHIPS = '''

[NPCShipArch]
nickname = ms5_tr_ge_armored_ship
loadout = li_grp_ge_armored_main_01
level = d5
ship_archetype = ge_armored
pilot = cruiser_default
state_graph = TRANSPORT
npc_class = lawful, CRUISER


'''



class Misson05(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m05/m05.ini'
    FOLDER = 'M05'
    FILE = 'm05'
    START_SAVE_ID = 32500
    STATIC_NPCSHIPS = NPCSHIPS
    SCRIPT_INDEX = 5
    DIRECT_SYSTEMS = [S.li_for, S.sig17]

    def get_save_states(self):
        return [
            SaveState(self, 'smuggler', 'Форбс, склад контрабанды'),
            SaveState(self, 'convoy', 'Сигма-17, транспорт Омега-9'),
            SaveState(self, 'scient', 'Сигма-17, взрыв исследовательской станции'),
            SaveState(self, 'arrest_battle', 'Сигма-17, линкор Грифон'),
        ]

    def get_dialogs(self):
        return [
            TextDialog(
                self, 'smuggler', 'База с уязвимыми точками',
                ru_content=MultiText([
                    'Чтобы уничтожить базу, вы должны проникнуть внутрь и уничтожить её ядро.',

                    'Атакуйте склады, отмеченные синим цветом на вашем интерфейсе, чтобы разблокировать двери базы.',

                    'После этого залетайте в туннель и атакуйте ядро.',

                    'В будущем вы сможете встретить подобные базы в случайных миссиях, которые можно взять в баре',
                ]),
            ),
            TextDialog(
                self, 'scient_pod', 'Уязвимые точки',
                ru_content=MultiText([
                    'Спасательные капусулы не успели активироваться!',

                    'Уничтожьте обломки станции, чтобы разблокировать спасательные капсулы и подобрать учёных',

                    'Скорее! Системы обеспечения скоро откажут!',
                ]),
            ),
        ]

    def get_ingame_thorns(self):
        return [
            IngameThorn(
                self,
                system_class=S.li_for,
                template=GENERIC_TWO_POINT,
                name='m05_smuggler1',
                points={
                    'camera': 'smuggler_cinema1_cam',
                    'marker': 'smuggler_cinema1',
                },
                duration=25,
            ),
            IngameThorn(
                self,
                system_class=S.li_for,
                template=GENERIC_TWO_POINT,
                name='m05_smuggler1b',
                points={
                    'camera': 'smuggler_cinema1_camB',
                    'marker': 'smuggler_cinema1',
                },
                duration=25,
            ),
            IngameThorn(
                self,
                system_class=S.li_for,
                template=GENERIC_TWO_POINT,
                name='m05_smuggler3',
                points={
                    'camera': 'smuggler_cinema3_cam',
                    'marker': 'smuggler_cinema3',
                },
                duration=25,
            ),
            IngameThorn(
                self,
                system_class=S.li_for,
                template=GENERIC_TWO_POINT,
                name='m05_smuggler_player',
                points={
                    'camera': 'player_smuggler_cam',
                    'marker': 'player_smuggler',
                },
                duration=25,
            ),


        ]
    def get_real_objects(self):
        return {
            'vendor_planet': Obj(self, li_for.ForbesDockring),
            'for_tlr_1': Conn(self, li_for.ForbesPlanetConn3, li_for.ForbesDockring),

            'detroit': Obj(self, li_for.ForbesLargeStation),
            'piratebase': Obj(self, li_for.ForbesJunkers),

            'for_tlr_2': Conn(self, li_for.ForbesPlanetConn3, li_for.ForbesLargeStation),
            'for_tlr_3': Conn(self, li_for.ForbesPlanetConn1, li_for.ForbesDockring),

            'sig17_jump': Obj(self, li_for.ForbesSigma17Jumpgate),

            'sig17_tlr_1': Conn(self, sig17.Sig17BattleshipConn1, sig17.Sig17ForbesJumpgate),
            'sig17_tlr_2': Conn(self, sig17.Sig17BattleshipConn1, sig17.Sig17Battleship),

            'for_jump': Obj(self, sig17.Sig17ForbesJumpgate),

            'for_tlr_4': Conn(self, li_for.ForbesPlanetConn1, li_for.ForbesSigma17Jumpgate),
        }

    def get_nn_objectives(self):
        return [
            NNObj(self, 'Встретьтесь с Хечтер в баре планеты Форбс', name='meet_vendor', target='vendor_planet'),

            NNObj(self, O.LAUNCH, name='launch'),

            NNObj(self, O.TLR, target='for_tlr_1'),
            NNObj(self, O.TLR, target='for_tlr_2'),
            NNObj(self, O.TLR, target='for_tlr_3'),
            NNObj(self, O.TLR, target='for_tlr_4'),

            NNObj(self, 'Сядьте на Детроит', name='first_dock_detroit', target='detroit', open_access=False),

            NNObj(self, 'Направляйтесь к базу контрабандистов',
                  name='goto_piratebase', target='piratebase', towards=True),
            NNObj(self, 'Сядьте на пиратскую базу', name='dock_piratebase', target='piratebase'),

            NNObj(self, 'Направляйтесь к складу контрабанды', name='goto_storage', target='smuggler_storage', towards=True),

            NNObj(self, 'Уничтожьте контрабандистов', name='destroy_smugglers'),
            NNObj(self, 'Уничтожьте склады и ядро склада контрабанды', name='destroy_storage', target='smuggler_storage', nag=False),
            NNObj(self, 'Заберите ключ', name='get_a_key'),

            NNObj(self, 'Возвращайтесь на Детроит', name='go_back_detroit', target='detroit', towards=True),
            NNObj(self, 'Сядьте на Детроит', name='dock_detroit', target='detroit'),

            NNObj(self, O.JUMPGATE, target='sig17_jump'),

            NNObj(self, O.TLR, target='sig17_tlr_1'),
            NNObj(self, O.TLR, target='sig17_tlr_2'),

            NNObj(self, 'Доберитесь до исследовательской станции',
                  name='reach_research',target='research_base', towards=True),
            NNObj(self, 'Сядьте на исследовательскую станцию', name='try_to_dock_on_research'),

            NNObj(self, O.GOTO, name='goto_convoy', target='convoy'),

            NNObj(self, O.DESTROY_PIRATES, name='destroy_pirates'),
            NNObj(self, 'Войдите в формацию с транспортом', name='join_transport_formation'),
            NNObj(self, 'Сопровождайте транспорт', name='follow_transport'),
            NNObj(self, 'Ожидайте разрешения на посадку', name='wait_for_docking_approve'),

            NNObj(self, 'Спасите Мандрейка из обломков станции', name='find_madrake_and_tractor_him'),
            NNObj(self, 'Попытайтесь спасти всех учёных!', name='save_all_scients'),

            NNObj(self, 'Возвращайтесь к торговому пути', name='goto_bship_tlr', target='bship_tlr2'),

            NNObj(self, 'Уничтожьте рейнландские истребители', name='destroy_rheinland_fighters'),

            NNObj(self, O.DOCKRING, name='final_planet', target='vendor_planet'),
        ]

    def get_static_points(self):
        defined_points = []

        defined_points.extend([
            Solar(self, S.li_for, 'smuggler_storage', ru_name='Склад контрабанды',
                  archetype='rmbase_smuggler', loadout='m05_smuggler_storage',
                  labels=['smuggler']),

            Solar(self, S.sig17, 'research_base', ru_name='Исследовательская станция Кларк',
                  archetype='d_depot', loadout='depot', labels=['deepspace']),


        ])

        sig17_points = [
            'convoy',
            'bship_tlr2',
        ]

        for p in sig17_points:
            defined_points.append(
                Point(self, S.sig17, p)
            )

        return defined_points

    def get_capital_ships(self):
        armored_ship = {
            'npc_ship_arch': 'ms5_tr_ge_armored_ship',
            'faction': 'fc_uk_grp',
            'labels': ['convoy'],
        }

        caps = [
            Capital(self, 'armored', ru_name='Транспорт Омега-9', **armored_ship),
        ]

        return caps

    def get_ships(self):
        return [
            Ship(
                self,
                'hatcher',
                jumper=True,
                hero=True,
                actor=actors.Hatcher,
                labels=[
                    'friend',
                ],
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.DefenderJuni,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=4),
                    animated_wings=True,
                )
            ),

            Ship(
                self,
                'smuggler_cinema',
                count=3,
                affiliation=faction.LibertyRogues.CODE,
                labels=[
                    'smuggler',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.Outcasts,
                    ship=ship.Barracuda,
                    level=NPC.D6,
                    equip_map=EqMap(base_level=4),
                    animated_wings=False,
                )
            ),
            Ship(
                self,
                'smuggler_cinema_go',
                count=3,
                affiliation=faction.LibertyRogues.CODE,
                labels=[
                    'smuggler',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.Outcasts,
                    ship=ship.Barracuda,
                    level=NPC.D6,
                    equip_map=EqMap(base_level=4),
                    animated_wings=True,
                )
            ),
            Ship(
                self,
                'smuggler_wing1',
                count=3,
                slide_z=-100,
                system_class=S.li_for,
                affiliation=faction.LibertyRogues.CODE,
                labels=[
                    'smuggler',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.Outcasts,
                    ship=ship.Barracuda,
                    level=NPC.D6,
                    equip_map=EqMap(base_level=4),
                    animated_wings=True,
                )
            ),
            Ship(
                self,
                'smuggler_wing2',
                count=3,
                slide_z=100,
                system_class=S.li_for,
                affiliation=faction.LibertyRogues.CODE,
                labels=[
                    'smuggler',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.Outcasts,
                    ship=ship.Barracuda,
                    level=NPC.D6,
                    equip_map=EqMap(base_level=4),
                    animated_wings=True,
                )
            ),
            Ship(
                self,
                'convoy_pir1',
                count=4,
                slide_z=-100,
                affiliation=faction.LibertyRogues.CODE,
                system_class=S.sig17,
                labels=[
                    'pirates',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.LibertyRogues,
                    ship=ship.Barracuda,
                    level=NPC.D6,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'convoy_pir2',
                count=4,
                slide_x=-80,
                slide_z=80,
                affiliation=faction.LibertyRogues.CODE,
                system_class=S.sig17,
                labels=[
                    'pirates',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.LibertyRogues,
                    ship=ship.Patriot,
                    level=NPC.D6,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'military',
                count=3,
                affiliation=faction.LibertyMain.CODE,
                system_class=S.sig17,
                labels=[
                    'military',
                    'friend',
                ],
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Defender,
                    level=NPC.D9,
                    equip_map=EqMap(base_level=4),
                )
            ),
            Ship(
                self,
                'rheinland',
                count=6,
                affiliation=faction.RheinlandMain.CODE,
                system_class=S.sig17,
                labels=[
                    'rheinland',
                    'enemy',
                ],
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=5),
                    extra_equip=[
                        'equip = cloak_fast, HpCloak01',
                    ],
                )
            ),
        ]
