import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture()
def some_item():
    item = Item("Смартфон", 10_000, 20)
    return item

@pytest.fixture()
def some_phone():
    new_phone = Phone("Nokia", 2_000, 3, 89143556677)
    return new_phone