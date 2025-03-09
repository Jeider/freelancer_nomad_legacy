from world.equipment import DefaultGood, MainEquipPrice, Icon
from world.weapon import Weapon

from fx.weapon import WeaponFX


RU_MINING_GAS_BONUS = 'Повышенные повреждения по газовым облакам и ледяным астероидам'
RU_MINING_JUNK_BONUS = 'Повышенные повреждения по залежам прессованного мусора'
RU_MINING_AST_BONUS = 'Повышенные повреждения по добываемым астероидам'
RU_EXPLORATION_BONUS = 'Показывает наиболее выгодные для добычи астероиды, прессованный мусор, газовые облака или ледяные астероиды'

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

LIGHTGUN = 'light'
HEAVYGUN = 'heavy'
CIVGUN = 'civilian'
PIRATEGUN = 'pirate'
HUNTERGUN = 'hunter'
SHIELDGUN = 'shield'


class FactionGun:
    WEAPON_FACTION = None

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)


class RheinlandGun(FactionGun):
    WEAPON_FACTION = Weapon.FACTION_RH


class LibertyGun(FactionGun):
    WEAPON_FACTION = Weapon.FACTION_LI


class BretoniaGun(FactionGun):
    WEAPON_FACTION = Weapon.FACTION_BR


class KusariGun(FactionGun):
    WEAPON_FACTION = Weapon.FACTION_KU


