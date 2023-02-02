import sqlite3
from vet import Vet


class SqliteDataAccess:
    def __init__(self, db_name: str):
        self.con = sqlite3.connect(db_name)
        self.c = self.con.cursor()

    def create_vet_table(self):
        sql = 'CREATE TABLE vets' \
              ' (id INTEGER PRIMARY KEY AUTOINCREMENT,' \
              'first_name VARCHAR(50),' \
              'last_name VARCHAR(50),' \
              'age INTEGER);'
        self.c.execute(sql)

    def create_vet(self, v:Vet):
        sql = 'INSERT INTO vets (first_name, last_name, age) VALUES (?, ?, ?)'
        self.c.execute(sql, (v.first_name, v.last_name, v.age))
        self.con.commit()