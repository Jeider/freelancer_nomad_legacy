import random


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

FUSE_DROP_TEMPLATE = '''[fuse]
name = {fuse_drop_name}{index:02d}
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


# [dump_cargo]
# at_t = 0.99
# origin_hardpoint = HpFX{index:02d}


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

FUSE_MAIN = 'xast_dmg_ast'
FUSE_DROP = 'xast_dmg_xdrop_ast'

items = 10

out_item = random.randint(1, items-1)

collis = []
fuses = []
fuses_drop = []
for i in range(1, items+1):
    fuse_name = FUSE_DROP if out_item == i else FUSE_MAIN
    collis.append(COLLISION_TEMPLATE.format(fuse_name=fuse_name, index=i))
    fuses.append(FUSE_TEMPLATE.format(fuse_main_name=FUSE_MAIN, index=i))
    fuses_drop.append(FUSE_DROP_TEMPLATE.format(fuse_drop_name=FUSE_DROP, index=i))

# print("\n".join(collis))

print("\n".join(fuses))
print("\n".join(fuses_drop))

