from world.names import *
from universe.markets import MarketCommodity


POD_RAWMATS = 1
POD_HIGHTECH = 2
POD_FOODS = 3
POD_CONSUMER = 4
POD_MEDICAL = 5
POD_MUNITIONS = 6
POD_CONTRABAND = 7
POD_REFINEDMATS = 8
POD_INDUSTRIAL = 9
POD_TRANSPARTS = 10
POD_MACHINES = 11
POD_ELECTRONICS = 12

ICON_DIAMONDS = 1
ICON_ROID = 2
ICON_REFINEDMATS = 3
ICON_BATTERY = 4
ICON_METAL = 5
ICON_HFUEL = 6
ICON_INDUSTRIAL = 7
ICON_HULLPANELS = 8
ICON_TLRPARTS = 9
ICON_ENGINECOMP = 10
ICON_MUNITIONS = 11
ICON_GREATFOOD = 12
ICON_ELECTRONICS = 13
ICON_WATERROID = 14
ICON_CHEMICAL = 15
ICON_FOOD = 16
ICON_CONSUMER = 17
ICON_DRUGS = 18
ICON_LIGHTARMS = 19
ICON_TOXIC = 20
ICON_FERTILIZER = 21
ICON_MACHINES = 22


class Commodity(MarketCommodity):
    ALIAS = None
    RU_NAME = None
    NICKNAME = None
    POD = None
    ICON = None

    DEFAULT_PRICE = 100
    PRICE_BEST_RATE = 0.25
    PRICE_CHEAP_RATE = 0.5
    PRICE_NORMAL_RATE = 0.75
    PRICE_BAD_RATE = 1

    PRICE_STEP = 20

    BASE_COMMODITY = True

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def __init__(self, ids):
        self.ids = ids

        self.ids_name = ids.new_name(self.get_ru_name())
        # self.ids_info = ids.new_info(
        #     InfocardBuilder.build_equip_infocard(
        #         self.get_ru_fullname(),
        #         self.get_ru_description_content()
        #     )
        # )

    def get_ru_name(self):
        return self.RU_NAME

    def get_best_price(self):
        return self.DEFAULT_PRICE * self.PRICE_BEST_RATE

    def get_cheap_price(self):
        return self.DEFAULT_PRICE * self.PRICE_CHEAP_RATE

    def get_normal_price(self):
        return self.DEFAULT_PRICE * self.PRICE_NORMAL_RATE

    def get_bad_price(self):
        return self.DEFAULT_PRICE * self.PRICE_BAD_RATE

    def get_price_step(self, depth):
        # TODO: increase by depth
        return self.PRICE_STEP

    def get_consume_price(self, produce_price, depth):
        price = produce_price
        for i in range(1, depth+1):
            price += self.get_price_step(i)

        return price


class BasicCommodity:
    DEFAULT_PRICE = 50


class DefaultCommodity:
    DEFAULT_PRICE = 50


class Roid:
    DEFAULT_PRICE = 100


class Alloy:
    DEFAULT_PRICE = 200


class Product:
    DEFAULT_PRICE = 400


class Luxury:
    DEFAULT_PRICE = 500


class TerraformMinerals(BasicCommodity, Commodity):
    ALIAS = TERRAFORM_MINERALS
    RU_NAME = 'Минеральные удобрения'
    NICKNAME = 'comm_terraform_minerals'
    POD = POD_FOODS
    ICON = ICON_FERTILIZER


class TerraformGases(BasicCommodity, Commodity):
    ALIAS = TERRAFORM_GASES
    RU_NAME = 'Терраформирующие газы'
    NICKNAME = 'comm_terraform_gases'
    POD = POD_FOODS
    ICON = ICON_CHEMICAL
    BASE_COMMODITY = False


class LaserBeamParts(BasicCommodity, Commodity):
    ALIAS = LASER_BEAM_PARS
    RU_NAME = 'Компоненты излучателя'
    NICKNAME = 'comm_laserbeam_components'
    POD = POD_MACHINES
    ICON = ICON_MACHINES
    BASE_COMMODITY = False


class BasicWater(BasicCommodity, Commodity):
    ALIAS = BASIC_WATER
    RU_NAME = 'Вода'
    NICKNAME = 'comm_basic_water'
    POD = POD_RAWMATS
    ICON = ICON_WATERROID


