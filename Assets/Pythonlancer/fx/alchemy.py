from tools.crc import crc32_minus_from_str

from text.dividers import SINGLE_DIVIDER

EFT_ENGINE_FIRE = 'EFT_ENGINE_FIRE'
EFT_ENGINE_TRAIL = 'EFT_ENGINE_TRAIL'
EFT_ENGINE_THRUSTER = 'EFT_ENGINE_THRUSTER'
EFT_MISSILE_DRIVE = 'EFT_MISSILE_DRIVE'
EFT_EXPLOSION_MISSILE = 'EFT_EXPLOSION_MISSILE'
EFT_EXPLOSION_MINE = 'EFT_EXPLOSION_MINE'
EFT_EXPLOSION_LARGE = 'EFT_EXPLOSION_LARGE'
EFT_WEAPON_MINE = 'EFT_WEAPON_MINE'


class FX:
    TEXTURES = []
    MEMBERS = []
    EFFECT_TYPE = None
    VIS_GENERIC = None
    SOUND = None
    FX_APPEND = ''

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    @classmethod
    def get_members(cls):
        return cls.MEMBERS

    @classmethod
    def get_effect(cls, member):
        if not cls.EFFECT_TYPE:
            raise Exception(f'Wrong configured fx {cls}')

        items = [
            '[Effect]',
            f'nickname = {member}{cls.FX_APPEND}',
            f'effect_type = {cls.EFFECT_TYPE}',
            f'vis_effect = {member}{cls.FX_APPEND}'
        ]
        if cls.VIS_GENERIC:
            items.append(f'vis_generic = {cls.VIS_GENERIC}')
        if cls.SOUND:
            items.append(f'snd_effect = {cls.SOUND}')

        return SINGLE_DIVIDER.join(items)

    @classmethod
    def get_vis_effect(cls, member):
        inside_name = f'{member}{cls.FX_APPEND}'
        items = [
            '[VisEffect]',
            f'nickname = {inside_name}',
            f'alchemy = fx\\generated\\{member}.ale',
            f'effect_crc = {crc32_minus_from_str(inside_name)}'
        ]
        for texture in cls.TEXTURES:
            items.append(f'textures = fx\\{texture}.txm')

        return SINGLE_DIVIDER.join(items)


class GenEngineFire(FX):
    EFFECT_TYPE = EFT_ENGINE_FIRE
    VIS_GENERIC = 'gf_min_smallengine02_fire'
    TEXTURES = ['planetflare']
    MEMBERS = [
        'gf_ci_smallengine02_fire',
        'gf_ci_smallengine03_fire',
        'gf_ci_smallengine04_fire',

        'gf_br_smallengine04_fire',
        'gf_br_smallengine05_fire',
        'gf_br_smallengine06_fire',

        'gf_co_smallengine04_fire',
        'gf_co_smallengine05_fire',
        'gf_co_smallengine06_fire',
    ]


class IonCannonEngineFire(FX):
    EFFECT_TYPE = EFT_ENGINE_FIRE
    VIS_GENERIC = 'gf_min_smallengine02_fire'
    TEXTURES = ['planetflare', 'kioncannon']
    MEMBERS = [
        'gf_li_smallengine04_fire',
        'gf_li_smallengine05_fire',
        'gf_li_smallengine06_fire',
    ]


class SarmaEngineFire(FX):
    EFFECT_TYPE = EFT_ENGINE_FIRE
    VIS_GENERIC = 'gf_min_smallengine02_fire'
    TEXTURES = ['planetflare', 'sarma']
    MEMBERS = [
        'gf_ku_smallengine04_fire',
        'gf_ku_smallengine05_fire',
        'gf_ku_smallengine06_fire',
    ]


