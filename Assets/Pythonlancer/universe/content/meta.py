from world.names import *

POP_XLARGE_PLANET = 10
POP_LARGE_PLANET = 9
POP_MINING_PLANET = 8
POP_ULTRA_MEGABASE = 7
POP_MEGABASE = 6
POP_LARGE_BASE = 5
POP_MEDIUM_BASE = 4
POP_SMALL_BASE = 3
POP_XSMALL_BASE = 2
POP_BATTLESHIP_CREW = 1

DEFENCE_OUTPOST = 100
DEFENCE_BATTLESHIP = 200
DEFENCE_LARGE_PLANET = 500
DEFENCE_MEGABASE = 50
DEFENCE_PRISON = 200
DEFENCE_PIRATES = -100

PRODUCE = 250
PRODUCE_BAD = PRODUCE  # 250
PRODUCE_NORMAL = PRODUCE * 2  # 500
PRODUCE_CHEAP = PRODUCE * 3  # 750
PRODUCE_BEST = PRODUCE * 4  # 1000
PRODUCE_MIN = 50

CONSUME = -50
RESELL = -1000

CONSUMES_PER_PRODUCE = {
    LUXURY_DIAMONDS: [DIAMONDS, PROD_MACHINES],
    PROD_MACHINES: [DIAMONDS],
    STATION_PANELS: [ALLOY_HEAVY],
    ROID_MINER_PARTS: [ALLOY_HEAVY, PROD_MACHINES],
    SMELTER_PARTS: [ALLOY_HEAVY, ALLOY_TEMPERATURE, PROD_MACHINES],

    LUXURY_GOODS: [POLYMERS],
    TLR_PARTS: [ALLOY_TEMPERATURE, PROD_MACHINES],
    ENGINE_PARTS: [ALLOY_TEMPERATURE, ALLOY_RADIATION, PROD_MACHINES],
    JUMPGATE_PARTS: [ALLOY_TEMPERATURE, PROD_MACHINES],
    MINING_EQUIPMENT: [ALLOY_HEAVY, PROD_MACHINES],

    REACTORS: [ALLOY_RADIATION, PROD_MACHINES],
    AMMUNITION: [ALLOY_TEMPERATURE, ALLOY_RADIATION, PROD_MACHINES],
    LUXURY_FOOD: [TERRAFORM_MINERALS],
    GREENHOUSE_PARTS: [POLYMERS, TERRAFORM_MINERALS],
    DEFENCE_SYSTEMS: [ELECTRONICS, OPTICAL_CHIPS, POLYMERS],

    ELECTRONICS: [GOLD, SILVER, ALLOY_CONDUCTOR, PROD_MACHINES, POLYMERS],
    LUXURY_GOLD: [GOLD, SILVER],
    OPTICAL_CHIPS: [PROD_MACHINES, ALLOY_CONDUCTOR],
    GAS_MINER_PARTS: [ALLOY_HEAVY, PROD_MACHINES],
    SOLAR_PLANT_PARTS: [ALLOY_CONDUCTOR, PROD_MACHINES],
    RESEARCH_EQUIP: [OPTICAL_CHIPS, ELECTRONICS, PROD_MACHINES],
}


class CommAction:

    def __init__(self, comm_name, value):
        self.comm_name = comm_name
        self.value = value

    def get_comm_name(self):
        return self.comm_name

    def get_comm_change(self):
        return self.value


class CommProduce(CommAction):
    def __init__(self, comm_name, value):
        if value < 0:
            raise Exception('produce should be positive')
        super().__init__(comm_name, value)


class CommConsume(CommAction):
    def __init__(self, comm_name):
        super().__init__(comm_name, CONSUME)


class CommResell(CommAction):
    def __init__(self, comm_name):
        super().__init__(comm_name, RESELL)


class BaseObjective:

    def get_actions(self):
        return []


class SingleObjective(BaseObjective):
    def __init__(self, comm_name):
        self.comm_name = comm_name

    def get_actions(self):
        return []


class ProduceBad(SingleObjective):

    def get_actions(self):
        return [CommProduce(self.comm_name, PRODUCE_BAD)]


class ProduceNormal(SingleObjective):

    def get_actions(self):
        return [CommProduce(self.comm_name, PRODUCE_NORMAL)]


class ProduceCheap(SingleObjective):

    def get_actions(self):
        return [CommProduce(self.comm_name, PRODUCE_CHEAP)]


