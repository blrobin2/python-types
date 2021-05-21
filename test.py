from app import get_full_name, get_name_with_age


def test_full_name():
    assert get_full_name('john', 'doe') == 'John Doe'


def test_name_with_age():
    assert get_name_with_age('john', 8) == 'john is this old: 8'
