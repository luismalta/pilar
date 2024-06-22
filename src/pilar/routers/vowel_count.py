from fastapi import APIRouter

from pilar.models.VowelCountModel import VowelCountModel
from pilar.utils import count_vowels

router = APIRouter()


@router.post("/vowel_count")
async def vowel_count(data: VowelCountModel) -> dict:
    """
    Calculates the number of vowels in each word provided in the request data.

    Args:
        data (VowelCountModel): The request data containing a list of words.

    Returns:
        dict: A dictionary where the keys are the words and the values are the
            number of vowels in each word.
    """
    response = {}
    for word in data.words:
        response[word] = count_vowels(word)
    return response
