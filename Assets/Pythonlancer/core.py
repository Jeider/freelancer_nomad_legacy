from managers.audio import AudioManager
from managers.misc_equip import MiscEquipManager
from managers.weapon import WeaponManager
from managers.population import PopulationManager
from managers.shiparch import ShiparchManager
from managers.universe import UniverseManager
from managers.story import StoryManager


INITIAL_EQUIP_STRING_ID = 280000
INITIAL_EQUIP_INFOCARD_ID = 286000

INITIAL_SHIP_STRING_ID = 263000
INITIAL_SHIP_INFOCARD_ID = 110000


class LancerCore(object):

    def __init__(self, enable_story=True, write=True):
        self.write = write

        self.last_equip_string_id = INITIAL_EQUIP_STRING_ID
        self.last_equip_infocard_id = INITIAL_EQUIP_INFOCARD_ID
        self.last_ship_string_id = INITIAL_SHIP_STRING_ID
        self.last_ship_infocard_id = INITIAL_SHIP_INFOCARD_ID

        self.misc_equip = MiscEquipManager(self)
        self.weapons = WeaponManager(self)
        self.shiparch = ShiparchManager(self)
        self.population = PopulationManager(self)
        self.universe = UniverseManager(self)
        self.story = StoryManager(self)

        self.enable_story = enable_story
        #
        # if self.has_story:
        #     self.audio = AudioManager()

    def get_next_equip_string_id(self):
        self.last_equip_string_id += 1
        return self.last_equip_string_id

    def get_next_equip_infocard_id(self):
        self.last_equip_infocard_id += 1
        return self.last_equip_infocard_id

    def get_next_ship_string_id(self):
        self.last_ship_string_id += 1
        return self.last_ship_string_id

    def get_next_ship_infocard_id(self):
        self.last_ship_infocard_id += 1
        return self.last_ship_infocard_id

    @property
    def has_story(self):
        return self.enable_story
