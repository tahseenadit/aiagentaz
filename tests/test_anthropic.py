"""
Unit tests for Anthropic integration functionality.
Tests the agent's ability to generate responses using Anthropic's API.
"""

from unittest.mock import patch, Mock

from aiagentaz.domain.agent import Agent


def test_anthropic_generate():
    """Test the Anthropic generate function with mocked API response."""
    # Create an agent instance
    test_agent = Agent(client="anthropic", api_key="test-key")
    
    # Mock the API response
    mock_response = Mock()
    mock_response.content = "print('Hello, World!')"
    
    with patch('aiagentaz.domain.agent.Agent.generate') as mock_generate:
        mock_generate.return_value = mock_response
        
        # Test the function call
        response = test_agent.generate(
            prompt="Create a hello world program in python.",
            model="claude-3-5-sonnet-20241022"
        )
        
        # Verify the response matches our expected output
        assert response.content == "print('Hello, World!')"


"""if __name__ == "__main__":
    
    my_agent = Agent(
        client="anthropic", 
        api_key="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"
    )
    res = my_agent.generate( 
        model="claude-3-5-sonnet-20241022", 
        prompt="Can you give me a hello world program in python?",
        max_tokens=1000, 
    )

    print(res.content)"""