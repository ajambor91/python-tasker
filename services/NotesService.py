from services.XML import XMLParser
class NotesService(object):

    def __init__(self):
        self.xml = XMLParser()
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(NotesService, cls).__new__(cls)
        return cls.instance
    def parse_data(self, data):
        self.xml.parse_data(data)

    def parse_file(self):
        return self.xml.parse_file()
