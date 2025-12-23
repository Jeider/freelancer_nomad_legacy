from world.equipment import DefaultGood, MainEquipPrice, Icon
from world.weapon import Weapon
from world import level

from world.names import *

from fx.weapon import WeaponFX

from text.strings import MultiString as MS


RU_MINING_GAS_BONUS = 'Эта пушка эффективно сжижает газовые облака'

RU_SHIELDGUN_BONUS = 'Это противощитовая пушка и она наносит внушительные повреждения по щиту за счет отсутствующих повреждений по корпусу'

RU_RATE_TEXT_PER_WEAPON_RATE = {
    Weapon.REFIRE_RATE_10: 'Обладает максимальной скорострельностью за счет минимальной мощности',
    Weapon.REFIRE_RATE_8: 'Обладает высокой скорострельностью за счет низкой мощности',
    Weapon.REFIRE_RATE_6: 'Обладает повышенной скорострельностью за счет пониженной мощности',
    Weapon.REFIRE_RATE_4: 'Обладает умеренной мощностью и скорострельностью',
    Weapon.REFIRE_RATE_3: 'Характеризуется повышенной мощностью за счет пониженной скорострельности',
    Weapon.REFIRE_RATE_2: 'Характеризуется высокой мощностью за счет низкой скорострельности',
    Weapon.REFIRE_RATE_1: 'Характеризуется максимальной мощностью за счет минимальной скорострельности',
}

RU_FEATURES_PER_FACTION = {
    Weapon.FACTION_RH: 'Бонус фракции: все рейнландские пушки имеют повышенную дальность',
    Weapon.FACTION_LI: 'Бонус фракции: все пушки Либерти лучше сопротивляются взрывам ракет, мин и т.п.',
    Weapon.FACTION_BR: 'Бонус фракции: корпусы всех бретонских пушек крепче на 50%',
    Weapon.FACTION_KU: 'Бонус фракции: все пушки Кусари наносят на 10% больше повреждений по щиту',
    Weapon.FACTION_CO: 'Бонус фракции: все пушки пограничных миров расходуют на 10% меньше энергии',
}

RU_EFFICIENT_TEXT_PER_EQUIP_TYPE = {
    Weapon.EQUIP_CIV: 'Класс эффективности: гражданский',
    Weapon.EQUIP_PIRATE: 'Класс эффективности: профессиональный',
    Weapon.EQUIP_MAIN: 'Класс эффективности: военный',
}


EN_MINING_GAS_BONUS = 'This weapon can efficiently mine gas puffs'

EN_SHIELDGUN_BONUS = 'This is a shield gun and it inflicts considerable damage on shields due to the lack of damage to the hull'

EN_RATE_TEXT_PER_WEAPON_RATE = {
    Weapon.REFIRE_RATE_10: 'Have maximal rate of fire with minimal damage',
    Weapon.REFIRE_RATE_8: 'Have considerable fire rate with low damage',
    Weapon.REFIRE_RATE_6: 'Have increased fire rate with little bit less damage',
    Weapon.REFIRE_RATE_4: 'Have moderate power and fire rate',
    Weapon.REFIRE_RATE_3: 'Have increased damage with little bit less fire rate',
    Weapon.REFIRE_RATE_2: 'Have considerable damage with low fire rate',
    Weapon.REFIRE_RATE_1: 'Have maximal damage with minimal rate of fire',
}

EN_FEATURES_PER_FACTION = {
    Weapon.FACTION_RH: 'Faction bonus: all Rheinland guns have increased firing range',
    Weapon.FACTION_LI: 'Faction bonus: all Liberty guns have better resistances from explosions of mines, missiles, etc',
    Weapon.FACTION_BR: 'Faction bonus: hulls of all Bretonia guns have additional 50% hit points',
    Weapon.FACTION_KU: 'Faction bonus: all Kusari guns have extra 10% damage on shields',
    Weapon.FACTION_CO: 'Faction bonus: all Border World guns drains on 10% less power',
}

EN_EFFICIENT_TEXT_PER_EQUIP_TYPE = {
    Weapon.EQUIP_CIV: 'Efficiency class: civilian',
    Weapon.EQUIP_PIRATE: 'Efficiency class: professional',
    Weapon.EQUIP_MAIN: 'Efficiency class: main',
}


