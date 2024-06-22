from typing import List

from pydantic import BaseModel


class VowelCountModel(BaseModel):
    """
    VowelCountModel is a class that represents the request data for counting
     the number of vowels in a list of words.
    """

    words: List[str]
