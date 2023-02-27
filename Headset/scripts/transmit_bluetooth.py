"""
Author: Charles Bostwick
Website: www.AwaywithCharles.com
GitHub: https://github.com/AwaywithCharles
License: MIT
"""

# Bluetooth module

import serial

# Set up Bluetooth serial port
bluetooth_port = '/dev/rfcomm0'  # Example port name, may vary
bluetooth_baud = 9600
bluetooth_timeout = 1.0

# Open Bluetooth serial port
bluetooth_serial = serial.Serial(
    port=bluetooth_port,
    baudrate=bluetooth_baud,
    timeout=bluetooth_timeout
)

# Read data from ADC and transmit over Bluetooth
while True:
    # Read data from MCP3008 ADC
    adc_value = read_adc()
    # Convert data to string (if necessary)
    data_str = str(adc_value)
    # Send data over Bluetooth
    bluetooth_serial.write(data_str.encode())


------
import serial
import time
import random

# Define the serial port for the HC-05 module
serial_port = '/dev/tty.HC-05-SerialPort'

# Connect to the serial port
ser = serial.Serial(serial_port, baudrate=9600)

# Define the number of amplifiers and ADCs
num_amps = 8
num_adcs = 2

# Define the sampling rate and number of samples to send
sampling_rate = 250
num_samples = 1000

# Generate some random data to send
data = [[random.randint(0, 1023) for i in range(num_amps)] for j in range(num_samples)]

# Send data to the receiving end (e.g. computer)
for i in range(num_samples):
    vals = ','.join(str(x) for x in data[i])
    ser.write(bytes(vals + '\n', 'utf-8'))
    time.sleep(1/sampling_rate)

# Close the serial port
ser.close()
