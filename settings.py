import json

def read_data():
    with open("/home/pi/topf/settings/settings.json", 'r') as read:
        return json.load(read)
    

def write_data(data):
    with open("/home/pi/topf/settings/settings.json", 'w') as write:
        json.dump(data, write, indent=4, separators=(',', ':'))