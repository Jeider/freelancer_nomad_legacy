import random

from templates.solar.base_solar import MineableSolar

GLYPH1 = 1
GLYPH2 = 2
GLYPH3 = 3
GLYPH4 = 4
GLYPH5 = 5
GLYPH6 = 6


class DysonRubic(MineableSolar):
    ALIAS = 'dyson_rubic'

    VALID_ARCHETYPE_TEMPLATE = 'dyson_rubic_valid_glyph0{d}'
    INVALID_ARCHETYPE_TEMPLATE = 'dyson_rubic_invalid_glyph0{d}'

    MAIN_LOADOUT_ITEMS = [
        'equip = attached_domkavash_generator, HpGen01',
        'equip = attached_domkavash_generator, HpGen02',
        'equip = beast_gen_light, HpGen01, 1',
        'equip = beast_gen_light, HpGen02, 2',
    ]

    def __init__(self):
        self.hardpoints = []
        self.glyph = GLYPH1

    def set_glyph(self, glyph):
        self.glyph = glyph

    def get_hardpoints(self):
        return self.hardpoints

    def get_init_loadout_items(self):
        return self.MAIN_LOADOUT_ITEMS

    def get_default_archetype(self):
        return self.INVALID_ARCHETYPE_TEMPLATE.format(d=self.glyph)

    def get_medium_reward_archetype(self):
        return self.get_default_archetype()

    def get_high_reward_archetype(self):
        return self.get_default_archetype()

    def get_ultra_reward_archetype(self):
        return self.VALID_ARCHETYPE_TEMPLATE.format(d=self.glyph)
