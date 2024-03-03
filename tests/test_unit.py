from pydantic import ValidationError
import pytest
from datetime import datetime
from src.contract import Sales, CategoryEnum

def test_sale_with_valid_data():

    valid_data = {
        "email": "buyer@example.com",
        "date": datetime.now(),
        "price": 100.5,
        "product": "Product X",
        "qty": 3,
        "category": "category3"
    }

    sale = Sales(**valid_data)

    assert sale.email == valid_data["email"]
    assert sale.date == valid_data["date"]
    assert sale.price == valid_data["price"]
    assert sale.product == valid_data["product"]
    assert sale.qty == valid_data["qty"]
    assert sale.category == valid_data["category"]

def test_sale_with_invalid_data():

    invalid_data = {
        "email": "buyer",
        "date": "not date",
        "price": -100.5,
        "product": "",
        "qty": -1,
        "category": "categoria3"
    }

    with pytest.raises(ValidationError):
        Sales(**invalid_data)

def test_validation_category():
    data = {
        "email": "buyer@example.com",
        "date": datetime.now(),
        "price": 100.5,
        "product": "Product X",
        "qty": 3,
        "category": "non existent category"
    }

    with pytest.raises(ValidationError):
        Sales(**data)