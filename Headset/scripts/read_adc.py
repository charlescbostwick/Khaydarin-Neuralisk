"""
Author: Charles Bostwick
Website: www.AwaywithCharles.com
GitHub: https://github.com/AwaywithCharles
License: MIT
"""

# MCP3008 ADC - start for basic reading

import Adafruit_ADS1x15
import Adafruit_BBIO.SPI as SPI
import time

# Set up ADC input pins
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
ADC_CHANNEL = 0

# Configure ADC and read data
def read_adc():
    # Set ADC gain and read analog voltage
    adc.set_gain(GAIN)
    value = adc.read_adc(ADC_CHANNEL)
    return value

# Read data from ADC and do something with it
while True:
    # Read data from MCP3008 ADC
    adc_value = read_adc()
    # Do something with the data (e.g. store, analyze, or transmit)

# Set up SPI interfaces for INA128 amplifiers
ina128_spi = SPI.SPI(1, 0) # (bus, device)
ina128_spi.mode = SPI.MODE_0
ina128_spi.msh = 1000000 # set clock speed

# Set up SPI interface for MCP3008 ADCs
mcp3008_spi = SPI.SPI(0, 0) # (bus, device)
mcp3008_spi.mode = SPI.MODE_0
mcp3008_spi.msh = 1000000 # set clock speed

# Set up pins for reading signals from electrodes
electrode_pins = ["P9_39", "P9_40", "P9_37", "P9_38", "P9_33", "P9_36", "P9_35", "P9_34", "P9_31", "P9_32",
                  "P9_29", "P9_30", "P9_27", "P9_28", "P9_25", "P9_26", "P9_23", "P9_24", "P9_21", "P9_22"]

# Loop through electrodes and read signal from each one
for i, electrode in enumerate(electrode_pins):
    # Set up INA128 amplifier for current electrode
    ina128_spi.writebytes([0x40 | (i << 2)]) # write to configuration register
    time.sleep(0.001) # wait for settling time
    # Read signal from current electrode using MCP3008 ADC
    mcp3008_spi.writebytes([0x01, (i % 8) << 4, 0x00]) # send read command
    adc_data = mcp3008_spi.readbytes(3) # read 3 bytes of data
    adc_value = ((adc_data[1] & 0x03) << 8) + adc_data[2] # combine bytes to get ADC value
    print("Electrode %d signal: %d" % (i, adc_value))
