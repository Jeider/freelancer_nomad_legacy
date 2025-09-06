import random


class TradingTrain:
    FRONT_OFFSET = 133
    CARGO_PODS_COUNT = 8
    ARCHETYPE = 'tr_point_large_train'
    LOADOUT = 'tr_point_test_large_train'


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
    POINTS_COUNT = 2

    @classmethod
    def get_points(cls):
        return random.sample(cls.TRANSPORT_POINTS, k=cls.POINTS_COUNT)