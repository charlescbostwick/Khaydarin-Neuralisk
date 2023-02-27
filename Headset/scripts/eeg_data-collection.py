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
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

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

# Define the SPI bus and device for the MCP3008 ADCs
SPI_PORT = 0
SPI_DEVICE_1 = 0
SPI_DEVICE_2 = 1
mcp_1 = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE_1))
mcp_2 = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE_2))

# Define the voltage reference for the MCP3008 ADCs
VREF = 3.3

# Initialize the data array
data = np.zeros((num_amps, num_samples))

# Collect data from the BeagleBone Black
for i in range(num_samples):
    # Read a line of data from the serial port
    line = ser.readline().decode('utf-8').strip()
    
    # Parse the data into an array
    vals = [int(x) for x in line.split(',')]
    
    # Read the voltage from the ADCs
    for j in range(num_amps):
        if j < 8:
            # Read from ADC 1
            adc_value = mcp_1.read_adc(j)
        else:
            # Read from ADC 2
            adc_value = mcp_2.read_adc(j - 8)
        
        # Convert the ADC value to a voltage
        voltage = adc_value * VREF / 1023
        
        # Amplify the voltage using the LM358 OP-Amps and INA128 amps
        voltage = voltage / (1000 / (1000 + 1))  # R1 = 1 kΩ, R2 = 100 kΩ
        voltage = voltage * (2 + (2 / 1))  # R3 = 2 kΩ, R4 = 1 kΩ
        
        # Store the data in the array
        data[j, i] = voltage
    
    # Wait for the next sample
    time.sleep(1/sampling_rate)

# Apply signal processing techniques to the data
processed_data = signal_processing.process_data(data, sampling_rate)

# Plot the data
plt.imshow(processed_data.T, cmap='hot', aspect='auto', origin='lower')
plt.show()

# Close the serial port
ser.close()
