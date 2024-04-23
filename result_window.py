import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
# To use graph from matplot lib in tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json
import os


def get_desired_data(time_var_list):

    data_dict = {
        "time":time_var_list,
        "char_count":[]
    }
    for i in range(len(time_var_list)):
        data_dict["char_count"].append(i+1)

    print(data_dict)
    return data_dict


def store_result_to_file_for_history(words_per_minute,typing_accuracy,typing_errors):
    collective_data_dict = {"wpm":[],
                            "accuracy":[],
                            "errors":[]}
    # If the file is empty or doesn't exists
    if (not os.path.exists('statistics_data.json') or os.path.getsize('statistics_data.json') == 0): 
        collective_data_dict = {"wpm":[words_per_minute],
                                "accuracy":[typing_accuracy],
                                "errors":[typing_errors]}
        
        json_object = json.dumps(collective_data_dict, indent=4)
        with open('statistics_data.json','w') as file:
            file.write(json_object)
 
    else:
        with open('statistics_data.json','r') as openfile:
            collective_data_dict:dict = json.load(openfile)
        collective_data_dict["wpm"].append(words_per_minute)
        collective_data_dict["accuracy"].append(typing_accuracy)
        collective_data_dict["errors"].append(typing_errors)
        json_object = json.dumps(collective_data_dict,indent=4)
        with open('statistics_data.json','w') as writefile:
            writefile.write(json_object)


def resultant_window(char_count:int,red_char_count:int,green_char_count:int,time_var:tk.StringVar,time_var_list:list):
    #For typing accuracy
    print("char count:",char_count)
    print(" red char count:",red_char_count)
    print("green char count:",green_char_count)

    if(char_count==0):
        print("divide by zero eroor")
        typing_accuracy = "0"
    else:
        typing_accuracy = str(round((green_char_count*100)/char_count,3))
    #For typing errors
    typing_errors = str(red_char_count)
    
    # number of words typed == char_count/5 
    # wpm = words achieved every one minute
    print("Char count",char_count)
    time_var_value = float(time_var.get())
    print("time is:",time_var_value)
    if time_var_value == 0:
        print("divide by zero error")
        words_per_minute = 0  # Handle division by zero case
    else:
        words_per_minute = (char_count * 60) / (5 * time_var_value)

    store_result_to_file_for_history(words_per_minute = float(words_per_minute),
                                     typing_accuracy = float(typing_accuracy),
                                     typing_errors = int(typing_errors))

    #Line Graph plot
    data_dict = get_desired_data(time_var_list=time_var_list)
    dataframe = pd.DataFrame(data_dict)

    #ui
    res_window = tk.Toplevel(background="#180227")
    res_window.title("TYPEWIZ")
    res_window.minsize(width=700, height=400)
    
    # matplotlib
    figure = plt.figure(figsize=(5,4),dpi=100,facecolor="#180227",edgecolor="white",)
    figure_plot = figure.add_subplot(1,1,1)
    figure_plot.set_ylabel("Character Count",color = "white")
    figure_plot.set_xlabel("Time",color = "white")
    # To group the data
    # panda
    dataframe= dataframe[['time', 'char_count']].groupby('time').first()
    line = dataframe.plot(kind ='line', legend = True, ax = figure_plot,
                   color = 'white', marker = '', fontsize = 10)
    figure_plot.set_facecolor('#180227')


    for text in line.get_xticklabels() + line.get_yticklabels():
        text.set_color('white')

    for label in (figure_plot.get_xticklabels() + figure_plot.get_yticklabels()):
        label.set_color('white')
    # Set the color for the borders of the graph
    for spine in figure_plot.spines.values():
        spine.set_edgecolor('white')
    figure_plot.set_title('Character Count Vs. Time',color = "white")

    # tkinter

    for i in range(3):  # Assuming there are 3 rows and 3 columns
        res_window.rowconfigure(i, weight=1)
        res_window.columnconfigure(i, weight=1)

    line_graph = FigureCanvasTkAgg(figure,res_window)
    line_graph.get_tk_widget().grid(row=0, column=0, rowspan=3, sticky="nsew")
    
    wpm_res_label = ctk.CTkLabel(master=res_window,text = str(round(words_per_minute,3)), font=("Helvetica", 40),fg_color="#180227")
    wpm_res_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    wpm_label = ctk.CTkLabel(master=res_window,text = "WPM",font=("Helvetica", 20),fg_color="#180227")
    wpm_label.grid(row=0, column=2, padx=10, pady=10, sticky="w")

    accuracy_res_label = ctk.CTkLabel(master=res_window,text = typing_accuracy+"%", font=("Helvetica", 40),fg_color="#180227")
    accuracy_res_label.grid(row=1, column=2, padx=10, pady=10, sticky="w")
    accuracy_label = ctk.CTkLabel(master=res_window,text = "Accuracy",font=("Helvetica", 25),fg_color="#180227")
    accuracy_label.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    errors_res_label = ctk.CTkLabel(master=res_window,text = typing_errors, font=("Helvetica", 40),fg_color="#180227")
    errors_res_label.grid(row=2, column=2, padx=10, pady=10, sticky="w")
    errors_label = ctk.CTkLabel(master=res_window,text = "Errors:",font=("Helvetica", 25),fg_color="#180227")
    errors_label.grid(row=2, column=1, padx=10, pady=10, sticky="w")
