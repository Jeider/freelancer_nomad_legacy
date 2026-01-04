import re
from text.dividers import SINGLE_DIVIDER
from tools.create_id import CreateId
from tools.audio_watcher import AudioWatcher

from text.strings import MultiString as MS

SPACE_ATTENUATION = -8
CUTSCENE_ATTENUATION = 0

SOUND_ARCH = '[Sound]'


class VoiceLine(object):
    COMMENT_START = "<span class='comment'>("
    COMMENT_END = ")</span>"

    def __init__(self, index, actor, ru='', en='', comment='', cinematic=False):
        self.index = index
        self.actor = actor
        self.ru = ru
        self.en = en
        self.comment = comment
        self.ids_sub = None
        self.cinematic = cinematic

    def is_cinematic(self):
        return self.cinematic

    def get_ru_replaced_text(self):
        return self.ru.replace('(', self.COMMENT_START).replace(')', self.COMMENT_END).replace('+', '')

    def get_ru_story_text(self):
        content = self.get_ru_replaced_text()

        return f'{self.actor.RU_NAME}: {content}'

    def get_ru_clean_text(self):
        return re.sub(r'\(.*?\)', '', self.ru).replace(',,', ',')

    def get_en_clean_text(self):
        return re.sub(r'\(.*?\)', '', self.en).replace(',,', ',')

    def get_ru_clean_ai_text(self):
        return re.sub(r'\(.*?\)', '', self.ru).replace(',,', '')

    def get_en_clean_ai_text(self):
        return re.sub(r'\(.*?\)', '', self.en).replace(',,', '')

    def get_ru_ai_gen_text(self):
        return (self.get_ru_clean_ai_text().replace('СБА', 'эс-бэ-а').replace('Трент', 'Трэнт')
                .replace('Рокфорд', 'Р+окфорд').replace('бизнес', 'б+изнэс'))

    def get_ru_sub_text(self):
        return self.get_ru_clean_text().replace('+', '')

    def get_en_sub_text(self):
        return self.get_en_clean_text().replace('+', '')

    def get_en_ai_gen_text(self):
        # print(self.index)
        return (self.get_en_clean_ai_text()
                .replace("'", '')
                .replace("Mr.", 'm+ister')
                .replace("mr.", 'm+ister')
                .replace('ASF', 'A-eS-eF')
                .replace(',,', ',')
                .replace('Mrs.', 'missis')
                .replace('EMP', 'Ee-Em-Pi'))

    def get_ru_subtitle(self):
        return MS(
            f'{self.actor.RU_NAME.get_ru()}:\\n{self.get_ru_sub_text()}',
            f'{self.actor.RU_NAME.get_en()}:\\n{self.get_en_sub_text()}'
        )

    def set_ids_sub(self, ids_sub):
        self.ids_sub = ids_sub

    def get_sub_id(self):
        return self.ids_sub.id

    def get_subtitle_text(self, russian):
        return self.get_ru_sub_text() if russian else self.get_en_sub_text()


class Sound:
    def __init__(self, line, name, mission_segment, attenuation=None):
        self.line = line
        self.name = name
        self.mission_segment = mission_segment
        self.attenuation = attenuation

    def get_nickname(self):
        raise NotImplementedError

    def get_ini(self):
        raise NotImplementedError

    def get_nickname_hash(self):
        return CreateId.get_audio_id(self.name)

    def get_attenuation(self):
        return self.attenuation

    def get_subtitle_content(self, russian=True, root=''):
        raise NotImplementedError

    def use_in_cinematic(self):
        return False


class SpaceSound(Sound):
    def use_in_cinematic(self):
        return self.line.is_cinematic()

    def get_nickname(self):
        return self.name

    def get_ini(self):
        attenuation = self.get_attenuation()
        return SINGLE_DIVIDER.join([
            SOUND_ARCH,
            f'msg = {self.get_nickname()}',
            f'attenuation = {attenuation if attenuation is not None else SPACE_ATTENUATION}'
        ])

    def get_subtitle_content(self, russian=True, root=''):
        return f'<Static AudioFile="{root}.utf|{self.get_nickname_hash()}" TextArea="Cinematic">{self.line.get_subtitle_text(russian)}</Static>'


class CutsceneSound(Sound):

    def use_in_cinematic(self):
        return True

    def get_destination(self, suffix=''):
        return self.mission_segment.get_destination(suffix)

    def get_short_destination(self, suffix=''):
        return self.mission_segment.get_short_destination(suffix)

    def get_duration(self, russian=True):
        return AudioWatcher().watch_cutscene_audio_duration(
            self.mission_segment.get_subfolder(),
            self.get_filename(),
            russian=russian
        )

    def get_nickname(self):
        return f'DX_{self.name}'

    def get_filename(self):
        return f'{self.name}.wav'

    def get_cutscene_ini(self, russian=True):
        suffix = "" if russian else "_ENG"
        return SINGLE_DIVIDER.join([
            SOUND_ARCH,
            f'nickname = {self.get_nickname()}',
            'type = voice',
            f'attenuation = {CUTSCENE_ATTENUATION}',
            f'file = {self.get_destination(suffix)}\\{self.get_filename()}',
            'is_2d = true',
        ])

    def get_subtitle_content(self, russian=True, root=''):
        suffix = "" if russian else "_ENG"
        return f'<Static AudioFile="{self.get_short_destination(suffix)}\\{self.get_filename()}" TextArea="Cinematic">{self.line.get_subtitle_text(russian)}</Static>'

    def get_thorn(self):
        nickname = self.get_nickname()
        return '''
{
    entity_name="'''+nickname+'''",
    template_name="'''+nickname+'''",
    type=SOUND,lt_grp=0, srt_grp=0, usr_flg=0, spatialprops={pos={0,0,0},orient={{1,0,0},{0,1,0},{0,0,1}}}, audioprops={attenuation=0,pan=0,dmin=50,dmax=1000,ain=360,aout=360,atout=0,rmix=0}, userprops={category="Audio"}
}
        '''

    @property
    def thorn_play(self, start_time=0, duration=30):
        return '''
{
    '''+str(start_time)+''',
    START_SOUND,
    {
        "'''+self.get_nickname()+'''"
    },
    {
        duration='''+str(duration)+'''
    }
},
'''

    @property
    def thorn_costume(self):
        actor = self.line.actor
        if not actor:
            raise Exception(f'{self.line} have no actor')
        if actor.CUTSCENE_APPEARANCE == '':
            raise Exception(f'{actor} have no costume for cutscene')

        return actor.CUTSCENE_APPEARANCE
