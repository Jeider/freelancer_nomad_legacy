import hashlib
import io
import wave
import json
import pathlib
import time

import httpx
from pydub import AudioSegment
from pydub.silence import detect_nonsilent

from settings import VOICESTUDIO_API_KEY, VOICESTUDIO_BASE_URL, VOICESTUDIO_MODEL

SOURCE_DIRS = {
    'ru': 'VOICE_SOURCE_RU',
    'en': 'VOICE_SOURCE_EN',
}
SOURCE_EXTENSIONS = ('.wav', '.mp3', '.flac', '.ogg', '.m4a')
SPEECH_LANG = {
    'ru': 'ru',
    'en': 'en',
}


class VoiceStudioClone(object):
    _warned = set()

    @staticmethod
    def assets_root():
        return pathlib.Path(__file__).resolve().parents[2]

    @classmethod
    def cache_path(cls):
        path = pathlib.Path(__file__).resolve().parents[1] / 'results' / 'voicestudio'
        path.mkdir(parents=True, exist_ok=True)
        return path / 'profiles.json'

    @classmethod
    def source_name_of(cls, actor, source_name=None):
        if source_name:
            return source_name
        if isinstance(actor, type):
            return actor.__name__
        name = type(actor).__name__
        if name == 'DynamicActor':
            raise Exception('DynamicActor has no class name; pass source_name')
        return name

    @classmethod
    def source_file(cls, source_name, source_lang):
        if source_lang not in SOURCE_DIRS:
            raise Exception('source_lang must be ru or en, got %s' % source_lang)
        folder = cls.assets_root() / SOURCE_DIRS[source_lang]
        for ext in SOURCE_EXTENSIONS:
            path = folder / f'{source_name}{ext}'
            if path.exists():
                return path
        expected = folder / f'{source_name}.wav'
        raise Exception(
            'Missing clone source for %s (%s): %s' % (source_name, source_lang, expected)
        )

    @classmethod
    def _client(cls):
        return httpx.Client(
            base_url=VOICESTUDIO_BASE_URL,
            timeout=httpx.Timeout(30.0, read=1200.0),
            headers={'Authorization': 'Bearer %s' % VOICESTUDIO_API_KEY},
        )

    @staticmethod
    def _log(message):
        print('VoiceStudio %s' % message)

    @classmethod
    def _request(cls, client, method, path, **kwargs):
        cls._log('%s %s' % (method, path))
        started = time.time()
        response = client.request(method, path, **kwargs)
        cls._log('%s %s -> %s in %.1fs (%s bytes)' % (
            method, path, response.status_code, time.time() - started, len(response.content),
        ))
        return response

    @classmethod
    def _load_cache(cls):
        path = cls.cache_path()
        if not path.exists():
            return {}
        return json.loads(path.read_text(encoding='utf-8'))

    @classmethod
    def _save_cache(cls, cache):
        cls.cache_path().write_text(json.dumps(cache, indent=2), encoding='utf-8')

    @classmethod
    def _profile_id(cls, client, source_name, source_lang, source):
        digest = hashlib.sha1(source.read_bytes()).hexdigest()
        key = '%s|%s|%s' % (source_name, source_lang, digest)
        cache = cls._load_cache()
        profile_id = cache.get(key)
        if profile_id:
            check = cls._request(client, 'GET', '/profiles/%s' % profile_id)
            if check.status_code == 200:
                cls._log('reuse profile %s for %s (%s)' % (profile_id, source_name, source_lang))
                return profile_id

        cls._log('clone %s (%s) from %s' % (source_name, source_lang, source.name))
        with open(source, 'rb') as handle:
            response = cls._request(
                client,
                'POST',
                '/profiles',
                data={
                    'name': 'nl-%s-%s' % (source_name, source_lang),
                    'kind': 'clone',
                    'language': SPEECH_LANG[source_lang],
                },
                files={'ref_audio': (source.name, handle, 'application/octet-stream')},
            )
        if response.status_code != 200:
            raise Exception(
                'VoiceStudio clone profile failed (%s): %s' % (response.status_code, response.text)
            )
        profile_id = response.json()['id']
        cache[key] = profile_id
        cls._save_cache(cache)
        cls._log('cloned %s (%s) -> %s' % (source_name, source_lang, profile_id))
        return profile_id

    @classmethod
    def _delivery_of(cls, actor, delivery):
        if delivery is not None:
            return delivery
        if actor is not None and hasattr(actor, 'get_voice_delivery'):
            return actor.get_voice_delivery()
        return getattr(actor, 'VOICE_DELIVERY', None)

    @classmethod
    def _warn_delivery(cls, delivery):
        if delivery is None or delivery.instruct or not delivery.emo_text:
            return
        if delivery.code in cls._warned:
            return
        cls._warned.add(delivery.code)
        cls._log(
            'delivery %s is reserved; omnivoice ignores it and clones the reference as-is'
            % delivery.code
        )

    @classmethod
    def _speed_of(cls, actor, speed, delivery):
        if delivery is not None and delivery.speed is not None:
            speed = delivery.speed
        elif speed is None and actor is not None and hasattr(actor, 'get_steos_speed'):
            speed = actor.get_steos_speed()
        if speed is None:
            speed = 1.0
        return max(0.25, min(float(speed), 4.0))

    @classmethod
    def generate_voice_bytes(cls, actor, text, source_lang, speech_lang=None, delivery=None, speed=None, source_name=None, denoise=True):
        if not text:
            raise Exception('text is mandatory')
        source_name = cls.source_name_of(actor, source_name)
        source = cls.source_file(source_name, source_lang)
        speech_lang = speech_lang or source_lang
        delivery = cls._delivery_of(actor, delivery)
        cls._warn_delivery(delivery)

        body = {
            'model': VOICESTUDIO_MODEL,
            'input': text,
            'response_format': 'wav',
            'speed': cls._speed_of(actor, speed, delivery),
            'language': SPEECH_LANG.get(speech_lang, speech_lang),
            'denoise': denoise,
        }
        if delivery is not None and delivery.instruct:
            body['instruct'] = delivery.instruct
        if delivery is not None and delivery.emo_text:
            body['description'] = delivery.emo_text

        with cls._client() as client:
            body['voice'] = cls._profile_id(client, source_name, source_lang, source)
            preview = text if len(text) <= 80 else text[:77] + '...'
            cls._log('speech voice=%s lang=%s speed=%s denoise=%s instruct=%s text=%r' % (
                body['voice'], body['language'], body['speed'], body['denoise'], body.get('instruct'), preview,
            ))
            response = cls._request(client, 'POST', '/v1/audio/speech', json=body)
        if response.status_code != 200:
            raise Exception(
                'VoiceStudio speech failed (%s): %s' % (response.status_code, response.text)
            )
        return cls._pcm_wav(response.content)

    @staticmethod
    def output_path(file_destination):
        return pathlib.Path(file_destination).with_suffix('.wav')

    @staticmethod
    def _pcm_wav(voice_bytes):
        # Reject MP3 (including MP3-in-WAV), raw PCM, empty/truncated responses.
        # Preserve the engine's sample rate and channels; store integer PCM16.
        try:
            with wave.open(io.BytesIO(voice_bytes), 'rb') as wav:
                channels, width, rate, frames, compression, _ = wav.getparams()
                samples = wav.readframes(frames)
        except (wave.Error, EOFError) as error:
            raise ValueError('VoiceStudio must return an uncompressed PCM WAV') from error
        if compression != 'NONE' or not frames or len(samples) != frames * channels * width:
            raise ValueError('VoiceStudio returned empty or truncated PCM WAV')
        segment = AudioSegment(data=samples, sample_width=width, frame_rate=rate, channels=channels)
        result = io.BytesIO()
        segment.set_sample_width(2).export(result, format='wav')
        return result.getvalue()

    @classmethod
    def trim_leading(cls, file_destination, thresh=-34, pad_ms=40, min_cut_ms=60):
        path = pathlib.Path(file_destination)
        if any(part.lower() == 'data' for part in path.resolve().parts):
            raise ValueError('Trimming source recordings cannot write DATA')
        seg = AudioSegment.from_wav(path).set_sample_width(2)
        regions = detect_nonsilent(seg, min_silence_len=180, silence_thresh=thresh)
        if not regions:
            return 0
        start, end = regions[0]
        if len(regions) > 1 and (end - start) < 250 and regions[1][0] - end >= 180:
            start = regions[1][0]
        cut = start - pad_ms
        if cut < min_cut_ms or len(seg) - cut < 150:
            return 0
        tmp = path.with_suffix(path.suffix + '.trim')
        seg[cut:].export(tmp, format='wav')
        tmp.replace(path)
        return cut

    @classmethod
    def _write(cls, voice_bytes, file_destination, trim_lead=False):
        path = cls.output_path(file_destination)
        if any(part.lower() == 'data' for part in path.resolve().parts):
            raise ValueError('VoiceStudio writes source recordings only; use DataFolder for DATA')
        pcm_wav = cls._pcm_wav(voice_bytes)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(pcm_wav)
        if trim_lead:
            cls.trim_leading(path)
        return path

    @classmethod
    def generate_ru_voice(cls, sound, file_destination):
        return cls._write(
            cls.generate_voice_bytes(
                actor=sound.line.actor,
                text=sound.line.get_ru_ai_gen_text(),
                source_lang='ru',
                speech_lang='ru',
                delivery=sound.line.delivery,
            ),
            file_destination,
        )

    @classmethod
    def generate_en_voice(cls, sound, file_destination):
        return cls._write(
            cls.generate_voice_bytes(
                actor=sound.line.actor,
                text=sound.line.get_en_ai_gen_text(),
                source_lang='en',
                speech_lang='en',
                delivery=sound.line.delivery,
            ),
            file_destination,
        )

    @classmethod
    def generate_ru_voice_simple(cls, actor, text, file_destination):
        return cls._write(
            cls.generate_voice_bytes(actor=actor, text=text, source_lang='ru', speech_lang='ru'),
            file_destination,
        )

    @classmethod
    def generate_sound(cls, actor, text, file_destination, source_name=None, source_lang='ru', speech_lang=None, delivery=None, speed=None, denoise=True, trim_lead=False):
        return cls._write(
            cls.generate_voice_bytes(
                actor=actor,
                text=text,
                source_lang=source_lang,
                speech_lang=speech_lang or source_lang,
                delivery=delivery,
                speed=speed,
                source_name=source_name,
                denoise=denoise,
            ),
            file_destination,
            trim_lead=trim_lead,
        )
