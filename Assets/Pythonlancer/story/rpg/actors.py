"""Voice actors belonging to RPG base dialogue, separate from campaign characters."""
from audio.delivery import NEUTRAL
from story.actors import Actor, ACTOR_MALE
from text.strings import MultiString as MS


class RpgTradeDirector(Actor):
    NAME = 'rpg_trade_director'
    TYPE = ACTOR_MALE
    RU_NAME = MS('Глава торгового управления', 'Trade Authority Director')
    VOICE_DELIVERY = NEUTRAL
    STEOS_SPEED = 1
    # VoiceStudio uses this class name for its own RU/EN reference recordings.
    # No fallback to Hassler or another campaign actor.


class RpgAvalonParkingOfficer(Actor):
    NAME = 'rpg_avalon_parking_officer'
    TYPE = ACTOR_MALE
    RU_NAME = MS('Капитан стоянки Авалона', 'Avalon Parking Captain')
    VOICE_DELIVERY = NEUTRAL
    STEOS_SPEED = 1
    COMM_APPEARANCE = 'br_captain_head, br_male_elite_body'
    # Own reference: Assets/VOICE_SOURCE_EN/RpgAvalonParkingOfficer.wav.
