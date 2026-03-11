from orderbook import OrderBook
from trader import Trader
from visualization import Visualizer
import utils

import time
import random

def run_simulation():
    order_book = OrderBook()
    # Add initial liquidity to both sides
    for price in range(99, 101):
        order_book.add_order('buy', price, random.randint(5, 15))
        order_book.add_order('sell', price + 1, random.randint(5, 15))
    order_book.match_orders()

    traders = [Trader(f"Trader_{i}", order_book, bias=random.choice(['buy', 'sell'])) for i in range(5)]
    vis = Visualizer(order_book)

    for _ in range(500):
        # Ensure at least one buy and one sell order per round
        traders[0].place_random_order(force_side='buy')
        traders[1].place_random_order(force_side='sell')
        for trader in traders[2:]:
            trader.place_random_order()
        vis.update()
        time.sleep(0.05)
    vis.show_final()

if __name__ == "__main__":
    run_simulation()
