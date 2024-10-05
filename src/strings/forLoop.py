
from typing import Callable


def forLoop(text: str, callBack: Callable[[str], str]) -> str:
    result: str = ""
    for letter in text:
        result += callBack(letter)
    return result