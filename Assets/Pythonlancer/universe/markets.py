import copy

from managers.tools import query as Q
from world.names import *

from text.dividers import SINGLE_DIVIDER


class MarketItem(object):
    def get_nickname(self):
        raise NotImplementedError

    def get_marketdata(self):
        raise NotImplementedError


class MarketEquip(MarketItem):
    MARKET_ITEM_TEMPLATE = 'MarketGood = {item_nickname}, {level}, {reputation}, {stock}, {price_mult}'

    MARKET_STOCK_AVAILABLE = '50, 50, 0'
    MARKET_STOCK_UNAVAILABLE = '0, 0, 1'

    MARKET_DEFAULT_REPUTATION = -1
    MARKET_DEFAULT_LEVEL = 0
    MARKET_DEFAULT_PRICE_MULTIPLIER = 1

    def get_market_level(self):
        raise Exception(f'{self} have no level definition')

    def get_market_reputation(self):
        return self.MARKET_DEFAULT_REPUTATION

    def get_market_stock(self):
        return self.MARKET_STOCK_AVAILABLE

    def get_market_price_multiplier(self):
        return self.MARKET_DEFAULT_PRICE_MULTIPLIER

    def get_market_item_params(self):
        return {
            'item_nickname': self.get_nickname(),
            'level': self.get_market_level(),
            'reputation': self.get_market_reputation(),
            'stock': self.get_market_stock(),
            'price_mult': self.get_market_price_multiplier(),
        }

    def get_marketdata(self):
        return self.MARKET_ITEM_TEMPLATE.format(**self.get_market_item_params())


class MarketShip(MarketItem):
    MARKET_ITEM_TEMPLATE = 'MarketGood = {item_nickname}, {level}, -1, 1, 1, 0, 1, 1'
    MARKET_DEFAULT_LEVEL = 0

    def get_market_level(self):
        return self.MARKET_DEFAULT_LEVEL

    def get_package_nickname(self):
        raise NotImplementedError

    def get_market_item_params(self):
        return {
            'item_nickname': self.get_package_nickname(),
            'level': self.get_market_level(),
        }

    def get_marketdata(self):
        return self.MARKET_ITEM_TEMPLATE.format(**self.get_market_item_params())


class MarketCommodity(MarketEquip):
    MARKET_STOCK_AVAILABLE = '150, 500, 0'

    def get_market_level(self):
        return self.MARKET_DEFAULT_LEVEL

    def in_stock(self):
        raise NotImplementedError

    def get_price_percent(self):
        raise NotImplementedError

    def get_market_stock(self):
        return (
            self.MARKET_STOCK_AVAILABLE
            if self.in_stock() else
            self.MARKET_STOCK_UNAVAILABLE
        )

    def get_market_price_multiplier(self):
        return self.get_price_percent()


class Market:
    MARKET_TEMPLATE = '''[BaseGood]
base = {base_nickname}
{items}'''

    def __init__(self, base_nickname, items):
        self.base_nickname = base_nickname
        self.items = items

    def get_base_nickname(self):
        return self.base_nickname

    def get_items(self):
        return self.items

    def append_items(self, items):
        self.items.extend(items)

    def get_items_marketdata(self):
        return SINGLE_DIVIDER.join([item.get_marketdata() for item in self.get_items()])

    def get_market_content(self):
        return self.MARKET_TEMPLATE.format(
            base_nickname=self.get_base_nickname(),
            items=self.get_items_marketdata(),
        )


