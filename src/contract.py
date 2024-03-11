from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, field_validator
from datetime import datetime
from enum import Enum

class CategoryEnum(str, Enum):
    category1 = "category1"
    category2 = "category2"
    category3 = "category3"

class Sales(BaseModel):
    """
    Data model for class Sales.

    Args:
        email (EmailStr): Buyer's email
        date (datetime): Sale date
        price (PositiveFloat): Unit price of the product
        product (str): Product description
        quantity (PositiveInt): Quantity of products
        category (CategoryEnum): Product category
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
