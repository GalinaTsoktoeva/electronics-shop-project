import pytest
from src.item import Item
from src.phone import Phone
from src.keyboard import KeyBoard


@pytest.fixture()
def some_item():
    item = Item("Смартфон", 10_000, 20)
    return item

@pytest.fixture()
def some_phone():
    new_phone = Phone("Nokia", 2_000, 3, 89143556677)
    return new_phone

@pytest.fixture()
def some_keyboard():
    new_keyboard = KeyBoard('Dark Project KD87A', 9600, 5)
    return new_keyboard