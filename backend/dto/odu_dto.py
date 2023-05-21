from pydantic import BaseModel


class OduDto(BaseModel):
    id: int
    string_representation: str

    def __int__(self, id: int, string_representation: str):
        self.id = id
        self.string_representation = string_representation
