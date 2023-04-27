# SoFar Sotter Wave Data Visualization
This Python script reads wave data from the SoFar Sotter wave measurement device and creates various plots based on the input data. The plots help to visualize and analyze the significant wave heights, mean and peak periods, and other parameters.

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
Save this script in the same folder as your SoFar Sotter wave data file (CSV format). Make sure there are no other CSV files in the folder.
Run the script using Python 3: python3 sofar_sotter_wave_analysis.py
When prompted, enter the name of the wave data file (including its extension).
The script will generate plots and save them as PNG files in the same folder as the script. It will also create a text file (Wave_analysis.txt) with the 10 highest significant wave heights recorded.
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

# Customization
You can customize the script by adding more plots or modifying existing plots. To add more plots, create new functions following the pattern of existing plot functions (e.g., create_sig_wave_plot, create_peak_period_plot, and create_mean_period_plot). Update the create_plots function to include any new plots you create, and add the corresponding filenames in the filenames list.
