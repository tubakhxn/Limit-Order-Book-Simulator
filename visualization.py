
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm

class Visualizer:
    def __init__(self, order_book):
        self.order_book = order_book
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.price_history = []
        self.volume_history = []
        self.liquidity_history = []
        self.max_snapshots = 50
        self.ani = animation.FuncAnimation(self.fig, self.animate, interval=100, blit=False)

    def update(self):
        self.price_history.append(self.order_book.mid_price)
        self.volume_history.append(self.order_book.trade_volume)
        # Capture liquidity snapshot for 3D histogram
        liquidity = {}
        for p, s in [(-p, s) for p, s in self.order_book.bids]:
            liquidity[p] = liquidity.get(p, 0) + s
        for p, s in [(p, s) for p, s in self.order_book.asks]:
            liquidity[p] = liquidity.get(p, 0) + s
        self.liquidity_history.append(liquidity)
        # Keep only last max_snapshots
        if len(self.liquidity_history) > self.max_snapshots:
            self.liquidity_history.pop(0)
        plt.pause(0.001)

    def animate(self, frame):
        self.ax.clear()
        if not self.liquidity_history:
            return
        N = min(self.max_snapshots, len(self.liquidity_history))
        liquidity_snapshots = self.liquidity_history[-N:]
        prices = sorted(set(p for snap in liquidity_snapshots for p in snap.keys()))
        times = np.arange(len(liquidity_snapshots))
        liquidity_matrix = np.zeros((len(times), len(prices)))
        for t, snap in enumerate(liquidity_snapshots):
            for i, p in enumerate(prices):
                liquidity_matrix[t, i] = snap.get(p, 0)
        xpos, ypos = np.meshgrid(prices, times)
        xpos = xpos.flatten()
        ypos = ypos.flatten()
        zpos = np.zeros_like(xpos)
        dx = 0.4 * np.ones_like(xpos)
        dy = 0.4 * np.ones_like(ypos)
        dz = liquidity_matrix.flatten()
        # Color gradient: blue for bids, red for asks, based on price
        colors = cm.coolwarm((xpos - min(prices)) / (max(prices) - min(prices) + 1e-6))
        self.ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors, alpha=0.8)
        self.ax.set_title('Animated 3D Order Book Liquidity Histogram')
        self.ax.set_xlabel('Price')
        self.ax.set_ylabel('Time')
        self.ax.set_zlabel('Liquidity')
        self.ax.set_xlim(min(prices)-1, max(prices)+1)
        self.ax.set_ylim(0, self.max_snapshots)
        self.ax.set_zlim(0, np.max(liquidity_matrix)+5)
        metrics = self.order_book.get_metrics()
        metric_text = '\n'.join([f'{k}: {v}' for k, v in metrics.items()])
        self.ax.text2D(0.05, 0.95, metric_text, transform=self.fig.transFigure, fontsize=10)

    def show_final(self):
        plt.show()
