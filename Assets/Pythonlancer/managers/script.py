from files.writer import FileWriter

from story.scripts import mission9, mission10, mission11, mission12, mission13  # Define to load
from story.script import StoryMission, ScriptIndex

from text.dividers import DIVIDER, SINGLE_DIVIDER

SCRIPT_SUBFOLDER = 'script'


class ScriptManager(object):

    def __init__(self):
        self.script_missions_db = {}
        self.script_missions_list = []

        for mission in StoryMission.subclasses:
            msn = mission()
            self.script_missions_db[msn.MISSION_INDEX] = msn
            self.script_missions_list.append(msn)

    def get_mission_by_index(self, index):
        if index not in self.script_missions_db:
            raise Exception('unknown mission index %d' % index)

        return self.script_missions_db[index]

    def get_missions(self):
        return self.script_missions_list

    def generate_script(self):
        index_filename = ScriptIndex.get_index_filename()
        index_content = ScriptIndex.get_index_content(self.script_missions_list)
        FileWriter.write_to_subfolder(SCRIPT_SUBFOLDER, index_filename, index_content)
        for mission in self.script_missions_list:
            FileWriter.write_to_subfolder(
                SCRIPT_SUBFOLDER, mission.get_root_file_link(), mission.get_story_script()
            )
            for actor in mission.actors:
                FileWriter.write_to_subfolder(
                    SCRIPT_SUBFOLDER, mission.get_actor_file_link(actor), mission.get_story_script(actor)
                )
