from SqliteDataAccess import SqliteDataAccess
from vet import Vet


s = SqliteDataAccess('db.db')
v1 = Vet('Karol', 'Kowalski', 43)
v2 = Vet('Bogumił', 'Piękny', 19)
v3 = Vet('Kazimiera', 'Duda', 75)
s.create_vet(v1)
s.create_vet(v2)
s.create_vet(v3)