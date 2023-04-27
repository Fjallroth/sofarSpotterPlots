import tkinter as tk
from tkinter import filedialog, IntVar
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from windrose import WindroseAxes
import numpy as np

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Wave Data Analyzer")
        self.input_file = tk.StringVar()


def read_data(filename):
    df = pd.read_csv(filename, usecols=['Epoch Time', 'Significant Wave Height (m)', 'Mean Period (s)', 'Peak Period (s)', 'Mean Direction (deg)', 'Peak Direction (deg)', 'Mean Directional Spread (deg)', 'Peak Directional Spread (deg)'], parse_dates=True)
    df['date'] = pd.to_datetime(df['Epoch Time'], unit='s')
    df.set_index('date', inplace=True)
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
    sigWave = sns.lineplot(x='date', y='Significant Wave Height (m)', data=df, linewidth=0.8) 
    sigWave.set_xlabel("Date", fontsize=20)
    sigWave.set_ylabel("Significant Wave Height (m)", fontsize=20)
    sigWave.set_title("Timeseries of Significant Wave Height", fontsize=20, fontweight='bold')
    fig_sigWave = sigWave.get_figure()

    return fig_sigWave

def create_peak_period_plot(df):
    plt.figure(figsize=(15, 8))
    peakP = sns.lineplot(x='date', y='Peak Period (s)', data=df, linewidth=0.5) 
    peakP.set_xlabel("Date", fontsize=20)
    peakP.set_ylabel("Peak Period (s)", fontsize=20)
    peakP.set_title("Timeseries of Peak Period", fontsize=20, fontweight='bold')
    fig_peakP = peakP.get_figure()

    return fig_peakP

def create_mean_period_plot(df):
    plt.figure(figsize=(15, 8))
    meanP = sns.lineplot(x='date', y='Mean Period (s)', data=df, linewidth=0.5)
    meanP.set_xlabel("Date", fontsize=20)
    meanP.set_ylabel("Mean Period (s)", fontsize=20)
    meanP.set_title("Timeseries of Mean Period", fontsize=20, fontweight='bold')
    fig_meanP = meanP.get_figure()

    return fig_meanP

def create_hs_peak_scatter_plot(df):
    plt.figure(figsize=(10, 6))
    hs_peak_scatter = sns.scatterplot(x='Peak Period (s)', y='Significant Wave Height (m)', data=df)
    hs_peak_scatter.set_xlabel("Peak Period (s)", fontsize=14)
    hs_peak_scatter.set_ylabel("Significant Wave Height (m)", fontsize=14)
    hs_peak_scatter.set_title("Scatterplot of Significant Wave Height vs Peak Period", fontsize=16, fontweight='bold')
    fig_hs_peak_scatter = hs_peak_scatter.get_figure()

    return fig_hs_peak_scatter

def create_hs_mean_scatter_plot(df):
    plt.figure(figsize=(10, 6))
    hs_mean_scatter = sns.scatterplot(x='Mean Period (s)', y='Significant Wave Height (m)', data=df)
    hs_mean_scatter.set_xlabel("Mean Period (s)", fontsize=14)
    hs_mean_scatter.set_ylabel("Significant Wave Height (m)", fontsize=14)
    hs_mean_scatter.set_title("Scatterplot of Significant Wave Height vs Mean Period", fontsize=16, fontweight='bold')
    fig_hs_mean_scatter = hs_mean_scatter.get_figure()

    return fig_hs_mean_scatter

def create_hs_histogram_plot(df):
    plt.figure(figsize=(10, 6))
    hs_histogram = sns.histplot(df['Significant Wave Height (m)'], kde=False, bins=20)
    hs_histogram.set_xlabel("Significant Wave Height (m)", fontsize=14)
    hs_histogram.set_ylabel("Frequency", fontsize=14)
    hs_histogram.set_title("Histogram of Significant Wave Height", fontsize=16, fontweight='bold')
    fig_hs_histogram = hs_histogram.get_figure()

    return fig_hs_histogram

def create_peak_period_histogram_plot(df):
    plt.figure(figsize=(10, 6))
    peakP_histogram = sns.histplot(df['Peak Period (s)'], kde=False, bins=20)
    peakP_histogram.set_xlabel("Peak Period (s)", fontsize=14)
    peakP_histogram.set_ylabel("Frequency", fontsize=14)
    peakP_histogram.set_title("Histogram of Peak Period", fontsize=16, fontweight='bold')
    fig_peakP_histogram = peakP_histogram.get_figure()

    return fig_peakP_histogram

def create_mean_period_histogram_plot(df):
    plt.figure(figsize=(10, 6))
    meanP_histogram = sns.histplot(df['Mean Period (s)'], kde=False, bins=20)
    meanP_histogram.set_xlabel("Mean Period (s)", fontsize=14)
    meanP_histogram.set_ylabel("Frequency", fontsize=14)
    meanP_histogram.set_title("Histogram of Mean Period", fontsize=16, fontweight='bold')
    fig_meanP_histogram = meanP_histogram.get_figure()

    return fig_meanP_histogram

def create_wave_rose_plot(df):
    ax = WindroseAxes.from_ax()
    ax.bar(df['Mean Direction (deg)'], df['Significant Wave Height (m)'], normed=True, opening=0.8, edgecolor='white')
    ax.set_legend(title="Significant Wave Height (m)", loc='upper left', bbox_to_anchor=(1, 1))
    ax.set_title("Wave Rose", fontsize=16, fontweight='bold')
    fig_wave_rose = ax.get_figure()

    return fig_wave_rose

def save_plots(plots, filenames):
    for plot, filename in zip(plots, filenames):
        plot.savefig(filename)

