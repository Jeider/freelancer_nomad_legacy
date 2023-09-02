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

RU_MINING_GAS_BONUS = 'Повышенные повреждения по газовым облакам и ледяным астероидам'
RU_MINING_JUNK_BONUS = 'Повышенные повреждения по залежам прессованного мусора'
RU_MINING_AST_BONUS = 'Повышенные повреждения по добываемым астероидам'
RU_EXPLORATION_BONUS = 'Показывает наиболее выгодные для добычи астероиды, прессованный мусор, газовые облака или ледяные астероиды'

RU_SHIELDGUN_BONUS = 'Это противощитовая пушка и она наносит внушительные повреждения по щиту за счет отсутствующих повреждений по корпусу'

RU_RATE_10 = 'Обладает максимальной скорострельностью за счет минимальной мощности'
RU_RATE_8 = 'Обладает высокой скорострельностью за счет низкой мощности'
RU_RATE_6 = 'Обладает повышенной скорострельностью за счет пониженной мощности'
RU_RATE_4 = 'Обладает умеренной мощностью и скорострельностью'
RU_RATE_3 = 'Характеризуется повышенной мощностью за счет пониженной скорострельности'
RU_RATE_2 = 'Характеризуется высокой мощностью за счет низкой скорострельности'
RU_RATE_1 = 'Характеризуется максимальной мощностью за счет минимальной скорострельности'

RU_RATE_TEXT_PER_WEAPON_RATE = {
    Weapon.REFIRE_RATE_10: RU_RATE_10,
    Weapon.REFIRE_RATE_8: RU_RATE_8,
    Weapon.REFIRE_RATE_6: RU_RATE_6,
    Weapon.REFIRE_RATE_4: RU_RATE_4,
    Weapon.REFIRE_RATE_3: RU_RATE_3,
    Weapon.REFIRE_RATE_2: RU_RATE_2,
    Weapon.REFIRE_RATE_1: RU_RATE_1,
}

RU_EFFICIENT_CIV = 'Класс эффективности: гражданский'
RU_EFFICIENT_PIRATE = 'Класс эффективности: профессиональный'
RU_EFFICIENT_MAIN = 'Класс эффективности: военный'

RU_EFFICIENT_TEXT_PER_EQUIP_TYPE = {
    Weapon.EQUIP_CIV: RU_EFFICIENT_CIV,
    Weapon.EQUIP_PIRATE: RU_EFFICIENT_PIRATE,
    Weapon.EQUIP_MAIN: RU_EFFICIENT_MAIN,
}


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

    def get_ru_fullname(self):
        return '{described_name} {name}'.format(
            name=self.get_ru_name(),
            described_name=self.RU_NAME_DESC,
        )


    def get_ru_description_content(self):
        content = []

        rate_text = RU_RATE_TEXT_PER_WEAPON_RATE.get(self.REFIRE_RATE)
        if rate_text:
            content.append(rate_text)

        efficient_text = RU_EFFICIENT_TEXT_PER_EQUIP_TYPE.get(self.EQUIP_TYPE)
        if efficient_text:
            content.append(efficient_text)

        if self.SHIELDGUN:
            content.append(RU_SHIELDGUN_BONUS)


        return content


class RheinlandLightgun(Gun):
    RU_NAME = 'Гремучий змей'
    RU_NAME_DESC = 'Легкая пушка рейнландских военных'
    BASE_NICKNAME = RH_LIGHTGUN
    MODEL = Weapon.RH_GAMMA_BEAMER
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 700
    LIFETIME = 1.0


class RheinlandHeavygun(Gun):
    RU_NAME = 'Огненный поцелуй'
    RU_NAME_DESC = 'Тяжелая пушка рейнландских военных'
    BASE_NICKNAME = RH_HEAVYGUN
    MODEL = Weapon.RH_PROTON_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_MAIN
    REFIRE_RATE = Weapon.REFIRE_RATE_2
    MUZZLE_VELOCITY = 500
    LIFETIME = 1.2


class RheinlandCivgun(Gun):
    RU_NAME = 'Звездный луч'
    RU_NAME_DESC = 'Базовая рейнландская пушка'
    BASE_NICKNAME = RH_CIVGUN
    MODEL = Weapon.RH_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 600
    LIFETIME = 0.8


class RheinlandHuntergun(Gun):
    RU_NAME = 'Незримый клинок'
    RU_NAME_DESC = 'Пушка рейнландских наемников'
    BASE_NICKNAME = RH_HUNTERGUN
    MODEL = Weapon.RH_GAMMA_BEAMER
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8


class RheinlandShieldgun(Gun):
    RU_NAME = 'Пламенное проклятие'
    RU_NAME_DESC = 'Рейнландская противощитовая пушка'
    BASE_NICKNAME = RH_SHIELDGUN
    MODEL = Weapon.RH_PROTON_BLASTER
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_4
    MUZZLE_VELOCITY = 600
    LIFETIME = 1.0
    SHIELDGUN = True


class RheinlandPirategun(Gun):
    RU_NAME = 'Наттер'
    RU_NAME_DESC = 'Пушка рейнландских пиратов'
    BASE_NICKNAME = RH_PIRATEGUN
    MODEL = Weapon.RH_THRUSTGUN
    EQUIP_TYPE = Weapon.EQUIP_CIV
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 750
    LIFETIME = 0.8


class RheinlandHessiangun(Gun):
    RU_NAME = 'Ротер Блиц'
    RU_NAME_DESC = 'Пушка гессенцев'
    BASE_NICKNAME = RH_HESSIANGUN
    MODEL = Weapon.RH_GAMMA_BEAMER
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_6
    MUZZLE_VELOCITY = 700
    LIFETIME = 1


class RheinlandJunkergun(Gun):
    RU_NAME = 'Скорпион'
    RU_NAME_DESC = 'Пушка рейнландских мусорщиков'
    BASE_NICKNAME = RH_JUNKERGUN
    MODEL = Weapon.CO_SHOCK_THERAPY
    EQUIP_TYPE = Weapon.EQUIP_PIRATE
    REFIRE_RATE = Weapon.REFIRE_RATE_8
    MUZZLE_VELOCITY = 600
    LIFETIME = 1

