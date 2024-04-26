import customtkinter
import psutil
import tkinter 
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
# from ui import BaseView


class DefaultView:
    def __init__(self, parent):
        self.parent = parent
        self.toplevel_window = None
        self.create_default_view()
        self.update_network_info()
        self.is_connected()
        # self.ip_addr()
        # self.get_ssid()
        # self.open_input_dialog_event()
        
        # self.open_input_dialog_event() 
         # Instantiate MyFrame
        # self.toplevel_window = None
    def open_input_dialog_event(self):
        # self.create_my_frame()    
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = ToplevelWindow(self.parent)
                  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()  # if window exists focus it
            
            # print("CTkInputDialog:", dialog.get_input())    
   
    # def create_my_frame(self):
    #     self.my_frame = MyFrame(self.parent)  # Instantiate MyFrame
    #     self.my_frame.grid(row=11, column=0, columnspan=2, sticky="nsew")

    def show(self):
        self.default_view.grid()

    def hide(self):
        self.default_view.grid_remove()

    def create_default_view(self):
        
        self.default_view = customtkinter.CTkFrame(self.parent)
        self.default_view.grid(row=0, column=1, rowspan=4, sticky="nsew")
        
        self.logo_label = customtkinter.CTkLabel(self.default_view, text="Stats",anchor="center", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=40 ,pady = 20,sticky="nsew")
         
        # Labels for network information

        self.status_header = customtkinter.CTkLabel(self.default_view, text="Status", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.status_header.grid(row=4, column=0, sticky="nsew")
        self.online_status =customtkinter.CTkLabel(self.default_view, text="Calculating...", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.online_status.grid(row=4, column=1, sticky="nsew")

        self.label_upload_header = customtkinter.CTkLabel(self.default_view, text="Upload:", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_upload_header.grid(row=5, column=0, sticky="nsew")
        self.label_upload = customtkinter.CTkLabel(self.default_view, text="Calculating...", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_upload.grid(row=5, column=1, sticky="nsew")

        self.label_download_header = customtkinter.CTkLabel(self.default_view, text="Download:", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_download_header.grid(row=6, column=0, sticky="nsew")

        self.label_download = customtkinter.CTkLabel(self.default_view, text="Calculating...", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_download.grid(row=6, column=1, sticky="nsew")

        self.label_name_header = customtkinter.CTkLabel(self.default_view, text="Name:", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_name_header.grid(row=7, column=0, sticky="nsew")

        self.label_name = customtkinter.CTkLabel(self.default_view, text="Your Name", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_name.grid(row=7, column=1, sticky="nsew")

        # Label for displaying IP address
        self.label_ip_header = customtkinter.CTkLabel(self.default_view, text="IP Address:", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_ip_header.grid(row=8, column=0, sticky="nsew")

        self.label_ip = customtkinter.CTkLabel(self.default_view, text="Your IP Address", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_ip.grid(row=8, column=1, sticky="nsew")

        self.label_ssid_header = customtkinter.CTkLabel(self.default_view, text="SSID", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_ssid_header.grid(row=9, column=0, sticky="nsew")

        self.label_ssid = customtkinter.CTkLabel(self.default_view, text="...", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_ssid.grid(row=9, column=1, sticky="nsew")
        
        button = customtkinter.CTkButton(self.default_view,  text="CTkButton", command=self.open_input_dialog_event)
        button.grid(row=10, column=0, padx=20, pady=20, sticky="ew")
        self.toplevel_window = None
        # self.default_view = customtkinter.CTkFrame(self.parent)
        # self.default_view.grid(row=0, column=2, rowspan=4, sticky="nsew")
        # self.logo_label1 = customtkinter.CTkLabel(self.default_view, text="Stats", font=customtkinter.CTkFont(size=30, weight="bold"))
        # self.logo_label1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")
         
        # self.default_view = customtkinter.CTkFrame(self.parent)
        # self.default_view.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

        # self.logo_label = customtkinter.CTkLabel(self.default_view, text="Stats", anchor="center", font=customtkinter.CTkFont(size=30, weight="bold"))
        # self.logo_label.pack(padx=40, pady=20, fill=tkinter.BOTH)

        # # Labels for network information
        # self.status_header = customtkinter.CTkLabel(self.default_view, text="Status", font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.status_header.pack(fill=tkinter.BOTH)

        # self.online_status = customtkinter.CTkLabel(self.default_view, text="Calculating...", font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.online_status.pack(fill=tkinter.BOTH)

        # self.label_upload_header = customtkinter.CTkLabel(self.default_view, text="Upload:", font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.label_upload_header.pack(fill=tkinter.BOTH)

        # self.label_upload = customtkinter.CTkLabel(self.default_view, text="Calculating...", font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.label_upload.pack(fill=tkinter.BOTH)

        # self.label_download_header = customtkinter.CTkLabel(self.default_view, text="Download:", font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.label_download_header.pack(fill=tkinter.BOTH)

        # self.label_download = customtkinter.CTkLabel(self.default_view, text="Calculating...", font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.label_download.pack(fill=tkinter.BOTH)

        # self.label_name_header = customtkinter.CTkLabel(self.default_view, text="Name:", font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.label_name_header.pack(fill=tkinter.BOTH)

        # self.label_name = customtkinter.CTkLabel(self.default_view, text="Your Name", font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.label_name.pack(fill=tkinter.BOTH)

        # # Label for displaying IP address
        # self.label_ip_header = customtkinter.CTkLabel(self.default_view, text="IP Address:", font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.label_ip_header.pack(fill=tkinter.BOTH)

        # self.label_ip = customtkinter.CTkLabel(self.default_view, text="Your IP Address", font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.label_ip.pack(fill=tkinter.BOTH)

        # self.label_ssid_header = customtkinter.CTkLabel(self.default_view, text="SSID", font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.label_ssid_header.pack(fill=tkinter.BOTH)

        # self.label_ssid = customtkinter.CTkLabel(self.default_view, text="...", font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.label_ssid.pack(fill=tkinter.BOTH)

        # button = customtkinter.CTkButton(self.default_view,  text="CTkButton", command=self.open_input_dialog_event)
        # button.pack(padx=20, pady=20, fill=tkinter.BOTH)

        self.toplevel_window = None



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

            # Schedule next update
            self.default_view.after(1500, self.update_network_info)

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
        self.parent.after(1000, self.is_connected) # check connection again after 1 second
    # def ip_addr(self):
    #     hostname = socket.gethostname()
    #     IPAddr = socket.gethostbyname(hostname)
    #     self.label_name.configure(text = hostname)
    #     self.label_ip.configure(text= IPAddr)

    # def get_ssid(self):
    #     connected_ssid = "No Connection"
    #     current_network = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')
    #     ssid_line = [x for x in current_network if 'SSID' in x and 'BSSID' not in x]
    #     if ssid_line:
    #         ssid_list = ssid_line[0].split(':')
    #         connected_ssid = ssid_list[1].strip()
    #         print(connected_ssid)     
    #     self.label_ssid.configure(text = connected_ssid)




    