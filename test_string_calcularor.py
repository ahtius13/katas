from main import string_calculator

def test_vacio():
    assert string_calculator("") == 0


def test_suma1():
    assert string_calculator("1") == 1


def test_suma2():
    assert string_calculator("1,2") == 3