class BasicOxygen(BasicCommodity, Commodity):
    ALIAS = BASIC_OXYGEN
    RU_NAME = 'Кислород'
    NICKNAME = 'comm_basic_oxygen'
    POD = POD_HIGHTECH
    ICON = ICON_CHEMICAL


class BasicFood(BasicCommodity, Commodity):
    ALIAS = BASIC_FOOD
    RU_NAME = 'Синтетическая пища'
    NICKNAME = 'comm_basic_food'
    POD = POD_FOODS
    ICON = ICON_FOOD


class BasicConsumer(BasicCommodity, Commodity):
    ALIAS = BASIC_CONSUMER
    RU_NAME = 'Ширпотреб'
    NICKNAME = 'comm_basic_consumer'
    POD = POD_CONSUMER
    ICON = ICON_CONSUMER


class BasicMeds(BasicCommodity, Commodity):
    ALIAS = BASIC_MEDS
    RU_NAME = 'Медпрепараты'
    NICKNAME = 'comm_basic_meds'
    POD = POD_MEDICAL
    ICON = ICON_DRUGS


class BasicWeapons(BasicCommodity, Commodity):
    ALIAS = BASIC_WEAPONS
    RU_NAME = 'Стрелковое оружие'
    NICKNAME = 'comm_basic_weapons'
    POD = POD_MUNITIONS
    ICON = ICON_LIGHTARMS


class BasicToxic(BasicCommodity, Commodity):
    ALIAS = BASIC_TOXIC
    RU_NAME = 'Токсичные отходы'
    NICKNAME = 'comm_basic_toxic'
    POD = POD_CONTRABAND
    ICON = ICON_TOXIC


class Metal(DefaultCommodity, Commodity):
    ALIAS = METAL
    RU_NAME = 'Металлолом'
    NICKNAME = 'comm_scrap_metal'
    POD = POD_REFINEDMATS
    ICON = ICON_REFINEDMATS
    BASE_COMMODITY = False


class PowerSolarEmpty(DefaultCommodity, Commodity):
    ALIAS = POWER_SOLAR_EMPTY
    RU_NAME = 'Разряженные генераторы'
    NICKNAME = 'comm_power_solar_empty'
    POD = POD_HIGHTECH
    ICON = ICON_BATTERY


class PowerSolar(DefaultCommodity, Commodity):
    ALIAS = POWER_SOLAR
    RU_NAME = 'Заряженные генераторы'
    NICKNAME = 'comm_power_solar'
    POD = POD_HIGHTECH
    ICON = ICON_BATTERY


class AlloyBasic(DefaultCommodity, Commodity):
    ALIAS = ALLOY_BASIC
    RU_NAME = 'Простой сплав'
    NICKNAME = 'comm_alloy_basic'
    POD = POD_INDUSTRIAL
    ICON = ICON_METAL


class GasBalloons(DefaultCommodity, Commodity):
    ALIAS = GAS_BALLOONS
    RU_NAME = 'Газовые баллоны'
    NICKNAME = 'comm_gas_balloons'
    POD = POD_TRANSPARTS
    ICON = ICON_HFUEL


class GasFuel(DefaultCommodity, Commodity):
    ALIAS = GAS_FUEL
    RU_NAME = 'Газовое топливо'
    NICKNAME = 'comm_gas_fuel'
    POD = POD_TRANSPARTS
    ICON = ICON_HFUEL


class ShipHullPanels(Product, Commodity):
    ALIAS = SHIP_HULL_PANELS
    RU_NAME = 'Панели обшивки корабля'
    NICKNAME = 'comm_shiphull_panels'
    POD = POD_REFINEDMATS
    ICON = ICON_HULLPANELS


class Diamonds(Roid, Commodity):
    ALIAS = DIAMONDS
    RU_NAME = 'Алмазы'
    NICKNAME = 'comm_roid_diamonds'
    POD = POD_RAWMATS
    ICON = ICON_DIAMONDS


class LuxuryDiamonds(Luxury, Commodity):
    ALIAS = LUXURY_DIAMONDS
    RU_NAME = 'Алмазные украшения'
    NICKNAME = 'comm_luxury_diamonds'
    POD = POD_CONSUMER
    ICON = ICON_DIAMONDS


class Niobium(Roid, Commodity):
    ALIAS = NIOBIUM
    RU_NAME = 'Ниобий'
    NICKNAME = 'comm_roid_niobium'
    POD = POD_RAWMATS
    ICON = ICON_ROID


