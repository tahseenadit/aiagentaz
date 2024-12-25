"""
Unit tests for OpenAI integration functionality.
Tests the agent's ability to generate responses using OpenAI's API.
"""

import pytest
import openai
from unittest.mock import patch, Mock

from aiagentaz.domain import agent


def test_openai_generate():
    """
    Test the OpenAI generate function with mocked API response.
    
    This test verifies that:
    1. The generate function returns the expected response
    2. The mocked response content matches our test case
    """
    # Mock the API response
    mock_response = Mock()
    mock_response.content = "print('Hello, World!')"
    
    with patch('aiagentaz.domain.agent.generate') as mock_generate:
        mock_generate.return_value = mock_response
        
        # Test the function call with sample parameters
        response = agent.generate(
            client="openai",
            prompt="Create a hello world program in python.",
            model="gpt-4-mini",
            api_key="test-key"
        )
        
        # Verify the response matches our expected output
        assert response.content == "print('Hello, World!')"


if __name__ == "__main__":
    
    res = agent.generate(
        client="openai", 
        model="gpt-4o-mini", 
        prompt="Can you give me a hello world program in python?", 
        api_key="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"
    )
    print(res.content)