class ProduceBest(SingleObjective):

    def get_actions(self):
        return [CommProduce(self.comm_name, PRODUCE_BEST)]


class Consume(SingleObjective):

    def get_actions(self):
        return [CommProduce(self.comm_name, CONSUME)]


class Resell(SingleObjective):

    def get_actions(self):
        return [CommProduce(self.comm_name, RESELL)]


class StaticObjective(BaseObjective):
    pass


class SupportRoidMiners(StaticObjective):

    def get_actions(self):
        return [
            CommConsume(ROID_MINER_PARTS),
        ]


class SupportSolarPlants(StaticObjective):

    def get_actions(self):
        return [
            CommConsume(POWER_SOLAR_EMPTY),
            CommConsume(STATION_PANELS),
        ]


class SupportBattleships(StaticObjective):

    def get_actions(self):
        return [
            CommConsume(REACTORS),
            CommConsume(SHIP_HULL_PANELS),
            CommConsume(ENGINE_PARTS),
        ]


class SupportShips(StaticObjective):
    def get_actions(self):
        return [
            CommConsume(SHIP_HULL_PANELS),
            CommConsume(ENGINE_PARTS),
        ]


class SupportTradelanes(StaticObjective):
    def get_actions(self):
        return [
            CommConsume(TLR_PARTS),
        ]


class SupportJumpgates(StaticObjective):
    def get_actions(self):
        return [
            CommConsume(JUMPGATE_PARTS),
        ]


class HaveGreenhouse(StaticObjective):
    def get_actions(self):
        return [
            CommConsume(GREENHOUSE_PARTS),
            CommProduce(BASIC_OXYGEN, PRODUCE_NORMAL),
        ]


class HaveSolarPanels(StaticObjective):
    def get_actions(self):
        return [
            CommConsume(SOLAR_PLANT_PARTS),
            CommConsume(POWER_SOLAR_EMPTY),
            CommProduce(POWER_SOLAR, PRODUCE_NORMAL),
        ]


class HaveReactor(StaticObjective):
    def get_actions(self):
        return [
            CommConsume(MOX_FUEL),
            CommConsume(REACTORS),

            CommProduce(BASIC_TOXIC, PRODUCE_BAD),
        ]


class AlloyProducerJob(StaticObjective):

    def get_actions(self):
        return [
            # CommConsume(METAL),
            CommConsume(NIOBIUM),
            CommConsume(URANIUM),
            CommConsume(BERILIUM),
            CommConsume(PLUMBUM),
            CommConsume(GOLD),
            CommConsume(SMELTER_PARTS),

            CommProduce(SHIP_HULL_PANELS, PRODUCE_CHEAP),
            CommProduce(POWER_SOLAR_EMPTY, PRODUCE_CHEAP),
            CommProduce(GAS_BALLOONS, PRODUCE_CHEAP),

            CommProduce(SOLAR_PLANT_PARTS, PRODUCE_BAD),
            CommProduce(BASIC_TOXIC, PRODUCE_BEST),

            CommProduce(ALLOY_BASIC, PRODUCE_BAD),
            CommProduce(ALLOY_HEAVY, PRODUCE_BAD),
            CommProduce(ALLOY_TEMPERATURE, PRODUCE_BAD),
            CommProduce(ALLOY_RADIATION, PRODUCE_BAD),
            CommProduce(ALLOY_CONDUCTOR, PRODUCE_BAD),
        ]


class JunkerJob(StaticObjective):

    def get_actions(self):
        return [
            # CommConsume(METAL),

            CommProduce(SHIP_HULL_PANELS, PRODUCE_BAD),
            CommProduce(ALLOY_BASIC, PRODUCE_BAD),
        ]


class CollectGas(StaticObjective):
    def get_actions(self):
        return [
            CommConsume(GAS_MINER_PARTS),
            CommConsume(GAS_BALLOONS),

            CommProduce(GAS_FUEL, PRODUCE_CHEAP),
        ]


class ConsumeHeavyMunitions(StaticObjective):
    def get_actions(self):
        return [
            CommConsume(AMMUNITION),
        ]


class GenerateSolarPower(StaticObjective):
    def get_actions(self):
        return [
            CommProduce(POWER_SOLAR, PRODUCE),
        ]


class ConsumeLuxury(StaticObjective):
    def get_actions(self):
        return [
            CommConsume(WATER_EXTRA),
            CommConsume(LUXURY_GOODS),
            CommConsume(LUXURY_GOLD),
            CommConsume(LUXURY_DIAMONDS),
            CommConsume(LUXURY_FOOD),
        ]


