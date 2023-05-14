class Gun(Equipment):
    # MUNITION
    HULL_DAMAGE = 245
    ENERGY_DAMAGE = 0
    WEAPON_TYPE = ''
    ONE_SHOT_SOUND = ''
    MUNITION_HIT_EFFECT = ''
    CONST_EFFECT = ''
    LIFETIME = 1
    VOLUME = 0

    # GUN
    HIT_PTS = 500
    IDS_NAME = ''
    IDS_INFO = ''
    DA_ARCHETYPE = ''
    MATERIAL_LIBRARY = ''
    EXPLOSION_RESISTANCE = 0.25
    TOUGHNESS = 0

    REFIRE_X10 = 10
    REFIRE_X8 = 8
    REFIRE_X6 = 6
    REFIRE_X4 = 4
    REFIRE_X3 = 3
    REFIRE_X2 = 2
    REFIRE_X1 = 1





    def __init__(self,
                 one_shot_sound, munition_hit_effect, const_effect, flash_particle_name, tractored_explosion,
                 weapon_type, da_archetype, material_library, lod_ranges,
                 refire_type, muzzle_cone_angle):
        pass
