import sys
import os
from luaparser import ast
from pprint import pprint

from pathlib import Path

from files.writer import FileWriter

from story.scripts import mission9, mission10, mission11, mission12, mission13

from jinja_templates.jinja_manager import JinjaTemplateManager

from universe.content import space_voice

from tools import merge_image
from tools import data_folder
from tools import steos
from tools import elevenlabs
from tools import audio
from tools import maxlancer

from tools.system_template import SystemTemplateLoader

from story.cutscenes.mission9.yokohama import Msn9YokohamaCutsceneThorn

from templates.solar.hacker_panel import HackerPanelManager, REL_TOP
from templates.dockable import upsilon_gasinside
from templates.dockable import station_debris
from templates.dockable import forbes_megafactory
from templates.dockable import sphere_megabase


def test_placement():
    base_class = forbes_megafactory.ForbesMegafactory
    content = base_class().get_instance(new_space_object_name=None, move_to=None)
    data_folder.DataFolder.sync_to_test_workspace(content, workspace_index='')


def generate_hacker_panels():
    HackerPanelManager().write_content()


def compile_story_audio():
    audio.AudioCompiler.compile_story()
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


def test_script():
    FileWriter.write('mission9.html', mission9.Mission9().get_story_script())
    FileWriter.write('mission10.html', mission10.Mission10().get_story_script())
    FileWriter.write('mission11.html', mission11.Mission11().get_story_script())
    FileWriter.write('mission12.html', mission12.Mission12().get_story_script())
    FileWriter.write('mission13.html', mission13.Mission13().get_story_script())
    # print(content)


# def parse_voices():
#     lines = []
#     for item in CONTENT.splitlines():
#         if item.startswith('msg'):
#             parts = item.split(' = ')
#             lines.append(parts[1])
#             print(f"'{parts[1]}',")



def test_voices():
    map = space_voice.ShipVoice.get_id_map()
    for valid, code in map:
        orig = os.path.join('PILOT', f'{code}.wav')
        new = os.path.join('PILOT', f'{valid}.wav')
        try:
            os.rename(orig, new)
        except Exception:
            print(valid)
    # print(lines)



def test_steos():
    result = steos.SteosVoice.get_voices_list()
    import pdb;pdb.set_trace()



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
    'compile_story_audio': compile_story_audio,
    'test_hacker_colors': test_hacker_colors,
    'test_placement': test_placement,
    'build_image': build_image,
    'get_frames': get_frames,
    'get_frames_ints': get_frames_ints,
    'test_story': test_story,
    'test_script': test_script,
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

