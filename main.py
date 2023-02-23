from graphs import *
from gui_class import *
from serial_connec import *




def create_gui(gui,ser,table):
    

    t1 =tab(gui.notebook)
    gui.notebook.add(t1.tab, text="Graphs (All)")
    g1 = Graph_4(6,6,ser,table)
    c1 = Canvas(g1.fig,t1.tab)
    g1.start_graph()
    c1.canvas.draw()
    c1.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


    t2 =tab(gui.notebook)
    gui.notebook.add(t2.tab, text="Pressure")
    g2 = Graph_1(5,4,'Pressure',ser,'r',None)
    c2 = Canvas(g2.fig,t2.tab)
    g2.start_graph()
    c2.canvas.draw()
    c2.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    t3 =tab(gui.notebook)
    gui.notebook.add(t3.tab, text="Ext_temp")
    g3 = Graph_1(5,4,'Ext_temp',ser,'b',None)
    c3 = Canvas(g3.fig,t3.tab)
    g3.start_graph()
    c3.canvas.draw()
    c3.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    t4 =tab(gui.notebook)
    gui.notebook.add(t4.tab, text="Humidity")
    g4 = Graph_1(5,4,'Humidity',ser,'g',None)
    c4 = Canvas(g4.fig,t4.tab)
    g4.start_graph()
    c4.canvas.draw()
    c4.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    t5 =tab(gui.notebook)
    gui.notebook.add(t5.tab, text="voltage")
    g5 = Graph_1(5,4,'Voltage',ser,None,None)
    c5 = Canvas(g5.fig,t5.tab)
    g5.start_graph()
    c5.canvas.draw()
    c5.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    columns = ['Time','Pressure','Ext_temp','Humidity','Voltage']
    
    for col in columns:
        table.table.heading(col, text=col)

     
    
    

def main():

    gui = Gui()
    ser = SerialConnection()
    
    create_gui(gui,ser)

    ser.main()

    try : 
        a = ser.start_conn()
        if a:
            print(f'Connected to port {ser.get_port} ')
            try :
                gui.root.mainloop()
                    
            except ValueError :
                print(f'Error in gui code')
        else :
            print(f'Error in starting connection to port {ser.get_port}')        
            ser.close_conn()
    except ValueError: 

        print(f'Error in starting connection to port {ser.get_port}')        


def test():
    
    gui = Gui()
    ser = SerialConnection()
    table = Table(gui.root)
    create_gui(gui,ser,table)
    

    gui.root.mainloop()
    



test()