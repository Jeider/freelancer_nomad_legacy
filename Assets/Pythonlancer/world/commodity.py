from world.names import *
from text import ru_info_commodity as ru_info
from text.infocards import InfocardBuilder


POD_RAWMATS = 'rawmats'
POD_HIGHTECH = 'hightech'
POD_FOODS = 'foods'
POD_CONSUMER = 'consumer'
POD_MEDICAL = 'medical'
POD_MUNITIONS = 'munitions'
POD_CONTRABAND = 'contraband'
POD_REFINEDMATS = 'refinedmats'
POD_INDUSTRIAL = 'industrial'
POD_TRANSPARTS = 'transparts'
POD_MACHINES = 'machines'
POD_ELECTRONICS = 'electronics'

ICON_DIAMONDS = 'commod_diamonds'
ICON_ROID = 'crudemats'
ICON_REFINEDMATS = 'refinedmats'
ICON_BATTERY = 'equipicon_shieldbatteries'
ICON_METAL = 'commod_metals'
ICON_HFUEL = 'commod_hfuels'
ICON_INDUSTRIAL = 'industrial'
ICON_HULLPANELS = 'commod_hullpanels'
ICON_TLRPARTS = 'commod_tradelaneparts'
ICON_ENGINECOMP = 'commod_enginecomponents'
ICON_MUNITIONS = 'munitions'
ICON_GREATFOOD = 'commod_luxuryfoods'
ICON_ELECTRONICS = 'electronics'
ICON_WATERROID = 'commod_waterice'
ICON_CHEMICAL = 'commod_chemicals'
ICON_FOOD = 'commod_foodrations'
ICON_CONSUMER = 'commod_consumergoods'
ICON_DRUGS = 'commod_drugs'
ICON_LIGHTARMS = 'commod_lightarms'
ICON_TOXIC = 'commod_toxicwaste'
ICON_FERTILIZER = 'commod_fertilizer'
ICON_MACHINES = 'commod_machines'
ICON_CREDITS = 'commod_credits'
ICON_ARTIFACTS = 'commod_legalartifacts'
ICON_BACTERIA = 'commod_nomadbacteria'
ICON_CHIP = 'commod_opticalchips'
ICON_OPTRONICS = 'commod_optronics'

EQUIP_TEMPLATE = '''[Commodity]
nickname = {nickname}
ids_name = {ids_name}
ids_info = {ids_info}
units_per_container = {units_per_container}
pod_appearance = cargopod_{pod}
loot_appearance = lootcrate_{pod}
decay_per_second = {decay_per_second}
volume = 1
hit_pts = 200
'''

GOOD_TEMPLATE = '''[Good]
nickname = {nickname}
msg_id_prefix = {msg_id_prefix}
equipment = {nickname}
category = commodity
price = {price}
combinable = true
good_sell_price = {good_sell_price}
bad_buy_price = {bad_buy_price}
bad_sell_price = {bad_sell_price}
good_buy_price = {good_buy_price}
shop_archetype = Equipment\\models\\commodities\\nn_icons\\cwire_refinedmats_2.3db
item_icon = Equipment\\models\\commodities\\nn_icons\\{icon}.3db
jump_dist = 4
'''


