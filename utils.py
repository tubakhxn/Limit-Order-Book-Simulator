# Utility functions for the simulator

def price_impact(order_size, liquidity):
    if liquidity == 0:
        return 0
    return order_size / liquidity
