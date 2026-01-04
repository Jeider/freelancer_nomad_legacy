from files.writer import FileWriter

from story.scripts import *
from story.script import StoryMission, ScriptIndex

from tools.data_folder import DataFolder

from text.dividers import DIVIDER, SINGLE_DIVIDER

SCRIPT_SUBFOLDER = 'script'

SUBTITLES_TEMPLATE = '''<?xml version="1.0" encoding="UTF-8"?>

<Subtitles>

{subtitles}

</Subtitles>
'''


class ScriptManager(object):

    def __init__(self, ids=None):
        self.script_missions_db = {}
        self.script_missions_list = []

        for mission in StoryMission.subclasses:
            msn = mission(ids=ids)
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

    def write_script_sounds(self, build_folder, russian):
        data_folder = DataFolder(build_to_folder=build_folder)
        cutscene_sounds_ini_ru = []
        cutscene_sounds_ini_en = []
        subtitles_content = []
        for mission in self.script_missions_list:
            for scene in mission.get_cutscenes():
                for sound in scene.get_sounds():
                    cutscene_sounds_ini_ru.append(sound.get_cutscene_ini())
                    cutscene_sounds_ini_en.append(sound.get_cutscene_ini(russian=False))
                    subtitles_content.append(sound.get_subtitle_content(russian=russian))

            if not mission.SYNC_SPACE:
                raise Exception('SYNC_SPACE obsolete')

            ru_space_voices = mission.get_voices()
            en_space_voices = mission.get_en_voices()

            if russian:
                for voice in ru_space_voices:
                    for sound in voice.get_sounds():
                        if sound.use_in_cinematic():
                            subtitles_content.append(sound.get_subtitle_content(
                                russian=True,
                                root=mission.get_voice_root_for_sound(sound, suffix='')
                            ))
            else:
                for voice in en_space_voices:
                    for sound in voice.get_sounds():
                        if sound.use_in_cinematic():
                            subtitles_content.append(sound.get_subtitle_content(
                                russian=False,
                                root=mission.get_voice_root_for_sound(sound, suffix='_en')
                            ))

            voices = ru_space_voices + en_space_voices
            voice_ini = []

            for voice in voices:
                voice_ini.append(voice.get_ini())

            data_folder.sync_audio_ini(
                f'voices_mission{mission.MISSION_INDEX:02d}',
                DIVIDER.join(voice_ini)
            )

        data_folder.sync_audio_ini(
            'story_sounds_gen_ru',
            DIVIDER.join(cutscene_sounds_ini_ru)
        )

        data_folder.sync_audio_ini(
            'story_sounds_gen_en',
            DIVIDER.join(cutscene_sounds_ini_en)
        )

        data_folder.sync_subtitles(
            SUBTITLES_TEMPLATE.format(subtitles=SINGLE_DIVIDER.join(subtitles_content))
        )
