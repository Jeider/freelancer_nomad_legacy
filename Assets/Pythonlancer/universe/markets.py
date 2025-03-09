from managers.weapon import GunQuery
from world import gun

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
        return self.MARKET_DEFAULT_LEVEL

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

    def get_market_item_params(self):
        return {
            'item_nickname': self.get_package_nickname(),
            'level': self.get_market_level(),
        }

    def get_marketdata(self):
        return self.MARKET_ITEM_TEMPLATE.format(**self.get_market_item_params())


class MarketBase:
    MARKET_TEMPLATE = '''[BaseGood]
base = {base_nickname}
{items}'''

    def __init__(self, core, base_nickname):
        self.core = core
        self.base_nickname = base_nickname

    def get_base_nickname(self):
        return self.base_nickname

    def get_items(self):
        raise NotImplementedError

    def get_items_marketdata(self):
        return SINGLE_DIVIDER.join([item.get_marketdata() for item in self.get_items()])

    def get_market_content(self):
        return self.MARKET_TEMPLATE.format(
            base_nickname=self.get_base_nickname(),
            items=self.get_items_marketdata(),
        )


class EquipMarket(MarketBase):
    GUNS = []

    def get_items(self):
        items = []
        for gun_query in self.GUNS:
            items.extend(
                self.core.weapon.get_guns_by_query(gun_query)
            )
        return items


class BizEquip(EquipDealer):
    GUNS = [
        GunQuery(gun.RheinlandLightgun, eq_classes=[1, 2, 3, 4]),
    ]


class CommodityDealer(MarketBase):
    pass


class ShipDealer(MarketBase):
    pass
