import os
import xml.etree.ElementTree as gfg
from app.init import get_app_data
class XMLParser(object):

    def __init__(self):
        self.notes = get_app_data('notes.xml')
        self.root = gfg.Element('root')
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(XMLParser, cls).__new__(cls)
        return cls.instance
    def parse_data(self, data):
        print(data)
        note = gfg.SubElement(self.root, 'note', id='note')
        note.text = data
        tree = gfg.ElementTree(self.root)
        with open (self.notes, "wb") as files :
            tree.write(files)

    def parse_file(self):
        tree = gfg.parse(self.notes)
        root = tree.getroot()
        notes_list = list()
        for child in root:
            notes_list.append(child.text)
        return notes_list
