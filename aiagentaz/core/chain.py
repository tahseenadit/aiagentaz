import inspect
from typing import Callable

class Chain:
    """Chain class for handling chain of prompts."""
    
    def __init__(self, res: str = None):
        self.res = res

    def has_keyword_argument(self, func: Callable, keyword: str) -> bool:
        """Check if the function has a keyword argument."""
        return keyword in inspect.signature(func).parameters
    
    def decorate(self, *args, **kwargs):
        """Decorate the function with the previous response."""
        if args and callable(args[0]):
            func = args[0]
            kwargs = kwargs.copy()
            kwargs["previous_response"] = self.res
            if self.has_keyword_argument(func, "previous_response"):
                res = func(*args[1:], **kwargs)
                chain = Chain(res)
                return chain.decorate
            else:
                raise ValueError(f"The function {func.__name__} must have a 'previous_response' keyword argument.")
        
