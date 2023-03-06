"""
Author: Charles Bostwick
Website: www.AwaywithCharles.com
GitHub: https://github.com/AwaywithCharles
License: MIT
"""

import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO

# Set up battery input pins
battery_pin = 'AIN0'
power_pin = 'P9_12'
ADC_SCALE = 1.8
ADC_OFFSET = 0.0

# Set up power output pins
enable_pin = 'P9_15'
power_enable = GPIO.LOW
power_disable = GPIO.HIGH

# Initialize ADC and GPIO pins
ADC.setup()
GPIO.setup(power_pin, GPIO.OUT)
GPIO.setup(enable_pin, GPIO.OUT)

# Read battery voltage and calculate remaining capacity
def read_battery():
    # Read battery voltage and convert to voltage
    adc_value = ADC.read(battery_pin)
    voltage = adc_value * ADC_SCALE + ADC_OFFSET
    # Calculate remaining capacity (specific values will depend on battery type)
    capacity = (voltage - 3.0) / 0.15
    if capacity > 100.0:
        capacity = 100.0
    elif capacity < 0.0:
        capacity = 0.0
    return capacity

# Manage power supply and report battery status
while True:
    # Read battery voltage and calculate remaining capacity
    battery_capacity = read_battery()
    # Check battery level and enable/disable power as needed
    if battery_capacity < 10.0:
        GPIO.output(enable_pin, power_disable)
    else:
        GPIO.output(enable_pin, power_enable)
    # Report battery status (e.g. log, display, or transmit)
    add later...