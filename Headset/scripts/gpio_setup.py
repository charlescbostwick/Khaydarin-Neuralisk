"""
Author: Charles Bostwick
Website: www.AwaywithCharles.com
GitHub: https://github.com/AwaywithCharles
License: MIT
"""

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import Adafruit_BBIO.GPIO as GPIO
import numpy as np
import time
import signal_processing

# Set up the MCP3008 ADCs
CLK = 'P9_22'
MISO = 'P9_21'
MOSI = 'P9_18'
CS1 = 'P9_17'
CS2 = 'P9_13'
CS3 = 'P9_15'

mcp1 = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS1, miso=MISO, mosi=MOSI)
mcp2 = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS2, miso=MISO, mosi=MOSI)
mcp3 = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS3, miso=MISO, mosi=MOSI)

# Set up the GPIO pins for the LM358s and INA128s
INA128_PD = 'P9_12'
INA128_GAIN = 'P9_14'
LM358_1 = 'P9_24'
LM358_2 = 'P9_26'
LM358_3 = 'P9_30'
LM358_4 = 'P9_28'
LM358_5 = 'P9_41'
LM358_6 = 'P9_42'
LM358_7 = 'P9_27'
LM358_8 = 'P9_25'

GPIO.setup(INA128_PD, GPIO.OUT)
GPIO.setup(INA128_GAIN, GPIO.OUT)
GPIO.setup(LM358_1, GPIO.OUT)
GPIO.setup(LM358_2, GPIO.OUT)
GPIO.setup(LM358_3, GPIO.OUT)
GPIO.setup(LM358_4, GPIO.OUT)
GPIO.setup(LM358_5, GPIO.OUT)
GPIO.setup(LM358_6, GPIO.OUT)
GPIO.setup(LM358_7, GPIO.OUT)
GPIO.setup(LM358_8, GPIO.OUT)

# Set the gain for the INA128s
GPIO.output(INA128_GAIN, GPIO.HIGH)  # Set gain to 1000

# Enable the INA128s
GPIO.output(INA128_PD, GPIO.LOW)

# Define the number of amplifiers and ADCs
num_amps = 8
num_adcs = 3

# Define the sampling rate and number of samples to collect
sampling_rate = 250
num_samples = 1000

# Initialize the data array
data = np.zeros((num_amps, num_samples))

# Collect data from the ADCs
for i in range(num_samples):
    # Read data from the MCP3008 ADCs
    vals1 = [mcp1.read_adc(i) for i in range(num_amps)]
    vals2 = [mcp2.read_adc(i) for i in range(num_amps)]
    vals3 = [mcp3.read_adc(i) for i in range(num_amps)]
    vals = np.array(vals1 + vals2 + vals3)
    
    # Store the data in the array
    data[:, i] = vals
    
    # Wait for the next sample
    time.sleep(1/sampling_rate)

# Disable the INA128s
GPIO.output(INA128_PD, GPIO.HIGH)

# Apply signal processing techniques to the data
processed_data = signal_processing.process_data(data, sampling_rate)

# Plot the data
plt.imshow(processed_data.T, cmap='hot', aspect='auto', origin='lower')
plt.show()

# Close the SPI interface
spi.close()
