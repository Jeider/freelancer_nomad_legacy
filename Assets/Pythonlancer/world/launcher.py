from world.equipment import DefaultGood, MainEquipPrice, Icon
from world.weapon import Weapon

# from fx.weapon import WeaponFX  # must be missile fx

RH_LIGHTGUN = 'rh_lightgun'
RH_HEAVYGUN = 'rh_heavygun'
RH_CIVGUN = 'rh_civgun'
RH_HUNTERGUN = 'rh_huntergun'
RH_SHIELDGUN = 'rh_shieldgun'
RH_PIRATEGUN = 'rh_pirategun'
RH_HESSIANGUN = 'rh_heassiangun'
RH_JUNKERGUN = 'rh_junkergun'




class Launcher(MainEquipPrice, Weapon, DefaultGood):
    DROP_CHANCE = 12
    MAX_PRICE = 120000

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def get_icon(self):
        raise Exception('icon exception')
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

    def get_ru_fullname(self):
        return '{described_name} {name}'.format(
            name=self.get_ru_name(),
            described_name=self.RU_NAME_DESC,
        )

    def get_ru_description_content(self):
        content = []
        return content


class RheinlandMissileLauncher(Gun):
    RU_NAME = 'Рейнландская ракетница'
    RU_NAME_DESC = 'Рейнландская ракетница базового типа'
    BASE_NICKNAME = RH_LIGHTGUN
    MODEL = Weapon.RH_GAMMA_BEAMER
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 700
    LIFETIME = 1.0
    FX_FACTION = WeaponFX.FX_RH
    FX_APPEARANCE = WeaponFX.FX_TACHYON