class DefendPrison(StaticObjective):
    def get_actions(self):
        return [
            CommConsume(DEFENCE_SYSTEMS),
        ]


class MakeResearch(StaticObjective):
    def get_actions(self):
        return [
            CommConsume(ELECTRONICS),
            CommConsume(RESEARCH_EQUIP),
            CommConsume(OPTICAL_CHIPS),
        ]


class SupportAsteroidBase(StaticObjective):
    def get_actions(self):
        return [
            CommConsume(MINING_EQUIPMENT),
        ]


class SelectedResellObjective(BaseObjective):
    PRICE_MULTIPLIER = 1
    GOODS_LIST = []


class FreeportObjective(SelectedResellObjective):
    def get_actions(self):
        return [
            CommResell(BASIC_WATER),
            CommResell(BASIC_OXYGEN),
            CommResell(BASIC_CONSUMER),
            CommResell(BASIC_MEDS),
            # CommResell(METAL),
            CommResell(ALLOY_BASIC),
        ]


class BaseProps:
    POPULATION = POP_MEDIUM_BASE

    ROOT_ACTIONS = []
    DEFAULT_OBJECTIVES = []
    DEFENCE_EFFECT = 0
    RESELL_GOODS_DEPTH_RANGE = 0
    RESELL_PRODUCTS_ONLY = False
    # DEFENCE_HIGH
    # DEFENCE_MEDIUM: +light arms cost, +repair cost
    # DEFENCE_SMALL: ++light arms cost, ++repair cost

    def __init__(self, objectives=None, raw_actions=None):
        self.objectives = (objectives if objectives else []) + self.DEFAULT_OBJECTIVES
        self.raw_actions = (raw_actions if raw_actions else []) + self.ROOT_ACTIONS

    def get_objectives(self):
        return self.objectives

    def get_raw_actions(self):
        return self.raw_actions


class GenericLockedBase(BaseProps):
    POPULATION = POP_XSMALL_BASE
    HAVE_STORE = False


class LockedBattleship(GenericLockedBase):
    pass


class LockedRoidMiner(GenericLockedBase):
    pass


class LockedAsteroid(GenericLockedBase):
    pass


class LockedSmelter(GenericLockedBase):
    pass


class LockedSolarPlant(GenericLockedBase):
    pass


class LockedHackableOutpost(GenericLockedBase):
    pass


class LargePlanet(BaseProps):
    DEFENCE_EFFECT = DEFENCE_LARGE_PLANET
    ROOT_ACTIONS = [
        CommProduce(BASIC_WATER, PRODUCE_CHEAP),
        CommProduce(BASIC_OXYGEN, PRODUCE_CHEAP),
        CommProduce(BASIC_CONSUMER, PRODUCE_NORMAL),
        CommProduce(BASIC_MEDS, PRODUCE_NORMAL),
    ]
    DEFAULT_OBJECTIVES = [
        ConsumeLuxury(),
    ]


class ManhattanSuperPlanet(LargePlanet):
    RESELL_GOODS_DEPTH_RANGE = 8
    RESELL_PRODUCTS_ONLY = True


class MiningPlanet(BaseProps):
    POPULATION = POP_SMALL_BASE
    ROOT_ACTIONS = [
        CommConsume(BASIC_WATER),
        CommConsume(BASIC_OXYGEN),
        CommConsume(BASIC_CONSUMER),
        CommConsume(BASIC_MEDS),
        # CommConsume(METAL),
        CommConsume(ALLOY_BASIC),
        CommConsume(POWER_SOLAR),
        CommConsume(STATION_PANELS),

        # CommConsume(TERRAFORM_GASES),
    ]


class ResortPlanet(BaseProps):
    POPULATION = POP_SMALL_BASE
    ROOT_ACTIONS = [
        CommProduce(BASIC_WATER, PRODUCE_BEST),
        CommProduce(BASIC_OXYGEN, PRODUCE_BEST),
        CommResell(BASIC_CONSUMER),
        CommProduce(BASIC_MEDS, PRODUCE_NORMAL),
        # CommConsume(METAL),
        CommConsume(ALLOY_BASIC),
        CommConsume(POWER_SOLAR),
        CommResell(POWER_SOLAR_EMPTY),

        CommProduce(WATER_EXTRA, PRODUCE_BEST),
    ]


