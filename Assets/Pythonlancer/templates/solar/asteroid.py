import random

from text.dividers import DIVIDER
from templates.solar.base_solar import MineableSolar


FUSE_TEMPLATE = '''[fuse]
name = {fuse_main_name}{index:02d}
lifetime = 0.100000
death_fuse = true

[destroy_hp_attachment]
at_t = 0.0
hardpoint = HpFX{index:02d}
fate = debris

[destroy_group]
at_t = 0.000000
group_name = ast{index:02d}_lod1
fate = disappear
'''


COLLISION_TEMPLATE = '''[CollisionGroup]
obj = ast{index:02d}_lod1
separable = true
child_impulse = 1.000000
parent_impulse = 60.000000
debris_type = debris_vanish
fuse = {fuse_name}{index:02d}, 0.000000, 1
explosion_resistance = 0.0001
hit_pts = 10000
root_health_proxy = false
'''

HARDPOINT_NAME_TEMPLATE = 'HpFX{index:02d}'

FUSE_MAIN = 'xast_dmg_ast'

CHUNKS = 10

INIT_ITEMS_TEMPLATE = 'equip = attached_xast_exploder, {hp}'


class AsteroidSolar(MineableSolar):
    ALIAS = 'asteroid'

    DEFAULT_ARCHETYPE = None
    ARCHETYPE_REWARD_MEDIUM = None
    ARCHETYPE_REWARD_HIGH = None
    ARCHETYPE_REWARD_ULTRA = None

    def __init__(self):
        self.collis = []
        self.fuses = []
        self.hardpoints = []
        for i in range(1, CHUNKS+1):
            self.collis.append(COLLISION_TEMPLATE.format(fuse_name=FUSE_MAIN, index=i))
            self.fuses.append(FUSE_TEMPLATE.format(fuse_main_name=FUSE_MAIN, index=i))
            self.hardpoints.append(HARDPOINT_NAME_TEMPLATE.format(index=i))
        self.init_loadout_items = [INIT_ITEMS_TEMPLATE.format(hp=hp) for hp in self.hardpoints]

    def get_collisions_string(self):
        return DIVIDER.join(self.collis)

    def get_fuses_string(self):
        return DIVIDER.join(self.fuses)

    def get_hardpoints(self):
        return self.hardpoints

    def get_init_loadout_items(self):
        return self.init_loadout_items



class AsteroidOmega15(AsteroidSolar, MineableSolar):
    DEFAULT_ARCHETYPE = 'om15_mineast_super'
    ARCHETYPE_REWARD_MEDIUM = 'om15_mineast_super_medium'
    ARCHETYPE_REWARD_HIGH = 'om15_mineast_super_high'
    ARCHETYPE_REWARD_ULTRA = 'om15_mineast_super_ultra'

    def get_default_archetype(self):
        return self.DEFAULT_ARCHETYPE

    def get_medium_reward_archetype(self):
        return self.ARCHETYPE_REWARD_MEDIUM

    def get_high_reward_archetype(self):
        return self.ARCHETYPE_REWARD_HIGH

    def get_ultra_reward_archetype(self):
        return self.ARCHETYPE_REWARD_ULTRA




# AsteroidTagaki
# AsteroidTau37
# AsteroidCalifornia
# AsteroidCuracao
# AsteroidLava
