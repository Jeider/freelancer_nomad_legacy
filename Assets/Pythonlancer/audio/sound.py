import re
from text.dividers import SINGLE_DIVIDER
from tools.create_id import CreateId


SPACE_ATTENUATION = 0
CUTSCENE_ATTENUATION = 0

SOUND_ARCH = '[Sound]'


class VoiceLine(object):
    COMMENT_START = "<span class='comment'>("
    COMMENT_END = ")</span>"

    def __init__(self, index, actor, ru='', en='', comment=''):
        self.index = index
        self.actor = actor
        self.ru = ru
        self.en = en
        self.comment = comment

    def get_ru_replaced_text(self):
        return self.ru.replace('(', self.COMMENT_START).replace(')', self.COMMENT_END)

    def get_ru_story_text(self):
        content = self.get_ru_replaced_text()

        return f'{self.actor.RU_NAME}: {content}'

    def get_ru_clean_text(self):
        return re.sub(r'\(.*?\)', '', self.ru)

    def get_ru_subtitle(self):
        return f'{self.actor.RU_NAME}:\n{self.get_ru_clean_text()}'


class Sound:
    def __init__(self, line, name):
        self.line = line
        self.name = name

    def get_nickname(self):
        raise NotImplementedError

    def get_ini(self):
        raise NotImplementedError

    def get_nickname_hash(self):
        the_id = CreateId.get_hex_id(self.name)
        return f'0x{str(the_id)[2:].upper()}'


class SpaceSound(Sound):
    def get_nickname(self):
        return self.name

    def get_ini(self):
        return SINGLE_DIVIDER.join([
            SOUND_ARCH,
            f'msg = {self.get_nickname()}',
            f'attenuation = {SPACE_ATTENUATION}'
        ])


class CutsceneSound(Sound):
    def __init__(self, destination, **kwargs):
        super().__init__(**kwargs)
        self.destination = destination

    def get_nickname(self):
        return f'DX_{self.name}'

    def get_cutscene_ini(self, root):
        return SINGLE_DIVIDER.join([
            SOUND_ARCH,
            f'msg = {self.get_nickname()}',
            'type = voice',
            f'attenuation = {CUTSCENE_ATTENUATION}',
            f'file = {root}\\{self.name}.wav',
            'is_2d = true',
        ])
