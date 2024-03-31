import struct
import ipaddress
import socket
import time

import netifaces
from classes.BroadcastSend import BroadcastSend
from classes.BroadcastListen import BroadcastListen
from classes.NetworkEx import NetworkEx
from services.NetworkService import NetworkService
class Network(NetworkEx):


    def __init__(self):
        super().__init__()
        self.hostname = socket.gethostname()
        self.ip = socket.gethostbyname(self.hostname)
        self.network_addr = ipaddress.IPv4Network.broadcast_address
        self.get_interfaces_info()
        self.calculate_broadcast()
        self.br = BroadcastSend()
        self.listen = BroadcastListen(self)
        self.network_services = NetworkService()
        print('(((((((((((((((((((((((((((((((((((((((((((', self.ip)
        self.network_services.start_listen(self.ip)


