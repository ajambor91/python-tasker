from tkinter import ttk
class AppMainWindowUserTab(ttk.Frame):

    def __init__(self, window):
        super().__init__(window)
        self.window = window
        self.label = None
        self.__create_label()

    def __create_label(self):
        self.label = ttk.Label(self, text="Welcome to GeeksForGeeks")
        self.label.grid(column=0, row=0, padx=30, pady=30)
        # self.window.add(self, text='User')
        self.pack()


