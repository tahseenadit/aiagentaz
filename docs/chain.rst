Chain
=====

The chain module provides a decorator-based approach for creating chains of operations.

Overview
--------

The chain functionality allows you to create sequences of operations where each step can access the result of the previous step. This is particularly useful for building complex AI workflows.

Basic Usage
----------

.. code-block:: python

    from aiagentaz.domain.chain import chain

    @chain
    def first_step():
        return "Initial prompt"

    @first_step
    def second_step(previous_response: str = None):
        return f"{previous_response} with enhancement"

    # Execute the chain
    result = second_step()

API Reference
------------

.. autofunction:: aiagentaz.domain.chain.chain

Chain Class
----------

.. autoclass:: aiagentaz.core.chain.Chain
   :members:
   :undoc-members:
   :show-inheritance:

Features
--------

- Decorator-based chain creation
- Automatic passing of previous responses
- Support for both positional and keyword arguments
- Error handling for missing previous responses

Example
-------

.. code-block:: python

    from aiagentaz.domain.chain import chain

    @chain
    def generate_initial_prompt():
        return "Write a story about a magical forest"

    @generate_initial_prompt
    def add_requirements(previous_response: str = None):
        return f"{previous_response}. Include a brave hero and a magical creature."

    @add_requirements
    def add_ending(previous_response: str = None):
        return f"{previous_response}. The story should have a happy ending."

    # Execute the chain
    final_prompt = add_ending()
    print(final_prompt)

Error Handling
-------------

The chain system includes built-in error handling:

- Validates that functions in the chain have the required `previous_response` parameter
- Raises clear error messages when chain requirements are not met
- Maintains type safety throughout the chain 