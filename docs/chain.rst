Chain
=====

The Chain module provides a decorator-based approach for creating sequential operations.

Overview
--------

The Chain module allows you to create a sequence of operations where each step can use the output of the previous step.

Basic Usage
-----------

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

API Reference
-------------

.. autoclass:: aiagentaz.domain.chain.Chain
   :special-members: __init__
   :exclude-members: model_construct, model_copy, model_dump, model_dump_json, model_json_schema, model_parametrized_name, model_post_init, model_rebuild, model_validate, model_validate_json, model_validate_strings

Methods
-------

.. automethod:: aiagentaz.domain.chain.Chain.decorate

.. automethod:: aiagentaz.domain.chain.Chain.has_keyword_argument

Chain Decorator
---------------

.. autofunction:: aiagentaz.domain.chain.chain

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
--------------

The chain system includes built-in error handling:

- Validates that functions in the chain have the required `previous_response` parameter
- Raises clear error messages when chain requirements are not met
- Maintains type safety throughout the chain 