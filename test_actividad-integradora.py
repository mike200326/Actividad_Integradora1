import pytest
from Actividad_Integradora import contains_code
from Actividad_Integradora import find_longest_palindrome
from Actividad_Integradora import longest_common_substring
from Actividad_Integradora import read_file

transmission1 = read_file('transmission1_content.txt')
transmission2 = read_file('transmission2_content.txt')
mcode1 = read_file('mcode1_content.txt')
mcode2 = read_file('mcode2_content.txt')
mcode3 = read_file('mcode3_content.txt')

def test_contains_code():
    assert contains_code(transmission1, mcode1) == 'true 27'
    assert contains_code(transmission1, mcode2) == 'false'
    assert contains_code(transmission1, mcode3) == 'false'
    assert contains_code(transmission2, mcode1) == 'false'
    assert contains_code(transmission2, mcode2) == 'false'
    assert contains_code(transmission2, mcode3) == 'false'

def test_find_longest_palindrom():
    assert find_longest_palindrome(transmission1) == '11 14' # Palìndromo: 0AA0
    assert find_longest_palindrome(transmission2) == '10 12' # Palindromo: E6E

def test_longest_common_substring():
    assert longest_common_substring(transmission1, transmission2) == '21 22'

if __name__ == "__main__":
    pytest.main()