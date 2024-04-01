from tkinter import *
from forms.FormsModule import *
class LoginForm(Frame):
    def __init__(self, window, **kwargs):
        super().__init__()
        self.form = FormGroup({
            "login": FormControl(self, label="Login"),
            "password": FormControl(self, label='Hasło')
        }, window)
        self.form.get('login').action_on_change(lambda value: self.__test(value))


    def __test(self, value):
        print(value)