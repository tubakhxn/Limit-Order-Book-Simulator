import bisect

class OrderBook:
    def __init__(self):
        self.bids = []  # [(price, size)]
        self.asks = []  # [(price, size)]
        self.trades = []
        self.best_bid = None
        self.best_ask = None
        self.trade_volume = 0
        self.mid_price = None

    def add_order(self, side, price, size):
        if side == 'buy':
            bisect.insort_left(self.bids, (-price, size))
        else:
            bisect.insort_left(self.asks, (price, size))
        self.update_best_prices()

    def cancel_order(self, side, price):
        book = self.bids if side == 'buy' else self.asks
        for i, (p, s) in enumerate(book):
            if (side == 'buy' and -p == price) or (side == 'sell' and p == price):
                del book[i]
                break
        self.update_best_prices()

    def match_orders(self):
        while self.bids and self.asks:
            bid_price, bid_size = self.bids[0]
            ask_price, ask_size = self.asks[0]
            if -bid_price >= ask_price:
                trade_size = min(bid_size, ask_size)
                self.trades.append({'price': ask_price, 'size': trade_size})
                self.trade_volume += trade_size
                if bid_size > trade_size:
                    self.bids[0] = (bid_price, bid_size - trade_size)
                else:
                    self.bids.pop(0)
                if ask_size > trade_size:
                    self.asks[0] = (ask_price, ask_size - trade_size)
                else:
                    self.asks.pop(0)
            else:
                break
        self.update_best_prices()

    def update_best_prices(self):
        self.best_bid = -self.bids[0][0] if self.bids else None
        self.best_ask = self.asks[0][0] if self.asks else None
        if self.best_bid is not None and self.best_ask is not None:
            self.mid_price = (self.best_bid + self.best_ask) / 2
        else:
            self.mid_price = None

    def get_metrics(self):
        spread = (self.best_ask - self.best_bid) if self.best_bid and self.best_ask else None
        return {
            'best_bid': self.best_bid,
            'best_ask': self.best_ask,
            'spread': spread,
            'trade_volume': self.trade_volume,
            'mid_price': self.mid_price
        }
