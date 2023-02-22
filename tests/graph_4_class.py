import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime, timedelta
import random


class Graphs_4:

    def __init__(self) -> None:
        self.fig, self.axs = plt.subplots(2, 2, figsize=(10, 6))
        self.graphs = [self.axs[0, 0], self.axs[0, 1], self.axs[1, 0], self.axs[1, 1]]
        self.x = [datetime.now() + timedelta(seconds=i) for i in range(100)]
        self.y1 = []
        self.y2 = []
        self.y3 = []
        self.y4 = []


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

    def animate(self,i):

        # line = self.__read_data() 
        # dict_value  = find_data(line[12:])
        dict_value = self.gen2()
        if dict_value :
            p = dict_value['Pressure']
            it = dict_value['Int_temp']
            et = dict_value['Ext_temp']
            h = dict_value['Humidity']
            v = dict_value['Voltage']
        
        
        # Add x and y to lists
        self.x.append(dt.datetime.now().strftime('%H:%M:%S'))

        self.lines[0].set_ydata(p)
        self.lines[1].set_ydata(et)
        self.lines[2].set_ydata(h)
        self.lines[3].set_ydata(v)
        

        return self.lines

    def _2_animate(self,i,x,y1,y2,y3,y4):

        # line = self.__read_data() 
        # dict_value  = find_data(line[12:])
        dict_value = self.gen2()
        if dict_value :
            p = dict_value['Pressure']
            it = dict_value['Int_temp']
            et = dict_value['Ext_temp']
            h = dict_value['Humidity']
            v = dict_value['Voltage']
        
        
        # Add x and y to lists
        x.append(dt.datetime.now().strftime('%H:%M:%S'))
        y1.append(p)
        y2.append(et)
        y1.append(h)
        y1.append(v)

        


    def start_graph(self):
        # Create the animation object
        animation = FuncAnimation(self.fig, self._2_animate, fargs = (self.x,self.y1,self.y2,self.y3,self.y4,), interval=30)

        # Show the plot
        plt.show()


if __name__ =='__main__':

    g = Graphs_4()
    a = g.gen2()
    #print(a)
    g.start_graph()
    