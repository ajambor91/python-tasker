import socket
from app.init import get_config
from services.NetworkService import NetworkService
import threading
class Listen:
    def __init__(self, network):
        self.network_service = NetworkService()
        self.network = network
        self.config = get_config()
        self.__set_socket()
        self.__run()

    def __set_socket(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.udp_socket.bind(('0.0.0.0', self.config.get('defaultPort')))
        print(self.config.get('defaultPort'))
        self.worker = threading.Thread(target= lambda: self.__listen())
    def __listen(self):
        while True:
            data, addr = self.udp_socket.recvfrom(1024)
            msg = data.decode()
            ip_addr = addr[0]
            print(self.network.ip, ip_addr)
            print(data.decode(), addr)
            if self.__checkAnswer(msg) is True and ip_addr != self.network.ip:
                self.__create_socket(ip_addr)

    def __run(self):
        self.worker.start()

    def __checkAnswer(self, answer):
        if answer == self.config.get("appUuid"):
            return True
        return False
    def __create_socket(self, addr):
        self.network_service.add_addr(addr)