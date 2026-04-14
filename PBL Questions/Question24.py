class MarketClosedError(Exception):
    pass

class StockBot:
    def execute_trade(self, market_open):
        if not market_open:
            raise MarketClosedError()
        print("Trade done")

try:
    sb = StockBot()
    sb.execute_trade(False)
except MarketClosedError:
    print("Market closed")
