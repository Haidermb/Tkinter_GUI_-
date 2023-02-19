import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the figure and axis
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 6))
fig.subplots_adjust(hspace=0.5, wspace=0.5)
axs = axs.ravel()

# Define the x data
x = np.linspace(0, 2*np.pi, 200)

# Define the initial y data for each graph
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x)

# Create the line objects for each graph
lines = []
for i, ax in enumerate(axs):
    if i == 0:
        line, = ax.plot(x, y1)
    elif i == 1:
        line, = ax.plot(x, y2)
    elif i == 2:
        line, = ax.plot(x, y3)
    else:
        line, = ax.plot(x, y4)
    lines.append(line)

# Define the animation function
def animate(frame):
    # Update the y data for each graph
    y1_new = np.sin(x + frame/10)
    y2_new = np.cos(x + frame/10)
    y3_new = np.tan(x + frame/10)
    y4_new = np.exp(x/10)*np.sin(x + frame/20)
    
    # Set the new y data for each line object
    lines[0].set_ydata(y1_new)
    lines[1].set_ydata(y2_new)
    lines[2].set_ydata(y3_new)
    lines[3].set_ydata(y4_new)
    
    return lines

# Create the animation object
animation = FuncAnimation(fig, animate, frames=200, interval=30)

# Show the plot
#plt.show()
x = np.linspace(0, 2*np.pi, 200)
print(x.shape)
print(lines[0])