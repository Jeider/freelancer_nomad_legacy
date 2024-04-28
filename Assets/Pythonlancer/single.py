import sys

from files.writer import FileWriter

from story.missions import mission9

from tools import merge_image
from tools import data_folder

from templates.solar.hacker_panel import HackerPanelManager, REL_TOP
from templates.dockable import upsilon_gasinside
from templates.dockable import station_debris
from templates.dockable import forbes_megafactory
from templates.dockable import sphere_megabase


def generate_hacker_panels():
    HackerPanelManager().write_content()


def test_hacker_colors():
    x = HackerPanelManager()

    x1 = x.get_random_hacker_panel()
    x2 = x1.get_space_content('om15_hacker01', 'rh_grp', (25.5, 3122.5, 234234.12), REL_TOP, 'om15_success')
    print(x2)
    pass


def test_placement():
    base_class = forbes_megafactory.ForbesMegafactory
    content = base_class().get_instance(new_space_object_name=None, move_to=None)
    data_folder.DataFolder.sync_to_test_workspace(content, workspace_index='')


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
    msn = mission9.Mission9()
    content = msn.get_story_script()
    FileWriter.write('mission9.html', content)
    print(content)


ACTIONS = {
    'generate_hacker_panels': generate_hacker_panels,
    'test_hacker_colors': test_hacker_colors,
    'test_placement': test_placement,
    'build_image': build_image,
    'get_frames': get_frames,
    'get_frames_ints': get_frames_ints,
    'test_story': test_story,
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

