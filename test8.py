import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random



class Graph:

    def __init__(self) -> None:
       
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.xs = []
        self.ys = []
        
    def gen(self):

        gen = random.randint(20,40)
        return gen

    def c_animate(self,i, xs, ys):

        # line = self.__read_data() 
        # dict_value  = find_data(line[12:])

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

    def start_graph(self):

        ani = animation.FuncAnimation(self.fig, self.c_animate, fargs=(self.xs, self.ys), interval=1000)
        plt.show()
            


if __name__ =='__main__':
    g = Graph()
    g.start_graph()