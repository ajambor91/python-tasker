import socket
from classes.SocketExTCP import SocketExTCP
from app.init import get_config
class SocketTCPRec:

    def __init__(self, host):

        self.host = host
        self.config = get_config()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.config.get('tcpListenPort')))
        self.server_socket.listen(5)

    def start_listening(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Połączenie nawiązane z {client_address}")
            # Tutaj obsługujesz połączenie

            # Po zakończeniu obsługi połączenia zamykasz gniazdo klienta
            client_socket.close()

    def stop_listening(self):
        self.server_socket.close()
        print("Nasłuchiwanie zostało zatrzymane.")