class GenEngineTrail(FX):
    EFFECT_TYPE = EFT_ENGINE_TRAIL
    VIS_GENERIC = 'gf_min_smallengine02_trail'
    TEXTURES = ['planetflare', 'sarma', 'beam']
    MEMBERS = [
        'gf_ci_smallengine02_trail',
        'gf_ci_smallengine03_trail',
        'gf_ci_smallengine04_trail',

        'gf_br_smallengine04_trail',
        'gf_br_smallengine05_trail',
        'gf_br_smallengine06_trail',

        'gf_co_smallengine04_trail',
        'gf_co_smallengine05_trail',
        'gf_co_smallengine06_trail',

        'gf_li_smallengine04_trail',
        'gf_li_smallengine05_trail',
        'gf_li_smallengine06_trail',

        'gf_ku_smallengine04_trail',
        'gf_ku_smallengine05_trail',
        'gf_ku_smallengine06_trail',
    ]


class Thruster(FX):
    EFFECT_TYPE = EFT_ENGINE_THRUSTER
    VIS_GENERIC = 'gf_min_s_thruster_01'
    TEXTURES = ['planetflare']
    MEMBERS = [
        'gf_rh_thruster04',  # li
        'gf_rh_thruster05',  # li
        'gf_rh_thruster06',  # li
        'gf_rh_thruster07',  # br
        'gf_rh_thruster08',  # br
        'gf_rh_thruster09',  # br
        'gf_rh_thruster10',  # ku
        'gf_rh_thruster11',  # ku
        'gf_rh_thruster12',  # ku
        'gf_rh_thruster13',  # bw
        'gf_rh_thruster14',  # bw
        'gf_rh_thruster15',  # bw

        # extra data (for future?)
        'gf_rh_thruster16',
        'gf_rh_thruster17',
        'gf_rh_thruster18',
        'gf_rh_thruster19',
        'gf_rh_thruster20',
        'gf_rh_thruster21',
    ]


LAUNCHER_IDS = [
    # RH
    11,
    12,
    13,

    # LI
    21,
    22,
    23,

    # BR
    31,
    32,
    33,

    # KU
    41,
    42,
    43,

    # BW
    51,
    52,
    53,
]

LAUNCHER_IDS_ALT = [
    # RH
    15,
    16,
    17,

    # LI
    25,
    26,
    27,

    # BR
    35,
    36,
    37,

    # KU
    45,
    46,
    47,

    # BW
    55,
    56,
    57,
]


class CruiseDisruptorDrive(FX):
    EFFECT_TYPE = EFT_MISSILE_DRIVE
    VIS_GENERIC = 'min_missile01_drive'
    TEXTURES = ['planetflare', 'beam', 'sarma', 'smoke']
    FX_APPEND = '_drive'
    MEMBERS = [f'li_cruisedis{idx:02d}' for idx in LAUNCHER_IDS]


class CruiseDisruptorImpact(FX):
    EFFECT_TYPE = EFT_EXPLOSION_MISSILE
    TEXTURES = ['planetflare', 'beam', 'sarma', 'smoke']
    FX_APPEND = '_impact'
    SOUND = 'asteroid_explosion'
    MEMBERS = [f'li_cruisedis{idx:02d}' for idx in LAUNCHER_IDS]


class TorpedoDrive(FX):
    EFFECT_TYPE = EFT_MISSILE_DRIVE
    VIS_GENERIC = 'min_missile01_drive'
    TEXTURES = ['planetflare', 'beam', 'sarma', 'smoke']
    FX_APPEND = '_drive'
    MEMBERS = [f'li_torpedo{idx:02d}' for idx in LAUNCHER_IDS]


class TorpedoImpact(FX):
    EFFECT_TYPE = EFT_EXPLOSION_LARGE
    TEXTURES = ['planetflare', 'beam', 'sarma', 'smoke']
    FX_APPEND = '_impact'
    SOUND = 'med_explosion1'
    MEMBERS = [f'li_torpedo{idx:02d}' for idx in LAUNCHER_IDS]


class EmpMissileDrive(FX):
    EFFECT_TYPE = EFT_MISSILE_DRIVE
    VIS_GENERIC = 'min_missile01_drive'
    TEXTURES = ['planetflare', 'beam', 'sarma', 'smoke', 'storm']
    FX_APPEND = '_drive'
    MEMBERS = [f'li_empmissile{idx:02d}' for idx in LAUNCHER_IDS]


