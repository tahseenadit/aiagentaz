Clients
=======

The clients module provides implementations for different AI service providers.

Overview
--------

The clients module contains implementations for various AI service providers, each with their own specific configuration and response handling.

Supported Clients
---------------

OpenAI
~~~~~~

.. autoclass:: aiagentaz.domain.clients.openai.OpenAIClient
   :members:
   :undoc-members:
   :show-inheritance:

Example
^^^^^^^

.. code-block:: python

    from aiagentaz.domain.clients.openai import OpenAIClient

    client = OpenAIClient(api_key="your-api-key")
    response = client.generate(
        prompt="Write a poem",
        model="gpt-4"
    )

Gemini
~~~~~~

.. autoclass:: aiagentaz.domain.clients.gemini.GeminiClient
   :members:
   :undoc-members:
   :show-inheritance:

Example
^^^^^^^

.. code-block:: python

    from aiagentaz.domain.clients.gemini import GeminiClient

    client = GeminiClient(api_key="your-api-key")
    response = client.generate(
        prompt="Explain quantum computing",
        model="gemini-1.5"
    )

Anthropic
~~~~~~~~

.. autoclass:: aiagentaz.domain.clients.anthropic.AnthropicClient
   :members:
   :undoc-members:
   :show-inheritance:

Example
^^^^^^^

.. code-block:: python

    from aiagentaz.domain.clients.anthropic import AnthropicClient

    client = AnthropicClient(api_key="your-api-key")
    response = client.generate(
        prompt="Write a story",
        model="claude-3-5-sonnet-20241022",
        max_tokens="1000"
    )

Client Configuration
------------------

Each client can be configured with the following common parameters:

- ``api_key`` (str): API key for the service provider
- Additional provider-specific parameters can be passed as keyword arguments

Error Handling
-------------

All clients include built-in error handling:

- API error handling
- Response validation
- Rate limiting support
- Timeout handling

Best Practices
-------------

1. Always use environment variables for API keys
2. Handle API errors gracefully
3. Implement proper rate limiting
4. Use appropriate models for your use case
5. Monitor API usage and costs 