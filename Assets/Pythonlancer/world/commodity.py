from world.names import *
from text import info_commodity as ru_info
from text.infocards import InfocardBuilder
from text.strings import MultiString as MS


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
    RU_NAME_REL1 = None
    RU_NAME_REL2 = None
    RU_NAME_REL3 = None
    RU_INFO = MS('', '')
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

    PRICE_VARIANCE_PERCENT = 2

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

        self.ids_name = ids.new_name(self.get_ru_name_clean())
        self.ids_info = ids.new_info(
            MS(
                InfocardBuilder.build_equip_infocard(
                    self.get_ru_name_clean().get_ru(),
                    self.get_en_info()
                ),
                InfocardBuilder.build_equip_infocard(
                    self.get_ru_name_clean().get_en(),
                    self.get_en_info()
                )
            )
        )

        self.good_price_multiplier = 5
        self.bad_price_multiplier = 2

    def get_market_level(self):
        return self.MARKET_DEFAULT_LEVEL

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

    def get_ru_name_clean(self):
        return MS(
            self.RU_NAME.get_ru().replace('+', ''),
            self.RU_NAME.get_en()
        )

    def get_ru_name_std(self):
        return self.RU_NAME.lower()

    def get_ru_name_rel1(self):
        return self.RU_NAME_REL1.lower() if self.RU_NAME_REL1 else self.RU_NAME.get_ru().lower()

    def get_ru_name_rel2(self):
        return self.RU_NAME_REL2.lower()

    def get_ru_name_rel3(self):
        return self.RU_NAME_REL3.lower()

    def get_en_name_rel1(self):
        return self.RU_NAME.get_en().lower()

    def get_en_name_rel2(self):
        return self.RU_NAME.get_en().lower()

    def get_en_name_rel3(self):
        return self.RU_NAME.get_en().lower()

    def get_name_rel1(self):
        return MS(self.get_ru_name_rel1(), self.get_en_name_rel1())

    def get_ru_info(self):
        return [self.RU_INFO.get_ru()]

    def get_en_info(self):
        return [self.RU_INFO.get_en()]

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
        return f'gcs_gen_commodity_{self.get_nickname()}'

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
    PRICE_VARIANCE_PERCENT = 25


class DefaultCommodity:
    DEFAULT_PRICE = 40
    PRICE_STEP = 10
    IS_DEFAULT = True
    PRICE_VARIANCE_PERCENT = 10


class Roid:
    DEFAULT_PRICE = 80
    PRICE_STEP = 15
    IS_ROID = True
    PRICE_VARIANCE_PERCENT = 8


class Alloy:
    DEFAULT_PRICE = 150
    PRICE_STEP = 25
    IS_ALLOY = True
    PRICE_VARIANCE_PERCENT = 7


class Product:
    DEFAULT_PRICE = 250
    PRICE_STEP = 50
    IS_PRODUCT = True
    PRICE_VARIANCE_PERCENT = 5


class Luxury:
    DEFAULT_PRICE = 400
    PRICE_STEP = 100
    IS_LUXURY = True
    PRICE_VARIANCE_PERCENT = 3


class Contraband:
    DEFAULT_PRICE = 300
    PRICE_STEP = 40
    IS_CONTRABAND = True
    PRICE_VARIANCE_PERCENT = 15


class TerraformMinerals(Product, Commodity):
    ALIAS = TERRAFORM_MINERALS
    RU_NAME = MS('Минер+альные удобр+ения', 'Fertilisers')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'минеральных удобрений'
    RU_NAME_REL3 = 'минеральных удобрениях'
    NICKNAME = 'comm_terraform_minerals'
    POD = POD_FOODS
    ICON = ICON_FERTILIZER
    RU_INFO = ru_info.TERRAFORM_MINERALS


class TerraformGases(Product, Commodity):
    ALIAS = TERRAFORM_GASES
    RU_NAME = MS('Терраформ+ирующие г+азы', 'Terraforming gases')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'терраформирующих газов'
    RU_NAME_REL3 = 'терраформирующих газах'
    NICKNAME = 'comm_terraform_gases'
    POD = POD_FOODS
    ICON = ICON_CHEMICAL
    BASE_COMMODITY = False
    RU_INFO = ru_info.TERRAFORM_GASES


