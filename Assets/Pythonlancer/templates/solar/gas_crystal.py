import random

from templates.solar.base_solar import MineableSolar


class BaseIceCrystal(MineableSolar):
    ALIAS = 'ice_crystal'

    ASTEROID_TEMPLATE = '''[Object]
nickname = {nickname}_ast01
pos = {asteroid_pos}
rotate = {asteroid_rotate}
archetype = {asteroid_archetype}
visit = 128'''

    ASTEROID_POS = (0, 0, 0)
    ASTEROID_ROTATE = (0, 0, 0)

    INNER_GAS_TEMPLATE = '''[Object]
nickname = {nickname}_inner_{gas_index}
pos = {gas_pos}
rotate = 0, 0, 0
archetype = sig13_mineable_gas_static
loadout = {gas_loadout}
visit = 128'''

    GAS_POSITIONS = []

    INIT_LOADOUT_ITEMS = [
        'equip = infinite_power',
        'equip = gas_puff_shield_static, HpShield01', 
        'equip = attached_gas_connect, HpRoot',
        'equip = fx_puff_crow_small, HpGas01',
    ]

    def get_init_loadout_items(self):
        return self.INIT_LOADOUT_ITEMS

    def get_asteroid_pos(self):
        raise NotImplementedError

    def get_asteroid_rot(self):
        raise NotImplementedError

    def get_gas_positions(self):
        raise NotImplementedError

    def get_asteroid(self, nickname, box_pos, asteroid_archetype):
        asteroid_pos = self.get_asteroid_pos()
        asteroid_rot = self.get_asteroid_rot()
        pos_x = box_pos[0] + asteroid_pos[0]
        pos_y = box_pos[1] + asteroid_pos[1]
        pos_z = box_pos[2] + asteroid_pos[2]
        return self.ASTEROID_TEMPLATE.format(
            nickname=nickname,
            asteroid_pos='{}, {}, {}'.format(pos_x, pos_y, pos_z),
            asteroid_rotate='{}, {}, {}'.format(*asteroid_rot),
            asteroid_archetype=asteroid_archetype,
        )

    def get_inner_gas_item(self, nickname, box_pos, gas_pos, loadout, index):
        pos_x = box_pos[0] + gas_pos[0]
        pos_y = box_pos[1] + gas_pos[1]
        pos_z = box_pos[2] + gas_pos[2]
        return self.INNER_GAS_TEMPLATE.format(
            nickname=nickname,
            gas_pos='{}, {}, {}'.format(pos_x, pos_y, pos_z),
            gas_loadout=loadout,
            gas_index=index,
        )

    def change_template(self):
        # do nothing, override if required
        pass



class SimpleCrystalAsteroid(BaseIceCrystal):
    DEFAULT_ARCHETYPE = 'icecrystal_mineast_super'
    ULTRA_REWARD_ARCHETYPE = 'icecrystal_mineast_super_ultra'

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def get_default_archetype(self):
        return self.DEFAULT_ARCHETYPE

    def get_medium_reward_archetype(self):
        return self.DEFAULT_ARCHETYPE

    def get_high_reward_archetype(self):
        return self.DEFAULT_ARCHETYPE

    def get_ultra_reward_archetype(self):
        return self.ULTRA_REWARD_ARCHETYPE

    def get_asteroid_pos(self):
        return self.template.ASTEROID_POS

    def get_asteroid_rot(self):
        return self.template.ASTEROID_ROTATE

    def get_gas_positions(self):
        return self.template.GAS_POSITIONS

    def change_template(self):
        self.template = random.choice(self.subclasses)


class CrystalTemplate1(SimpleCrystalAsteroid):
    ASTEROID_POS = (0, 0, 0)
    ASTEROID_ROTATE = (0, 0, 0)

    GAS_POSITIONS = [
        (0, 0, 120),
        (0, 0, 0),
        (0, 0, -120),
    ]


class CrystalTemplate2(SimpleCrystalAsteroid):
    ASTEROID_POS = (0, 0, 0)
    ASTEROID_ROTATE = (-34.7, 20.2, 41.3)

    GAS_POSITIONS = [
        (-19.5, 73.7, 92.7),
        (0, 0, 0),
        (19.5, -73.7, -92.7),
    ]


class CrystalTemplate3(SimpleCrystalAsteroid):
    ASTEROID_POS = (0, 0, 0)
    ASTEROID_ROTATE = (-130.3, 45.5, -85.2)

    GAS_POSITIONS = [
        (86.6, 62.9, -54.3),
        (0, 0, 0),
        (-86.6, -62.9, 54.3),
    ]


class CrystalTemplate4(SimpleCrystalAsteroid):
    ASTEROID_POS = (0, 0, 0)
    ASTEROID_ROTATE = (46.2, 46.5, 167.5)

    GAS_POSITIONS = [
        (-40, 97.5, 57.4),
        (0, 0, 0),
        (40, -97.5, -57.4),
    ]


class ComplexCrystalAsteroid(BaseIceCrystal):
    ALIAS = 'complex_ice_crystal'

    DEFAULT_ARCHETYPE = 'ice_asteroid_insane'
    ARCHETYPE_REWARD_MEDIUM = 'ice_asteroid_insane'
    ARCHETYPE_REWARD_HIGH = 'ice_asteroid_insane'
    ARCHETYPE_REWARD_ULTRA = 'ice_asteroid_insane_ultra'

    GAS_POSITIONS =[
        (0, 0, -10),
        (-80, -300, 0),
        (-40, -200, 0),
        (-180, 130, 0),
        (-80, 110, 20),
        (-130, 30, 50),
        (100, 00, 100),
        (40, 100, 130),
        (80, -150, 120),
        (-30, -200, 80),
        (10, -100, -70),
        (-30, 200, 32),
        (-125, 200, 45),
        (-5, 165, -100),
        (50, -30, -180),
        (22, 100, -140),
        (80, -85, 100),
        (90, 150, 95),
        (100, 80, -20),
        (20, -115, 10),
    ]

    def get_asteroid_pos(self):
        return self.ASTEROID_POS

    def get_asteroid_rot(self):
        return self.ASTEROID_ROTATE

    def get_gas_positions(self):
        return self.GAS_POSITIONS

    def get_default_archetype(self):
        return self.DEFAULT_ARCHETYPE

    def get_medium_reward_archetype(self):
        return self.ARCHETYPE_REWARD_MEDIUM

    def get_high_reward_archetype(self):
        return self.ARCHETYPE_REWARD_HIGH

    def get_ultra_reward_archetype(self):
        return self.ARCHETYPE_REWARD_ULTRA
