import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from datetime import datetime, timedelta

class FourAnimatedGraphs:

    def __init__(self):
        self.x = [datetime.now().strftime('%H:%M:%S')]
        self.y1 = np.sin(np.linspace(0, 10, 100))
        self.y2 = np.cos(np.linspace(0, 10, 100))
        self.y3 = np.exp(-np.linspace(0, 10, 100))
        self.y4 = np.log(np.linspace(1, 11, 100))

        self.fig, self.axs = plt.subplots(2, 2, figsize=(10, 6))
        self.graphs = [self.axs[0, 0], self.axs[0, 1], self.axs[1, 0], self.axs[1, 1]]

        self.lines = []
        for graph in self.graphs:
            line, = graph.plot([], [])
            self.lines.append(line)

        self.animations = []
        for i in range(len(self.lines)):
            animation = FuncAnimation(self.fig, self.update_graph, frames=100, fargs=(i,), interval=50)
            self.animations.append(animation)

    def update_graph(self, frame, i):
        x = [datetime.now().strftime('%H:%M:%S')]
        if i == 0:
            y = np.sin(np.linspace(0, 10, 100) + 0.1 * frame)
        elif i == 1:
            y = np.cos(np.linspace(0, 10, 100) + 0.1 * frame)
        elif i == 2:
            y = np.exp(-(np.linspace(0, 10, 100) + 0.1 * frame))
        elif i == 3:
            y = np.log(np.linspace(1, 11, 100) + 0.1 * frame)
        self.lines[i].set_data(x, y)
        self.graphs[i].relim()
        self.graphs[i].autoscale_view()
        return self.lines[i], self.graphs[i]

    def start_animation(self):
        plt.tight_layout()
        plt.show()



graphs = FourAnimatedGraphs()
graphs.start_animation()