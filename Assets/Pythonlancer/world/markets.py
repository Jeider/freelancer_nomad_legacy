class MarketEquip(object):
    MARKET_ITEM_TEMPLATE = 'MarketGood = {item_nickname}, {level}, {reputation}, {stock}, {price_mult}'

    MARKET_STOCK_AVAILABLE = '50, 50, 0'
    MARKET_STOCK_UNAVAILABLE = '0, 0, 1'

    MARKET_DEFAULT_REPUTATION = -1
    MARKET_DEFAULT_LEVEL = 0
    MARKET_DEFAULT_PRICE_MULTIPER = 1

    def get_market_level(self):
        return self.MARKET_DEFAULT_LEVEL

    def get_market_reputation(self):
        return self.MARKET_DEFAULT_REPUTATION

    def get_market_stock(self):
        return self.MARKET_STOCK_AVAILABLE

    def get_market_price_multipler(self):
        return self.MARKET_DEFAULT_PRICE_MULTIPER

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


class MarketBase(object):
    MARKET_TEMPLATE = '''[BaseGood]
base = {base_nickname}
{items}'''

    def get_base_nickname(self):
        raise NotImplementedError

    def get_items(self):
        raise NotImplementedError