class FactionGun:
    WEAPON_FACTION = None

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)


class RheinlandGun(FactionGun):
    WEAPON_FACTION = WEAPON_RH


class LibertyGun(FactionGun):
    WEAPON_FACTION = WEAPON_LI


class BretoniaGun(FactionGun):
    WEAPON_FACTION = WEAPON_BR


class KusariGun(FactionGun):
    WEAPON_FACTION = WEAPON_KU


class BorderWorldGun(FactionGun):
    WEAPON_FACTION = WEAPON_BW


class GenericGun:
    GENERIC_KIND = None


class Lightgun(GenericGun):
    GENERIC_KIND = LIGHTGUN


class Heavygun(GenericGun):
    GENERIC_KIND = HEAVYGUN


class Civgun(GenericGun):
    GENERIC_KIND = CIVGUN


class Pirategun(GenericGun):
    GENERIC_KIND = PIRATEGUN


class Huntergun(GenericGun):
    GENERIC_KIND = HUNTERGUN


class Shieldgun(GenericGun):
    GENERIC_KIND = SHIELDGUN


class Gun(MainEquipPrice, Weapon, DefaultGood):
    DROP_CHANCE = 12
    MAX_PRICE = 120000
    FX_FACTION = WeaponFX.FX_LI
    FX_APPEARANCE = WeaponFX.FX_LASER

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def get_market_level(self):
        return level.GUN_LEVEL_PER_CLASS[self.equipment_class]

    def get_icon(self):
        icon = self.ICON_PER_WEAPON_MODEL[self.MODEL]
        return Icon.get_icon_path(icon)

    def get_max_price(self):
        return self.MAX_PRICE

    def get_ru_base_name(self):
        return self.RU_NAME.get_ru()

    def get_ru_name(self):
        return '{MODEL} {mark}'.format(
            MODEL=self.get_ru_base_name(),
            mark=self.get_mark_name(),
        )

    def get_ru_fullname(self):
        return '{described_name} {name}'.format(
            name=self.get_ru_name(),
            described_name=self.RU_NAME_DESC.get_ru(),
        )

    def get_ru_description_content(self):
        content = []

        efficient_text = RU_EFFICIENT_TEXT_PER_EQUIP_TYPE.get(self.EQUIP_TYPE)
        if efficient_text:
            content.append(efficient_text)

        rate_text = RU_RATE_TEXT_PER_WEAPON_RATE.get(self.REFIRE_RATE)
        if rate_text:
            content.append(rate_text)

        if self.SHIELDGUN:
            content.append(RU_SHIELDGUN_BONUS)

        if self.is_gas_efficient():
            content.append(RU_MINING_GAS_BONUS)

        faction_bonus_text = RU_FEATURES_PER_FACTION.get(self.WEAPON_FACTION)
        if faction_bonus_text:
            content.append(faction_bonus_text)

        return content

    def get_en_base_name(self):
        return self.RU_NAME.get_en()

    def get_en_name(self):
        return '{MODEL} {mark}'.format(
            MODEL=self.get_en_base_name(),
            mark=self.get_mark_name(),
        )

    def get_en_fullname(self):
        return '{described_name} {name}'.format(
            name=self.get_en_name(),
            described_name=self.RU_NAME_DESC.get_en(),
        )

    def get_en_description_content(self):
        content = []

        efficient_text = EN_EFFICIENT_TEXT_PER_EQUIP_TYPE.get(self.EQUIP_TYPE)
        if efficient_text:
            content.append(efficient_text)

        rate_text = EN_RATE_TEXT_PER_WEAPON_RATE.get(self.REFIRE_RATE)
        if rate_text:
            content.append(rate_text)

        if self.SHIELDGUN:
            content.append(EN_SHIELDGUN_BONUS)

        if self.is_gas_efficient():
            content.append(EN_MINING_GAS_BONUS)

        faction_bonus_text = EN_FEATURES_PER_FACTION.get(self.WEAPON_FACTION)
        if faction_bonus_text:
            content.append(faction_bonus_text)

        return content

    @classmethod
    def is_generic(cls):
        if hasattr(cls, 'WEAPON_FACTION') and cls.WEAPON_FACTION is not None:
            if hasattr(cls, 'GENERIC_KIND') and cls.GENERIC_KIND is not None:
                return True


