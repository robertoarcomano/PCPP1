"""
1 import sqlite3
    1.1 :memory: in RAM
2 connection
3 get the cursor
4 cursor.execute
    4.1 executemany
5 conn.commit()
6 select: iterator cursor.execute
    6.1 without iterator: cursor.fetchall
"""
import sqlite3


class Database:
    def __init__(self, db_filename):
        self.connection = sqlite3.connect(db_filename)
        self.cursor = self.connection.cursor()

    def create_db(self):
        try:
            self.cursor.execute("create table users(id number, name text)")
        except:
            pass

    def delete(self):
        self.cursor.execute("delete from users")

    def insert(self, n):
        if n == 1:
            self.cursor.execute("insert into users(id, name) values(0,'Roberto');")
        else:
            multi_insert = [(i, "Roberto_" + str(i)) for i in range(1, n)]
            self.cursor.executemany("insert into users(id, name) values (?,?)", multi_insert)

    def update(self):
        self.cursor.execute("update users set name=name || '_updated'")

    def commit(self):
        self.connection.commit()

    def select(self):
        return self.cursor.execute("select * from users")

    def select_no_iterator(self):
        self.select()
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()


db = Database("hello.db")
db.create_db()
db.delete()
db.insert(1)
db.insert(10)

# Updating
db.update()

# Select using the iterator
for row in db.select():
    print(row)

# Select without using the iterator
rows = db.select_no_iterator()
print(rows)

# Select using fetchone
cursor = db.select()
print(cursor.fetchone())
print(cursor.fetchone())

db.commit()
db.close()
