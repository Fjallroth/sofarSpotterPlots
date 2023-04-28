# Sofar Spotter Wave Data Visualization (Now with AI!)
This Python script reads wave data from the Sofar Spotter wave measurement device and creates various plots based on the input data. The plots help to visualize and analyze the significant wave heights, mean and peak periods, and other parameters.
This is Python application that provides users with an easy-to-use graphical interface for importing wave dataset files in CSV format, selecting desired plots, and generating an AI-generated report on the dataset. The generated plots are saved as PNG files, and the report is saved as a TXT file in the working directory.
This is for the Sofar Ocean Spotter and uses the data pulled from the dashboard (csv file is expected, if your dashboard provides a different file format it should be sufficient to change the file extension to .csv) [more information on the spotter can be found here](https://www.sofarocean.com/products/spotter)

The standard script will generate plots, the AI script also includes an AI generated report which analyses the CSV file and describes the wave characteristics. This version also requires the user to enter their OpenAI API key. I have used gpt-3.5-turbo here as I do not currently have access to GPT-4. 

This script is run 100% on your machine so there is no way that your API key will be visible to anyone other than OpenAI. Please ensure you remove your API key before sharing the code!

# Prerequisites
To run this script, you will need the following Python libraries:
-pandas
-numpy
-seaborn
-matplotlib
-tkinter
-windrose
-openai (this is only required when using AI version)


# Usage
Run the script: python sofarSpotterGraphs.py (or sofarSpotterGraphsAIReport.py if using AI script)
Browse for the input CSV file containing wave dataset columns (Epoch Time, Significant Wave Height (m), Mean Period (s), Peak Period (s), Mean Direction (deg), Peak Direction (deg), Mean Directional Spread (deg), and Peak Directional Spread (deg)).
Select desired plots from the list of available checkboxes.
Click the "Analyze" button to generate the selected plots and an AI-generated report on the dataset.
The generated plots will be saved as PNG files in the working directory, and the AI-generated report will be saved as a TXT file.

# Functions
- read_data(filename): Reads the input CSV file and returns a pandas DataFrame.
- set_plot_style(): Sets the plot style for seaborn.
- create_plots(df): Generates a list of plots based on the input DataFrame.
- create_sig_wave_plot(df): Creates a timeseries plot of significant wave height.
- create_peak_period_plot(df): Creates a timeseries plot of peak period.
- create_mean_period_plot(df): Creates a timeseries plot of mean period.
- create_hs_peak_scatter_plot(df): Creates a scatterplot of significant wave height vs peak period.
- create_hs_mean_scatter_plot(df): Creates a scatterplot of significant wave height vs mean period.
- create_hs_histogram_plot(df): Creates a histogram of significant wave height.
- create_peak_period_histogram_plot(df): Creates a histogram of peak period.
- create_mean_period_histogram_plot(df): Creates a histogram of mean period.
- create_wave_rose_plot(df): Creates a wave rose plot.
- save_plots(plots, filenames): Saves the generated plots as PNG files.
- browse_file(app): Opens a file dialog to select the input CSV file.
- generate_ai_report(df): Generates an AI report using the GPT-3.5-turbo model.
- save_report(report, filename): Saves the AI-generated report as a TXT file.
- main(app): Main function that executes the entire process.
- create_ui(app): Creates the user interface with tkinter.
- create_selected_plots(df): Creates the selected plots based on the user input.
- save_plots(plots, filenames): Saves the generated plots as PNG files.

# Notes

Make sure to install the required dependencies before running the script.
The input CSV file should have the appropriate column names for the script to work properly.
The AI-generated report may take some time to generate, depending on the dataset size and complexity. 
It can be that your CSV file is too large, I have removed all the unused coloumns from the prompt to reduce tokens as far as possible but the limitation is the number of tokens your chosen model can process.

