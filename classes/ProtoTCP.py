import socket
import threading
from classes.SocketExTCP import SocketExTCP
from app.init import get_config

class ProtoTCP:
    def __init__(self, host):
        self.socket = SocketExTCP(socket.AF_INET, socket.SOCK_STREAM)
        self.thread = threading.Thread(target=lambda: self.__receive_data())
        self.config = get_config()
        self.host = host
        self.__connect()
        self.socket.bind((self.host, self.config.get('defaultPort')))
        print("YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
        self.socket.listen()
        self.thread.start()
    def __connect(self):

        self.socket.connect((self.host, self.config.get('defaultPort')))

    def __receive_data(self):
        print("XXXXXXXXXXXXXXXXXX")

        conn, addr = self.socket.accept()
        print("XXXXXXXXXXXXXXXXXX")
        with conn:
            print('Połączono z', addr)
            while True:
                # Odbieranie danych
                data_received = conn.recv(1024)
                if not data_received:
                    break
                print('Odebrano:', data_received.decode())
    def send_data(self, data):
        if self.socket:
            self.socket.sendall(data)

    def close_connection(self):
        if self.socket:
            self.socket.close()
            self.socket = None


