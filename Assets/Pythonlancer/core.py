from managers.audio import AudioManager
from managers.ids import IDsManager
from managers.misc_equip import MiscEquipManager
from managers.weapon import WeaponManager
from managers.population import PopulationManager
from managers.shiparch import ShiparchManager
from managers.universe import UniverseManager
from managers.story import StoryManager


class LancerCore(object):

    def __init__(self, enable_story=True, write=True, story=True):
        self.write = write

        self.ids = IDsManager(self)
        self.misc_equip = MiscEquipManager(self)
        self.weapons = WeaponManager(self)
        self.shiparch = ShiparchManager(self)
        self.population = PopulationManager(self)
        self.universe = UniverseManager(self)
        self.story = StoryManager(self) if story else None

        self.enable_story = enable_story
        #
        # if self.has_story:
        #     self.audio = AudioManager()

    @property
    def has_story(self):
        return self.enable_story


def get_core():
    return LancerCore(write=False, story=False)