class DietrichLightgun(Gun, RheinlandGun):
    DAMAGE_MULTIPLIER = 1.25
    RU_NAME = MS('Рогатый змей', 'Hornviper')
    RU_NAME_DESC = MS('Легкая пушка мятежников Дитриха', 'Dietrich\'s rebels light gun')
    BASE_NICKNAME = 'dtr_lightgun'
    MODEL = Weapon.RH_PLASMA_GAT_CANNON
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_10
    MUZZLE_VELOCITY = 800
    LIFETIME = 1.2
    FX_FACTION = WeaponFX.FX_DTR
    FX_APPEARANCE = WeaponFX.FX_TACHYON


class DietrichHeavygun(Gun, RheinlandGun):
    DAMAGE_MULTIPLIER = 1.25
    RU_NAME = MS('Огненный поцелуй', 'Firekiss')
    RU_NAME_DESC = MS('Тяжелая пушка мятежников Дитриха', 'Dietrich\'s rebels heavy gun')
    BASE_NICKNAME = 'dtr_heavygun'
    MODEL = Weapon.RH_PROTON_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_2
    MUZZLE_VELOCITY = 500
    LIFETIME = 1.2
    FX_FACTION = WeaponFX.FX_DTR
    FX_APPEARANCE = WeaponFX.FX_PLASMA


class DietrichShieldgun(Gun, RheinlandGun, Heavygun):
    DAMAGE_MULTIPLIER = 1.15
    RU_NAME = MS('Годендаг', 'Goedendag')
    RU_NAME_DESC = MS('Противощитовая пушка мятежников Дитриха', 'Dietrich\'s rebels shield gun')
    BASE_NICKNAME = 'dtr_shieldgun'
    MODEL = Weapon.RH_PROTON_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_4
    MUZZLE_VELOCITY = 600
    LIFETIME = 0.8
    FX_FACTION = WeaponFX.FX_DTR
    FX_APPEARANCE = WeaponFX.FX_PULSE


class RheinlandLightgun(Gun, RheinlandGun, Lightgun):
    RU_NAME = MS('Гремучий змей', 'Rattlesnake')
    RU_NAME_DESC = MS('Легкая пушка рейнландских военных', 'Rheinland military light gun')
    BASE_NICKNAME = 'rh_lightgun'
    MODEL = Weapon.RH_GAMMA_BEAMER
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 700
    LIFETIME = 1.0
    FX_FACTION = WeaponFX.FX_RH
    FX_APPEARANCE = WeaponFX.FX_TACHYON


class RheinlandHeavygun(Gun, RheinlandGun, Heavygun):
    RU_NAME = MS('Пламенное проклятие', 'Flamecurse')
    RU_NAME_DESC = MS('Тяжелая пушка рейнландских военных', 'Rheinland military heavy gun')
    BASE_NICKNAME = 'rh_heavygun'
    MODEL = Weapon.RH_PROTON_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_2
    MUZZLE_VELOCITY = 500
    LIFETIME = 1.2
    FX_FACTION = WeaponFX.FX_RH
    FX_APPEARANCE = WeaponFX.FX_PLASMA


class RheinlandCivgun(Gun, RheinlandGun, Civgun):
    RU_NAME = MS('Звездный луч', 'Starbeam')
    RU_NAME_DESC = MS('Гражданская пушка Рейнланда', 'Rheinland Civilian Gun')
    BASE_NICKNAME = 'rh_civgun'
    MODEL = Weapon.RH_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_RH
    FX_APPEARANCE = WeaponFX.FX_LASER


class RheinlandHuntergun(Gun, RheinlandGun, Huntergun):
    RU_NAME = MS('Незримый клинок', 'Stealthblade')
    RU_NAME_DESC = MS('Пушка рейнландских наемников', 'Rheinland bounty hunters gun')
    BASE_NICKNAME = 'rh_huntergun'
    MODEL = Weapon.RH_GAMMA_BEAMER
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8
    FX_FACTION = WeaponFX.FX_RH
    FX_APPEARANCE = WeaponFX.FX_PARTICLE


