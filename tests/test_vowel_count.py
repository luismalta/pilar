import pytest
from pilar.utils import count_vowels

test_cases = [
    ("batman", 2),
    ("robin", 2),
    ("coringa", 3),
]


@pytest.mark.parametrize("case, expected_result", test_cases)
def test_count_vowels_correctly(case: str, expected_result: int):
    """
    Test case to verify if the count_vowels function returns the correct result
    """
    result = count_vowels(case)
    assert result == expected_result
