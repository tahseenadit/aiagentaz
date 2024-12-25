"""
Agent module for handling client interactions and generation requests.

This module provides the main functionalities for setting up clients and generating
responses using different AI service providers.
"""

from contextlib import contextmanager


from ..core.clients import known_clients
from ..core.request import Request

class Agent:
    """Base Agent class for handling AI client interactions.
    
    This class serves as a foundation for AI agents, managing client configuration
    and initialization parameters.
    
    Attributes:
        client: The required AI client instance.
        client_kwargs (dict): Dictionary storing client configuration parameters.
    """

    def __init__(self, client, **kwargs) -> None:
        """Initialize the Agent with a required client and additional parameters.
        
        Args:
            client: The AI client instance (required).
            **kwargs: Additional keyword arguments for client configuration.
        """
        self.client_kwargs = kwargs
        self.client_kwargs["client"] = client
        

    @contextmanager
    def get_client(self, client=None, **kwargs):
        """
        Context manager for handling client initialization and cleanup.
        
        Args:
            client (str, optional): The name of the client to initialize. Defaults to None.
            **kwargs: Additional keyword arguments passed to the client constructor.
            
        Yields:
            object: An initialized client instance or None if initialization fails.
            
        Example:
            with get_client("openai", api_key="key") as client:
                if client:
                    result = client.generate(prompt="Hello")
        """
        request = Request(client)

        try:
            config = known_clients[client]
            yield config.client_class(**kwargs)
        except Exception as e:
            print(f"Error initializing client: {e}")
            yield None  # Yield None if there's an error and exit early
        finally:
            # Any cleanup code can go here if needed
            pass


    def generate(self, model=None, prompt=None, **kwargs):
        """
        Generate a response using the specified client and configuration.

        Args:
            model (str): The model to use for generation. Defaults to None.
            prompt (str): The input prompt for generation. Defaults to None.
            **kwargs: Additional keyword arguments for client configuration and generation.

        Returns:
            object: The generation result from the client, or 0 if an error occurs.

        Example:
            response = generate(
                client="openai",
                prompt="Write a poem",
                api_key="your-key",
                model="gpt-4"
            )
        """
        # Prepare arguments for the generation call
        call_kwargs = kwargs  # The additional arguments passed to the call to this function

        # Initialize client and generate response
        with self.get_client(**self.client_kwargs) as client:
            if client:
                try:
                    res = client.generate(prompt=prompt, model=model, **call_kwargs)
                    return res
                except Exception as e:
                    print(f"Error during generation: {e}")

