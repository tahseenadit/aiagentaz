from pydantic import BaseModel, field_validator, Field
from typing import Callable


class Tool(BaseModel):
    """A tool is a function that can be used to generate a response.
    
    Args:
        name: The name of the tool
        fn: The function to be called when the tool is used
    """
    name: str = Field(description="The name of the tool")
    fn: Callable = Field(description="The function to be called when the tool is used")
    policies: list[str] = Field(default_factory=list, description="The policies to be used when the tool is used")
    
    @field_validator('fn')
    def validate_fn(cls, v: Callable) -> Callable:
        if not callable(v):
            raise ValueError("fn must be a callable")
        return v

    @field_validator('policies')
    def validate_policies(cls, v: list[str]) -> list[str]:
        if not isinstance(v, list):
            raise ValueError("policies must be a list")
        if not all(isinstance(policy, str) for policy in v):
            raise ValueError("policies must be a list of strings")
        return v

    def bind_policies(self, policies: list[str]) -> None:
        self.policies.extend(policies)