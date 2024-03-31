from classes.Tray import Tray

class Top():
    def __init__(self):
        self.app_tray = Tray()

    def run_app(self):
        self.app_tray.create_icon()