class EmpMissileImpact(FX):
    EFFECT_TYPE = EFT_EXPLOSION_MISSILE
    TEXTURES = ['planetflare', 'beam', 'sarma', 'smoke', 'storm']
    FX_APPEND = '_impact'
    SOUND = 'asteroid_explosion'
    MEMBERS = [f'li_empmissile{idx:02d}' for idx in LAUNCHER_IDS]


class MissileDrive(FX):
    EFFECT_TYPE = EFT_MISSILE_DRIVE
    VIS_GENERIC = 'min_missile01_drive'
    TEXTURES = ['planetflare', 'beam', 'sarma', 'smoke']
    FX_APPEND = '_drive'
    MEMBERS = [f'li_missile{idx:02d}' for idx in LAUNCHER_IDS + LAUNCHER_IDS_ALT]


class MissileImpact(FX):
    EFFECT_TYPE = EFT_EXPLOSION_MISSILE
    TEXTURES = ['planetflare', 'beam', 'sarma', 'smoke']
    FX_APPEND = '_impact'
    SOUND = 'med_explosion1'
    MEMBERS = [f'li_missile{idx:02d}' for idx in LAUNCHER_IDS + LAUNCHER_IDS_ALT]



'''


[Effect]
nickname = li_cruisedis01_drive
effect_type = EFT_MISSILE_DRIVE
vis_effect = li_cruisedis01_drive
vis_generic = min_missile01_drive

[Effect]
nickname = li_cruisedis01_impact
effect_type = EFT_EXPLOSION_MISSILE
snd_effect = asteroid_explosion
vis_effect = li_cruisedis01_impact

[Effect]
nickname = li_mine01_blast25
effect_type = EFT_EXPLOSION_MINE
snd_effect = asteroid_explosion
vis_effect = li_mine01_blast25

[Effect]
nickname = li_mine01_blast50
effect_type = EFT_EXPLOSION_MINE
snd_effect = asteroid_explosion
vis_effect = li_mine01_blast50

[Effect]
nickname = li_mine01
effect_type = EFT_WEAPON_MINE
vis_effect = li_mine01

[Effect]
nickname = li_mine02_blast25
effect_type = EFT_EXPLOSION_MINE
snd_effect = asteroid_explosion
vis_effect = li_mine02_blast25

[Effect]
nickname = li_mine02_blast50
effect_type = EFT_EXPLOSION_MINE
snd_effect = asteroid_explosion
vis_effect = li_mine02_blast50

[Effect]
nickname = li_mine02
effect_type = EFT_WEAPON_MINE
EFT_EXPLOSION_LARGE
vis_effect = li_mine02

[Effect]
nickname = li_torpedo01_drive
effect_type = EFT_MISSILE_DRIVE
vis_effect = li_torpedo01_drive
vis_generic = min_missile01_drive

[Effect]
nickname = li_torpedo01_impact
effect_type = EFT_EXPLOSION_LARGE
snd_effect = med_explosion1
vis_effect = li_torpedo01_impact

[Effect]
nickname = rh_empmissile_drive
effect_type = EFT_MISSILE_DRIVE
vis_effect = rh_empmissile_drive
vis_generic = min_missile01_drive

[Effect]
nickname = rh_empmissile_impact
effect_type = EFT_EXPLOSION_MISSILE
snd_effect = asteroid_explosion
vis_effect = rh_empmissile_impact

[Effect]
nickname = rh_missile01_drive
effect_type = EFT_MISSILE_DRIVE
vis_effect = rh_missile01_drive
vis_generic = min_missile01_drive

[Effect]
nickname = rh_missile01_impact
effect_type = EFT_EXPLOSION_MISSILE
snd_effect = med_explosion1
vis_effect = rh_missile01_impact

[Effect]
nickname = rh_missile02_drive
effect_type = EFT_MISSILE_DRIVE
vis_generic = min_missile01_drive
vis_effect = rh_missile02_drive

[Effect]
nickname = rh_missile02_impact
effect_type = EFT_EXPLOSION_MISSILE
snd_effect = med_explosion1
vis_effect = rh_missile02_impact



'''