import httpx

from settings import STEOS_API_KEY

class SteosVoice(object):
    @classmethod
    def get_headers(cls):
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": STEOS_API_KEY,
        }

    @classmethod
    def get_voices_list(cls):
        body = {'voice_id': 1,
                'text': 'Hello, my name is Gabe Newell. And today I will reveal the release data of half life 3.',
                                                                        'format': 'mp3'}

        url = "https://public.api.voice.steos.io/api/v1/steos-voice-controller/available-voices"
        response = httpx.get(url, headers=cls.get_headers())
        import pdb;pdb.set_trace()
        pdb.set_trace()
        response = httpx.get(url, headers=cls.get_headers())
        import pdb;pdb.set_trace()
        return response.json()