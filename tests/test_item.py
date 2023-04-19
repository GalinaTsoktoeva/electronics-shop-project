"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item(some_item):
    assert some_item.name == "Смартфон"
    assert some_item.price == 10000
    assert some_item.quantity == 20

def test_calculate_total_price(some_item):
    assert some_item.calculate_total_price() == 200_000

def test_apply_discount(some_item):
    some_item.pay_rate = 0.8
    some_item.apply_discount()
    assert some_item.price == 8_000

def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_repr(some_item):
    assert repr(some_item) == "Item('Смартфон', 10000, 20)"

def test_str(some_item):
    assert str(some_item) == 'Смартфон'

def test_setter(some_item):
    some_item.name = "Rabbit"
    assert some_item.name == "Rabbit"

def test_add(some_item):
    assert some_item + some_item == 40