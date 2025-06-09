import random

from universe import sirius as S
from universe.systems import li_mnh, sphere, co_cad
from story.ingame import ingame_mission
from story.math import euler_to_quat
from story import actors
from text.dividers import SINGLE_DIVIDER, DIVIDER

from story.ingame import names as N
from story.ingame import objectives as O
from story.ingame.tools import (
    Point, Obj, Conn, NNObj, Ship, Solar, Capital, SaveState, DockableBattleshipSolar, StaticJumpgate,
    MultiText, TextDialog, Direct, Trigger, DRY_RUN, DIALOG_YES_NO
)
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT, GENERIC_MOUNTED_ROTATABLE

from world.npc import NPC, EqMap
from world import ship
from universe import faction

NPCSHIPS = '''

[NPCShipArch]
nickname = cloak_checker_shiparch
loadout = cloak_checker_loadout
level = d20
ship_archetype = cloak_checker
pilot = transport_easy
state_graph = TRANSPORT
npc_class = lawful

[NPCShipArch]
nickname = ms6_rh_gunship
loadout = ms6_gunship
level = d25
ship_archetype = rh_gunboat
pilot = cruiser_anticruiser
state_graph = CRUISER
npc_class = lawful, CRUISER, d22

[NPCShipArch]
nickname = ms6_rh_cruiser
loadout = rh_grp_cruiser
level = d25
ship_archetype = rh_cruiser
pilot = cruiser_default
state_graph = CRUISER
npc_class = lawful, CRUISER, d22

[NPCShipArch]
nickname = ms6_or_elite_ship
loadout = ms6_cloak_co_elite2
level = d20
ship_archetype = or_elite
pilot = mod_fighter_version_a
state_graph = FIGHTER
npc_class = unlawful, class_fighter,  d20

[NPCShipArch]
nickname = ms6_osiris
loadout = li_battleship_02_cloak
level = d20
ship_archetype = or_osiris
pilot = li_battleship_02
state_graph = CRUISER
npc_class = lawful, CRUISER

[NPCShipArch]
nickname = ms6_no_fighter
loadout = ms6_no_fighter
level = d10
ship_archetype = no_fighter
pilot = mod_fighter_version_a
state_graph = FIGHTER
npc_class = lawful, FIGHTER

'''


