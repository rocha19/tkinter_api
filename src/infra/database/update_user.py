from connection import connect

def updateUserDb(user: list):
    print(user)
    with connect:
        curs = connect.cursor()
        query = 'UPDATE user SET name=?, email=?, phone=?, date_at=?, state=?, observation=? WHERE id=?'
        curs.execute(query, user)