class ProdMachines(Product, Commodity):
    ALIAS = PROD_MACHINES
    RU_NAME = 'Промышленные станки'
    NICKNAME = 'comm_prod_machines'
    POD = POD_MACHINES
    ICON = ICON_INDUSTRIAL


class StationPanels(Product, Commodity):
    ALIAS = STATION_PANELS
    RU_NAME = 'Панели обшивки станций'
    NICKNAME = 'comm_station_panels'
    POD = POD_REFINEDMATS
    ICON = ICON_HULLPANELS


class AlloyHeavy(Alloy, Commodity):
    ALIAS = ALLOY_HEAVY
    RU_NAME = 'Суперсплав'
    NICKNAME = 'comm_alloy_heavy'
    POD = POD_INDUSTRIAL
    ICON = ICON_METAL


class RoidMinerParts(Product, Commodity):
    ALIAS = ROID_MINER_PARTS
    RU_NAME = 'Детали рудокопа'
    NICKNAME = 'comm_roidminer_parts'
    POD = POD_MACHINES
    ICON = ICON_INDUSTRIAL


class SmelterParts(Product, Commodity):
    ALIAS = SMELTER_PARTS
    RU_NAME = 'Детали плавильной установки'
    NICKNAME = 'comm_smelter_parts'
    POD = POD_MACHINES
    ICON = ICON_INDUSTRIAL


class WaterExtra(Luxury, Commodity):
    ALIAS = WATER_EXTRA
    RU_NAME = 'Чистая вода'
    NICKNAME = 'comm_water_extra'
    POD = POD_RAWMATS
    ICON = ICON_WATERROID


class Berilium(Roid, Commodity):
    ALIAS = BERILIUM
    RU_NAME = 'Берилий'
    NICKNAME = 'comm_roid_berilium'
    POD = POD_RAWMATS
    ICON = ICON_ROID


class Nicollum(Roid, Commodity):
    ALIAS = NICOLLUM
    RU_NAME = 'Никель'
    NICKNAME = 'comm_roid_nicollum'
    POD = POD_RAWMATS
    ICON = ICON_ROID


class LuxuryGoods(Luxury, Commodity):
    ALIAS = LUXURY_GOODS
    RU_NAME = 'Роскошные товары'
    NICKNAME = 'comm_luxury_consumer'
    POD = POD_CONSUMER
    ICON = ICON_CONSUMER


class TLRParts(Product, Commodity):
    ALIAS = TLR_PARTS
    RU_NAME = 'Детали торгового пути'
    NICKNAME = 'comm_tlr_parts'
    POD = POD_REFINEDMATS
    ICON = ICON_TLRPARTS


class EngineParts(Product, Commodity):
    ALIAS = ENGINE_PARTS
    RU_NAME = 'Детали двигателей'
    NICKNAME = 'COMM_ENGINE_COMPONENTS'
    POD = POD_TRANSPARTS
    ICON = ICON_ENGINECOMP


class JumpGateParts(Product, Commodity):
    ALIAS = JUMPGATE_PARTS
    RU_NAME = 'Детали гиперворот'
    NICKNAME = 'comm_jumpgate_parts'
    POD = POD_REFINEDMATS
    ICON = ICON_TLRPARTS


class AlloyTemperature(Alloy, Commodity):
    ALIAS = ALLOY_TEMPERATURE
    RU_NAME = 'Высокотемпературный сплав'
    NICKNAME = 'comm_alloy_temperature'
    POD = POD_INDUSTRIAL
    ICON = ICON_METAL


class MiningEquipment(Product, Commodity):
    ALIAS = MINING_EQUIPMENT
    RU_NAME = 'Горное оборудование'
    NICKNAME = 'comm_mining_equip'
    POD = POD_MACHINES
    ICON = ICON_INDUSTRIAL


class Polymers(Product, Commodity):
    ALIAS = POLYMERS
    RU_NAME = 'Полимеры'
    NICKNAME = 'comm_polymers'
    POD = POD_HIGHTECH
    ICON = ICON_CHEMICAL


class Uranium(Roid, Commodity):
    ALIAS = URANIUM
    RU_NAME = 'Уран'
    NICKNAME = 'comm_roid_uranium'
    POD = POD_RAWMATS
    ICON = ICON_ROID


class Plumbum(Roid, Commodity):
    ALIAS = PLUMBUM
    RU_NAME = 'Свинец'
    NICKNAME = 'comm_roid_plumbum'
    POD = POD_RAWMATS
    ICON = ICON_ROID


