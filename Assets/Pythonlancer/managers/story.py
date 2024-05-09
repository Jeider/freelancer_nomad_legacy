from jinja_templates.jinja_manager import JinjaTemplateManager

from story.ingame.gameplay.mission1a import Misson01A
from story.ingame.gameplay.mission1b import Misson01B
from files.writer import FileWriter

from tools.data_folder import DataFolder




class StoryManager(object):

    def __init__(self, universe):
        self.universe = universe
        universe_root = self.universe.get_universe_root()

        tpl_manager = JinjaTemplateManager()

        m01a = Misson01A(universe_root)
        m01b = Misson01B(universe_root)

        x = tpl_manager.get_result(m01a.get_template(), m01a.get_context())
        x2 = tpl_manager.get_result(m01b.get_template(), m01b.get_context())

        # import pdb;pdb.set_trace()

        DataFolder.sync_story_mission('M01A', 'm01a', x)
        DataFolder.sync_story_mission('M01B', 'm01b', x2)

        for thorn in m01a.ingame_thorns:
            content = tpl_manager.get_result(thorn.get_template(), thorn.get_context())
            DataFolder.sync_story_ingame_thorn(thorn.get_name(), content)



        # FileWriter.write('missions/m01a.ini', x)

        print('done')
