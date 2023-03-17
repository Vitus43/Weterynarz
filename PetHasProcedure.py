class PetHasProcedure:
    def __init__(self, pet_id: int, procedure_id: int, date: str):
        self.pet_id = pet_id
        self.procedure_id = procedure_id
        self.date = date

    def __repr__(self) -> str:
        return f'{self.pet_id} {self.procedure_id} {self.date}'

    def __eq__(self, other):
        return self.pet_id == other.pet_id and self.procedure_id == other.procedure_id and self.date == other.date
