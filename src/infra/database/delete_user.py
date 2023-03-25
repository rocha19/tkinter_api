from connection import connect

user = [1]

def deleteUserDb(user: str):
    parseUserIdToList = [user]
    with connect:
        curs = connect.cursor()
        query = 'DELETE FROM user WHERE id=?'
        curs.execute(query, parseUserIdToList)
