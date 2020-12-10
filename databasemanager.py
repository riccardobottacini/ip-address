import sqlite3
import random
import os
import argparse
import hashlib

conn = None
cursor = None

def db_creation(path):

    global conn
    global cursor
    conn=sqlite3.connect(path)
    cursor=conn.cursor()
    try:
        cursor.execute("SELECT * FROM users")
    # if the table does not exist create one
    except:
        cursor.execute('''CREATE TABLE users
                       (username VARCHAR(255) NOT NULL,
                        password VARCHAR(255) NOT NULL,
                        salt VARCHAR(255) NOT NULL,
                        PRIMARY KEY (username))''')

def save_new_username(username, password):

    global conn
    global cursor

    salt = str(random.random())
    digest = salt + password
    for i in range(1000):
        digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()
    cursor.execute("INSERT OR REPLACE INTO users VALUES (?,?,?)",
                   (username, digest, salt))
    print("The registration has been successful")
    conn.commit()


def check_for_username(username, password):

    global conn
    global cursor
    row = cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    results = row.fetchall()
    salt = str(results[0][2])
    digest = salt + password
    for i in range(1000):
        digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()
    if digest == results[0][1]:
        return True
    else:
        return False
    conn.commit()

def parse_args():
    """Parse user inputs: username and password."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help="add a username (requires -p)",
                        required=False)
    parser.add_argument('-p', help="the username password",
                        required=True)

    return parser.parse_args()

if __name__ == "__main__":
    path = "data/database.db"
    args = parse_args()
    db_creation(path)
    if args.a and args.p:
        save_new_username(args.a, args.p)
    conn.close()