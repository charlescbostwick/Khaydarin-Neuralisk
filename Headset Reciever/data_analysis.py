"""
Author: Charles Bostwick
Website: www.AwaywithCharles.com
GitHub: https://github.com/AwaywithCharles
License: MIT
"""

# Define the STFT parameters
nperseg = 256  # Number of samples per segment
noverlap = nperseg // 2  # Number of overlapping samples
fs = 1000  # Sample rate in Hz

# Compute the STFT of the filtered EEG signal
f, t, Zxx = signal.stft(filtered_eeg, fs=fs, nperseg=nperseg, noverlap=noverlap)

# Plot the STFT as a heatmap
import matplotlib.pyplot as plt
plt.pcolormesh(t, f, np.abs(Zxx), vmin=0, vmax=np.abs(Zxx).max(), shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
