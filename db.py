import psycopg2

class Connection:
    def __init__(self, db_name, user, password='', host='localhost', port='5432'):
        connect_str = "dbname='%s' user='%s' host='%s' port='%s' password='%s'" % (
                          db_name,
                          user,
                          host,
                          port,
                          password
                      )
        try:
            conn = psycopg2.connect(connect_str)
            cursor = conn.cursor()
            self.execute = cursor.execute
        except Exception as e:
            print("Cannot connect. Invalid dbname, username or password!")
            print(e)



#try:
#    connect_str = "dbname='dzhakhar_db' user='dzhakhar' host='localhost' " + \
#                  "password='qwerty123'"
#    conn = psycopg2.connect(connect_str)
#    cursor = conn.cursor()
#    cursor.execute("""CREATE TABLE tutorials (name char(40));""")
#    cursor.execute("""SELECT * FROM tutorials;""")
#    rows = cursor.fetchall()
#    print(rows)
#except Exception as e:
#    print("Can't connect. Invalid dbname, user or password?")
#    print(e)
