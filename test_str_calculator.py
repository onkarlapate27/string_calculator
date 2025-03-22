from str_calculator import add

def test_empty_str_input():
    assert add("") == 0

def test_single_digit_str_input():
    assert add("2") == 2

def test_double_digits_str_input():
    assert add("2, 7") == 9

def test_n_digits_str_input():
    assert add("2, 7, 4, 6, 7, 8") == 34

def test_digits_with_spaces_input():
    assert add("     2, 7,     10") == 19

def test_digits_separated_by_newline_char_input():
    assert add("2, 7, 8\n 8") == 25