import socket
import threading

from app.init import get_config
import threading
class SocketTCPRec:

    def __init__(self, host):
        self.worker = threading.Thread(target=lambda: self.__start_listening())
        self.host = host
        self.config = get_config()
        self.__set_socket()
        self.__run_socket()
    def stop_listening(self):
        self.server_socket.close()
    def __run_socket(self):
        self.worker.start()
    def __set_socket(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.config.get('tcpListenPort')))
        self.server_socket.listen(5)
    def __start_listening(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Połączenie nawiązane z {client_address}")
            print(f"Dane: {client_socket.recv(1024).decode()}")
            client_socket.close()





