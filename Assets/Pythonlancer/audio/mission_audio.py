from audio.actors import ACTOR_MALE, ACTOR_TRENT, ACTOR_FEMALE, Trent

from text.dividers import DIVIDER, SINGLE_DIVIDER
from tools.create_id import CreateId


XML_INIT = '<?xml version="1.0" encoding="ISO-8859-1"?>'
XML_FILE_TEMPLATE = '<UTFXML filename="{filename}.utf">'
XML_ROOT_OPEN = '<UTF_ROOT>'

XML_ITEM_TEMPLATE = '<test_voice name="{voiceline_hash}" type="file" filename="{folder}\\{voiceline_nickname}.wav"/>'

XML_ROOT_CLOSE = '</UTF_ROOT>'
XML_FINAL = '</UTFXML>'

THN_SOUND_START = r'{'
THN_SOUND_CONTENT = 'entity_name="{nickname}", template_name="{nickname}"'
THN_SOUND_END = r', type=SOUND,lt_grp=0, srt_grp=0, usr_flg=0, spatialprops={pos={0,0,0},orient={{1,0,0},{0,1,0},{0,0,1}}}, audioprops={attenuation=0,pan=0,dmin=50,dmax=1000,ain=360,aout=360,atout=0,rmix=0}, userprops={category="Audio"}},'

ETHER_COMM_TEMPLATE = (
    ';{actor_name}: \n'
    'Act_EtherComm = {voicepack_name}, {dialog_id}, Player, {voiceline}, -1, {comm_appearance}\n'
    'Act_NNIds = {history_id}, HISTORY'
)


class EtherComm(object):

    def __init__(self, voiceline, actor, dialog_id, history_id, rus_text, eng_text):
        self.voiceline = voiceline
        self.actor = actor
        self.dialog_id = dialog_id
        self.history_id = history_id
        self.rus_text = rus_text
        self.eng_text = eng_text


