import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from windrose import WindroseAxes
import numpy as np

def read_data(filename):
    df = pd.read_csv(filename, usecols= ['# year ',' month ',' day',' hour ','min',' sec',' milisec ', ' Significant Wave Height',' Mean Period', ' Peak Period',' Mean Direction', ' Peak Direction',   ' Mean Spreading', ' Peak Spreading'], parse_dates={'date':['# year ',' month ',' day',' hour ','min',' sec']})

    df.rename(columns = {'# year ':'year', ' month ':'month',' day':'day',' hour ':'hour',' sec':'sec',' milisec ':'milisec',' Significant Wave Height':'Significant Wave Height', ' Mean Period':'Mean Period',' Peak Period':'Peak Period',' Mean Direction':'Mean Direction',' Peak Direction':'Peak Direction',' Mean Spreading':'Mean Spreading',' Peak Spreading':'Peak Spreading'}, inplace = True)
    df.columns = df.columns.str.replace(' ','_')

    df['date'] = pd.to_datetime(df['date'],format = '%Y %m %d %H %M %S')
    df.index = df['date']
    del df['date']

    df = df[~df.index.duplicated()]

    return df

def set_plot_style():
    sns.set_theme(style="darkgrid", font='sans-serif')

def create_plots(df):
    fig_sigWave = create_sig_wave_plot(df)
    fig_peakP = create_peak_period_plot(df)
    fig_meanP = create_mean_period_plot(df)
    # Add more plots as needed

    return [fig_sigWave, fig_peakP, fig_meanP]

def create_sig_wave_plot(df):
    plt.figure(figsize=(15, 8))
    sigWave = sns.lineplot(x='date', y='Significant_Wave_Height', data=df, linewidth=0.8)
    sigWave.set_xlabel("Date", fontsize=20)
    sigWave.set_ylabel("Significant Wave Height (m)", fontsize=20)
    sigWave.set_title("Timeseries of Significant Wave Height", fontsize=20, fontweight='bold')
    fig_sigWave = sigWave.get_figure()

    return fig_sigWave

def create_peak_period_plot(df):
    plt.figure(figsize=(15, 8))
    peakP = sns.lineplot(x='date', y='Peak_Period', data=df, linewidth=0.5)
    peakP.set_xlabel("Date", fontsize=20)
    peakP.set_ylabel("Peak Period (s)", fontsize=20)
    peakP.set_title("Timeseries of Peak Period", fontsize=20, fontweight='bold')
    fig_peakP = peakP.get_figure()

    return fig_peakP

def create_mean_period_plot(df):
    plt.figure(figsize=(15, 8))
    meanP = sns.lineplot(x='date', y='Mean_Period', data=df, linewidth=0.5)
    meanP.set_xlabel("Date", fontsize=20)
    meanP.set_ylabel("Mean Period (s)", fontsize=20)
    meanP.set_title("Timeseries of Mean Period", fontsize=20, fontweight='bold')
    fig_meanP = meanP.get_figure()

    return fig_meanP

def create_hs_peak_scatter_plot(df):
    plt.figure(figsize=(10, 6))
    hs_peak_scatter = sns.scatterplot(x='Peak_Period', y='Significant_Wave_Height', data=df)
    hs_peak_scatter.set_xlabel("Peak Period (s)", fontsize=14)
    hs_peak_scatter.set_ylabel("Significant Wave Height (m)", fontsize=14)
    hs_peak_scatter.set_title("Scatterplot of Significant Wave Height vs Peak Period", fontsize=16, fontweight='bold')
    fig_hs_peak_scatter = hs_peak_scatter.get_figure()

    return fig_hs_peak_scatter

def create_hs_mean_scatter_plot(df):
    plt.figure(figsize=(10, 6))
    hs_mean_scatter = sns.scatterplot(x='Mean_Period', y='Significant_Wave_Height', data=df)
    hs_mean_scatter.set_xlabel("Mean Period (s)", fontsize=14)
    hs_mean_scatter.set_ylabel("Significant Wave Height (m)", fontsize=14)
    hs_mean_scatter.set_title("Scatterplot of Significant Wave Height vs Mean Period", fontsize=16, fontweight='bold')
    fig_hs_mean_scatter = hs_mean_scatter.get_figure()

    return fig_hs_mean_scatter

