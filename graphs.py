import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

from serial_connec import *

class Graph_1:
    def __init__(self,x: int,y: int,k:str) -> None:
       
        # Create a Matplotlib figure and add a plot to it
        self.fig = plt.Figure(figsize=(x, y), dpi=100)
        self.ax = self.fig1.add_subplot(111)
        self.xs = []
        self.ys = []
        self.k = k
        
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
        
    def c_animate(self,i,xs,ys):
        s1 = SerialConnection()
        # line =     
        # line = self.__read_data() 
        # dict_value  = find_data(line[12:])
        dict_value  = self.gen2()
        if dict_value :
            y = dict_value[self.k]
            
        #h = self.gen()
        
        # Add x and y to lists
        xs.append(dt.datetime.now().strftime('%H:%M:%S'))
        ys.append(y)


        # Limit x and y lists to 10 items
        xs = xs[-20:]
        ys = ys[-20:]
        # Draw x and y lists
        self.ax.clear()
        self.ax.plot(xs, ys,marker ='.',color ='r')
        self.ax.set_xticklabels(xs,rotation=45)
        plt.subplots_adjust(bottom=0.38)
        self.ax.set_title(self.k)
        
    def start_graph(self):
   
        self.ani = animation.FuncAnimation(self.fig, self.c_animate ,fargs=(self.xs, self.ys), interval=1000)
        plt.show()



class Graph_4:

    def __init__(self,x,y) -> None:
       
        self.fig = plt.figure(figsize=(x,y),tight_layout=True)
        self.ax1 = self.fig.add_subplot(2, 2, 1)
        self.ax2 = self.fig.add_subplot(2, 2, 2)
        self.ax3 = self.fig.add_subplot(2, 2, 3)
        self.ax4 = self.fig.add_subplot(2, 2, 4)


        self.xs = []
        self.ys = []
        self.y1 = []
        self.y2 = []
        self.y3 = []
        self.y4 = []

        
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
        
    def c_animate(self,i,xs,y1,y2,y3,y4):

        # line = self.__read_data() 
        # dict_value  = find_data(line[12:])
        dict_value  = self.gen2()
        if dict_value :
            p = dict_value['Pressure']
            it = dict_value['Int_temp']
            et = dict_value['Ext_temp']
            h = dict_value['Humidity']
            v = dict_value['Voltage']
        
        #h = self.gen()
        
        # Add x and y to lists
        xs.append(dt.datetime.now().strftime('%H:%M:%S'))
        y1.append(p)
        y2.append(et)
        y3.append(h)
        y4.append(v)



        # Limit x and y lists to 10 items
        xs = xs[-10:]
        y1 = y1[-10:]
        y2 = y2[-10:]
        y3 = y3[-10:]
        y4 = y4[-10:]

        # Draw x and y lists
        self.ax1.clear()
        self.ax1.plot(xs, y2,marker ='.',color ='r')
        self.ax1.set_xticklabels(xs,rotation=45)


        self.ax2.clear()
        self.ax2.plot(xs, y2,marker='.',color ='b')
        self.ax2.set_xticklabels(xs,rotation=45)



        self.ax3.clear()
        self.ax3.plot(xs, y3,marker ='.',color ='g')
        self.ax3.set_xticklabels(xs,rotation=45)


        self.ax4.clear()
        self.ax4.plot(xs, y4,marker ='.')
        self.ax4.set_xticklabels(xs,rotation=45)

        # Format plot
        
        #plt.xticks(rotation=45, ha='right')
        #plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.38)
        self.ax1.set_title('Pressure')
        self.ax2.set_title('Ext_Temp')
        self.ax3.set_title('Humid')
        self.ax4.set_title('Volt')
        
        #plt.title('TMP102 Temperature over Time')
        #plt.ylabel('Temperature (deg C)')

    def start_graph(self):
   
        self.ani = animation.FuncAnimation(self.fig, self.c_animate ,fargs=(self.xs, self.y1,self.y2,self.y3,self.y4), interval=1000)
        plt.show()


if __name__ =='__main__':
    
    p = Graph_4(8,8)
    
    p.start_graph()
    