class MissionAudio(object):
    VOICEPACK_NAME_TEMPLATE_PER_ACTOR = {
        ACTOR_MALE: 'echo_m{mission}',
        ACTOR_TRENT: 'echo_m{mission}_player',
        ACTOR_FEMALE: 'echo_m{mission}_female',
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

    VOICE_ARCH = '[Voice]'
    SOUND_ARCH = '[Sound]'
    MISSION_ID = 1
    START_DIALOGS_ID = 1
    START_HISTORY_ID = 1

    CUTSCENE_VOICES = []

    ATTENUATION = 'attenuation = 0'

    CUTSCENE_SOUND_DEFAULTS = [
        'type = voice',
        ATTENUATION,
        'is_2d = true',
    ]

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def __init__(self, male_actors, female_actors):
        self.male_voicelines = []
        self.trent_voicelines = []
        self.female_voicelines = []

        self.male_actors = male_actors
        self.female_actors = female_actors

        self.male_actor_names = male_actors.keys()
        self.female_actor_names = female_actors.keys()

        self.last_dialog_id = self.START_DIALOGS_ID
        self.last_history_id = self.START_HISTORY_ID
        self.ether_comms = []

        self.parse_ingame_audio()

    def get_next_dialog_id(self):
        self.last_dialog_id += 1
        return self.last_dialog_id

    def get_next_history_id(self):
        self.last_history_id += 1
        return self.last_history_id

    def get_actor_from_voiceline(self, voiceline):
        return voiceline.split('_')[-1] 

    def parse_ingame_audio(self):
        for voiceline, rus_text in self.INGAME_VOICES_MAP:
            actor_name = self.get_actor_from_voiceline(voiceline)
            actor = None

            if actor_name in self.male_actor_names:
                self.male_voicelines.append(voiceline)
                actor = self.male_actors[actor_name]

            elif actor_name in self.female_actor_names:
                self.female_voicelines.append(voiceline)
                actor = self.female_actors[actor_name]

            elif actor_name == Trent.NAME:
                self.trent_voicelines.append(voiceline)
                actor = Trent

            else:
                raise Exception('Unknown actor %s' % actor)

            ether_comm = EtherComm(
                voiceline=voiceline,
                actor=actor,
                dialog_id=self.get_next_dialog_id(),
                history_id=self.get_next_history_id(),
                rus_text=rus_text,
                eng_text='',
            )
            self.ether_comms.append(ether_comm)

    def get_mission_index(self):
        return '0{mission_id}'.format(mission_id=self.MISSION_ID)

    def get_voicepack_name(self, template):
        return template.format(mission=self.get_mission_index())

    def get_male_voicepack_name(self):
        return self.get_voicepack_name(
            template=self.VOICEPACK_NAME_TEMPLATE_PER_ACTOR[ACTOR_MALE]
        )

    def get_trent_voicepack_name(self):
        return self.get_voicepack_name(
            template=self.VOICEPACK_NAME_TEMPLATE_PER_ACTOR[ACTOR_TRENT]
        )

    def get_female_voicepack_name(self):
        return self.get_voicepack_name(
            template=self.VOICEPACK_NAME_TEMPLATE_PER_ACTOR[ACTOR_FEMALE]
        )

    def get_voicepack_by_actor(self, actor):
        if actor.is_male():
            return self.get_male_voicepack_name()
        elif actor.is_female():
            return self.get_female_voicepack_name()
        elif actor.is_player():
            return self.get_trent_voicepack_name()
        raise Exception('Unknown voicepack for actor')

    def get_voice_root(self, nickname, actor):
        items = [
            self.VOICE_ARCH,
            'nickname = {nickname}'.format(nickname=nickname),
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

    def get_ingame_sound_item(self, voiceline):
        lines = [
            self.SOUND_ARCH,
            'msg = {voiceline}'.format(voiceline=voiceline),
            'attenuation = 0',
        ]
        return SINGLE_DIVIDER.join(lines)

    def get_ini_ingame_voicedata(self, voicelines, voice_root):
        items = []
        items.append(voice_root)

        for voiceline in voicelines:
            items.append(
                self.get_ingame_sound_item(voiceline)
            )

        return DIVIDER.join(items)

    def get_ini_ingame_voicefile_content(self):
        items = [
            self.get_ini_ingame_voicedata(self.male_voicelines, self.get_male_voice_root()),
            self.get_ini_ingame_voicedata(self.trent_voicelines, self.get_trent_voice_root()),
            self.get_ini_ingame_voicedata(self.female_voicelines, self.get_female_voice_root()),
        ]
        return DIVIDER.join(items)

    def get_hash_for_voiceline(self, voiceline_nickname):
        return CreateId.get_id(voiceline_nickname)

    def _get_utf_file_content(self, voicelines, voicepack_nickname):
        items = [
            XML_INIT,
            XML_FILE_TEMPLATE.format(filename=voicepack_nickname),
            XML_ROOT_OPEN,
        ]
        for voiceline_nickname in voicelines:
            template_params = {
                'voiceline_nickname': voiceline_nickname,
                'voiceline_hash': self.get_hash_for_voiceline(voiceline_nickname),
                'folder': voicepack_nickname,
            }
            items.append(XML_ITEM_TEMPLATE.format(**template_params))
        items.append(XML_ROOT_CLOSE)
        items.append(XML_FINAL)
        return SINGLE_DIVIDER.join(items)

    def get_utf_male_voicefile_content(self):
        voicepack_nickname = self.get_male_voicepack_name()
        return self._get_utf_file_content(self.male_voicelines, voicepack_nickname)

    def get_utf_trent_voicefile_content(self):
        voicepack_nickname = self.get_trent_voicepack_name()
        return self._get_utf_file_content(self.trent_voicelines, voicepack_nickname)

    def get_utf_female_voicefile_content(self):
        voicepack_nickname = self.get_female_voicepack_name()
        return self._get_utf_file_content(self.female_voicelines, voicepack_nickname)

    def get_utf_file_content(self):
        items = [
            self.get_utf_male_voicefile_content(),
            self.get_utf_trent_voicefile_content(),
            self.get_utf_female_voicefile_content(),
        ]
        return DIVIDER.join(items)

    def get_cutscene_sound_nickname(self, voiceline):
        return 'DX_{voiceline}'.format(voiceline=voiceline)

    def get_cutscene_sound_file_destination(self, voiceline):
        return 'audio\\mod\\m{mission_index}\\{voiceline}.wav'.format(
            mission_index=self.get_mission_index(),
            voiceline=voiceline
        )

    def get_cutscene_sound_item(self, voiceline):
        nickname = self.get_cutscene_sound_nickname(voiceline)
        lines = [
            self.SOUND_ARCH,
            'nickname = {voice_nickname}'.format(voice_nickname=self.get_cutscene_sound_nickname(voiceline)),
            'file = {file_destination}'.format(file_destination=self.get_cutscene_sound_file_destination(voiceline)),
        ]
        lines.extend(self.CUTSCENE_SOUND_DEFAULTS)
        return SINGLE_DIVIDER.join(lines)

    def get_ini_cutscene_sounds_content(self):
        items = [self.get_cutscene_sound_item(voiceline) for voiceline in self.CUTSCENE_VOICES]
        return DIVIDER.join(items)

    def get_cutscene_thn_sound_item(self, voiceline):
        lines = [
            THN_SOUND_START,
            THN_SOUND_CONTENT.format(nickname=self.get_cutscene_sound_nickname(voiceline)),
            THN_SOUND_END,
        ]
        return ''.join(lines)

    def get_thn_cutscene_sounds_content(self):
        items = [self.get_cutscene_thn_sound_item(voiceline) for voiceline in self.CUTSCENE_VOICES]
        return SINGLE_DIVIDER.join(items)

    def get_ingame_rus_dialog_strings(self):
        items = {}
        for ether_comm in self.ether_comms:
            items[ether_comm.dialog_id] = ether_comm.rus_text
        return items

    def get_ingame_rus_history_strings(self):
        items = {}
        for ether_comm in self.ether_comms:
            items[ether_comm.history_id] = '*' + ether_comm.rus_text
        return items

    def get_ingame_ether_comms(self):
        items = []

        for ether_comm in self.ether_comms:
            items.append(
                ETHER_COMM_TEMPLATE.format(
                    actor_name=ether_comm.actor.NAME,
                    voicepack_name=self.get_voicepack_by_actor(ether_comm.actor),
                    voiceline=ether_comm.voiceline,
                    dialog_id=ether_comm.dialog_id,
                    history_id=ether_comm.history_id,
                    comm_appearance='tmp',
                )
            )

        return DIVIDER.join(items)
