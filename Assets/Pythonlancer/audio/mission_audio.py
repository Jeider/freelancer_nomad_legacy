from audio.actors import ACTOR_MALE, ACTOR_TRENT, ACTOR_FEMALE

from text.dividers import DIVIDER, SINGLE_DIVIDER
from tools.create_id import CreateId


XML_INIT = '<?xml version="1.0" encoding="ISO-8859-1"?>'
XML_FILE_TEMPLATE = '<UTFXML filename="{filename}">'
XML_ROOT_OPEN = '<UTF_ROOT>'

XML_ITEM_TEMPLATE = '<test_voice name="{voiceline_hash}" type="file" filename="{folder}\\{voiceline_nickname}.wav"/>'

XML_ROOT_CLOSE = '</UTF_ROOT>'
XML_FINAL = '</UTFXML>'


class MissionAudio(object):
    VOICEPACK_NAME_TEMPLATE_PER_ACTOR = {
        ACTOR_MALE: 'm{mission}',
        ACTOR_TRENT: 'm{mission}_player',
        ACTOR_FEMALE: 'm{mission}_female',
    }

    FILE_TEMPLATE = '{file}.utf'

    ANIMATIONS_PER_ACTOR = {
        ACTOR_MALE: [
            'SC_MLHEAD_MOTION_WALLA_CASL_000LV_XA_%',
            'SC_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07',
        ],
        ACTOR_TRENT: [
            'Sc_dx_GCS_W04aP01_Trent',
            'SC_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07',
        ],
        ACTOR_FEMALE: [
            'SC_FMHEAD_MOTION_WALLA_CASL_000LV_XA_%',
            'SC_FMBODY_CHRB_IDLE_SMALL_000LV_XA_05',
        ]
    }

    MALE_VOICELINES = []
    FEMALE_VOICELINES = []
    TRENT_VOICELINES = []

    VOICE_ARCH = '[Voice]'
    SOUND_ARCH = '[Sound]'
    MISSION_ID = 1

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def __init__(self, male_voicelines, trent_voicelines, female_voicelines):
        self.male_voicelines = male_voicelines
        self.trent_voicelines = trent_voicelines
        self.female_voicelines = female_voicelines

    def get_mission_index(self):
        return '0{mission_id}'.format(mission_id=self.MISSION_ID)

    def get_voicepack_name(self, template):
        return template.format(mission=self.get_mission_index())

    def get_male_voicepack_name(self):
        return self.get_voicepack_name(
            template=self.VOICEPACK_NAME_TEMPLATE_PER_ACTOR(ACTOR_MALE)
        )

    def get_trent_voicepack_name(self):
        return self.get_voicepack_name(
            template=self.VOICEPACK_NAME_TEMPLATE_PER_ACTOR(ACTOR_TRENT)
        )

    def get_female_voicepack_name(self):
        redturn self.get_voicepack_name(
            template=self.VOICEPACK_NAME_TEMPLATE_PER_ACTOR(ACTOR_FEMALE)
        )

    def get_voice_root(self, nickname, actor):
        items = [
            self.VOICE_ARCH,
            'nickname = {nickname}',
        ]
        animations = self.ANIMATIONS_PER_ACTOR[actor]
        for animation in animations:
            items.append('script = {animation}'.format(animation=animation))
        return SINGLE_DIVIDER.join(items)
    
    def get_male_voice_root(self):
        return self.get_voice_root(
            nickname=self.get_male_voicepack_name(),
            actor=ACTOR_MALE,
        )
    
    def get_trent_voice_root(self):
        return self.get_voice_root(
            nickname=self.get_trent_voicepack_name(),
            actor=ACTOR_TRENT,
        )
    
    def get_female_voice_root(self):
        return self.get_voice_root(
            nickname=self.get_female_voicepack_name(),
            actor=ACTOR_FEMALE,
        )

    def get_sound_item(self, voiceline):
        items = [
            self.SOUND_ARCH,
            'msg = {voiceline}'.format(voiceline=voiceline),
            'attenuation = 0',
        ]
        return SINGLE_DIVIDER.join(items)


    def get_ini_voicedata(self, voicelines, voice_root):
        items = []
        items.append(voice_root)

        for voiceline in voicelines:
            items.append(
                self.get_sound_item(voiceline)
            )

        return DIVIDER.join(voicelines)


    def get_ini_voicefile_content(self):
        items = [
            self.get_ini_voicedata(self.male_voicelines, self.get_male_voice_root),
            self.get_ini_voicedata(self.trent_voicelines, self.get_trent_voice_root),
            self.get_ini_voicedata(self.female_voicelines, self.get_female_voice_root),
        ]
        return DIVIDER.join(item)

    def get_hash_for_voiceline(self, voiceline_nickname):
        return CreateId.get_id(voiceline_nickname)

    def _get_utf_file_content(self, filename, voicelines, folder_name):
        items = [
            XML_INIT,
            XML_FILE_TEMPLATE.format(filename=filename),
            XML_ROOT_OPEN,
        ]
        for voiceline_nickname in voicelines:
            template_params = {
                'voiceline_nickname': voiceline_nickname,
                'voiceline_hash': self.get_hash_for_voiceline(voiceline_nickname),
                'folder': folder_name,
            }
            items.append(XML_ITEM_TEMPLATE.format(**template_params))
        items.append(XML_ROOT_CLOSE)
        items.append(XML_FINAL)
        return DIVIDER.join(items)

    def get_utf_male_voicefile_content(self):
        voicelines = self.get_voicedata(self.male_voicelines, self.get_male_voice_root)
        folder_name = self.get_male_voicepack_name()
        return self._get_utf_file_content(voicelines, folder_name)

    def get_utf_trent_voicefile_content(self):
        voicelines = self.get_voicedata(self.trent_voicelines, self.get_trent_voice_root)
        folder_name = self.get_trent_voicepack_name()
        return self._get_utf_file_content(voicelines, folder_name)

    def get_utf_female_voicefile_content(self):
        voicelines = self.get_voicedata(self.female_voicelines, self.get_female_voice_root)
        folder_name = self.get_female_voicepack_name()
        return _get_utf_file_content(voicelines, folder_name)
