from classes.SocketTCPSend import SocketTCPSend
from classes.SocketTCPRec import SocketTCPRec
from services.NotesService import NotesService
class NetworkService(object):


    def __init__(self):
        self._send_sockets = list()
        self._notes_service = NotesService()
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(NetworkService, cls).__new__(cls)
        return cls.instance
    def add_addr(self, addr):
        self._send_sockets.append(SocketTCPSend(addr))
    def start_listen(self, ip):
        self.listen_socket =  SocketTCPRec(ip)
    def receive_msg(self, data):
        self._notes_service.parse_data(data.decode())
    def broadcast_messages(self, msg):
        for socket in self._send_sockets:
            socket.send_data(msg)
