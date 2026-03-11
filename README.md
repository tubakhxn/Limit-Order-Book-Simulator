## Dev/Creator: tubakhxn

# Limit-Order-Book-Simulator

### What is this project about?
This project simulates a real financial exchange limit order book, visualizing order flow and liquidity in real time with advanced 3D quant-style graphics. It models buy/sell orders, market/limit orders, order matching, cancellations, and price impact, and animates the evolving order book for educational and research purposes.

### How to fork
1. Click the "Fork" button at the top right of the GitHub repository page.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/yourusername/Limit-Order-Book-Simulator.git
   ```
3. Install dependencies and run as described below.

### What are all the files?
- **main.py**: Entry point; runs the simulation loop and visualization.
- **orderbook.py**: Implements the order book, order matching, and metrics.
- **trader.py**: Simulates traders placing random orders and cancellations.
- **visualization.py**: Handles real-time 2D/3D animated visualization of the order book and metrics.
- **utils.py**: Utility functions (e.g., price impact calculation).
- **requirements.txt**: Lists Python dependencies (matplotlib, numpy).
- **README.md**: Project documentation, instructions, and overview.

A Python simulator for a financial exchange limit order book with real-time animated visualization.

## Features
- Simulates buy (bid) and sell (ask) orders
- Limit and market orders
- Order matching engine (highest bid matches lowest ask)
- Order cancellations
- Price impact calculation
- Multiple traders with configurable behavior
- Real-time animated visualization using matplotlib
- Metrics: best bid, best ask, spread, trade volume, price movement

## Visualization
- Green bars: buy-side liquidity
- Red bars: sell-side liquidity
- Blue line: mid-price
- Live updating price chart
- Animated order flow

![Visualization Screenshot](placeholder_screenshot.png)

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the simulator:
   ```bash
   python main.py
   ```

## Project Structure
```
Limit-Order-Book-Simulator/
│
├── main.py
├── orderbook.py
├── trader.py
├── visualization.py
├── utils.py
├── requirements.txt
└── README.md
```

## How It Works
- Traders place random limit and market orders.
- The order book matches orders and updates best bid/ask.
- Visualization animates the order flow and metrics in real time.

## Screenshots
Replace `placeholder_screenshot.png` with actual screenshots after running the simulator.

---

**Enjoy simulating and visualizing order flow like a real exchange!**
