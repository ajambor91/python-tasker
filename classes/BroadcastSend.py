
import socket
import time

from app.init import get_config
import threading
class BroadcastSend:
    def __init__(self):
        self.config = get_config()
        self.__set_broadcast()
        self.__run()
    def __set_broadcast(self):
        self.worker = threading.Thread(target= lambda: self.__broadcast())
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def __run(self):
        self.worker.start()
    def __broadcast(self):
        while True:
            time.sleep(1)
            self.udp_socket.sendto(self.config.get("appUuid").encode(), ("255.255.255.255", self.config.get('defaultPort')))