from audio.mission_audio import MissionAudio
from audio.mission7 import Mission7Audio
from audio.mission8 import Mission8Audio
from audio.actors import Actor

from text.strings import StringCompiler
from text.dividers import DIVIDER


class AudioManager(object):

    def __init__(self):
        self.ingame_sounds_ini = []
        self.ingame_sounds_xml = []
        self.cutscene_sounds_ini = []
        self.cutscene_sounds_thn = []
        self.ether_comm_ru_strings = {}
        self.ether_comm_mission_texts = []
        self.misc_ru_strings = {}
        self.misc_ru_infocards = {}

        self.male_actors = {}
        self.female_actors = {}

        self.load_game_data()

    def load_game_data(self):
        for actor in Actor.subclasses:
            if actor.is_male():
                self.male_actors[actor.NAME] = actor
            elif actor.is_female():
                self.female_actors[actor.NAME] = actor

        for mission_sound_class in MissionAudio.subclasses:
            mission_sound = mission_sound_class(self.male_actors, self.female_actors)
            self.ingame_sounds_ini.append(mission_sound.get_ini_ingame_voicefile_content())
            self.ingame_sounds_xml.append(mission_sound.get_utf_file_content())
            self.cutscene_sounds_ini.append(mission_sound.get_ini_cutscene_sounds_content())
            self.cutscene_sounds_thn.append(mission_sound.get_thn_cutscene_sounds_content())
            self.ether_comm_ru_strings.update(mission_sound.get_ingame_rus_dialog_strings())
            self.ether_comm_ru_strings.update(mission_sound.get_ingame_rus_history_strings())
            self.ether_comm_mission_texts.append(mission_sound.get_ingame_ether_comms())
            self.misc_ru_strings.update(mission_sound.get_misc_rus_strings())
            self.misc_ru_infocards.update(mission_sound.get_misc_rus_infocards())

    def get_ingame_sounds_ini(self):
        return DIVIDER.join(self.ingame_sounds_ini)

    def get_ingame_sounds_xml(self):
        return DIVIDER.join(self.ingame_sounds_xml)

    def get_cutscene_sounds_ini(self):
        return DIVIDER.join(self.cutscene_sounds_ini)

    def get_cutscene_sounds_thn(self):
        return DIVIDER.join(self.cutscene_sounds_thn)

    def get_ether_comm_ru_strings(self):
        return StringCompiler.compile_names(self.ether_comm_ru_strings)

    def get_ether_comm_mission_texts(self):
        return DIVIDER.join(self.ether_comm_mission_texts)

    def get_misc_ru_strings(self):
        return StringCompiler.compile_names(self.misc_ru_strings)

    def get_misc_ru_infocards(self):
        return StringCompiler.compile_infocards(self.misc_ru_infocards)
