import unittest
from SqliteDataAccess import SqliteDataAccess
import os
from vet import Vet
from Owner import Owner
from Pet import Pet


class TestVetCrud(unittest.TestCase):

    def setUp(self):
        self.s = SqliteDataAccess('test.db')
        self.s.create_vet_table()

    def tearDown(self):
        self.s.con.close()
        os.remove('test.db')
    def test_create_vet(self):
        v = Vet('Karol', 'Kowalski', 43, 1)
        self.s.create_vet(v)
        c = self.s.read_vet(1)
        print(v, c)
        self.assertEqual(v, c)

    def test_update_vet(self):
        v = Vet('Karol', 'Kowalski', 43, 1)
        self.s.create_vet(v)
        v.age = 44
        self.s.update_vet(v)
        c = self.s.read_vet(1)
        self.assertEqual(v, c)

    def test_delete_vet(self):
        v = Vet(id=1, first_name='Karol', last_name='Kowalski', age=43)
        self.s.create_vet(v)
        vets_before = self.s.read_all_vets()
        self.s.delete_vet(1)
        vets_after = self.s.read_all_vets()
        self.assertEqual(len(vets_before), len(vets_after) + 1)


class TestOwnerCrud(unittest.TestCase):

    def setUp(self):
        self.s = SqliteDataAccess('test.db')
        self.s.create_owner_table()

    def tearDown(self):
        self.s.con.close()
        os.remove('test.db')

    def test_create_owner(self):
        o = Owner('Jan', 'Baczewski', 31, '1995-03-11', 1)
        self.s.create_owner(o)
        c = self.s.read_owner(1)
        print(o, c)
        self.assertEqual(o, c)

    def test_update_owner(self):
        o = Owner('Jan', 'Baczewski', 31, '1995-03-11', 1)
        self.s.create_owner(o)
        o.age = 44
        self.s.update_owner(o)
        c = self.s.read_owner(1)
        self.assertEqual(o, c)

    def test_delete_owner(self):
        o = Owner('Jan', 'Baczewski', 31, '1995-03-11', 1)
        self.s.create_owner(o)
        owners_before = self.s.read_all_owners()
        self.s.delete_owner(1)
        owners_after = self.s.read_all_owners()
        self.assertEqual(len(owners_before), len(owners_after) + 1)

class TestPetCrud(unittest.TestCase):

    def setUp(self):
        self.s = SqliteDataAccess('test.db')
        self.s.create_owner_table()
        self.s.create_pet_table()

    def tearDown(self):
        self.s.con.close()
        os.remove('test.db')

    def test_create_pet(self):
        o = Owner('Jan', 'Baczewski', 31, '1995-03-11', 1)
        self.s.create_owner(o)
        p = Pet('Bazyl', 'chomik', 2001, 1, 1)
        self.s.create_pet(p)
        c = self.s.read_pet(1)
        print(p, c)
        self.assertEqual(p, c)

    def test_update_pet(self):
        o = Owner('Jan', 'Baczewski', 31, '1995-03-11', 1)
        self.s.create_owner(o)
        o1 = Owner('Kacper', 'Warzyń', 31, '1995-03-11', 2)
        self.s.create_owner(o1)
        p = Pet('Bazyl', 'chomik', 2001, 1, 1)
        self.s.create_pet(p)
        p.first_name = 'Mateusz'
        p.race = 'kogut'
        p.year = 2002
        p.owner = 2
        self.s.update_pet(p)
        c = self.s.read_pet(1)
        f = self.s.read_owner(c.owner)
        self.assertEqual(f, o1)

    def test_delete_pet(self):
        o = Owner('Jan', 'Baczewski', 31, '1995-03-11', 1)
        self.s.create_owner(o)
        p = Pet('Bazyl', 'chomik', 2001, 1, 1)
        self.s.create_pet(p)
        pets_before = self.s.read_all_pets()
        self.s.delete_pet(1)
        pets_after = self.s.read_all_pets()
        self.assertEqual(len(pets_after) + 1, len(pets_before))


class TestOwnerFilter(unittest.TestCase):

    def setUp(self):
        self.s = SqliteDataAccess('test.db')
        self.s.create_owner_table()
        self.populate_owner_table()

    def tearDown(self):
        self.s.con.close()
        os.remove('test.db')

    def populate_owner_table(self):
        o = [Owner('Jan', 'Baczewski', 31, '1995-03-11', 1),
             Owner('Kacper', 'Warzyń', 31, '1995-03-11', 2),
             Owner('Bartek', 'Garnek', 22, '2003-12-30', 3),
             Owner('Kamil', 'Kolega', 19, '2005-02-04', 4),
             Owner('Krzysztof', 'Brzęczyszczykiewicz', 66, '1963-04-17', 5),
             Owner('Bogumił', 'Lotny', 34, '1994-03-01', 6),
             Owner('Maciej', 'Wysokodrzewny', 52, '1982-07-19', 7),
             Owner('Stanisław', 'Wróbel', 44, '1999-11-15', 8),
             Owner('Konrad', 'Piękny', 27, '2003-06-29', 9)]
        for i in o:
            self.s.create_owner(i)

    def test_get_owner_by_age(self):
        os = self.s.get_owner_by_age(31)
        self.assertEqual(len(os), 2)

    def test_get_owner_by_age_returns_empty_list(self):
        os = self.s.get_owner_by_age(999)
        self.assertEqual(len(os), 0)

    def test_get_owner_by_names_first_letter(self):
        os = self.s.get_owner_by_names_first_letter('K')
        self.assertEqual(len(os), 4)