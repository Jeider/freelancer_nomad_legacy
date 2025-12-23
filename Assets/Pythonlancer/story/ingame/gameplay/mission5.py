import random

from universe import sirius as S
from universe.systems import li_for, sig17
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors
from text.dividers import SINGLE_DIVIDER, DIVIDER

from story.ingame import names as N
from story.ingame import objectives as O
from story.ingame.tools import (
    Point, Obj, Conn, NNObj, Ship, Solar, Capital, SaveState, MultiText,
    MultiLine, TextDialog, Direct, Trigger, DRY_RUN
)
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT, GENERIC_MOUNTED_ROTATABLE

from world.npc import NPC, EqMap
from world import ship
from universe import faction

from text.strings import MultiString as MS

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


class ResearchChunk:
    MANDRAKE_CHUNK = MS('Обломок с Мандрейком', 'Chunk with Mandrake')
    GENERIC_CHUNK = MS('Обломок станции', "Station chunk")

    def __init__(self, pod_root, chunk_index, pod_name, is_mandrake=False):
        self.pod_root: ScientPods = pod_root
        self.chunk_index = chunk_index
        self.is_mandrake = is_mandrake
        self.solar = Solar(self.pod_root.mission, S.sig17, self.get_chunk_name(),
                           ru_name=self.MANDRAKE_CHUNK if is_mandrake else self.GENERIC_CHUNK,
                           auto_archetype=True)
        self.pod_name = pod_name

    def get_chunk_index(self):
        return f'{self.chunk_index:02d}'

    def get_chunk_name(self):
        return ScientPods.CHUNK_NAME.format(self.chunk_index)

    def get_pod_name(self):
        return ScientPods.POD_NAME.format(self.chunk_index)

    def define_solar(self):
        return self.solar.define()

    def spawn_solar(self):
        return SINGLE_DIVIDER.join([
            self.solar.spawn(),
            self.solar.mark(),
        ])

    def mark(self):
        return SINGLE_DIVIDER.join([
            self.solar.mark(),
        ])

    def unmark(self):
        return SINGLE_DIVIDER.join([
            self.solar.unmark(),
        ])

    def destroy(self):
        return SINGLE_DIVIDER.join([
            self.solar.destroy(),
        ])

    def destroy_pod(self):
        return SINGLE_DIVIDER.join([
            f'Act_Destroy = {self.get_pod_name()}'
        ])

    def define_pod(self):
        return f'''
[MsnLoot]
nickname = {self.get_pod_name()}
archetype = escape_pod
string_id = {self.pod_name.id}
rel_pos_obj = {self.get_chunk_name()}
rel_pos_offset = 0, 0, 0
velocity = 0, 10, 0
equip_amount = 1
health = 1.000000
Can_Jettison = false
'''


