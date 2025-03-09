from pydantic import BaseModel

# Определим модель для данных, которые будем получать через POST-запрос
class Item(BaseModel):
    name: str
    description: str = None
    price: float