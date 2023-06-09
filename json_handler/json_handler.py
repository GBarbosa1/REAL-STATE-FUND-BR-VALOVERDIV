import json

def json_load(file):
    with open("settings.json","r") as file:
        jsonData = json.load(file)
    return jsonData
    