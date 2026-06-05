"""
Unit tests for Gemini integration functionality.
Tests the agent's ability to generate responses using Gemini's API.
"""


from unittest.mock import patch, Mock

from aiagentaz.src.agent import Agent
from aiagentaz.src.tools import Tool, tool


def test_gemini_generate():
    """Test the Gemini generate function with mocked API response."""
    # Create an agent instance
    test_agent = Agent(client="openai", api_key="test-key")

    # Mock the API response
    mock_response = Mock()
    mock_response.content = "print('Hello, World!')"

    with patch('aiagentaz.src.agent.Agent.generate') as mock_generate:
        mock_generate.return_value = mock_response

        # Test the function call
        response = test_agent.generate(
            prompt="Create a hello world program in python.",
            model="gemini-1.5-flash"
        )

        # Verify the response matches our expected output
        assert response.content == "print('Hello, World!')"


def test_gemini_bind_tools():
    """Test the Gemini bind tools function with mocked API response."""
    # Create an agent instance
    test_agent = Agent(client="gemini", api_key="test-key")
    
    # Create a test tool function
    def test_tool(self, prompt: str) -> str:
        return "print('Hello, World!')"

    # Create a test tool object with the test tool function
    test_tool = Tool(name="test_tool", fn=test_tool)
    
    # Bind the test policies to the test tool
    test_tool.bind_policies(policies=["Should only return a string"])

    # Create a list of test tools
    test_tools = [test_tool]

    # Bind the test tools to the test agent
    test_agent.bind_tools(tools=test_tools)
    assert test_agent.tools == test_tools


def test_gemini_validate_tools():
    """Test the Gemini validate tools function with mocked API response."""
    # Create an agent instance
    test_agent = Agent(client="gemini", api_key="test-key")
    
    # Create a test tool function
    def test_tool(self, prompt: str) -> str:
        return "print('Hello, World!')"

    # Create a test tool object with the test tool function
    test_tool = Tool(name="test_tool", fn=test_tool)
    
    # Bind the test policies to the test tool
    test_tool.bind_policies(policies=["Should only return a string"])

    # Create a list of test tools
    test_tools = [test_tool]

    # Bind the test tools to the test agent
    test_agent.bind_tools(tools=test_tools)
    test_agent.validate_tools()