Agent
=====

The Agent class provides a unified interface for interacting with various AI services.

Overview
--------

The Agent class serves as the main entry point for making requests to different AI service providers. It handles client initialization, configuration, and request generation.

Basic Usage
-----------

.. code-block:: python

    from aiagentaz.domain.agent import Agent

    # Initialize an agent with OpenAI
    agent = Agent(
        client="openai",
        api_key="your-api-key"
    )

    # Generate a response
    response = agent.generate(
        model="gpt-4",
        prompt="Write a hello world program"
    )

API Reference
-------------

.. autoclass:: aiagentaz.domain.agent.Agent
   :members: generate, get_client, validate_client
   :undoc-members:
   :show-inheritance:
   :special-members: __init__
   :exclude-members: model_construct, model_copy, model_dump, model_dump_json, model_json_schema, model_parametrized_name, model_post_init, model_rebuild, model_validate, model_validate_json, model_validate_strings, copy

Configuration
-------------

The Agent class accepts the following configuration parameters:

- ``client`` (str): The AI service provider to use (required)
- ``api_key`` (str): API key for the service provider
- Additional provider-specific parameters can be passed as keyword arguments

Supported Clients
----------------

- OpenAI
- Gemini
- Anthropic

Example
-------

.. code-block:: python

    from aiagentaz.domain.agent import Agent

    # Initialize with OpenAI
    openai_agent = Agent(
        client="openai",
        api_key="your-openai-key",
        model="gpt-4"
    )

    # Initialize with Gemini
    gemini_agent = Agent(
        client="gemini",
        api_key="your-gemini-key",
        model="gemini-1.5"
    )

    # Generate responses
    openai_response = openai_agent.generate(
        prompt="Write a poem about AI"
    )

    gemini_response = gemini_agent.generate(
        prompt="Explain quantum computing"
    ) 