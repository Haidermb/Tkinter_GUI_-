import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graphs import *
        

class Gui:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Graphs, Table, and Terminal")
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

    
            
            
        
class tab():

    def __init__(self,n):
        # Create a frame for the first tab
        self.tab = ttk.Frame(n)


class Canvas():
    
    def __init__(self,fig,tab1) -> None:
        
        # Add the plot to a Tkinter canvas
        
            self.canvas = FigureCanvasTkAgg(fig, master=tab1)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


