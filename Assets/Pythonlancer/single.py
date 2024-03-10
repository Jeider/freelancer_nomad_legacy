import sys

from templates.solar.hacker_panel import HackerPanelManager


def generate_hacker_panels():
    HackerPanelManager().write_content()


def test_hacker_colors():
    pass


ACTIONS = {
    # 'generate_hacker_panels': generate_hacker_panels,
    'test_hacked_colors': test_hacker_colors,
}


def single(action):
    action_function = ACTIONS.get(action)
    if action_function:
        raise Exception('Unknown action')

    action_function()

try:
    action = sys.argv[1]
except IndexError:
    raise Exception('Action argument is required')

single(action)

