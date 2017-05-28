from db import Connection
import json
import random

with open("settings.json") as settings_file:
    settings = json.load(settings_file)

db = settings['db']
pool = []
max_connections = int(settings['max_connections'])

def get_connection():
    # temporary so
    # should create new connection or return existed one if the pool of connections is exceeded
    if len(pool) > max_connections:
        return random.choice(pool)

    connection = Connection(db['name'], db['username'], db['password'], db['host'], db['port'])
    pool.append(connection)
    return connection
