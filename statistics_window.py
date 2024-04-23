import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
# To use graph from matplot lib in tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json
import os
def load_data_from_file_for_stats():
    if(not os.path.exists('statistics_data.json') or os.path.getsize('statistics_data.json') == 0):
        print("file is empty or the file doesn't exist")
        return
    with open('statistics_data.json','r') as readfile:
        dict_data = json.load(readfile)
    return dict_data

def stat_window():
    stat_window =tk.Toplevel(background = "#180227")
    stat_window.title("STATISTICS")
    stat_window.minsize(width = 900, height = 600)

    collective_dict_data = load_data_from_file_for_stats()
    print(collective_dict_data)
    # grid configuaration
    for i in range(4):  # Assuming there are 4 rows and 4 columns
        stat_window.rowconfigure(i, weight=1)
        stat_window.columnconfigure(i, weight=1)

    # Line Graph for Wpm vs accuracy
    figure_wpm_vs_accuracy = plt.figure(figsize=(5,4),dpi=100,facecolor="#180227",edgecolor="white",)
    figure_plot_wpm_vs_accuracy = figure_wpm_vs_accuracy.add_subplot(1,1,1)
    figure_plot_wpm_vs_accuracy.set_ylabel("Words Per Minute",color = "white")
    figure_plot_wpm_vs_accuracy.set_xlabel("Accuracy",color = "white")
    # To group the data
    # panda
    dataframe = pd.DataFrame(collective_dict_data)
    dataframe= dataframe[["wpm", "accuracy"]].groupby("accuracy").first()
    line_wpm_vs_accuracy = dataframe.plot(kind ='line', legend = True, ax = figure_plot_wpm_vs_accuracy,
                   color = 'white', marker = 'o', fontsize = 10)
    figure_plot_wpm_vs_accuracy.set_facecolor('#180227')


    for text in line_wpm_vs_accuracy.get_xticklabels() + line_wpm_vs_accuracy.get_yticklabels():
        text.set_color('white')

    for label in (figure_plot_wpm_vs_accuracy.get_xticklabels() + figure_plot_wpm_vs_accuracy.get_yticklabels()):
        label.set_color('white')
    # Set the color for the borders of the graph
    for spine in figure_plot_wpm_vs_accuracy.spines.values():
        spine.set_edgecolor('white')
    figure_plot_wpm_vs_accuracy.set_title('Words Per Minute Vs. Accuracy',color = "white")

    line_graph_wpm_vs_accuracy = FigureCanvasTkAgg(figure_wpm_vs_accuracy,stat_window)
    line_graph_wpm_vs_accuracy.get_tk_widget().grid(row = 0,column = 0,rowspan = 2, sticky='nsew')

    # Line Graph for Wpm vs Errors
    figure_wpm_vs_errors = plt.figure(figsize=(5,4),dpi=100,facecolor="#180227",edgecolor="white",)
    figure_plot_wpm_vs_errors = figure_wpm_vs_errors.add_subplot(1,1,1)
    figure_plot_wpm_vs_errors.set_ylabel("Words Per Minute",color = "white")
    figure_plot_wpm_vs_errors.set_xlabel("Accuracy",color = "white")
    # To group the data
    # panda
    dataframe_errors = pd.DataFrame(collective_dict_data)
    print(collective_dict_data)
    dataframe_errors= dataframe_errors[["wpm", "errors"]].groupby("errors").first()
    line_wpm_vs_errors = dataframe_errors.plot(kind ='line', legend = True, ax = figure_plot_wpm_vs_errors,
                   color = 'white', marker = 'o', fontsize = 10)
    figure_plot_wpm_vs_errors.set_facecolor('#180227')


    for text in line_wpm_vs_errors.get_xticklabels() + line_wpm_vs_errors.get_yticklabels():
        text.set_color('white')

    for label in (figure_plot_wpm_vs_errors.get_xticklabels() + figure_plot_wpm_vs_errors.get_yticklabels()):
        label.set_color('white')
    # Set the color for the borders of the graph
    for spine in figure_plot_wpm_vs_errors.spines.values():
        spine.set_edgecolor('white')
    figure_plot_wpm_vs_errors.set_title('Words Per Minute Vs. Errors',color = "white")

    line_graph_wpm_vs_errors = FigureCanvasTkAgg(figure_wpm_vs_errors,stat_window)
    line_graph_wpm_vs_errors.get_tk_widget().grid(row = 0,column = 2,rowspan = 2, sticky='nsew')

    stat_label = ctk.CTkLabel(master=stat_window,
                              font=("Helvetica", 20),
                              fg_color="#180227",
                              text="No. of plays = {}".format(len(collective_dict_data["wpm"])))
    stat_label.grid(row = 2,column = 1,rowspan = 2, sticky='nsew')