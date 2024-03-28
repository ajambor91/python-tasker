from classes.Tray import Tray
from classes.Network import Network
from app.init import *


def run_app():
    tray = Tray()
    network = Network()
    tray.create_icon()

if __name__ == '__main__':
    if lock_app() is True:
        run_app()