class LaserBeamParts(Product, Commodity):
    ALIAS = LASER_BEAM_PARS
    RU_NAME = MS('Компон+енты излуч+ателя', 'Laser beam parts')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'компонентов излучателя'
    RU_NAME_REL3 = 'компонентах излучателя'
    NICKNAME = 'comm_laserbeam_components'
    POD = POD_MACHINES
    ICON = ICON_MACHINES
    BASE_COMMODITY = False
    RU_INFO = ru_info.LASERBEAM_COMPONENTS


class BasicWater(BasicCommodity, Commodity):
    ALIAS = BASIC_WATER
    RU_NAME = MS('Вода', 'Water')
    RU_NAME_REL1 = 'В+оду'
    RU_NAME_REL2 = 'воды'
    RU_NAME_REL3 = 'воде'
    NICKNAME = 'comm_basic_water'
    POD = POD_RAWMATS
    ICON = ICON_WATERROID
    RU_INFO = ru_info.WATER


class BasicOxygen(BasicCommodity, Commodity):
    ALIAS = BASIC_OXYGEN
    RU_NAME = MS('Кислор+од', 'Oxygen')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'кислорода'
    RU_NAME_REL3 = 'кислороде'
    NICKNAME = 'comm_basic_oxygen'
    POD = POD_HIGHTECH
    ICON = ICON_CHEMICAL
    RU_INFO = ru_info.OXYGEN


class BasicFood(BasicCommodity, Commodity):
    ALIAS = BASIC_FOOD
    RU_NAME = MS('Синтетическая пища', 'Synthetic food')
    RU_NAME_REL1 = 'Синтет+ическую пищу'
    RU_NAME_REL2 = 'синтетической пищи'
    RU_NAME_REL3 = 'синтетической пище'
    NICKNAME = 'comm_basic_food'
    POD = POD_FOODS
    ICON = ICON_FOOD
    RU_INFO = ru_info.SYNTS_FOOD


class BasicConsumer(BasicCommodity, Commodity):
    ALIAS = BASIC_CONSUMER
    RU_NAME = MS('Ширпотр+еб', 'Consumer goods')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'ширпотреба'
    RU_NAME_REL3 = 'ширпотребе'
    NICKNAME = 'comm_basic_consumer'
    POD = POD_CONSUMER
    ICON = ICON_CONSUMER
    RU_INFO = ru_info.CONSUMER_GOODS


class BasicMeds(BasicCommodity, Commodity):
    ALIAS = BASIC_MEDS
    RU_NAME = MS('Медпрепар+аты', 'Medicines')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'медпрепаратов'
    RU_NAME_REL3 = 'медпрепаратах'
    NICKNAME = 'comm_basic_meds'
    POD = POD_MEDICAL
    ICON = ICON_DRUGS
    RU_INFO = ru_info.MEDS


class BasicWeapons(BasicCommodity, Commodity):
    ALIAS = BASIC_WEAPONS
    RU_NAME = MS('Стрелк+овое оружие', 'Light arms')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'стрелкового оружия'
    RU_NAME_REL3 = 'стрелковом оружии'
    NICKNAME = 'comm_basic_weapons'
    POD = POD_MUNITIONS
    ICON = ICON_LIGHTARMS
    RU_INFO = ru_info.LIGHT_ARMS


class BasicToxic(BasicCommodity, Commodity):
    ALIAS = BASIC_TOXIC
    RU_NAME = MS('Токс+ичные отх+оды', 'Toxic waste')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'токсичных отходов'
    RU_NAME_REL3 = 'токсичных отходах'
    NICKNAME = 'comm_basic_toxic'
    POD = POD_CONTRABAND
    ICON = ICON_TOXIC
    RU_INFO = ru_info.TOXIC


class Metal(DefaultCommodity, Commodity):
    ALIAS = METAL
    RU_NAME = MS('Металлол+ом', 'Scrap metal')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'металлолома'
    RU_NAME_REL3 = 'металлоломе'
    NICKNAME = 'comm_scrap_metal'
    POD = POD_REFINEDMATS
    ICON = ICON_REFINEDMATS


class PowerSolarEmpty(DefaultCommodity, Commodity):
    ALIAS = POWER_SOLAR_EMPTY
    RU_NAME = MS('Разр+яженные генер+аторы', 'Empty power cells')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'разряженных генераторов'
    RU_NAME_REL3 = 'разряженных генераторах'
    NICKNAME = 'comm_power_solar_empty'
    POD = POD_HIGHTECH
    ICON = ICON_BATTERY


