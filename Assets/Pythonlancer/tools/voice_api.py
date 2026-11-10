from settings import VOICE_BACKEND
from tools.steos import SteosVoice
from tools.voicestudio import VoiceStudioClone
from tools.wav_post import goldwave_wav


def _backend():
    if VOICE_BACKEND == 'voicestudio':
        return VoiceStudioClone
    if VOICE_BACKEND == 'steos':
        return SteosVoice
    raise Exception('Unknown VOICE_BACKEND %s' % VOICE_BACKEND)


def _finish(path):
    if VOICE_BACKEND == 'voicestudio' and path:
        goldwave_wav(path)
    return path


class VoiceApi(object):

    @classmethod
    def generate_ru_voice(cls, sound, file_destination, default_actor=None):
        backend = _backend()
        if backend is VoiceStudioClone:
            return _finish(backend.generate_ru_voice(sound, file_destination, default_actor=default_actor))
        if default_actor:
            raise Exception('default_actor requires VOICE_BACKEND=voicestudio')
        return backend.generate_ru_voice(sound, file_destination)

    @classmethod
    def generate_en_voice(cls, sound, file_destination, default_actor=None):
        backend = _backend()
        if backend is VoiceStudioClone:
            return _finish(backend.generate_en_voice(sound, file_destination, default_actor=default_actor))
        if default_actor:
            raise Exception('default_actor requires VOICE_BACKEND=voicestudio')
        return backend.generate_en_voice(sound, file_destination)

    @classmethod
    def generate_ru_voice_simple(cls, actor, text, file_destination):
        return _finish(_backend().generate_ru_voice_simple(actor=actor, text=text, file_destination=file_destination))

    @classmethod
    def generate_sound(cls, actor, text, file_destination, source_name=None, source_lang='ru', speech_lang=None, delivery=None, speed=None, denoise=True, trim_lead=False):
        if VOICE_BACKEND == 'steos':
            return SteosVoice.generate_sound(actor, text, file_destination)
        return _finish(VoiceStudioClone.generate_sound(
            actor=actor,
            text=text,
            file_destination=file_destination,
            source_name=source_name,
            source_lang=source_lang,
            speech_lang=speech_lang,
            delivery=delivery,
            speed=speed,
            denoise=denoise,
            trim_lead=trim_lead,
        ))
