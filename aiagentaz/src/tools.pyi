from typing import Callable

class Tool:
    name: str
    fn: Callable

    def __init__(self, name: str, fn: Callable):
        ...