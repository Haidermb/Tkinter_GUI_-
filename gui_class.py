import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graphs import *
import datetime as dt
  

class Gui:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Graphs, Table, and Terminal")
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)
                    
        
class tab:

    def __init__(self,n):
        # Create a frame for the first tab
        self.tab = ttk.Frame(n)


class Canvas:
    
    def __init__(self,fig,tab1) -> None:
        
        # Add the plot to a Tkinter canvas
        
            self.canvas = FigureCanvasTkAgg(fig, master=tab1)
            # self.canvas.draw()
            # self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

class Table:

    def __init__(self,r) -> None:
        
        self.table_frame = ttk.Frame(r)
        self.table_frame.pack(fill='both', expand=True)
        self.table = ttk.Treeview(self.table_frame, columns=('Time','Pressure','Ext_temp','Humidity','Voltage'), show='headings',height=5)


        self.scrollbar = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.table.pack(side="left", fill="both", expand=True)


        self.table.column("# 1", anchor='center', width=100)
        self.table.column("# 2", anchor='center', width=100)
        self.table.column("# 3", anchor='center', width=100)
        self.table.column("# 4", anchor='center', width=100)
        self.table.column("# 5", anchor='center', width=100)


    def insert(self,d_v):
        x = dt.datetime.now().strftime('%H:%M:%S')
        self.table.insert('',index=0,values=(x,d_v['Pressure'],d_v['Ext_temp'],d_v['Humidity'],d_v['Voltage']))     
        