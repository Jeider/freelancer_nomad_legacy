"""Authored English story emotion presets for VoiceLine(delivery_en=...).

IndexTTS vector order: happy, angry, sad, afraid, disgusted, melancholic,
surprised, calm. No pitch, age, speed or voice identity overrides here.
VoiceLine.get_delivery('en') retains the original actor/line voice settings.
Neutral narration and computer announcements need no marker.

Preset ratios stay as written. EMOTION_SCALE and TEXT_ALPHA make the
rendered hint quiet. These are intentions, not a guarantee of a take.
"""
from audio.delivery import Delivery

# Full slider is 1.0. 0.2 keeps the colour without taking over the voice.
EMOTION_SCALE = 0.2
# Text emotion is capped at 0.6 by the composer. Stay well under that.
TEXT_ALPHA = 0.12


def _vector(code, *, happy=0, angry=0, sad=0, afraid=0, disgusted=0,
            melancholic=0, surprised=0, calm=0):
    return Delivery('story_en_' + code, emo_vector=tuple(
        value * EMOTION_SCALE
        for value in (happy, angry, sad, afraid, disgusted, melancholic, surprised, calm)))


WARM = _vector('warm', happy=.4, calm=.4)
AMUSED = _vector('amused', happy=.7, calm=.1)
REASSURING = _vector('reassuring', happy=.15, calm=.8)
RELIEVED = _vector('relieved', happy=.55, calm=.5)
PROUD = _vector('proud', happy=.6, calm=.25)
EXCITED = _vector('excited', happy=.8, surprised=.35)
UNCERTAIN = _vector('uncertain', afraid=.25, surprised=.4, calm=.15)
CONCERNED = _vector('concerned', sad=.2, afraid=.4, calm=.25)
ALARMED = _vector('alarmed', afraid=.65, surprised=.4)
PANICKED = _vector('panicked', afraid=1, sad=.15)
SHOCKED = _vector('shocked', surprised=.9, afraid=.2)
SURPRISED_HAPPY = _vector('surprised_happy', happy=.3, surprised=.5)
URGENT = _vector('urgent', angry=.4, afraid=.35, calm=.1)
COMMAND = _vector('command', angry=.35, calm=.45)
STERN = _vector('stern', angry=.45, calm=.5)
ANGRY = _vector('angry', angry=.45, disgusted=.5)
FURIOUS = _vector('furious', angry=1, disgusted=.25)
THREATENING = _vector('threatening', angry=.6, calm=.4)
DISGUSTED = _vector('disgusted', disgusted=.8, angry=.25)
SOMBRE = _vector('sombre', sad=.45, melancholic=.5, calm=.15)
GRIEVING = _vector('grieving', sad=.95, melancholic=.25)
REFLECTIVE = _vector('reflective', melancholic=.4, calm=.6)
DETERMINED = _vector('determined', angry=.25, calm=.6)
DRY = _vector('dry', calm=.8)

# Non-basic deliveries use IndexTTS text emotion (the backend caps alpha at .6).
TEASING = Delivery('story_en_teasing', emo_text='playfully teasing, amused and friendly', emo_alpha=TEXT_ALPHA)
SARDONIC = Delivery('story_en_sardonic', emo_text='dry sarcastic irritation, restrained mockery', emo_alpha=TEXT_ALPHA)
WEARY = Delivery('story_en_weary', emo_text='exhausted and frustrated, weary resignation', emo_alpha=TEXT_ALPHA)