class EquipSet:

    def __init__(self, *queries, weapon_faction=None):
        self.queries = queries
        self.weapon_faction = weapon_faction

    def get_equip_items(self, core, root_weapon_faction=None, root_misc_equip_type=None):
        items = []
        for init_query in self.queries:
            query = copy.copy(init_query)
            root_equip_type = root_misc_equip_type

            if query.__class__ == Q.Gun:
                items.extend(
                    core.weapons.get_guns_by_query(query)
                )

            elif query.__class__ == Q.GenericGun:
                used_weapon_faction = self.weapon_faction if self.weapon_faction else root_weapon_faction
                if not used_weapon_faction:
                    raise Exception('weapon faction is not defined for some EquipSet')

                items.extend(
                    core.weapons.get_generic_guns_by_query(used_weapon_faction, query)
                )

            elif query.__class__ == Q.Engine:
                if not query.eq_type:
                    query.eq_type = root_equip_type

                if not query.eq_type:
                    raise Exception('misc equip type is not defined for some Engine in EquipSet')

                items.extend(
                    core.misc_equip.get_engine_by_query(query)
                )

            elif query.__class__ == Q.Power:
                if not query.eq_type:
                    query.eq_type = root_equip_type

                if not query.eq_type:
                    raise Exception('misc equip type is not defined for some Power in EquipSet')

                items.extend(
                    core.misc_equip.get_power_by_query(query)
                )

            elif query.__class__ == Q.Shield:
                if not query.eq_type:
                    query.eq_type = root_equip_type

                if not query.eq_type:
                    raise Exception('misc equip type is not defined for some Shield in EquipSet')

                items.extend(
                    core.misc_equip.get_shield_by_query(query)
                )

            elif query.__class__ == Q.Thruster:
                if not query.eq_type:
                    query.eq_type = root_equip_type

                if not query.eq_type:
                    raise Exception('misc equip type is not defined for some Thruster in EquipSet')

                items.extend(
                    core.misc_equip.get_thruster_by_query(query)
                )

            else:
                raise Exception('Unknown query type')

        return items


class ShipSet:

    def __init__(self, *archetypes):
        self.archetypes = archetypes

    def get_ships(self, core):
        items = []
        for archetype in self.archetypes:
            items.append(
                core.shiparch.get_ship_by_archetype(archetype)
            )

        return items


BizSetDebug = EquipSet(
    Q.Gun('rh_lightgun', eq_classes=[1, 2, 3, 4]),
    Q.GenericGun(HUNTERGUN, eq_classes=[3, 5, 7, 9]),
    Q.Engine(CO_OUTCAST, eq_classes=[3, 5, 7, 9]),
    Q.Power(None, eq_classes=[5, 6, 7]),
    Q.Shield(KU_PIRATE, eq_classes=[2, 3]),
    Q.Thruster(RH_CIV, eq_classes=[1, 8]),
    weapon_faction=WEAPON_BR,
)

BattleshipSet = EquipSet(
    Q.GenericGun(LIGHTGUN, eq_classes=DEBUG_CLASSES),
    Q.Engine(None, eq_classes=DEBUG_CLASSES),
    Q.Power(None, eq_classes=DEBUG_CLASSES),
    Q.Shield(None, eq_classes=DEBUG_CLASSES),
    Q.Thruster(None, eq_classes=DEBUG_CLASSES),
)

PoliceOutpostSet = EquipSet(
    Q.GenericGun(LIGHTGUN, eq_classes=DEBUG_CLASSES),
    Q.Engine(None, eq_classes=DEBUG_CLASSES),
    Q.Power(None, eq_classes=DEBUG_CLASSES),
    Q.Shield(None, eq_classes=DEBUG_CLASSES),
    Q.Thruster(None, eq_classes=DEBUG_CLASSES),
)

PrisonSet = EquipSet(
    Q.GenericGun(LIGHTGUN, eq_classes=DEBUG_CLASSES),
    Q.Engine(None, eq_classes=DEBUG_CLASSES),
    Q.Power(None, eq_classes=DEBUG_CLASSES),
    Q.Shield(None, eq_classes=DEBUG_CLASSES),
    Q.Thruster(None, eq_classes=DEBUG_CLASSES),
)

ShipyardSet = EquipSet(
    Q.GenericGun(LIGHTGUN, eq_classes=DEBUG_CLASSES),
    Q.Engine(None, eq_classes=DEBUG_CLASSES),
    Q.Power(None, eq_classes=DEBUG_CLASSES),
    Q.Shield(None, eq_classes=DEBUG_CLASSES),
    Q.Thruster(None, eq_classes=DEBUG_CLASSES),
)

