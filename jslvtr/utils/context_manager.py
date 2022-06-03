import sqlite3


class DatabaseConnection():
    def __init__(self, db):
        self._db = db
        self._conn = None

    def __enter__(self):
        self._conn = sqlite3.connect(self._db)
        return self._conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            print('An error ocurred. Rolling back...')
            self._conn.rollback()
        else:
            self._conn.commit()
        self._conn.close()


if __name__ == '__main__':
    name = input("Enter name: ")
    email = input("Enter email: ")
    with DatabaseConnection('data.db') as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users(name text, email text);")
        cursor.execute("INSERT INTO users VALUES(?, ?);", (name, email))
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        for row in result:
            print(f'name: {row[0]}, email: {row[1]}')
