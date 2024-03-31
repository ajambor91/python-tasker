from services.XMLParser import XMLParser
class AuthService:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(AuthService, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.xml = XMLParser()
    def is_user_data(self):