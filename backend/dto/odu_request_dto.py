from pydantic import BaseModel


class OduRequestDto(BaseModel):
    odu_id: int
    x0: float
    y0: float
    interval_length: float
    step: float
    eps: float
