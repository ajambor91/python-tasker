import os
import xml.etree.ElementTree as gfg
class XMLParser(object):
    user_home_path = os.path.expanduser("~")
    notes = '\\notes.xml'
    root = gfg.Element('root')

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(XMLParser, cls).__new__(cls)
        return cls.instance
    def parse_data(self, data):
        print(data)
        # print(self.user_home_path)
        note = gfg.SubElement(self.root, 'note', id='note')
        # noteXml.attrib = 'data'
        note.text = data
        # self.root.append(note)
        tree = gfg.ElementTree(self.root)
        path = self.user_home_path + self.notes
        with open (path, "wb") as files :
            tree.write(files)

    def parse_file(self):
        path = self.user_home_path + self.notes
        print('PATH', path)
        tree = gfg.parse(path)
        root = tree.getroot()
        notes_list = list()
        for child in root:
            notes_list.append(child.text)
            print('xxxdfdfdf',notes_list)
        return notes_list