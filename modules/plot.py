import customtkinter
import psutil
import tkinter as tk
import threading
import socket
import time
import wmi
from psutil import net_io_counters
import subprocess
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.dates as mdates
from datetime import datetime, timedelta
RANDOM_STATE = 42  # used to help randomly select the data points
low_memory = False
LARGE_FONT = ("Verdana", 12)
style.use("ggplot")

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")
        self.resizable(False, False) 
        # add widgets onto the frame...
        self.live_plot_frame = customtkinter.CTkFrame(self)
        self.live_plot_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # Create labels frame
        self.labels_frame = customtkinter.CTkFrame(self.live_plot_frame)
        self.labels_frame.grid(row=0, column=0, sticky="nsew")

        # Create plot frame
        self.plot_frame = customtkinter.CTkFrame(self.live_plot_frame)
        self.plot_frame.grid(row=0, column=1, sticky="nsew")

        # Labels
        self.live_plot_label = customtkinter.CTkLabel(self.labels_frame, text="Live")
        self.live_plot_label.pack(pady=10, padx=10)

        # Matplotlib figure
        self.figure = Figure(figsize=(5, 5), dpi=100)
        self.ax = self.figure.add_subplot(111)
        # Format the x-axis to show the time
        myFmt = mdates.DateFormatter("%H:%M:%S")
        self.ax.xaxis.set_major_formatter(myFmt)
        # Set dark mode style
        self.figure.patch.set_facecolor('black')
        self.ax.set_facecolor('black')
        self.ax.spines['bottom'].set_color('white')
        self.ax.spines['top'].set_color('white')
        self.ax.spines['left'].set_color('white')
        self.ax.spines['right'].set_color('white')
        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')
        self.ax.yaxis.label.set_color('white')
        self.ax.xaxis.label.set_color('white')
        self.ax.title.set_color('white')

        # Initial x and y data
        dateTimeObj = datetime.now() + timedelta(seconds=-360)
        self.x_data = [dateTimeObj + timedelta(seconds=i) for i in range(360)]
        self.y_data = [0 for i in range(360)]
        # Create the plot
        self.plot = self.ax.plot(self.x_data, self.y_data, label='CPU', color='lime')[0]
        self.ax.set_ylim(0, 100)
        self.ax.set_xlim(self.x_data[0], self.x_data[-1])
        
        # Add legend
        self.ax.legend()

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.plot_frame)

        self.canvas.get_tk_widget().pack(side='top', fill=tk.BOTH, expand=True)
        self.animate()

    def animate(self):
        # append new data point to the x and y data
        self.x_data.append(datetime.now())
        self.y_data.append(psutil.cpu_percent())
        # remove oldest data point
        self.x_data = self.x_data[1:]
        self.y_data = self.y_data[1:]
        # update plot data
        self.plot.set_xdata(self.x_data)
        self.plot.set_ydata(self.y_data)
        self.ax.set_xlim(self.x_data[0], self.x_data[-1])
        self.canvas.draw_idle()  # redraw plot
        self.after(1000, self.animate)  # repeat after 1s
