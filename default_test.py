import tkinter
import customtkinter
from modules.plot import ToplevelWindow
import tkinter
import customtkinter
# from default_test import DefaultViewFrame
from modules.default_view import DefaultView

import customtkinter
import psutil
# import tkinter 
import threading
import socket
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
class DefaultViewFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        # self.create_default_view()
        
        # self.ip_addr()
        # self.get_ssid()
        # self.open_input_dialog_event()
        
        
        self.default_view = customtkinter.CTkFrame(parent,fg_color="blue")
        # self.default_view.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True)

        # Status
        self.status_header = customtkinter.CTkLabel(self.default_view, text="Status", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.status_header.pack(side=tkinter.TOP, fill=tkinter.BOTH, padx=20, pady=(20, 10))

        self.online_status = customtkinter.CTkLabel(self.default_view, text="Calculating...", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.online_status.pack(side=tkinter.TOP, fill=tkinter.BOTH, padx=20, pady=(10, 20))

        # Upload
        self.label_upload_header = customtkinter.CTkLabel(self.default_view, text="Upload:", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_upload_header.pack(side=tkinter.TOP, fill=tkinter.BOTH, padx=20, pady=(20, 10))

        self.label_upload = customtkinter.CTkLabel(self.default_view, text="Calculating...", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_upload.pack(side=tkinter.TOP, fill=tkinter.BOTH, padx=20, pady=(10, 20))

        # Download
        self.label_download_header = customtkinter.CTkLabel(self.default_view, text="Download:", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_download_header.pack(side=tkinter.TOP, fill=tkinter.BOTH, padx=20, pady=(20, 10))

        self.label_download = customtkinter.CTkLabel(self.default_view, text="Calculating...", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_download.pack(side=tkinter.TOP, fill=tkinter.BOTH, padx=20, pady=(10, 20))

        # Name
        self.label_name_header = customtkinter.CTkLabel(self.default_view, text="Name:", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_name_header.pack(side=tkinter.TOP, fill=tkinter.BOTH, padx=20, pady=(20, 10))

        self.label_name = customtkinter.CTkLabel(self.default_view, text="Your Name", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_name.pack(side=tkinter.TOP, fill=tkinter.BOTH, padx=20, pady=(10, 20))

        # IP Address
        self.label_ip_header = customtkinter.CTkLabel(self.default_view, text="IP Address:", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_ip_header.pack(side=tkinter.TOP, fill=tkinter.BOTH, padx=20, pady=(20, 10))

        self.label_ip = customtkinter.CTkLabel(self.default_view, text="Your IP Address", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_ip.pack(side=tkinter.TOP, fill=tkinter.BOTH, padx=20, pady=(10, 20))

        # SSID
        self.label_ssid_header = customtkinter.CTkLabel(self.default_view, text="SSID", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_ssid_header.pack(side=tkinter.TOP, fill=tkinter.BOTH, padx=20, pady=(20, 10))

        self.label_ssid = customtkinter.CTkLabel(self.default_view, text="...", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_ssid.pack(side=tkinter.TOP, fill=tkinter.BOTH, padx=20, pady=(10, 20))


        button = customtkinter.CTkButton(self.default_view,  text="CTkButton", command=self.open_input_dialog_event)
        button.pack(padx=20, pady=20, fill=tkinter.BOTH)

        self.toplevel_window = None
        # self.update_network_info()
        # self.is_connected()
        self.update_network_info()
        self.is_connected()
        # self.toplevel_window = None

    def open_input_dialog_event(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)
        else:
            self.toplevel_window.focus()
    def update_network_info(self):
            counter = net_io_counters()

            upload = counter.bytes_sent
            download = counter.bytes_recv

            # Calculate speed
            self.upload_speed = upload - getattr(self, 'last_upload', 0)
            self.down_speed = download - getattr(self, 'last_download', 0)

            self.label_upload.configure(text = self.size(self.upload_speed) ) 
            self.label_download.configure(text = self.size(self.down_speed) ) 
            # self.label_download["text"] = self.size(self.down_speed)

            # Update last values
            self.last_upload = upload
            self.last_download = download
            print(upload)
            print(download)
            # Schedule next update
            self.default_view.after(1500, self.update_network_info)
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
            current_network = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')
            ssid_line = [x for x in current_network if 'SSID' in x and 'BSSID' not in x]
            if ssid_line:
                ssid_list = ssid_line[0].split(':')
                connected_ssid = ssid_list[1].strip()
                print(connected_ssid) 
        except OSError:
            state = "Offline"
             
        # print(state)
        if state == "Offline":
                 self.online_status.configure(text_color="red")   
                 self.online_status.configure(text ="offine")
                 self.label_name.configure(text = hostname)
                 self.label_ip.configure(text= "-")
                 self.label_ssid.configure(text = "No connection")
        else:       
                self.online_status.configure(text_color="green")   
                self.online_status.configure(text ="online")
                self.label_name.configure(text = hostname)
                self.label_ip.configure(text= IPAddr)
                self.label_ssid.configure(text = connected_ssid)
        self.after(1000, self.is_connected) # check connection again after 1 second