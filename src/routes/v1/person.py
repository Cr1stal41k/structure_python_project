from fastapi import APIRouter

from repository.crud import (create_person, delete_persons_by_id, get_persons,
                             get_persons_by_name, update_persons_by_id)
from repository.schemas import PersonSchema

router = APIRouter(
    prefix='/persons',
    tags=['persons'],
    responses={404: {'description': 'Not found'}},
)

# Обработка GET-запроса с параметром пути
@router.get('/persons/')
def get_person():
    return get_persons()


# Обработка GET-запроса с параметром пути
@router.get('/persons/{name}')
def get_person(name: str):
    return get_persons_by_name(name)


# Обработка POST-запроса с JSON-данными
@router.post('/persons/')
def create_persons(person: PersonSchema):
    return create_person(person)


# Обработка PUT-запроса для обновления данных
@router.put('/persons/{id}')
def update_person(id: str, person: PersonSchema):
    return update_persons_by_id(id, person)


# Обработка DELETE-запроса
@router.delete('/persons/{id}')
def delete_person(id: int):
    return delete_persons_by_id(id)
