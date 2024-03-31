from classes.ProtoTCP import ProtoTCP
class NetworkService(object):

    _sockets = list()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(NetworkService, cls).__new__(cls)
        return cls.instance
    def add_addr(self, addr):
        print('******************************')
        self._sockets.append(ProtoTCP(addr))

    def broadcast_messages(self, msg):
        for socket in self._sockets:
            socket.send_data(msg)
