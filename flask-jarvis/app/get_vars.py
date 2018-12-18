import json

PATH = "/home/flask/config.json"
PATH = "/home/centos/config.json"

def my_vars(key, path=PATH):
    with open(path) as f:
        data = json.load(f)
    return data['vars'][key]
