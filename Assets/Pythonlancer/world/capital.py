from text.dividers import DIVIDER, SINGLE_DIVIDER

DEBRIS = 'debris'
DISAPPEAR = 'disappear'


class Capital:
    TEMPLATE_CODE = None
    ARCHETYPE = None
    RU_NAME = None

    HIT_PTS = None
    PARTS_HP = None
    EXTRA_DAMAGE = None

    NO_DEATH_FUSE = False

    DAMAGE_FUSE1 = None
    DAMAGE_FUSE2 = None
    DAMAGE_FUSE3 = None

    DAMAGE_FUSE1_HEALTH_FACTOR = 0.5
    DAMAGE_FUSE2_HEALTH_FACTOR = 0.25
    DAMAGE_FUSE3_HEALTH_FACTOR = 0.15

    DAMAGE_FX = None
    DAMAGE_FX_LARGE = None
    DAMAGE_FX_SMALL = None
    HURT_FX = 'explosion_sfx_csx_large04'
    HURT_HP = 'HpMount'

    INITIAL_PART_DAMAGE_FACTOR = 0.5

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def __init__(self, ids):
        self.ids = ids
        self.fuses_definitions = []
        self.used_parts = []

        if not self.RU_NAME:
            raise Exception(f'Capital ship {self.ARCHETYPE} have no ru_name')

        self.ids_name = self.ids.new_name(self.RU_NAME)

    def get_hit_pts(self):
        return self.HIT_PTS

    def get_ids_name(self):
        return self.ids_name.id

    def get_ids_info(self):
        return 1  # TODO: сделать описания капшипов

    def get_part_hit_pts(self, hit_pts_multipler=1):
        return self.PARTS_HP * hit_pts_multipler

    def add_extra_damage_fuse(self, fuse_name, damage, obj, hardpoint, part_fate='debris',
                              silent=False, is_large=False):
        actions = [
            f''' 
[fuse]
name = {fuse_name}
lifetime = 0.100000
death_fuse = {"false" if self.NO_DEATH_FUSE else "true"} ''',
            f'''
[start_effect]
effect = {self.HURT_FX}
at_t = 0.100000
hardpoint = {self.HURT_HP}
pos_offset = 0, 0, 0 ''',
        ]

        if hardpoint:
            damage_fx = self.DAMAGE_FX_LARGE if is_large else self.DAMAGE_FX

            if not damage_fx:
                raise Exception(f'Ship {self.ARCHETYPE} requires damage_fx to be appeared')
            actions.append(f'''
[start_effect]
effect = {damage_fx}
hardpoint = {hardpoint}
at_t = 0.000000 ''')

        if not silent:
            actions.append(f'''
[damage_root]
at_t = 0.9
damage_type = relative
hitpoints = {damage} ''')

        if not self.NO_DEATH_FUSE:
            actions.append(f'''
[destroy_group]
at_t = 0.99
group_name = {obj}
fate = {part_fate} ''')

        self.fuses_definitions.append(SINGLE_DIVIDER.join(actions))

    def add_initial_damage_fuse(self, fuse_name, obj, damage):
        self.fuses_definitions.append(
            f''' 
[fuse]
name = {fuse_name}
lifetime = 0.100000
death_fuse = true

[damage_group]
group_name = {obj}
at_t = 0.100000
damage_type = relative
hitpoints = {damage}
            '''
        )

    def get_part_fuses_definitions(self):
        return SINGLE_DIVIDER.join(self.fuses_definitions)

    def get_damage(self, part_kind, obj, hardpoint=None, part_fate=DEBRIS,
                   hit_pts_multipler=1, silent=False, is_large=False):
        if part_kind in self.used_parts:
            raise Exception(f'Part of ship {self.ARCHETYPE} is already used')
        self.used_parts.append(part_kind)

        params = []

        extra_dmg_fuse_name = f'fuse_{self.ARCHETYPE}_extra_dmg_{part_kind}'
        self.add_extra_damage_fuse(
            fuse_name=extra_dmg_fuse_name,
            damage=self.EXTRA_DAMAGE,
            obj=obj,
            hardpoint=hardpoint,
            part_fate=part_fate,
            silent=silent,
            is_large=is_large,
        )
        params.append(f'fuse = {extra_dmg_fuse_name}, 0.000000, 1')

        init_dmg_fuse_name = f'fuse_{self.ARCHETYPE}_init_dmg_{part_kind}'


        print(init_dmg_fuse_name)
        init_damage = (self.PARTS_HP * self.INITIAL_PART_DAMAGE_FACTOR) * hit_pts_multipler
        print(init_damage)
        self.add_initial_damage_fuse(
            init_dmg_fuse_name,
            obj,
            init_damage,
        )
        params.append(f'fuse = {init_dmg_fuse_name}, 0.000000, {self.get_hit_pts()*2}')

        params.extend([
            f'hit_pts = {self.get_part_hit_pts(hit_pts_multipler)+init_damage}',
            'root_health_proxy = true',
        ])

        if init_dmg_fuse_name == 'fuse_ku_battleship_m13_assault_init_dmg_eng1':
            print('1')
        return SINGLE_DIVIDER.join(params)

    @property
    def root(self):
        params = [
            f'nickname = {self.ARCHETYPE}',
            f'hit_pts = {self.get_hit_pts()}',
            f'ids_name = {self.get_ids_name()}',
            f'ids_info = {self.get_ids_info()}',
        ]

        if self.DAMAGE_FUSE1:
            params.append(f'fuse = {self.DAMAGE_FUSE1}, 0, {self.get_hit_pts()*self.DAMAGE_FUSE1_HEALTH_FACTOR}')

        if self.DAMAGE_FUSE2:
            params.append(f'fuse = {self.DAMAGE_FUSE2}, 0, {self.get_hit_pts()*self.DAMAGE_FUSE2_HEALTH_FACTOR}')

        return SINGLE_DIVIDER.join(params)

    def control_tower(self, obj, hardpoint=None):
        return self.get_damage('control_tower', obj, hardpoint, part_fate=DISAPPEAR)

    def nose(self, obj, hardpoint=None, hit_pts_multipler=2):
        return self.get_damage('nose', obj, hardpoint, hit_pts_multipler=hit_pts_multipler)

    def front(self, obj, hardpoint=None, hit_pts_multipler=2):
        return self.get_damage('front', obj, hardpoint, hit_pts_multipler=hit_pts_multipler)

    def tail(self, obj, hardpoint=None):
        return self.get_damage('tail', obj, hardpoint)

    def platform(self, obj, hardpoint=None):
        return self.get_damage('platform', obj, hardpoint, part_fate=DISAPPEAR, hit_pts_multipler=2)

    def eng1(self, obj, hardpoint=None):
        return self.get_damage('eng1', obj, hardpoint, part_fate=DISAPPEAR)

    def eng2(self, obj, hardpoint=None):
        return self.get_damage('eng2', obj, hardpoint, part_fate=DISAPPEAR)

    def eng3(self, obj, hardpoint=None):
        return self.get_damage('eng3', obj, hardpoint, part_fate=DISAPPEAR)

    def eng4(self, obj, hardpoint=None):
        return self.get_damage('eng4', obj, hardpoint, part_fate=DISAPPEAR)

    def large_eng1(self, obj, hardpoint=None):
        return self.get_damage('large_eng1', obj, hardpoint, part_fate=DISAPPEAR, is_large=True,
                               hit_pts_multipler=2)

    def large_eng2(self, obj, hardpoint=None):
        return self.get_damage('large_eng2', obj, hardpoint, part_fate=DISAPPEAR, is_large=True,
                               hit_pts_multipler=2)

    def reactor1(self, obj, hardpoint=None):
        return self.get_damage('reactor1', obj, hardpoint, part_fate=DISAPPEAR)

    def reactor2(self, obj, hardpoint=None):
        return self.get_damage('reactor2', obj, hardpoint, part_fate=DISAPPEAR)

    def wing1(self, obj, hardpoint=None, silent=False, disappear=False):
        return self.get_damage('wing1', obj, hardpoint, silent=silent,
                               part_fate=DISAPPEAR if disappear else DEBRIS)

    def wing2(self, obj, hardpoint=None, silent=False, disappear=False):
        return self.get_damage('wing2', obj, hardpoint, silent=silent,
                               part_fate=DISAPPEAR if disappear else DEBRIS)

    def shield1(self, obj, hardpoint=None, disappear=False):
        return self.get_damage('shield1', obj, hardpoint,
                               part_fate=DISAPPEAR if disappear else DEBRIS)

    def shield2(self, obj, hardpoint=None, disappear=False):
        return self.get_damage('shield2', obj, hardpoint,
                               part_fate=DISAPPEAR if disappear else DEBRIS)

    def spike1(self, obj, hardpoint=None):
        return self.get_damage('spike1', obj, hardpoint, part_fate=DISAPPEAR)

    def spike2(self, obj, hardpoint=None):
        return self.get_damage('spike2', obj, hardpoint, part_fate=DISAPPEAR)

    def tower1(self, obj, hardpoint=None):
        return self.get_damage('tower1', obj, hardpoint, part_fate=DISAPPEAR)

    def tower2(self, obj, hardpoint=None):
        return self.get_damage('tower2', obj, hardpoint, part_fate=DISAPPEAR)


