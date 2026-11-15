"""Per-line delivery for VoiceLine.

omnivoice applies only instruct tags: whisper, age, pitch. One tag per
category. Freeform emotion text is ignored.

IndexTTS 2.5 applies emotion. Those deliveries switch the request to indextts2.
Sliders are an 8-vector, each 0..1, and that is the strong path.
Text emotion uses emo_text plus emo_alpha, and the composer caps that
at 0.6. Do not set both on one delivery: the server rejects the mix.
"""


class Delivery(object):
    def __init__(self, code, instruct=None, emo_text=None, emo_alpha=None, emo_vector=None, speed=None):
        self.code = code
        self.instruct = instruct
        self.emo_text = emo_text
        self.emo_alpha = emo_alpha
        self.emo_vector = emo_vector
        self.speed = speed


NEUTRAL = Delivery('neutral')

# omnivoice instruct.
WHISPER = Delivery('whisper', instruct='whisper')

CHILD = Delivery('child', instruct='child')
TEENAGER = Delivery('teenager', instruct='teenager')
YOUNG_ADULT = Delivery('young_adult', instruct='young adult')
MIDDLE_AGED = Delivery('middle_aged', instruct='middle-aged')
MIDDLE_AGED_SLOW = Delivery('middle_aged_slow', instruct='middle-aged', speed=0.9)
ELDERLY = Delivery('elderly', instruct='elderly')
ELDERLY_SLOW = Delivery('elderly_slow', instruct='elderly', speed=0.7)
ELDERLY_NO_FAST = Delivery('elderly_slow', instruct='elderly', speed=0.9)

VERY_LOW_PITCH = Delivery('very_low_pitch', instruct='very low pitch')
VERY_LOW_PITCH_SLOW = Delivery('very_low_pitch', instruct='very low pitch', speed=0.75)
VERY_LOW_PITCH_NOT_FAST = Delivery('very_low_pitch', instruct='very low pitch', speed=0.85)
LOW_PITCH = Delivery('low_pitch', instruct='low pitch')
LOW_PITCH_SLOW = Delivery('low_pitch', instruct='low pitch', speed=0.75)
LOW_PITCH_NOT_FAST = Delivery('low_pitch', instruct='low pitch', speed=0.85)
LOW_PITCH_FAST = Delivery('low_pitch', instruct='low pitch', speed=1.4)
LOW_PITCH_XFAST = Delivery('low_pitch', instruct='low pitch', speed=1.7)
MODERATE_PITCH = Delivery('moderate_pitch', instruct='moderate pitch')
MODERATE_PITCH_FAST = Delivery('moderate_pitch', instruct='moderate pitch', speed=1.2)
HIGH_PITCH = Delivery('high_pitch', instruct='high pitch')
HIGH_PITCH_SLOW = Delivery('high_pitch', instruct='high pitch', speed=0.8)
HIGH_PITCH_FAST = Delivery('high_pitch', instruct='high pitch', speed=1.2)
HIGH_PITCH_NOT_FAST = Delivery('high_pitch', instruct='high pitch', speed=0.9)
TEENAGER_HIGH_PITCH = Delivery('teenager_high_pitch', instruct='teenager, high pitch')
VERY_HIGH_PITCH = Delivery('very_high_pitch', instruct='very high pitch')
VERY_HIGH_PITCH_SLOW = Delivery('very_high_pitch_slow', instruct='very high pitch', speed=0.85)
VERY_HIGH_PITCH_FAST = Delivery('very_high_pitch_slow', instruct='very high pitch', speed=1.2)
VERY_HIGH_PITCH_SUPER_SLOW = Delivery('very_high_pitch_slow', instruct='very high pitch', speed=0.5)

LIGHT = Delivery('light', instruct='young adult, high pitch')
LIGHTER = Delivery('lighter', instruct='teenager, very high pitch')

# IndexTTS sliders: happy, angry, sad, afraid, disgusted, melancholic, surprised, calm.
def _slider(code, index, weight=1.0):
    vector = [0.0] * 8
    vector[index] = weight
    return Delivery(code, emo_vector=tuple(vector))


HAPPY = _slider('happy', 0)
ANGRY = _slider('angry', 1)
SAD = _slider('sad', 2)
AFRAID = _slider('afraid', 3)
DISGUSTED = _slider('disgusted', 4)
MELANCHOLIC = _slider('melancholic', 5)
SURPRISED = _slider('surprised', 6)
CALM = _slider('calm', 7)

# Slider max. Text emotion cannot go past 0.6, so this is the stronger afraid.
TERRIFIED = _slider('terrified', 3)

# IndexTTS text emotion. Alpha stays at the composer cap.
def _text(code, text, alpha=0.6):
    return Delivery(code, emo_text=text, emo_alpha=alpha)


URGENT = _text('urgent', 'urgent')
TIRED = _text('tired', 'tired')
SARCASTIC = _text('sarcastic', 'sarcastic')
SHOUTING = _text('shouting', 'shouting')
