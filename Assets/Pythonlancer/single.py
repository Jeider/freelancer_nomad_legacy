import sys
import os
from time import sleep
import pathlib

from text.dividers import DIVIDER, SINGLE_DIVIDER

from core import get_core

from files.writer import FileWriter

from managers.script import ScriptManager

from templates.jinja_manager import JinjaTemplateManager

from story.cutscenes.meta import LipSyncManager

from universe.audio.manager import PilotManager
from universe.audio import pilot
from universe.audio import dispatcher
from universe.audio import nnvoice
from universe.audio import mission_comission

from universe.content import mineable

from templates.hardcoded_inis.audio import VoicesSpaceMaleTemplate, VoicesSpaceFemaleTemplate
from templates.hardcoded_inis.missions import VoicePropertiesTemplate

from tools import merge_image
from tools import data_folder
from tools import elevenlabs
from tools import audio_folder
from tools import maxlancer
from tools.audio_pilot import TempPilot, VanillaPilot

from story import actors

from tools.system_template import SystemTemplateLoader

from templates.solar import hacker_panel
from templates.dockable import terraforming
from templates.dockable import valensia
from templates.dockable import upsilon_gasinside
from templates.dockable import tunnel
from templates.misc import rmbase
from templates.misc import trading
from templates.dockable import nomad_asf_hq
from templates.dockable import order_shipyard

from templates.dockable import m13


def draw_base():
    new_name = None
    move_to = None
    workspace = '1'

    # base_class = m13.RockfordGenerator
    # new_name = 'or_hq_vienna_entry'
    # move_to = (13900, 0, 32400)
    #
    # base_class = trading.XenosOutpostPanels
    # new_name = 'xenos_control01'
    # move_to = (-2000, 0, -10000)
    #
    # base_class = order_shipyard.OrderShipyard
    # new_name = 'or_hq_shipyard_01'
    # move_to = (-20000, 0, 0)

    # base_class = ast_om15_xxxlarge.AsteroidOne
    # new_name = 'communicator'
    # move_to = (-9500, 0, -10000)

    base_class = nomad_asf_hq.AsfHQ
    the_base = base_class()

    content = the_base.get_instance(new_space_object_name=new_name, move_to=move_to)
    data_folder.DataFolder.sync_to_test_workspace(content, workspace_index=workspace)


def draw_base_for_hardpoints():
    new_name = None
    move_to = None
    workspace = '0'

    # base_class = m13.RockfordGenerator
    # new_name = 'or_hq_vienna_entry'
    # move_to = (13900, 0, 32400)

    base_class = terraforming.TerraformingTwo
    # new_name = 'or_hq_vienna_entry'
    the_base = base_class()

    the_base.get_instance(new_space_object_name=new_name, move_to=move_to)
    the_base.parse_segments()
    # print(the_base.get_segments_as_hardpoints_xml())
    print(the_base.get_segments_as_loadout(warning=True))
    # print(the_base.get_instance_from_segments())


def generate_hacker_panels():
    hacker_panel.HackerPanelManager().write_content()


def compile_audio():
    audio_folder.AudioFolder.compile_xml_to_utf()
    print('done')


def compile_pilots_ini():
    PilotManager.compile_pilots_ini()


def compile_pilots_audio():
    PilotManager.compile_pilots_audio()


def test_hacker_colors():
    x = hacker_panel.HackerPanelManager()

    x1 = x.get_random_hacker_panel()
    x2 = x1.get_space_content('sphere_depot_02_hacker', 'rh_grp', (-960, 17, 7000), hacker_panel.REL_TOP, 'sphere_success')
    print(x2)
    pass


def dump_system():
    system_template = SystemTemplateLoader.get_template('sphere')
    points = system_template.dump_points()
    for point in points:
        print(point)


def dump_story_system():
    current_path = pathlib.Path().resolve()
    path = current_path.parent.parent / 'DATA' / 'UNIVERSE' / 'SPECIAL' / 'SPHERE'
    system_template = SystemTemplateLoader.get_template('sphere_dev', source_path=path)
    points = system_template.dump_points()
    for point in points:
        print(f"'{point}',")


def build_image():
    merge_image.build_image()


def get_frames():
    results = merge_image.get_frames()
    for item in results:
        print(item)


