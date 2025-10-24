import pathlib
from pydub import AudioSegment

LOADOUTS_GEN = 'loadout_gen.ini'



def get_duration_pydub(file_path):
    audio_file = AudioSegment.from_file(file_path)
    duration = audio_file.duration_seconds
    return duration


class AudioWatcher:

    def __init__(self):
        self.root = pathlib.Path().resolve().parent.parent

    def get_root(self):
        return self.root

    def get_data(self):
        return self.get_root() / 'DATA'

    def get_audio(self):
        return self.get_data() / 'AUDIO'

    def get_cutscene_audio_ru(self):
        return self.get_audio() / 'MOD'

    def get_cutscene_audio_en(self):
        return self.get_audio() / 'MOD_ENG'

    def watch_cutscene_audio_duration(self, subfolder, file_path, russian=True):
        root = self.get_cutscene_audio_ru() if russian else self.get_cutscene_audio_en()
        duration = get_duration_pydub(root / subfolder / file_path)
        return duration
