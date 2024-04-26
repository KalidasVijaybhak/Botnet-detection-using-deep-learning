import customtkinter

class NetworkTestView:
    def __init__(self,parent):
        self.parent = parent
    def show(self):
        self.network_test_view.grid()

    def hide_network_test(self):
        self.network_test_view.grid_remove() 

    def create_default_view(self):
        self.network_test_view= customtkinter.CTkFrame(self.parent)
        button = customtkinter.CTkButton(self.parent, text="my button", command=self.sidebar_button_event)
        button.grid(row=0, column=0, padx=20, pady=20)
    def sidebar_button_event(self):
        print("sidebar_button click")    