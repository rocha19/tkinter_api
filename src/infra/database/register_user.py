from connection import connect


def registerUser(user: list):
    with connect:
        curs = connect.cursor()
        curs.execute(
            'CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, phone TEXT, date_at DATE, state TEXT, observation TEXT)'
            )
        
        query = 'INSERT INTO user (name, email, phone, date_at, state, observation) VALUES (?, ?, ?, ?, ?, ?)'
        curs.execute(query, user)

# user = [
#     'John Doe', 
#     'upchh@example.com', 
#     '1234567890', 
#     '2020-01-01', 
#     'New York',
#     'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation'
#     ]