class PowerSolar(DefaultCommodity, Commodity):
    ALIAS = POWER_SOLAR
    RU_NAME = MS('Зар+яженные генер+аторы', 'Charged power cells')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'заряженных генераторов'
    RU_NAME_REL3 = 'заряженных генераторах'
    NICKNAME = 'comm_power_solar'
    POD = POD_HIGHTECH
    ICON = ICON_BATTERY
    RU_INFO = ru_info.POWER_SOLAR


class AlloyBasic(DefaultCommodity, Commodity):
    ALIAS = ALLOY_BASIC
    RU_NAME = MS('Прост+ой сплав', 'Basic alloy')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'простого сплава'
    RU_NAME_REL3 = 'простом сплаве'
    NICKNAME = 'comm_alloy_basic'
    POD = POD_INDUSTRIAL
    ICON = ICON_METAL
    RU_INFO = ru_info.ALLOY_BASIC


class GasBalloons(DefaultCommodity, Commodity):
    ALIAS = GAS_BALLOONS
    RU_NAME = MS('Сж+иженный газ', 'Liquified gas')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'газовых баллонов'
    RU_NAME_REL3 = 'газовых баллонах'
    NICKNAME = 'comm_gas_balloons'
    POD = POD_TRANSPARTS
    ICON = ICON_HFUEL


class GasFuel(DefaultCommodity, Commodity):
    ALIAS = GAS_FUEL
    RU_NAME = MS('Г+азовое топливо', 'Gas fuel')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'газового топлива'
    RU_NAME_REL3 = 'газовом топливе'
    NICKNAME = 'comm_gas_fuel'
    POD = POD_TRANSPARTS
    ICON = ICON_HFUEL
    RU_INFO = ru_info.GAS_FUEL


class ShipHullPanels(Product, Commodity):
    ALIAS = SHIP_HULL_PANELS
    RU_NAME = MS('Пан+ели обш+ивки корабл+я', 'Ship hull panels')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'панелей обшивки корабля'
    RU_NAME_REL3 = 'панелях обшивки корабля'
    NICKNAME = 'comm_shiphull_panels'
    POD = POD_REFINEDMATS
    ICON = ICON_HULLPANELS


class Diamonds(Roid, Commodity):
    ALIAS = DIAMONDS
    RU_NAME = MS('Алм+азы', 'Diamonds')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'алмазов'
    RU_NAME_REL3 = 'алмазах'
    NICKNAME = 'comm_roid_diamonds'
    POD = POD_RAWMATS
    ICON = ICON_DIAMONDS
    RU_INFO = ru_info.DIAMONDS


class LuxuryDiamonds(Luxury, Commodity):
    ALIAS = LUXURY_DIAMONDS
    RU_NAME = MS('Алм+азные украш+ения', 'Luxury diamonds')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'алмазных украшений'
    RU_NAME_REL3 = 'алмазных украшениях'
    NICKNAME = 'comm_luxury_diamonds'
    POD = POD_CONSUMER
    ICON = ICON_DIAMONDS
    RU_INFO = ru_info.DIAMONDS


class Niobium(Roid, Commodity):
    ALIAS = NIOBIUM
    RU_NAME = MS('Ни+обий', 'Niobium')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'ниобия'
    RU_NAME_REL3 = 'ниобии'
    NICKNAME = 'comm_roid_niobium'
    POD = POD_RAWMATS
    ICON = ICON_ROID
    RU_INFO = ru_info.NIOBIUM


class ProdMachines(Product, Commodity):
    ALIAS = PROD_MACHINES
    RU_NAME = MS('Пром+ышленные станк+и', 'Production machines')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'промышленных станков'
    RU_NAME_REL3 = 'промышленных станках'
    NICKNAME = 'comm_prod_machines'
    POD = POD_MACHINES
    ICON = ICON_INDUSTRIAL
    RU_INFO = ru_info.PROD_MACHINES


class StationPanels(Product, Commodity):
    ALIAS = STATION_PANELS
    RU_NAME = MS('Пан+ели обш+ивки ст+анций', "Station hull panels")
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'панелей обшивки станций'
    RU_NAME_REL3 = 'панелях обшивки станций'
    NICKNAME = 'comm_station_panels'
    POD = POD_REFINEDMATS
    ICON = ICON_HULLPANELS
    RU_INFO = ru_info.STATION_PANELS


class AlloyHeavy(Alloy, Commodity):
    ALIAS = ALLOY_HEAVY
    RU_NAME = MS('Суперспл+ав', 'Heavy alloy')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'суперсплава'
    RU_NAME_REL3 = 'суперсплаве'
    NICKNAME = 'comm_alloy_heavy'
    POD = POD_INDUSTRIAL
    ICON = ICON_METAL
    RU_INFO = ru_info.ALLOY_HEAVY


