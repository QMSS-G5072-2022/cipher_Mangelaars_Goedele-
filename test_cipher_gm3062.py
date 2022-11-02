import pytest

def cipher(text, shift, encrypt=True):
    # Question 1d
    assert not isinstance(shift, str)
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            # circular shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text


def test_cipher():
    actual = cipher("hello", 1)
    assert actual == "ifmmp"

def test_cipher_negative():
    actual = cipher("hello", -1)
    assert actual == "gdkkn"

def test_cipher_symbol():
    actual = cipher("hello 8", 1)
    assert actual == "ifmmp 8"

def test_cipher_string():
    with pytest.raises(AssertionError):
        cipher("hello", "three")
    
@pytest.mark.parametrize("example, expected", [
    ('Hello', "Ifmmp"),
    ('bingo', "cjohp"),
    ('SNAKE', "TOBLF"),
    ('Hi Bob', "Ij Cpc"),
])
def test_cipher_multiple_looping_(example, expected):
    result = cipher(example, 1)
    assert result == expected

@pytest.mark.parametrize("shift", range(1, 11))
def test_integration(shift):
    output = cipher("hello", shift)
    assert "hello" == cipher(output, -shift)