def browse_file(app):
    filename = filedialog.askopenfilename()
    app.input_file.set(filename)

def main(app):
    set_plot_style()

    filename = app.input_file.get()
    df = read_data(filename)
    plots = create_selected_plots(df)
    filenames = [
        'sigWave.png', 'peakP.png', 'meanP.png', 'hs_peak_scatter.png', 'hs_mean_scatter.png',
        'hs_histogram.png', 'peakP_histogram.png', 'meanP_histogram.png', 'wave_rose.png'
    ]
    save_plots(plots, filenames)

    plt.show()

    print("\033[1;34mThis script has been successfully completed. You will find the graphics in your working directory as well as a txt file with the 10 highest significant wave heights recorded.")

def create_ui(app):
    root = app.root
    root.title("Wave Data Analyzer")
    app.sig_wave_checkbox_var = tk.IntVar()
    app.peak_period_checkbox_var = tk.IntVar()
    app.mean_period_checkbox_var = tk.IntVar()
    app.sig_wave_vs_peak_period_checkbox_var = tk.IntVar()
    app.sig_wave_vs_mean_period_checkbox_var = tk.IntVar()
    app.sig_wave_hist_checkbox_var = tk.IntVar()
    app.peak_period_hist_checkbox_var = tk.IntVar()
    app.mean_period_hist_checkbox_var = tk.IntVar()
    app.wave_rose_checkbox_var = tk.IntVar()

    input_label = tk.Label(app.root, text="Input File:")
    input_label.grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky="E")

    input_entry = tk.Entry(app.root, textvariable=app.input_file, width=60)
    input_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="W")

    browse_button = tk.Button(app.root, text="Browse", command=lambda: browse_file(app))
    browse_button.grid(row=0, column=2, padx=(0, 10), pady=(10, 0), sticky="W")


    # Create checkboxes to select plots
    tk.Label(root, text="Select Plots:").grid(row=1, column=0, sticky="w")
    sig_wave_checkbox = tk.Checkbutton(root, text="Timeseries of Significant Wave Height", variable=app.sig_wave_checkbox_var)
    sig_wave_checkbox.grid(row=1, column=1, sticky="w")
    peak_period_checkbox = tk.Checkbutton(root, text="Timeseries of Peak Period", variable=app.peak_period_checkbox_var)
    peak_period_checkbox.grid(row=2, column=1, sticky="w")
    mean_period_checkbox = tk.Checkbutton(root, text="Timeseries of Mean Period", variable=app.mean_period_checkbox_var)
    mean_period_checkbox.grid(row=3, column=1, sticky="w")
    sig_wave_vs_peak_period_checkbox = tk.Checkbutton(root, text="Scatterplot of Significant Wave Height vs Peak Period", variable=app.sig_wave_vs_peak_period_checkbox_var)
    sig_wave_vs_peak_period_checkbox.grid(row=4, column=1, sticky="w")
    sig_wave_vs_mean_period_checkbox = tk.Checkbutton(root, text="Scatterplot of Significant Wave Height vs Mean Period", variable=app.sig_wave_vs_mean_period_checkbox_var)
    sig_wave_vs_mean_period_checkbox.grid(row=5, column=1, sticky="w")
    sig_wave_hist_checkbox = tk.Checkbutton(root, text="Histogram of Significant Wave Height", variable=app.sig_wave_hist_checkbox_var)
    sig_wave_hist_checkbox.grid(row=6, column=1, sticky="w")
    peak_period_hist_checkbox = tk.Checkbutton(root, text="Histogram of Peak Period", variable=app.peak_period_hist_checkbox_var)
    peak_period_hist_checkbox.grid(row=7, column=1, sticky="w")
    mean_period_hist_checkbox = tk.Checkbutton(root, text="Histogram of Mean Period", variable=app.mean_period_hist_checkbox_var)
    mean_period_hist_checkbox.grid(row=8, column=1, sticky="w")
    wave_rose_checkbox = tk.Checkbutton(root, text="Wave Rose", variable=app.wave_rose_checkbox_var)
    wave_rose_checkbox.grid(row=9, column=1, sticky="w")

    analyze_button = tk.Button(root, text="Analyze", command=lambda: main(app))
    analyze_button.grid(row=10, column=1)

    root.mainloop()

def create_selected_plots(df):
    plots = []

    if app.sig_wave_checkbox_var.get():
        plots.append(create_sig_wave_plot(df))
    if app.peak_period_checkbox_var.get():
        plots.append(create_peak_period_plot(df))
    if app.mean_period_checkbox_var.get():
        plots.append(create_mean_period_plot(df))
    if app.sig_wave_vs_peak_period_checkbox_var.get():
        plots.append(create_hs_peak_scatter_plot(df))  # Updated function call
    if app.sig_wave_vs_mean_period_checkbox_var.get():
        plots.append(create_hs_mean_scatter_plot(df))  # Updated function call
    if app.sig_wave_hist_checkbox_var.get():
        plots.append(create_hs_histogram_plot(df))
    if app.peak_period_hist_checkbox_var.get():
        plots.append(create_peak_period_histogram_plot(df))
    if app.mean_period_hist_checkbox_var.get():
        plots.append(create_mean_period_histogram_plot(df))
    if app.wave_rose_checkbox_var.get():
        plots.append(create_wave_rose_plot(df))

    return plots

if __name__ == "__main__":
    app = App()
    create_ui(app)
    app.root.mainloop()

def save_plots(plots, filenames):
    for plot, filename in zip(plots, filenames):
        plot.savefig(filename)


if __name__ == "__main__":
    main()
