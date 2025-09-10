import random
from story.math import relocate_point

from text.dividers import DIVIDER

ORIENT_HEXAGON = [0, 60, 120, 180, 240, 320]


class TradingTrain:
    FRONT_OFFSET = 133
    CARGO_PODS_COUNT = 8
    ARCHETYPE = 'tr_point_large_train'
    LOADOUT = 'tr_point_test_large_train'
    HP_CARGO = 'HpCargo'


class TradingTrainCargo(TradingTrain):
    FRONT_OFFSET = 10
    CARGO_PODS_COUNT = 8
    ARCHETYPE = 'tr_point_train_cargo'
    LOADOUT = 'tr_point_test_train_cargo'
    HP_CARGO = 'HpCargoA'


class TradingTrainCargoEmpty(TradingTrainCargo):
    FRONT_OFFSET = 10
    CARGO_PODS_COUNT = 0
    ARCHETYPE = 'tr_point_train_cargo'
    LOADOUT = ''


class TradingLargeTransport(TradingTrain):
    FRONT_OFFSET = 100
    CARGO_PODS_COUNT = 4
    ARCHETYPE = 'tr_point_large_transport'
    LOADOUT = 'tr_point_test_large_transport'


class TradingSmallTransport(TradingTrain):
    FRONT_OFFSET = 65
    CARGO_PODS_COUNT = 2
    ARCHETYPE = 'tr_point_small_transport'
    LOADOUT = 'tr_point_test_small_transport'


class TradingFixture:
    ARCHETYPE = 'docking_fixture_traders'
    TRANSPORT_POINTS = [
        -132, -45, 45, 132
    ]
    POINTS_COUNT = 3

    @classmethod
    def get_points(cls):
        return random.sample(cls.TRANSPORT_POINTS, k=cls.POINTS_COUNT)


class WeaponPlatform:
    ARCHETYPE = 'rmbase_smuggler'
    LOADOUT = 'rmbase_smuggler'


class StorageSmuggler:
    ARCHETYPE = 'rmbase_smuggler'
    LOADOUT = 'rmbase_smuggler'


class StorageTrader:
    ARCHETYPE = 'rmbase_trader'
    LOADOUT = 'rmbase_trader'


class StorageFactory:
    ARCHETYPE = 'rmbase_newgasminer'
    LOADOUT = 'rmbase_newgasminer_prod'


class StorageGasminer:
    ARCHETYPE = 'rmbase_newgasminer'
    LOADOUT = 'rmbase_newgasminer'


class OutpostPanel:
    ARCHETYPE = 'rmbase_panels'
    LOADOUT = 'rmbase_panels'


class OutpostDoors:
    ARCHETYPE = 'rmbase_doors'
    LOADOUT = 'rmbase_doors'


class OutpostShipyard:
    ARCHETYPE = 'rmbase_shipyard'
    LOADOUT = 'rmbase_shipyard'
