from fastapi import APIRouter

from schemas.schema_input import Item

router = APIRouter(
    prefix='/methods',
    tags=['DefaultRouter'],
    responses={404: {'description': 'Not found'}},
)

# Обработка GET-запроса с параметром пути
@router.get('/items/{item_id}')
def get_item(item_id: int, q: str = None):
    return {'item_id': item_id, 'q': q}


# Обработка POST-запроса с JSON-данными
@router.post(
    '/items/',
    summary='Получить информацию о предмете',
    description='Возвращает информацию о предмете по ID',
)
def create_item(item: Item):
    return {'name': item.name, 'price': item.price}


# Обработка PUT-запроса для обновления данных
@router.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {'item_id': item_id, 'name': item.name, 'price': item.price}


# Обработка DELETE-запроса
@router.delete('/items/{item_id}')
def delete_item(item_id: int):
    return {'message': f'Item {item_id} has been deleted'}
