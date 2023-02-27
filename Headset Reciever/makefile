#
#
# Author: Charles Bostwick
# Website: www.AwaywithCharles.com
# GitHub: https://github.com/AwaywithCharles
# License: MIT
#
#

# import necessary modules
import eeg_data_analysis
import eeg_ui

# create an instance of the data analysis object
analysis = eeg_data_analysis.EEGDataAnalysis()

# create an instance of the UI object
ui = eeg_ui.EEGUI()

# launch the UI
ui.launch()

# get the data from the UI
data = ui.get_data()

# analyze the data
results = analysis.analyze(data)

# display the results in the UI
ui.show_results(results)