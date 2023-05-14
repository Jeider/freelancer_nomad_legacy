from world.equipment import MainMiscEquip, Equipment


class Power(MainMiscEquip):

    MAX_POWER_ELITE = 12000
    MAX_REGEN = 1200

    BASE_THRUST_CAPACITY = 1000
    BASE_THRUST_REGEN = 100

    POWER_MAX_HIT_PTS = 8000


DA_archetype = equipment\models\st\rh_radiation_shield.3db
material_library = equipment\models\rh_equip.mat

DA_archetype = equipment\models\st\li_disruptor_shield.3db
material_library = equipment\models\li_equip.mat

DA_archetype = equipment\models\st\br_conversion_shield.3db
material_library = equipment\models\br_equip.mat

DA_archetype = equipment\models\st\ku_displacement_shield.3db
material_library = equipment\models\ku_equip.mat

DA_archetype = equipment\models\st\li_refractor_shield.3db
material_library = equipment\models\li_equip.mat



[ShieldGenerator]
nickname = rh_shield01_ELITE
ids_name = 263870
ids_info = 273696
HP_child = HpConnect
explosion_resistance = 0.25
debris_type = debris_normal
parent_impulse = 20
child_impulse = 80
volume = 0
mass = 5
toughness = 10
hp_type = hp_elite_shield_special_1
shield_type = S_rh_elite
shield_collapse_sound = shield_offline
shield_rebuilt_sound = shield_rebuilt
shield_hit_effects = 0, gf_rh_shield01
shield_hit_effects = 200, gf_rh_shield02
shield_hit_effects = 500, gf_rh_shield03
shield_collapse_particle = rh_shield_offline
separation_explosion = sever_debris
LODranges = 0, 600
lootable = false
offline_rebuild_time = 10
offline_threshold = 0.15
hit_pts = 3000
max_capacity = 649.6875
regeneration_rate = 15.75
rebuild_power_draw = 27.72
constant_power_draw = 16.8



[ShieldGenerator]
nickname = li_shield01_ELITE
ids_name = 263897
ids_info = 273674
HP_child = HpConnect
explosion_resistance = 0.25
debris_type = debris_normal
parent_impulse = 20
child_impulse = 80
volume = 0
mass = 5
toughness = 10
shield_type = S_li_elite
shield_collapse_sound = shield_offline
shield_rebuilt_sound = shield_rebuilt
shield_hit_effects = 0, gf_li_shield01
shield_hit_effects = 200, gf_li_shield02
shield_hit_effects = 500, gf_li_shield03
separation_explosion = sever_debris
shield_collapse_particle = li_shield_offline
LODranges = 0, 600
lootable = false
offline_rebuild_time = 10
offline_threshold = 0.15
hit_pts = 3000
hp_type = hp_elite_shield_special_1
max_capacity = 590.625
regeneration_rate = 15.75
rebuild_power_draw = 18.9
constant_power_draw = 16.8

[ShieldGenerator]
nickname = br_shield01_ELITE
ids_name = 263924
ids_info = 273674
HP_child = HpConnect
explosion_resistance = 0.25
debris_type = debris_normal
parent_impulse = 20
child_impulse = 80
volume = 0
mass = 5
toughness = 10
shield_type = S_br_elite
shield_collapse_sound = shield_offline
shield_rebuilt_sound = shield_rebuilt
shield_hit_effects = 0, gf_br_shield01
shield_hit_effects = 200, gf_br_shield02
shield_hit_effects = 500, gf_br_shield03
separation_explosion = sever_debris
shield_collapse_particle = br_shield_offline
LODranges = 0, 600
lootable = false
offline_rebuild_time = 8
offline_threshold = 0.15
hit_pts = 3000
hp_type = hp_elite_shield_special_1
max_capacity = 590.625
regeneration_rate = 15.75
rebuild_power_draw = 25.2
constant_power_draw = 16.8


[ShieldGenerator]
nickname = ku_shield01_ELITE
ids_name = 263951
ids_info = 273674
HP_child = HpConnect
explosion_resistance = 0.25
debris_type = debris_normal
parent_impulse = 20
child_impulse = 80
volume = 0
mass = 5
toughness = 10
shield_type = S_ku_elite
shield_collapse_sound = shield_offline
shield_rebuilt_sound = shield_rebuilt
shield_hit_effects = 0, gf_ku_shield01
shield_hit_effects = 200, gf_ku_shield02
shield_hit_effects = 500, gf_ku_shield03
separation_explosion = sever_debris
shield_collapse_particle = ku_shield_offline
LODranges = 0, 600
lootable = false
offline_rebuild_time = 10
offline_threshold = 0.15
hit_pts = 3000
hp_type = hp_elite_shield_special_1
max_capacity = 590.625
regeneration_rate = 17.325
rebuild_power_draw = 25.2
constant_power_draw = 21

[ShieldGenerator]
nickname = co_shield01_ELITE
ids_name = 263978
ids_info = 273674
HP_child = HpConnect
explosion_resistance = 0.25
debris_type = debris_normal
parent_impulse = 20
child_impulse = 80
volume = 0
mass = 5
toughness = 10
shield_type = S_co_elite
shield_collapse_sound = shield_offline
shield_rebuilt_sound = shield_rebuilt
shield_hit_effects = 0, gf_pi_shield01
shield_hit_effects = 200, gf_pi_shield02
shield_hit_effects = 500, gf_pi_shield03
separation_explosion = sever_debris
shield_collapse_particle = co_shield_offline
LODranges = 0, 600
lootable = false
offline_rebuild_time = 10
offline_threshold = 0.15
hit_pts = 3000
hp_type = hp_elite_shield_special_1
max_capacity = 561.09375
regeneration_rate = 14.9625
rebuild_power_draw = 25.2
constant_power_draw = 10.08