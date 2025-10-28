from universe.audio.base_pilot import PilotVoice
from universe.audio.pilot_line import PilotLine as L
from universe.audio.parse_rule import RuleNNVoice, RuleNNVoiceHigh, RuleNNVoiceFast, RuleNNVoiceXFast, RuleNNVoiceSlow


class NNVoiceEng(PilotVoice):
    LINES = [

        L('mod_got_key_roid_miner', 'Key for Roid Miner is acquired', RuleNNVoice),
        L('mod_got_key_station', 'Key for Station is acquired', RuleNNVoice),
        L('mod_got_key_factory', 'Key for Factory is acquired', RuleNNVoice),
        L('mod_got_key_asteroid', 'Key for Asteroid is acquired', RuleNNVoice),
        L('mod_got_key_gas_miner', 'Key for Gas Miner is acquired', RuleNNVoice),
        L('mod_got_key_battleship', 'Key for Battleship is acquired', RuleNNVoice),

        L('mod_have_key_roid_miner', 'This asteroid contains key', RuleNNVoice),
        L('mod_have_key_factory', 'This debris bricket contains key for factory', RuleNNVoice),
        L('mod_have_key_asteroid', 'This asteroid contains key', RuleNNVoice),
        L('mod_have_key_gas_miner', 'This ice asteroid contains key', RuleNNVoice),

        L('mod_xenos_fail_timeout', 'You was detected by far scanner', RuleNNVoice),
        L('mod_xenos_fail_patrol', 'You was detected by patrol', RuleNNVoice),

        L('mod_xenos_enter_gas', 'Entering into cloud', RuleNNVoice),
        L('mod_xenos_exit_gas', 'Leaving out from cloud', RuleNNVoice),

        L('mod_hacker_color00', 'Maximal', RuleNNVoiceXFast),
        L('mod_hacker_color01', 'Very high', RuleNNVoiceXFast),
        L('mod_hacker_color02', 'High', RuleNNVoiceFast),
        L('mod_hacker_color03', 'Medium', RuleNNVoice),
        L('mod_hacker_color04', 'Low', RuleNNVoice),
        L('mod_hacker_color05', 'Very low', RuleNNVoice),
        L('mod_hacker_color06', 'Minimal', RuleNNVoice),
        L('mod_hacker_destroy', 'Attack blocks by your weapons. After hit block will say his position relatively to maximal block. Find block marked as maximal. Destroy all blocks with such color', RuleNNVoice),

        L('mod_cloak_patrol', 'Patrol is near', RuleNNVoice),
        L('mod_hacked_complete', 'Panel is hacked out', RuleNNVoice),
        L('mod_door_hacked', 'Door of station is hacked and locked', RuleNNVoice),
    ]
    # STEOS_ID = 549  # Atomic Heart, Filatova
    STEOS_ID = 219  # Witcher, Yennifer
    FOLDER = 'nnvoice_eng'









