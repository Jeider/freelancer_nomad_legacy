from managers.ids import IDsManager
from managers.chars import CharacterManager
from managers.misc_equip import MiscEquipManager
from managers.weapon import WeaponManager
from managers.population import PopulationManager
from managers.shiparch import ShiparchManager
from managers.npc_armor import NPCArmorManager
from managers.universe import UniverseManager
from managers.story import StoryManager
from managers.store import StoreManager


class LancerCore(object):

    def __init__(self, write=True, story=True):
        self.write = write

        self.ids = IDsManager(self)
        self.chars = CharacterManager(self)
        self.misc_equip = MiscEquipManager(self)
        self.weapons = WeaponManager(self)
        self.shiparch = ShiparchManager(self)
        self.npc_armor = NPCArmorManager(self)
        self.population = PopulationManager(self)
        self.store = StoreManager(self)
        self.universe = UniverseManager(self)
        self.story = StoryManager(self) if story else None

        self.chars.post_load()


def get_core():
    return LancerCore(write=False, story=False)
