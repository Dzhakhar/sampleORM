from db import Connection
import json

with open("settings.json") as settings_file:
    settings = json.load(settings_file)

db = settings['db']
connection = Connection(db['name'], db['username'], db['password'], db['host'], db['port'])

print(connection.__dict__)
