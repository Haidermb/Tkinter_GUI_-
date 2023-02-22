from graphs import *
from gui_class import *
from serial_connec import *


ser = SerialConnection()

ser.main()

try : 
    a = ser.start_conn()
    if a:
        print(f'Connected to port {ser.get_port} ')

except ValueError: 

    print(f'Error in starting connection to port {ser.get_port}')        


gui = Gui()

t1 =tab(gui.notebook)
g1 = Graph_4(5,4)
c1 = Canvas(g1.fig,t1)

t2 =tab(gui.notebook)
g2 = Graph_1(5,4,'Pressure',ser)
c2 = Canvas(g1.fig,t1)

t3 =tab(gui.notebook)
g3 = Graph_1()
c3 = Canvas(g1.fig,t1)

t4 =tab(gui.notebook)
g4 = Graph_1()
c4 = Canvas(g1.fig,t1)

t5 =tab(gui.notebook)
g5 = Graph_1()
c5 = Canvas(g1.fig,t1)

gui.root.mainloop()