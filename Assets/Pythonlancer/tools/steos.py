import httpx
import base64

from story.voiceline import VoiceLine
from story.script import MissionSegment

from settings import STEOS_API_KEY

class SteosVoice(object):

    @classmethod
    def generate_voice_bytes(cls, actor, text):
        if not actor.STEOS_ID:
            raise Exception('Actor %s have no steos actor id' % actor.NAME)
        if not text or text == '':
            raise Exception('text is mandatory')

        url = f"https://public.api.voice.steos.io/api/v1/synthesize-controller/synthesis-by-text?authToken={STEOS_API_KEY}"

        body = {
            "voiceId": actor.STEOS_ID,
            "text": text,
            "pitchShift": actor.STEOS_PITCH,
            "speedMultiplier": actor.STEOS_SPEED,
            "format": "mp3"
        }

        response = httpx.post(url, json=body)
        if response.status_code != 200:
            raise Exception('Voice generation failed. Response code %d' % response.status_code)
        return base64.b64decode(response.json()["fileContents"])

    @classmethod
    def generate_ru_voice(cls, voice_line: VoiceLine, segment: MissionSegment):
        voice_bytes = cls.generate_voice_bytes(actor=voice_line.actor, text=voice_line.ru)
        line_name = segment.get_name_for_line(voice_line)
        with open(f"results/steos/{line_name}.mp3", "wb") as fout:
            fout.write(voice_bytes)
