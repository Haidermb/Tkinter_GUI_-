import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd



def open_terminal():
    # Create a new window for the terminal
    terminal_window = tk.Toplevel(root)
    terminal_window.title("Terminal")
    
    # Create a text widget for the terminal
    terminal_text = tk.Text(terminal_window)
    terminal_text.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    # Add some sample text to the terminal
    terminal_text.insert(tk.END, "Welcome to the terminal!\n")
    terminal_text.insert(tk.END, "Type your commands here.\n")

    # Add a horizontal scrollbar to the terminal
    terminal_scrollbar = ttk.Scrollbar(terminal_window, orient="horizontal", command=terminal_text.xview)
    terminal_text.configure(xscrollcommand=terminal_scrollbar.set)
    terminal_scrollbar.pack(side="bottom", fill="x")


# Create a new Tkinter window
root = tk.Tk()
root.title("Graphs, Table, and Terminal")


# Create a notebook widget to hold multiple tabs
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

tab5 = ttk.Frame(notebook)
notebook.add(tab5, text="Graphs (All)")


# Create a button to open the terminal window
terminal_button = ttk.Button(root, text="Open Terminal", command=open_terminal)
terminal_button.pack(side=tk.RIGHT, padx=1, pady=1 )

# Create a frame for the first tab
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Graph 1")

# Create a Matplotlib figure and add a plot to it
fig1 = plt.Figure(figsize=(5, 4), dpi=100)
ax1 = fig1.add_subplot(111)
ax1.plot([1, 2, 3, 4], [10, 20, 30, 40])

# Add the plot to a Tkinter canvas
canvas1 = FigureCanvasTkAgg(fig1, master=tab1)
canvas1.draw()
canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a frame for the second tab
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Graph 2")

# Create another Matplotlib figure and add a plot to it
fig2 = plt.Figure(figsize=(5, 4), dpi=100)
ax2 = fig2.add_subplot(111)
ax2.plot([1, 2, 3, 4], [40, 30, 20, 10])

# Add the plot to a Tkinter canvas
canvas2 = FigureCanvasTkAgg(fig2, master=tab2)
canvas2.draw()
canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a frame for the third tab
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Graph 3")

# Create a third Matplotlib figure and add a plot to it
fig3 = plt.Figure(figsize=(5, 4), dpi=100)
ax3 = fig3.add_subplot(111)
ax3.plot([1, 2, 3, 4], [20, 10, 30, 40])

# Add the plot to a Tkinter canvas
canvas3 = FigureCanvasTkAgg(fig3, master=tab3)
canvas3.draw()
canvas3.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a frame for the fourth tab
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="Graph 4")

# Create a fourth Matplotlib figure and add a plot to it
fig4 = plt.Figure(figsize=(5, 4), dpi=100)
ax4 = fig4.add_subplot(111)
ax4.plot([1, 2, 3, 4], [30, 40, 10, 20])

# Add the plot to a Tkinter canvas
canvas4 = FigureCanvasTkAgg(fig4, master=tab4)
canvas4.draw()
canvas4.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


fig5 = plt.Figure(figsize=(5, 4), dpi=100, tight_layout=True)
ax1 = fig5.add_subplot(2, 2, 1)
ax2 = fig5.add_subplot(2, 2, 2)
ax3 = fig5.add_subplot(2, 2, 3)
ax4 = fig5.add_subplot(2, 2, 4)
ax1.plot([1, 2, 3, 4], [10, 20, 30, 40])
ax2.plot([1, 2, 3, 4], [40, 30, 20, 10])
ax3.plot([1, 2, 3, 4], [20, 10, 30, 40])
ax4.plot([1, 2, 3, 4], [30, 40, 10, 20])
canvas1 = FigureCanvasTkAgg(fig5, master=tab5)
canvas1.draw()
canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)




# terminal_frame = ttk.Frame(root)
# terminal_frame.pack(fill='both', expand=True)

# terminal_text = tk.Text(terminal_frame)
# terminal_text.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# terminal_text.insert(tk.END, "Welcome to the terminal!\n")
# terminal_text.insert(tk.END, "Type your commands here.\n")

# terminal_scrollbar = ttk.Scrollbar(terminal_frame, orient="horizontal", command=terminal_text.xview)
# terminal_text.configure(xscrollcommand=terminal_scrollbar.set)
# terminal_scrollbar.pack(side="bottom", fill="x")

# Create a frame for the table
table_frame = ttk.Frame(root)
table_frame.pack(fill='both', expand=True)

# Create a Pandas DataFrame to use as the table data
data = {'Name': ['John', 'Mary', 'Steve', 'Sarah','John', 'Mary', 'Steve', 'Sarah','John', 'Mary', 'Steve', 'Sarah'],
        'Age': [25, 30,50,60,25, 30,50,60,25, 30,50,60],
         'Email':['test1@gmail.com','test3@gmail.com','test4@gmail.com','test5@gmail.com','5t@gmail.com','t65@gmail.com','45t@gmail.com','t23@gmail.com','32t@gmail.com','213t@gmail.com','t@gmail.com','t@gmail.com'],
         'phone':[12334324,21889787,82738978,12736782,12334324,21889787,82738978,12736782,12334324,21889787,82738978,12736782]   }

df = pd.DataFrame(data)
table = ttk.Treeview(table_frame, columns=list(df.columns), show='headings')

for col in df.columns:
    table.heading(col, text=col)

for i, row in df.iterrows():
    table.insert("", "end", values=list(row))

scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
table.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
table.pack(side="left", fill="both", expand=True)

# scroll_bar = ttk.Scrollbar(root)

# scroll_bar.pack( side = 'right',fill = 'y')

# scrollbar = ttk.Scrollbar(root, orient="vertical")
# root.configure(yscrollcommand=scrollbar.set)

root.mainloop()