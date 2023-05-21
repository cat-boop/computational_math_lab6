from dto.odu_dto import OduDto
from entity.odu import Odu


def map(odu: Odu) -> OduDto:
    return OduDto(id=odu.id, string_representation=odu.string_representation)
