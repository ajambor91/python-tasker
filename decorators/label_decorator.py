from tkinter import ttk
def label_decorator(text_class):
    class TextLabel(text_class, ttk.Label):
        def __init__(self, *args, **kwargs):
            # print("Przed inicjalizacją instancji klasy", cls.__name__)
            super().__init__(*args, **kwargs)
            # print("Po inicjalizacji instancji klasy", cls.__name__)

    return TextLabel