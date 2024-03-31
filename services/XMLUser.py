import os
import xml.etree.ElementTree as gfg
from app.init import get_app_data
class XMLUser(object):
    USER_FILE_NAME = 'user_data.xml'
    def __init__(self):
        self.user_file = get_app_data(self.USER_FILE_NAME)
        self.root = gfg.Element('root')
        self.tree = gfg.ElementTree(self.root)
        self.user = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(XMLUser, cls).__new__(cls)
        return cls.instance
    def parse_data(self, data):
        print(data)
        note = gfg.SubElement(self.root, 'note', id='note')
        note.text = data
        tree = gfg.ElementTree(self.root)
        self.__add_user_tag()
        self.__add_user_name('Adam')
        self.__add_user_email('adam@adam.pl')
        self.__set_login_stage(1)
        with open (self.user_file, "wb") as files :
            tree.write(files)

    def parse_file(self):
        path = self.user_home_path + self.notes
        tree = gfg.parse(path)
        root = tree.getroot()
        notes_list = list()
        for child in root:
            notes_list.append(child.text)
        return notes_list

    def __add_user_tag(self):
        self.user = gfg.SubElement(self.root, 'user')


    def __add_user_email(self, email):
        email_element = gfg.SubElement(self.user, 'email')
        email_element.text = email

    def __add_user_name(self, name):
        name_element = gfg.SubElement(self.user, 'name')
        name_element.text = name

    def __set_login_stage(self, level):
        login_stage = gfg.SubElement(self.user, 'login_stage')
        login_stage.text = level