class ScientPods:

    MAIN = 'SCIENT_PODS_init'
    SYSTEM_CLASS = S.sig17
    SYSTEM_NAME = SYSTEM_CLASS.NAME
    CHUNK_NAME = 'research_chunk_{0}'
    POD_NAME = 'scient_pod_{}'
    CHUNKS_COUNT = 12
    MANDRAKE_ARRIVE_PODS = 4
    CHUNK_DESTROYED_TRIGGER = 'research_chunk_{0}_destroyed'
    POD_ACQUIRED_TRIGGER = 'scient_pod_{0}_acquired'
    END_TRIGGER = 'SCIENT_PODS_exit'
    POD_SUCCESS = 'POD_success'

    MANDRAKE_COUNTER = 'marker_mandrake_arrive_counter'
    TOTAL_COUNTER = 'marker_progress_counter'
    CHECK_MARKER = 'marker_relative_obj'
    SUCCESS_MARKER = 'mandrake_acquired'

    MISSION_TIMEOUT = 60

    MANDRAKE_NAME = MS('Капсула Мандрейка', 'Capsule with Mandrake')
    SCIENT_NAME = MS('Капсула с учёным', 'Capsule with scientist')

    def __init__(self, mission, direct, trigger):
        self.mission: ingame_mission.IngameMission = mission
        self.direct: Direct = direct
        self.trigger: Trigger = trigger
        self.chunks: list[ResearchChunk] = []
        self.objects_defined = False
        self.triggers_defined = False
        self.mandrake_chunk = 1
        self.reward_solar = Solar(self.mission, S.sig17, 'research_reward',
                                  ru_name=MS('Награда', 'Reward'), archetype='hidden_connect',
                                  loadout='m05_scient_reward')
        self.mandrake_ids_name = self.mission.ids.new_name(self.MANDRAKE_NAME)
        self.scient_ids_name = self.mission.ids.new_name(self.SCIENT_NAME)
        self.init_chunks()

    def init_chunks(self):
        have_mandrake = False
        for i in range(1, self.CHUNKS_COUNT+1):
            is_mandrake = i == self.mandrake_chunk
            if is_mandrake:
                have_mandrake = True
            chunk = ResearchChunk(self, chunk_index=i, is_mandrake=is_mandrake,
                                  pod_name=self.mandrake_ids_name if is_mandrake else self.scient_ids_name)
            self.chunks.append(chunk)

        if not have_mandrake:
            raise Exception(f'have no mandrake, index is {self.mandrake_chunk}')

    def turn(self):
        if not self.objects_defined:
            raise Exception('Scient pod objects is not defined')
        if not self.triggers_defined:
            raise Exception('Scient pod triggers is not defined')
        return self.trigger.turn(self.MAIN)

    def define_objects(self):
        definitions = [f'''
[MsnSolar]
nickname = {self.MANDRAKE_COUNTER}
system = sig17
position = 100000, 0, 0
archetype = msn5_pod_counter
radius = 0
string_id = 1

[MsnSolar]
nickname = {self.TOTAL_COUNTER}
system = sig17
position = 100000, 200, 0
archetype = msn5_pod_counter
radius = 0
string_id = 1

[MsnSolar]
nickname = {self.CHECK_MARKER}
system = sig17
position = 100000, 100, 0
archetype = msn5_pod_counter
radius = 0
string_id = 1

[MsnSolar]
nickname = {self.SUCCESS_MARKER}
system = sig17
position = 100000, -100, 0
archetype = msn5_pod_counter
radius = 0
string_id = 1''',
            self.reward_solar.define()
        ]

        for chunk in self.chunks:
            definitions.extend([
                chunk.define_solar(),
                chunk.define_pod(),
            ])

        self.objects_defined = True
        return DIVIDER.join(definitions)

    def draw_main_chunks(self):
        actions = []
        for chunk in self.chunks:
            if chunk.is_mandrake:
                continue
            actions.extend([
                chunk.spawn_solar(),
                self.trigger.turn(self.CHUNK_DESTROYED_TRIGGER.format(chunk.chunk_index)),
            ])
        return SINGLE_DIVIDER.join(actions)

    def deactivate_chunks(self):
        actions = []
        for chunk in self.chunks:
            actions.append(
                self.trigger.off(self.CHUNK_DESTROYED_TRIGGER.format(chunk.chunk_index))
            )
        return SINGLE_DIVIDER.join(actions)

    def mark_all_chunks(self):
        actions = []
        for chunk in self.chunks:
            actions.append(chunk.mark())
        return SINGLE_DIVIDER.join(actions)

    def destroy_all_chunks(self):
        actions = []
        for chunk in self.chunks:
            actions.append(chunk.destroy())
            actions.append(chunk.destroy_pod())
        return SINGLE_DIVIDER.join(actions)

    def draw_mandrake_chunks(self):
        actions = []
        for chunk in self.chunks:
            if not chunk.is_mandrake:
                # actions.append(chunk.unmark())
                continue
            actions.extend([
                chunk.spawn_solar(),
                self.trigger.turn(self.CHUNK_DESTROYED_TRIGGER.format(chunk.chunk_index)),
            ])
        return SINGLE_DIVIDER.join(actions)

    def get_chunk_triggers(self):
        actions = []

        for chunk in self.chunks:
            pod_name = chunk.get_pod_name()
            actions.extend([
                self.trigger.new(self.CHUNK_DESTROYED_TRIGGER.format(chunk.chunk_index)),
                f'Cnd_Destroyed = {chunk.get_chunk_name()}',
                f'Act_SpawnLoot = {pod_name}',
                f'Act_Invulnerable = {pod_name}, true',
                f'Act_MarkObj = {pod_name}, 1',
                self.trigger.turn(self.POD_ACQUIRED_TRIGGER.format(chunk.chunk_index)),
                '',
                self.trigger.new(self.POD_ACQUIRED_TRIGGER.format(chunk.chunk_index)),
                f'Cnd_LootAcquired = {pod_name}, Player',
                f'Act_RemoveCargo = {pod_name}',
                self.hit_total_counter(),
                self.hit_mandrake_counter(),
            ])
            if chunk.is_mandrake:
                actions.extend([
                    f'Act_SpawnSolar = {self.SUCCESS_MARKER}',
                    self.trigger.turn('POD_MANDRAKE_ACQUIRE_have_remaining'),
                    self.trigger.turn('POD_MANDRAKE_ACQUIRE_have_remaining__false'),
                    '',
                    ####
                    self.trigger.new('POD_MANDRAKE_ACQUIRE_have_remaining'),
                    self.direct.inside_pos(self.SYSTEM_NAME, self.TOTAL_COUNTER, 5000, obj=self.TOTAL_COUNTER),
                    self.trigger.off('POD_MANDRAKE_ACQUIRE_have_remaining__false'),
                    self.mark_all_chunks(),
                    self.mission.script.line(605),
                    self.trigger.turn('LOOT_MISSION_perfect_objective'),
                    '',
                    ####
                    self.trigger.new('POD_MANDRAKE_ACQUIRE_have_remaining__false'),
                    f'Cnd_Timer = 1',
                    self.trigger.turn(self.POD_SUCCESS),
                    self.trigger.off('POD_MANDRAKE_ACQUIRE_have_remaining'),
                    '',
                ])

        return SINGLE_DIVIDER.join(actions)

    def hit_mandrake_counter(self):
        damage = ((100 / self.MANDRAKE_ARRIVE_PODS) / 100) * 1.025
        return f'Act_AdjHealth = {self.MANDRAKE_COUNTER}, -{damage}'

    def hit_total_counter(self):
        damage = ((100 / self.CHUNKS_COUNT) / 100) * 1.025
        return f'Act_AdjHealth = {self.TOTAL_COUNTER}, -{damage}'

    def define_triggers(self):
        self.triggers_defined = True
        content = [
            self.trigger.new(self.MAIN, dry=True),
            self.draw_main_chunks(),
            f'Act_SpawnSolar = {self.MANDRAKE_COUNTER}',
            f'Act_SpawnSolar = {self.TOTAL_COUNTER}',
            self.trigger.turn('POD_mandrake_arrive'),
            self.trigger.turn('POD_all_acquired'),
            self.trigger.turn('POD_timeout'),
            '',
            ####
            self.trigger.new('POD_mandrake_arrive'),
            f'Cnd_Destroyed = {self.MANDRAKE_COUNTER}',
            self.draw_mandrake_chunks(),
            '',
            ####
            self.trigger.new('POD_all_acquired'),
            f'Cnd_Destroyed = {self.TOTAL_COUNTER}',
            self.reward_solar.spawn(),
            self.reward_solar.fuse('fuse_dump_cargo'),
            self.trigger.turn(self.POD_SUCCESS),
            '',
            ####
            self.trigger.new('POD_timeout'),
            f'Cnd_Timer = {self.MISSION_TIMEOUT}',
            self.trigger.turn('POD_mandrake_in'),
            self.trigger.turn('POD_mandrake_in__false'),
            '',
            ####
            self.trigger.new('POD_mandrake_in'),
            self.direct.inside_pos(self.SYSTEM_NAME, self.TOTAL_COUNTER, 5000, obj=self.SUCCESS_MARKER),
            self.deactivate_chunks(),
            self.trigger.turn(self.POD_SUCCESS),
            self.trigger.off('POD_mandrake_in__false'),
            self.destroy_all_chunks(),
            '',
            ####
            self.trigger.new('POD_mandrake_in__false'),
            f'Cnd_Timer = 0.25',
            'Act_ChangeState = FAIL, 1',
            '',
            ####
            self.trigger.new(self.POD_SUCCESS),
            DRY_RUN,
            self.trigger.off('POD_timeout'),
            self.trigger.off('POD_mandrake_in'),
            self.trigger.off('POD_mandrake_in__false'),
            self.trigger.off('POD_all_acquired'),
            self.trigger.off('POD_MANDRAKE_ACQUIRE_have_remaining'),
            self.trigger.off('POD_MANDRAKE_ACQUIRE_have_remaining__false'),
            self.trigger.turn(self.END_TRIGGER),
            ####
            ####
            self.get_chunk_triggers(),
            '',
        ]
        return SINGLE_DIVIDER.join(content)