class Commodity:
    ALIAS = None
    RU_NAME = None
    RU_INFO = ''
    NICKNAME = None
    POD = None
    ICON = None

    IS_DEFAULT = False
    IS_BASIC = False
    IS_ROID = False
    IS_ALLOY = False
    IS_PRODUCT = False
    IS_LUXURY = False
    IS_CONTRABAND = False

    DEFAULT_PRICE = 100
    PRICE_BEST_RATE = 0.25
    PRICE_CHEAP_RATE = 0.5
    PRICE_NORMAL_RATE = 0.75
    PRICE_BAD_RATE = 1

    PRICE_STEP = 20

    UNITS_PER_CONTAINER = 30
    DECAY_PER_SECOND = 0

    BASE_COMMODITY = True

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def __init__(self, ids):
        self.ids = ids

        self.ids_name = ids.new_name(self.get_ru_name())
        self.ids_info = ids.new_info(
            InfocardBuilder.build_equip_infocard(
                self.get_ru_name(),
                self.get_ru_info()
            )
        )

        self.good_price_multiplier = 5
        self.bad_price_multiplier = 2

    def get_nickname(self):
        return self.NICKNAME

    def set_good_price_multiplier(self, multiplier):
        self.good_price_multiplier = multiplier

    def set_bad_price_multiplier(self, multiplier):
        self.bad_price_multiplier = multiplier

    def get_good_price_multiplier(self):
        return self.good_price_multiplier

    def get_bad_price_multiplier(self):
        return self.bad_price_multiplier

    def get_ru_name(self):
        return self.RU_NAME

    def get_ru_info(self):
        return [self.RU_INFO]

    def get_default_price(self):
        return self.DEFAULT_PRICE

    def get_best_price(self):
        return self.get_default_price() * self.PRICE_BEST_RATE

    def get_cheap_price(self):
        return self.get_default_price() * self.PRICE_CHEAP_RATE

    def get_normal_price(self):
        return self.get_default_price() * self.PRICE_NORMAL_RATE

    def get_bad_price(self):
        return self.get_default_price() * self.PRICE_BAD_RATE

    def get_price_step(self, depth):
        # TODO: increase by depth
        return self.PRICE_STEP

    def get_consume_price(self, produce_price, depth):
        price = produce_price
        for i in range(1, depth+1):
            price += self.get_price_step(i)

        return price

    def get_ids_name(self):
        return self.ids_name.id

    def get_ids_info(self):
        return self.ids_info.id

    def get_pod(self):
        return self.POD

    def get_units_per_container(self):
        return self.UNITS_PER_CONTAINER

    def get_decay_per_second(self):
        return self.DECAY_PER_SECOND

    def get_equip(self):
        return EQUIP_TEMPLATE.format(
            nickname=self.get_nickname(),
            ids_name=self.get_ids_name(),
            ids_info=self.get_ids_info(),
            pod=self.get_pod(),
            units_per_container=self.get_units_per_container(),
            decay_per_second=self.get_decay_per_second(),
        )

    def get_msg_id_prefix(self):
        return f'msg_id_{self.get_nickname()}'

    def get_good_sell_price(self):
        return self.get_good_price_multiplier()

    def get_bad_buy_price(self):
        return self.get_good_price_multiplier()

    def get_bad_sell_price(self):
        return self.get_bad_price_multiplier()

    def get_good_buy_price(self):
        return self.get_bad_price_multiplier()

    def get_good(self):
        return GOOD_TEMPLATE.format(
            nickname=self.get_nickname(),
            msg_id_prefix=self.get_msg_id_prefix(),
            price=self.get_default_price(),
            good_sell_price=self.get_good_sell_price(),
            bad_buy_price=self.get_bad_buy_price(),
            bad_sell_price=self.get_bad_sell_price(),
            good_buy_price=self.get_good_buy_price(),
            icon=self.ICON,
        )


class BasicCommodity:
    DEFAULT_PRICE = 20
    PRICE_STEP = 5
    IS_BASIC = True


class DefaultCommodity:
    DEFAULT_PRICE = 40
    PRICE_STEP = 10
    IS_DEFAULT = True


class Roid:
    DEFAULT_PRICE = 80
    PRICE_STEP = 15
    IS_ROID = True


class Alloy:
    DEFAULT_PRICE = 150
    PRICE_STEP = 25
    IS_ALLOY = True


class Product:
    DEFAULT_PRICE = 250
    PRICE_STEP = 50
    IS_PRODUCT = True


class Luxury:
    DEFAULT_PRICE = 400
    PRICE_STEP = 100
    IS_LUXURY = True


class Contraband:
    DEFAULT_PRICE = 300
    PRICE_STEP = 40
    IS_CONTRABAND = True


class TerraformMinerals(Product, Commodity):
    ALIAS = TERRAFORM_MINERALS
    RU_NAME = 'Минеральные удобрения'
    NICKNAME = 'comm_terraform_minerals'
    POD = POD_FOODS
    ICON = ICON_FERTILIZER
    RU_INFO = ru_info.TERRAFORM_MINERALS


class TerraformGases(Product, Commodity):
    ALIAS = TERRAFORM_GASES
    RU_NAME = 'Терраформирующие газы'
    NICKNAME = 'comm_terraform_gases'
    POD = POD_FOODS
    ICON = ICON_CHEMICAL
    BASE_COMMODITY = False
    RU_INFO = ru_info.TERRAFORM_GASES


