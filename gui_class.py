import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Gui:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Graphs, Table, and Terminal")
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)
        self.tab1 = ttk.Frame(self.notebook)
        
        
    def tab(self):
            
        
        tab1 = ttk.Frame(self.notebook)
        self.notebook.add(tab1, text="Graph 1")

        # Create a Matplotlib figure and add a plot to it
        fig1 = plt.Figure(figsize=(5, 4), dpi=100)
        ax1 = fig1.add_subplot(111)
        ax1.plot([1, 2, 3, 4], [10, 20, 30, 40])

        # Add the plot to a Tkinter canvas
        canvas1 = FigureCanvasTkAgg(fig1, master=tab1)
        canvas1.draw()
        canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)




        
