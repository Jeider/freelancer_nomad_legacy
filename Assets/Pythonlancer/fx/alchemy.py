from tools.crc import crc32_minus_from_str

from text.dividers import SINGLE_DIVIDER

EFT_ENGINE_FIRE = 'EFT_ENGINE_FIRE'
EFT_ENGINE_TRAIL = 'EFT_ENGINE_TRAIL'
EFT_ENGINE_THRUSTER = 'EFT_ENGINE_THRUSTER'


class FX:
    TEXTURES = []
    MEMBERS = []
    EFFECT_TYPE = None
    VIS_GENERIC = None

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
            f'nickname = {member}',
            f'effect_type = {cls.EFFECT_TYPE}',
            f'vis_effect = {member}'
        ]
        if cls.VIS_GENERIC:
            items.append(f'vis_generic = {cls.VIS_GENERIC}')
        for texture in cls.TEXTURES:
            items.append(f'textures = fx\\{texture}.txm')

        return SINGLE_DIVIDER.join(items)

    @classmethod
    def get_vis_effect(cls, member):
        items = [
            '[VisEffect]',
            f'nickname = {member}',
            f'alchemy = fx\\generated\\{member}.ale',
            f'effect_crc = {crc32_minus_from_str(member)}'
        ]
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
    TEXTURES = ['planetflare', 'sarma', 'beam']
    MEMBERS = [
        'gf_rh_thruster04',  # li
        'gf_rh_thruster05',  # li pir
        'gf_rh_thruster06',  # li civ
        'gf_rh_thruster07',  # br
        'gf_rh_thruster08',  # br pir
        'gf_rh_thruster09',  # br civ
        'gf_rh_thruster10',  # ku
        'gf_rh_thruster11',  # ku pir
        'gf_rh_thruster12',  # ku civ
        'gf_rh_thruster13',  # no

        # extra data (for future?)
        'gf_rh_thruster14',
        'gf_rh_thruster15',
        'gf_rh_thruster16',
        'gf_rh_thruster17',
        'gf_rh_thruster18',
        'gf_rh_thruster19',
        'gf_rh_thruster20',
        'gf_rh_thruster21',
    ]
