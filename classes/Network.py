
import ipaddress
import socket

class Network:


    def __init__(self):
        self.hostname = socket.gethostname()
        # print(self.hostname)
        # self.ip = socket.gethostbyname(self.hostname)
        # self.network_addr = ipaddress.ip_interface(f"{ip}/{subnet_mask}").network
        # self.network_addr = ipaddress.IPv4Network.broadcast_address
        # print(self.network_addr)