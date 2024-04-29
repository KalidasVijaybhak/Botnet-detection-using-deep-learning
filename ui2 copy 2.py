import multiprocessing
import os
import tkinter
from tkinter import messagebox
import customtkinter
from csv_view import CsvWindow, CsvWindowThread
from default_test import DefaultViewFrame
from modules.default_view import DefaultView
from tkinter import filedialog as fd
import customtkinter
from tkinter.messagebox import showinfo
# import tkinter 
from netstat import PcapToCsvConverter
import psutil
import threading
from matplotlib.ticker import AutoMinorLocator
import socket
from matplotlib.ticker import MultipleLocator
from modules.plot import ToplevelWindow
import time
import wmi
from psutil import net_io_counters
import subprocess
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import subprocess
from scapy.all import *
import pandas as pd
import statistics
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
 
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light")
customtkinter.set_default_color_theme("green")
import pywinstyles
...
# pywinstyles.apply_style(window, acrylic)

class App(customtkinter.CTk):
    
    frames = {"frame1": None, "frame2": None}
    
    def frame1_selector(self):
        App.frames["frame2"].pack_forget()
        App.frames["frame3"].pack_forget()
        App.frames["frame4"].pack_forget()
        App.frames["frame1"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

    def frame2_selector(self):
        App.frames["frame1"].pack_forget()
        App.frames["frame3"].pack_forget()
        App.frames["frame4"].pack_forget()
        App.frames["frame2"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
    def frame3_selector(self):
        App.frames["frame1"].pack_forget()
        App.frames["frame4"].pack_forget()
        App.frames["frame2"].pack_forget()
        App.frames["frame3"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

    def frame4_selector(self):
        App.frames["frame1"].pack_forget()

        App.frames["frame2"].pack_forget()
        App.frames["frame3"].pack_forget()
        App.frames["frame4"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

    
    def __init__(self):
        super().__init__()
        # self.state('withdraw')
        # self.title("Change Frames")
        self.toplevel_window = None
        self.csvwindow = None
        self.title("DeepBot.py")
        self.geometry(f"{800}x{580}")
        self.resizable(False, False) 
        self.capture_running = False
        self.capture_thread = None
        self.capture_process = None
        self.capture_interval_running = False
        
        # self.create_default_view()
        # self.update_network_info()
        # self.is_connected()
        # self.ip_addr()
        # self.get_ssid()
        # self.open_input_dialog_event()
        
        # self.open_input_dialog_event() 
         # Instantiate MyFrame
        # self.toplevel_window = None
    # if window exists focus it
                
                # print("CTkInputDialog:", dialog.get_input())    
        # self.geometry("{0}x{0}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))

        # contains everything
        main_container = customtkinter.CTkFrame(self)
        main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        
        # left side panel -> for frame selection
        # left_side_panel = customtkinter.CTkFrame(main_container, width=150)
        # left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=10, pady=10)

        # buttons to select the frames
        self.sidebar_frame = customtkinter.CTkFrame(main_container, width=150, corner_radius=7)
        self.sidebar_frame.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=10, pady=10)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Deepbot", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(side=tkinter.TOP, padx=20, pady=(20, 10))

        

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Home", command=self.frame1_selector)
        self.sidebar_button_1.pack(side=tkinter.TOP, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Live Network Detect", command=self.frame2_selector)
        self.sidebar_button_2.pack(side=tkinter.TOP, padx=20, pady=10)

        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Test Network Data", command=self.frame3_selector)
        self.sidebar_button_3.pack(side=tkinter.TOP, padx=20, pady=10)

        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Capture Net Data", command=self.frame4_selector)
        self.sidebar_button_4.pack(side=tkinter.TOP, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="", anchor="w")
        self.appearance_mode_label.pack(side=tkinter.TOP, padx=20, pady=(30, 180))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.pack(side=tkinter.TOP, padx=20, pady=(10, 10))
        self.appearance_mode_optionemenu.set("Dark")

        # right side panel -> to show the frame1 or frame 2
        self.right_side_panel = customtkinter.CTkFrame(main_container)
        self.right_side_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        self.right_side_container = customtkinter.CTkFrame(self.right_side_panel,fg_color="white")
       
        self.right_side_container.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

        # self.status_header.grid(row=4, column=0, sticky="nsew")
        # App.frames['frame1'] = DefaultViewFrame(self.right_side_panel) 
        # App.frames['frame1'].pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        App.frames['frame1'] =customtkinter.CTkFrame(main_container,)
        App.frames["frame1"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
        # App.frames['frame1'].pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True)
 

        # Status
        self.stats = customtkinter.CTkLabel(App.frames['frame1'], text="STATS", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.stats.grid(row=0, column=0, padx=40 ,pady = 20,sticky="nsew")

        self.status_header = customtkinter.CTkLabel(App.frames['frame1'], text="Status", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.status_header.grid(row=4, column=0, sticky="nsew")
        self.online_status =customtkinter.CTkLabel(App.frames['frame1'], text="Calculating...", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.online_status.grid(row=4, column=1, sticky="nsew")

        self.label_upload_header = customtkinter.CTkLabel(App.frames['frame1'], text="Upload:", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_upload_header.grid(row=5, column=0, sticky="nsew")
        self.label_upload = customtkinter.CTkLabel(App.frames['frame1'], text="Calculating...", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_upload.grid(row=5, column=1, sticky="nsew")

        self.label_download_header = customtkinter.CTkLabel(App.frames['frame1'], text="Download:", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_download_header.grid(row=6, column=0, sticky="nsew")

        self.label_download = customtkinter.CTkLabel(App.frames['frame1'], text="Calculating...", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_download.grid(row=6, column=1, sticky="nsew")

        self.label_name_header = customtkinter.CTkLabel(App.frames['frame1'], text="Name:", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_name_header.grid(row=7, column=0, sticky="nsew")

        self.label_name = customtkinter.CTkLabel(App.frames['frame1'], text="Your Name", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_name.grid(row=7, column=1, sticky="nsew")

        # Label for displaying IP address
        self.label_ip_header = customtkinter.CTkLabel(App.frames['frame1'], text="IP Address:", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_ip_header.grid(row=8, column=0, sticky="nsew")

        self.label_ip = customtkinter.CTkLabel(App.frames['frame1'], text="Your IP Address", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_ip.grid(row=8, column=1, sticky="nsew")

        self.label_ssid_header = customtkinter.CTkLabel(App.frames['frame1'], text="SSID", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_ssid_header.grid(row=9, column=0, sticky="nsew")

        self.label_ssid = customtkinter.CTkLabel(App.frames['frame1'], text="...", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_ssid.grid(row=9, column=1, sticky="nsew")

        self.label_adaptername_header = customtkinter.CTkLabel(App.frames['frame1'], text="Adapter Name", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_adaptername_header.grid(row=10, column=0, sticky="nsew")

        self.label_adaptername = customtkinter.CTkLabel(App.frames['frame1'], text="...", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_adaptername.grid(row=10, column=1, sticky="nsew")
        
        button = customtkinter.CTkButton(App.frames['frame1'],  text="Network Graph", command=self.open_input_dialog_event)
        button.grid(row=11, column=0, padx=20, pady=20, sticky="ew")
        self.toplevel_window = None

        

        # self.toplevel_window = None
        # self.update_netwo
        # rk_info()
        self.is_connected()
        self.update_network_info()
        self.get_active_network_interface_name()
         
        # self.is_connected()
        # # self.toplevel_window = None


        App.frames['frame2'] = customtkinter.CTkFrame(main_container)
        self.entry = customtkinter.CTkEntry(self.frames['frame2'], placeholder_text="File path")
        self.entry.grid(row=0, column=0, columnspan=2, padx=(20, 10), pady=(20, 10), sticky="nsew")

        bt_side = customtkinter.CTkButton(self.frames['frame2'], text="Open",command = self.select_file)
        bt_side.grid(row=0, column=2, padx=(0, 20), pady=(20, 10), sticky="nsew")

        # bt_rect = customtkinter.CTkButton(self.frames['frame2'], text="Verify",command = self.check_and_notify)
        # bt_rect.grid(row=0, column=2, padx=(10, 20), pady=(20, 10), sticky="nsew")

        bt_small = customtkinter.CTkButton(self.frames['frame2'], text="Test",command = self.check_and_notify)
        bt_small.grid(row=2, column=0, columnspan=3, padx=(20, 20), pady=(10, 20), sticky="nsew")

        # self.frames['frame2'].grid_rowconfigure(0, weight=1)
        # self.frames['frame2'].grid_rowconfigure(1, weight=1)
        self.frames['frame2'].grid_columnconfigure(0, weight=10)
        self.frames['frame2'].grid_columnconfigure(1, weight=1)
        self.frames['frame2'].grid_columnconfigure(2, weight=1)
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(self.frames['frame2'], text="MODEL ")
        self.label_radio_group.grid(row=1, column=0, columnspan=1, padx=10, pady=(0,0), sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(self.frames['frame2'],text = "Transformers" ,variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=1, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(self.frames['frame2'],text = "CNN_LSTM" , variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=1, column=2, pady=10, padx=20, sticky="n")
    
        App.frames['frame3'] = customtkinter.CTkFrame(main_container)
        bt_detect = customtkinter.CTkButton(self.frames['frame3'], text="View Data", command=self.processed_table)
        bt_detect.grid(row=1, column=0, columnspan=3, padx=(20, 20), pady=(10, 20), sticky="nsew")
        # self.progressbar_1 = customtkinter.CTkProgressBar(App.frames['frame3'])
        # self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="nsew")
        self.bt_side1 = customtkinter.CTkButton(self.frames['frame3'], text="Live Detect", command=self.capture_interval_start)
        self.bt_side1.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")
        
        self.bt_side2 = customtkinter.CTkButton(self.frames['frame3'], text="Stop", command=self.stop_capture_interval)
        self.bt_side2.grid(row=0, column=1,columnspan=2, padx=(10,20), pady=(20, 10), sticky="nsew")
        self.bt_side2.configure(fg_color = "red")
        self.bt_side2.configure(hover_color ="#D16165033" )
        self.bt_side2.configure(state = "disabled")
        # Configure column weights for proper resizing
        self.frames['frame3'].grid_columnconfigure(0, weight=1)
        self.frames['frame3'].grid_columnconfigure(1, weight=1)
        self.frames['frame3'].grid_columnconfigure(2, weight=1)
        # self.live_plot_frame = customtkinter.CTkFrame(self)
        # self.live_plot_frame.grid(row=2, column=0, columnspan=3, sticky="nsew")

        # Create labels frame
        self.labels_frame = customtkinter.CTkFrame(self.frames['frame3'])
        self.labels_frame.grid(row=2, column=0, sticky="nsew")

        # Create plot frame
        self.plot_frame = customtkinter.CTkFrame(self.frames['frame3'])
        self.plot_frame.grid(row=2, column=1, sticky="nsew")
        
        self.live_plot_label = customtkinter.CTkLabel(self.labels_frame, text="No scan in progress")
        self.live_plot_label.pack(pady=10, padx=10)
        self.detection_msg = customtkinter.CTkLabel(self.labels_frame, text="")
        self.detection_msg.pack(pady=10, padx=10)
        bt_side4 = customtkinter.CTkButton(self.labels_frame, text="", command=self.stop_capture2)
        bt_side4.pack(pady=10, padx=10)

        
        
        # Matplotlib figure
        self.figure = plt.Figure(figsize=(5, 5), dpi=100)
        self.ax = self.figure.add_subplot(111)
        myFmt = mdates.DateFormatter("%H:%M:%S")
        self.ax.xaxis.set_major_formatter(myFmt)
        self.figure.patch.set_facecolor('#2B2B2B')
        self.ax.set_facecolor('#2B2B2B')
        self.ax.spines['bottom'].set_color('white')
        self.ax.spines['top'].set_color('white')
        self.ax.spines['left'].set_color('white')
        self.ax.spines['right'].set_color('white')
        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')
        self.ax.yaxis.label.set_color('white')
        self.ax.xaxis.label.set_color('white')
        self.ax.title.set_color('white')
        self.y_data = []
        dateTimeObj = datetime.now() + timedelta(seconds=-360)
        self.x_data = [dateTimeObj + timedelta(seconds=i) for i in range(4000)]
        self.y_data = [0 for i in range(4000)]
        interface = self.label_adaptername.cget("text")
        # self.plot = self.ax.plot(self.x_data, self.y_data, label=interface, color='lime')[0]
        self.plot = self.ax.plot(self.x_data, self.y_data, label='Incoming Packets  ', color='cyan')[0]
        self.ax.set_ylim(0, 100)
        self.ax.set_xlim(self.x_data[0], self.x_data[-1])
        # self.upload_plot, = self.ax.plot(self.x_data, [0] * len(self.x_data), label="Upload", color='cyan')
        # self.download_plot, = self.ax.plot(self.x_data, [0] * len(self.x_data), label="Download", color='magenta')
        self.ax.legend()

        # Canvas
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(side='top', fill=tkinter.BOTH, expand=True)

        # Initialize lists to store data
        self.timestamps = []
        self.incoming_diffs = []
        self.outgoing_diffs = []
        self.last_net_io = None

        # Call the animate function
        self.animate()


        App.frames['frame4'] = customtkinter.CTkFrame(main_container)
        bt_detect_f4 = customtkinter.CTkButton(self.frames['frame4'], text="View Data", command=self.processed_table)
        bt_detect_f4.grid(row=1, column=0, columnspan=3, padx=(20, 20), pady=(10, 20), sticky="nsew")
        # self.progressbar_1 = customtkinter.CTkProgressBar(App.frames['frame3'])
        # self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="nsew")
        self.bt_side_f4 = customtkinter.CTkButton(self.frames['frame4'], text="Live Detect", command=self.start_capture_pre)
        self.bt_side_f4.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")
        
        self.bt_side2_f4 = customtkinter.CTkButton(self.frames['frame4'], text="Stop", command=self.stop_capture_pre)
        self.bt_side2_f4.grid(row=0, column=1,columnspan=2, padx=(10,20), pady=(20, 10), sticky="nsew")
        self.bt_side2_f4.configure(fg_color = "red")
        self.bt_side2_f4.configure(hover_color ="#D16165033" )
        self.bt_side2_f4.configure(state = "disabled")
        # Configure column weights for proper resizing
        self.frames['frame4'].grid_columnconfigure(0, weight=1)
        self.frames['frame4'].grid_columnconfigure(1, weight=1)
        self.frames['frame4'].grid_columnconfigure(2, weight=1)
        # self.labels_frame_f4 = customtkinter.CTkFrame(self.frames['frame4'])
        # self.labels_frame_f4.grid(row=2, column=0, sticky="nsew")
        self.live_plot_label_capture = customtkinter.CTkLabel(self.frames['frame4'], text="")
        self.live_plot_label_capture.grid(row=2, column=1,columnspan=2, padx=(10,20), pady=(20, 10), sticky="nsew")

    def animate(self):
        self.timestamps = []
        self.incoming_diffs = []
        self.last_net_io = {}
        outgoing_diffs = []
        # global timestamps, incoming_diffs, outgoing_diffs
        self.last_net_io = psutil.net_io_counters(pernic=True)
    # Get network usage statistics
        self.net_io = psutil.net_io_counters(pernic=True)

        # Get current timestamp
        self.current_time = datetime.now()

        # Calculate total incoming and outgoing packets
        self.total_incoming = sum(io.bytes_recv for io in self.net_io.values())
        self.total_outgoing = sum(io.bytes_sent for io in self.net_io.values())

        # Calculate differences
        self.last_total_incoming = sum(io.bytes_recv for io in self.last_net_io.values())
        self.last_total_outgoing = sum(io.bytes_sent for io in self.last_net_io.values())

        self.incoming_diff = self.total_incoming - self.last_total_incoming
        outgoing_diff = self.total_outgoing - self.last_total_outgoing
        
        # incoming_diffs.append(incoming_diff)
        # outgoing_diffs.append(outgoing_diff)
        self.timestamps.append(self.current_time)

        self.last_net_io = self.net_io
        self.x_data.append(self.current_time)
        self.y_data.append(self.incoming_diff)
        # remove oldest data point
        y_min = min(self.y_data[-5:])
        y_max = max(self.y_data[-10:])
       

    # Plot outgoing difference
        # plt.plot(timestamps, outgoing_diffs, label='Outgoing Packets Difference', color='green')
        # update plot data
        self.plot.set_xdata(self.x_data)
        self.plot.set_ydata(self.y_data)
        self.ax.set_ylim(0, y_max+10 )
        self.five_minutes_ago = self.current_time - timedelta(seconds=60)
        self.ax.set_xlim(self.five_minutes_ago, self.current_time)

        # Set minor ticks at 1-minute intervals
        # self.ax.xaxis.set_minor_locator(AutoMinorLocator(6))
        # self.ax.xaxis.set_major_locator(MultipleLocator(60))
        self.canvas.draw_idle()  # redraw plot
        self.after(1000, self.animate)  # repeat after 1s
        
    #     self.ax.set_facecolor('black')
    #     self.ax.spines['bottom'].set_color('white')
    #     self.ax.spines['top'].set_color('white')
    #     self.ax.spines['left'].set_color('white')
    #     self.ax.spines['right'].set_color('white')
    #     self.ax.tick_params(axis='x', colors='white')
    #     self.ax.tick_params(axis='y', colors='white')
    #     self.ax.yaxis.label.set_color('white')
    #     self.ax.xaxis.label.set_color('white')
    #     self.ax.title.set_color('white')

    #     self.timestamps = []
    #     self.incoming_diffs = []
    #     self.outgoing_diffs = []
    #     self.last_net_io = None

    #     self.setup_plot()

    # def setup_plot(self):
    #     # Plot incoming and outgoing differences
    #     self.upload_plot, = self.ax.plot([], [], label="Upload", color='cyan')
    #     self.download_plot, = self.ax.plot([], [], label="Download", color='magenta')

    #     self.ax.legend()
    #     self.ax.set_xlabel('Time')
    #     self.ax.set_ylabel('Bytes Difference')
    #     self.ax.set_title('Network Usage Difference Over Time')

    #     # Create canvas to display plot in tkinter
    #     # self.canvas = FigureCanvasTkAgg(self.figure, master=self)
    #     # self.canvas_widget = self.canvas.get_tk_widget()
    #     # self.canvas_widget.pack(side='top', fill=tk.BOTH, expand=True)
    #     self.canvas = FigureCanvasTkAgg(self.figure, master=self.plot_frame)
    #     self.canvas.get_tk_widget().pack(side='top', fill=tkinter.BOTH, expand=True)
    #     # Call the animate function
    #     self.animate()

    # def animate(self):
    # # Get network usage statistics
    #     net_io = psutil.net_io_counters(pernic=True)

    #     # Get current timestamp
    #     current_time = datetime.now()

    #     # Calculate total incoming and outgoing bytes
    #     total_incoming = sum(io.bytes_recv for io in net_io.values())
    #     total_outgoing = sum(io.bytes_sent for io in net_io.values())

    #     # Calculate differences
    #     if self.last_net_io:
    #         incoming_diff = total_incoming - self.last_net_io[0]
    #         outgoing_diff = total_outgoing - self.last_net_io[1]
    #     else:
    #         incoming_diff = outgoing_diff = 0

    #     self.incoming_diffs.append(incoming_diff)
    #     self.outgoing_diffs.append(outgoing_diff)
    #     self.timestamps.append(current_time)

    #     # Update last_net_io
    #     self.last_net_io = (total_incoming, total_outgoing)

    #     # Limit data to last 100 points for better visualization
    #     if len(self.timestamps) > 100:
    #         self.timestamps = self.timestamps[-100:]
    #         self.incoming_diffs = self.incoming_diffs[-100:]
    #         self.outgoing_diffs = self.outgoing_diffs[-100:]

    #     # Update plot data
    #     self.upload_plot.set_data(self.timestamps, self.outgoing_diffs)
    #     self.download_plot.set_data(self.timestamps, self.incoming_diffs)

    #     # Set appropriate limits for x-axis
    #     if self.timestamps[0] != self.timestamps[-1]:
    #         self.ax.set_xlim(self.timestamps[0], self.timestamps[-1])

    #     # Redraw canvas
    #     self.canvas.draw()

    #     # Repeat after 1 second
    #     self.after(1000, self.animate)    
    def start_capture(self,interface, output_file):
        capture_command = [
            "C:\\Program Files\\Wireshark\\tshark.exe",  # Path to tshark on Windows
            "-i", interface,
            "-w", output_file,
        ]
        # Start capturing live network traffic
        self.process = subprocess.Popen(capture_command)
        
        return self.process
     
    # def stop_capture(self,process):
    #     # Terminate the tshark process
    #     print("hi helo ")
    #     print(process)
    #     # self.capture_running = False
    #     # Check if the process is still running
    #     # if process.poll() is None:
    #     # Terminate the process
    #     process.kill()

     

    # def capture_and_process(self):
    #     output_file = "output.pcap"  # Output file where captured traffic will be stored
    #     csv_output = "outputnew678912.csv"  # Output CSV file
    #     try:
    #         # Start capturing traffic
    #         interface = self.label_adaptername.cget("text")

    #         capture_process = self.start_capture(interface, output_file)
    #         print(f"Capturing traffic on interface {interface}. Press Ctrl+C to stop.")

    #         # Keep the script running until interrupted
    #         while True:
    #             continue

    #     except KeyboardInterrupt:
    #         # Stop capturing on Ctrl+C
    #         self.stop_capture(capture_process)
    #         print("\nCapture stopped.")

    #         # Process the captured pcap file and extract features to CSV
    #         self.pcap_to_csv(output_file, csv_output)
    output_file = "output.pcap"
   
    def start_capture1(self):
          # Output file where captured traffic will be stored
        try:
            if not self.capture_running:
                # self.live_plot_label.configure(text ="Capturing...")
                self.bt_side2.configure(state = "normal") 
                self.bt_side1.configure(state = "disabled")
                self.bt_side2.configure(fg_color = "red")
                self.bt_side2.configure(hover_color ="#D16165033" )
                interface = self.label_adaptername.cget("text")
                # Start capturing traffic
                # interface = "Wi-Fi"  # Update with your interface
                self.capture_process = threading.Thread(target=self.start_capture(interface, self.output_file),daemon = True)
                self.capture_process.start()
                self.capture_running = True
                # messagebox.showinfo("Capture Started", f"Capturing traffic on interface {interface}.")
            else:
                messagebox.showwarning("Warning", "Capture process is already running.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start capture: {str(e)}")
            print(e)
    csv_output = "outputnew678912.csv"
    def start_capture_pre(self):
          # Output file where captured traffic will be stored
        try:
            if not self.capture_running:
                self.live_plot_label_capture.configure(text ="Capturing...")
                self.bt_side2_f4.configure(state = "normal") 
                self.bt_side_f4.configure(state = "disabled")
                self.bt_side2_f4.configure(fg_color = "red")
                self.bt_side2_f4.configure(hover_color ="#D16165033" )
                interface = self.label_adaptername.cget("text")
                # Start capturing traffic
                # interface = "Wi-Fi"  # Update with your interface
                self.capture_process = threading.Thread(target=self.start_capture(interface, self.output_file),daemon = True)
                self.capture_process.start()
                self.capture_running = True
                messagebox.showinfo("Capture Started", f"Capturing traffic on interface {interface}.")
            else:
                messagebox.showwarning("Warning", "Capture process is already running.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start capture: {str(e)}")
            print(e)
    csv_output = "outputnew678912.csv"


    def stop_capture2(self):
        try:
            # self.live_plot_label.configure(text="Capturing..")
            # self.bt_side2_f4.configure(state="disabled")
            # self.bt_side_f4.configure(state="normal")

            if self.capture_running:
                print("Stopping capture...")
                self.capture_running = False
                self.process.terminate()
                self.capture_process.join()  # Wait for capture process to finish

                # Start the CSV conversion in a separate thread
                self.start_csv_conversion(self.output_file, self.csv_output)
                # self.csv_thread.start()
                # if self.csv_thread.is_alive():
                #     print("Thread is still running after joining")
                # else:
                #     print("Thread has finished executing")
                # messagebox.showinfo("Capture Stopped", "Capture stopped successfully.")

            # else:
                # messagebox.showwarning("Warning", "Capture process is not running.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to stop capture: {str(e)}")
            print(e)
    def stop_capture_pre(self):
        try:
            self.live_plot_label_capture.configure(text="Capture Finished")
            self.bt_side2_f4.configure(state="disabled")
            self.bt_side_f4.configure(state="normal")

            if self.capture_running:
                print("Stopping capture...")
                self.capture_running = False
                self.process.terminate()
                self.capture_process.join()  # Wait for capture process to finish
                self.processing_csv()
                # Start the CSV conversion in a separate thread
                self.start_csv_conversion(self.output_file, self.csv_output)
                # self.csv_thread.start()
                # if self.csv_thread.is_alive():
                #     print("Thread is still running after joining")
                # else:
                #     print("Thread has finished executing")
                messagebox.showinfo("Capture Stopped", "Capture stopped successfully.")

            else:
                messagebox.showwarning("Warning", "Capture process is not running.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to stop capture: {str(e)}")
            print(e)
    def processing_csv(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        print("called")
    # Construct the path to the file "output.csv" in the same folder
        file_path = os.path.join(script_dir, "outputnew678912.csv")
        
        # Check if the file exists
        if os.path.exists(file_path):
            self.live_plot_label.configure(text ="")
        else:
            self.live_plot_label.configure(text ="Processing Data")
        self.after(1000, self.processing_csv)    

    

    def start_csv_conversion(self, input_file, output_file):
        try:
            # Start the CSV conversion
            # self.pcap_to_csv(input_file, output_file)
            # self.csv_thread_pcap = threading.Thread(target= self.pcap_to_csv, args=(input_file, output_file)) 
            # self.csv_thread_pcap.start()

            subprocess.Popen(["python", "netstat.py"])
            # self.processing_csv()
    # Wait for the process to finish and capture its output
            # stdout_data, stderr_data = process.communicate()
            
            # Check if the process exited successfully
             
            
            # Notify the user that the conversion is completed
            # messagebox.showinfo("Conversion Completed", f"CSV file saved as {output_file}.")
        except Exception as e:
            # Handle any errors that occur during conversion
            messagebox.showerror("Error", f"Failed to convert pcap to CSV: {str(e)}")
            print(e)
        
    

    def stop_capture_interval(self):
        # global capture_interval_running
        # Set the flag to indicate that the capture interval should stop
        self.capture_interval_running = False
        # print("Stopping capture...")
        # time.sleep(5)
        # print("Capture stopped after 5 seconds.")
        

        # Stop the capture process if it's running
        if self.capture_process and self.capture_process.is_alive():
            self.live_plot_label.configure(text ="Stopping scanning...")
            self.bt_side2.configure(state="disabled")
            self.bt_side1.configure(state="disabled")
            self.capture_process.cancel()
            def delete_files():
                self.live_plot_label.configure(text ="No scan in progress")
                try:
                    # File paths to delete
                    csv_file = "data_with_predictions.csv"
                    pcap_file = "output.pcap"

                    # Delete CSV file if exists
                    if os.path.exists(csv_file):
                        os.remove("outputnew678912.csv")
                        empty_df = pd.DataFrame()
                        empty_df.to_csv(csv_file, index=False)
                        print(f"Deleted file: {csv_file}")

                    # Delete PCAP file if exists
                    if os.path.exists(pcap_file):
                        os.remove(pcap_file)
                        print(f"Deleted file: {pcap_file}")

                except Exception as e:
                    print(f"Error deleting files: {e}")
                self.bt_side1.configure(state = "normal")
        # Schedule the function to delete files after 10 seconds
            threading.Timer(5.0, delete_files).start()
       
            print("Stopping scanning process")
            # self.bt_side1.configure(state = "normal")
            
            # messagebox.showinfo("Capture Stopped", "Capture stopped successfully.")


    def check_botnet(self):
        try:
            # Read the CSV file
            df = pd.read_csv("data_with_predictions.csv")

            # Check if the 'Label' column exists
            if 'Predicted_Label' not in df.columns:
                print("Error: 'Label' column not found in the CSV file.")
                print("no botnet")
                return

            # Check the distribution of the 'Label' column
            label_counts = df['Predicted_Label'].value_counts(normalize=True)

            # Check if label '1' is greater than 80%
            if label_counts.get(1, 0) > 0.8:
                print("Botnet detected!")
                self.detection_msg.configure(text ="Botnet detected!")
            else:
                print("No botnet detected.")
                self.detection_msg.configure(text ="No botnet detected")

        except Exception as e:
            print(f"Error: {e}")

    def capture_interval_start(self):
    # Set the flag to indicate that the capture interval is running
        
        interface = self.label_adaptername.cget("text")
        self.live_plot_label.configure(text ="Scanning...")
        messagebox.showinfo("Capture Started", f"Capturing traffic on interface {interface}.")
        self.capture_interval()

    def capture_interval(self):
    # Set the flag to indicate that the capture interval is running
        self.capture_interval_running = True
        self.live_plot_label.configure(text ="Scanning...")
        
        # Start the capture
        self.start_capture1()

        # Define a function to stop the capture after 10 seconds
        def stop_after_10_seconds():
            threading.Timer(10.0, self.stop_capture2).start()

        # Schedule the function to stop the capture after 10 seconds
        stop_after_10_seconds()

        # Schedule the next capture to start after 20 seconds
        if self.capture_interval_running:
            self.live_plot_label.configure(text ="Scanning...")
            self.capture_process = threading.Timer(20.0, self.capture_interval)
            self.live_plot_label.configure(text ="Scanning...")
            self.check_botnet()
            self.capture_process.start()

     
        # self.csv_thread.join()
    # def execute_pcap_to_csv(self, output_file, csv_output):
    #     try:
    #         # Call your pcap_to_csv function here
    #         self.process_pcap = subprocess.Popen(self.pcap_to_csv(output_file, csv_output))
            
    #     except Exception as e:
    #         print("Error in csv_thread:", e)

    #     return self.process_pcap
        
         # Output CSV file
        # Process the captured pcap file and extract features to CSV
       
    def check_file_existence(self,file_path):
        return os.path.exists(file_path)

    def check_and_notify(self):
        file_path = self.entry.cget("placeholder_text")
        if self.check_file_existence(file_path):
            pass
        elif file_path == "File path":
            messagebox.showinfo("Error",'Spedify file first')
        else:
            messagebox.showwarning("Error", "The file does not exist at the specified path.")

    def select_file(self):
        filetypes = (
            ('csv files', '*.csv'),
            ('All files', '*.*')
        )
        
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        
        if filename:
            self.entry.configure(placeholder_text = filename)


 

    def get_active_network_interface_name(self):

        try:
            hostname = socket.gethostname()
            ipv4Address = socket.gethostbyname(hostname)
            socket.create_connection(("www.google.com", 80)) # better to set timeout as well
            state = "Online"
            
        except OSError:
            state = "Offline"
        if state == "Online":
            # print(state)
            nics = psutil.net_if_addrs()
            for interface, addresses in nics.items():
                for addr in addresses:
                    if addr.address == ipv4Address and addr.family == socket.AF_INET:
                        self.label_adaptername.configure(text=interface)
                        # print(interface)
                        # print("connection")
        else:
            # print("Interface not found for IPv4 address:", ipv4Address)
            self.label_adaptername.configure(text="No connection")
            # print("no_connection")

            # print(interface)
            

        self.after(1500, self.get_active_network_interface_name)


        # Example usage
    
    def open_input_dialog_event(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)
        else:
            self.toplevel_window.focus()
    def processed_table(self):
        if self.csvwindow is None or not self.toplevel_window.winfo_exists():
                # self.toplevel_window = CsvWindow(self)
                subprocess.Popen(["python", "csv_view.py"])
                # csv_window_thread = CsvWindowThread(self)
                # csv_window_thread.start()
        else:
                self.toplevel_window.focus()
    def update_network_info(self):
            counter = net_io_counters()

            upload = counter.bytes_sent
            download = counter.bytes_recv

            # Calculate speed
            self.upload_speed = upload - getattr(self, 'last_upload', 0)
            self.down_speed = download - getattr(self, 'last_download', 0)
            # print(self.upload_speed)
            # print(self.down_speed)
            self.label_upload.configure(text = self.size(self.upload_speed) ) 
            self.label_download.configure(text = self.size(self.down_speed) ) 
            # self.label_download["text"] = self.size(self.down_speed)

            # Update last values
            self.last_upload = upload
            self.last_download = download
            # print(upload)
            # print(download)
            # Schedule next update
            self.after(1500, self.update_network_info)
    def open_input_dialog_event(self):
        # self.create_my_frame()    
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = ToplevelWindow(self)
                # create window if its None or destroyed
            else:
                self.toplevel_window.focus()  
    @staticmethod
    def size(B):
        KB = 1024
        MB = KB ** 2
        GB = KB ** 3
        TB = KB ** 4

        if B < KB:
            return f"{B} Bytes"
        elif KB <= B < MB:
            return f"{B / KB:.2f} KB"
        elif MB <= B < GB:
            return f"{B / MB:.2f} MB"
        elif GB <= B < TB:
            return f"{B / GB:.2f} GB"
        elif TB <= B:
            return f"{B / TB:.2f} TB"

    def is_connected(self):
        try:
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            socket.create_connection(("www.google.com", 80)) # better to set timeout as well
            state = "Online"
            try:
                current_network = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')
                ssid_line = [x for x in current_network if 'SSID' in x and 'BSSID' not in x]
                if ssid_line:
                    ssid_list = ssid_line[0].split(':')
                    connected_ssid = ssid_list[1].strip()
                else:
                    connected_ssid = "No connection"
            except UnicodeDecodeError:
                connected_ssid = "Error decoding network information"

        except OSError:
            state = "Offline"
            connected_ssid = "No connection"
            
        if state == "Offline":
            self.online_status.configure(text_color="red")   
            self.online_status.configure(text="Offline")
            self.label_name.configure(text=hostname)
            self.label_ip.configure(text="-")
            self.label_ssid.configure(text="No connection")
        else:       
            self.online_status.configure(text_color="green")   
            self.online_status.configure(text="Online")
            self.label_name.configure(text=hostname)
            self.label_ip.configure(text=IPAddr)
            self.label_ssid.configure(text=connected_ssid)
        
        self.after(1000, self.is_connected) # check connection again after 1 second
        # self.ip_addr()
        # self.get_ssid()








        

    

        


    def sidebar_button_event(self):
        print("sidebar_button click")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


        

a = App()

a.mainloop()