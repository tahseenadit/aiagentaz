from typing import Literal, Any, ContextManager, overload

from aiagentaz.src.clients.openai import OpenAIClient
from aiagentaz.src.clients.gemini import GeminiClient
from aiagentaz.src.clients.anthropic import AnthropicClient

class Agent:
    client: str
    client_kwargs: dict[str, Any]
    
    def __init__(
            self, 
            client: Literal["openai", "gemini", "anthropic"], 
            /, 
            **kwargs: Any
        ) -> None: ...

    @overload
    def get_client(
            self, 
            client: Literal["openai"], 
            **kwargs: Any
        ) -> ContextManager[OpenAIClient]: ...
    
    @overload
    def get_client(
            self, 
            client: Literal["gemini"], 
            **kwargs: Any
        ) -> ContextManager[GeminiClient]: ...
    
    @overload
    def get_client(
            self, 
            client: Literal["anthropic"], 
            **kwargs: Any
        ) -> ContextManager[AnthropicClient]: ...
