class Pet:
    def __init__(self, first_name: str, race: str, year: int, owner: id, id: int = 0):
        self.first_name = first_name
        self.race = race
        self.year = year
        self.owner = owner
        self.id = id

    def __repr__(self) -> str:
        return f'{self.id} {self.first_name} {self.race} {self.year} {self.owner}'

    def __eq__(self, other):
        return self.id == other.id and self.first_name == other.first_name and self.race == other.race and self.year == other.year and self.owner == other.owner