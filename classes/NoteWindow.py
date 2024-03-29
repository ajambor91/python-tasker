from tkinter import *
from classes.XML import XMLParser
class NoteWindow:
    def __init__(self, window):
        self.window = window
        # add widgets here

        self.window.title('Hello Python')
        # self.window.geometry("300x200+10+20")
        self.create_text_area()
        self.add_submit_button()
        self.window.mainloop()
        self.window.wait_visibility()
    def create_text_area(self):
        self.text_area =Text(self.window, height=100, width=100)
        self.text_area.place(x=80, y=10)

    def add_submit_button(self):
        self.btn = Button(self.window, text="Zapisz", fg='blue')
        self.btn.place(x=80, y=100)
        self.btn.bind('<Button-1>',self._save_note)

    def _get_note_content(self):
        text = self.text_area.get("1.0", "end-1c")
        print('DSDASDSDSD',text)
        return text
    def _save_note(self, event):
        # print('SAVED!')
        # print(self.text_area'')
        parser = XMLParser()
        parser.parse_data(data=self._get_note_content())
