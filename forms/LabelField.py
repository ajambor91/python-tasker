from tkinter import ttk


class LabelField(ttk.Label):
    BACKGROUND_COLOR = '#f0e589'
    BORDER_WIDTH = 0
    FONT = ('Georgia', 14)

    def __init__(self, root, label):
        super().__init__(root, text=label)
        self.root = root
        self.pack()

