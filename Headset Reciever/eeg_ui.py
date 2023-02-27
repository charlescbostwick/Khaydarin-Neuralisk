"""
Author: Charles Bostwick
Website: www.AwaywithCharles.com
GitHub: https://github.com/AwaywithCharles
License: MIT
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QSlider
from PyQt5.QtCore import Qt, QTimer
import serial
from collections import deque
import signal_processing

class EEGVisualizer(QWidget):
    def __init__(self):
        super().__init__()
        
        # Initialize the UI elements
        self.data_label = QLabel("EEG Data")
        self.slider_label = QLabel("Threshold: 50")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        
        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.data_label)
        layout.addWidget(self.slider_label)
        layout.addWidget(self.slider)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        self.setLayout(layout)
        
        # Set up the serial connection
        self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
        self.ser.flush()
        
        # Set up the timer for periodically reading data from the serial port
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        
        # Set up the deque for storing data
        self.data = deque(maxlen=200)
        
        # Connect the button signals to their respective functions
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.slider.valueChanged.connect(self.slider_change)
        
    def start(self):
        self.timer.start(50)
        
    def stop(self):
        self.timer.stop()
        
    def update_data(self):
        while self.ser.in_waiting:
            line = self.ser.readline().decode('utf-8').rstrip()
            if line:
                self.data.append(float(line))
        filtered_data = signal_processing.butter_bandpass_filter(self.data, 1, 50, 200)
        threshold = self.slider.value() / 100.0 * max(filtered_data)
        color_values = [int((x / threshold) * 255) for x in filtered_data]
        self.data_label.setStyleSheet("background-color: rgb({}, 0, 0);".format(color_values[-1]))
        
    def slider_change(self, value):
        self.slider_label.setText("Threshold: {}".format(value))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    eeg_visualizer = EEGVisualizer()
    eeg_visualizer.show()
    sys.exit(app.exec_())