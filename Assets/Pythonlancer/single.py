import sys
import os
from time import sleep

from files.writer import FileWriter

from managers.script import ScriptManager

from jinja_templates.jinja_manager import JinjaTemplateManager

from universe.audio import space_voice
from universe.audio.pilot import FirstPilot, PirateOne
from universe.audio.mission_comission import MCVoice

from tools import merge_image
from tools import data_folder
from tools import elevenlabs
from tools import audio_folder
from tools import maxlancer
from tools.audio_pilot import TempPilot, VanillaPilot

from story import actors

from tools.system_template import SystemTemplateLoader

from story.cutscenes.mission9.yokohama import Msn9YokohamaCutsceneThorn

from templates.solar.hacker_panel import HackerPanelManager, REL_TOP
from templates.dockable import forbes_megafactory


def test_placement():
    base_class = forbes_megafactory.ForbesMegafactory
    content = base_class().get_instance(new_space_object_name=None, move_to=None)
    data_folder.DataFolder.sync_to_test_workspace(content, workspace_index='')


def generate_hacker_panels():
    HackerPanelManager().write_content()


def compile_audio():
    audio_folder.AudioFolder.compile_xml_to_utf()
    print('done')


def test_hacker_colors():
    x = HackerPanelManager()

    x1 = x.get_random_hacker_panel()
    x2 = x1.get_space_content('om15_hacker01', 'rh_grp', (25.5, 3122.5, 234234.12), REL_TOP, 'om15_success')
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
    pilot = PirateOne()

    TempPilot.prepare_temp_folders(pilot)
    # TempPilot.fill_audio(pilot, skip=True)

    # TempPilot.fill_files_for_xml(pilot)
    TempPilot.build_voice_xml(pilot)







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
    # text = 'Фрилансер альфа один деш один. Это станция Магдеб+ург. Расскажите цель своей миссии'
    # SteosVoice.generate_test_sound(actors.King, text, 'demo')


def generate_story_voices():
    script_manager = ScriptManager()
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



ACTIONS = {
    'generate_hacker_panels': generate_hacker_panels,
    'compile_audio': compile_audio,
    'test_hacker_colors': test_hacker_colors,
    'test_placement': test_placement,
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