class Misson06(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m06/m06.ini'
    FOLDER = 'M06'
    FILE = 'm06'
    START_SAVE_ID = 32700
    STATIC_NPCSHIPS = NPCSHIPS
    SCRIPT_INDEX = 6
    DIRECT_SYSTEMS = [S.li_mnh, S.sphere, S.co_cad]

    def get_save_states(self):
        return [
            SaveState(self, 'patrols', 'Подлёт к Сфере'),
            SaveState(self, 'first_tunnel', 'Сфера. После первого шлюза'),
            SaveState(self, 'nomad_zone', 'Сфера. Зона с Номадами'),
            SaveState(self, 'the_core', 'Ядро Сферы'),
            SaveState(self, 'lab', 'Лаборатория'),
        ]

    def get_dialogs(self):
        return [
            TextDialog(
                self, 'mount', 'Установка устройства невидимости',
                ru_content=MultiText([
                    'Хетчер выдала вам устройство невидимости. Вы должны установить его на место вашей контрмеры',

                    'Если вы вылетите без установленного устройства невидимости, то миссия будет проиграна.',
                ]),
            ),
            TextDialog(
                self, 'stealth', 'Устройство невидимости',
                ru_content=MultiText([
                    'Устройство невидимости активировано. Вы ни в коем случае не должны его выключать до определенного момента, '
                    'иначе миссий будет проиграна.',
                ]),
            ),
            TextDialog(
                self, 'patrols', 'Патрули',
                ru_content=MultiText([
                    'Вы входите в зону патрулей, которые могут вас обнаружить. Внимательно следите за передвижением вражеских грузовиков. '
                    'Это единственные корабли, которые могут вас обнаружить. В случае приближения грузовика будет активирована сигнальная система.',

                    'Доклад анатиликов про зону с патрулями:',

                    'По периметру базы размещены телескопы. Находясь в подпространстве вы все еще можете наносить физические повреждения. Если ударить телескоп, можно '
                    'отвлечь вражеский патруль и тем самым спокойно влететь в Сферу.',

                    'Загрузить стратегию в нейросеть?'
                ]),
                dialog_type=DIALOG_YES_NO,
            ),
            TextDialog(
                self, 'nomad_zone', 'Зона с номадами',
                ru_content=MultiText([
                    'Вам потребуется выключить невидимость, чтобы вступить в схватку. Комбинация по умолчанию: Ctrl+W',
                    'Эту комбинацию можно изменить в настройках: для этого нужно заменить ВТОРУЮ '
                    'кнопку для события МАГН. ЛУЧ (все) / НЕВИДИМОСТЬ. Комбинация должна содержать Ctrl.',

                    'Доклад аналитиков про зону с кочевниками:',

                    'Снизу есть отверстие к энергетической комнате. Если сломать генератор, то произойдёт экстренный '
                    'выброс энергии, который сможет уничтожить или хотя бы повредить номадское зерно.',

                    'Загрузить стратегию в нейросеть?'
                ]),
                dialog_type=DIALOG_YES_NO,
            ),
            TextDialog(
                self, 'the_core', 'Ядро Сферы',
                ru_content=MultiText([
                    'Вы приближаетесь к ядру. Данные о количестве рейнландских ученых в ядре неизвестно. '
                    'Вы в любом случае не должны дать никому покинуть ядро, иначе миссия будет проиграна.',

                    'Доклад аналитиков про ядро Сферы:',

                    'В районе ядра расположены небольше лаборатории, на которых может укрыться Роттерман. Рекомендуется '
                    'предварительно взломать и заблокировать их двери. Сенсоры кораблей ученых достаточно слабые, поэтому '
                    'вы можете спокойно лететь вдали от них при этом не будучи замеченным. На ближне аванпосте есть датчики слежения, '
                    'поэтому вы должны взломать его последним, так как будет немедленно обнаружены.',

                    'Загрузить стратегию в нейросеть?',
                ]),
                dialog_type=DIALOG_YES_NO,
            ),
            TextDialog(
                self, 'hacking', 'Взлом',
                ru_content=MultiText([
                    'Чтобы взломать панель, вы должны уничтожить все блоки нужного цвета.',
                    'Стреляйте по разным блокам в поисках искомого цвета. Разные блоки выдают разные звуки, '
                    'в зависимости от дальности до искомого цвета: '
                    'Максимальное, Очень высокое, Высокое, Средне, Низкое, Очень низкое, Минимальное.',
                    'Найдите цвет, который будет обозначен как "максимальное" и уничтожьте все блоки с этим цветом.',
                ]),
            ),
            TextDialog(
                self, 'torpedo', 'Торпеды',
                ru_content=MultiText([
                    'Вражеские корабли атакуют Миссури тяжелыми торпедами',
                    'Вы должны уничтожить эти торпеды своими пушками. Можно так же использовать любые ракеты. '
                    'В том числе и ракеты, сбивающие круиз. Торпеды могут об них сдетонировать.',
                    'Не пытайтесь сбить торпеды своим щитом. Вы будете мгновенно уничтожены!'
                ]),
            ),
        ]

    def get_real_objects(self):
        return {
            'vendor_planet': Obj(self, li_mnh.ManhMiningDockring),
        }

    def get_nn_objectives(self):
        return [
            NNObj(self, 'Встретьтесь с Хечтер в баре планеты Форбс', name='00_meet_vendor', target='vendor_planet'),
            NNObj(self, O.LAUNCH, name='00_launch_to_space'),
            NNObj(self, 'Направляйтесь к Миссури', name='01_goto_dread', target='dread_mnh1'),
            NNObj(self, 'Подберите указанное устройство', name='02_pick_up_cloaking_device'),
            NNObj(self, 'Установите устройство невидимости и взлетите', name='03_mount_cloaking_device_and_launch'),
            NNObj(self, O.GOTO, name='04_road_to_station', target='04_road_to_station'),
            NNObj(self, O.GOTO, name='04_road_to_station02', target='04_road_to_station02'),

            NNObj(self, O.GOTO, name='T_goto_telescope01',
                  target='telescope01', nag=False),
            NNObj(self, 'Совершите физический удар по телескопу, не выходя из невидимости',
                  name='T_hit_telescope01',
                  target='telescope01', nag=False),
            NNObj(self, O.GOTO, name='T_go_to_upper_wp01', target='t_go_to_upper_wp01', nag=False),
            NNObj(self, O.GOTO, name='T_go_to_tunnel_wp01', target='t_go_to_tunnel_wp01', nag=False),

            NNObj(self, 'Доберитесь до рейнландской станции',
                  name='05_around_station', target='05_around_station', nag=False),
            NNObj(self, 'Проникните внутрь Сферы', name='06_enter_the_sphere', target='06_enter_the_sphere', nag=False),

            NNObj(self, 'Доберитесь до шлюза', name='07_goto_first_tunnel_enter_point', target='07_goto_first_tunnel_enter_point'),

            NNObj(self, 'Пролетите через шлюз', name='07_meet_alaric_after_first_tunnel', target='07_meet_alaric_after_first_tunnel'),

            NNObj(self, 'Направляйтесь к следующему шлюзу', name='08_goto_second_tunnel', target='08_goto_second_tunnel'),

            NNObj(self, O.GOTO, name='08_goto_second_tunnel_wp01', target='08_goto_second_tunnel_wp01'),
            NNObj(self, O.GOTO, name='08_goto_second_tunnel_wp02', target='08_goto_second_tunnel_wp02'),
            NNObj(self, O.GOTO, name='08_goto_second_tunnel_wp03', target='08_goto_second_tunnel_wp03'),
            NNObj(self, O.GOTO, name='08_goto_second_tunnel_wp04', target='08_goto_second_tunnel_wp04'),
            NNObj(self, O.GOTO, name='08_goto_second_tunnel_wp05', target='08_goto_second_tunnel_wp05'),

            NNObj(self, 'Пролетите через второй шлюз', name='09_enter_the_second_tunnel', target='09_enter_the_second_tunnel'),
            NNObj(self, 'Направляйтесь к шлюзу', name='09_enter_the_second_tunnel_wp01', target='09_enter_the_second_tunnel_wp01'),
            NNObj(self, 'Пролетите через шлюз', name='09_enter_the_second_tunnel_wp02', target='09_enter_the_second_tunnel_wp02'),

            NNObj(self, 'Направляйтесь к следующему шлюзу', name='10_goto_third_tunnel', target='10_goto_third_tunnel'),
            NNObj(self, O.GOTO, name='10_goto_third_tunnel_wp01', target='10_goto_third_tunnel_wp01'),
            NNObj(self, O.GOTO, name='10_goto_third_tunnel_wp02', target='10_goto_third_tunnel_wp02'),
            NNObj(self, O.GOTO, name='10_goto_third_tunnel_wp03', target='10_goto_third_tunnel_wp03'),
            NNObj(self, O.GOTO, name='10_goto_third_tunnel_wp04', target='10_goto_third_tunnel_wp04'),

            NNObj(self, O.GOTO, name='NZ_goto_bottom_side', target='nz_goto_bottom_side', nag=False),
            NNObj(self, O.GOTO, name='NZ_goto_bottom_box', target='nz_goto_bottom_box', nag=False),
            NNObj(self, 'Уничтожьте указанный объект', name='NZ_destroy_kernel_deactivator',
                  target='sphere_kernel_deactivator', nag=False),
            NNObj(self, 'Срочно вылетите из текущей локации', name='NZ_leave_from_bottom_box', target='nz_leave_from_bottom_box', nag=False),
            NNObj(self, 'Выйдите из зоны поражения лазера', name='NZ_go_away_from_lazerburn', target='nz_go_away_from_lazerburn', nag=False),

            NNObj(self, 'Уничтожьте номадское зерно', name='11_destroy_nomad_core',
                  target='sphere_kernel'),
            NNObj(self, 'Уничтожьте номадские истребители', name='12_destroy_nomad_fighters'),

            NNObj(self, 'Проникните в ядро Сферы', name='13_goto_sphere_core', target='13_goto_sphere_core'),

            NNObj(self, 'Направляйтесь к шлюзу', name='13_goto_nomad_area_exit', target='13_goto_nomad_area_exit'),
            NNObj(self, 'Пролетите через шлюз', name='13_enter_the_last_tunnel', target='13_enter_the_last_tunnel'),
            NNObj(self, 'Направляйтесь к ядру Сферы', name='13_fly_to_core', target='13_fly_to_core'),
            NNObj(self, 'Направляйтесь к шлюзу', name='13_goto_the_core_last_tunnel', target='13_goto_the_core_last_tunnel', nag=False),
            NNObj(self, 'Проникните в ядро Сферы', name='13_enter_the_core', target='13_enter_the_core', nag=False),

            NNObj(self, O.GOTO, name='13_second_way_wp01', target='13_second_way_wp01'),

            NNObj(self, O.GOTO, name='TC_alt_way_wp01', target='tc_alt_way_wp01', nag=False),
            NNObj(self, O.GOTO, name='TC_alt_way_wp02', target='tc_alt_way_wp02', nag=False),
            NNObj(self, O.GOTO, name='TC_alt_way_wp03', target='tc_alt_way_wp03', nag=False),
            NNObj(self, 'Взломайте двери базы', name='TC_alt_way_destroy_scienthome_control_panel',
                  target='tc_alt_way_destroy_scienthome_control_panel', nag=False),

            NNObj(self, O.GOTO, name='TC_alt_way_wp04', target='tc_alt_way_wp04', nag=False),
            NNObj(self, O.GOTO, name='TC_alt_way_wp05', target='tc_alt_way_wp05', nag=False),
            NNObj(self, O.GOTO, name='TC_alt_way_wp06', target='tc_alt_way_wp06', nag=False),
            NNObj(self, 'Взломайте двери базы', name='TC_alt_way_destroy_outpost_control_panel',
                  target='tc_alt_way_destroy_outpost_control_panel', nag=False),
            NNObj(self, O.GOTO, name='TC_alt_way_wp07', target='tc_alt_way_wp07', nag=False),
            NNObj(self, O.GOTO, name='TC_alt_way_wp08', target='tc_alt_way_wp08', nag=False),

            NNObj(self, 'Направляйтесь к Роттерману', name='13_goto_reitherman', target='13_goto_reitherman', nag=False),
            NNObj(self, 'Убейте Роттермана', name='14_kill_reitherman'),
            NNObj(self, 'Поймайте и убейте ассистента', name='15_catch_and_kill_assistant'),
            NNObj(self, 'Направляйтесь к шлюзу', name='16_back_to_second_tunnel', target='16_back_to_second_tunnel', nag=False),

            NNObj(self, O.GOTO, name='16_enter_backroad_tunnel', target='16_enter_backroad_tunnel', nag=False),
            NNObj(self, O.GOTO, name='16_leave_the_core_by_backroad_tunnel', target='16_leave_the_core_by_backroad_tunnel', nag=False),
            NNObj(self, O.GOTO, name='16_leave_the_core_by_huge_tunnel', target='16_leave_the_core_by_huge_tunnel', nag=False),
            NNObj(self, O.GOTO, name='16_goto_last_tunnel_wp01', target='16_goto_last_tunnel_wp01', nag=False),
            NNObj(self, 'Направляйтесь к шлюзу', name='16_goto_last_tunnel_exit', target='16_goto_last_tunnel_exit', nag=False),
            NNObj(self, 'Пролетите через шлюз', name='16_exit_last_tunel', target='16_exit_last_tunel', nag=False),

            NNObj(self, 'Направляйтесь к лаборатории', name='17_goto_lab', target='sphere_laboratory01'),
            NNObj(self, 'Уничтожьте генераторы щита лаборатории', name='18_destroy_lab_shield'),
            NNObj(self, 'Совершите стыковку с лабораторией', name='19_dock_on_lab', target='sphere_laboratory01'),
            NNObj(self, 'Покиньте Сферу', name='20_back_to_first_tunnel', target='20_back_to_first_tunnel'),

            NNObj(self, O.GOTO, name='20_back_to_exit_wp01', target='20_back_to_exit_wp01'),
            NNObj(self, 'Направляйтесь к шлюзу', name='20_back_to_exit_wp02', target='20_back_to_exit_wp02'),
            NNObj(self, 'Пролетите через шлюз', name='20_back_to_exit_airlock01', target='20_back_to_exit_airlock01'),
            NNObj(self, O.GOTO, name='20_back_to_exit_wp03', target='20_back_to_exit_wp03'),

            NNObj(self, 'Сядьте на Миссури', name='21_dock_on_dread',
                  target='dread_escape'),
            NNObj(self, 'Направляйтесь к месту сражения', name='22_destroy_torpedoes_look_at',
                  target='22_destroy_torpedoes_look_at'),
            NNObj(self, 'Уничтожьте торпеды', name='22_destroy_torpedoes'),
            NNObj(self, 'Направлятесь к гипердыре в Большой Омикрон', name='23_goto_omicron_major_jumphole',
                  target='sphere_to_omicron1B', towards=True),
            NNObj(self, 'Используйте гипердыру в Большой Омикрон', name='24_jump_to_omicron_major',
                  target='sphere_to_omicron1B'),
            NNObj(self, 'Направляйтесь к фрипорту Тринидат', name='25_goto_tobago_base',
                  target='co_cad_03', towards=True),
            NNObj(self, 'Сядьте на фрипорт Тринидат', name='26_dock_on_tobago_base',
                  target='co_cad_03'),
        ]

    def get_static_points(self):
        defined_points = []

        defined_points.extend([
            DockableBattleshipSolar(
                self, S.li_mnh, 'dread_mnh1', faction='li_grp',
                archetype='l_dreadnought', loadout='li_dreadnought_03',
                ru_name='Линкор Миссури', base='sphere_01_base',
                labels=['friend', 'asf', 'dread']
            ),
            DockableBattleshipSolar(
                self, S.sphere, 'dread_init', faction='li_grp',
                archetype='l_dreadnought', loadout='li_dreadnought_03',
                ru_name='Линкор Миссури', base='sphere_01_base',
                labels=['friend', 'asf', 'dread']
            ),
            DockableBattleshipSolar(
                self, S.sphere, 'dread_escape', faction='li_grp',
                archetype='l_dreadnought', loadout='li_dreadnought_03',
                ru_name='Линкор Миссури', base='sphere_01_base',
                labels=['friend', 'asf', 'dread']
            ),
            DockableBattleshipSolar(
                self, S.sphere, 'dread_defend1', faction='li_grp',
                archetype='l_dreadnought_destroyable', loadout='li_dreadnought_03',
                ru_name='Линкор Миссури', base='sphere_02_base',
                labels=['friend', 'asf', 'dread']
            ),
            Solar(self, S.sphere, 'sphere_laboratory01', faction='li_grp', ru_name='Лаборатория',),
            StaticJumpgate(self, S.sphere, 'sphere_to_omicron1B', ru_name='Гиперврата в Большой Омикрон'),
            Solar(self, S.co_cad, 'co_cad_03', ru_name='Фрипорт Тринидат'),
        ])

        telescopes = [
            'telescope01',
            'telescope02',
            'telescope03',
            'telescope04',
        ]
        tele_sols = []
        for tele in telescopes:
            tele_sol = Solar(
                self, S.sphere, tele,
                ru_name='Телескоп',
                archetype='telescope_msn',
                loadout='telescope',
                labels=['telescopes'],
            )
            defined_points.append(tele_sol)
            tele_sols.append(tele_sol)

        self.add_solar_group('TELESCOPE', tele_sols)

        nomad_zone_solars = [
            Solar(
                self, S.sphere, 'sphere_kernel', faction='fc_n_grp',
                archetype='nomad_kernel', loadout='sphere_kernel_light',
                ru_name='Номадское зерно',
            ),
            Solar(
                self, S.sphere, 'sphere_kernel_deactivator', faction='fc_n_grp',
                archetype='msn6_nomad_area_generator', loadout='space_arch_generator',
                ru_name='Генератор', labels=['nomad_area_gen'],
            ),
            Solar(
                self, S.sphere, 'sphere_kernel_lazerburner', faction='fc_n_grp',
                archetype='space_hidden_root', loadout='nomad_sphere_run_laser',
                ru_name='Излучатель',
            ),
            Solar(
                self, S.sphere, 'sphere_kernel_bottom_lockeddoor',
                archetype='lair_locked_door',
                ru_name='Дверь',
            ),
        ]

        defined_points.extend(nomad_zone_solars)
        self.add_solar_group('NOMAD_ZONE', nomad_zone_solars)

        lab_solars = [
            Solar(
                self, S.sphere, 'sphere_laboratory01', faction='rh_grp',
                archetype='space_port_dmg', loadout='lab01_loadout_wo_shield',
                ru_name='Лаборатория', base='sphere_99_base'
            ),
            Solar(
                self, S.sphere, 'lab_shield01', faction='rh_grp',
                    archetype='space_shieldgen_destroyable', loadout='lab01_shielgen_turrets',
                ru_name='Генератор щита', labels=['lab_shield'],
            ),
            Solar(
                self, S.sphere, 'lab_shield02', faction='rh_grp',
                archetype='space_shieldgen_destroyable', loadout='lab01_shielgen_turrets',
                ru_name='Генератор щита', labels=['lab_shield'],
            ),
        ]

        defined_points.extend(lab_solars)
        self.add_solar_group('LAB', lab_solars)

        core_solars = [
            Solar(self, S.sphere, 'sphere_depot_01', faction='rh_grp',
                  ru_name='Блокпост', archetype='space_police01_front_dock', base='sphere_91_base'),
            Solar(self, S.sphere, 'sphere_depot_02', faction='rh_grp',
                  ru_name='Склад', archetype='space_police01', base='sphere_92_base'),

            Solar(self, S.sphere, 'sphere_depot_01_hacker_layer_1', ru_name='Взлом', archetype='m06_hacker_02_layer_01'),
            Solar(self, S.sphere, 'sphere_depot_01_hacker_layer_2', ru_name='Взлом', archetype='m06_hacker_02_layer_02'),
            Solar(self, S.sphere, 'sphere_depot_01_hacker_layer_3', ru_name='Взлом', archetype='m06_hacker_02_layer_03'),
            Solar(self, S.sphere, 'sphere_depot_01_hacker_layer_valid', ru_name='Взлом', archetype='m06_hacker_02_valid'),

            Solar(self, S.sphere, 'sphere_depot_02_hacker_layer_1', ru_name='Взлом', archetype='m06_hacker_01_layer_01'),
            Solar(self, S.sphere, 'sphere_depot_02_hacker_layer_2', ru_name='Взлом', archetype='m06_hacker_01_layer_02'),
            Solar(self, S.sphere, 'sphere_depot_02_hacker_layer_3', ru_name='Взлом', archetype='m06_hacker_01_layer_03'),
            Solar(self, S.sphere, 'sphere_depot_02_hacker_layer_valid', ru_name='Взлом', archetype='m06_hacker_01_valid'),
        ]
        defined_points.extend(core_solars)
        self.add_solar_group('THE_CORE', core_solars)

        sphere_points = [
            '04_road_to_station',
            '04_road_to_station02',
            't_go_to_upper_wp01',
            't_go_to_tunnel_wp01',
            '05_around_station',
            '06_enter_the_sphere',
            '07_goto_first_tunnel_enter_point',
            '07_meet_alaric_after_first_tunnel',
            '08_goto_second_tunnel',
            '08_goto_second_tunnel_wp01',
            '08_goto_second_tunnel_wp02',
            '08_goto_second_tunnel_wp03',
            '08_goto_second_tunnel_wp04',
            '08_goto_second_tunnel_wp05',
            '09_enter_the_second_tunnel',
            '09_enter_the_second_tunnel_wp01',
            '09_enter_the_second_tunnel_wp02',
            '10_goto_third_tunnel',
            '10_goto_third_tunnel_wp01',
            '10_goto_third_tunnel_wp02',
            '10_goto_third_tunnel_wp03',
            '10_goto_third_tunnel_wp04',
            'nz_goto_bottom_side',
            'nz_goto_bottom_box',
            'nz_leave_from_bottom_box',
            'nz_go_away_from_lazerburn',
            '13_goto_sphere_core',
            '13_goto_nomad_area_exit',
            '13_enter_the_last_tunnel',
            '13_fly_to_core',
            '13_goto_the_core_last_tunnel',
            '13_enter_the_core',
            '13_second_way_wp01',
            'tc_alt_way_wp01',
            'tc_alt_way_wp02',
            'tc_alt_way_wp03',
            'tc_alt_way_destroy_scienthome_control_panel',
            'tc_alt_way_wp04',
            'tc_alt_way_wp05',
            'tc_alt_way_wp06',
            'tc_alt_way_destroy_outpost_control_panel',
            'tc_alt_way_wp07',
            'tc_alt_way_wp08',
            '13_goto_reitherman',
            '16_back_to_second_tunnel',
            '16_enter_backroad_tunnel',
            '16_leave_the_core_by_backroad_tunnel',
            '16_leave_the_core_by_huge_tunnel',
            '16_goto_last_tunnel_wp01',
            '16_goto_last_tunnel_exit',
            '16_exit_last_tunel',
            '20_back_to_first_tunnel',
            '20_back_to_exit_wp01',
            '20_back_to_exit_wp02',
            '20_back_to_exit_airlock01',
            '20_back_to_exit_wp03',
            '22_destroy_torpedoes_look_at',
        ]

        for p in sphere_points:
            defined_points.append(
                Point(self, S.sphere, p)
            )

        return defined_points

    def get_capital_ships(self):
        rcr = {
            'npc_ship_arch': 'ms6_rh_cruiser',
            'faction': 'rh_grp',
            'labels': ['rh_cruiser'],
            'ru_name': N.RH_CRUISER,
        }

        caps = []
        out_caps = []

        out_cr_count = 2

        for index in range(1, out_cr_count+1):
            cap = f'patrol_cruiser_{index}'
            the_cap = Capital(self, cap, **rcr)
            caps.append(the_cap)
            out_caps.append(the_cap)

        self.add_capital_group('ENTER_CAP', out_caps)

        torp_gb = {
            'npc_ship_arch': 'ms6_rh_gunship',
            'faction': 'rh_grp',
            'labels': ['torpedo'],
            'ru_name': N.RH_GUNBOAT,
        }

        torp_caps = []

        torp_gb_count = 3

        for index in range(1, torp_gb_count+1):
            cap = f'torpedo_gunboat_{index}'
            the_cap = Capital(self, cap, **torp_gb)
            caps.append(the_cap)
            torp_caps.append(the_cap)

        self.add_capital_group('TORP_GB', torp_caps)

        return caps

    def get_ships(self):
        return [
            Ship(
                self,
                'hatcher',
                hero=True,
                actor=actors.Hatcher,
                labels=[
                    'friend',
                ],
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.DefenderJuni,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=5),
                    animated_wings=True,
                )
            ),
            Ship(
                self,
                'alaric',
                hero=True,
                actor=actors.Alaric,
                labels=[
                    'friend',
                ],
                npc=NPC(
                    faction=faction.LibertyHunters,
                    ship=ship.Hammerhead,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=5),
                )
            ),
            Ship(
                self,
                'alaric_cloak',
                hero=True,
                actor=actors.Alaric,
                labels=[
                    'friend',
                ],
                npc=NPC(
                    faction=faction.LibertyHunters,
                    ship=ship.Hammerhead,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=5),
                    extra_equip=[
                        'equip = cloak_fast, HpCM01, 1',
                    ],
                    # TODO: Disable CMs
                )
            ),
            Ship(
                self,
                'patrol_freighter',
                count=5,
                labels=[
                    'patrol',
                    'cloak_checker',
                ],
                affiliation=faction.RheinlandMain.CODE,
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Humpback,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=4),
                )
            ),
            Ship(
                self,
                'patrol_fighter',
                count=10,
                labels=[
                    'patrol',
                ],
                affiliation=faction.RheinlandMain.CODE,
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=4),
                )
            ),
            Ship(
                self,
                'no_fighter',
                count=25,
                affiliation=faction.Nomad.CODE,
                system_class=S.sphere,
                labels=['enemy', 'nomad'],
                static_npc_shiparch='ms6_no_fighter'
            ),
            Ship(
                self,
                'reitherman',
                actor=actors.Reitherman,
                labels=[
                    'enemy',
                ],
                affiliation=faction.RheinlandMain.CODE,
                npc=NPC(
                    faction=faction.RheinlandCivilians,
                    ship=ship.CSV,
                    level=NPC.D6,
                    equip_map=EqMap(base_level=3),
                )
            ),
            Ship(
                self,
                'runner',
                actor=actors.FinnRunner,
                labels=[
                    'enemy',
                ],
                arrival_obj='sphere_depot_01',
                npc=NPC(
                    faction=faction.RheinlandCivilians,
                    ship=ship.Humpback,
                    level=NPC.D6,
                    equip_map=EqMap(base_level=3),
                    # TODO: Disable CMs
                )
            ),
            Ship(
                self,
                'lab_defend',
                count=2,
                labels=[
                    'lab_ship',
                ],
                system_class=S.sphere,
                slide_x=200,
                affiliation=faction.RheinlandMain.CODE,
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Banshee,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=4),
                )
            ),
            Ship(
                self,
                'lab_reinforcement',
                count=3,
                labels=[
                    'lab_ship',
                ],
                system_class=S.sphere,
                slide_x=200,
                affiliation=faction.RheinlandMain.CODE,
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Banshee,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=4),
                )
            ),
            Ship(
                self,
                'lab_patrol',
                count=2,
                labels=[
                    'lab_patrol',
                ],
                affiliation=faction.RheinlandMain.CODE,
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Banshee,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=4),
                )
            ),
            Ship(
                self,
                'exit_sphere_li_fighter',
                count=5,
                labels=[
                    'li_bg_fighter',
                    'liberty',
                    'background',
                ],
                system_class=S.sphere,
                slide_x=300,
                affiliation=faction.LibertyMain.CODE,
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Defender,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=4),
                )
            ),
            Ship(
                self,
                'exit_sphere_rh_fighter',
                count=5,
                labels=[
                    'rh_bg_fighter',
                    'rheinland',
                    'background',
                ],
                system_class=S.sphere,
                slide_x=300,
                affiliation=faction.RheinlandMain.CODE,
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=4),
                )
            ),

            Ship(
                self,
                'li_elite',
                count=15,
                labels=[
                    'liberty',
                ],
                affiliation=faction.LibertyMain.CODE,
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Defender,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=4),
                )
            ),
            Ship(
                self,
                'li_fighter',
                count=5,
                labels=[
                    'liberty',
                ],
                affiliation=faction.LibertyMain.CODE,
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Patriot,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=4),
                )
            ),
            Ship(
                self,
                'rh_elite',
                count=15,
                labels=[
                    'rheinland',
                    'defend_fight_enemy',
                ],
                affiliation=faction.RheinlandMain.CODE,
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=4),
                )
            ),
            Ship(
                self,
                'rh_fighter',
                count=5,
                labels=[
                    'rheinland',
                    'defend_fight_enemy',
                ],
                affiliation=faction.RheinlandMain.CODE,
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Banshee,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=4),
                )
            ),
            Ship(
                self,
                'rh_elite_reinforcement',
                count=5,
                labels=[
                    'rheinland',
                ],
                relative_pos=True,
                relative_range=1500,
                affiliation=faction.RheinlandMain.CODE,
                npc=NPC(
                    faction=faction.RheinlandMain,
                    ship=ship.Valkyrie,
                    level=NPC.D8,
                    equip_map=EqMap(base_level=4),
                )
            ),

            Ship(
                self,
                'li_delta',
                count=4,
                labels=[
                    'liberty',
                ],
                relative_pos=True,
                relative_range=2000,
                jumper=False,
                base_name='Дельта',
                affiliation=faction.LibertyMain.CODE,
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Defender,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=5),
                )
            ),

        ]