class RoidMinerParts(Product, Commodity):
    ALIAS = ROID_MINER_PARTS
    RU_NAME = MS('Дет+али рудок+опа', 'Roid miner parts')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'деталей рудокопа'
    RU_NAME_REL3 = 'деталях рудокопа'
    NICKNAME = 'comm_roidminer_parts'
    POD = POD_MACHINES
    ICON = ICON_INDUSTRIAL
    RU_INFO = ru_info.ROID_MINER_PARTS


class SmelterParts(Product, Commodity):
    ALIAS = SMELTER_PARTS
    RU_NAME = MS('Дет+али плав+ильной устан+овки', "Smelter parts")
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'деталей плавильной установки'
    RU_NAME_REL3 = 'деталях плавильной установки'
    NICKNAME = 'comm_smelter_parts'
    POD = POD_MACHINES
    ICON = ICON_INDUSTRIAL


class WaterExtra(Luxury, Commodity):
    ALIAS = WATER_EXTRA
    RU_NAME = MS('Минер+альная вода', 'Luxury mineral water')
    RU_NAME_REL1 = 'Минер+альную воду'
    RU_NAME_REL2 = 'минеральной воды'
    RU_NAME_REL3 = 'минеральной воде'
    NICKNAME = 'comm_water_extra'
    POD = POD_RAWMATS
    ICON = ICON_WATERROID
    RU_INFO = ru_info.WATER_EXTRA


class Berilium(Roid, Commodity):
    ALIAS = BERILIUM
    RU_NAME = MS('Бер+илий', 'Berilium')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'берилия'
    RU_NAME_REL3 = 'берилии'
    NICKNAME = 'comm_roid_berilium'
    POD = POD_RAWMATS
    ICON = ICON_ROID
    RU_INFO = ru_info.BERILIUM


class Nicollum(Roid, Commodity):
    ALIAS = NICOLLUM
    RU_NAME = MS('Н+икель', 'Nicollum')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'никеля'
    RU_NAME_REL3 = 'никеле'
    NICKNAME = 'comm_roid_nicollum'
    POD = POD_RAWMATS
    ICON = ICON_ROID
    RU_INFO = ru_info.NICOLLUM


class LuxuryGoods(Luxury, Commodity):
    ALIAS = LUXURY_GOODS
    RU_NAME = MS('Роск+ошные товары', 'Luxury goods')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'роскошных товаров'
    RU_NAME_REL3 = 'роскошных товарах'
    NICKNAME = 'comm_luxury_consumer'
    POD = POD_CONSUMER
    ICON = ICON_CONSUMER
    RU_INFO = ru_info.LUXURY_GOODS


class TLRParts(Product, Commodity):
    ALIAS = TLR_PARTS
    RU_NAME = MS('Дет+али торг+овых пут+ей', 'Trade lane parts')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'деталей торговых путей'
    RU_NAME_REL3 = 'деталях торговых путей'
    NICKNAME = 'comm_tlr_parts'
    POD = POD_REFINEDMATS
    ICON = ICON_TLRPARTS
    RU_INFO = ru_info.TLR_PARTS


class EngineParts(Product, Commodity):
    ALIAS = ENGINE_PARTS
    RU_NAME = MS('Компон+енты дв+игателей', 'Engine parts')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'компонентов двигателей'
    RU_NAME_REL3 = 'компонентах двигателей'
    NICKNAME = 'comm_engine_components'
    POD = POD_TRANSPARTS
    ICON = ICON_ENGINECOMP
    RU_INFO = ru_info.ENGINE_COMPONENTS


class JumpGateParts(Product, Commodity):
    ALIAS = JUMPGATE_PARTS
    RU_NAME = MS('Дет+али гипервр+ат', 'Jumpgate parts')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'деталей гиперврат'
    RU_NAME_REL3 = 'деталях гиперврат'
    NICKNAME = 'comm_jumpgate_parts'
    POD = POD_REFINEDMATS
    ICON = ICON_TLRPARTS
    RU_INFO = ru_info.JG_COMPONENTS


class AlloyTemperature(Alloy, Commodity):
    ALIAS = ALLOY_TEMPERATURE
    RU_NAME = MS('Высокотемперат+урный сплав', 'High-temperature alloy')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'высокотемпературного сплава'
    RU_NAME_REL3 = 'высокотемпературном сплаве'
    NICKNAME = 'comm_alloy_temperature'
    POD = POD_INDUSTRIAL
    ICON = ICON_METAL
    RU_INFO = ru_info.ALLOY_TEMPERATURE


