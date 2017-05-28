from root import get_connection

class Model:
    def __init__(self, name):
        self.connection = get_connection()
        self.execute = self.connection.execute


for i in range(150):
    print(str(i) + ':')
    print(Model('Dzh').__dict__['connection'])
