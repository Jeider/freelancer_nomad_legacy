import sys

from templates.solar.hacker_panel import HackerPanelManager, REL_TOP


def generate_hacker_panels():
    HackerPanelManager().write_content()


def test_hacker_colors():
    x = HackerPanelManager()

    x1 = x.get_random_hacker_panel()
    x2 = x1.get_space_content('om15_hacker01', 'rh_grp', (25.5, 3122.5, 234234.12), REL_TOP, 'om15_success')
    print(x2)
    pass


ACTIONS = {
    'generate_hacker_panels': generate_hacker_panels,
    'test_hacker_colors': test_hacker_colors,
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

