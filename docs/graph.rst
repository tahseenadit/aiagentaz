Graph
=====

The graph module provides a graph-based workflow system for creating complex operation chains.

Overview
--------

The graph system allows you to create directed acyclic graphs (DAGs) of operations, where each node can depend on the output of other nodes. This is particularly useful for creating complex workflows with multiple dependencies.

Basic Usage
-----------

.. code-block:: python

    from aiagentaz.domain.graph.operators.basicoperator import BasicOperator

    def task_1(input_from_upstream_node: str):
        return "task_1_result"
    
    def task_2(input_from_upstream_node: str):
        return f"task_2_result: {input_from_upstream_node}"
    
    # Create operators
    op1 = BasicOperator("task_1", task_1)
    op2 = BasicOperator("task_2", task_2)
    
    # Create workflow
    workflow = op1 >> op2
    
    # Execute workflow
    result = workflow.execute_task()

API Reference
-------------

BasicOperator
~~~~~~~~~~~~~

.. autoclass:: aiagentaz.domain.graph.operators.basicoperator.BasicOperator
   :special-members: __init__
   :exclude-members: model_construct, model_copy, model_dump, model_dump_json, model_json_schema, model_parametrized_name, model_post_init, model_rebuild, model_validate, model_validate_json, model_validate_strings

BasicOperator Methods
~~~~~~~~~~~~~~~~~~~~~    

.. automethod:: aiagentaz.domain.graph.operators.basicoperator.BasicOperator.execute_task

DependencyABC
~~~~~~~~~~~~~

.. autoclass:: aiagentaz.core.graph.abc.DependencyABC
   :special-members: __init__
   :exclude-members: model_construct, model_copy, model_dump, model_dump_json, model_json_schema, model_parametrized_name, model_post_init, model_rebuild, model_validate, model_validate_json, model_validate_strings

DependencyABC Methods
~~~~~~~~~~~~~~~~~~~~~

.. automethod:: aiagentaz.core.graph.abc.DependencyABC.execute_task

Features
--------

- Graph-based workflow creation
- Operator chaining using the `>>` operator
- Automatic dependency management
- Support for complex workflows with multiple dependencies
- Type-safe operation execution

Example
-------

.. code-block:: python

    from aiagentaz.domain.graph.operators.basicoperator import BasicOperator

    def generate_prompt(input_from_upstream_node: str):
        return "Write a story about " + input_from_upstream_node

    def enhance_prompt(input_from_upstream_node: str):
        return input_from_upstream_node + " with a magical twist"

    def add_requirements(input_from_upstream_node: str):
        return input_from_upstream_node + ". Include a hero and a villain."

    # Create operators
    prompt_gen = BasicOperator("prompt_gen", generate_prompt)
    enhancer = BasicOperator("enhancer", enhance_prompt)
    requirements = BasicOperator("requirements", add_requirements)

    # Create workflow
    workflow = prompt_gen >> enhancer >> requirements

    # Execute with initial input
    prompt_gen.input_from_upstream_node = "a forest"
    result = workflow.execute_task()

Error Handling
--------------

The graph system includes built-in error handling:

- Validates that all required inputs are provided
- Ensures proper connection between nodes
- Handles circular dependencies
- Provides clear error messages for common issues 