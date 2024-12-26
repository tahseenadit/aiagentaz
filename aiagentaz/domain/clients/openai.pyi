from typing import Optional, Dict, Any
from openai.types.chat import ChatCompletion

class OpenAIClient:
    def __init__(self, **kwargs: Dict[str, Any]) -> None: ...

    def generate(
        self,
        prompt: Optional[str] = None,
        model: Optional[str] = None,
        **kwargs: Dict[str, Any]
    ) -> Optional[ChatCompletion.Choice.Message]: ...
