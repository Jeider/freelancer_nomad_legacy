import random

from universe import sirius as S
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors

from story.ingame import objectives as O
from story.ingame.tools import (
    Point, Obj, Conn, NNObj, Ship, Solar, Capital, SaveState, DockableBattleshipSolar,
    Direct, Trigger
)

from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT, GENERIC_MOUNTED_ROTATABLE, GENERIC_TWO_POINT_MOVE2

from world.npc import NPC, EqMap
from world import ship
from universe import faction

from text.dividers import SINGLE_DIVIDER, DIVIDER


NPCSHIPS = '''
[NPCShipArch]
nickname = ms13_no_fighter
loadout = ms13_no_fighter
level = d13
ship_archetype = no_fighter
pilot = mod_fighter_version_a
state_graph = FIGHTER
npc_class = lawful, FIGHTER

[NPCShipArch]
nickname = ms13_no_elite
loadout = ms13_no_elite
level = d13
ship_archetype = no_elite
pilot = mod_fighter_version_a
state_graph = FIGHTER
npc_class = lawful, FIGHTER

[NPCShipArch]
nickname = ms13_beast_ship_far
loadout = beast_ship_far
level = d13
ship_archetype = beast_ship
pilot = MSN13_Nomad_Battleship
state_graph = CRUISER
npc_class = lawful, CRUISER

[NPCShipArch]
nickname = ms13_beast_ship_far_near
loadout = beast_ship_far_near_bh
level = d13
ship_archetype = beast_ship
pilot = MSN13_Nomad_Battleship
state_graph = CRUISER
npc_class = lawful, CRUISER


[NPCShipArch]
nickname = ms13_no_fighter_catcher
loadout = ms13_no_fighter_cd
level = d13
ship_archetype = no_fighter
pilot = pilot_mod_catcher
state_graph = FIGHTER
npc_class = lawful, FIGHTER

[NPCShipArch]
nickname = MSN13_Nomad_Battleship
loadout = MSN13_Nomad_Battleship
level = d18
ship_archetype = no_battleship
pilot = MSN13_Nomad_Battleship
state_graph = CRUISER
npc_class = lawful, CRUISER

[NPCShipArch]
nickname = ms13_li_dread
loadout = li_dreadnought_03
level = d10
ship_archetype = li_dreadnought
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

[NPCShipArch]
nickname = ms13_osiris
loadout = li_battleship_02
level = d10
ship_archetype = or_osiris
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

[NPCShipArch]
nickname = beast_fire_shiparch
loadout = beast_fire_ship
level = d10
ship_archetype = beast_ultra_fire_ship
pilot = pilot_mod_bomber
state_graph = CRUISER
npc_class = lawful, CRUISER, d5

[NPCShipArch]
nickname = beast_weapon_shiparch
loadout = beast_large_weapon_ship
level = d10
ship_archetype = beast_weapon
pilot = mod_fighter_version_a
state_graph = CRUISER
npc_class = lawful, CRUISER, d5
'''


class Kernel:
    def __init__(self, kernel_index, ships_indexes=None):
        self.kernel_index = kernel_index
        self.ship_indexes = ships_indexes if ships_indexes else []

    def add_ship_index(self, ship_index):
        self.ship_indexes.append(ship_index)

    def get_kernel_index(self):
        return f'{self.kernel_index:02d}'


