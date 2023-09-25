from audio.mission_audio import MissionAudio
from audio.mission8 import Mission8Audio

from text.dividers import DIVIDER


class AudioManager(object):

    def __init__(self):
        self.ingame_sounds_ini = []
        self.ingame_sounds_xml = []
        self.cutscene_sounds_ini = []
        self.cutscene_sounds_thn = []

        self.male_actors = ['brighton']
        self.female_actors = ['darcy']

        self.load_game_data()

    def load_game_data(self):
        for mission_sound_class in MissionAudio.subclasses:
            mission_sound = mission_sound_class(self.male_actors, self.female_actors)
            self.ingame_sounds_ini.append(mission_sound.get_ini_ingame_voicefile_content())
            self.ingame_sounds_xml.append(mission_sound.get_utf_file_content())
            self.cutscene_sounds_ini.append(mission_sound.get_ini_cutscene_sounds_content())
            self.cutscene_sounds_thn.append(mission_sound.get_thn_cutscene_sounds_content())

    def get_ingame_sounds_ini(self):
        return DIVIDER.join(self.ingame_sounds_ini)

    def get_ingame_sounds_xml(self):
        return DIVIDER.join(self.ingame_sounds_xml)

    def get_cutscene_sounds_ini(self):
        return DIVIDER.join(self.cutscene_sounds_ini)

    def get_cutscene_sounds_thn(self):
        return DIVIDER.join(self.cutscene_sounds_thn)
