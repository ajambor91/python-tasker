
import socket
import time

from app.init import get_config
import threading
class Broadcast:
    import socket

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
        # Tworzenie gniazda UDP
        while True:
            time.sleep(1)
            self.udp_socket.sendto(self.config.get("appUuid").encode(), ("255.255.255.255", self.config.get('defaultPort')))

        # Wysyłanie wiadomości na adres broadcast

        # Zamykanie gniazda
        # self.udp_socket.close()

        # if __name__ == "__main__":
        #     broadcast_address = "255.255.255.255"  # Adres broadcast
        #     port = 12345  # Port, na którym chcesz wysłać wiadomość
        #     message = "Hello, world!"  # Wiadomość do wysłania
        #
        #     self.send_broadcast_packet(broadcast_address, port, message)