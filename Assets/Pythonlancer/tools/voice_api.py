from settings import VOICE_BACKEND
from tools.steos import SteosVoice
from tools.voicestudio import VoiceStudioClone


def _backend():
    if VOICE_BACKEND == 'voicestudio':
        return VoiceStudioClone
    if VOICE_BACKEND == 'steos':
        return SteosVoice
    raise Exception('Unknown VOICE_BACKEND %s' % VOICE_BACKEND)


class VoiceApi(object):

    @classmethod
    def generate_ru_voice(cls, sound, file_destination):
        return _backend().generate_ru_voice(sound, file_destination)

    @classmethod
    def generate_en_voice(cls, sound, file_destination):
        return _backend().generate_en_voice(sound, file_destination)

    @classmethod
    def generate_ru_voice_simple(cls, actor, text, file_destination):
        return _backend().generate_ru_voice_simple(actor=actor, text=text, file_destination=file_destination)

    @classmethod
    def generate_sound(cls, actor, text, file_destination, source_name=None, source_lang='ru', speech_lang=None, delivery=None, speed=None):
        if VOICE_BACKEND == 'steos':
            return SteosVoice.generate_sound(actor, text, file_destination)
        return VoiceStudioClone.generate_sound(
            actor=actor,
            text=text,
            file_destination=file_destination,
            source_name=source_name,
            source_lang=source_lang,
            speech_lang=speech_lang,
            delivery=delivery,
            speed=speed,
        )
