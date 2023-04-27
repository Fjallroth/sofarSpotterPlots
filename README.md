# Sofar Spotter Wave Data Visualization
This Python script reads wave data from the Sofar Spotter wave measurement device and creates various plots based on the input data. The plots help to visualize and analyze the significant wave heights, mean and peak periods, and other parameters.

# Prerequisites
To run this script, you will need the following Python libraries:
- pandas
- matplotlib
- seaborn
- windrose
- numpy
You can install the libraries using the following command:

pip install pandas matplotlib seaborn windrose numpy

# Usage
Run the script using Python 3: python3 sofar_sotter_wave_analysis.py
When prompted, select the wave data file (including its extension).
The script will generate plots and save them as PNG files in the same folder as the script.
Open the generated PNG files to view the plots, or use the text file for further analysis.

# Plots
The script generates the following plots:

- Timeseries of Significant Wave Height
- Timeseries of Peak Period
- Timeseries of Mean Period
- Scatterplot of Significant Wave Height vs Peak Period
- Scatterplot of Significant Wave Height vs Mean Period
- Histogram of Significant Wave Height
- Histogram of Peak Period
- Histogram of Mean Period
- Wave Rose

