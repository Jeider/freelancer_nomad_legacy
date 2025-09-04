import httpx
import base64
import pathlib

from pathlib import Path

from settings import STEOS_API_KEY

from story.actors import DynamicActor

r'''
Как получить голоса:
https://public.api.voice.steos.io/api/v1/steos-voice-controller/available-voices/<токен>
'''



class SteosVoice(object):

    @staticmethod
    def get_steos_temp_path():
        current_path = pathlib.Path().resolve()
        return current_path / 'results' / 'steos' / 'temp'

    @classmethod
    def generate_voice_bytes(cls, actor, text):
        if not actor.get_steos_id():
            raise Exception('Actor %s have no steos actor id' % actor.NAME)
        if not text or text == '':
            raise Exception('text is mandatory')

        url = f"https://public.api.voice.steos.io/api/v1/synthesize-controller/synthesis-by-text?authToken={STEOS_API_KEY}"

        the_actor = (
            actor
            if type(actor) == DynamicActor
            else actor()
        )

        body = {
            "voiceId": the_actor.get_steos_id(),
            "text": text,
            "pitchShift": the_actor.get_steos_pitch(),
            "speedMultiplier": the_actor.get_steos_speed(),
            "format": "mp3"
        }

        response = httpx.post(url, json=body)
        if response.status_code != 200:
            raise Exception('Voice generation failed. Response code %d' % response.status_code)
        return base64.b64decode(response.json()["fileContents"])

    @classmethod
    def generate_ru_voice(cls, sound, file_destination: Path):
        voice_bytes = cls.generate_voice_bytes(actor=sound.line.actor, text=sound.line.get_ru_ai_gen_text())
        with open(file_destination, "wb") as fout:
            fout.write(voice_bytes)

    @classmethod
    def generate_ru_voice_simple(cls, actor, text, file_destination: Path):
        voice_bytes = cls.generate_voice_bytes(actor=actor, text=text)
        with open(file_destination, "wb") as fout:
            fout.write(voice_bytes)

    @classmethod
    def generate_test_sound(cls, actor, text, name):
        voice_bytes = cls.generate_voice_bytes(actor=actor, text=text)
        with open(f'results/steos/{name}.mp3', "wb") as fout:
            fout.write(voice_bytes)

    @classmethod
    def prepare_temp_path(cls):
        steos_path = SteosVoice.get_steos_temp_path()

        if steos_path.exists():
            steos_path.rmdir()
        steos_path.mkdir()

    @classmethod
    def generate_temp_sound(cls, actor, text, name):
        voice_bytes = cls.generate_voice_bytes(actor=actor, text=text)
        with open(f'results/steos/temp/{name}.mp3', "wb") as fout:
            fout.write(voice_bytes)

    @classmethod
    def generate_sound(cls, actor, text, file_destination):
        voice_bytes = cls.generate_voice_bytes(actor=actor, text=text)
        with open(file_destination, "wb") as fout:
            fout.write(voice_bytes)
