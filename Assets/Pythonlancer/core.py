from managers.audio import AudioManager
from managers.misc_equip import MiscEquipManager
from managers.weapon import WeaponManager
from managers.population import PopulationManager
from managers.shiparch import ShiparchManager
from managers.universe import UniverseManager


INITIAL_EQUIP_STRING_ID = 280000
INITIAL_EQUIP_INFOCARD_ID = 286000

INITIAL_SHIP_STRING_ID = 263000
INITIAL_SHIP_INFOCARD_ID = 110000


class LancerCore(object):

    def __init__(self, enable_story=True):
        # world and universe
        self.misc_equip = MiscEquipManager(INITIAL_EQUIP_STRING_ID, INITIAL_EQUIP_INFOCARD_ID)
        self.weapons = WeaponManager(self.misc_equip.last_string_id, self.misc_equip.last_infocard_id)
        self.shiparch = ShiparchManager(self.misc_equip, INITIAL_SHIP_STRING_ID, INITIAL_SHIP_INFOCARD_ID)
        self.population = PopulationManager(self.misc_equip, self.weapons, self.shiparch)
        self.universe = UniverseManager(self.misc_equip, self.weapons, self.shiparch)

        self.enable_story = enable_story

        if self.has_story:
            self.audio = AudioManager()

    @property
    def has_story(self):
        return self.enable_story
    
