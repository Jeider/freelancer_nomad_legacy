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
    MultiText, MultiLine, TextDialog, Direct, Trigger, DRY_RUN, DIALOG_YES_NO
)
from story.ingame.ingame_thorn import IngameThorn, GENERIC_TWO_POINT, GENERIC_MOUNTED_ROTATABLE

from world.npc import NPC, EqMap
from world import ship
from universe import faction

from text.strings import MultiString as MS

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
pilot = mod_fighter_universe
state_graph = FIGHTER
npc_class = lawful, fighter_ace

'''


class Misson06(ingame_mission.IngameMission):
    JINJA_TEMPLATE = 'missions/m06/m06.ini'
    FOLDER = 'M06'
    FILE = 'm06'
    START_SAVE_ID = 32600
    START_SAVE_RU_NAME = MS('Нью-Йорк, Планета Питтсбург', 'New York, Planet Pittsburgh')
    STATIC_NPCSHIPS = NPCSHIPS
    SCRIPT_INDEX = 6
    DIRECT_SYSTEMS = [S.li_mnh, S.sphere, S.co_cad]
    RTC = ['vendor_msn']
    INIT_OFFER = MultiLine(
        [
            'ЗАДАЧА:',
            'Приостановить рейландские исследования на режимном объекте.',
            '',
            'СЛОЖНОСТЬ:',
            'Рискованная.',
            '',
            'НАГРАДА:',
            '250 000 кредитов.',
        ],
        [
            'OBJECTIVE:',
            'Stop Rheinland research at a sensitive site.',
            '',
            'DIFFICULTY:',
            'Risky.',
            '',
            'REWARD:',
            '250 000 credits.',
        ]
    ).get_content()

    def get_save_states(self):
        return [
            SaveState(self, 'patrols', MS('Подлёт к Сфере', 'Near The Sphere')),
            SaveState(self, 'first_tunnel', MS('Сфера. После первого шлюза', 'The Sphere. After first airlock')),
            SaveState(self, 'nomad_zone', MS('Сфера. Зона с Номадами', 'The Sphere. Nomad Zone')),
            SaveState(self, 'the_core', MS('Ядро Сферы', "The Sphere's core")),
            SaveState(self, 'lab', MS('Лаборатория', 'Laboratory')),
        ]

    def get_dialogs(self):
        return [
            TextDialog(
                self, 'mount', MS('Установка устройства невидимости', 'Mount cloaking device'),
                ru_content=MultiText([
                    'Хетчер выдала вам устройство невидимости. Вы должны установить его на место вашей контрмеры.',

                    'Если вы вылетите без установленного устройства невидимости, то миссия будет проиграна.',
                ],
                [
                    'You got cloaking device from Hatcher. You must mount it on your ship on Countermeasure mount point.'
                    
                    'Mission will failed when you\'ll try launch without mounted cloaking device',
                ]

                ),
            ),
            TextDialog(
                self, 'stealth', MS('Устройство невидимости', 'Cloaking device'),
                ru_content=MultiText([
                    'Устройство невидимости активировано. Вы ни в коем случае не должны его выключать до определенного момента, '
                    'иначе миссий будет проиграна.',
                ],
                [
                    'Cloaking device is active. You should deactivate it ONLY by mission objective or mission will be failed',
                ]),
            ),
            TextDialog(
                self, 'patrols', MS('Патрули', 'Patrols'),
                ru_content=MultiText([
                    'Вы входите в зону патрулей, которые могут вас обнаружить. Внимательно следите за передвижением вражеских грузовиков. '
                    'Это единственные корабли, которые могут вас обнаружить. В случае приближения грузовика будет активирована сигнальная система.',

                    'Доклад анатиликов про зону с патрулями:',

                    'По периметру базы размещены телескопы. Находясь в подпространстве вы все еще можете наносить физические повреждения. Если ударить телескоп, можно '
                    'отвлечь вражеский патруль и тем самым спокойно влететь в Сферу.',

                    'Загрузить стратегию в нейросеть?'
                ],[
                    'You are entering patrol zone. This patrols can detect. You must carefully look at enemy freighters. '
                    "It's only ships that can detect you. Special alert will be activated when freighter is too near to you."

                    "Analytics' report about patrol zone: ",

                    "There placed some telescope. You can hit on them by your ship (your ship have physical appearance). "
                    "This action can distract enemy patrol and you can enter The Sphere without problems",

                    "Load this strategy in your NeuralNet?"
                ]),
                dialog_type=DIALOG_YES_NO,
            ),
            TextDialog(
                self, 'nomad_zone', MS('Зона с номадами', 'Nomad Zone'),
                ru_content=MultiText([
                    'Вам потребуется выключить невидимость, чтобы вступить в схватку. Комбинация по умолчанию: Ctrl+W',
                    'Эту комбинацию можно изменить в настройках: для этого нужно заменить ВТОРУЮ '
                    'кнопку для события МАГН. ЛУЧ (все) / НЕВИДИМОСТЬ. Комбинация должна содержать Ctrl.',

                    'Доклад аналитиков про зону с кочевниками:',

                    'Снизу есть отверстие к энергетической комнате. Если сломать генератор, то произойдёт экстренный '
                    'выброс энергии, который сможет уничтожить или хотя бы повредить номадское зерно. Важно: эта энергия может '
                    'повредить в том числе и ваш корабль, вы должны покинуть энергетическую комнату и уклониться от '
                    'энергетического луча.',

                    'Загрузить стратегию в нейросеть?'
                ],[
                    "Now you must deactivate your invisibility. Default keyboard combination: Ctrl+W",
                    "You can change it combination by settings. You need to change SECOND button for action "
                    "Tractor beam (all) / Invisibility. Combination must contain Ctrl button.",

                    "Analytics' report about Nomad Zone:",

                    "This zone have tunnel at the bottom side. This is tunnel to energy room. You can broke power generator "
                    "and extract danger energy beam. This beam can damage nomad kernel and nomad fighters. But be warned - this power beam "
                    "can destroy your ship, you must leave this chamber soon as possible.",

                    "Load this strategy in your NeuralNet?"
                ]),
                dialog_type=DIALOG_YES_NO,
            ),
            TextDialog(
                self, 'the_core', MS('Ядро Сферы', "The Sphere's core"),
                ru_content=MultiText([
                    'Вы приближаетесь к ядру. Данные о количестве рейнландских ученых в ядре неизвестно. '
                    'Вы в любом случае не должны дать никому покинуть ядро, иначе миссия будет проиграна.',

                    'Если вы не справляетесь с миссией, то с помощью лончера может переключить сложность на лёгкую. Тогда ваши цели будут менее стремительно покидать Сферу, когда вас обнаружат.',

                    'Доклад аналитиков про ядро Сферы:',

                    'В районе ядра расположены небольшие базы, на которых может укрыться Роттерман, а так же на них могут находиться ассистенты профессора, которые '
                    'могут вызвать сигнал о подмоге. Ваша задача - или уничтожить Роттермана вручную, а потом перехватить ассистента. Или вы можете '
                    'заблокировать двери баз, чтобы ни Роттерман ни ассистенты не могли вылететь. При этом Роттерман в любом случае попытается покинуть '

                    'В районе ядра расположены небольше лаборатории, на которых может укрыться Роттерман. Рекомендуется '
                    'предварительно взломать и заблокировать их двери. Сенсоры кораблей ученых достаточно слабые, поэтому '
                    'вы можете спокойно лететь вдали от них при этом не будучи замеченным. На ближнем аванпосте есть датчики слежения, '
                    'поэтому вы должны взломать его последним, так как будет немедленно обнаружены. После этого вы должны незамедлительно атаковать '
                    'Роттермана',

                    'Загрузить стратегию в нейросеть?',
                ],[
                    'You are near the core. The is no known data about amount of rheinland scients inside sphere. '
                    'You should no one left the core alive. In other case mission will be failed.',

                    "If you can't handle this mission: you always can switch difficulty to easy by launcher. Then your targets will be less likely to flee the Sphere rapidly when you are discovered.",

                    "Analytics's report about the core:",

                    "Near the core area there are small laboratories where Rottman may be hiding. "
                    "It is recommended to first hack and lock their doors. The sensors on the scientists' "
                    "ships are quite weak, so you can safely fly at a distance from them without being detected. "
                    "The nearest outpost has tracking sensors, so you should hack it last, as you will be immediately "
                    "detected. After that, you must immediately attack Rottman.",
                    
                    "Load this strategy in your NeuralNet?"
                ]),
                dialog_type=DIALOG_YES_NO,
            ),
            TextDialog(
                self, 'hacking', MS('Взлом', 'Hacking'),
                ru_content=MultiText([
                    'Чтобы взломать панель, вы должны уничтожить все блоки нужного цвета.',
                    'Стреляйте по разным блокам в поисках искомого цвета. Разные блоки выдают разные звуки '
                    'в зависимости от дальности до искомого цвета: '
                    'Максимальное, Очень высокое, Высокое, Средне, Низкое, Очень низкое, Минимальное.',
                    'Найдите цвет, который будет обозначен как "максимальное" и уничтожьте все блоки с этим цветом.',
                ],[
                    'To hack this panel you must fire on blocks with correct colors. ',
                    'Fire different blocks by your guns. Those blocks will activate sounds of this color. '
                    'Different blocks produce different sounds depending on the distance to the desired color:'
                    "Maximal, Very high, High, Medium. Low, Very low, Minimal.",
                    'Find the color with sound "maximal" and destroy blocks with such color',
                ]),
            ),
            TextDialog(
                self, 'torpedo', MS('Торпеды', 'Torpedoes'),
                ru_content=MultiText([
                    'Вражеские корабли атакуют Миссури тяжелыми торпедами',
                    'Вы должны уничтожить эти торпеды своими пушками. Можно так же использовать любые ракеты. '
                    'В том числе и ракеты, сбивающие круиз. Торпеды могут об них сдетонировать.',
                    'Не пытайтесь сбить торпеды своим щитом. Вы будете мгновенно уничтожены!'
                ],[
                    'Enemy ships attack Missouri with heavy torpedoes',
                    'You must attack torpedoes by your guns. You also can use any missiles. '
                    'Also you can use CD missiles. '
                    'Torpedoes can detonate by any missile.',
                    'Do not try to detonate torpedoes by your shield. You will be immediately destroyed!'
                ]),
            ),
        ]

    def get_real_objects(self):
        return {
            'vendor_planet': Obj(self, li_mnh.ManhMiningDockring),
        }

    def get_nn_objectives(self):
        return [
            NNObj(self, MS('Встретьтесь с Хечтер в баре планеты Питтсбург', 'Meet Hatcher in bar of Planet Pittsburgh'), name='00_meet_vendor', target='vendor_planet'),
            NNObj(self, O.LAUNCH, name='00_launch_to_space'),
            NNObj(self, MS('Направляйтесь к Миссури', 'Go to Missouri'), name='01_goto_dread', target='dread_mnh1', towards=True),
            NNObj(self, MS('Подберите указанное устройство', 'Collect cloaking device'), name='02_pick_up_cloaking_device'),
            NNObj(self, MS('Установите устройство невидимости и взлетите', 'Mount cloaking device and launch'), name='03_mount_cloaking_device_and_launch'),
            NNObj(self, O.GOTO, name='04_road_to_station', target='04_road_to_station', nag=False),
            NNObj(self, O.GOTO, name='04_road_to_station02', target='04_road_to_station02', nag=False),

            NNObj(self, O.GOTO, name='T_goto_telescope01',
                  target='telescope01', nag=False),
            NNObj(self, MS('Совершите физический удар по телескопу, не выходя из невидимости', 'Make physical hit on telescope without exiting out of invisibility mode'),
                  name='T_hit_telescope01',
                  target='telescope01', nag=False),
            NNObj(self, O.GOTO, name='T_go_to_upper_wp01', target='t_go_to_upper_wp01', nag=False),
            NNObj(self, O.GOTO, name='T_go_to_tunnel_wp01', target='t_go_to_tunnel_wp01', nag=False),

            NNObj(self, MS('Доберитесь до рейнландской станции', 'Reach rheinland station'),
                  name='05_around_station', target='05_around_station', nag=False),
            NNObj(self, MS('Проникните внутрь Сферы', 'Enter into The Sphere'), name='06_enter_the_sphere', target='06_enter_the_sphere', nag=False),

            NNObj(self, MS('Доберитесь до шлюза', 'Reach airlock'), name='07_goto_first_tunnel_enter_point', target='07_goto_first_tunnel_enter_point', nag=False),

            NNObj(self, MS('Пролетите через шлюз', 'Fly through airlock'), name='07_meet_alaric_after_first_tunnel', target='07_meet_alaric_after_first_tunnel', nag=False),

            NNObj(self, MS('Направляйтесь к следующему шлюзу', 'Go to next airlock'), name='08_goto_second_tunnel', target='08_goto_second_tunnel', nag=False),

            NNObj(self, O.GOTO, name='08_goto_second_tunnel_wp01', target='08_goto_second_tunnel_wp01', nag=False),
            NNObj(self, O.GOTO, name='08_goto_second_tunnel_wp02', target='08_goto_second_tunnel_wp02', nag=False),
            NNObj(self, O.GOTO, name='08_goto_second_tunnel_wp03', target='08_goto_second_tunnel_wp03', nag=False),
            NNObj(self, O.GOTO, name='08_goto_second_tunnel_wp04', target='08_goto_second_tunnel_wp04', nag=False),
            NNObj(self, O.GOTO, name='08_goto_second_tunnel_wp05', target='08_goto_second_tunnel_wp05', nag=False),

            NNObj(self, MS('Пролетите через второй шлюз', 'Fly through second airlock'), name='09_enter_the_second_tunnel', target='09_enter_the_second_tunnel', nag=False),
            NNObj(self, MS('Направляйтесь к шлюзу', 'Go to airlock'), name='09_enter_the_second_tunnel_wp01', target='09_enter_the_second_tunnel_wp01', nag=False),
            NNObj(self, MS('Пролетите через шлюз', 'Fly through airlock'), name='09_enter_the_second_tunnel_wp02', target='09_enter_the_second_tunnel_wp02', nag=False),

            NNObj(self, MS('Направляйтесь к следующему шлюзу', 'Go to next airlock'), name='10_goto_third_tunnel', target='10_goto_third_tunnel', nag=False),
            NNObj(self, O.GOTO, name='10_goto_third_tunnel_wp01', target='10_goto_third_tunnel_wp01', nag=False),
            NNObj(self, O.GOTO, name='10_goto_third_tunnel_wp02', target='10_goto_third_tunnel_wp02', nag=False),
            NNObj(self, O.GOTO, name='10_goto_third_tunnel_wp03', target='10_goto_third_tunnel_wp03', nag=False),
            NNObj(self, O.GOTO, name='10_goto_third_tunnel_wp04', target='10_goto_third_tunnel_wp04', nag=False),

            NNObj(self, O.GOTO, name='NZ_goto_bottom_side', target='nz_goto_bottom_side', nag=False),
            NNObj(self, O.GOTO, name='NZ_goto_bottom_box', target='nz_goto_bottom_box', nag=False),
            NNObj(self, MS('Уничтожьте указанный объект', 'Destroy marked object'), name='NZ_destroy_kernel_deactivator',
                  target='sphere_kernel_deactivator', nag=False),
            NNObj(self, MS('Срочно вылетите из текущей локации', 'Leave this area!'), name='NZ_leave_from_bottom_box', target='nz_leave_from_bottom_box', nag=False),
            NNObj(self, MS('Выйдите из зоны поражения лазера', 'Leave laser damage zone!'), name='NZ_go_away_from_lazerburn', target='nz_go_away_from_lazerburn', nag=False),

            NNObj(self, MS('Уничтожьте номадское зерно', 'Destroy nomad kernel'), name='11_destroy_nomad_core',
                  target='sphere_kernel', nag=False),
            NNObj(self, MS('Уничтожьте номадские истребители', "Destroy nomad fighters"), name='12_destroy_nomad_fighters', nag=False),

            NNObj(self, MS('Проникните в ядро Сферы', 'Enter the core'), name='13_goto_sphere_core', target='13_goto_sphere_core', nag=False),

            NNObj(self, MS('Направляйтесь к шлюзу', 'Go to airlock'), name='13_goto_nomad_area_exit', target='13_goto_nomad_area_exit', nag=False),
            NNObj(self, MS('Пролетите через шлюз', 'Fly through airlock'), name='13_enter_the_last_tunnel', target='13_enter_the_last_tunnel', nag=False),
            NNObj(self, MS('Направляйтесь к ядру Сферы', "Go to the Sphere's core"), name='13_fly_to_core', target='13_fly_to_core', nag=False),
            NNObj(self, MS('Направляйтесь к шлюзу', 'Go to airlock'), name='13_goto_the_core_last_tunnel', target='13_goto_the_core_last_tunnel', nag=False),
            NNObj(self, MS('Проникните в ядро Сферы', "Ehter the core"), name='13_enter_the_core', target='13_enter_the_core', nag=False),

            NNObj(self, O.GOTO, name='13_second_way_wp01', target='13_second_way_wp01', nag=False),

            NNObj(self, O.GOTO, name='TC_alt_way_wp01', target='tc_alt_way_wp01', nag=False),
            NNObj(self, O.GOTO, name='TC_alt_way_wp02', target='tc_alt_way_wp02', nag=False),
            NNObj(self, O.GOTO, name='TC_alt_way_wp03', target='tc_alt_way_wp03', nag=False),
            NNObj(self, MS('Взломайте двери базы', 'Hack station doors'), name='TC_alt_way_destroy_scienthome_control_panel',
                  target='tc_alt_way_destroy_scienthome_control_panel', nag=False),

            NNObj(self, O.GOTO, name='TC_alt_way_wp04', target='tc_alt_way_wp04', nag=False),
            NNObj(self, O.GOTO, name='TC_alt_way_wp05', target='tc_alt_way_wp05', nag=False),
            NNObj(self, O.GOTO, name='TC_alt_way_wp06', target='tc_alt_way_wp06', nag=False),
            NNObj(self, MS('Взломайте двери базы', 'Hack station doors'), name='TC_alt_way_destroy_outpost_control_panel',
                  target='tc_alt_way_destroy_outpost_control_panel', nag=False),
            NNObj(self, O.GOTO, name='TC_alt_way_wp07', target='tc_alt_way_wp07', nag=False),
            NNObj(self, O.GOTO, name='TC_alt_way_wp08', target='tc_alt_way_wp08', nag=False),

            NNObj(self, MS('Направляйтесь к Роттерману', 'Go to Reithreman'), name='13_goto_reitherman', target='13_goto_reitherman', nag=False),
            NNObj(self, MS('Убейте Роттермана', 'Kill Reitherman'), name='14_kill_reitherman'),
            NNObj(self, MS('Поймайте и убейте ассистента', 'Catch and kill Assistant'), name='15_catch_and_kill_assistant'),
            NNObj(self, MS('Направляйтесь к шлюзу', 'Go to airlock'), name='16_back_to_second_tunnel', target='16_back_to_second_tunnel', nag=False),

            NNObj(self, O.GOTO, name='16_enter_backroad_tunnel', target='16_enter_backroad_tunnel', nag=False),
            NNObj(self, O.GOTO, name='16_leave_the_core_by_backroad_tunnel', target='16_leave_the_core_by_backroad_tunnel', nag=False),
            NNObj(self, O.GOTO, name='16_leave_the_core_by_huge_tunnel', target='16_leave_the_core_by_huge_tunnel', nag=False),
            NNObj(self, O.GOTO, name='16_goto_last_tunnel_wp01', target='16_goto_last_tunnel_wp01', nag=False),
            NNObj(self, MS('Направляйтесь к шлюзу', 'Go to airlock'), name='16_goto_last_tunnel_exit', target='16_goto_last_tunnel_exit', nag=False),
            NNObj(self, MS('Пролетите через шлюз', 'Fly through airlock'), name='16_exit_last_tunel', target='16_exit_last_tunel', nag=False),

            NNObj(self, MS('Направляйтесь к лаборатории', 'Go to laboratory'), name='17_goto_lab', target='sphere_laboratory01'),
            NNObj(self, MS('Уничтожьте генераторы щита лаборатории', "Destroy laboratory shield generators"), name='18_destroy_lab_shield'),
            NNObj(self, MS('Совершите стыковку с лабораторией', 'Dock with laboratory'), name='19_dock_on_lab', target='sphere_laboratory01'),
            NNObj(self, MS('Покиньте Сферу', 'Leave The Sphere'), name='20_back_to_first_tunnel', target='20_back_to_first_tunnel'),

            NNObj(self, O.GOTO, name='20_back_to_exit_wp01', target='20_back_to_exit_wp01'),
            NNObj(self, MS('Направляйтесь к шлюзу', 'Go to airlock'), name='20_back_to_exit_wp02', target='20_back_to_exit_wp02'),
            NNObj(self, MS('Пролетите через шлюз', 'Fly through airlock'), name='20_back_to_exit_airlock01', target='20_back_to_exit_airlock01'),
            NNObj(self, O.GOTO, name='20_back_to_exit_wp03', target='20_back_to_exit_wp03'),

            NNObj(self, MS('Сядьте на Миссури', "Dock with Missouri"), name='21_dock_on_dread',
                  target='dread_escape'),
            NNObj(self, MS('Направляйтесь к месту сражения', 'Go to battle zone'), name='22_destroy_torpedoes_look_at',
                  target='22_destroy_torpedoes_look_at'),
            NNObj(self, MS('Уничтожьте торпеды', "Destroy torpedoes"), name='22_destroy_torpedoes'),
            NNObj(self, MS('Направлятесь к гипердыре в Большой Омикрон', 'Go to jumphole to Omicron Major'), name='23_goto_omicron_major_jumphole',
                  target='sphere_to_omicron1B', towards=True),
            NNObj(self, MS('Используйте гипердыру в Большой Омикрон', 'Use jumphole to Omicron Major'), name='24_jump_to_omicron_major',
                  target='sphere_to_omicron1B'),
            NNObj(self, MS('Направляйтесь к фрипорту Тринидат', 'Go to freeport Trinidad'), name='25_goto_tobago_base',
                  target='co_cad_03', towards=True),
            NNObj(self, MS('Сядьте на фрипорт Тринидат', 'Dock with freeport Trinidad'), name='26_dock_on_tobago_base',
                  target='co_cad_03'),
        ]

    def get_static_points(self):
        defined_points = []

        missouri_name = MS('Линкор Миссури', 'Battleship Missouri')

        defined_points.extend([
            DockableBattleshipSolar(
                self, S.li_mnh, 'dread_mnh1', faction='li_grp',
                archetype='l_dreadnought', loadout='li_dreadnought_03',
                ru_name=missouri_name, base='sphere_01_base',
                labels=['friend', 'asf', 'dread']
            ),
            DockableBattleshipSolar(
                self, S.sphere, 'dread_init', faction='li_grp',
                archetype='l_dreadnought', loadout='li_dreadnought_03',
                ru_name=missouri_name, base='sphere_01_base',
                labels=['friend', 'asf', 'dread']
            ),
            DockableBattleshipSolar(
                self, S.sphere, 'dread_escape', faction='li_grp',
                archetype='l_dreadnought', loadout='li_dreadnought_03',
                ru_name=missouri_name, base='sphere_01_base',
                labels=['friend', 'asf', 'dread']
            ),
            DockableBattleshipSolar(
                self, S.sphere, 'dread_defend1', faction='li_grp',
                archetype='l_dreadnought_destroyable', loadout='li_dreadnought_03',
                ru_name=missouri_name, base='sphere_02_base',
                labels=['friend', 'asf', 'dread']
            ),
            Solar(self, S.sphere, 'sphere_laboratory01', faction='li_grp', ru_name=MS('Лаборатория', 'Laboratory'),),
            StaticJumpgate(self, S.sphere, 'sphere_to_omicron1B', ru_name=MS('Гипердыра в Большой Омикрон', 'Jumphole to Omicron Major')),
            Solar(self, S.co_cad, 'co_cad_03', ru_name=MS('Фрипорт Тринидат', 'Freeport Trinidad')),
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
                ru_name=MS('Телескоп', 'Telescope'),
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
                ru_name=MS('Номадское зерно', 'Nomad Kernel'), labels=['nomad', 'enemy']
            ),
            Solar(
                self, S.sphere, 'sphere_kernel_deactivator', faction='fc_n_grp',
                archetype='msn6_nomad_area_generator', loadout='space_arch_generator',
                ru_name=MS('Генератор', "Generator"), labels=['nomad_area_gen'],
            ),
            Solar(
                self, S.sphere, 'sphere_kernel_lazerburner',
                archetype='space_hidden_root', loadout='nomad_sphere_run_laser',
                ru_name=MS('Излучатель', 'Emitter'),
            ),
            Solar(
                self, S.sphere, 'sphere_kernel_bottom_lockeddoor',
                archetype='lair_locked_door',
                ru_name=MS('Дверь', 'Door'),
            ),
        ]

        defined_points.extend(nomad_zone_solars)
        self.add_solar_group('NOMAD_ZONE', nomad_zone_solars)

        lab_solars = [
            Solar(
                self, S.sphere, 'sphere_laboratory01', faction='rh_grp',
                archetype='space_port_dmg', loadout='lab01_loadout_wo_shield',
                ru_name=MS('Лаборатория', "Laboratory"), base='sphere_99_base'
            ),
            Solar(
                self, S.sphere, 'lab_shield01', faction='rh_grp',
                    archetype='space_shieldgen_destroyable', loadout='lab01_shielgen_turrets',
                ru_name=MS('Генератор щита', 'Shield generator'), labels=['lab_shield'],
            ),
            Solar(
                self, S.sphere, 'lab_shield02', faction='rh_grp',
                archetype='space_shieldgen_destroyable', loadout='lab01_shielgen_turrets',
                ru_name=MS('Генератор щита', 'Shield generator'), labels=['lab_shield'],
            ),
        ]

        defined_points.extend(lab_solars)
        self.add_solar_group('LAB', lab_solars)

        hack = MS('Взлом', 'hack')

        core_solars = [
            Solar(self, S.sphere, 'sphere_depot_01', faction='rh_grp',
                  ru_name=MS('Блокпост', 'Outpost'), archetype='space_police01_front_dock', base='sphere_91_base'),
            Solar(self, S.sphere, 'sphere_depot_02', faction='rh_grp',
                  ru_name=MS('Склад', "Storage"), archetype='space_police01', base='sphere_92_base'),

            Solar(self, S.sphere, 'sphere_depot_01_hacker_layer_1', ru_name=hack, archetype='m06_hacker_02_layer_01'),
            Solar(self, S.sphere, 'sphere_depot_01_hacker_layer_2', ru_name=hack, archetype='m06_hacker_02_layer_02'),
            Solar(self, S.sphere, 'sphere_depot_01_hacker_layer_3', ru_name=hack, archetype='m06_hacker_02_layer_03'),
            Solar(self, S.sphere, 'sphere_depot_01_hacker_layer_valid', ru_name=hack, archetype='m06_hacker_02_valid'),

            Solar(self, S.sphere, 'sphere_depot_02_hacker_layer_1', ru_name=hack, archetype='m06_hacker_01_layer_01'),
            Solar(self, S.sphere, 'sphere_depot_02_hacker_layer_2', ru_name=hack, archetype='m06_hacker_01_layer_02'),
            Solar(self, S.sphere, 'sphere_depot_02_hacker_layer_3', ru_name=hack, archetype='m06_hacker_01_layer_03'),
            Solar(self, S.sphere, 'sphere_depot_02_hacker_layer_valid', ru_name=hack, archetype='m06_hacker_01_valid'),
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
                    'li_bg_fighter',
                    'liberty',
                    'background',
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
                jumper=True,
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
                radius=0,
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
                    level=NPC.D12,
                    equip_map=EqMap(base_level=5),
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
                base_name=MS('Дельта', 'Delta'),
                affiliation=faction.LibertyMain.CODE,
                npc=NPC(
                    faction=faction.LibertyMain,
                    ship=ship.Defender,
                    level=NPC.D10,
                    equip_map=EqMap(base_level=5),
                )
            ),

        ]
