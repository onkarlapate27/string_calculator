from str_calculator import add

def test_empty_str_input():
    assert add("") == 0

def test_single_digit_str_input():
    assert add("2") == 2