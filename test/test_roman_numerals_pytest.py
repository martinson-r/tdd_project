from app.roman_numerals import parse
from pytest import mark


# def test_roman_numeral_parser():
#     result = parse("IX")
#     assert result == 9


@mark.parametrize("s,expected", [("IX", 9), ("X", 10)])
def test_roman_numeral_parser(s, expected):
    result = parse(s)

    assert result == expected
