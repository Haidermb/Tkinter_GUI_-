import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from datetime import datetime, timedelta
import random

class FourAnimatedGraphs:

    def __init__(self):
        self.x = [datetime.now() + timedelta(seconds=i) for i in range(100)]
        self.y1 =[]
        self.y2 =[]
        self.y3 = []
        self.y4 = []

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
    def gen2(self):
        a = {}
        l = ['Pressure','Int_temp','Ext_temp','Humidity','Voltage']
        p = random.randint(1,10)
        it = random.randint(1,10)
        et  = random.randint(20,40)
        h = random.randint(60,80)
        v = random.randint(1,5)
        
        a.update({l[0]:p})
        a.update({l[1]:it})
        a.update({l[2]:et})
        a.update({l[3]:h})
        a.update({l[4]:v})    

        return a    


    def update_graph(self, frame, i):
        dict_value = self.gen2()
        if dict_value :
            p = dict_value['Pressure']
            it = dict_value['Int_temp']
            et = dict_value['Ext_temp']
            h = dict_value['Humidity']
            v = dict_value['Voltage']
            
        
        if i == 0:
            y = np.linspace(0, 10, 100)+p
        elif i == 1:
            y = np.linspace(0, 10, 100)+p
        elif i == 2:
            y = np.linspace(0, 10, 100)+p
        elif i == 3:
            y = np.linspace(0, 10, 100)+p
        self.lines[i].set_data(x, y)
        self.graphs[i].relim()
        self.graphs[i].autoscale_view()
        return self.lines[i], self.graphs[i]

    def start_animation(self):
        plt.tight_layout()
        plt.show()
        plt.xticks(rotation=45, ha='right')

graphs = FourAnimatedGraphs()
graphs.start_animation()