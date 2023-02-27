"""
Author: Charles Bostwick
Website: www.AwaywithCharles.com
GitHub: https://github.com/AwaywithCharles
License: MIT
"""

import socket

# Set up socket settings
server_ip = '192.168.1.100'  # Example IP address, may vary
server_port = 1234
buffer_size = 1024

# Create socket object and connect to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# Read data from ADC and transmit over network
while True:
    # Read data from MCP3008 ADC
    adc_value = read_adc()
    # Convert data to string (if necessary)
    data_str = str(adc_value)
    # Send data over network
    client_socket.sendall(data_str.encode())