def test_init(some_keyboard):
    assert str(some_keyboard) == "Dark Project KD87A"

def test_lang(some_keyboard):
    assert some_keyboard.language == "EN"

def test_change_lang(some_keyboard):
    some_keyboard.change_lang()
    assert some_keyboard.language == "RU"
    some_keyboard.change_lang()
    assert some_keyboard.language == "EN"