class LaserBeamParts(Product, Commodity):
    ALIAS = LASER_BEAM_PARS
    RU_NAME = 'Компоненты излучателя'
    NICKNAME = 'comm_laserbeam_components'
    POD = POD_MACHINES
    ICON = ICON_MACHINES
    BASE_COMMODITY = False
    RU_INFO = ru_info.LASERBEAM_COMPONENTS


class BasicWater(BasicCommodity, Commodity):
    ALIAS = BASIC_WATER
    RU_NAME = 'Вода'
    NICKNAME = 'comm_basic_water'
    POD = POD_RAWMATS
    ICON = ICON_WATERROID
    RU_INFO = ru_info.WATER


class BasicOxygen(BasicCommodity, Commodity):
    ALIAS = BASIC_OXYGEN
    RU_NAME = 'Кислород'
    NICKNAME = 'comm_basic_oxygen'
    POD = POD_HIGHTECH
    ICON = ICON_CHEMICAL
    RU_INFO = ru_info.OXYGEN


class BasicFood(BasicCommodity, Commodity):
    ALIAS = BASIC_FOOD
    RU_NAME = 'Синтетическая пища'
    NICKNAME = 'comm_basic_food'
    POD = POD_FOODS
    ICON = ICON_FOOD
    RU_INFO = ru_info.SYNTS_FOOD


class BasicConsumer(BasicCommodity, Commodity):
    ALIAS = BASIC_CONSUMER
    RU_NAME = 'Ширпотреб'
    NICKNAME = 'comm_basic_consumer'
    POD = POD_CONSUMER
    ICON = ICON_CONSUMER
    RU_INFO = ru_info.CONSUMER_GOODS


class BasicMeds(BasicCommodity, Commodity):
    ALIAS = BASIC_MEDS
    RU_NAME = 'Медпрепараты'
    NICKNAME = 'comm_basic_meds'
    POD = POD_MEDICAL
    ICON = ICON_DRUGS
    RU_INFO = ru_info.MEDS


class BasicWeapons(BasicCommodity, Commodity):
    ALIAS = BASIC_WEAPONS
    RU_NAME = 'Стрелковое оружие'
    NICKNAME = 'comm_basic_weapons'
    POD = POD_MUNITIONS
    ICON = ICON_LIGHTARMS
    RU_INFO = ru_info.LIGHT_ARMS


class BasicToxic(BasicCommodity, Commodity):
    ALIAS = BASIC_TOXIC
    RU_NAME = 'Токсичные отходы'
    NICKNAME = 'comm_basic_toxic'
    POD = POD_CONTRABAND
    ICON = ICON_TOXIC
    RU_INFO = ru_info.TOXIC


class Metal(DefaultCommodity, Commodity):
    ALIAS = METAL
    RU_NAME = 'Металлолом'
    NICKNAME = 'comm_scrap_metal'
    POD = POD_REFINEDMATS
    ICON = ICON_REFINEDMATS


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
    RU_INFO = ru_info.POWER_SOLAR


class AlloyBasic(DefaultCommodity, Commodity):
    ALIAS = ALLOY_BASIC
    RU_NAME = 'Простой сплав'
    NICKNAME = 'comm_alloy_basic'
    POD = POD_INDUSTRIAL
    ICON = ICON_METAL
    RU_INFO = ru_info.ALLOY_BASIC


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
    RU_INFO = ru_info.GAS_FUEL


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
    RU_INFO = ru_info.DIAMONDS


class LuxuryDiamonds(Luxury, Commodity):
    ALIAS = LUXURY_DIAMONDS
    RU_NAME = 'Алмазные украшения'
    NICKNAME = 'comm_luxury_diamonds'
    POD = POD_CONSUMER
    ICON = ICON_DIAMONDS
    RU_INFO = ru_info.DIAMONDS


class Niobium(Roid, Commodity):
    ALIAS = NIOBIUM
    RU_NAME = 'Ниобий'
    NICKNAME = 'comm_roid_niobium'
    POD = POD_RAWMATS
    ICON = ICON_ROID
    RU_INFO = ru_info.NIOBIUM


