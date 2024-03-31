from classes.SocketTCPSend import SocketTCPSend
from classes.SocketTCPRec import SocketTCPRec
class NetworkService(object):


    _send_sockets = list()
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(NetworkService, cls).__new__(cls)
        return cls.instance
    def add_addr(self, addr):
        print('******************************')
        self._send_sockets.append(SocketTCPSend(addr))
    def start_listen(self, ip):
        self.listen_socket =  SocketTCPRec(ip)
    def broadcast_messages(self, msg):
        for socket in self._sockets:
            socket.send_data(msg)