class BorderWorldGun(FactionGun):
    WEAPON_FACTION = Weapon.FACTION_CO


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

    def get_ru_fullname(self):
        return '{described_name} {name}'.format(
            name=self.get_ru_name(),
            described_name=self.RU_NAME_DESC,
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

        faction_bonus_text = RU_FEATURES_PER_FACTION.get(self.WEAPON_FACTION)
        if faction_bonus_text:
            content.append(faction_bonus_text)

        return content

    def is_generic(self):
        if hasattr(self, 'WEAPON_FACTION') and self.WEAPON_FACTION is not None:
            if hasattr(self, 'GENERIC_KIND') and self.GENERIC_KIND is not None:
                return True


class RheinlandLightgun(Gun, RheinlandGun, Lightgun):
    RU_NAME = 'Гремучий змей'
    RU_NAME_DESC = 'Легкая пушка рейнландских военных'
    BASE_NICKNAME = 'rh_lightgun'
    MODEL = Weapon.RH_GAMMA_BEAMER
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 700
    LIFETIME = 1.0
    FX_FACTION = WeaponFX.FX_RH
    FX_APPEARANCE = WeaponFX.FX_TACHYON


class RheinlandHeavygun(Gun, RheinlandGun, Heavygun):
    RU_NAME = 'Огненный поцелуй'
    RU_NAME_DESC = 'Тяжелая пушка рейнландских военных'
    BASE_NICKNAME = 'rh_heavygun'
    MODEL = Weapon.RH_PROTON_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_2
    MUZZLE_VELOCITY = 500
    LIFETIME = 1.2
    FX_FACTION = WeaponFX.FX_RH
    FX_APPEARANCE = WeaponFX.FX_PLASMA


class RheinlandCivgun(Gun, RheinlandGun, Civgun):
    RU_NAME = 'Звездный луч'
    RU_NAME_DESC = 'Базовая рейнландская пушка'
    BASE_NICKNAME = 'rh_civgun'
    MODEL = Weapon.RH_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_RH
    FX_APPEARANCE = WeaponFX.FX_LASER


class RheinlandHuntergun(Gun, RheinlandGun, Huntergun):
    RU_NAME = 'Незримый клинок'
    RU_NAME_DESC = 'Пушка рейнландских наемников'
    BASE_NICKNAME = 'rh_huntergun'
    MODEL = Weapon.RH_GAMMA_BEAMER
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8
    FX_FACTION = WeaponFX.FX_RH
    FX_APPEARANCE = WeaponFX.FX_PARTICLE


class RheinlandPirategun(Gun, RheinlandGun, Pirategun):
    RU_NAME = 'Наттер'
    RU_NAME_DESC = 'Пушка рейнландских пиратов'
    BASE_NICKNAME = 'rh_pirategun'
    MODEL = Weapon.RH_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_LASER


class RheinlandHessiangun(Gun, RheinlandGun):
    RU_NAME = 'Ротер Блиц'
    RU_NAME_DESC = 'Пушка гессенцев'
    BASE_NICKNAME = 'rh_hessiangun'
    MODEL = Weapon.RH_GAMMA_BEAMER
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 700
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_PARTICLE


class RheinlandJunkergun(Gun, RheinlandGun):
    RU_NAME = 'Стервятник'
    RU_NAME_DESC = 'Пушка мусорщиков'
    BASE_NICKNAME = 'rh_junkergun'
    MODEL = Weapon.CO_SHOCK_THERAPY
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_PHOTON


class RheinlandShieldgun(Gun, RheinlandGun, Shieldgun):
    RU_NAME = 'Пламенное проклятие'
    RU_NAME_DESC = 'Рейнландская противощитовая пушка'
    BASE_NICKNAME = 'rh_shieldgun'
    MODEL = Weapon.RH_PROTON_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_4
    MUZZLE_VELOCITY = 600
    LIFETIME = 1.0
    SHIELDGUN = True
    FX_FACTION = WeaponFX.FX_RH
    FX_APPEARANCE = WeaponFX.FX_PULSE


class RheinlandHeavyTurret(Gun, RheinlandGun):
    DAMAGE_MULTIPLER = 2
    RU_NAME = 'Рука Смерти'
    RU_NAME_DESC = 'Тяжелая рейнландская турель'
    BASE_NICKNAME = 'rh_heavyturret'
    MODEL = Weapon.RH_PLASMA_GAT_CANNON
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 700
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_RH
    FX_APPEARANCE = WeaponFX.FX_PULSE
    IS_TURRET = True
    EXTRA_SHIELD_DAMAGE_FACTOR = 0.5


class LibertyLightgun(Gun, LibertyGun, Lightgun):
    RU_NAME = 'Возмездие'
    RU_NAME_DESC = 'Легкая пушка военных Либерти'
    BASE_NICKNAME = 'li_lightgun'
    MODEL = Weapon.LI_LASER_BEAM
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8
    FX_FACTION = WeaponFX.FX_LI
    FX_APPEARANCE = WeaponFX.FX_LASER


class LibertyHeavygun(Gun, LibertyGun, Heavygun):
    RU_NAME = 'Молот магмы'
    RU_NAME_DESC = 'Тяжелая пушка военных Либерти'
    BASE_NICKNAME = 'li_heavygun'
    MODEL = Weapon.LI_HEAVY_ION_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_2
    MUZZLE_VELOCITY = 500
    LIFETIME = 1.2
    FX_FACTION = WeaponFX.FX_LI
    FX_APPEARANCE = WeaponFX.FX_PLASMA


class LibertyCivgun(Gun, LibertyGun, Civgun):
    RU_NAME = 'Справедливость'
    RU_NAME_DESC = 'Базовая пушка Либерти'
    BASE_NICKNAME = 'li_civgun'
    MODEL = Weapon.LI_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8
    FX_FACTION = WeaponFX.FX_CI
    FX_APPEARANCE = WeaponFX.FX_LASER


class LibertyHuntergun(Gun, LibertyGun, Huntergun):
    RU_NAME = 'Винтчестер'
    RU_NAME_DESC = 'Пушка наемников Либерти'
    BASE_NICKNAME = 'li_huntergun'
    MODEL = Weapon.LI_PLASMA_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_4
    MUZZLE_VELOCITY = 700
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_CI
    FX_APPEARANCE = WeaponFX.FX_TACHYON


class LibertyPirategun(Gun, LibertyGun, Pirategun):
    RU_NAME = 'Азраель'
    RU_NAME_DESC = 'Пушка пиратов Либерти'
    BASE_NICKNAME = 'li_pirategun'
    MODEL = Weapon.RH_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_PHOTON


class LibertyRoguegun(Gun, LibertyGun):
    RU_NAME = 'Вассаго'
    RU_NAME_DESC = 'Пушка разбойников Либерти'
    BASE_NICKNAME = 'li_roguegun'
    MODEL = Weapon.LI_PLASMA_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_LASER


class LibertyStarlinegun(Gun, LibertyGun):
    RU_NAME = 'Разбойник'
    RU_NAME_DESC = 'Пушка банды Старлайна'
    BASE_NICKNAME = 'li_starlinegun'
    MODEL = Weapon.LI_LASER_BEAM
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 700
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_PARTICLE


class LibertyShieldgun(Gun, LibertyGun, Shieldgun):
    RU_NAME = 'Клинок лавы'
    RU_NAME_DESC = 'Либертийская противощитовая пушка'
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
    RU_NAME = 'Растворитель'
    RU_NAME_DESC = 'Легкая пушка бретонских военных'
    BASE_NICKNAME = 'br_lightgun'
    MODEL = Weapon.BR_MASS_DRIVER
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 700
    LIFETIME = 1.0
    FX_FACTION = WeaponFX.FX_BR
    FX_APPEARANCE = WeaponFX.FX_TACHYON


class BretoniaHeavygun(Gun, BretoniaGun, Heavygun):
    RU_NAME = 'Небесный путь'
    RU_NAME_DESC = 'Тяжелая пушка бретонских военных'
    BASE_NICKNAME = 'br_heavygun'
    MODEL = Weapon.BR_RAILGUN
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_4
    MUZZLE_VELOCITY = 700
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_BR
    FX_APPEARANCE = WeaponFX.FX_PARTICLE


class BretoniaCivgun(Gun, BretoniaGun, Civgun):
    RU_NAME = 'Флешпоинт'
    RU_NAME_DESC = 'Базовая бретонская пушка'
    BASE_NICKNAME = 'br_civgun'
    MODEL = Weapon.BR_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_BR
    FX_APPEARANCE = WeaponFX.FX_PHOTON


class BretoniaHuntergun(Gun, BretoniaGun, Huntergun):
    RU_NAME = 'Потрошитель'
    RU_NAME_DESC = 'Пушка бретонских наемников'
    BASE_NICKNAME = 'br_huntergun'
    MODEL = Weapon.BR_MASS_DRIVER
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_BR
    FX_APPEARANCE = WeaponFX.FX_NEUTRON


class BretoniaPirategun(Gun, BretoniaGun, Pirategun):
    RU_NAME = 'Скорпион'
    RU_NAME_DESC = 'Пушка бретонских пиратов'
    BASE_NICKNAME = 'br_pirategun'
    MODEL = Weapon.BR_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_4
    MUZZLE_VELOCITY = 700
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_PARTICLE


class BretoniaXenosgun(Gun, BretoniaGun):
    RU_NAME = 'Тарантул'
    RU_NAME_DESC = 'Пушка ксеносов'
    BASE_NICKNAME = 'br_xenosgun'
    MODEL = Weapon.CO_RAILDADDY
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_3
    MUZZLE_VELOCITY = 700
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_PLASMA


class BretoniaIragun(Gun, BretoniaGun):
    RU_NAME = 'Маттертиф'
    RU_NAME_DESC = 'Пушка ирландских сепаратистов'
    BASE_NICKNAME = 'br_iragun'
    MODEL = Weapon.BR_MASS_DRIVER
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_4
    MUZZLE_VELOCITY = 700
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_NEUTRON


class BretoniaShieldgun(Gun, BretoniaGun, Shieldgun):
    RU_NAME = 'Солнечный путь'
    RU_NAME_DESC = 'Бретонская противощитовая пушка'
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
    RU_NAME = 'Гром'
    RU_NAME_DESC = 'Легкая пушка кусарийских военных'
    BASE_NICKNAME = 'ku_lightgun'
    MODEL = Weapon.KU_ION_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8
    FX_FACTION = WeaponFX.FX_KU
    FX_APPEARANCE = WeaponFX.FX_PHOTON


class KusariHeavygun(Gun, KusariGun, Heavygun):
    RU_NAME = 'Дезинфектор'
    RU_NAME_DESC = 'Тяжелая пушка кусарийских военных'
    BASE_NICKNAME = 'ku_heavygun'
    MODEL = Weapon.KU_AUTO_TESLA
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_4
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_KU
    FX_APPEARANCE = WeaponFX.FX_NEUTRON


class KusariCivgun(Gun, KusariGun, Civgun):
    RU_NAME = 'Гелиос'
    RU_NAME_DESC = 'Базовая кусарийская пушка'
    BASE_NICKNAME = 'ku_civgun'
    MODEL = Weapon.KU_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_CI
    FX_APPEARANCE = WeaponFX.FX_PHOTON


class KusariHuntergun(Gun, KusariGun, Huntergun):
    RU_NAME = 'Ярость'
    RU_NAME_DESC = 'Пушка кусарийская наемников'
    BASE_NICKNAME = 'ku_huntergun'
    MODEL = Weapon.KU_ION_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_KU
    FX_APPEARANCE = WeaponFX.FX_LASER


class KusariPirategun(Gun, KusariGun, Pirategun):
    RU_NAME = 'Танто'
    RU_NAME_DESC = 'Пушка кусарийская пиратов'
    BASE_NICKNAME = 'ku_pirategun'
    MODEL = Weapon.KU_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_NEUTRON


class KusariShinobigun(Gun, KusariGun):
    RU_NAME = 'Ниндзято'
    RU_NAME_DESC = 'Пушка клана Шиноби'
    BASE_NICKNAME = 'ku_shinobigun'
    MODEL = Weapon.CO_SHOCK_THERAPY
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_TACHYON


class KusariDragongun(Gun, KusariGun):
    RU_NAME = 'Вакидзаси'
    RU_NAME_DESC = 'Пушка кровавых драконов'
    BASE_NICKNAME = 'ku_dragongun'
    MODEL = Weapon.KU_ION_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_LASER


class KusariShieldgun(Gun, KusariGun, Shieldgun):
    RU_NAME = 'Успокоитель'
    RU_NAME_DESC = 'Кусарийская противощитовая пушка'
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
    RU_NAME = 'Цербер'
    RU_NAME_DESC = 'Легкая пушка Ордена'
    BASE_NICKNAME = 'or_lightgun'
    MODEL = Weapon.CO_PROTON_COOKER
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_TACHYON


class OrderHeavygun(Gun, BorderWorldGun, Heavygun):
    RU_NAME = 'Оникс'
    RU_NAME_DESC = 'Тяжелая пушка Ордена'
    BASE_NICKNAME = 'or_heavygun'
    MODEL = Weapon.CO_SHOCK_THERAPY
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_3
    MUZZLE_VELOCITY = 700
    LIFETIME = 3
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_PLASMA


class BorderWorldCorsairgun(Gun, BorderWorldGun):
    RU_NAME = 'Саламанка'
    RU_NAME_DESC = 'Пушка Корсаров'
    BASE_NICKNAME = 'bw_corsairgun'
    MODEL = Weapon.CO_RAILDADDY
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_4
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_NEUTRON


class BorderWorldShieldgun(Gun, BorderWorldGun, Shieldgun):
    RU_NAME = 'Рапира'
    RU_NAME_DESC = 'Противощитовая пушка пограничья'
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
    RU_NAME = 'Вирм'
    RU_NAME_DESC = 'Пушка Изгоев'
    BASE_NICKNAME = 'bw_outcastgun'
    MODEL = Weapon.CO_RAILDADDY
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_4
    MUZZLE_VELOCITY = 700
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_PARTICLE


class BorderWorldCivgun(Gun, BorderWorldGun, Civgun):
    RU_NAME = 'Ангелито'
    RU_NAME_DESC = 'Гражданская пушка пограничья'
    BASE_NICKNAME = 'bw_civgun'
    MODEL = Weapon.CO_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_PHOTON


class BorderWorldPirategun(Gun, BorderWorldGun, Pirategun):
    RU_NAME = 'Драгун'
    RU_NAME_DESC = 'Пушка пиратов пограничья'
    BASE_NICKNAME = 'bw_pirategun'
    MODEL = Weapon.CO_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 600
    LIFETIME = 1
    FX_FACTION = WeaponFX.FX_PI
    FX_APPEARANCE = WeaponFX.FX_LASER
