"""Здесь надо написать тесты с использованием pytest для модуля Phone."""

def test_phone(some_phone):
    assert some_phone.name == "Nokia"
    assert some_phone.price == 2_000
    assert some_phone.quantity == 3
    assert some_phone.number_of_sim == 89143556677

def test_number_of_sim(some_phone):
    assert some_phone.number_of_sim == 89143556677

def test_str(some_phone):
    assert str(some_phone) == "Nokia"

def test_repr(some_phone):
    assert repr(some_phone) == "Phone('Nokia', 2000, 3, 89143556677)"