from aiagentaz.core.chain import Chain
from typing import Callable

def chain(*args, **kwargs) -> Callable:
    """Chain the functions together."""
    if args and callable(args[0]):
        func = args[0]
        res = func(*args[1:], **kwargs)
        chain = Chain(res)
        return chain.decorate
    else:
        raise ValueError("First argument must be a callable function.")
