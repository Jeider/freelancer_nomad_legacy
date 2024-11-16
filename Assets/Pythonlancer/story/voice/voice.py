from text.dividers import SINGLE_DIVIDER, DIVIDER

RU_VOICE_FOLDER = 'AUDIO_XML_RU'

XML_INIT = '<?xml version="1.0" encoding="ISO-8859-1"?>'
XML_FILE_TEMPLATE = '<UTFXML filename="{filename}.utf">'
XML_ROOT_OPEN = '<UTF_ROOT>'

XML_ITEM_TEMPLATE = '<test_voice name="{voiceline_hash}" type="file" filename="{folder}\\{voiceline_nickname}.wav"/>'

XML_ROOT_CLOSE = '</UTF_ROOT>'
XML_FINAL = '</UTFXML>'

VOICE_ARCH = '[Voice]'


class Voice:
    COMM_ANIMATIONS = []

    def __init__(self, voice_name, sounds):
        self.voice_name = voice_name
        self.sounds = sounds

    def get_xml(self):
        pass

    def get_ini(self):
        items = [self.get_root_ini()]

        for sound in self.sounds:
            items.append(sound.get_ini())

        return DIVIDER.join(items)

    def get_root_ini(self):
        items = [
            VOICE_ARCH,
            f'nickname = {self.voice_name}',
        ]
        for animation in self.COMM_ANIMATIONS:
            items.append(f'script = {animation}')
        return SINGLE_DIVIDER.join(items)


class MaleVoice(Voice):
    COMM_ANIMATIONS = [
        'SC_MLHEAD_MOTION_WALLA_CASL_000LV_XA_%',
        'SC_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07',
    ]


class FemaleVoice(Voice):
    COMM_ANIMATIONS = [
        'SC_FMHEAD_MOTION_WALLA_CASL_000LV_XA_%',
        'SC_FMBODY_CHRB_IDLE_SMALL_000LV_XA_05',
    ]


class TrentVoice(Voice):
    COMM_ANIMATIONS = [
        'Sc_dx_GCS_W04aP01_Trent',
        'SC_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07',
    ]