def create_hs_histogram_plot(df):
    plt.figure(figsize=(10, 6))
    hs_histogram = sns.histplot(df['Significant_Wave_Height'], kde=False, bins=20)
    hs_histogram.set_xlabel("Significant Wave Height (m)", fontsize=14)
    hs_histogram.set_ylabel("Frequency", fontsize=14)
    hs_histogram.set_title("Histogram of Significant Wave Height", fontsize=16, fontweight='bold')
    fig_hs_histogram = hs_histogram.get_figure()

    return fig_hs_histogram

def create_peak_period_histogram_plot(df):
    plt.figure(figsize=(10, 6))
    peakP_histogram = sns.histplot(df['Peak_Period'], kde=False, bins=20)
    peakP_histogram.set_xlabel("Peak Period (s)", fontsize=14)
    peakP_histogram.set_ylabel("Frequency", fontsize=14)
    peakP_histogram.set_title("Histogram of Peak Period", fontsize=16, fontweight='bold')
    fig_peakP_histogram = peakP_histogram.get_figure()

    return fig_peakP_histogram

def create_mean_period_histogram_plot(df):
    plt.figure(figsize=(10, 6))
    meanP_histogram = sns.histplot(df['Mean_Period'], kde=False, bins=20)
    meanP_histogram.set_xlabel("Mean Period (s)", fontsize=14)
    meanP_histogram.set_ylabel("Frequency", fontsize=14)
    meanP_histogram.set_title("Histogram of Mean Period", fontsize=16, fontweight='bold')
    fig_meanP_histogram = meanP_histogram.get_figure()

    return fig_meanP_histogram

def create_wave_rose_plot(df):
    ax = WindroseAxes.from_ax()
    ax.bar(df['Mean_Direction'], df['Significant_Wave_Height'], normed=True, opening=0.8, edgecolor='white')
    ax.set_legend(title="Significant Wave Height (m)", loc='upper left', bbox_to_anchor=(1, 1))
    ax.set_title("Wave Rose", fontsize=16, fontweight='bold')
    fig_wave_rose = ax.get_figure()

    return fig_wave_rose

def save_plots(plots, filenames):
    for plot, filename in zip(plots, filenames):
        plot.savefig(filename)

def main():
    set_plot_style()

    filename = input("\033[1;32mEnter the name of the file containing bulk parameters data, including its extension: ")
    df = read_data(filename)
    plots = create_plots(df)
    filenames = [
        'sigWave.png', 'peakP.png', 'meanP.png', 'hs_peak_scatter.png', 'hs_mean_scatter.png',
        'hs_histogram.png', 'peakP_histogram.png', 'meanP_histogram.png', 'wave_rose.png'
    ]
    save_plots(plots, filenames)

    plt.show()

    print("\033[1;34mThis script has been successfully completed. You will find the graphics in your working directory as well as a txt file with the 10 highest significant wave heights recorded.")

if __name__ == "__main__":
    main()
def save_plots(plots, filenames):
    for plot, filename in zip(plots, filenames):
        plot.savefig(filename)

def main():
    set_plot_style()

    filename = input("\033[1;32mEnter the name of the file containing bulk parameters data, including its extension: ")
    df = read_data(filename)
    plots = create_plots(df)
    filenames = ['sigWave.png', 'peakP.png', 'meanP.png']
    save_plots(plots, filenames)

    # You can also add the other plots as needed in a similar fashion
    # Don't forget to update the `create_plots` function and add the corresponding filenames

    plt.show()

    print("\033[1;34mThis script has been successfully completed. You will find the graphics in your working directory as well as a txt file with the 10 highest significant wave heights recorded.")

if __name__ == "__main__":
    main()