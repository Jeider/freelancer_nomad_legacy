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

import universe.content.planet_info_ru as PLANET_RU
import universe.content.planet_info_en as PLANET_EN
from text.strings import MultiString as MS


class TemplateManger:

    def __init__(self, lancer_core):
        self.core = lancer_core


class DescriptionPack:
    def __init__(self, ru_infos, en_infos):
        self.last_index = -1
        self.ru_infos = ru_infos
        self.en_infos = en_infos
        if len(self.ru_infos) != len(en_infos):
            raise Exception(f'Desc pack {self} have wrong descriptions count')

    def get_next(self):
        self.last_index += 1
        try:
            return MS(self.ru_infos[self.last_index], self.en_infos[self.last_index])
        except IndexError:
            raise Exception('no descriptions left')
            # self.last_index = 0
            # return self.ru_infos[self.last_index]


class LancerCore(object):

    def __init__(self, difficulty, write=True, story=True, russian=True, build_folder=None):
        self.russian = russian
        self.write = write
        self.build_folder = build_folder
        self.difficulty = difficulty  # mandatory!

        self.descriptions = {
            'planet_ice': DescriptionPack(PLANET_RU.ICE_PLANETS, PLANET_EN.ICE_PLANETS),
            'planet_desert': DescriptionPack(PLANET_RU.DESERT_PLANETS, PLANET_EN.DESERT_PLANETS),
            'planet_gas': DescriptionPack(PLANET_RU.GAS_GIANTS, PLANET_EN.GAS_GIANTS),
            'stars': DescriptionPack(PLANET_RU.STARS, PLANET_EN.STARS),
            'planet_moon': DescriptionPack(PLANET_RU.MOON, PLANET_EN.MOON),
            'planet_lava': DescriptionPack(PLANET_RU.LAVA, PLANET_EN.LAVA),
            'planet_terra': DescriptionPack(PLANET_RU.TERRA, PLANET_EN.TERRA),
        }

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

    def get_next_desc(self, store):
        return self.descriptions[store].get_next()


def get_core():
    return LancerCore(write=False, story=False, difficulty=NormalDifficulty)