class WaterPlanet(BaseProps):
    POPULATION = POP_SMALL_BASE
    ROOT_ACTIONS = [
        CommProduce(BASIC_WATER, PRODUCE_BEST),
        CommProduce(BASIC_OXYGEN, PRODUCE_BEST),
        CommConsume(BASIC_CONSUMER),
        CommConsume(BASIC_MEDS),
        # CommConsume(METAL),
        CommConsume(ALLOY_BASIC),
        CommConsume(POWER_SOLAR),
        CommResell(POWER_SOLAR_EMPTY),
    ]


class SpaceStation(BaseProps):
    ROOT_ACTIONS = [
        CommConsume(BASIC_WATER),
        CommConsume(BASIC_OXYGEN),
        CommConsume(BASIC_CONSUMER),
        CommConsume(BASIC_MEDS),
        # CommConsume(METAL),
        CommConsume(ALLOY_BASIC),
        CommConsume(GAS_FUEL),
        CommConsume(STATION_PANELS),
    ]


class TradelaneSupportStation(SpaceStation):
    DEFAULT_OBJECTIVES = [
        SupportTradelanes(),
    ]


class GasMiningStation(SpaceStation):
    DEFAULT_OBJECTIVES = [
        CollectGas(),
    ]


class RoidMiningStation(SpaceStation):
    DEFAULT_OBJECTIVES = [
        SupportRoidMiners(),
    ]


class Megabase(SpaceStation):
    POPULATION = POP_MEGABASE


class MegaTradingbase(Megabase):
    RESELL_GOODS_DEPTH_RANGE = 10


class MediumStation(SpaceStation):
    POPULATION = POP_MEDIUM_BASE


class LargeTradingBase(MediumStation):
    POPULATION = POP_MEDIUM_BASE
    RESELL_GOODS_DEPTH_RANGE = 8


class TradingBase(MediumStation):
    POPULATION = POP_MEDIUM_BASE
    RESELL_GOODS_DEPTH_RANGE = 6


class Shipyard(SpaceStation):
    POPULATION = POP_SMALL_BASE
    DEFAULT_OBJECTIVES = [
        SupportShips(),
    ]


class Refinery(SpaceStation):
    POPULATION = POP_SMALL_BASE
    DEFAULT_OBJECTIVES = [
        AlloyProducerJob(),
    ]


class Freeport(SpaceStation):
    POPULATION = POP_SMALL_BASE
    # RESELL_GOODS_DEPTH_RANGE = 3


class Outpost(SpaceStation):
    POPULATION = POP_SMALL_BASE
    DEFENCE_EFFECT = DEFENCE_OUTPOST


class Research(SpaceStation):
    POPULATION = POP_SMALL_BASE
    DEFAULT_OBJECTIVES = [
        MakeResearch(),
    ]


class Prison(SpaceStation):
    POPULATION = POP_SMALL_BASE
    DEFENCE_EFFECT = DEFENCE_PRISON
    DEFAULT_OBJECTIVES = [
        DefendPrison(),
    ]


class Battleship(SpaceStation):
    POPULATION = POP_BATTLESHIP_CREW
    DEFENCE_EFFECT = DEFENCE_BATTLESHIP
    DEFAULT_OBJECTIVES = [
        HaveReactor(),
        ConsumeHeavyMunitions(),
    ]


class LuxuryLiner(SpaceStation):
    POPULATION = POP_BATTLESHIP_CREW
    DEFAULT_OBJECTIVES = [
        HaveReactor(),
    ]


class PirateStation(SpaceStation):
    POPULATION = POP_SMALL_BASE
    DEFENCE_EFFECT = DEFENCE_PIRATES


class PirateAsteroid(PirateStation):
    POPULATION = POP_SMALL_BASE
    DEFENCE_EFFECT = DEFENCE_PIRATES
    DEFAULT_OBJECTIVES = [
        SupportAsteroidBase(),
    ]


class PirateGasMiner(PirateStation):
    POPULATION = POP_SMALL_BASE
    DEFENCE_EFFECT = DEFENCE_PIRATES
    DEFAULT_OBJECTIVES = [
        CollectGas(),
    ]


class JunkerBase(PirateStation):
    POPULATION = POP_SMALL_BASE
    DEFENCE_EFFECT = DEFENCE_PIRATES
    DEFAULT_OBJECTIVES = [
        JunkerJob(),
    ]
