import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import threading
import sys




class Graph:

    def __init__(self) -> None:
       
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.xs = []
        self.ys = []

        self.v = None
        
    def gen(self):

        gen = random.randint(20,40)
        return gen

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
        
    def c_animate(self,i, xs, ys):

        # line = self.__read_data() 
        # dict_value  = find_data(line[12:])
        # if dict_value :
            # p = dict_value['Pressure']
            # it = dict_value['Int_temp']
            # et = dict_value['Ext_temp']
            # h = dict_value['Humidity']
            # v = dict_value['Voltage']
        
        h = self.gen()

        # Add x and y to lists
        xs.append(dt.datetime.now().strftime('%H:%M:%S'))
        ys.append(h)

        # Limit x and y lists to 20 items
        xs = xs[-20:]
        ys = ys[-20:]

        # Draw x and y lists
        self.ax.clear()
        self.ax.plot(xs, ys)

        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('TMP102 Temperature over Time')
        plt.ylabel('Temperature (deg C)')

    def c_animate_test(self,i, xs, ys):

        if self.__Serial.is_open:    
        # line = self.__read_data() 
        # dict_value  = find_data(line[12:])
        # if dict_value :
            a = None
            dict_value = self.gen2() 
            if dict_value :

                v = self.v
                value = dict_value[v]
                # p = dict_value['Pressure']
                # it = dict_value['Int_temp']
                # et = dict_value['Ext_temp']
                # h = dict_value['Humidity']
                # v = dict_value['Voltage']
        

        h = value

        # Add x and y to lists
        xs.append(dt.datetime.now().strftime('%H:%M:%S'))
        ys.append(h)

        # Limit x and y lists to 20 items
        xs = xs[-20:]
        ys = ys[-20:]

        # Draw x and y lists
        self.ax.clear()
        self.ax.plot(xs, ys)

        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('TMP102 Temperature over Time')
        plt.ylabel('Temperature (deg C)')

            
    def start_graph(self,w):

        self.v = w    
        self.ani = animation.FuncAnimation(self.fig, self.c_animate ,fargs=(self.xs, self.ys), interval=1000)
        plt.show()


if __name__ =='__main__':
    
    p = Graph()
    v = Graph()
    h = Graph()
    t = Graph()
    
    #l = ['Pressure','Int_temp','Ext_temp','Humidity','Voltage']

    # t1 = threading.Thread(target=p.start_graph('Pressure',))
    #t2 = threading.Thread(target=t.start_graph,args=('Ext_temp',))
    # t3 = threading.Thread(target=h.start_graph(),args=('Humidity',))
    # t3 = threading.Thread(target=v.start_graph(),args=('Voltage',))
    # t2.start()    
    p.start_graph(None)
    

