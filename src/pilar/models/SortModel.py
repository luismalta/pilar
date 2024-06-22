from typing import List, Literal
from pydantic import BaseModel


class SortModel(BaseModel):
    """
    SortModel is a class that represents the request data for sorting a
        list of words
    """
    words: List[str]
    order: Literal['asc', 'desc']
