"""
Author: Charles Bostwick
Website: www.AwaywithCharles.com
GitHub: https://github.com/AwaywithCharles
License: MIT
"""

# just a start, lots of work to go....

import matplotlib.pyplot as plt

# Set up plot settings
x_min = 0
x_max = 100
y_min = -10
y_max = 10

# Create plot object
fig, ax = plt.subplots()
line, = ax.plot([], [])

# Initialize plot settings
def init_plot():
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([y_min, y_max])
    line.set_data([], [])
    return line,

# Update plot data
def update_plot(data):
    x_data = range(len(data))
    line.set_data(x_data, data)
    return line,

# Read data from ADC and update plot
while True:
    # Read data from MCP3008 ADC
    adc_value = read_adc()
    # Do something with the data (e.g. store, analyze, or transmit)
    # Update plot with new data
    plot_data = [adc_value] * 10
    line, = update_plot(plot_data)
    fig.canvas.draw()
    plt.pause(0.001)