class ActiveKernel:

    MAIN = 'ACTIVE_KERNEL_init'
    KERNEL_NAME = 'om13_alt_field_kernels1_{0}'
    KERNEL_TRIGGER_NAME = 'ACTIVE_KERNEL_{0}_detect'
    KERNELS_COUNT = 65
    SHIPS_PER_KERNEL = 3
    SHIPS_COUNT = KERNELS_COUNT * SHIPS_PER_KERNEL
    SHIP_GROUP = 'active_kernel_ship'
    SHIP_OFFSETS = [
        (0, 150, 0),
        (100, -40, 0),
        (-100, -40, 0),
    ]
    NOMAD_SETREP = 'OUTER_KERNEL_setrep'
    SHIP_OBJLIST = 'ol_no_avoid'
    DETECT_RANGE = 600
    NOMAD_SHIP_CLASS = 'active_kernel_ship'
    SYSTEM_NAME = S.om13_alt.NAME

    def __init__(self, direct, trigger):
        self.direct: Direct = direct
        self.trigger: Trigger = trigger
        self.kernels = []
        self.init_kernels()
        self.defined = False

    def init_kernels(self):
        ship_index = 1
        kernel_index = 1
        for i in range(1, self.KERNELS_COUNT+1):
            kernel = Kernel(kernel_index=kernel_index)
            self.kernels.append(kernel)
            for j in range(1, self.SHIPS_PER_KERNEL+1):
                kernel.add_ship_index(ship_index)
                ship_index += 1
            kernel_index += 1

    def turn(self):
        if not self.defined:
            raise Exception('Active kernel is not defined')
        return self.trigger.turn(self.MAIN)

    def activate_kernels(self):
        content = []
        for kernel in self.kernels:
            content.append(
                self.trigger.turn(self.KERNEL_TRIGGER_NAME.format(kernel.get_kernel_index()))
            )
        return SINGLE_DIVIDER.join(content)

    def deactivate_kernels(self):
        content = []
        for kernel in self.kernels:
            content.append(
                self.trigger.off(self.KERNEL_TRIGGER_NAME.format(kernel.get_kernel_index()))
            )
        return SINGLE_DIVIDER.join(content)

    def get_kernel_triggers(self):
        triggers = []
        for kernel in self.kernels:
            name = self.KERNEL_NAME.format(kernel.get_kernel_index())
            pos = self.direct.get_point(self.SYSTEM_NAME, name).get_position()

            kernel_actions = [
                self.trigger.new(self.KERNEL_TRIGGER_NAME.format(kernel.get_kernel_index())),
                self.direct.inside_pos(self.SYSTEM_NAME, name, self.DETECT_RANGE),
            ]

            ship_index = 0
            for ship_member_index in kernel.ship_indexes:
                ship_offset = self.SHIP_OFFSETS[ship_index]
                ship_pos = [
                    float(pos[0])+ship_offset[0],
                    float(pos[1])+ship_offset[1],
                    float(pos[2])+ship_offset[2]
                ]
                kernel_actions.append(
                    f'Act_SpawnShip = {self.SHIP_GROUP}{ship_member_index}, {self.SHIP_OBJLIST}, {ship_pos[0]}, {ship_pos[1]}, {ship_pos[2]}'
                )
                kernel_actions.append(self.trigger.turn(self.NOMAD_SETREP))
                ship_index += 1

            triggers.append(SINGLE_DIVIDER.join(kernel_actions))

        return DIVIDER.join(triggers)

    def hide_ships(self):
        content = []
        for i in range(self.SHIPS_COUNT+1):
            content.append(
                f'Act_Destroy = {self.SHIP_GROUP}{i}, SILENT'
            )
        return SINGLE_DIVIDER.join(content)

    def define(self):
        self.defined = True
        content = [
            self.trigger.new(self.MAIN, dry=True),
            self.activate_kernels(),
            '',
            self.get_kernel_triggers(),
        ]
        return SINGLE_DIVIDER.join(content)

    def deactivate(self):
        content = [
            self.deactivate_kernels(),
            self.hide_ships(),
        ]
        return SINGLE_DIVIDER.join(content)


