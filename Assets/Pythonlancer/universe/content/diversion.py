import random
from story.math import relocate_point

from text.dividers import DIVIDER, SINGLE_DIVIDER

from text.strings import MultiString as MS

ORIENT_HEXAGON = [0, 60, 120, 180, 240, 320]


class TradingTrain:
    FRONT_OFFSET = 133
    CARGO_COUNT = 50
    CARGO_PODS_COUNT = 8
    ARCHETYPE = 'tr_point_large_train'
    LOADOUT = 'tr_point_test_large_train'
    HP_CARGO = 'HpCargo'
    EMPTY = False
    RU_NAME_START = 'Поезд для'
    EN_NAME_START = 'Train for'

    @classmethod
    def get_loadout_name(cls, commodity):
        return f'lod_{cls.ARCHETYPE}_cargo_{commodity.get_nickname()}'

    @classmethod
    def get_ids_name(cls, space_misc_ids, commodity):
        return space_misc_ids.new_name(
            MS(
                f'{cls.RU_NAME_START} {commodity.get_ru_name_rel2()}',
                f'{cls.EN_NAME_START} {commodity.get_en_name_rel2()}'
            )
        )

    @classmethod
    def get_loadout_content(cls, commodity):
        items = [
            '[Loadout]',
            f'nickname = {cls.get_loadout_name(commodity)}'
        ]
        for i in range(1, cls.CARGO_PODS_COUNT+1):
            items.append(
                f'equip = cargopod_{commodity.get_pod()}, {cls.HP_CARGO}{i:02d}'
            )
            items.append(
                f'cargo = {commodity.get_nickname()}, {cls.CARGO_COUNT}, {cls.HP_CARGO}{i:02d}'
            )
        return SINGLE_DIVIDER.join(items)


class TradingTrainCargo(TradingTrain):
    FRONT_OFFSET = 10
    CARGO_PODS_COUNT = 8
    ARCHETYPE = 'tr_point_train_cargo'
    LOADOUT = 'tr_point_test_train_cargo'
    HP_CARGO = 'HpCargoA'


class TradingTrainCargoEmpty(TradingTrainCargo):
    FRONT_OFFSET = 10
    CARGO_PODS_COUNT = 0
    ARCHETYPE = 'tr_point_train_cargo_empty'
    LOADOUT = ''
    EMPTY = True


class TradingLargeTransport(TradingTrain):
    FRONT_OFFSET = 100
    CARGO_PODS_COUNT = 4
    ARCHETYPE = 'tr_point_large_transport'
    LOADOUT = 'tr_point_test_large_transport'
    RU_NAME_START = 'Транспорт для'
    EN_NAME_START = 'Transport for'


class TradingSmallTransport(TradingTrain):
    FRONT_OFFSET = 65
    CARGO_PODS_COUNT = 2
    ARCHETYPE = 'tr_point_small_transport'
    LOADOUT = 'tr_point_test_small_transport'
    RU_NAME_START = 'Транспорт для'
    EN_NAME_START = 'Transport for'


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

