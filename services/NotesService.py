from services.XMLParser import XMLParser
from services.NetworkService import NetworkService
class NotesService(object):

    def __init__(self):
        self.xml = XMLParser()
        self.network_service = NetworkService()
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(NotesService, cls).__new__(cls)
        return cls.instance
    def parse_data(self, data):
        self.xml.parse_data(data)
        self.__broadcast_msg(data)

    def parse_file(self):
        return self.xml.parse_file()

    def __broadcast_msg(self, data):
        self.network_service.broadcast_messages(data)
