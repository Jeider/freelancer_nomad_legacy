from world.equipment import DefaultGood, MainEquipPrice, Icon
from world.weapon import Weapon


class Gun(MainEquipPrice, Weapon, DefaultGood):
    DROP_CHANCE = 12
    MAX_PRICE = 120000

    RH_LIGHTGUN = 'rh_lightgun'
    RH_HEAVYGUN = 'rh_heavygun'
    RH_CIVGUN = 'rh_civgun'
    RH_HUNTERGUN = 'rh_huntergun'
    RH_SHIELDGUN = 'rh_shieldgun'
    RH_PIRATEGUN = 'rh_pirategun'
    RH_HESSIANGUN = 'rh_heassiangun'
    RH_JUNKERGUN = 'rh_junkergun'

    RH_GUNS = [
        {
            'ru_name': 'Гремучий змей',
            'base_nickname': RH_LIGHTGUN,
            'model': Weapon.RH_GAMMA_BEAMER,
            'equip_type': Weapon.EQUIP_MAIN,
            'refire_rate': Weapon.REFIRE_RATE_6,
            'muzzle_velocity': 700,
            'lifetime': 1.0,
        },
        {
            'ru_name': 'Огненный поцелуй',
            'base_nickname': RH_HEAVYGUN,
            'model': Weapon.RH_PROTON_BLASTER,
            'equip_type': Weapon.EQUIP_MAIN,
            'refire_rate': Weapon.REFIRE_RATE_2,
            'muzzle_velocity': 500,
            'lifetime': 1.2,
        },
        {
            'ru_name': 'Звездный луч',
            'base_nickname': RH_CIVGUN,
            'model': Weapon.GE_SHREDDER_SHOTGUN,
            'equip_type': Weapon.EQUIP_CIV,
            'refire_rate': Weapon.REFIRE_RATE_4,
            'muzzle_velocity': 600,
            'lifetime': 0.8,
        },
        {
            'ru_name': 'Незримый клинок',
            'base_nickname': RH_HUNTERGUN,
            'model': Weapon.GE_SHREDDER_SHOTGUN,
            'equip_type': Weapon.EQUIP_PIRATE,
            'refire_rate': Weapon.REFIRE_RATE_8,
            'muzzle_velocity': 750,
            'lifetime': 0.8,
        },
        {
            'ru_name': 'Пламенное проклятие',
            'base_nickname': RH_SHIELDGUN,
            'model': Weapon.RH_PROTON_BLASTER,
            'equip_type': Weapon.EQUIP_CIV,
            'refire_rate': Weapon.REFIRE_RATE_4,
            'muzzle_velocity': 600,
            'lifetime': 1.0,
            'shieldgun': True,
        },
        {
            'ru_name': 'Наттер',
            'base_nickname': RH_PIRATEGUN,
            'model': Weapon.CO_RAILDADDY,
            'equip_type': Weapon.EQUIP_CIV,
            'refire_rate': Weapon.REFIRE_RATE_8,
            'muzzle_velocity': 750,
            'lifetime': 0.8,
        },
        {
            'ru_name': 'Ротер Блиц',
            'base_nickname': RH_HESSIANGUN,
            'model': Weapon.RH_GAMMA_BEAMER,
            'equip_type': Weapon.EQUIP_PIRATE,
            'refire_rate': Weapon.REFIRE_RATE_6,
            'muzzle_velocity': 700,
            'lifetime': 1,
        },
        {
            'ru_name': 'Скорпион',
            'base_nickname': RH_JUNKERGUN,
            'model': Weapon.CO_RAILDADDY,
            'equip_type': Weapon.EQUIP_PIRATE,
            'refire_rate': Weapon.REFIRE_RATE_8,
            'muzzle_velocity': 600,
            'lifetime': 1,
        },
    ]

    def get_icon(self):
        icon = self.ICON_PER_WEAPON_MODEL[self.model]
        return Icon.get_icon_path(icon)

    def get_max_price(self):
        return self.MAX_PRICE

    def get_ru_base_name(self):
        return self.ru_name

    def get_ru_name(self):
        return '{model} {mark}'.format(
            model=self.get_ru_base_name(),
            mark=self.get_mark_name(),
        )
