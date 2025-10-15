import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "Skypro"),
        ("hello", "Hello"),
        ("test", "Test"),
    ]
)
def test_capitalize_positive(utils, input_str, expected):
    assert utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Skypro", "Skypro"),
        ("", ""),
        ("123abc", "123abc"),
    ]
)
def test_capitalize_negative(utils, input_str, expected):
    assert utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   skypro", "skypro"),
        ("  indented", "indented"),
        ("  mixed", "mixed"),
    ]
)
def test_trim_positive(utils, input_str, expected):
    assert utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "skypro"),
        ("", ""),
        ("already trimmed", "already trimmed"),
    ]
)
def test_trim_negative(utils, input_str, expected):
    assert utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize(
    "string, symbol",
    [
        ("SkyPro", "S"),
        ("Hello, world!", ","),
        ("12345", "3"),
    ]
)
def test_contains_positive(utils, string, symbol):
    assert utils.contains(string, symbol) is True


@pytest.mark.negative
@pytest.mark.parametrize(
    "string, symbol",
    [
        ("SkyPro", "U"),
        ("Hello, world!", "z"),
        ("12345", "9"),
    ]
)
def test_contains_negative(utils, string, symbol):
    assert utils.contains(string, symbol) is False


@pytest.mark.positive
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "k", "SyPro"),
        ("Hello, world!", "o", "Hell, wrld!"),
        ("123123", "3", "1212"),
    ]
)
def test_delete_symbol_positive(utils, string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "z", "SkyPro"),
        ("Hello", "xyz", "Hello"),
        ("", "a", ""),
    ]
)
def test_delete_symbol_negative(utils, string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected
