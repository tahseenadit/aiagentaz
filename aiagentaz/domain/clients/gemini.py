import google.generativeai as genai

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
            **kwargs: Configuration parameters for the Gemini API.
                     Must include 'api_key' for authentication.
        
        Raises:
            Exception: If configuration fails (e.g., invalid API key).
        """
        try:
            # Configure the Gemini API with provided parameters
            genai.configure(**kwargs)
        except Exception as e:
            print(f"Error configuring API: {e}")

    def generate(self, prompt: str = None, model: str = None, **kwargs) -> str | None:
        """Generate text using the specified Gemini model.
        
        Args:
            prompt: The input text prompt for generation.
            model: The name of the Gemini model to use (e.g., 'gemini-pro').
            **kwargs: Additional parameters for text generation.
        
        Returns:
            str | None: The generated text if successful, None if an error occurs.
        
        Raises:
            Exception: If text generation fails.
        """
        try:
            # Initialize the model with specified name
            self.model = genai.GenerativeModel(model_name=model)            
            # Generate content based on the prompt
            response = self.model.generate_content(prompt)            
            return response.text            
        except Exception as e:
            print(f"Error generating text: {e}")
            return None