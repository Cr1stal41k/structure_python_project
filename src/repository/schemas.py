# Добавляем скачанные библиотеки
from pydantic import BaseModel


class TunedModel(BaseModel):
    class Config:
        orm_mode = True


class PersonSchema(TunedModel):
    _id: int = None
    name: str
    second_name: str
    number: str


class FilmSchema(TunedModel):
    _id: int = None
    name: str
    director: int
