import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graphs import Graph
        

class Gui:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Graphs, Table, and Terminal")
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

    
            
            
        
class tab(Gui):

    def new_tab(self):
        # Create a frame for the first tab
        self.tab = ttk.Frame(self.notebook)


class Canvas(tab):
    
    def __init__(self) -> None:
        # Create a Matplotlib figure and add a plot to it
            self.g = Graph()
        
        # Add the plot to a Tkinter canvas
        
            self.canvas = FigureCanvasTkAgg(self.g.fig, master=self.tab)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


