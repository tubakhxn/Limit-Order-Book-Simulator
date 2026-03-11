import random

class Trader:
    def __init__(self, name, order_book, bias=None):
        self.name = name
        self.order_book = order_book
        self.bias = bias  # 'buy', 'sell', or None

    def place_random_order(self, force_side=None):
        # Improve trader logic: bias, forced side, balanced flow
        if force_side:
            side = force_side
        elif self.bias:
            side = self.bias if random.random() < 0.7 else ('sell' if self.bias == 'buy' else 'buy')
        else:
            side = random.choice(['buy', 'sell'])
        price = random.uniform(99, 102)
        size = random.randint(1, 10)
        order_type = random.choices(['limit', 'market'], weights=[0.7, 0.3])[0]
        if order_type == 'limit':
            self.order_book.add_order(side, round(price, 2), size)
        else:
            # Market order: match immediately
            if side == 'buy' and self.order_book.asks:
                price = self.order_book.asks[0][0]
                self.order_book.add_order('buy', price, size)
            elif side == 'sell' and self.order_book.bids:
                price = -self.order_book.bids[0][0]
                self.order_book.add_order('sell', price, size)
        self.order_book.match_orders()
        # Random cancellation
        if random.random() < 0.1:
            if side == 'buy' and self.order_book.bids:
                price = -self.order_book.bids[0][0]
                self.order_book.cancel_order('buy', price)
            elif side == 'sell' and self.order_book.asks:
                price = self.order_book.asks[0][0]
                self.order_book.cancel_order('sell', price)
