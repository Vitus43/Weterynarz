class Procedure:
    def __init__(self, name: str, id: int = 0):
        self.name = name
        self.id = id

    def __repr__(self) -> str:
        return f'{self.id} {self.name}'

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