class LibertyCruiser(Capital):
    TEMPLATE_CODE = 'lcr'
    ARCHETYPE = 'li_cruiser'
    RU_NAME = 'Крейсер Либерти'

    DAMAGE_FUSE1 = 'li_cruiser_burning_fuse01'
    DAMAGE_FUSE2 = 'li_cruiser_burning_fuse02'

    DAMAGE_FX = 'gf_li_capexplosion03popper'

    HIT_PTS = 250000
    PARTS_HP = 10000
    EXTRA_DAMAGE = 20000


class BretoniaGunboat(Capital):
    TEMPLATE_CODE = 'bgb'
    ARCHETYPE = 'br_gunboat'
    RU_NAME = 'Канонерка Бретонии'

    DAMAGE_FUSE1 = 'br_gunship_burning_fuse01'
    DAMAGE_FUSE2 = 'br_gunship_burning_fuse02'

    DAMAGE_FX = 'gf_explosion_br_destroyer_smallexp'

    HIT_PTS = 180000
    PARTS_HP = 8000
    EXTRA_DAMAGE = 20000


class BretoniaDestroyer(Capital):
    TEMPLATE_CODE = 'bdr'
    ARCHETYPE = 'br_destroyer'
    RU_NAME = 'Эсминец Бретонии'

    DAMAGE_FUSE1 = 'br_destroyer_burning_fuse01'
    DAMAGE_FUSE2 = 'br_destroyer_burning_fuse02'

    DAMAGE_FX = 'gf_explosion_br_destroyer_smallexp'

    HIT_PTS = 240000
    PARTS_HP = 12500
    EXTRA_DAMAGE = 30000


