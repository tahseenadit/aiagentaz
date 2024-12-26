from typing import Optional, Dict, Any

class GeminiClient:
    def __init__(self, **kwargs: Dict[str, Any]) -> None: ...

    def generate(
        self, 
        prompt: Optional[str] = None, 
        model: Optional[str] = None, 
        **kwargs: Dict[str, Any]
    ) -> Optional[str]: ... 