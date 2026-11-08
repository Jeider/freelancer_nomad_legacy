"""Per-line delivery for VoiceLine.

Pass one of these constants as VoiceLine(..., delivery=LIGHT).

omnivoice applies only the instruct tags below: whisper, age, pitch.
One tag per category. LIGHT is young adult + high pitch.
Freeform emotion strings are rejected, so HAPPY/ANGRY/... stay reserved
for IndexTTS and are ignored by omnivoice.
"""


class Delivery(object):
    def __init__(self, code, instruct=None, emo_text=None, speed=None):
        self.code = code
        self.instruct = instruct
        self.emo_text = emo_text
        self.speed = speed


NEUTRAL = Delivery('neutral')

# Applied by omnivoice instruct.
WHISPER = Delivery('whisper', instruct='whisper', emo_text='whisper')

CHILD = Delivery('child', instruct='child')
TEENAGER = Delivery('teenager', instruct='teenager')
YOUNG_ADULT = Delivery('young_adult', instruct='young adult')
MIDDLE_AGED = Delivery('middle_aged', instruct='middle-aged')
ELDERLY = Delivery('elderly', instruct='elderly')

VERY_LOW_PITCH = Delivery('very_low_pitch', instruct='very low pitch')
LOW_PITCH = Delivery('low_pitch', instruct='low pitch')
MODERATE_PITCH = Delivery('moderate_pitch', instruct='moderate pitch')
HIGH_PITCH = Delivery('high_pitch', instruct='high pitch')
TEENAGER_HIGH_PITCH = Delivery('teenager_high_pitch', instruct='teenager, high pitch')
VERY_HIGH_PITCH = Delivery('very_high_pitch', instruct='very high pitch')
VERY_HIGH_PITCH_SLOW = Delivery('very_high_pitch_slow', instruct='very high pitch', speed=0.85)

LIGHT = Delivery('light', instruct='young adult, high pitch')
LIGHTER = Delivery('lighter', instruct='teenager, very high pitch')

# Reserved. IndexTTS emo_text / emo vector. omnivoice does not apply these.
HAPPY = Delivery('happy', emo_text='happy')
ANGRY = Delivery('angry', emo_text='angry')
SAD = Delivery('sad', emo_text='sad')
AFRAID = Delivery('afraid', emo_text='afraid')
DISGUSTED = Delivery('disgusted', emo_text='disgusted')
MELANCHOLIC = Delivery('melancholic', emo_text='melancholic')
SURPRISED = Delivery('surprised', emo_text='surprised')
CALM = Delivery('calm', emo_text='calm')

# Reserved freeform character. Same rule: IndexTTS only, until the engine changes.
URGENT = Delivery('urgent', emo_text='urgent')
TIRED = Delivery('tired', emo_text='tired')
SARCASTIC = Delivery('sarcastic', emo_text='sarcastic')
SHOUTING = Delivery('shouting', emo_text='shouting')
