import struct
import ipaddress
import socket
import time

import netifaces
from classes.BroadcastSend import BroadcastSend
from classes.BroadcastListen import BroadcastListen

class NetworkEx:
    def __init__(self):
        self.interfaces_details_list = None
        self.interfaces = netifaces.interfaces()
        self.broadcast_addresses = None

    def calculate_broadcast(self):
        self.broadcast_addresses = list()
        for interface in self.interfaces_details_list:
            ip_int = self.convert_adresses_to_bin(interface.get('ip'))
            mask_int = self.convert_adresses_to_bin(interface.get('subnet_mask'))

            binary_broadcast = self.calculate_broadcast_bin(mask_int, mask_int)
            # decimal_broadcast = self.binary_to_decimal(binary_broadcast)

            decimal_broadcast = self.binary_to_ip(binary_broadcast)
            self.broadcast_addresses.append(decimal_broadcast)

    def get_interfaces_info(self):
        self.interfaces_details_list = list()
        try:
            for interface in self.interfaces:

                addresses = netifaces.ifaddresses(interface)
                if netifaces.AF_INET in addresses:
                    ip_address_info = addresses[netifaces.AF_INET]
                    for details in ip_address_info:
                        self.interfaces_details_list.append({
                            'ip': details.get('addr'),
                            'subnet_mask': details.get('netmask')
                        })

        except ValueError:
            print(ValueError)
    def convert_adresses_to_bin(self, addr):
        bytes_data = addr.encode()

        # Konwersja każdego bajtu na reprezentację binarną
        binary_list = [bin(byte)[2:] for byte in bytes_data]

        # Łączenie reprezentacji binarnych bajtów w jeden ciąg binarny
        binary_string = ''.join(binary_list)

        return binary_string
    def calculate_broadcast_bin(self, subnet_mask_binary, ip_binary):
        inverted_subnet_mask = ''.join('1' if bit == '0' else '0' for bit in subnet_mask_binary)
        broadcast_address_binary = ''.join('1' if ip_bit == '1' or subnet_bit == '1' else '0' for ip_bit, subnet_bit in
                                           zip(ip_binary, inverted_subnet_mask))
        return broadcast_address_binary
    def binary_to_decimal(self, binary_data):
        return int(binary_data, 2)

    def binary_to_ip(self,binary_address):
        # binary_address = '101011000000011000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        binary_address = binary_address[:32]

        # Konwersja binarnej postaci adresu IP na postać dziesiętną
        decimal_address = int(binary_address, 2)

        # Konwersja dziesiętnej postaci adresu na adres IP
        ip_address = ipaddress.IPv4Address(decimal_address)
        return str(ip_address)