.. AI Agent AZ documentation master file, created by
   sphinx-quickstart on Sat Dec 28 14:48:39 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

AI Agent AZ
===========

A Python package that provides a simple and unified interface for interacting with various AI services.

Features
--------

- 🤖 Unified interface for different AI service providers (OpenAI, Gemini, Anthropic)
- ⛓️ Decorator-based chain operations for complex workflows
- 🔄 Graph-based workflow system with operator chaining

Quick Start
-----------

Basic Usage
~~~~~~~~~~~

.. code-block:: python

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

Chain Operations
~~~~~~~~~~~~~~~~

Chain multiple operations using decorators:

.. code-block:: python

    from aiagentaz.domain.chain import chain

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

Graph-based Workflows
~~~~~~~~~~~~~~~~~~~~~

Create complex workflows using the graph-based system:

.. code-block:: python

    from aiagentaz.domain.graph.operators.basicoperator import BasicOperator

    def task_1(input_from_upstream_node: str):
        return "task_1_result"
    
    def task_2(input_from_upstream_node: str):
        return f"task_2_result: {input_from_upstream_node}"
    
    task_1 = BasicOperator("task_1", task_1)
    task_2 = BasicOperator("task_2", task_2)
    
    workflow = task_1 >> task_2
    result = workflow.execute_task()

Supported AI Services
---------------------

OpenAI
~~~~~~

- Simple text generation
- Models: GPT-4, GPT-3.5, etc.

Gemini
~~~~~~

- Simple text generation
- Models: Gemini 1.5, etc.

Anthropic
~~~~~~~~~

- Simple text generation
- Models: Claude 3.5, etc.

API Reference
-------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   agent
   chain
   graph
   clients
