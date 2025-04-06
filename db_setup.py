import sqlite3

def create_database():
    conn = sqlite3.connect('app/database/ecommerce.db')
    with open('schema.sql', 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("Database created successfully.")

if __name__ == '__main__':
    create_database()