class MiningEquipment(Product, Commodity):
    ALIAS = MINING_EQUIPMENT
    RU_NAME = MS('Г+орное обор+удование', 'Mining equipment')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'горного оборудования'
    RU_NAME_REL3 = 'горном оборудовании'
    NICKNAME = 'comm_mining_equip'
    POD = POD_MACHINES
    ICON = ICON_INDUSTRIAL
    RU_INFO = ru_info.MINING_EQUIP


class Polymers(Product, Commodity):
    ALIAS = POLYMERS
    RU_NAME = MS('Полим+еры', 'Polymers')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'полимеров'
    RU_NAME_REL3 = 'полимерах'
    NICKNAME = 'comm_polymers'
    POD = POD_HIGHTECH
    ICON = ICON_CHEMICAL


class Uranium(Roid, Commodity):
    ALIAS = URANIUM
    RU_NAME = MS('Уран', "Uranium")
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'урана'
    RU_NAME_REL3 = 'уране'
    NICKNAME = 'comm_roid_uranium'
    POD = POD_RAWMATS
    ICON = ICON_ROID
    RU_INFO = ru_info.URANIUM


class Plumbum(Roid, Commodity):
    ALIAS = PLUMBUM
    RU_NAME = MS('Свин+ец', 'Plumbum')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'свинца'
    RU_NAME_REL3 = 'свинце'
    NICKNAME = 'comm_roid_plumbum'
    POD = POD_RAWMATS
    ICON = ICON_ROID
    RU_INFO = ru_info.PLUMBUM


class Reactors(Product, Commodity):
    ALIAS = REACTORS
    RU_NAME = MS('Компон+енты ре+актора', "Reactor components")
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'компонентов реактора'
    RU_NAME_REL3 = 'компонентах реактора'
    NICKNAME = 'comm_reactors'
    POD = POD_HIGHTECH
    ICON = ICON_BATTERY
    RU_INFO = ru_info.REACTORS


class MOXFuel(Product, Commodity):
    ALIAS = MOX_FUEL
    RU_NAME = MS('Реакт+ивное топливо', 'MOX Fuel')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'реактивного топлива'
    RU_NAME_REL3 = 'реактивном топливе'
    NICKNAME = 'comm_mox_fuel'
    POD = POD_HIGHTECH
    ICON = ICON_CHEMICAL
    RU_INFO = ru_info.MOX_FUEL


class Ammunition(Product, Commodity):
    ALIAS = AMMUNITION
    RU_NAME = MS('Тяжелые снаряды', 'Heavy munitions')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'тяжелых снарядов'
    RU_NAME_REL3 = 'тяжелых снарядах'
    NICKNAME = 'comm_munitions'
    POD = POD_MUNITIONS
    ICON = ICON_MUNITIONS
    RU_INFO = ru_info.MUNITIONS


class LuxuryFood(Luxury, Commodity):
    ALIAS = LUXURY_FOOD
    RU_NAME = MS('Роск+ошная пища', 'Luxury food')
    RU_NAME_REL1 = 'роск+ошную пищу'
    RU_NAME_REL2 = 'роскошной пищи'
    RU_NAME_REL3 = 'роскошной пище'
    NICKNAME = 'comm_luxury_food'
    POD = POD_FOODS
    ICON = ICON_GREATFOOD
    RU_INFO = ru_info.LUXURY_FOOD


class AlloyRadiation(Commodity):
    ALIAS = ALLOY_RADIATION
    RU_NAME = MS('Противорадиаци+онный сплав', 'Anti-radiation alloy')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'противорадиационного сплава'
    RU_NAME_REL3 = 'противорадиационном сплаве'
    NICKNAME = 'comm_alloy_radiation'
    POD = POD_INDUSTRIAL
    ICON = ICON_METAL
    RU_INFO = ru_info.ALLOY_RADIATION


class GreenhouseParts(Product, Commodity):
    ALIAS = GREENHOUSE_PARTS
    RU_NAME = MS('Обор+удование оранжер+еи', "Greenhouse parts")
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'оборудования оранжереи'
    RU_NAME_REL3 = 'оборудовании оранжереи'
    NICKNAME = 'comm_greenhouse_parts'
    POD = POD_MACHINES
    ICON = ICON_REFINEDMATS
    RU_INFO = ru_info.GREENHOUSE_PARTS


