from tkinter import *
class FormGroup(Frame):
    def __init__(self, data, root, **kwargs):
        super().__init__()
        self.controls = {}
        self.__set_controls(data)
        self.grid(column=0, row=0, padx=2, pady=2)

    def __set_controls(self, controls):
        for key, control in controls.items():
            self.controls[key] = control
    def add_control(self, name, control):
        self.controls[name] = control

    def remove_control(self, name):
        del self.controls[name]

    def get(self, control):
        controls = control.split()

        try:
            control = self.controls[controls[0]]
            if isinstance(control, FormGroup):
                return control.get(".".join(controls[1:]))
            else:
                return control
        except Exception as e:
            print("CANNOT FIND CONTROL NAME")
            return False


