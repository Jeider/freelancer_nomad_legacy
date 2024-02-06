import random

from text.dividers import DIVIDER


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

EXPLODER_EQUIP = 'attached_xast_exploder'


class AsteroidSolar(object):
    def __init__(self):
        collis = []
        fuses = []
        hardpoints = []
        for i in range(1, CHUNKS+1):
            collis.append(COLLISION_TEMPLATE.format(fuse_name=fuse_name, index=i))
            fuses.append(FUSE_TEMPLATE.format(fuse_main_name=FUSE_MAIN, index=i))
            hardpoints.append(HARDPOINT_NAME_TEMPLATE.format(index=i))

    def get_collisions_string(self):
        return DIVIDER.join(self.collis)

    def get_fuses_string(self):
        return DIVIDER.join(self.fuses)

    def get_hardpoints(self):
        return self.hardpoints


class AsteroidOmega15(AsteroidSolar):
    DEFAULT_ARCHETYPE = 'om15_mineast_super'
    MEDIUM_REWARD_ARCHETYPE = 'om15_mineast_super_medium'
    HIGH_REWARD_ARCHETYPE = 'om15_mineast_super_huge'
    ULTRA_REWARD_ARCHETYPE = 'om15_mineast_super_ultra'


# AsteroidTagaki
# AsteroidTau37
# AsteroidCalifornia
# AsteroidCuracao
# AsteroidLava
