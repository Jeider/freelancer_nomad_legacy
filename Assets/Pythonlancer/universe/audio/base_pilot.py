from universe.audio.pilot_line import PilotLine as L
from universe.audio import parse_rule as R

from audio.sound import SpaceSound
from audio.voice import Voice

from text.dividers import DIVIDER

SCREAM_TEMPLATE = 'gcs_combat_scream_0{digit}-'
FORMATION_TEMPLATE = 'gcs_refer_formationdesig_{digit:02d}'
NUMBER_START_TEMPLATE = 'gcs_misc_number_{digit}'
NUMBER_END_TEMPLATE = 'gcs_misc_number_{digit}-'
TEMP_FORMATION_TEMPLATE = 'formation_{digit}'
TEMP_NUMBER_TEMPLATE = 'number_{digit}'

FORMATIONS = [
    (1, '+альфа'),
    (2, 'б+эта'),
    (3, 'г+амма'),
    (4, 'д+ельта'),
    (5, '+эпсилон'),
    (6, 'з+ета'),
    (7, 'т+ета'),
    (8, 'й+ота'),
    (9, 'к+аппа'),
    (10, 'л+ямбда'),
    (11, 'омикр+он'),
    (12, 'с+игма'),
    (13, 'ом+ега'),
    (14, 'кр+асный'),
    (15, 'с+иний'),
    (16, 'золот+ой'),
    (17, 'зел+ёный'),
    (18, 'сер+ебрянный'),
    (19, 'ч+ерный'),
    (20, 'б+елый'),
    (21, 'ж+елтый'),
    (22, 'м+атсу'),
    (23, 'с+акура'),
    (24, 'ф+удзи'),
    (25, 'бот+ан'),
    (26, 'х+аги'),
    (27, 'суз+уки'),
    (28, 'к+ику'),
    (29, 'ян+аги'),
]

NUMBERS = [
    (0, 'ноль'),
    (1, 'один'),
    (2, 'два'),
    (3, 'три'),
    (4, 'четыре'),
    (5, 'пять'),
    (6, 'шесть'),
    (7, 'семь'),
    (8, 'восемь'),
    (9, 'девять'),
    (10, 'десять'),
    (11, 'од+иннадцать'),
    (12, 'двен+адцать'),
    (13, 'трин+адцать'),
    (14, 'чет+ырнадцать'),
    (15, 'пятн+адцать'),
    (16, 'шестн+адцать'),
    (17, 'семн+адцать'),
    (18, 'восемн+адцать'),
    (19, 'девятн+адцать'),
    (20, 'дв+адцать'),
]

VOICE_ROOT = '''
[Voice]
nickname = {nickname}
{animations}

{lines}
'''

MALE_ANIMATIONS = '''
script = SC_MLHEAD_MOTION_WALLA_CASL_000LV_XA_%
script = SC_MLBODY_CHRB_IDLE_SMALL_000LV_XA_07
'''

FEMALE_ANIMATIONS = '''
script = SC_FMHEAD_MOTION_WALLA_CASL_000LV_XA_%
script = SC_FMBODY_CHRB_IDLE_SMALL_000LV_XA_05
'''


class PilotVoice:
    STEOS_ID = None
    FOLDER = None
    STATIC_KIND = None
    LINES = []
    IS_MALE = True
    VOICE_DATA = None
    MVOICE_AUDIO_PROP = None
    MVOICE_MISSION_PROP = None
    ATTENUATION = -6
    ENABLED = True

    def get_lines(self):
        return self.LINES

    def get_dynamic_lines(self):
        return []

    def get_sounds(self):
        lines = self.get_lines()
        sounds = []
        for line in lines:
            sounds.append(
                SpaceSound(
                    name=line.get_code(),
                    line=line.get_text(),
                )
            )
        return sounds

    def get_voice(self):
        return Voice(
            voice_name=self.FOLDER,
            sounds=self.get_sounds(),
        )

    def get_gender(self):
        return 'male' if self.IS_MALE else 'female'

    def get_nickname(self):
        return self.FOLDER

    def get_voice_ini(self):
        animations = (
            MALE_ANIMATIONS
            if self.IS_MALE
            else FEMALE_ANIMATIONS
        )
        attenuation = f'attenuation = {self.ATTENUATION}'
        voice_root = VOICE_ROOT.format(
            nickname=self.get_nickname(),
            animations=animations,
            lines=self.VOICE_DATA.format(
                attenuation=f'attenuation = {self.ATTENUATION}',
            )
        )
        voice_root += DIVIDER + DIVIDER.join(
            [line.get_sound(attenuation=attenuation) for line in self.get_dynamic_lines()]
        )
        return voice_root

    def get_voice_props_ini(self):
        return self.MVOICE_AUDIO_PROP.format(
            nickname=self.get_nickname(),
            gender=self.get_gender(),
        )

    def get_mission_props_ini(self):
        return self.MVOICE_MISSION_PROP.format(
            nickname=self.get_nickname(),
        )


class SignedVoice(PilotVoice):

    def __init__(self, core, *args, **kwargs):
        # core mandatory to access ingame data
        self.core = core
        super().__init__(*args, **kwargs)

    def get_number_lines(self):
        lines = []
        for digit, text in NUMBERS:
            lines.append(
                L(
                    code=NUMBER_START_TEMPLATE.format(digit=digit),
                    ru_text=text,
                    parse_rule=R.RuleNumberFirst
                )
            )
            lines.append(
                L(
                    code=NUMBER_END_TEMPLATE.format(digit=digit),
                    ru_text=text,
                    parse_rule=R.RuleNumberSecond
                )
            )
        return lines

    def get_formation_lines(self):
        lines = []
        for digit, text in FORMATIONS:
            lines.append(
                L(
                    code=FORMATION_TEMPLATE.format(digit=digit),
                    ru_text=text,
                    parse_rule=R.RuleFormation
                )
            )
        return lines

    def get_lines(self):
        lines = super().get_lines()
        lines.extend(self.get_number_lines() + self.get_formation_lines())
        return lines


class BaseIdentifiedVoice(SignedVoice):

    def get_bases_lines(self):
        lines = []

        for base in self.core.universe.get_bases():
            lines.append(
                L(
                    code=base.get_base_msg_relative(),
                    ru_text=base.get_ru_name(),
                    parse_rule=R.RuleBase
                )
            )
        return lines

    def get_lines(self):
        lines = super().get_lines()
        lines.extend(self.get_bases_lines())
        return lines


class SystemIdentifiedVoice(BaseIdentifiedVoice):
    def get_system_lines(self):
        lines = []
        for sys in self.core.universe.universe_root.get_all_systems():
            if sys.IS_STORY:
                continue
            lines.append(
                L(
                    code=sys.get_system_msg_relative(),
                    ru_text=sys.RU_NAME,
                    parse_rule=R.RuleSystem
                )
            )

        for comm in self.core.store.get_commodities():
            lines.append(
                L(
                    code=comm.get_msg_id_prefix(),
                    ru_text=comm.get_name_rel1(),
                    parse_rule=R.RuleCommodity
                )
            )

        return lines

    def get_dynamic_lines(self):
        lines = super().get_lines()
        lines.extend(self.get_system_lines())
        return lines

    def get_lines(self):
        lines = super().get_lines()
        lines.extend(self.get_system_lines())
        return lines
