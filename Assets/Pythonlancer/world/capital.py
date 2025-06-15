from text.dividers import DIVIDER, SINGLE_DIVIDER


class Capital:
    TEMPLATE_CODE = None
    ARCHETYPE = None

    HIT_PTS = None
    PARTS_HP = None
    EXTRA_DAMAGE = None

    DAMAGE_FX = None

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def __init__(self, ids):
        self.ids = ids
        # pass improve in future

    def get_hit_pts(self):
        return self.HIT_PTS

    def get_fuses(self):
        return ''

    def get_damage(self, obj, point):
        return ''

    @property
    def root(self):
        params = [
            f'nickname = {self.ARCHETYPE}',
            f'hit_pts = {self.get_hit_pts()}',
            self.get_fuses(),
        ]
        return SINGLE_DIVIDER.join(params)

    def control_tower(self, obj=''):
        return ''

    def nose(self, obj=''):
        return ''

    def front(self, obj=''):
        return ''

    def tail(self, obj=''):
        return ''

    def platform(self, obj=''):
        return ''

    def eng1(self, obj=''):
        return ''

    def eng2(self, obj=''):
        return ''

    def eng3(self, obj=''):
        return ''

    def eng4(self, obj=''):
        return ''

    def wing1(self, obj=''):
        return ''

    def wing2(self, obj=''):
        return ''

    def wing3(self, obj=''):
        return ''

    def wing4(self, obj=''):
        return ''

    def spike1(self, obj=''):
        return ''

    def spike2(self, obj=''):
        return ''

    def tower1(self, obj=''):
        return ''

    def tower2(self, obj=''):
        return ''


class LibertyCruiser(Capital):
    TEMPLATE_CODE = 'lcr'
    ARCHETYPE = 'li_cruiser'

    HIT_PTS = 200000
    PARTS_HP = 10000
    EXTRA_DAMAGE = 20000


class BretoniaGunboat(Capital):
    TEMPLATE_CODE = 'bgb'
    ARCHETYPE = 'br_gunboat'

    HIT_PTS = 100000
    PARTS_HP = 5000
    EXTRA_DAMAGE = 10000


class BretoniaDestroyer(Capital):
    TEMPLATE_CODE = 'bdr'
    ARCHETYPE = 'br_destroyer'

    HIT_PTS = 200000
    PARTS_HP = 10000
    EXTRA_DAMAGE = 20000


class KusariGunboat(Capital):
    TEMPLATE_CODE = 'kgb'
    ARCHETYPE = 'ku_gunboat'

    HIT_PTS = 100000
    PARTS_HP = 5000
    EXTRA_DAMAGE = 10000


class KusariDestroyer(Capital):
    TEMPLATE_CODE = 'kdr'
    ARCHETYPE = 'ku_destroyer'

    HIT_PTS = 200000
    PARTS_HP = 10000
    EXTRA_DAMAGE = 20000


class RheinlandGunboat(Capital):
    TEMPLATE_CODE = 'rgb'
    ARCHETYPE = 'rh_gunboat'

    HIT_PTS = 100000
    PARTS_HP = 5000
    EXTRA_DAMAGE = 10000


class RheinlandCruiser(Capital):
    TEMPLATE_CODE = 'rcr'
    ARCHETYPE = 'rh_cruiser'

    HIT_PTS = 200000
    PARTS_HP = 10000
    EXTRA_DAMAGE = 20000


class Armored(Capital):
    TEMPLATE_CODE = 'armored'
    ARCHETYPE = 'ge_armored'

    DAMAGE_FUSES = [
        'intermed_damage_smallship03',
        'intermed_damage_smallship02',
        'intermed_damage_smallship01',
    ]

    HIT_PTS = 100000
    PARTS_HP = 5000
    EXTRA_DAMAGE = 10000
