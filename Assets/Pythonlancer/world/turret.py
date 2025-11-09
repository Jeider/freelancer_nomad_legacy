from world.names import *
from world.equipment import Equipment, DefaultGood
from text.infocards import InfocardBuilder
from text.strings import MultiString as MS


class Turret(Equipment, DefaultGood):
    COMBINABLE = False
    WEAPON_CODE = CLOAK

    INFO1 = MS('Устройство, позволяющее вашему кораблю длительное время находиться в невидимости.',
               'With this device you can become invisible.')

    INFO2 = MS('Вы можете установить данное устройство только на точку монтирования Контрмеры.',
               'You can mount this device only on Countermeassure mount point.')

    INFO3 = MS('Для переключения режимов невидимости используйте ВТОРИЧНУЮ кнопку "МАГН.ЛУЧ (все). / Невидимость. '
               'Комбинация ОБЯЗАТЕЛЬНО должна включать кнопку Ctrl.',
               'To switch invisible modes use SECONDARY button "Tractor beam (ALL) / Invisibility". '
               'Combination MUST contain Ctrl button.')

    def __init__(self, ids, nickname, in_time, out_time, ru_name, ru_fullname, en_name, en_fullname,
                 ru_extra_descript, en_extra_descript, price):
        self.ids = ids

        self.nickname = nickname
        self.in_time = in_time
        self.out_time = out_time
        self.price = price

        self.ru_name = ru_name
        self.ru_fullname = ru_fullname
        self.en_name = en_name
        self.en_fullname = en_fullname
        self.ru_extra_descript = ru_extra_descript
        self.en_extra_descript = en_extra_descript

        self.ids_name = ids.new_name(
            MS(
                self.ru_name,
                self.en_name
            )
        )
        self.ids_info = ids.new_info(
            MS(
                InfocardBuilder.build_equip_infocard(
                    self.ru_fullname,
                    self.get_ru_description_content()
                ),
                InfocardBuilder.build_equip_infocard(
                    self.en_fullname,
                    self.get_en_description_content()
                )
            )
        )

    def get_price(self):
        return self.price

    def get_market_level(self):
        return -1  # ????

    def get_nickname(self):
        return self.nickname

    def get_rate(self):
        return self.get_civ_rate()

    def get_ru_description_content(self):
        content = []

        content.append(self.INFO1.get_ru())
        content.append(self.INFO2.get_ru())
        content.append(self.INFO3.get_ru())
        content.append(self.ru_extra_descript)

        return content

    def get_en_description_content(self):
        content = []

        content.append(self.INFO1.get_en())
        content.append(self.INFO2.get_en())
        content.append(self.INFO3.get_en())
        content.append(self.en_extra_descript)

        return content

    def get_ids_name(self):
        return self.ids_name.id

    def get_ids_info(self):
        return self.ids_info.id

    def get_icon(self):
        return r'equipment\models\icons\ge\ge_scanner01.3db'

    def get_muzzle_velocity(self):
        return 1200

    def get_flash_particle(self):
        raise NotImplementedError
        # return 'rh_capgun_01_flash'

    def get_impact_effect(self):
        raise NotImplementedError
        # return 'rh_capgun_01_impact'

    def get_proj_effect(self):
        raise NotImplementedError
        # return 'rh_capgun_01_proj'

    def get_weapon_class(self):
        raise NotImplementedError
        # return 'T_turret02'

    def get_model(self):
        raise NotImplementedError

    def get_material(self):
        raise NotImplementedError

    def get_hit_pts(self):
        raise NotImplementedError

    def get_fire_sound(self):
        raise NotImplementedError
        # return 'fire_capship'

    def get_hull_damage(self):
        raise NotImplementedError

    def get_energy_damage(self):
        return 0

    def get_turn_rate(self):
        return 60

    def get_equip(self):
        nickname = self.get_nickname()
        return f'''
[Munition]
nickname = {nickname}_ammo
hp_type = hp_gun
requires_ammo = false
hit_pts = 2
hull_damage = {self.get_hull_damage()}
energy_damage = {self.get_energy_damage()}
weapon_type = {self.get_weapon_class()}
one_shot_sound = {self.get_fire_sound()}
munition_hit_effect = {self.get_impact_effect()}
const_effect = {self.get_proj_effect()}
lifetime = 3.000000
force_gun_ori = false
mass = 10
volume = 0.000100

[Gun]
nickname = rh_double_turret01
ids_name = {self.get_ids_name()}
ids_info = {self.get_ids_info()}
DA_archetype = {self.get_model()}
material_library = {self.get_material()}
HP_child = HPConnect
hit_pts = {self.get_hit_pts()}
explosion_resistance = 0.25
debris_type = debris_turret_large
parent_impulse = 20
child_impulse = 80
volume = 0.000000
mass = 10
damage_per_fire = 0
power_usage = 0
refire_delay = 0.500000
muzzle_velocity = {self.get_muzzle_velocity()}
toughness = 10 ;1.600000
flash_particle_name = {self.get_flash_particle()}
flash_radius = 12
projectile_archetype = {nickname}_ammo
separation_explosion = sever_debris
auto_turret = true
turn_rate = {self.get_turn_rate()}
lootable = false
hp_gun_type = hp_turret_special_2

[LOD]
obj = Root
LODranges = 0, 5000

[LOD]
obj = barrel
LODranges = 0, 2500
'''
