from files.writer import FileWriter

from story.scripts import mission9, mission10, mission11, mission12, mission13
from story.script import StoryMission, MissionIndex

from text.dividers import DIVIDER, SINGLE_DIVIDER

SCRIPT_SUBFOLDER = 'script'


class ScriptManager(object):

    def __init__(self):
        self.script_missions = [mission() for mission in StoryMission.subclasses]

        self.generate_script()

    def generate_script(self):
        index_filename = MissionIndex.get_index_filename()
        index_content = MissionIndex.get_index_content(self.script_missions)
        FileWriter.write_to_subfolder(SCRIPT_SUBFOLDER, index_filename, index_content)
        for mission in self.script_missions:
            FileWriter.write_to_subfolder(
                SCRIPT_SUBFOLDER, mission.get_root_file_link(), mission.get_story_script()
            )
            for actor in mission.actors:
                FileWriter.write_to_subfolder(
                    SCRIPT_SUBFOLDER, mission.get_actor_file_link(actor), mission.get_story_script(actor)
                )

