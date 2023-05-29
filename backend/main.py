from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dto.odu_request_dto import OduRequestDto
from dto.odu_response_dto import OduResponseDto
from service import odu_service

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
async def root():
    return "pong"


@app.get("/get_available_functions")
async def root():
    return odu_service.get_available_odu_dtos()


@app.post("/find_best_similar", response_model=OduResponseDto)
async def root(odu_request_dto: OduRequestDto):
    print(odu_request_dto)
    try:
        return odu_service.find_best_similar(odu_request_dto.odu_id, odu_request_dto.x0, odu_request_dto.y0,
                                             odu_request_dto.interval_length, odu_request_dto.step, odu_request_dto.eps)
    except (ZeroDivisionError, OverflowError) as error:
        return OduResponseDto(enhanced_eiler=[], runge_kutta=[], miln=[], perfect_solution=[], x_range=[], y_range=[])
