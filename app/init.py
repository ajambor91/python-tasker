import os
import json
user_home_path = os.path.expanduser("~")


def get_app_data(file=None):
    print('()()()()()()()())()()()()())()()()()',user_home_path)
    if isinstance(file, str):
        return os.path.join(user_home_path, 'AppData\\Local\\notes',  file)
    else:
        return os.path.join(user_home_path, 'AppData\\Local\\notes')
def get_path(file):
    __location__ = os.path.realpath(os.path.join(os.getcwd()))
    return  os.path.join(__location__, file)
def get_file(file):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    return  os.path.join(__location__, file)
def get_config():
    config_file_path = get_file('config.json');
    config_file = open(config_file_path)
    config = json.load(config_file)
    return config

def lock_app():
    config = get_config()
    lock_path = os.path.join(user_home_path, config.get('appdataDir'), config.get('lockFileName'))
    try:
        appDataDir = open(lock_path,"x")
    except Exception as e:
        return False
    return True

