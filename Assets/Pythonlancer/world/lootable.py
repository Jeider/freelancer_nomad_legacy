class Lootable(object):
    DROP_CHANCE = None
    DROP_MIN_WORTH = None
    DROP_WORTH_MULT = None
    DROP_MIN = None
    DROP_MAX1 = None
    DROP_MAX2 = None

    LOOTPROP_TEMPLATE = '''[mLootProps]
nickname = {nickname}
drop_properties = {chance}, {min_worth}, {worth_mult}, {min}, {max1}, {max2}
'''

    def get_drop_chance(self):
        if self.DROP_CHANCE is None:
            raise NotImplementedError('DROP_CHANCE not defined')
        return self.DROP_CHANCE

    def get_drop_min_worth(self):
        if self.DROP_MIN_WORTH is None:
            raise NotImplementedError('DROP_MIN_WORTH not defined')
        return self.DROP_MIN_WORTH

    def get_drop_worth_mult(self):
        if self.DROP_WORTH_MULT is None:
            raise NotImplementedError('DROP_WORTH_MULT not defined')
        return self.DROP_WORTH_MULT

    def get_drop_min(self):
        if self.DROP_MIN is None:
            raise NotImplementedError('DROP_MIN not defined')
        return self.DROP_MIN

    def get_drop_max1(self):
        if self.DROP_MAX1 is None:
            raise NotImplementedError('DROP_MAX1 not defined')
        return self.DROP_MAX1

    def get_drop_max2(self):
        if self.DROP_MAX2 is None:
            raise NotImplementedError('DROP_MAX2 not defined')
        return self.DROP_MAX2

    def get_lootprops_template_params(self):
        return {
            'nickname': self.get_nickname(),
            'chance': self.get_drop_chance(),
            'min_worth': self.get_drop_min_worth(),
            'worth_mult': self.get_drop_worth_mult(),
            'min': self.get_drop_min(),
            'max1': self.get_drop_max1(),
            'max2': self.get_drop_max2(),
        }

    def get_lootprops(self):
        return self.LOOTPROP_TEMPLATE.format(**self.get_lootprops_template_params())


class LootableEquip(Lootable):
    DROP_CHANCE = 5
    DROP_MIN = 0
    DROP_MAX1 = 2
    DROP_MAX2 = 0


class LootableAmmo(Lootable):
    DROP_MIN = 0
    DROP_MAX1 = 40
    DROP_MAX2 = 15


class LootableCommodity(Lootable):
    CHANCE = 100
    DROP_MIN = 1
    DROP_MAX1 = 1000
    DROP_MAX2 = 1000


class LootableRepair(Lootable):
    CHANCE = 33
    DROP_MIN = 0
    DROP_MAX1 = 1000
    DROP_MAX2 = 1000
