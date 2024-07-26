import sqlite3
import hashlib

class db():
    def __init__(self,username,password,apiKey):
        self.username = username
        self.password = password
        self.key = apiKey
        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL ,
                key TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def hash_password(self):
        return hashlib.sha256(self.password.encode()).hexdigest()

    def register_user(self):
        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()

        hashed_password = self.hash_password()

        try:
            c.execute('INSERT INTO users (username, password ,key) VALUES (?, ?, ?)', (self.username, hashed_password ,self.key))
            conn.commit()
            print("User registered successfully.")
        except sqlite3.IntegrityError:
            print("Username already exists.")

        conn.close()

    def login_user(self):
        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()
        hashed_password = self.hash_password()

        c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (self.username, hashed_password))
        user = c.fetchone()
        conn.close()
        if user:
            return True
        else:
            return False

    def update_user_key(self):
        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()
        hashed_password = self.hash_password()
        c.execute('''
            UPDATE users
            SET key = ?
            WHERE username = ? AND password = ?
        ''', (self.key, self.username, hashed_password))

    def getUserKey(self):
        conn = sqlite3.connect('user_data.db')
        c = conn.cursor()
        hashed_password = self.hash_password()
        c.execute('''
                    SELECT key
                    FROM users
                    WHERE username = ? AND password = ?
                ''', (self.username, hashed_password))
        key = c.fetchone()
        return key



if __name__ == "__main__":
    database = db("ali","lordali","sk-None-gJTETjgbTZ6wn7Y")
    if not database.login_user():
        database.register_user()


