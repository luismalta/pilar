from typing import List
from fastapi import APIRouter
from pilar.models.SortModel import SortModel
from pilar.utils import sort_words

router = APIRouter()


@router.post("/sort")
async def sort(data: SortModel) -> List[str]:
    """
    Sorts a list of words in ascending or descending.

    Args:
        data (SortModel): The request data containing a list of words and
            whether to sort in ascending or descending order.

    Returns:
        List[str]: The sorted list of words.
    """
    return sort_words(data.words, data.order)