class Misson05(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m05/m05.ini'
    FOLDER = 'M05'
    FILE = 'm05'
    START_SAVE_ID = 32500
    START_SAVE_RU_NAME = MS('Планета Форбс', 'Planet Forbes')
    STATIC_NPCSHIPS = NPCSHIPS
    SCRIPT_INDEX = 5
    DIRECT_SYSTEMS = [S.li_for, S.sig17]
    RTC = ['vendor_msn']
    INIT_OFFER = MultiLine(
        [
            'ЗАДАЧА:',
            'Выяснить местоположения доктора Мандрейка и доставить его на планету Форбс.',
            '',
            'СЛОЖНОСТЬ:',
            'Средняя.',
            '',
            'НАГРАДА:',
            '12 500 кредитов.',
        ],
        [
            'OBJECTIVE:',
            'Find the location of professor Mandrake and get him to the Planet Forbes.',
            '',
            'DIFFICULTY:',
            'Medium.',
            '',
            'REWARD:',
            '12 500 credits.',
        ]
    ).get_content()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scient_pods = ScientPods(self, direct=self.direct, trigger=self.trigger)

    def get_initial_context(self) -> dict:
        context = super().get_initial_context()
        context['scient_pods'] = self.scient_pods
        return context

    def get_save_states(self):
        return [
            SaveState(self, 'smuggler', MS('Форбс, склад контрабанды', 'Forbes, smuggler Storage')),
            SaveState(self, 'convoy', MS('Сигма-17, транспорт Омега-9', 'Sigma-17, transport Omega-9')),
            SaveState(self, 'scient', MS('Сигма-17, взрыв исследовательской станции', 'Sigma-17, explosion of research station')),
            SaveState(self, 'arrest_battle', MS('Сигма-17, линкор Грифон', 'Sigma-17, battleship Griffin')),
        ]

    def get_dialogs(self):
        return [
            TextDialog(
                self, 'smuggler', MS('База с уязвимыми точками', 'Base with vulnerable points'),
                ru_content=MultiText([
                    'Чтобы уничтожить базу, вы должны проникнуть внутрь и уничтожить её ядро.',

                    'Атакуйте склады, отмеченные синим цветом на вашем интерфейсе, чтобы разблокировать двери базы.',

                    'После этого залетайте в туннель и атакуйте ядро.',

                    'В будущем вы сможете встретить подобные базы в случайных миссиях, которые можно взять в баре',
                ],
                    [
                    'In order to destoy base, you should enter inside this base and destroy the core.',

                    'Attack the storages, marked by blue color in your interface. Doors will be opened after explode of all storages.',

                    'After you enter the tunnel and destroy the core.',

                    'You can find such bases in bar missions against installations in freeflight mode.',
                ]),
            ),
            TextDialog(
                self, 'scient_pod', MS('Спасение учёных', "Saving of scients"),
                ru_content=MultiText([
                    'Спасательные капусулы не успели активироваться!',

                    'Уничтожьте обломки станции, чтобы разблокировать спасательные капсулы и подобрать учёных',

                    'Скорее! Системы обеспечения скоро откажут!',
                ],
                [
                    'The escape pods did not activate in time!',

                    'You must destroy station chunks and loot extracted escape pods.',

                    'Hurry! Support systems will soon fail!',
                ]
                ),
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
            NNObj(self, MS('Встретьтесь с Хечтер в баре планеты Форбс', 'Meet Hatcher in bar of Planet Forbes'),
                  name='meet_vendor', target='vendor_planet'),

            NNObj(self, O.LAUNCH, name='launch'),

            NNObj(self, O.TLR, target='for_tlr_1'),
            NNObj(self, O.TLR, target='for_tlr_2'),
            NNObj(self, O.TLR, target='for_tlr_3'),
            NNObj(self, O.TLR, target='for_tlr_4'),

            NNObj(self, MS('Сядьте на Детроит', 'Dock with Detroit'), name='first_dock_detroit', target='detroit', open_access=False),

            NNObj(self, MS('Направляйтесь на пиратскую базу', 'Go to pirate base'),
                  name='goto_piratebase', target='piratebase', towards=True),
            NNObj(self, MS('Сядьте на пиратскую базу', 'Dock with pirate base'), name='dock_piratebase', target='piratebase'),

            NNObj(self, MS('Направляйтесь к складу контрабанды', 'Go to smuggler\'s storage'), name='goto_storage', target='smuggler_storage', towards=True),

            NNObj(self, MS('Уничтожьте контрабандистов', 'Destroy smugglers'), name='destroy_smugglers'),
            NNObj(self, MS('Уничтожьте склады и ядро склада контрабанды',
                           'Destroy storage and core of the smuggler\'s storage'),
                  name='destroy_storage', target='smuggler_storage', nag=False),
            NNObj(self, MS('Заберите ключ', 'Collect the key'), name='get_a_key'),

            NNObj(self, MS('Возвращайтесь на Детроит', 'Go back to Detroit'), name='go_back_detroit', target='detroit', towards=True),
            NNObj(self, MS('Сядьте на Детроит', 'Dock with Detroit'), name='dock_detroit', target='detroit'),

            NNObj(self, O.JUMPGATE, target='sig17_jump'),

            NNObj(self, O.TLR, target='sig17_tlr_1'),
            NNObj(self, O.TLR, target='sig17_tlr_2'),

            NNObj(self, MS('Доберитесь до исследовательской станции', 'Reach research station'),
                  name='reach_research',target='research_base', towards=True),
            NNObj(self, MS('Сядьте на исследовательскую станцию', 'Dock with research station'),
                  name='try_to_dock_on_research'),

            NNObj(self, O.GOTO, name='goto_convoy', target='convoy'),

            NNObj(self, O.DESTROY_PIRATES, name='destroy_pirates'),
            NNObj(self, MS('Войдите в формацию с транспортом', 'Join transport formation'),
                  name='join_transport_formation'),
            NNObj(self, MS('Сопровождайте транспорт', 'Escort transport'), name='follow_transport'),
            NNObj(self, MS('Ожидайте разрешения на посадку', 'Wait docking approvement'), name='wait_for_docking_approve'),

            NNObj(self, MS('Спасите Мандрейка из обломков станции', 'Save Mandrake from station chunks!'), name='find_madrake_and_tractor_him'),
            NNObj(self, MS('Попытайтесь спасти всех учёных!', 'Try to save all scients!'), name='save_all_scients'),

            NNObj(self, MS('Возвращайтесь к торговому пути', 'Go back to tradelane'), name='goto_bship_tlr', target='bship_tlr2'),

            NNObj(self, MS('Уничтожьте рейнландские истребители', 'Destroy rheinland fighters'), name='destroy_rheinland_fighters'),

            NNObj(self, O.JUMPGATE, target='for_jump'),

            NNObj(self, O.DOCKRING, name='final_planet', target='vendor_planet'),

        ]

    def get_static_points(self):
        defined_points = []

        defined_points.extend([
            Solar(self, S.li_for, 'smuggler_storage', ru_name=MS('Склад контрабанды', "Smuggler's storage"),
                  archetype='rmbase_smuggler', loadout='m05_smuggler_storage',
                  labels=['smuggler']),

            Solar(self, S.sig17, 'research_base', ru_name=MS('Исследовательская станция Кларк', 'Research station Clark'),
                  archetype='d_depot_clean', loadout='depot', labels=['deepspace']),
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
            Capital(self, 'armored', ru_name=MS('Транспорт Омега-9', "Transport Omega-9"), **armored_ship),
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
                    'li_military',
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
                    level=NPC.D10,
                    equip_map=EqMap(base_level=5),
                    animated_wings=False,
                    extra_equip=[
                        'equip = cloak_fast, HpCloak01, 1',
                    ],
                )
            ),
        ]