class RheinlandPirategun(Gun, RheinlandGun, Pirategun):
    RU_NAME = MS('Наттер', 'Natter')
    RU_NAME_DESC = MS('Пушка рейнландских пиратов', 'Rheinland Pirate gun')
    BASE_NICKNAME = 'rh_pirategun'
    MODEL = Weapon.RH_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_LASER


class RheinlandHessiangun(Gun, RheinlandGun):
    RU_NAME = MS('Ротер Блиц', 'Roter Blitz')
    RU_NAME_DESC = MS('Пушка гессенцев', 'Hessians gun')
    BASE_NICKNAME = 'rh_hessiangun'
    MODEL = Weapon.RH_GAMMA_BEAMER
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 700
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_PARTICLE


class RheinlandJunkergun(Gun, RheinlandGun):
    RU_NAME = MS('Стервятник', 'Vulture')
    RU_NAME_DESC = MS('Пушка мусорщиков', 'Junkers gun')
    BASE_NICKNAME = 'rh_junkergun'
    MODEL = Weapon.CO_SHOCK_THERAPY
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_PHOTON


class RheinlandShieldgun(Gun, RheinlandGun, Shieldgun):
    RU_NAME = MS('Ослепитель', 'Dazzler')
    RU_NAME_DESC = MS('Рейнландская противощитовая пушка', 'Rheinland anti-shield gun')
    BASE_NICKNAME = 'rh_shieldgun'
    MODEL = Weapon.RH_PROTON_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_4
    MUZZLE_VELOCITY = 600
    LIFETIME = 1.0
    SHIELDGUN = True
    FX_FACTION = WeaponFX.FX_RH
    FX_APPEARANCE = WeaponFX.FX_PULSE


class LibertyLightgun(Gun, LibertyGun, Lightgun):
    RU_NAME = MS('Возмездие', 'Vengeance')
    RU_NAME_DESC = MS('Легкая пушка военных Либерти', 'Liberty military light gun')
    BASE_NICKNAME = 'li_lightgun'
    MODEL = Weapon.LI_LASER_BEAM
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8
    FX_FACTION = WeaponFX.FX_LI
    FX_APPEARANCE = WeaponFX.FX_LASER


class LibertyHeavygun(Gun, LibertyGun, Heavygun):
    RU_NAME = MS('Молот магмы', 'Magma Hammer')
    RU_NAME_DESC = MS('Тяжелая пушка военных Либерти', "Liberty military heavy gun")
    BASE_NICKNAME = 'li_heavygun'
    MODEL = Weapon.LI_HEAVY_ION_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_2
    MUZZLE_VELOCITY = 500
    LIFETIME = 1.2
    FX_FACTION = WeaponFX.FX_LI
    FX_APPEARANCE = WeaponFX.FX_PLASMA


class LibertyCivgun(Gun, LibertyGun, Civgun):
    RU_NAME = MS('Справедливость', 'Justice')
    RU_NAME_DESC = MS('Гражданская пушка Либерти', 'Liberty civilian gun')
    BASE_NICKNAME = 'li_civgun'
    MODEL = Weapon.LI_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8
    FX_FACTION = WeaponFX.FX_CI
    FX_APPEARANCE = WeaponFX.FX_LASER


class LibertyHuntergun(Gun, LibertyGun, Huntergun):
    RU_NAME = MS('Винтчестер', 'Winchester')
    RU_NAME_DESC = MS('Пушка наемников Либерти', 'Liberty bounty hunters gun')
    BASE_NICKNAME = 'li_huntergun'
    MODEL = Weapon.LI_PLASMA_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_4
    MUZZLE_VELOCITY = 700
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_CI
    FX_APPEARANCE = WeaponFX.FX_TACHYON


class LibertyPirategun(Gun, LibertyGun, Pirategun):
    RU_NAME = MS('Азраель', "Azrael")
    RU_NAME_DESC = MS('Пушка пиратов Либерти', 'Liberty pirates gun')
    BASE_NICKNAME = 'li_pirategun'
    MODEL = Weapon.RH_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_PHOTON


