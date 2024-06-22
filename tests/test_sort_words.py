from pilar.utils import sort_words

words = ["batman", "Robin", "coringa"]


def test_sort_words_acending_correctly():
    """
    Test case to verify if the sort_words function correctly sorts a list of
        words in acsending order ignoring case.
    """

    expected_result = ["batman", "coringa", "Robin"]

    result = sort_words(words, 'asc')

    assert result == expected_result


def test_sort_words_descending_correctly():
    """
    Test case to verify if the sort_words function correctly sorts a list of
        words in descending order ignoring case.
    """

    expected_result = ["Robin", "coringa", "batman"]

    result = sort_words(words, 'desc')

    assert result == expected_result
