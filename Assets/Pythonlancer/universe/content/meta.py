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
CONSUME_MIN = 0

RESELL = -1000
RESELL_MIN = -400


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


class HaveSmelter(StaticObjective):
    pass


class AlloyProducerJob(StaticObjective):

    def get_actions(self):
        return [
            CommConsume(METAL),
            CommConsume(NIOBIUM),
            CommConsume(BERILIUM),
            CommConsume(PLUMBUM),
            CommConsume(GOLD),

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
            CommConsume(METAL),

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
            CommConsume(ELECTRONICS),
            CommConsume(RESEARCH_EQUIP),
            CommConsume(OPTICAL_CHIPS),
        ]


class LookupResellObjective(BaseObjective):
    PRICE_MULTIPLIER = 1
    SEARCH_PRODUCE_DEPTH = 1


class LargeTradingBaseObjective(LookupResellObjective):
    pass


class SmallTradingBaseObjective(LookupResellObjective):
    pass


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
            CommResell(METAL),
            CommResell(ALLOY_BASIC),
        ]


class BaseProps:
    POPULATION = POP_MEDIUM_BASE

    ROOT_ACTIONS = []
    DEFAULT_OBJECTIVES = []
    DEFENCE_EFFECT = 0
    # DEFENCE_HIGH
    # DEFENCE_MEDIUM: +light arms cost, +repair cost
    # DEFENCE_SMALL: ++light arms cost, ++repair cost

    def __init__(self, objectives=None, raw_actions=None):
        self.objectives = (objectives if objectives else []) + self.DEFAULT_OBJECTIVES
        self.raw_actions = (raw_actions if raw_actions else []) + self.ROOT_ACTIONS

    def get_objectives(self):
        return self.objectives


class GenericLockedBase(BaseProps):
    POPULATION = POP_XSMALL_BASE


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


class MiningPlanet(BaseProps):
    POPULATION = POP_SMALL_BASE
    ROOT_ACTIONS = [
        CommConsume(BASIC_WATER),
        CommConsume(BASIC_OXYGEN),
        CommConsume(BASIC_CONSUMER),
        CommConsume(BASIC_MEDS),
        CommConsume(METAL),
        CommConsume(ALLOY_BASIC),
        CommConsume(POWER_SOLAR),
        CommConsume(STATION_PANELS),

        CommConsume(TERRAFORM_GASES),
    ]


class ResortPlanet(BaseProps):
    POPULATION = POP_SMALL_BASE
    ROOT_ACTIONS = [
        CommProduce(BASIC_WATER, PRODUCE_BEST),
        CommProduce(BASIC_OXYGEN, PRODUCE_BEST),
        CommResell(BASIC_CONSUMER),
        CommProduce(BASIC_MEDS, PRODUCE_NORMAL),
        CommConsume(METAL),
        CommConsume(ALLOY_BASIC),
        CommConsume(POWER_SOLAR),
        CommResell(POWER_SOLAR_EMPTY),

        CommProduce(WATER_EXTRA, PRODUCE_BEST),
    ]


class WaterPlanet(BaseProps):
    POPULATION = POP_SMALL_BASE
    ROOT_ACTIONS = [
        CommResell(BASIC_WATER),
        CommResell(BASIC_OXYGEN),
        CommConsume(BASIC_CONSUMER),
        CommConsume(BASIC_MEDS),
        CommConsume(METAL),
        CommConsume(ALLOY_BASIC),
        CommConsume(POWER_SOLAR),
        CommResell(POWER_SOLAR_EMPTY),

        CommConsume(TERRAFORM_GASES),
        CommProduce(WATER_EXTRA, PRODUCE_BEST),
    ]


class SpaceStation(BaseProps):
    ROOT_ACTIONS = [
        CommConsume(BASIC_WATER),
        CommConsume(BASIC_OXYGEN),
        CommConsume(BASIC_CONSUMER),
        CommConsume(BASIC_MEDS),
        CommConsume(METAL),
        CommConsume(ALLOY_BASIC),
        CommConsume(GAS_FUEL),
        CommConsume(STATION_PANELS),
    ]


class Megabase(SpaceStation):
    POPULATION = POP_MEGABASE


class MediumStation(SpaceStation):
    POPULATION = POP_MEDIUM_BASE


class TradingBase(MediumStation):
    POPULATION = POP_MEDIUM_BASE


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


class PirateStation(BaseProps):
    POPULATION = POP_SMALL_BASE
    DEFENCE_EFFECT = DEFENCE_PIRATES


class PirateAsteroid(BaseProps):
    POPULATION = POP_SMALL_BASE
    DEFENCE_EFFECT = DEFENCE_PIRATES
    DEFAULT_OBJECTIVES = [
        SupportAsteroidBase(),
    ]


class PirateGasMiner(BaseProps):
    POPULATION = POP_SMALL_BASE
    DEFENCE_EFFECT = DEFENCE_PIRATES
    DEFAULT_OBJECTIVES = [
        CollectGas(),
    ]


class JunkerBase(BaseProps):
    POPULATION = POP_SMALL_BASE
    DEFENCE_EFFECT = DEFENCE_PIRATES
    DEFAULT_OBJECTIVES = [
        JunkerJob(),
    ]
