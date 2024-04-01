from tkinter import Tk, ttk
from classes.AppMainWindowUserTab import AppMainWindowUserTab
class AppMainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.notebook = ttk.Notebook(self)
        self.user_tab = None
        self.__set_window()
        self.__add_user_tab()
        self.mainloop()



    def __set_window(self):
        self.wait_visibility()
        self.geometry("400x300-0-0")
    def __add_user_tab(self):

        self.notebook.add(AppMainWindowUserTab(self), text='User')
        self.notebook.grid(column=0, row=0, padx=2, pady=2)
