import socket
from app.init import get_config
class SocketTCPRec:

    def __init__(self, host):

        self.host = host
        self.config = get_config()
        self.__set_socket()
        self.__start_listening()
    def stop_listening(self):
        self.server_socket.close()
    def __set_socket(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.config.get('tcpListenPort')))
        self.server_socket.listen(5)
    def __start_listening(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Połączenie nawiązane z {client_address}")
            client_socket.close()





