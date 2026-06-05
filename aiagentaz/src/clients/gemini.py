from google import genai
from google.genai import types
from aiagentaz.src.core.prompts.gemini_prompts import SYSTEM_PROMPT_VALIDATE_GUARDRAILS
from aiagentaz.src.tools import Tool

import inspect

class GeminiClient:
    """Client for interacting with Google's Gemini AI model.
    
    This class provides a wrapper around Google's generative AI functionality,
    handling configuration and text generation requests.
    
    Attributes:
        model: The configured GenerativeModel instance used for text generation.
    """

    def __init__(self, **kwargs) -> None:
        """Initialize and configure the Gemini AI client.
        
        Args:
            kwargs: Configuration parameters for the Gemini API.
                    Must include 'api_key' for authentication.
        
        Raises:
            Exception: If configuration fails (e.g., invalid API key).
        """
        try:
            # Configure the Gemini API with provided parameters
            self.client = genai.Client(**kwargs)
            self.tools: list[Tool] = []
        except Exception as e:
            print(f"Error configuring API: {e}")


    def _construct_tools_metadata(self, tools: list[Tool]) -> list[dict]:
        """Construct the metadata for the tools.
        
        Args:
            tools: The list of tools to construct the metadata for (required). Must be a list of Tool objects.

        Returns:
            list[dict]: The metadata for the tools.
        """
        tools_metadata = []
        for tool in tools:
            source_code = inspect.getsource(tool.fn)
            tools_metadata.append({
                "name": tool.name,
                "source_code": source_code,
                "policies": tool.policies
            })
        return tools_metadata

    def _validate_tools(
        self, 
        model: str, 
        tools: list[Tool], 
        policies: list[str], 
        **kwargs
    ) -> dict:
        """Validate the policies for the tools.
        
        Args:
            model: The name of the Gemini model to use (required).
            tools: The list of tools to validate (required). Must be a list of Tool objects.
            policies: The list of policies to validate (required). Must be a list of strings.
            kwargs: Additional parameters for text generation.
        """
        # Construct the metadata for the tools
        tools_metadata = self._construct_tools_metadata(tools)
        print(tools_metadata)
        # Construct the prompt for the validation
        prompt = SYSTEM_PROMPT_VALIDATE_TOOLS.format(
            tools=tools_metadata
        )
        response = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content


    def bind_tools(self, tools: list[Tool], **kwargs) -> None:
        """Bind the tools to the agent.

        Args:
            tools: The list of tools to bind to the agent (required). Must be a list of Tool objects.
            kwargs: Additional parameters for text generation.
        """
        self.tools = tools

    
    def validate_tools(self, **kwargs) -> None:
        """Validate the tools for the agent.

        Args:
            kwargs: Additional parameters for text generation.
        """
        self._validate_tools(self.tools, **kwargs)

    
    def generate(self, prompt: str, model: str, **kwargs) -> str:
        """Generate text using the specified Gemini model.
        
        Args:
            prompt: The input text prompt for generation (required).
            model: The name of the Gemini model to use (required).
            kwargs: Additional parameters for text generation.
        
        Returns:
            str | None: The generated text if successful, None if an error occurs.
        
        Raises:
            ValueError: If prompt or model is None or empty.
        """
        if not prompt or not model:
            raise ValueError("Both prompt and model parameters are required.")
        


        try:
            # Initialize the model with specified name
            self.chat = self.client.chats.create(model=model)            
            # Generate content based on the prompt
            response = self.model.generate_content(prompt)            
            return response.text            
        except Exception as e:
            print(f"Error generating text: {e}")