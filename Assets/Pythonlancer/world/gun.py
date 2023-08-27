from world.equipment import DefaultGood, MainEquipPrice, Icon
from world.weapon import Weapon


RH_LIGHTGUN = 'rh_lightgun'
RH_HEAVYGUN = 'rh_heavygun'
RH_CIVGUN = 'rh_civgun'
RH_HUNTERGUN = 'rh_huntergun'
RH_SHIELDGUN = 'rh_shieldgun'
RH_PIRATEGUN = 'rh_pirategun'
RH_HESSIANGUN = 'rh_heassiangun'
RH_JUNKERGUN = 'rh_junkergun'


class Gun(MainEquipPrice, Weapon, DefaultGood):
    DROP_CHANCE = 12
    MAX_PRICE = 120000

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def get_icon(self):
        icon = self.ICON_PER_WEAPON_MODEL[self.MODEL]
        return Icon.get_icon_path(icon)

    def get_max_price(self):
        return self.MAX_PRICE

    def get_ru_base_name(self):
        return self.RU_NAME

    def get_ru_name(self):
        return '{MODEL} {mark}'.format(
            MODEL=self.get_ru_base_name(),
            mark=self.get_mark_name(),
        )



class RheinlandLightgun(Gun):
    RU_NAME = 'Гремучий змей'
    BASE_NICKNAME = RH_LIGHTGUN
    MODEL = Weapon.RH_GAMMA_BEAMER
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 700
    LIFETIME = 1.0


class RheinlandHeavygun(Gun):
    RU_NAME = 'Огненный поцелуй'
    BASE_NICKNAME = RH_HEAVYGUN
    MODEL = Weapon.RH_PROTON_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_2
    MUZZLE_VELOCITY = 500
    LIFETIME = 1.2


class RheinlandCivgun(Gun):
    RU_NAME = 'Звездный луч'
    BASE_NICKNAME = RH_CIVGUN
    MODEL = Weapon.RH_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 600
    LIFETIME = 0.8


class RheinlandHuntergun(Gun):
    RU_NAME = 'Незримый клинок'
    BASE_NICKNAME = RH_HUNTERGUN
    MODEL = Weapon.RH_GAMMA_BEAMER
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8


class RheinlandShieldgun(Gun):
    RU_NAME = 'Пламенное проклятие'
    BASE_NICKNAME = RH_SHIELDGUN
    MODEL = Weapon.RH_PROTON_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_4
    MUZZLE_VELOCITY = 600
    LIFETIME = 1.0
    SHIELDGUN = True


class RheinlandPirategun(Gun):
    RU_NAME = 'Наттер'
    BASE_NICKNAME = RH_PIRATEGUN
    MODEL = Weapon.RH_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8


class RheinlandHessiangun(Gun):
    RU_NAME = 'Ротер Блиц'
    BASE_NICKNAME = RH_HESSIANGUN
    MODEL = Weapon.RH_GAMMA_BEAMER
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 700
    LIFETIME = 1


class RheinlandJunkergun(Gun):
    RU_NAME = 'Скорпион'
    BASE_NICKNAME = RH_JUNKERGUN
    MODEL = Weapon.CO_SHOCK_THERAPY
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 600
    LIFETIME = 1