class ProdMachines(Product, Commodity):
    ALIAS = PROD_MACHINES
    RU_NAME = 'Промышленные станки'
    NICKNAME = 'comm_prod_machines'
    POD = POD_MACHINES
    ICON = ICON_INDUSTRIAL
    RU_INFO = ru_info.PROD_MACHINES


class StationPanels(Product, Commodity):
    ALIAS = STATION_PANELS
    RU_NAME = 'Панели обшивки станций'
    NICKNAME = 'comm_station_panels'
    POD = POD_REFINEDMATS
    ICON = ICON_HULLPANELS
    RU_INFO = ru_info.STATION_PANELS


class AlloyHeavy(Alloy, Commodity):
    ALIAS = ALLOY_HEAVY
    RU_NAME = 'Суперсплав'
    NICKNAME = 'comm_alloy_heavy'
    POD = POD_INDUSTRIAL
    ICON = ICON_METAL
    RU_INFO = ru_info.ALLOY_HEAVY


class RoidMinerParts(Product, Commodity):
    ALIAS = ROID_MINER_PARTS
    RU_NAME = 'Детали рудокопа'
    NICKNAME = 'comm_roidminer_parts'
    POD = POD_MACHINES
    ICON = ICON_INDUSTRIAL
    RU_INFO = ru_info.ROID_MINER_PARTS


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
    RU_INFO = ru_info.WATER_EXTRA


class Berilium(Roid, Commodity):
    ALIAS = BERILIUM
    RU_NAME = 'Берилий'
    NICKNAME = 'comm_roid_berilium'
    POD = POD_RAWMATS
    ICON = ICON_ROID
    RU_INFO = ru_info.BERILIUM


class Nicollum(Roid, Commodity):
    ALIAS = NICOLLUM
    RU_NAME = 'Никель'
    NICKNAME = 'comm_roid_nicollum'
    POD = POD_RAWMATS
    ICON = ICON_ROID
    RU_INFO = ru_info.NICOLLUM


class LuxuryGoods(Luxury, Commodity):
    ALIAS = LUXURY_GOODS
    RU_NAME = 'Роскошные товары'
    NICKNAME = 'comm_luxury_consumer'
    POD = POD_CONSUMER
    ICON = ICON_CONSUMER
    RU_INFO = ru_info.LUXURY_GOODS


class TLRParts(Product, Commodity):
    ALIAS = TLR_PARTS
    RU_NAME = 'Детали торгового пути'
    NICKNAME = 'comm_tlr_parts'
    POD = POD_REFINEDMATS
    ICON = ICON_TLRPARTS
    RU_INFO = ru_info.TLR_PARTS


class EngineParts(Product, Commodity):
    ALIAS = ENGINE_PARTS
    RU_NAME = 'Детали двигателей'
    NICKNAME = 'comm_engine_components'
    POD = POD_TRANSPARTS
    ICON = ICON_ENGINECOMP
    RU_INFO = ru_info.ENGINE_COMPONENTS


class JumpGateParts(Product, Commodity):
    ALIAS = JUMPGATE_PARTS
    RU_NAME = 'Детали гиперворот'
    NICKNAME = 'comm_jumpgate_parts'
    POD = POD_REFINEDMATS
    ICON = ICON_TLRPARTS
    RU_INFO = ru_info.JG_COMPONENTS


class AlloyTemperature(Alloy, Commodity):
    ALIAS = ALLOY_TEMPERATURE
    RU_NAME = 'Высокотемпературный сплав'
    NICKNAME = 'comm_alloy_temperature'
    POD = POD_INDUSTRIAL
    ICON = ICON_METAL
    RU_INFO = ru_info.ALLOY_TEMPERATURE


class MiningEquipment(Product, Commodity):
    ALIAS = MINING_EQUIPMENT
    RU_NAME = 'Горное оборудование'
    NICKNAME = 'comm_mining_equip'
    POD = POD_MACHINES
    ICON = ICON_INDUSTRIAL
    RU_INFO = ru_info.MINING_EQUIP


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
    RU_INFO = ru_info.URANIUM


class Plumbum(Roid, Commodity):
    ALIAS = PLUMBUM
    RU_NAME = 'Свинец'
    NICKNAME = 'comm_roid_plumbum'
    POD = POD_RAWMATS
    ICON = ICON_ROID
    RU_INFO = ru_info.PLUMBUM