MainPlanetSet = EquipSet(
    Q.GenericGun(HUNTERGUN, eq_classes=DEBUG_CLASSES),
    Q.Engine(None, eq_classes=DEBUG_CLASSES),
    Q.Power(None, eq_classes=DEBUG_CLASSES),
    Q.Shield(None, eq_classes=DEBUG_CLASSES),
    Q.Thruster(None, eq_classes=DEBUG_CLASSES),
)

CivPlanetSet = EquipSet(
    Q.GenericGun(CIVGUN, eq_classes=DEBUG_CLASSES),
    Q.Engine(None, eq_classes=DEBUG_CLASSES),
    Q.Power(None, eq_classes=DEBUG_CLASSES),
    Q.Shield(None, eq_classes=DEBUG_CLASSES),
    Q.Thruster(None, eq_classes=DEBUG_CLASSES),
)

StationSet = EquipSet(
    Q.GenericGun(CIVGUN, eq_classes=DEBUG_CLASSES),
    Q.Engine(None, eq_classes=DEBUG_CLASSES),
    Q.Power(None, eq_classes=DEBUG_CLASSES),
    Q.Shield(None, eq_classes=DEBUG_CLASSES),
    Q.Thruster(None, eq_classes=DEBUG_CLASSES),
)

ResearchSet = EquipSet(
    Q.GenericGun(SHIELDGUN, eq_classes=DEBUG_CLASSES),
    Q.Engine(None, eq_classes=DEBUG_CLASSES),
    Q.Power(None, eq_classes=DEBUG_CLASSES),
    Q.Shield(None, eq_classes=DEBUG_CLASSES),
    Q.Thruster(None, eq_classes=DEBUG_CLASSES),
)

LargeStationSet = EquipSet(
    Q.GenericGun(LIGHTGUN, eq_classes=DEBUG_CLASSES),
    Q.GenericGun(SHIELDGUN, eq_classes=DEBUG_CLASSES_SHIELDGUN),
    Q.Engine(None, eq_classes=DEBUG_CLASSES),
    Q.Power(None, eq_classes=DEBUG_CLASSES),
    Q.Shield(None, eq_classes=DEBUG_CLASSES),
    Q.Thruster(None, eq_classes=DEBUG_CLASSES),
)

PirateSet = EquipSet(
    Q.GenericGun(PIRATEGUN, eq_classes=DEBUG_CLASSES),
    Q.Engine(None, eq_classes=DEBUG_CLASSES),
    Q.Power(None, eq_classes=DEBUG_CLASSES),
    Q.Shield(None, eq_classes=DEBUG_CLASSES),
    Q.Thruster(None, eq_classes=DEBUG_CLASSES),
)

OutcastSet = EquipSet(
    Q.Gun('bw_outcastgun', eq_classes=DEBUG_CLASSES),
    Q.Engine(None, eq_classes=DEBUG_CLASSES),
    Q.Power(None, eq_classes=DEBUG_CLASSES),
    Q.Shield(None, eq_classes=DEBUG_CLASSES),
    Q.Thruster(None, eq_classes=DEBUG_CLASSES),
)

CorsairSet = EquipSet(
    Q.Gun('bw_corsairgun', eq_classes=DEBUG_CLASSES),
    Q.Engine(None, eq_classes=DEBUG_CLASSES),
    Q.Power(None, eq_classes=DEBUG_CLASSES),
    Q.Shield(None, eq_classes=DEBUG_CLASSES),
    Q.Thruster(None, eq_classes=DEBUG_CLASSES),
)

OrderSet = EquipSet(
    Q.Gun('or_lightgun', eq_classes=DEBUG_CLASSES),
    Q.Gun('or_heavygun', eq_classes=DEBUG_CLASSES),
    Q.Engine(None, eq_classes=DEBUG_CLASSES),
    Q.Power(None, eq_classes=DEBUG_CLASSES),
    Q.Shield(None, eq_classes=DEBUG_CLASSES),
    Q.Thruster(None, eq_classes=DEBUG_CLASSES),
)
