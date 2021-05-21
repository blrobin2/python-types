from app import get_full_name, \
    get_name_with_age, \
    get_items, \
    process_items, \
    process_items2, \
    process_prices, \
    say_hi


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


def test_process_items2():
    items = process_items2((1, 2, 'three'), {b'101', b'202'})
    assert items == ((1, 2, 'three'), {b'101', b'202'})


def test_process_prices(capsys):
    process_prices(dict(apple=2.0, pear=4.3))
    captured = capsys.readouterr()
    assert captured.out == "apple : 2.0\npear : 4.3\n"


def test_say_hi(capsys):
    say_hi("jeff")
    say_hi()
    captured = capsys.readouterr()
    assert captured.out == "Hey Jeff!\nHello World!\n"