class Reactors(Product, Commodity):
    ALIAS = REACTORS
    RU_NAME = 'Компоненты реактора'
    NICKNAME = 'comm_reactors'
    POD = POD_HIGHTECH
    ICON = ICON_BATTERY
    RU_INFO = ru_info.REACTORS


class MOXFuel(Product, Commodity):
    ALIAS = MOX_FUEL
    RU_NAME = 'Реактивное топливо'
    NICKNAME = 'comm_mox_fuel'
    POD = POD_HIGHTECH
    ICON = ICON_CHEMICAL
    RU_INFO = ru_info.MOX_FUEL


class Ammunition(Product, Commodity):
    ALIAS = AMMUNITION
    RU_NAME = 'Тяжелые снаряды'
    NICKNAME = 'comm_munitions'
    POD = POD_MUNITIONS
    ICON = ICON_MUNITIONS
    RU_INFO = ru_info.MUNITIONS


class LuxuryFood(Luxury, Commodity):
    ALIAS = LUXURY_FOOD
    RU_NAME = 'Роскошная пища'
    NICKNAME = 'comm_luxury_food'
    POD = POD_FOODS
    ICON = ICON_GREATFOOD
    RU_INFO = ru_info.LUXURY_FOOD


class AlloyRadiation(Commodity):
    ALIAS = ALLOY_RADIATION
    RU_NAME = 'Противорадиационный сплав'
    NICKNAME = 'comm_alloy_radiation'
    POD = POD_INDUSTRIAL
    ICON = ICON_METAL
    RU_INFO = ru_info.ALLOY_RADIATION


class GreenhouseParts(Product, Commodity):
    ALIAS = GREENHOUSE_PARTS
    RU_NAME = 'Оборудование оранжереи'
    NICKNAME = 'comm_greenhouse_parts'
    POD = POD_MACHINES
    ICON = ICON_REFINEDMATS
    RU_INFO = ru_info.GREENHOUSE_PARTS


class DefenceSystems(Product, Commodity):
    ALIAS = DEFENCE_SYSTEMS
    RU_NAME = 'Защитные системы'
    NICKNAME = 'comm_defence_systems'
    POD = POD_MUNITIONS
    ICON = ICON_MUNITIONS


class Gold(Roid, Commodity):
    ALIAS = GOLD
    RU_NAME = 'Золото'
    NICKNAME = 'comm_roid_gold'
    POD = POD_RAWMATS
    ICON = ICON_ROID
    RU_INFO = ru_info.GOLD


class Silver(Roid, Commodity):
    ALIAS = SILVER
    RU_NAME = 'Серебро'
    NICKNAME = 'comm_roid_silver'
    POD = POD_RAWMATS
    ICON = ICON_ROID
    RU_INFO = ru_info.SILVER


class Electronics(Product, Commodity):
    ALIAS = ELECTRONICS
    RU_NAME = 'Электроника'
    NICKNAME = 'comm_electronics'
    POD = POD_ELECTRONICS
    ICON = ICON_ELECTRONICS
    RU_INFO = ru_info.ELECTRONICS


class LuxuryGold(Luxury, Commodity):
    ALIAS = LUXURY_GOLD
    RU_NAME = 'Украшения'
    NICKNAME = 'comm_luxury_gold'
    POD = POD_CONSUMER
    ICON = ICON_METAL
    RU_INFO = ru_info.LUXURY_GOLD


class OpticalChips(Product, Commodity):
    ALIAS = OPTICAL_CHIPS
    RU_NAME = 'Оптические чипы'
    NICKNAME = 'comm_optical_chips'
    POD = POD_ELECTRONICS
    ICON = ICON_CHIP


class AlloyConductor(Alloy, Commodity):
    ALIAS = ALLOY_CONDUCTOR
    RU_NAME = 'Сверхпроводящий сплав'
    NICKNAME = 'comm_alloy_conductor'
    POD = POD_INDUSTRIAL
    ICON = ICON_METAL
    RU_INFO = ru_info.ALLOY_CONDUCTOR


class GasMinerParts(Product, Commodity):
    ALIAS = GAS_MINER_PARTS
    RU_NAME = 'Детали для газодобытчика'
    NICKNAME = 'comm_gasminer_parts'
    POD = POD_MACHINES
    ICON = ICON_INDUSTRIAL
    RU_INFO = ru_info.GASMINER_PARTS


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
