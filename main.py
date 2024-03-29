from classes.Tray import Tray
from classes.Network import Network
from app.init import *
from classes.Top import Top

def run_app():
    # tray = Tray()
    top = Top()
    network = Network()
    # tray.create_icon()
    top.run_app()

if __name__ == '__main__':
    # if lock_app() is True:
    run_app()



