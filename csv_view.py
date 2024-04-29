import customtkinter
import random
import csv
from CTkTable import *
from CTkXYFrame import *


import threading

class CsvWindowThread(threading.Thread):
    def __init__(self, parent):
        self.toplevel_window = None
        self.csvwindow = None
        threading.Thread.__init__(self)
        self.parent = parent

    def run(self):
        self.toplevel_window = CsvWindow(self.parent)


# Assuming this code is inside a class or function
# Create and start the thread

class CsvWindow(customtkinter.CTk):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry(f"{600}x{500}")
        
        xy_frame = CTkXYFrame(self)
        xy_frame.pack(fill="both", expand=True, padx=10, pady=10)

        random_list = []

        with open('outputnew678912.csv', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            csv_data = list(csv_reader)

        # Get the number of rows and columns in the CSV file
        num_rows = len(csv_data)
        num_columns = len(csv_data[0]) if csv_data else 0
            
        table = CTkTable(xy_frame, row=num_rows, column=num_columns, values=csv_data)
        table.pack()

class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)


if __name__ == "__main__":
    app = CsvWindow()
    app.mainloop()