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
