class Owner:
    def __init__(self, first_name: str, last_name: str, age: int, date_joined: str, id: int = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.date_joined = date_joined
        self.id = id

    def __repr__(self) -> str:
        return f'{self.id} {self.first_name} {self.last_name} {self.age} {self.date_joined}'

    def __eq__(self, other):
        return self.id == other.id and self.first_name == other.first_name and self.last_name == other.last_name and self.age == other.age and self.date_joined == other.date_joined