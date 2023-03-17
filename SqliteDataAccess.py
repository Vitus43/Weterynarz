import sqlite3
from vet import Vet
from Owner import Owner
from Pet import Pet
from Procedure import Procedure
from PetHasProcedure import PetHasProcedure


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

    def create_vet(self, v: Vet):
        sql = 'INSERT INTO vets (first_name, last_name, age) VALUES (?, ?, ?)'
        self.c.execute(sql, (v.first_name, v.last_name, v.age))
        self.con.commit()

    def read_vet(self, id: int) -> Vet:
        sql = 'SELECT * FROM vets WHERE id = ?'
        self.c.execute(sql, (id,))
        data = self.c.fetchone()
        vet = Vet(data[1], data[2], data[3], data[0])
        return vet

    def update_vet(self, v: Vet):
        sql = 'UPDATE vets SET first_name = ?, last_name = ?, age = ? WHERE id = ?'
        self.c.execute(sql, (v.first_name, v.last_name, v.age, v.id))
        self.con.commit()

    def read_all_vets(self) -> list:
        sql = 'SELECT * FROM vets'
        vets = []
        for row in self.c.execute(sql):
            v = Vet(row[1], row[2], row[3], row[0])
            vets.append(v)
        return vets

    def delete_vet(self, id: int):
        sql = 'DELETE FROM vets WHERE id = ?'
        self.c.execute(sql, (id,))
        self.con.commit()

    # OWNER


    def create_owner_table(self):
        sql = 'CREATE TABLE owners' \
              ' (id INTEGER PRIMARY KEY AUTOINCREMENT,' \
              'first_name VARCHAR(50),' \
              'last_name VARCHAR(50),' \
              'age INTEGER,' \
              'date_joined DATE);'
        self.c.execute(sql)

    def create_owner(self, o: Owner):
        sql = 'INSERT INTO owners (first_name, last_name, age, date_joined) VALUES (?, ?, ?, ?)'
        self.c.execute(sql, (o.first_name, o.last_name, o.age, o.date_joined))
        self.con.commit()

    def read_owner(self, id: int) -> Owner:
        sql = 'SELECT * FROM owners WHERE id = ?'
        self.c.execute(sql, (id,))
        data = self.c.fetchone()
        owner = Owner(data[1], data[2], data[3], data[4], data[0])
        return owner

    def update_owner(self, o: Owner):
        sql = 'UPDATE owners SET first_name = ?, last_name = ?, age = ? WHERE id = ?'
        self.c.execute(sql, (o.first_name, o.last_name, o.age, o.id))
        self.con.commit()

    def read_all_owners(self) -> list:
        sql = 'SELECT * FROM owners'
        owners = []
        for row in self.c.execute(sql):
            o = Owner(row[1], row[2], row[3], row[4], row[0])
            owners.append(o)
        return owners

    def delete_owner(self, id: int):
        sql = 'DELETE FROM owners WHERE id = ?'
        self.c.execute(sql, (id,))
        self.con.commit()


    # OWNER FILTROWANIE


    def get_owner_by_age(self, age: int) -> list:
        sql = 'SELECT * FROM owners WHERE age = ?'
        owners = []
        for row in self.c.execute(sql, (age,)):
            o = Owner(row[1], row[2], row[3], row[4], row[0])
            owners.append(o)
        return owners

    def get_owner_by_names_first_letter(self, l: str) ->list:
        sql = f'SELECT * FROM owners WHERE first_name LIKE "{l}%"'
        owners = []
        for row in self.c.execute(sql):
            o = Owner(row[1], row[2], row[3], row[4], row[0])
            owners.append(o)
        return owners


    # PET


    def create_pet_table(self):
        sql = 'CREATE TABLE pets' \
              ' (id INTEGER PRIMARY KEY AUTOINCREMENT,' \
              'first_name VARCHAR(50),' \
              'race VARCHAR(50),' \
              'year INTEGER,' \
              'owner_id INTEGER NOT NULL, ' \
              'FOREIGN KEY(owner_id) REFERENCES owners(id));'
        self.c.execute(sql)

    def create_pet(self, p: Pet):
        sql = 'INSERT INTO pets (first_name, race, year, owner_id) VALUES (?, ?, ?, ?)'
        self.c.execute(sql, (p.first_name, p.race, p.year, p.owner))
        self.con.commit()

    def read_pet(self, id: int) -> Pet:
        sql = 'SELECT * FROM pets WHERE id = ?'
        self.c.execute(sql, (id,))
        data = self.c.fetchone()
        pet = Pet(data[1], data[2], data[3], data[4], data[0])
        return pet

    def update_pet(self, p: Pet):
        sql = 'UPDATE pets SET first_name = ?, race = ?, year = ?, owner_id = ? WHERE id = ?'
        self.c.execute(sql, (p.first_name, p.race, p.year, p.owner, p.id))
        self.con.commit()

    def read_all_pets(self) -> list:
        sql = 'SELECT * FROM pets'
        pets = []
        for row in self.c.execute(sql):
            p = Pet(row[1], row[2], row[3], row[4], row[0])
            pets.append(p)
        return pets

    def delete_pet(self, id: int):
        sql = 'DELETE FROM pets WHERE id = ?'
        self.c.execute(sql, (id,))
        self.con.commit()


    #PROCEDURE


    def create_procedure_table(self):
        sql = 'CREATE TABLE procedure' \
              ' (id INTEGER PRIMARY KEY AUTOINCREMENT,' \
              'name VARCHAR(50))'
        self.c.execute(sql)

    def create_procedure(self, p: Procedure):
        sql = 'INSERT INTO procedure (name) VALUES (?)'
        self.c.execute(sql, (p.name,))
        self.con.commit()

    def read_procedure(self, id: int)-> Procedure:
        sql = 'SELECT * FROM procedure WHERE id = ?'
        self.c.execute(sql, (id,))
        data = self.c.fetchone()
        procedure = Procedure(data[1], data[0])
        return procedure

    def update_procedure(self, p: Procedure):
        sql = 'UPDATE procedure SET name = ? WHERE id = ?'
        self.c.execute(sql, (p.name,))
        self.con.commit()

    def read_all_procedures(self)-> list:
        sql = 'SELECT * FROM procedure'
        procedures = []
        for row in self.c.execute(sql):
            p = Procedure(row[1], row[0])
            procedures.append(p)
        return procedures

    def delete_procedure(self, id: int):
        sql = 'DELETE FROM procedure WHERE id = ?'
        self.c.execute(sql, (id,))
        self.con.commit()


    #PetHasProcedure


    def create_pethasprocedure_table(self):
        sql = 'CREATE TABLE pethasprocedure' \
              '(pet_id INTEGER, ' \
              'procedure_id INTEGER, ' \
              'date DATE, ' \
              'FOREIGN KEY (pet_id) REFERENCES pets(id), ' \
              'FOREIGN KEY (procedure_id) REFERENCES procedure(id), ' \
              'PRIMARY KEY (pet_id, procedure_id, date)'
        self.c.execute(sql)

    def create_pethasprocedure(self,p: PetHasProcedure ):
        sql = 'INSERT INTO pethasprocedure (pet_id, procedure_id, date) VALUES (?, ?, ?)'
        self.c.execute(sql, (p.pet_id, p.procedure_id, p.date))
        self.con.commit()

    def read_all_pethasprocedure(self):
        sql = 'SELECT * FROM pethasprocedure'
        pethasprocedure = []
        for row in self.c.execute(sql):
            p = PetHasProcedure(row[0], row[1], row[2])
            pethasprocedure.append(p)
        return pethasprocedure