def get_frames_ints():
    results = merge_image.get_frames_ints()
    for item in results:
        print(item)


def test_story():
    jinja = JinjaTemplateManager()
    tpl = 'missions/m01/m01a.ini'

    x = jinja.get_result(tpl, {})
    FileWriter.write('missions/m01a.ini', x)
    print('done')


def generate_script():
    ScriptManager().generate_script()
    # FileWriter.write('mission9.html', mission9.Mission9().get_story_script())
    # FileWriter.write('mission10.html', mission10.Mission10().get_story_script())
    # FileWriter.write('mission11.html', mission11.Mission11().get_story_script())
    # FileWriter.write('mission12.html', mission12.Mission12().get_story_script())
    # FileWriter.write('mission13.html', mission13.Mission13().get_story_script())
    # print(content)


# def parse_voices():
#     lines = []
#     for item in CONTENT.splitlines():
#         if item.startswith('msg'):
#             parts = item.split(' = ')
#             lines.append(parts[1])
#             print(f"'{parts[1]}',")



def test_voices():
    props = VanillaPilot.parse_vanilla_voice_props()
    return


def test_steos():
    # SteosVoice.prepare_temp_path()


    #
    # PilotManager.prepare_pilots_audio()
    #
    # return

    the_pilot = nnvoice.NNVoice()

    TempPilot.prepare_temp_folders(the_pilot)
    TempPilot.fill_audio(the_pilot, skip=True)

    TempPilot.fill_files_for_xml(the_pilot)
    TempPilot.build_voice_xml(the_pilot)



    # the_pilot = nnvoice.NNVoice()
    #
    # TempPilot.prepare_temp_folders(the_pilot)
    # TempPilot.fill_audio(the_pilot, skip=True)
    #
    # TempPilot.fill_files_for_xml(the_pilot)
    # TempPilot.build_voice_xml(the_pilot)



    return

    lines = pilot.get_number_lines()

    # for line in lines:
    #     SteosVoice.generate_temp_sound(
    #         actor=line.get_actor(steos_id=pilot.STEOS_ID),
    #         text=line.get_temp_text(),
    #         name=line.get_code(),
    #     )
    #     sleep(0.2)
    #
    # return

    for line in lines:
        line.process_temp()
    



    return


def generate_story_voices():
    script_manager = ScriptManager()
    # import pdb;pdb.set_trace()

    msn = script_manager.get_mission_by_index(9)
    for voice in msn.get_voices():
        audio_folder.AudioFolder.compile_story_voice_to_xml(voice)


def test_interaction():
    i = input('Wait for you action').strip().lower()
    if i == 's':
        print('saved!')
    elif i == 'x':
        print('ignored')
    else:
        print('unknown action')

    i = input('Next action').strip().lower()


def test_elevenlabs():
    result = elevenlabs.ElevenLabs.get_line('Это Рэйнланд, омега один слеш один. Я направляюсь к станции Потсдам. Скоро буду.')
    import pdb;pdb.set_trace()


class MySupriseField(mineable.DefaultField):
    BOX_SIZE = 1800
    DENSITY_MULTIPLER = 3
    DRIFT_X = 0.8
    DRIFT_Y = 1
    DRIFT_Z = 0.8
    EMPTY_CHANCE = 0
    # ROTATE_X_MIN = -180
    # ROTATE_X_MAX = 180
    # ROTATE_Y_MIN = -180
    # ROTATE_Y_MAX = 180
    # ROTATE_Z_MIN = -180
    # ROTATE_Z_MAX = 180


class MyField(mineable.StaticObjectField):
    ALIAS = 'bh_hazard_field'
    INDEX = 1
    STATIC_ARCHETYPES = [
        'bh_hazard',
    ]
    FIELD_CLASS = MySupriseField
    REWARDS_GROUP_CLASS = mineable.DefaultSupriseRewardsGroup
    ULTRA_REWARD = False


def generate_field():
    core = get_core()
    the_sys = core.universe.universe_root.get_all_system_by_name('bh')

    field = MyField(system=the_sys)
    content = field.get_system_content()
    print(content)