class KusariGunboat(Capital):
    TEMPLATE_CODE = 'kgb'
    ARCHETYPE = 'ku_gunboat'
    RU_NAME = 'Канонерка Кусари'

    DAMAGE_FUSE1 = 'ku_gunship_burning_fuse01'
    DAMAGE_FUSE2 = 'ku_gunship_burning_fuse01'

    DAMAGE_FX = 'gf_explosion_ku_gunboat_smallexp'

    HIT_PTS = 160000
    PARTS_HP = 6000
    EXTRA_DAMAGE = 18000


class KusariDestroyer(Capital):
    TEMPLATE_CODE = 'kdr'
    ARCHETYPE = 'ku_destroyer'
    RU_NAME = 'Эсминец Кусари'

    DAMAGE_FUSE1 = 'ku_destroyer_burning_fuse01'
    DAMAGE_FUSE2 = 'ku_destroyer_burning_fuse02'

    DAMAGE_FX = 'gf_explosion_ku_cruiser_smallexp'

    HIT_PTS = 220000
    PARTS_HP = 10000
    EXTRA_DAMAGE = 28000


class RheinlandGunboat(Capital):
    TEMPLATE_CODE = 'rgb'
    ARCHETYPE = 'rh_gunboat'
    RU_NAME = 'Канонерка Рейнланда'

    DAMAGE_FUSE1 = 'rh_gunship_burning_fuse01'
    DAMAGE_FUSE2 = 'rh_gunship_burning_fuse02'

    DAMAGE_FX = 'gf_explosion_rh_gunboat_bigexplosionsmall'

    HIT_PTS = 120000
    PARTS_HP = 10000
    EXTRA_DAMAGE = 23000


class RheinlandCruiser(Capital):
    TEMPLATE_CODE = 'rcr'
    ARCHETYPE = 'rh_cruiser'
    RU_NAME = 'Крейсер Рейнланда'

    DAMAGE_FUSE1 = 'rh_cruiser_burning_fuse01'
    DAMAGE_FUSE2 = 'rh_cruiser_burning_fuse02'

    DAMAGE_FX = 'gf_explosion_rh_cruiser_bigexplosionsmall'

    HIT_PTS = 220000
    PARTS_HP = 10000
    EXTRA_DAMAGE = 28000


class Armored(Capital):
    TEMPLATE_CODE = 'armored'
    ARCHETYPE = 'ge_armored'
    RU_NAME = 'Бронированный транспорт'

    DAMAGE_FUSE1 = 'intermed_damage_smallship01'
    DAMAGE_FUSE2 = 'intermed_damage_smallship02'
    DAMAGE_FUSE3 = 'intermed_damage_smallship03'

    DAMAGE_FX = 'explosion_cv_fighter_silent'

    HIT_PTS = 150000
    PARTS_HP = 5000
    EXTRA_DAMAGE = 10000


class Miner(Capital):
    TEMPLATE_CODE = 'miner'
    ARCHETYPE = 'ge_miner'
    RU_NAME = 'Рудокоп'

    NO_DEATH_FUSE = True

    HIT_PTS = 250000
    PARTS_HP = 8000
    EXTRA_DAMAGE = 20000


class RheinlandBattleshipM11(Capital):
    TEMPLATE_CODE = 'rbs_m11'
    ARCHETYPE = 'rh_battleship_m11'
    RU_NAME = 'Линкор Рейнланда'

    DAMAGE_FUSE2 = 'rh_battleship_burning_fuse02'

    DAMAGE_FX = 'gf_explosion_rh_battleship_bigexplosion'
    # gf_explosion_rh_battleship_explosionsmall

    HIT_PTS = 600000
    PARTS_HP = 25000
    EXTRA_DAMAGE = 60000


class KusariBattleshipM12Runner(Capital):
    TEMPLATE_CODE = 'kbs_runner'
    ARCHETYPE = 'ku_battleship_m13_assault'
    RU_NAME = 'Линкор Кусари'

    DAMAGE_FX = 'gf_explosion_ku_battleship_smallexp'

    HIT_PTS = 10000000
    PARTS_HP = 20000
    EXTRA_DAMAGE = 2000000

