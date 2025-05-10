import random

from universe import sirius as S
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors

from story.ingame import objectives as O
from story.ingame.tools import Point, Obj, Conn, NNObj, Ship, Solar, Capital, SaveState, DockableBattleshipSolar
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT, GENERIC_MOUNTED_ROTATABLE, GENERIC_TWO_POINT_MOVE2

from world.npc import NPC, EqMap
from world import ship
from universe import faction


NPCSHIPS = '''
[NPCShipArch]
nickname = ms13_no_fighter
loadout = ms6_no_fighter
level = d13
ship_archetype = no_fighter
pilot = mod_fighter_version_a
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


class Misson13(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m13/m13.ini'
    FOLDER = 'M13'
    FILE = 'm13'
    SCRIPT_INDEX = 13
    DIRECT_SYSTEMS = [S.sphere2, S.sphere2_inside, S.beast01]
    STATIC_NPCSHIPS = NPCSHIPS
    RTC = ['captured']

    def get_save_states(self):
        return [
            SaveState(self, 'beast_reactor', 'Сфера. Крыг ожил'),
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
                ru_name='Линкор Осирис', base='om13_chase_99_base',
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
                count=5,
                affiliation=faction.Nomad.CODE,
                system_class=S.sphere2,
                slide_z=60, slide_x=60, radius=0,
                labels=['enemy', 'nomad'],
                static_npc_shiparch='ms13_no_fighter'
            ),
            Ship(
                self,
                'sph_no_f03',
                count=5,
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
        ]
