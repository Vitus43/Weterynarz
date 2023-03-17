class Vet:
    def __init__(self, first_name: str, last_name: str, age: int, id: int = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.id = id

    def __eq__(self, other):
        return self.id == other.id and self.first_name == other.first_name and self.last_name == other.last_name and self.age == other.age

    def __repr__(self)-> str:
        return f'{self.id} {self.first_name} {self.last_name} {self.age}'

