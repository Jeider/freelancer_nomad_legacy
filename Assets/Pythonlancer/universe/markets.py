from text.dividers import SINGLE_DIVIDER

class NotEnoughLookupKwargsException(Exception):
    pass


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
    MARKET_DEFAULT_PRICE_MULTIPLER = 1

    def get_market_level(self):
        return self.MARKET_DEFAULT_LEVEL

    def get_market_reputation(self):
        return self.MARKET_DEFAULT_REPUTATION

    def get_market_stock(self):
        return self.MARKET_STOCK_AVAILABLE

    def get_market_price_multipler(self):
        return self.MARKET_DEFAULT_PRICE_MULTIPLER

    def get_market_item_params(self):
        return {
            'item_nickname': self.get_nickname(),
            'level': self.get_market_level(),
            'reputation': self.get_market_reputation(),
            'stock': self.get_market_stock(),
            'price_mult': self.get_market_price_multipler(),
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


class MarketBase(object):
    MARKET_KIND = None
    MARKET_TEMPLATE = '''[BaseGood]
base = {base_nickname}
{items}'''

    DEFAULT_ITEMS = []

    def __init__(self, base_nickname, items):
        self.base_nickname = base_nickname
        self.items = items

    def get_base_nickname(self):
        return self.base_nickname

    def get_items(self):
        return self.items

    def get_item_markets(self):
        items = [item.get_marketdata() for item in self.get_items()]
        items.extend(self.DEFAULT_ITEMS)
        return items

    def get_items_string(self):
        return SINGLE_DIVIDER.join(self.get_item_markets())

    def get_market_content(self):
        return self.MARKET_TEMPLATE.format(
            base_nickname=self.get_base_nickname(),
            items=self.get_items_string(),
        )


class LookupQuery:

    SHORCUTS = [
        'equipme
    ]
    def __init__(self, equip, **lookup_kwargs):
        self.equip = equip
        self.lookup_kwargs = lookup_kwargs


class EquipDealer(MarketBase):
    DEFAULT_ITEMS = [
        'MarketGood = ge_s_repair_01, 0, -1, 15, 15, 0, 1',
    ]
    GUNS = []
    THRUSTERS = []
    MISC_EQUIP = []


class BizEquip(EquipDealer):
    GUNS = [
        LookupQuery(gun.Rh),
    ]


class CommodityDealer(MarketBase):
    pass


class ShipDealer(MarketBase):
    pass
