from tkinter import ttk
from forms.LoginForm import LoginForm
class AppMainWindowUserTab(ttk.Frame):

    def __init__(self, window):
        super().__init__(window)
        self.window = window
        self.label = None
        self.__create_label()

    def __create_label(self):
        self.control = LoginForm(self)
        self.control.grid(column=0, row=0, padx=2, pady=2)



