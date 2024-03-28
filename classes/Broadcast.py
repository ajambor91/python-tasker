
import socket

class Broadcast:
    import socket

    def send_broadcast_packet(self,broadcast_address, port):
        # Tworzenie gniazda UDP
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        # Wysyłanie wiadomości na adres broadcast
        udp_socket.sendto('Hiiiii'.encode(), (broadcast_address, port))

        # Zamykanie gniazda
        udp_socket.close()

        # if __name__ == "__main__":
        #     broadcast_address = "255.255.255.255"  # Adres broadcast
        #     port = 12345  # Port, na którym chcesz wysłać wiadomość
        #     message = "Hello, world!"  # Wiadomość do wysłania
        #
        #     self.send_broadcast_packet(broadcast_address, port, message)