class Misson13(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m13/m13.ini'
    FOLDER = 'M13'
    FILE = 'm13'
    START_SAVE_ID = 33300
    SCRIPT_INDEX = 13
    DIRECT_SYSTEMS = [S.sphere2, S.sphere2_inside, S.beast01, S.om13_alt]
    STATIC_NPCSHIPS = NPCSHIPS
    RTC = ['captured', 'last_brief']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.active_kernel = ActiveKernel(direct=self.direct, trigger=self.trigger)

    def get_initial_context(self) -> dict:
        context = super().get_initial_context()
        context['active_kernel'] = self.active_kernel
        return context

    def get_save_states(self):
        return [
            SaveState(self, 'beast_reactor', 'Сфера. Крыг ожил'),
            SaveState(self, 'chamber01', 'Омега-13. Кокон'),
            SaveState(self, 'chamber02', 'Омега-13. Второй кокон'),
            SaveState(self, 'chamber02_after', 'Омега-13. После второго кокона'),
        ]

    def get_ingame_thorns(self):
        return [
            IngameThorn(
                self,
                system_class=S.sphere2,
                template=GENERIC_MOUNTED_ROTATABLE,
                name='m13_osiris_hit',
                params={
                    'cam_pos_x': 50,
                    'cam_pos_y': -40,
                    'cam_pos_z': 350,
                    'rotate_duration': 20,
                    'rotate_angle': 60,
                    'remove_smooth': True,
                },
                duration=20,
                target='osiris',
            ),
            IngameThorn(
                self,
                system_class=S.sphere2,
                template=GENERIC_TWO_POINT,
                name='m13_laser_fire',
                points={
                    'camera': 'cam_laser',
                    'marker': 'cam_laser_marker',
                },
                duration=25,
            ),
            IngameThorn(
                self,
                system_class=S.sphere2,
                template=GENERIC_TWO_POINT_MOVE2,
                name='m13_laser_fire_done',
                points={
                    'camera': 'cam_alaric',
                    'marker': 'cam_alaric_marker',
                    'marker_two': 'cam_alaric2',
                },
                params={
                    'move_duration': 30,
                    'remove_smooth': True,
                },
                duration=60,
            ),
            IngameThorn(
                self,
                system_class=S.sphere2,
                template=GENERIC_TWO_POINT_MOVE2,
                name='m13_opens',
                points={
                    'camera': 'cam_open',
                    'marker': 'cam_open_marker',
                    'marker_two': 'cam_open2',
                },
                params={
                    'move_duration': 15,
                },
                duration=60,
            ),
            IngameThorn(
                self,
                system_class=S.sphere2,
                template=GENERIC_TWO_POINT,
                name='m13_beast_fire',
                points={
                    'camera': 'cam_fire',
                    'marker': 'cam_fire_marker',
                },
                duration=25,
            ),
            IngameThorn(
                self,
                system_class=S.sphere2,
                template=GENERIC_TWO_POINT_MOVE2,
                name='m13_beast_collector',
                points={
                    'camera': 'cam_collector',
                    'marker': 'cam_collector_marker',
                    'marker_two': 'cam_collector2',
                },
                params={
                    'move_duration': 15,
                },
                duration=25,
            ),
            IngameThorn(
                self,
                system_class=S.sphere2,
                template=GENERIC_TWO_POINT_MOVE2,
                name='m13_sphere_help',
                points={
                    'camera': 'cam_help',
                    'marker': 'edison',
                    'marker_two': 'cam_help2',
                },
                params={
                    'move_duration': 8,
                    # 'remove_smooth': True,
                },
                duration=60,
            ),
            IngameThorn(
                self,
                system_class=S.sphere2,
                template=GENERIC_TWO_POINT,
                name='m13_sphere_help2',
                points={
                    'camera': 'cam_edison',
                    'marker': 'edison',
                },
                duration=25,
            ),
            IngameThorn(
                self,
                system_class=S.om13_alt,
                template=GENERIC_TWO_POINT,
                name='m13_engine_cam1',
                points={
                    'camera': 'engine_cam1',
                    'marker': 'after_chamber2_player',
                },
                duration=25,
            ),
            IngameThorn(
                self,
                system_class=S.om13_alt,
                template=GENERIC_TWO_POINT,
                name='m13_engine_cam2',
                points={
                    'camera': 'engine_cam2',
                    'marker': 'engine_cam2_mrk',
                },
                duration=25,
            ),
            IngameThorn(
                self,
                system_class=S.om13_alt,
                template=GENERIC_TWO_POINT,
                name='m13_engine_cam3',
                points={
                    'camera': 'engine_cam3',
                    'marker': 'engine_cam3_mrk',
                },
                duration=25,
            ),
            IngameThorn(
                self,
                system_class=S.om13_alt,
                template=GENERIC_TWO_POINT,
                name='m13_engine_cam4',
                points={
                    'camera': 'engine_cam4',
                    'marker': 'after_chamber2_edison',
                },
                duration=25,
            ),
            IngameThorn(
                self,
                system_class=S.om13_alt,
                template=GENERIC_TWO_POINT,
                name='m13_engine_cam5',
                points={
                    'camera': 'engine_cam5',
                    'marker': 'after_chamber2_player',
                },
                duration=25,
            ),
            IngameThorn(
                self,
                system_class=S.om13_alt,
                template=GENERIC_MOUNTED_ROTATABLE,
                name='m13_bh_cam1',
                params={
                    'cam_pos_x': -50,
                    'cam_pos_y': 10,
                    'cam_pos_z': 0,
                    'rotate_duration': 10,
                    'rotate_angle': -20,
                    'remove_smooth': True,
                },
                duration=60,
                target='Player',
            ),
            IngameThorn(
                self,
                system_class=S.om13_alt,
                template=GENERIC_MOUNTED_ROTATABLE,
                name='m13_bh_cam2',
                params={
                    'cam_pos_x': 50,
                    'cam_pos_y': 10,
                    'cam_pos_z': 0,
                    'rotate_duration': 10,
                    'rotate_angle': -5,
                    'remove_smooth': False,
                },
                duration=60,
                target='Player',
            ),
            IngameThorn(
                self,
                system_class=S.om13_alt,
                template=GENERIC_TWO_POINT,
                name='m13_bh_cam3',
                points={
                    'camera': 'bh_cam3',
                    'marker': 'bh_player',
                },
                duration=90,
            ),
            IngameThorn(
                self,
                system_class=S.om13_alt,
                template=GENERIC_TWO_POINT_MOVE2,
                name='m13_bh_cam3_1',
                points={
                    'camera': 'bh_cam3d',
                    'marker': 'bh_player',
                    'marker_two': 'bh_cam3c',
                },
                params={
                    'move_duration': 5,
                    'remove_smooth': True,
                },
                duration=60,
            ),
            IngameThorn(
                self,
                system_class=S.om13_alt,
                template=GENERIC_TWO_POINT_MOVE2,
                name='m13_bh_cam3_2',
                points={
                    'camera': 'bh_cam3c',
                    'marker': 'bh_player',
                    'marker_two': 'bh_cam3b',
                },
                params={
                    'move_duration': 5,
                    'remove_smooth': True,
                },
                duration=60,
            ),
            IngameThorn(
                self,
                system_class=S.om13_alt,
                template=GENERIC_TWO_POINT_MOVE2,
                name='m13_bh_cam3_3',
                points={
                    'camera': 'bh_cam3b',
                    'marker': 'bh_player',
                    'marker_two': 'bh_cam3a',
                },
                params={
                    'move_duration': 5,
                    'remove_smooth': True,
                },
                duration=60,
            ),
            IngameThorn(
                self,
                system_class=S.om13_alt,
                template=GENERIC_TWO_POINT_MOVE2,
                name='m13_bh_cam3_4',
                points={
                    'camera': 'bh_cam3a',
                    'marker': 'bh_player',
                    'marker_two': 'bh_cam3',
                },
                params={
                    'move_duration': 5,
                    'remove_smooth': True,
                },
                duration=60,
            ),
            IngameThorn(
                self,
                system_class=S.om13_alt,
                template=GENERIC_TWO_POINT,
                name='m13_bh_cam4',
                points={
                    'camera': 'bh_cam4',
                    'marker': 'bh_player',
                },
                duration=90,
            ),
            IngameThorn(
                self,
                system_class=S.om13_alt,
                template=GENERIC_TWO_POINT,
                name='m13_bh_cam4_1',
                points={
                    'camera': 'bh_cam4a',
                    'marker': 'bh_player',
                },
                duration=90,
            ),
            IngameThorn(
                self,
                system_class=S.om13_alt,
                template=GENERIC_TWO_POINT,
                name='m13_bh_cam4_2',
                points={
                    'camera': 'bh_cam4b',
                    'marker': 'bh_player',
                },
                duration=90,
            ),
        ]

    def get_static_points(self):
        sphere_points = [
            'goto_core',
            'goto_lazer',
            'goto_catacomb',
            'goto_catacomb2',
            'exit_catacomb1',
            'exit_catacomb2',
            'escape1',
            'escape2',
        ]

        sphere_solars = [
            'lazer1',
            'krieg1',
            'sph02_door02',
            'sph02_door02_open',
            'sph02_to_inside',
            'inside_to_sph02',
            'sph02_door03',
            'sph02_door03_open',
            'sph02_door03_close',
        ]

        sphere_gens = [
            'sph2_core_F01',
            'sph2_core_F02',
            'sph2_core_F03',
            'sph2_core_F04',
            'sph2_core_F05',
            'sph2_core_F06',
            'sph2_core_F07',
            'sph2_core_F08',
            'sph2_core_G01',
            'sph2_core_G02',
            'sph2_core_G03',
            'sph2_core_G04',
            'sph2_core_G05',
            'sph2_core_G06',
            'sph2_core_G07',
            'sph2_core_G08',
        ]

        krieg_gens = [
            'krieg_gen1',
            'krieg_gen2',
            'krieg_gen3',
            'krieg_gen4',
            'krieg_gen5',
            'krieg_gen6',
        ]

        inside_solars = [
            ('sph02_ins_airlock_exit', 'выход'),
        ]

        inside_points = [
            'inside01',
            'inside02',
            'inside02b',
            'inside03',
            'inside04',
            'inside05',
            'inside06',
            'inside07',
        ]

        defined_points = []
        for p in sphere_points:
            defined_points.append(
                Point(self, S.sphere2, p)
            )

        for p in inside_points:
            defined_points.append(
                Point(self, S.sphere2_inside, p)
            )

        for sol in sphere_solars:
            defined_points.append(
                Solar(self, S.sphere2, sol, ru_name='test'),
            )

        for s_gen in sphere_gens:
            defined_points.append(
                Solar(self, S.sphere2, s_gen, ru_name='Генератор',
                      archetype='sphere_generator', loadout='sphere_generator_laser'),
            )

        for kr_gen in krieg_gens:
            defined_points.append(
                Solar(self, S.sphere2, kr_gen, ru_name='Генератор',
                      archetype='beast_generator', labels=['the_krieg', 'krieg_the_gen']),
            )

        for sol, ru_name in inside_solars:
            defined_points.append(
                Solar(self, S.sphere2_inside, sol, ru_name=ru_name),
            )

        defined_points.extend([
            Solar(self, S.sphere2, 'krieg_sleep', ru_name='Крыг', loadout='beast_sleep', archetype='beast_1500'),
            Solar(self, S.sphere2, 'krieg_opens', ru_name='Крыг', loadout='beast_arrive', archetype='beast_1500',
                  labels=['the_krieg']),
            Solar(self, S.sphere2, 'krieg_opens_force', ru_name='Крыг',
                  loadout='beast_force_open', archetype='beast_1500'),
            Solar(self, S.sphere2, 'krieg_collector', ru_name='Крыг',
                  loadout='beast_collector', archetype='beast_1500'),
            Solar(self, S.sphere2, 'krieg_silent', ru_name='Крыг',
                  loadout='beast_silent', archetype='beast_1500'),
            Solar(self, S.sphere2, 'hit_fx', ru_name='Удар!', loadout='beast_hit', archetype='hidden_connect'),
        ])

        gens_count = 3
        gens = [f'gen{i}' for i in range(1, gens_count+1)]
        for sol in gens:
            defined_points.append(
                Solar(self, S.sphere2, sol, ru_name='Генератор', labels=['enemy', 'lazergen', 'lazer_generators'],
                      archetype='dyson_generator', loadout='dyson_generator_msn3'),
            )

        wplatforms_count = 5
        wplatforms = [f'wp{i}' for i in range(1, wplatforms_count+1)]
        for sol in wplatforms:
            defined_points.append(
                Solar(self, S.sphere2, sol, ru_name='Орудийная платформа', labels=['enemy', 'lazergen'],
                      archetype='wplatform_ms2', loadout='ms2_the_platform'),
            )

        krieg_turrets = []

        large_turrets_count = 14
        large_wplatforms = [f'big_turr{i:02d}' for i in range(1, large_turrets_count+1)]
        for sol in large_wplatforms:
            solar = Solar(self, S.sphere2, sol, ru_name='Орудийная платформа',
                labels=['enemy', 'the_krieg'],
                archetype='lair_platform', loadout='beast_platform01',
                pilot='pilot_solar_hardest_beast',
            )
            defined_points.append(solar)
            krieg_turrets.append(solar)

        small_turrets_count = 12
        small_wplatforms = [f'def_turr{i:02d}' for i in range(1, small_turrets_count+1)]
        for sol in small_wplatforms:
            solar = Solar(self, S.sphere2, sol, ru_name='Орудийная платформа',
                labels=['enemy', 'the_krieg'],
                archetype='lair_platform', loadout='beast_platform02',
                pilot='pilot_solar_hardest_beast',
            )
            defined_points.append(solar)
            krieg_turrets.append(solar)

        self.add_solar_group('KRIEG_WP', krieg_turrets)

        defined_points.append(
            DockableBattleshipSolar(
                self, S.sphere2, 'osiris_arrive1',
                archetype='o_osiris', loadout='li_battleship_02',
                ru_name='Линкор Осирис', base='sphere2_99_base',
                labels=['friend', 'asf', 'osiris']),
        )

        defined_points.append(
            DockableBattleshipSolar(
                self, S.sphere2, 'osiris_escape',
                archetype='o_osiris', loadout='li_battleship_02',
                ru_name='Линкор Осирис', base='sphere2_99_base',
                labels=['friend', 'asf', 'osiris']),
        )

        defined_points.append(
            Solar(self, S.sphere2_inside, 'inside_column1', ru_name='Поток энергии Сферы',
                  labels=['enemy', 'energy_beam'],
                  archetype='sphere_energy_column', loadout='sphere_column_power'),
        )
        defined_points.append(
            Solar(self, S.sphere2_inside, 'inside_column2', ru_name='Поток энергии Сферы',
                  labels=['enemy', 'energy_beam'],
                  archetype='sphere_energy_column', loadout='sphere_column_power'),
        )

        sphere_no_caps = [
            'sph_no_bs01',
            'sph_no_bs02',
            'sph_no_bs03',
            'sph_no_bs04',
            'sph_no_bs05',
        ]
        no_caps_sols = []
        for no_cap in sphere_no_caps:
            no_sol = Solar(
                self, S.sphere2, no_cap,
                ru_name='Линкор Кочевников',
                faction='fc_n_grp',
                labels=['enemy', 'no_cap', 'nomad'],
                archetype='d_n_battleship',
                loadout='MSN13_Nomad_Battleship'
            )
            defined_points.append(no_sol)
            no_caps_sols.append(no_sol)

        self.add_solar_group('SPHERE_NO_CAP', no_caps_sols)

        defined_points.append(
            Solar(self, S.sphere2, 'power_container', ru_name='Контейнер с энергоядром'),
        )

        sphere_walls = [
            'wall1',
            'wall2',
            'wall3',
            'wall4',
        ]
        wall_sols = []
        for wall in sphere_walls:
            wall_sol = Solar(
                self, S.sphere2, wall,
                ru_name='Стена Сферы',
                archetype='beast_move_block',
                loadout='sphere_extend_block01'
            )
            defined_points.append(wall_sol)
            wall_sols.append(wall_sol)

        self.add_solar_group('SPHERE_WALL', wall_sols)

        ### OMEGA 13

        defined_points.append(
            DockableBattleshipSolar(
                self, S.om13_alt, 'osiris_bh1',
                archetype='o_osiris', loadout='li_battleship_02',
                ru_name='Линкор Осирис', base='om13_alt_99_base',
                labels=['friend', 'asf', 'osiris']),
        )

        om13_points = [
            'kernels1',
            'kernels1_exit',
            'kernels1_inside',
            'kernels1_inside2',
            'kernels1_tunnel',
            'kernels1_after',

            'kernel2_ast1_in',
            'kernel2_ast1_wall1',
            'kernel2_ast1_mid1',
            'kernel2_ast1_wall2',
            'kernel2_ast1_end',
            'kernel2_ast2_in',
            'kernel2_ast2_mid1',
            'kernel2_ast2_end',
            'kernel2_ast3_in',
            'kernel2_ast3_mid1',
            'kernel2_ast3_exit',
            'kernel2_ast4_in',
            'kernel2_ast4_split',
            'kernel2_ast4_mid1',
            'kernel2_ast4_exit',
            'kernel2_ast5_in',
            'kernel2_ast5_wall1',
            'kernel2_ast5_core',
            'kernel2_ast5_wall2',
            'kernel2_ast5_exit',
            'kernel2_ast5_out',
        ]

        for p in om13_points:
            defined_points.append(
                Point(self, S.om13_alt, p),
            )

        defined_points.extend([
            Solar(self, S.om13_alt, 'inside_kernel01', ru_name='Номадское зерно',
                  loadout='beast_kernel_light', archetype='inside_beast_kernel'),
            Solar(self, S.om13_alt, 'inside_kernel02', ru_name='Номадское зерно',
                  loadout='beast_kernel_light', archetype='inside_beast_kernel'),
        ])

        kernels1_sols = []

        kernels1_count = ActiveKernel.KERNELS_COUNT
        kernels1_names = [f'om13_alt_field_kernels1_{i:02d}' for i in range(1, kernels1_count+1)]
        for sol in kernels1_names:
            solar = Solar(self, S.om13_alt, sol, ru_name='Номадское зерно',
                archetype='space_kernel', loadout='space_kernel_light',
            )
            defined_points.append(solar)
            kernels1_sols.append(solar)

        self.add_solar_group('KERNELS1', kernels1_sols)

        kernels = [
            'om13alt_beast_kernel1_01',
            'om13alt_ast_a_inside_kernel01',
            'om13alt_ast_a_inside_kernel02',
        ]
        kernel_sols = [
            Solar(self, S.om13_alt, kernel, ru_name='Номадское зерно',
                  archetype='space_beast_kernel', loadout='space_beast_kernel_light')
            for kernel in kernels
        ]
        defined_points.extend(kernel_sols)
        self.add_solar_group('OM13_BEAST_KERNELS', kernel_sols)

        walls = [
            'om13alt_ast_b_dmg1',
            'om13alt_ast_b_dmg2',
            'om13alt_ast_a_dmg01',
            'om13alt_ast_a_dmg02',
            'om13alt_ast_a_dmg03',
            'om13alt_ast_a_dmg04',
            'om13alt_ast_a_dmg05',
            'om13alt_ast_a_dmg06',
        ]
        wall_sols = [
            Solar(self, S.om13_alt, wall, ru_name='Перегородка туннеля',
                  archetype='om15_static_xlarge_ast04_dmg')
            for wall in walls
        ]
        defined_points.extend(wall_sols)
        self.add_solar_group('OM13_WALLS', wall_sols)

        defined_points.append(
            Solar(self, S.om13_alt, 'om13alt_ast_a_lrg01', ru_name='Астероид',
                  archetype='om15_static_large_ast02'),
        )

        defined_points.append(
            Solar(self, S.om13_alt, 'om13alt_ast_a_lrg01', ru_name='Астероид',
                  archetype='om15_static_large_ast02'),
        )

        defined_points.extend([
            Solar(self, S.om13_alt, 'krieg_far', ru_name='Крыг', loadout='beast_sleep', archetype='beast_1500'),
        ])

        om13_caps_in_group = 3
        om13_no_caps = [
            ('OM13_BS1', 'bs1'),
            ('OM13_BS2', 'bs2'),
            ('OM13_BS3', 'bs3'),
        ]
        for group_name, group in om13_no_caps:
            group_sols = []
            for index in range(1, om13_caps_in_group+1):
                no_cap = f'{group}_{index}'
                no_sol = Solar(
                    self, S.om13_alt, no_cap,
                    ru_name='Линкор Кочевников',
                    faction='fc_n_grp',
                    labels=['enemy', 'no_cap', 'nomad', group_name],
                    archetype='d_n_battleship',
                    loadout='MSN13_Nomad_Battleship'
                )
                defined_points.append(no_sol)
                group_sols.append(no_sol)

            self.add_solar_group(group_name, group_sols)

        defined_points.append(
            Solar(self, S.om13_alt, 'om13alt_bh', ru_name='Чёрная дыра'),
        )

        return defined_points

    def get_capital_ships(self):
        li_dread = {
            'npc_ship_arch': 'ms13_li_dread',
            'faction': 'asf_grp',
            'labels': ['friend', 'asf_a', 'asf'],
        }
        beast_fire = {
            'npc_ship_arch': 'beast_fire_shiparch',
            'labels': ['the_krieg_core'],
        }
        osiris = {
            'npc_ship_arch': 'ms13_osiris',
            'faction': 'asf_grp',
            'labels': ['friend', 'asf'],
        }

        caps = [
            Capital(self, 'li_dread', ru_name='Линкор Миссури', **li_dread),
            Capital(self, 'krieg_fire', ru_name='Выстрел', radius=0, **beast_fire),
            Capital(self, 'osiris', ru_name='Линкор Осирис', **osiris),
        ]

        return caps

    def get_nn_objectives(self):
        return [
            NNObj(self, O.LAUNCH, name='launch'),

            NNObj(self, O.GOTO, name='goto_core', target='goto_core'),
            NNObj(self, O.GOTO, name='goto_lazer', target='goto_lazer'),

            NNObj(self, 'Уничтожьте генераторы лазерной установки', name='destroy_lazergens'),

            NNObj(self, O.GOTO, target='goto_catacomb'),
            NNObj(self, O.GOTO, target='goto_catacomb2'),

            NNObj(self, O.GOTO, target='inside01'),
            NNObj(self, O.GOTO, target='inside02'),
            NNObj(self, O.GOTO, target='inside02b'),
            NNObj(self, O.GOTO, target='inside03'),
            NNObj(self, O.GOTO, target='inside04'),
            NNObj(self, O.GOTO, target='inside05'),
            NNObj(self, O.GOTO, target='inside06'),
            NNObj(self, O.GOTO, target='inside07'),

            NNObj(self, 'Уничтожьте энергопоток', target='inside_column1'),
            NNObj(self, 'Уничтожьте энергопоток', target='inside_column2'),

            NNObj(self, O.GOTO, target='exit_catacomb1'),
            NNObj(self, O.GOTO, target='exit_catacomb2'),

            NNObj(self, 'Уничтожьте контейнер энергоядра', name='destroy_powercell_container',
                  target='power_container'),
            NNObj(self, 'Подберите энергоядро', name='get_sphere_powercell'),

            NNObj(self, O.GOTO, target='escape1', reach_range=2000),
            NNObj(self, O.GOTO, target='escape2', reach_range=1500),

            NNObj(self, 'Сядьте на Осирис', name='dock_osiris_escape', target='osiris_escape'),

            NNObj(self, O.GOTO, target='kernels1'),
            NNObj(self, O.GOTO, target='kernels1_exit'),
            NNObj(self, O.GOTO, target='kernels1_inside', reach_range=500),
            NNObj(self, O.GOTO, target='kernels1_inside2', reach_range=500),
            NNObj(self, O.GOTO, target='kernels1_tunnel', reach_range=600),
            NNObj(self, O.GOTO, target='kernels1_after'),

            NNObj(self, O.GOTO, target='kernel2_ast1_in', reach_range=500),
            NNObj(self, O.GOTO, target='kernel2_ast1_wall1', reach_range=500),
            NNObj(self, O.GOTO, target='kernel2_ast1_mid1', reach_range=400),
            NNObj(self, O.GOTO, target='kernel2_ast1_wall2', reach_range=300),
            NNObj(self, O.GOTO, target='kernel2_ast1_end', reach_range=500),
            NNObj(self, O.GOTO, target='kernel2_ast2_in', reach_range=500),
            NNObj(self, O.GOTO, target='kernel2_ast2_mid1', reach_range=500),
            NNObj(self, O.GOTO, target='kernel2_ast2_end', reach_range=500),
            NNObj(self, O.GOTO, target='kernel2_ast3_in', reach_range=500),
            NNObj(self, O.GOTO, target='kernel2_ast3_mid1', reach_range=300),
            NNObj(self, O.GOTO, target='kernel2_ast3_exit', reach_range=500),
            NNObj(self, O.GOTO, target='kernel2_ast4_in', reach_range=500),
            NNObj(self, O.GOTO, target='kernel2_ast4_split', reach_range=500),
            NNObj(self, O.GOTO, target='kernel2_ast4_mid1', reach_range=500),
            NNObj(self, O.GOTO, target='kernel2_ast4_exit', reach_range=500),
            NNObj(self, O.GOTO, target='kernel2_ast5_in', reach_range=500),
            NNObj(self, O.GOTO, target='kernel2_ast5_wall1', reach_range=500),
            NNObj(self, O.GOTO, target='kernel2_ast5_core', reach_range=500),
            NNObj(self, O.GOTO, target='kernel2_ast5_wall2', reach_range=500),
            NNObj(self, O.GOTO, target='kernel2_ast5_exit', reach_range=500),
            NNObj(self, O.GOTO, target='kernel2_ast5_out', reach_range=600),

            NNObj(self, 'Уничтожьте перегородку', name='kernels1_door1', target='om13alt_ast_b_dmg2'),
            NNObj(self, 'Уничтожьте перегородку', name='kernels1_door2', target='om13alt_ast_b_dmg1'),
            NNObj(self, 'Уничтожьте зерно', name='destroy_inside_kernel01', target='inside_kernel01'),

            NNObj(self, 'Уничтожьте перегородку', name='om13alt_ast_a_dmg01', target='om13alt_ast_a_dmg01'),
            NNObj(self, 'Уничтожьте перегородку', name='om13alt_ast_a_dmg02', target='om13alt_ast_a_dmg02'),
            NNObj(self, 'Уничтожьте перегородку', name='om13alt_ast_a_dmg03', target='om13alt_ast_a_dmg03'),
            NNObj(self, 'Уничтожьте перегородку', name='om13alt_ast_a_dmg04', target='om13alt_ast_a_dmg04'),
            NNObj(self, 'Уничтожьте перегородку', name='om13alt_ast_a_dmg05', target='om13alt_ast_a_dmg05'),
            NNObj(self, 'Уничтожьте перегородку', name='om13alt_ast_a_dmg06', target='om13alt_ast_a_dmg06'),

            NNObj(self, 'Уничтожьте номадские истребитекли', name='destroy_chamber_elite'),
            NNObj(self, 'Уничтожьте зерно', name='destroy_inside_kernel02', target='inside_kernel02'),

            NNObj(self, 'Подберите энергоядро', name='get_om13_powercell'),
            NNObj(self, 'Направляйтесь в чёрную дыру', target='om13alt_bh', towards=True),




        ]

    def get_ships(self):
        return [
            # Ship(
            #     self,
            #     'no_chamber',
            #     count=10,
            #     affiliation=faction.Nomad.CODE,
            #     system_class=S.sphere2,
            #     slide_z=60,
            #     slide_x=60,
            #     radius=0,
            #     labels=[
            #         'enemy',
            #         'nomad',
            #     ],
            #     static_npc_shiparch='ms13_no_fighter'
            # ),
            Ship(
                self,
                'sph_no_f01',
                count=5,
                affiliation=faction.Nomad.CODE,
                system_class=S.sphere2,
                slide_z=60, slide_x=60, radius=0,
                labels=['enemy', 'nomad'],
                static_npc_shiparch='ms13_no_fighter'
            ),
            Ship(
                self,
                'sph_no_f02',
                count=4,
                affiliation=faction.Nomad.CODE,
                system_class=S.sphere2,
                slide_z=60, slide_x=60, radius=0,
                labels=['enemy', 'nomad'],
                static_npc_shiparch='ms13_no_fighter'
            ),
            Ship(
                self,
                'sph_no_f03',
                count=4,
                affiliation=faction.Nomad.CODE,
                system_class=S.sphere2,
                slide_z=60, slide_x=60, radius=0,
                labels=['enemy', 'nomad'],
                static_npc_shiparch='ms13_no_fighter'
            ),
            Ship(
                self,
                'hatcher',
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
                    level=NPC.D19,
                    equip_map=EqMap(base_level=6),
                )
            ),
            Ship(
                self,
                'alaric',
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
                'wingman',
                count=5,
                system_class=S.om7,
                labels=[
                    'friend',
                    'asf',
                    'trent_wing'
                ],
                unique_npc_entry=True,
                base_name='Альфа',
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Defender,
                    level=NPC.D6,
                    equip_map=EqMap(base_level=6),
                )
            ),

            Ship(
                self,
                'edison_trent',
                actor=actors.EdisonTrent,
                labels=[
                    'friend',
                ],
                hero=True,
                radius=0,
                npc=NPC(
                    faction=faction.Corsairs,
                    ship=ship.Titan,
                    level=NPC.D19,
                    equip_map=EqMap(base_level=6),
                )
            ),
            Ship(
                self,
                'active_kernel_ship',
                count=ActiveKernel.SHIPS_COUNT,
                affiliation=faction.Nomad.CODE,
                system_class=S.om13_alt,
                radius=0,
                labels=['enemy', 'nomad'],
                static_npc_shiparch='ms13_no_fighter_catcher'
            ),
            Ship(
                self,
                'chamber1_no_fighter',
                count=12,
                affiliation=faction.Nomad.CODE,
                system_class=S.om13_alt,
                radius=0,
                labels=['enemy', 'nomad'],
                static_npc_shiparch='ms13_no_fighter'
            ),
            Ship(
                self,
                'chamber2_no_fighter',
                count=12,
                affiliation=faction.Nomad.CODE,
                system_class=S.om13_alt,
                radius=0,
                labels=['enemy', 'nomad', 'chamber_elite'],
                static_npc_shiparch='ms13_no_elite'
            ),
            Ship(
                self,
                'beast_ship_far',
                labels=[
                    'beast',
                    'enemy',
                ],
                radius=0,
                static_npc_shiparch='ms13_beast_ship_far'
            ),
            Ship(
                self,
                'beast_ship_far_near',
                labels=[
                    'beast',
                    'enemy',
                ],
                radius=0,
                static_npc_shiparch='ms13_beast_ship_far_near'
            ),
            Ship(
                self,
                'chaser1',
                count=3,
                affiliation=faction.Nomad.CODE,
                system_class=S.om13_alt,
                radius=0,
                slide_z=150,
                labels=['enemy', 'nomad'],
                static_npc_shiparch='ms13_no_fighter_catcher'
            ),
            Ship(
                self,
                'chaser2',
                count=3,
                affiliation=faction.Nomad.CODE,
                system_class=S.om13_alt,
                radius=0,
                slide_z=150,
                labels=['enemy', 'nomad'],
                static_npc_shiparch='ms13_no_fighter_catcher'
            ),
            Ship(
                self,
                'chaser3',
                count=3,
                affiliation=faction.Nomad.CODE,
                system_class=S.om13_alt,
                radius=0,
                slide_z=150,
                labels=['enemy', 'nomad'],
                static_npc_shiparch='ms13_no_fighter_catcher'
            ),
        ]
