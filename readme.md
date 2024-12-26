# AI Agent AZ

A Python package that provides a simple and unified interface for interacting with various AI services.

## Features

- 🤖 Unified interface for AI service providers

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
    model="gpt-4o-mini", 
    prompt="Can you give me a hello world program in python?", 
)
print(res.content)
```

## Supported AI Services

Currently supported AI service providers:
- OpenAI
- Gemini

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
pip install -e ".[dev]"
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

Made with ❤️ by Md Tahseen Anam
```
