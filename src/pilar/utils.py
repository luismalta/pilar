from typing import List, Literal


def count_vowels(word: str) -> int:
    """
    Count the number of vowels in a given word.

    Args:
        word (str): The word to count the vowels in.

    Returns:
        int: The number of vowels in the word.
    """
    vowels_count = 0
    for letter in word:
        if letter.lower() in "aeiou":
            vowels_count += 1
    return vowels_count


def sort_words(words: List[str], order: Literal['asc', 'desc']) -> List[str]:
    """
    Sorts a list of words in ascending or descending order ignoring case.

    Args:
        words (List[str]): The list of words to sort.

    Returns:
        List[str]: The sorted list of words.
    """

    return sorted(words, key=str.casefold, reverse=order == 'desc')