class Reactors(Product, Commodity):
    ALIAS = REACTORS
    RU_NAME = 'Компоненты реактора'
    NICKNAME = 'comm_reactors'
    POD = POD_HIGHTECH
    ICON = ICON_BATTERY


class MOXFuel(Product, Commodity):
    ALIAS = MOX_FUEL
    RU_NAME = 'Реактивное топливо'
    NICKNAME = 'comm_mox_fuel'
    POD = POD_HIGHTECH
    ICON = ICON_CHEMICAL


class Ammunition(Product, Commodity):
    ALIAS = AMMUNITION
    RU_NAME = 'Тяжелые снаряды'
    NICKNAME = 'comm_munitions'
    POD = POD_MUNITIONS
    ICON = ICON_MUNITIONS


class LuxuryFood(Luxury, Commodity):
    ALIAS = LUXURY_FOOD
    RU_NAME = 'Роскошная пища'
    NICKNAME = 'comm_luxury_food'
    POD = POD_FOODS
    ICON = ICON_GREATFOOD


class AlloyRadiation(Commodity):
    ALIAS = ALLOY_RADIATION
    RU_NAME = 'Противорадиационный сплав'
    NICKNAME = 'comm_alloy_radiation'
    POD = POD_INDUSTRIAL
    ICON = ICON_METAL


class GreenhouseParts(Product, Commodity):
    ALIAS = GREENHOUSE_PARTS
    RU_NAME = 'Оборудование оранжереи'
    NICKNAME = 'comm_greenhouse_parts'
    POD = POD_MACHINES
    ICON = ICON_REFINEDMATS


class DefenceSystems(Product, Commodity):
    ALIAS = DEFENCE_SYSTEMS
    RU_NAME = 'Защитные системы'
    NICKNAME = 'comm_greenhouse_parts'
    POD = POD_MUNITIONS
    ICON = ICON_MUNITIONS


class Gold(Roid, Commodity):
    ALIAS = GOLD
    RU_NAME = 'Золото'
    NICKNAME = 'comm_roid_gold'
    POD = POD_RAWMATS
    ICON = ICON_ROID


class Silver(Roid, Commodity):
    ALIAS = SILVER
    RU_NAME = 'Серебро'
    NICKNAME = 'comm_roid_silver'
    POD = POD_RAWMATS
    ICON = ICON_ROID


class Electronics(Product, Commodity):
    ALIAS = ELECTRONICS
    RU_NAME = 'Электроника'
    NICKNAME = 'comm_electronics'
    POD = POD_ELECTRONICS
    ICON = ICON_ELECTRONICS


class LuxuryGold(Luxury, Commodity):
    ALIAS = LUXURY_GOLD
    RU_NAME = 'Украшения'
    NICKNAME = 'comm_luxury_gold'
    POD = POD_CONSUMER
    ICON = ICON_METAL


class OpticalChips(Product, Commodity):
    ALIAS = OPTICAL_CHIPS
    RU_NAME = 'Оптические чипы'
    NICKNAME = 'comm_optical_chips'
    POD = POD_ELECTRONICS
    ICON = ICON_ELECTRONICS


class AlloyConductor(Alloy, Commodity):
    ALIAS = ALLOY_CONDUCTOR
    RU_NAME = 'Сверхпроводящий сплав'
    NICKNAME = 'comm_alloy_conductor'
    POD = POD_INDUSTRIAL
    ICON = ICON_METAL


class GasMinerParts(Product, Commodity):
    ALIAS = GAS_MINER_PARTS
    RU_NAME = 'Детали для газодобытчика'
    NICKNAME = 'comm_gasminer_parts'
    POD = POD_MACHINES
    ICON = ICON_INDUSTRIAL


class SolarPlantParts(Product, Commodity):
    ALIAS = SOLAR_PLANT_PARTS
    RU_NAME = 'Компоненты солн. генератора'
    NICKNAME = 'comm_solarplant_parts'
    POD = POD_MACHINES
    ICON = ICON_INDUSTRIAL


class ResearchEquip(Product, Commodity):
    ALIAS = RESEARCH_EQUIP
    RU_NAME = 'Точное оборудование'
    NICKNAME = 'comm_research_equip'
    POD = POD_HIGHTECH
    ICON = ICON_INDUSTRIAL
