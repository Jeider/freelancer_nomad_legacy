from story.actors import DynamicActor

from universe.audio.parse_rule import RuleDefault

SOUND_TEMPLATE = '''[Sound]
msg = {code}
duration = 2
{attenuation}
Priority = -6'''

SOUND_FILE_TEMPLATE = '''[Sound]
msg = {code}
duration = 2
{attenuation}
file = Audio\\MOD_ENG\\{voice}\\{code}.wav
Priority = -6'''


class PilotLine(object):
    def __init__(self, code, ru_text, parse_rule=None):
        self.code = code
        self.ru_text = ru_text
        self.parse_rule = parse_rule if parse_rule else RuleDefault

    def get_text(self):
        return self.ru_text

    def get_temp_text(self):
        return self.parse_rule.get_temp_text(self.ru_text)

    def get_actor(self, steos_id):
        return DynamicActor(
            steos_id=steos_id,
            steos_pitch=self.parse_rule.STEOS_PITCH,
            steos_speed=self.parse_rule.STEOS_SPEED,
        )

    def get_code(self):
        return self.code

    def get_subfolder(self):
        return self.parse_rule.get_subfolder()

    def process_temp(self):
        return self.parse_rule.process_temp(self.code)

    def is_static(self):
        return self.parse_rule.is_static()

    def is_static_from_root(self):
        return self.parse_rule.is_static_from_root()

    def get_sound(self, attenuation):
        return SOUND_TEMPLATE.format(
            code=self.code,
            attenuation=attenuation,
        )

    def get_sound_as_file(self, attenuation, voice):
        return SOUND_FILE_TEMPLATE.format(
            code=self.code,
            attenuation=attenuation,
            voice=voice
        )

    def get_static_file(self):
        return self.parse_rule.get_static_file(self.ru_text)