class LibertyRoguegun(Gun, LibertyGun):
    RU_NAME = MS('Вассаго', 'Vassago')
    RU_NAME_DESC = MS('Пушка разбойников Либерти', 'Liberty rogues gun')
    BASE_NICKNAME = 'li_roguegun'
    MODEL = Weapon.LI_PLASMA_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_LASER


class LibertyStarlinegun(Gun, LibertyGun):
    RU_NAME = MS('Разбойник', 'Gunslinger')
    RU_NAME_DESC = MS('Пушка банды Старлайна', 'Starline band gun')
    BASE_NICKNAME = 'li_starlinegun'
    MODEL = Weapon.LI_LASER_BEAM
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 700
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_PARTICLE


class LibertyShieldgun(Gun, LibertyGun, Shieldgun):
    RU_NAME = MS('Клинок лавы', 'Lavablade')
    RU_NAME_DESC = MS('Либертийская противощитовая пушка', 'Liberty Anti-Shield gun')
    BASE_NICKNAME = 'li_shieldgun'
    MODEL = Weapon.LI_HEAVY_ION_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_3
    MUZZLE_VELOCITY = 600
    LIFETIME = 1.0
    SHIELDGUN = True
    FX_FACTION = WeaponFX.FX_LI
    FX_APPEARANCE = WeaponFX.FX_PULSE


class BretoniaLightgun(Gun, BretoniaGun, Lightgun):
    RU_NAME = MS('Растворитель', 'Dissolver')
    RU_NAME_DESC = MS('Легкая пушка бретонских военных', 'Bretonia military light gun')
    BASE_NICKNAME = 'br_lightgun'
    MODEL = Weapon.BR_MASS_DRIVER
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 700
    LIFETIME = 1.0
    FX_FACTION = WeaponFX.FX_BR
    FX_APPEARANCE = WeaponFX.FX_TACHYON


class BretoniaHeavygun(Gun, BretoniaGun, Heavygun):
    RU_NAME = MS('Небесный путь', 'Skyrail')
    RU_NAME_DESC = MS('Тяжелая пушка бретонских военных', 'Bretonia military heavy gun')
    BASE_NICKNAME = 'br_heavygun'
    MODEL = Weapon.BR_RAILGUN
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_4
    MUZZLE_VELOCITY = 700
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_BR
    FX_APPEARANCE = WeaponFX.FX_PARTICLE


class BretoniaCivgun(Gun, BretoniaGun, Civgun):
    RU_NAME = MS('Флешпоинт', 'Flashpoint')
    RU_NAME_DESC = MS('Бретонская гражданская пушка', 'Bretonia civilian gun')
    BASE_NICKNAME = 'br_civgun'
    MODEL = Weapon.BR_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_BR
    FX_APPEARANCE = WeaponFX.FX_PHOTON


class BretoniaHuntergun(Gun, BretoniaGun, Huntergun):
    RU_NAME = MS('Потрошитель', 'Ripper')
    RU_NAME_DESC = MS('Пушка бретонских наемников', 'Bretonia bounty hunters gun')
    BASE_NICKNAME = 'br_huntergun'
    MODEL = Weapon.BR_MASS_DRIVER
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_BR
    FX_APPEARANCE = WeaponFX.FX_NEUTRON


class BretoniaPirategun(Gun, BretoniaGun, Pirategun):
    RU_NAME = MS('Скорпион', 'Scorpion')
    RU_NAME_DESC = MS('Пушка бретонских пиратов', 'Bretonia pirate gun')
    BASE_NICKNAME = 'br_pirategun'
    MODEL = Weapon.BR_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_4
    MUZZLE_VELOCITY = 700
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_PARTICLE


class BretoniaXenosgun(Gun, BretoniaGun):
    RU_NAME = MS('Тарантул', 'Tarantula')
    RU_NAME_DESC = MS('Пушка ксеносов', 'Xenos gun')
    BASE_NICKNAME = 'br_xenosgun'
    MODEL = Weapon.CO_RAILDADDY
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_3
    MUZZLE_VELOCITY = 700
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_PLASMA