class DefenceSystems(Product, Commodity):
    ALIAS = DEFENCE_SYSTEMS
    RU_NAME = MS('Защ+итные сист+емы', "Defence systems")
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'защитных систем'
    RU_NAME_REL3 = 'защитных системах'
    NICKNAME = 'comm_defence_systems'
    POD = POD_MUNITIONS
    ICON = ICON_MUNITIONS


class Gold(Roid, Commodity):
    ALIAS = GOLD
    RU_NAME = MS('З+олото', "Gold")
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'золота'
    RU_NAME_REL3 = 'золоте'
    NICKNAME = 'comm_roid_gold'
    POD = POD_RAWMATS
    ICON = ICON_ROID
    RU_INFO = ru_info.GOLD


class Silver(Roid, Commodity):
    ALIAS = SILVER
    RU_NAME = MS('Серебр+о', 'Silver')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'серебра'
    RU_NAME_REL3 = 'серебре'
    NICKNAME = 'comm_roid_silver'
    POD = POD_RAWMATS
    ICON = ICON_ROID
    RU_INFO = ru_info.SILVER


class Electronics(Product, Commodity):
    ALIAS = ELECTRONICS
    RU_NAME = MS('Электр+оника', 'Electronics')
    RU_NAME_REL1 = 'Электронику'
    RU_NAME_REL2 = 'электроники'
    RU_NAME_REL3 = 'электронике'
    NICKNAME = 'comm_electronics'
    POD = POD_ELECTRONICS
    ICON = ICON_ELECTRONICS
    RU_INFO = ru_info.ELECTRONICS


class LuxuryGold(Luxury, Commodity):
    ALIAS = LUXURY_GOLD
    RU_NAME = MS('Украш+ения', 'Luxury gold')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'украшений'
    RU_NAME_REL3 = 'украшенях'
    NICKNAME = 'comm_luxury_gold'
    POD = POD_CONSUMER
    ICON = ICON_METAL
    RU_INFO = ru_info.LUXURY_GOLD


class OpticalChips(Product, Commodity):
    ALIAS = OPTICAL_CHIPS
    RU_NAME = MS('Опт+ические чипы', 'Optical chips')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'оптических чипов'
    RU_NAME_REL3 = 'оптических чипах'
    NICKNAME = 'comm_optical_chips'
    POD = POD_ELECTRONICS
    ICON = ICON_CHIP


class AlloyConductor(Alloy, Commodity):
    ALIAS = ALLOY_CONDUCTOR
    RU_NAME = MS('Сверхпровод+ящий сплав', 'Conductor alloy')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'сверхпроводящего сплава'
    RU_NAME_REL3 = 'сверхпроводящем сплаве'
    NICKNAME = 'comm_alloy_conductor'
    POD = POD_INDUSTRIAL
    ICON = ICON_METAL
    RU_INFO = ru_info.ALLOY_CONDUCTOR


class GasMinerParts(Product, Commodity):
    ALIAS = GAS_MINER_PARTS
    RU_NAME = MS('Детали для газодоб+ытчика', "Gas Miner Parts")
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'деталей для газодобытчика'
    RU_NAME_REL3 = 'деталях для газодобытчика'
    NICKNAME = 'comm_gasminer_parts'
    POD = POD_MACHINES
    ICON = ICON_INDUSTRIAL
    RU_INFO = ru_info.GASMINER_PARTS


class SolarPlantParts(Product, Commodity):
    ALIAS = SOLAR_PLANT_PARTS
    RU_NAME = MS('Компоненты солн. генер+атора', 'Solar Plant components')
    RU_NAME_REL1 = 'Компоненты солнечного генер+атора'
    RU_NAME_REL2 = 'компонентов солнечного генератора'
    RU_NAME_REL3 = 'компонентах солнечного генератора'
    NICKNAME = 'comm_solarplant_parts'
    POD = POD_MACHINES
    ICON = ICON_INDUSTRIAL


class ResearchEquip(Product, Commodity):
    ALIAS = RESEARCH_EQUIP
    RU_NAME = MS('Т+очное оборудование', 'Research equipment')
    # RU_NAME_REL1 = RU_NAME
    RU_NAME_REL2 = 'точного оборудования'
    RU_NAME_REL3 = 'точном оборудовании'
    NICKNAME = 'comm_research_equip'
    POD = POD_HIGHTECH
    ICON = ICON_INDUSTRIAL
