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

    @field_validator('fn')
    def validate_fn(cls, v: Callable):
        if not callable(v):
            raise ValueError("fn must be a callable")
        return v
    
    def __init__(self, name: str, fn: Callable):
        super().__init__(name=name, fn=fn)