class BretoniaIragun(Gun, BretoniaGun):
    RU_NAME = MS('Маттертиф', 'Matterthief')
    RU_NAME_DESC = MS('Пушка ирландских сепаратистов', 'Ireland separatists gun')
    BASE_NICKNAME = 'br_iragun'
    MODEL = Weapon.BR_MASS_DRIVER
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_4
    MUZZLE_VELOCITY = 700
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_NEUTRON


class BretoniaShieldgun(Gun, BretoniaGun, Shieldgun):
    RU_NAME = MS('Солнечный путь', 'Sunrail')
    RU_NAME_DESC = MS('Бретонская противощитовая пушка', 'Bretonia Anti-Shield Gun')
    BASE_NICKNAME = 'br_shieldgun'
    MODEL = Weapon.BR_RAILGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 600
    LIFETIME = 1.0
    SHIELDGUN = True
    FX_FACTION = WeaponFX.FX_BR
    FX_APPEARANCE = WeaponFX.FX_PULSE


class KusariLightgun(Gun, KusariGun, Lightgun):
    RU_NAME = MS('Гром', 'Skyblast')
    RU_NAME_DESC = MS('Легкая пушка кусарийских военных', "Kusari military light gun")
    BASE_NICKNAME = 'ku_lightgun'
    MODEL = Weapon.KU_ION_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8
    FX_FACTION = WeaponFX.FX_KU
    FX_APPEARANCE = WeaponFX.FX_PHOTON


class KusariHeavygun(Gun, KusariGun, Heavygun):
    RU_NAME = MS('Дезинфектор', "Disinfector")
    RU_NAME_DESC = MS('Тяжелая пушка кусарийских военных', 'Kusari heavy gun')
    BASE_NICKNAME = 'ku_heavygun'
    MODEL = Weapon.KU_AUTO_TESLA
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_4
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_KU
    FX_APPEARANCE = WeaponFX.FX_NEUTRON


class KusariCivgun(Gun, KusariGun, Civgun):
    RU_NAME = MS('Гелиос', 'Helios')
    RU_NAME_DESC = MS('Гражданская пушка Кусари', 'Kusari civilian gun')
    BASE_NICKNAME = 'ku_civgun'
    MODEL = Weapon.KU_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_CI
    FX_APPEARANCE = WeaponFX.FX_PHOTON


class KusariHuntergun(Gun, KusariGun, Huntergun):
    RU_NAME = MS('Ярость', 'Fury')
    RU_NAME_DESC = MS('Пушка кусарийская наемников', 'Kusari bounty hunters gun')
    BASE_NICKNAME = 'ku_huntergun'
    MODEL = Weapon.KU_ION_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_KU
    FX_APPEARANCE = WeaponFX.FX_LASER


class KusariPirategun(Gun, KusariGun, Pirategun):
    RU_NAME = MS('Танто', 'Tanto')
    RU_NAME_DESC = MS('Пушка кусарийская пиратов', 'Kusari pirates gun')
    BASE_NICKNAME = 'ku_pirategun'
    MODEL = Weapon.KU_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_NEUTRON


class KusariShinobigun(Gun, KusariGun):
    RU_NAME = MS('Ниндзято', 'Ninjato')
    RU_NAME_DESC = MS('Пушка клана Шиноби', 'Shinobi Gun')
    BASE_NICKNAME = 'ku_shinobigun'
    MODEL = Weapon.CO_SHOCK_THERAPY
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_TACHYON


class KusariDragongun(Gun, KusariGun):
    RU_NAME = MS('Вакидзаси', 'Wakizashi')
    RU_NAME_DESC = MS('Пушка кровавых драконов', 'Blood Dragons gun')
    BASE_NICKNAME = 'ku_dragongun'
    MODEL = Weapon.KU_ION_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_LASER


class KusariShieldgun(Gun, KusariGun, Shieldgun):
    RU_NAME = MS('Успокоитель', 'Debilitator')
    RU_NAME_DESC = MS('Кусарийская противощитовая пушка', 'Kusari Anti-Shield Gun')
    BASE_NICKNAME = 'ku_shieldgun'
    MODEL = Weapon.KU_AUTO_TESLA
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_4
    MUZZLE_VELOCITY = 600
    LIFETIME = 1.0
    SHIELDGUN = True
    FX_FACTION = WeaponFX.FX_KU
    FX_APPEARANCE = WeaponFX.FX_PULSE


