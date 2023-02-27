"""
Author: Charles Bostwick
Website: www.AwaywithCharles.com
GitHub: https://github.com/AwaywithCharles
License: MIT
"""

from scipy import signal

# Define the bandpass filter parameters
fs = 1000  # Sample rate in Hz
lowcut = 1  # Low cutoff frequency in Hz
highcut = 50  # High cutoff frequency in Hz
order = 5  # Filter order

# Define the filter coefficients
nyquist = 0.5 * fs
low = lowcut / nyquist
high = highcut / nyquist
b, a = signal.butter(order, [low, high], btype='band')

# Apply the bandpass filter to the EEG signal
filtered_eeg = signal.filtfilt(b, a, eeg_signal)
