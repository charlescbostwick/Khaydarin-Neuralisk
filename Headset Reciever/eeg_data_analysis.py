"""
Author: Charles Bostwick
Website: www.AwaywithCharles.com
GitHub: https://github.com/AwaywithCharles
License: MIT
"""

import serial
import time
import numpy as np
import matplotlib.pyplot as plt
import signal_processing

# Define the serial port for the HC-05 module
serial_port = '/dev/tty.HC-05-SerialPort'

# Connect to the serial port
ser = serial.Serial(serial_port, baudrate=9600)

# Define the number of amplifiers and ADCs
num_amps = 8
num_adcs = 2

# Define the sampling rate and number of samples to collect
sampling_rate = 250
num_samples = 1000

# Initialize the data array
data = np.zeros((num_amps, num_samples))

# Collect data from the BeagleBone Black
for i in range(num_samples):
    # Read a line of data from the serial port
    line = ser.readline().decode('utf-8').strip()
    
    # Parse the data into an array
    vals = [int(x) for x in line.split(',')]
    
    # Store the data in the array
    data[:, i] = np.array(vals)
    
    # Wait for the next sample
    time.sleep(1/sampling_rate)

# Apply signal processing techniques to the data
processed_data = signal_processing.process_data(data, sampling_rate)

# Plot the data
plt.imshow(processed_data.T, cmap='hot', aspect='auto', origin='lower')
plt.show()

# Close the serial port
ser.close()
