from universe.audio.pilot_line import PilotLine as L
from universe.audio import parse_rule as R
from universe.audio.base_pilot import EnglishBaseIdentifiedVoice
from universe.audio.static import dispatcher as dispatcher_static

from text.strings import MultiString as MS


class EnglishStationDispatcher(EnglishBaseIdentifiedVoice):
    VOICE_DATA = dispatcher_static.VOICE_DATA
    MVOICE_AUDIO_PROP = ''
    MVOICE_MISSION_PROP = ''
    LINES = [
        L('mod_refer_base_liner-','liner', R.RuleBaseNoProcess),
        L('mod_refer_base_roid_miner-', 'Roid Miner', R.RuleBaseNoProcess),
        L('mod_refer_base_gas_miner-', 'Gas Miner', R.RuleBaseNoProcess),
        L('mod_refer_base_solar_plant-', 'Solar Plant', R.RuleBaseNoProcess),
        L('mod_refer_base_research_base-', 'Research Base', R.RuleBaseNoProcess),
        L('mod_refer_base_battleship-', 'Battleship', R.RuleBaseNoProcess),
        L('mod_refer_base_freeport-', 'Freeport', R.RuleBaseNoProcess),
        L('mod_refer_base_prison-', 'Prison', R.RuleBaseNoProcess),
        L('mod_refer_base_outpost-', 'Outpost', R.RuleBaseNoProcess),
        L('mod_refer_base_research-', 'Research', R.RuleBaseNoProcess),
        L('mod_refer_base_shipyard-', 'Shipyard', R.RuleBaseNoProcess),
        L('mod_refer_base_factory-', 'Factory', R.RuleBaseNoProcess),
        L('mod_refer_base_station-', 'Station', R.RuleBaseNoProcess),
        L('mod_refer_base_border-', 'Border Station', R.RuleBaseNoProcess),
    ]

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)


class EngMaleDispatcher(EnglishStationDispatcher):
    STEOS_ID = 294  # lebedev, stalker
    FOLDER = 'dispatcher_en01'
    ATTENUATION = -4


class EngFemaleDispatcher(EnglishStationDispatcher):
    STEOS_ID = 175  # Tracer ?
    FOLDER = 'dispatcher_en02'
    IS_MALE = False
    ATTENUATION = -4


class EngFemaleRoboDispatcher(EnglishStationDispatcher):
    STEOS_ID = 175  # Tracer ?
    FOLDER = 'dispatcher_en03'
    IS_MALE = False
    ATTENUATION = -4
