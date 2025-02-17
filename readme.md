# AI Agent AZ

A Python package that provides a simple and unified interface for interacting with various AI services.

## Features

- 🤖 Unified interface for different AI service providers
- ⛓️ Decorator-based chain operations

## Installation

```bash
pip install aiagentaz
```

## Quick Start

```python
from aiagentaz.domain.agent import Agent

my_agent = Agent(
    client="openai", 
    api_key="your-api-key"
)
res = my_agent.generate( 
    model="gpt-4", 
    prompt="Can you give me a hello world program in python?", 
)
print(res.content)
```

## Chain Examples

Chain multiple operations using decorators:

```python
from aiagentaz.domain.chain import chain

# Define chain of operations
@chain
def get_prompt():
    return "Write a story about a magical forest"

@get_prompt
def enhance_prompt(previous_response: str = None):
    return previous_response + " Give it a title and a short description"

@enhance_prompt
def add_details(previous_response: str = None):
    return previous_response + " Generate a list of 5 key events in the story"

# Execute the chain
result = add_details()
print(result)
```

Each function in the chain can access the result of the previous function through the `previous_response` parameter.

## Supported AI Services

Currently supported AI service providers:
- OpenAI
- Gemini
- Anthropic

## Capabilities

### OpenAI
- Simple text generation

### Gemini
- Simple text generation

### Anthropic
- Simple text generation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup

1. Clone the repository
```bash
git clone https://github.com/yourusername/aiagentaz.git
cd aiagentaz
```

2. Install development dependencies
```bash
pip install -e .
```

3. Run tests
```bash
pytest
```

## Support

If you encounter any problems or have any questions, please [open an issue](https://github.com/tahseenadit/aiagentaz/issues).

## Acknowledgments

- Inspired by the need for a unified AI service interface

---
