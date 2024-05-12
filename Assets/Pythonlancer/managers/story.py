from jinja_templates.jinja_manager import JinjaTemplateManager

from story.ingame.gameplay import *
from story.ingame.ingame_mission import IngameMission

from files.writer import FileWriter

from tools.data_folder import DataFolder




class StoryManager(object):

    def __init__(self, universe):
        self.universe = universe
        universe_root = self.universe.get_universe_root()

        tpl_manager = JinjaTemplateManager()

        thorns = []

        for mission_class in IngameMission.subclasses:
            mission = mission_class(universe_root)
            content = tpl_manager.get_result(mission.get_template(), mission.get_context())
            thorns.extend(mission.ingame_thorns)

            DataFolder.sync_story_mission(mission.FOLDER, mission.FILE, content)

        for thorn in thorns:
            content = tpl_manager.get_result(thorn.get_template(), thorn.get_context())
            DataFolder.sync_story_ingame_thorn(thorn.get_name(), content)
