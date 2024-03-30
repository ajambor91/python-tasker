import socket
from app.init import get_config

class Listen:
    def __init__(self):
        self.config = get_config()
        self.__set_socket()
        self.__run()

    def __set_socket(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.udp_socket.bind(('0.0.0.0', self.config.get('defaultPort')))
    def __run(self):
        while True:
            data, addr = self.udp_socket.recvfrom(1024)
            print(data.decode(), addr)