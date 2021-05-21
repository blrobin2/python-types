from app import get_full_name

def test_full_name():
  assert get_full_name('john', 'doe') == 'John Doe'
