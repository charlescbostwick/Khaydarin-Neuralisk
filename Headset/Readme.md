# Khaydarin Neurolisk EEG Headset

This is a project to create an EEG (electroencephalogram) headset using a BeagleBone Black and various external components. The goal of the project is to read brainwave data from the user, transmit it over Bluetooth to a computer or mobile device, and display the data in real-time using a data visualization tool like Matplotlib.

The headset will include 20 INA128 instrumentation amplifiers, 20 silver chloride electrodes, 3 MCP3008 ADCs, 20 LM358 operational amplifiers, 1 HC-05 Bluetooth module, resistors, capacitors, diodes, a Gens Ace 3.7V 450mAh LiPo battery, 22 AWG PTFE or silicone wire, JST connectors, header pins and connectors, and electrode connectors. The headset will be 3D printed in TPU, which is a flexible and durable material.

The idea for this project came about when I was having trouble sourcing some components for OpenBCI and decided to build my own. My goal is to create a low-cost alternative for home use that is still of high quality.

To make this headset work, I will be interfacing all of the components with a BeagleBone Black. The INA128 amplifiers will be connected to the power supply, input signal, and output signal pins on the board, while the MCP3008 ADCs will use the SPI interface to communicate with the BeagleBone Black. The LM358 operational amplifiers will be connected in a similar way to the INA128 amplifiers, and the HC-05 Bluetooth module will be connected to the serial interface on the board.

To read the signals from the 20 electrodes, I will need to connect the electrode wires and connectors to the appropriate pins on the BeagleBone Black and write code to read the signals from the INA128 amplifiers and MCP3008 ADCs. I may also need to implement signal processing algorithms in Python to filter and analyze the EEG signals.

## Dependencies
The project requires the following Python libraries and external components:

- **Adafruit_BBIO:** A Python library for interacting with the BeagleBone Black's GPIO pins, SPI, I2C, and ADC.
- **Adafruit_ADS1x15:** A Python library for interacting with the ADS1015 and ADS1115 analog-to-digital converters.
- **Matplotlib:** A Python library for creating data visualizations, including line plots, scatter plots, histograms, and more.
- **NumPy:** A Python library for working with arrays and matrices of numerical data. It is often used in scientific computing and data analysis.
- **PyBluez:** A Python library for Bluetooth communication.
- **PySerial:** A Python library for serial communication.
- **SciPy:** A Python library for scientific computing and data analysis. It includes functions for - optimization, integration, signal processing, and more.
- **Socket:** A Python library for network programming.

## Installation

To install the required Python libraries, you can use the pip package manager to install each library individually. For example, to install Matplotlib, you can run the following command in a terminal:
<pre>
```
sudo pip install matplotlib
```
</pre>
Similarly, you can install NumPy, PyBluez, PySerial, SciPy, and Socket using pip. Adafruit_BBIO and Adafruit_ADS1x15 can also be installed using pip by running the following commands:
<pre>
```
sudo pip install Adafruit_BBIO
sudo pip install Adafruit_ADS1x15
```
</pre>
Please note that some dependencies may already be installed on your system, depending on your operating system and Python distribution. Additionally, there may be other dependencies that you need to install depending on the specific requirements of your project.

## Getting Started
To run the EEG headset, you can use the Python scripts included in the scripts directory. Each script is designed to perform a specific function, such as reading data from the ADC or transmitting data over Bluetooth. You can modify the scripts or combine them as needed to suit your requirements.

The external components, such as the printed circuit board (PCB), 3D printed frame, and electrodes, are stored in the components directory. You can modify or customize these components as needed to fit your specific application.

## Conclusion
The Khaydarin Neurolisk EEG headset is an open-source project that is designed to be customizable and easy to use. However, it is important to note that I am not an expert and this project should be approached with caution. While I have provided instructions and recommendations based on my own experience, there may be risks involved in building and using the headset, and it is up to the user to assess those risks and take appropriate precautions.

By following the instructions in this README file, you can get started with building and using the EEG headset in your own projects. However, it is important to approach the project with caution, and to take appropriate safety measures when building and using the headset.

PS: My scripts are all over the place right now and just generally ideas that I am brainstorming.
