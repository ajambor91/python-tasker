import socket
from classes.SocketExTCP import SocketExTCP
from app.init import get_config
class SocketTCPSend:
    def __init__(self, host):
        self.socket = SocketExTCP(socket.AF_INET, socket.SOCK_STREAM)
        self.config = get_config()
        self.host = host
        self.__connect()

    def __connect(self):

        self.socket.connect((self.host, self.config.get('tcpSendPort')))

    def send_data(self, data):
        if self.socket:
            self.socket.sendall(data)

    def close_connection(self):
        if self.socket:
            self.socket.close()
            self.socket = None


