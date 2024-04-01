from forms.TextField import TextField
from forms.LabelField import LabelField
from tkinter import *
class FormControl(Frame):
    value = None
    label_text = None
    def __init__(self, root, label, value=None):
        super().__init__(root)
        self.__text_field = TextField(root, value)
        self.__label = LabelField(root, label)
        self.pack()

    def set_value(self, value):
        self.__text_field.delete(0, END)
        self.__text_field.insert(0, value)

    def get_value(self):
        return self.__text_field.get()
    def action_on_change(self, callback):
        self.__text_field.bind("<FocusOut>",lambda ev: callback(self.__text_field.get()))