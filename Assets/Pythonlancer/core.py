from difficulty import NormalDifficulty

from managers.ids import IDsManager
from managers.chars import CharacterManager
from managers.misc_equip import MiscEquipManager
from managers.weapon import WeaponManager
from managers.population import PopulationManager
from managers.shiparch import ShiparchManager
from managers.npc_armor import NPCArmorManager
from managers.factions import FactionManager
from managers.universe import UniverseManager
from managers.story import StoryManager
from managers.store import StoreManager
from managers.fx import FxManager

from managers.jinja_manager import JinjaTemplateManager


class TemplateManger:

    def __init__(self, lancer_core):
        self.core = lancer_core


class LancerCore(object):

    def __init__(self, difficulty, write=True, story=True, russian=True, build_folder=None):
        self.russian = russian
        self.write = write
        self.build_folder = build_folder
        self.difficulty = difficulty  # mandatory!

        self.tpl_manager = JinjaTemplateManager()
        self.ids = IDsManager(self)
        self.chars = CharacterManager(self)
        self.misc_equip = MiscEquipManager(self)
        self.weapons = WeaponManager(self)
        self.shiparch = ShiparchManager(self)
        self.npc_armor = NPCArmorManager(self)
        self.factions = FactionManager(self)
        self.population = PopulationManager(self)
        self.store = StoreManager(self)
        self.universe = UniverseManager(self)
        self.story = StoryManager(self) if story else None
        self.fx = FxManager(self)

        self.chars.post_load()


def get_core():
    return LancerCore(write=False, story=False, difficulty=NormalDifficulty)