def generate_points():
    points = {
        'kernel2_ast1_in': '-7870, -538, -7906',
        'kernel2_ast1_wall1': '-7215, -167, -7573',
        'kernel2_ast1_wall2': '-6523, 276, -7479',
        'kernel2_ast1_end': '-6494, 115, -6336',
        'kernel2_ast2_in': '-4879, -235, -3877',
        'kernel2_ast2_mid1': '-3504, -246, -3033',
        'kernel2_ast2_end': '-2189, 70, -3062',
        'kernel2_ast3_in': '155, 62, -3307',
        'kernel2_ast3_mid1': '1490, -235, -3543',
        'kernel2_ast3_exit': '2968, -198, -2996',
        'kernel2_ast4_in': '3895, 527, -1377',
        'kernel2_ast4_split': '4903, 699, -683',
        'kernel2_ast4_mid1': '5770, 942, -1275',
        'kernel2_ast4_exit': '6710, 806, -1666',
        'kernel2_ast5_in': '8758, 511, -2579',
        'kernel2_ast5_wall1': '9376, 494, -2650',
        'kernel2_ast5_core': '9838, 446, -3017',
        'kernel2_ast5_wall2': '10265, 275, -3544',
        'kernel2_ast5_exit': '10614, 125, -3856',
    }

    data = []

    for name, pos in points.items():
        data.append(
            f'''[Object]
nickname = {name}
pos = {pos}
rotate = 0, 0, 0
archetype = nav_buoy
'''
        )

    names_list = [f"'{name}'," for name in points.keys()]
    names_combined = SINGLE_DIVIDER.join(names_list)

    targets_list = [
        f"NNObj(self, O.GOTO, target='{name}', reach_range=500),"
        for name in points.keys()
    ]
    targets_combined = SINGLE_DIVIDER.join(targets_list)

    nav_list = [
        f"{{{{ nn_{name}.reach() }}}}"
        for name in points.keys()
    ]
    nav_combined = SINGLE_DIVIDER.join(nav_list)


    data_combined = SINGLE_DIVIDER.join(data)

    print(nav_combined)


def generate_cutscene_voices():
    script_manager = ScriptManager()
    # import pdb;pdb.set_trace()

    msn = script_manager.get_mission_by_index(12)

    for cutscene in msn.get_cutscenes():
        audio_folder.AudioFolder.generate_cutscene_sounds(cutscene)


def meta():
    tpl_manager = JinjaTemplateManager()
    script_manager = ScriptManager()
    meta_manager = LipSyncManager(tpl_manager=tpl_manager)

    msn = script_manager.get_mission_by_index(12)

    # meta_manager.edit_cutscene(msn, 'sprague')
    meta_manager.edit_sound_from_scene(msn, 'sprague', 160)

    print('meta done')


def scene():
    tpl_manager = JinjaTemplateManager()
    script_manager = ScriptManager()
    msn = script_manager.get_mission_by_index(12)
    cutscene = msn.get_cutscene_by_code('sprague')
    cutscene.get_thorn(tpl_manager).sync_content()
    # cutscene.get_decision_thorn(tpl_manager).sync_content()
    # cutscene.get_accept_thorn(tpl_manager).sync_content()

    print('scene done')


def dbg():
    pass


ACTIONS = {
    'generate_hacker_panels': generate_hacker_panels,
    'compile_audio': compile_audio,
    'test_hacker_colors': test_hacker_colors,
    'draw_base': draw_base,
    'draw_base_for_hardpoints': draw_base_for_hardpoints,
    'build_image': build_image,
    'get_frames': get_frames,
    'get_frames_ints': get_frames_ints,
    'test_story': test_story,
    'generate_script': generate_script,
    'test_voices': test_voices,
    'test_steos': test_steos,
    'test_interaction': test_interaction,
    'test_elevenlabs': test_elevenlabs,
    'dump_system': dump_system,
    'dump_story_system': dump_story_system,
    'compile_pilots_ini': compile_pilots_ini,
    'compile_pilots_audio': compile_pilots_audio,
    'generate_story_voices': generate_story_voices,
    'generate_cutscene_voices': generate_cutscene_voices,
    'generate_field': generate_field,
    'generate_points': generate_points,
    'meta': meta,
    'scene': scene,
    'dbg': dbg,
}


def single(action):
    action_function = ACTIONS.get(action, None)
    if action_function is None:
        raise Exception('Unknown action')

    action_function()

try:
    action = sys.argv[1]
except IndexError:
    raise Exception('Action argument is required')

single(action)

