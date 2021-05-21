from app import get_full_name, get_name_with_age, get_items, process_items


def test_full_name():
    assert get_full_name('john', 'doe') == 'John Doe'


def test_name_with_age():
    assert get_name_with_age('john', 8) == 'john is this old: 8'


def test_items():
    assert get_items('a', 1, 1.5, True, b'101') == ('a', 1, 1.5, True, b'101')


def test_process_items(capsys):
    process_items(['list', 'of', 'words'])
    captured = capsys.readouterr()
    assert captured.out == "list\nof\nwords\n"
