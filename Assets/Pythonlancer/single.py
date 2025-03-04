import sys
import os
from time import sleep

from text.dividers import DIVIDER

from core import get_core

from files.writer import FileWriter

from managers.script import ScriptManager

from templates.jinja_manager import JinjaTemplateManager

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

from story.cutscenes.mission9.yokohama import Msn9YokohamaCutsceneThorn

from templates.solar import hacker_panel
from templates.dockable import terraforming
from templates.dockable import valensia
from templates.dockable import upsilon_gasinside
from templates.dockable import tunnel
from templates.misc import rmbase
from templates.misc import trading

from templates.dockable import m13


def draw_base():
    new_name = None
    move_to = None
    workspace = '2'

    # base_class = m13.RockfordGenerator
    # new_name = 'or_hq_vienna_entry'
    # move_to = (13900, 0, 32400)

    base_class = trading.XenosOutpostPanels
    new_name = 'xenos_control01'
    move_to = (-2000, 0, -10000)
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

    base_class = upsilon_gasinside.Vienna
    the_base = base_class()

    the_base.get_instance(new_space_object_name=new_name, move_to=move_to)
    the_base.parse_segments()
    # print(the_base.get_segments_as_hardpoints_xml())
    # print(the_base.get_segments_as_loadout())
    print(the_base.get_instance_from_segments())



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
    x2 = x1.get_space_content('xenos_control_hack', 'or_grp', (-2000, 0, -9920), hacker_panel.REL_FRONT, 'xenos_success')
    print(x2)
    pass


def dump_system():
    system_template = SystemTemplateLoader.get_template('rh_biz')
    points = system_template.dump_points()
    for point in points:
        print(point)


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
    for msn in script_manager.get_missions():
        for voice in msn.get_voices():
            audio_folder.AudioFolder.compile_story_voice_to_xml(voice)


def test_elevenlabs():
    result = elevenlabs.ElevenLabs.get_line('Это Рэйнланд, омега один слеш один. Я направляюсь к станции Потсдам. Скоро буду.')
    import pdb;pdb.set_trace()


def test_lua():
    manager = maxlancer.SceneEntityLoader.get_entity_manager('m9_yokohama')

    scene = Msn9YokohamaCutsceneThorn()

    content = scene.get_content()

    FileWriter.write('m9_yokohama.lua', content)


    import pdb;pdb.set_trace()


class MySupriseField(mineable.DefaultField):
    BOX_SIZE = 800
    DENSITY_MULTIPLER = 6
    DRIFT_X = 0.8
    DRIFT_Y = 0.25
    DRIFT_Z = 0.8
    EMPTY_CHANCE = 0
    ROTATE_X_MIN = -10
    ROTATE_X_MAX = 10
    ROTATE_Y_MIN = -180
    ROTATE_Y_MAX = 180
    ROTATE_Z_MIN = -10
    ROTATE_Z_MAX = 10


class MyField(mineable.StaticObjectField):
    ALIAS = 'rs_battle'
    STATIC_ARCHETYPES = [
        'k_battleship',
        'l_dreadnought',
        'b_battleship',
        'o_osiris',
    ]
    FIELD_CLASS = MySupriseField
    REWARDS_GROUP_CLASS = mineable.DefaultSupriseRewardsGroup
    ULTRA_REWARD = False


def generate_field():
    core = get_core()
    asf = core.universe.universe_root.get_all_system_by_name('asf_hq')

    field = MyField(system=asf)
    content = field.get_system_content()
    print(content)




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
    'test_elevenlabs': test_elevenlabs,
    'test_lua': test_lua,
    'dump_system': dump_system,
    'compile_pilots_ini': compile_pilots_ini,
    'compile_pilots_audio': compile_pilots_audio,
    'generate_story_voices': generate_story_voices,
    'generate_field': generate_field,
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

