from tkinter import Button, SE, FLAT, N
class NoteAddButton(Button):
    background = '#47A2FE'
    foreground = '#fff'
    borderwidth = 0
    borderradius = 10
    anchor = SE
    text = 'Zapisz'
    def __init__(self, window, root):
        super().__init__(root,
                         foreground=self.foreground,
                         background=self.background,
                         text=self.text,
                         borderwidth=self.borderwidth,
                         padx=self.borderradius,
                         pady=self.borderradius,
                         command=lambda: self.__save_note())
        self.window = window
        self.root = root
    def __run(self):
        self.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)


    def __save_note(self):
        self.window.on_save_action()
        pass