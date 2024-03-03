from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, field_validator
from datetime import datetime
from enum import Enum

class CategoryEnum(str, Enum):
    category1 = "category1"
    category2 = "category2"
    category3 = "category3"

class Sales(BaseModel):
    """
    Data model for class Sales
    Args:
        email (EmailStr): buyer's email
        date (datetime): sale date
        price (PositiveFloat): unit price of the product
        product (str): product description
        quantity (PositiveInt): quantity of products
        category (CategoryEnum): product category
    """
    email: EmailStr
    date: datetime
    price: PositiveFloat
    product: str
    quantity: PositiveInt
    category: CategoryEnum

    @field_validator('category')
    def category_exist_in_enum(cls, error):
        return error
