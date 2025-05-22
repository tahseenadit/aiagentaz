# Changelog / release notes

All notable changes to this project will be documented in this file.

This is an early-stage library (version 0.1.0). The functionality may change in future releases.

## [0.2.0] - 2024-01-XX

### Added
- Initial implementation for Graph-based workflow system with:
  - Base node abstraction with dependency management
  - BasicOperator node implementation supporting callable tasks
  - Operator chaining using '>>' operator
- Support for chaining mechanism for implementing chain of prompts:
  - @chain decorator for creating chainable functions
  - Automatic passing of previous response between chain steps
- Unit tests for prompts chaining mechanism:
  - Single function execution
  - Function chaining with arguments
  - Error handling for missing previous responses
- Unit tests for graph operations and chaining:
  - Basic operator task execution
  - Operator chaining and workflow execution
  - Input/output validation between nodes

### Developer Notes
- Introduced core graph architecture for future extensibility
- Added comprehensive test coverage for new graph features
- Introduced chaining mechanism for prompts chaining
- Added comprehensive test coverage for chaining mechanism
