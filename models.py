from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Схемы для таблицы "Пользователи"
class UserCreateSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class UserReadSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True

# Схемы для таблицы "Товары"
class ProductCreateSchema(BaseModel):
    name: str
    description: str
    price: float

class ProductReadSchema(BaseModel):
    id: int
    name: str
    description: str
    price: float

    class Config:
        orm_mode = True

# Схемы для таблицы "Заказы"
class OrderCreateSchema(BaseModel):
    user_id: int
    product_id: int
    order_date: datetime
    status: str

class OrderReadSchema(BaseModel):
    id: int
    user_id: int
    product_id: int
    order_date: datetime
    status: str

    class Config:
        orm_mode = True
