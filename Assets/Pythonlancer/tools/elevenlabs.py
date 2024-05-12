import requests
from settings import ELEVENLABS_API_KEY




class ElevenLabs(object):

    @classmethod
    def get_line(cls, text):
        url = "https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB"

        querystring = {"output_format":"mp3_44100_128"}

        payload = {
            "text": text,
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            },
            "previous_request_ids": [],
            "model_id": "eleven_multilingual_v2"
        }
        headers = {
            "xi-api-key": ELEVENLABS_API_KEY,
            "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
        import pdb;pdb.set_trace()

        filename = 'out.mp3'
        with open(filename, mode='wb') as localfile:
            localfile.write(response.content)

        import pdb;pdb.set_trace()

