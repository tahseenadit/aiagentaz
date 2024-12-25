from typing import Any

class Agent:
    client: str
    client_kwargs: dict[str, Any]
    
    def __init__(self, client: str, /, **kwargs: Any) -> None: ...