class OrderLightgun(Gun, BorderWorldGun, Lightgun):
    RU_NAME = MS('Цербер', 'Cerberus')
    RU_NAME_DESC = MS('Легкая пушка Ордена', "Order Light Gun")
    BASE_NICKNAME = 'or_lightgun'
    MODEL = Weapon.CO_PROTON_COOKER
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_TACHYON


class OrderHeavygun(Gun, BorderWorldGun, Heavygun):
    RU_NAME = MS('Оникс', 'Onyx')
    RU_NAME_DESC = MS('Тяжелая пушка Ордена', 'Order Heavy Gun')
    BASE_NICKNAME = 'or_heavygun'
    MODEL = Weapon.CO_SHOCK_THERAPY
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_3
    MUZZLE_VELOCITY = 700
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_PLASMA


class BorderWorldCorsairgun(Gun, BorderWorldGun):
    RU_NAME = MS('Саламанка', 'Salamanca')
    RU_NAME_DESC = MS('Пушка Корсаров', 'Corsair gun')
    BASE_NICKNAME = 'bw_corsairgun'
    MODEL = Weapon.CO_RAILDADDY
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_4
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_NEUTRON


class BorderWorldShieldgun(Gun, BorderWorldGun, Shieldgun):
    RU_NAME = MS('Рапира', 'Rapier')
    RU_NAME_DESC = MS('Противощитовая пушка пограничья', 'Border World Anti-Shield Gun')
    BASE_NICKNAME = 'bw_shieldgun'
    MODEL = Weapon.CO_SHOCK_THERAPY
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_4
    MUZZLE_VELOCITY = 600
    LIFETIME = 1.0
    SHIELDGUN = True
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_PULSE


class BorderWorldOutcastgun(Gun, BorderWorldGun):
    RU_NAME = MS('Вирм', 'Wyrm')
    RU_NAME_DESC = MS('Пушка Изгоев', 'Outcast gun')
    BASE_NICKNAME = 'bw_outcastgun'
    MODEL = Weapon.CO_RAILDADDY
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_4
    MUZZLE_VELOCITY = 700
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_PARTICLE


class BorderWorldCivgun(Gun, BorderWorldGun, Civgun):
    RU_NAME = MS('Ангелито', "Angelito")
    RU_NAME_DESC = MS('Гражданская пушка пограничья', 'Border World civilian gun')
    BASE_NICKNAME = 'bw_civgun'
    MODEL = Weapon.CO_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_PHOTON


class BorderWorldPirategun(Gun, BorderWorldGun, Pirategun):
    RU_NAME = MS('Драгун', 'Dragoon')
    RU_NAME_DESC = MS('Пушка пиратов пограничья', 'Border World pirate gun')
    BASE_NICKNAME = 'bw_pirategun'
    MODEL = Weapon.CO_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_LASER


class AsfLightgun(Gun, LibertyGun):
    RU_NAME = MS('Бриллиант', 'Diamondback')
    RU_NAME_DESC = MS('Тяжелая пушка СБА', 'ASF heavy gun')
    BASE_NICKNAME = 'asf_lightgun'
    MODEL = Weapon.LI_AUTO_CANNON
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_2
    MUZZLE_VELOCITY = 600
    LIFETIME = 1.2
    FX_FACTION = WeaponFX.FX_LI
    FX_APPEARANCE = WeaponFX.FX_DIAMOND


class AsfDiamondback(Gun, LibertyGun):
    DAMAGE_MULTIPLIER = 1.35
    RU_NAME = MS('Бриллиант', 'Diamondback')
    RU_NAME_DESC = MS('Тяжелая пушка СБА', 'ASF heavy gun')
    BASE_NICKNAME = 'asf_heavygun'
    MODEL = Weapon.LI_AUTO_CANNON
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_2
    MUZZLE_VELOCITY = 800
    LIFETIME = 1.5
    FX_FACTION = WeaponFX.FX_SP
    FX_APPEARANCE = WeaponFX.FX_DIAMOND
