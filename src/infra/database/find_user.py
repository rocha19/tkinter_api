from connection import connect

def findUsers():
    users = []
    with connect:
        curs = connect.cursor()
        query = 'SELECT * FROM user'
        curs.execute(query)
        info = curs.fetchall()
        for index in info:
            users.append(index)
    return users
