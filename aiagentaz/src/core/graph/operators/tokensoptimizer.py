"""
This operator is used to optimize the prompt for the LLM.

Summarization:
Instead of sending the entire chat history, use an AI to create a summary of the conversation.
The summary can be updated with each new message, condensing the conversation history while retaining important context.
This reduces the number of tokens needed, as the chatbot receives a concise overview of the discussion. 
2. Sliding Window:
Implement a "sliding window" that keeps only the most recent messages in the context.
Older messages are discarded as new ones are added, ensuring the chatbot focuses on the most relevant part of the conversation.
This approach is efficient and prioritizes recent messages, which are often most important for maintaining context. 
3. Categorized Excerpts:
Divide the chat history into different categories or topics.
When the user asks a question, only send the relevant excerpts to the chatbot.
This method can be particularly useful when dealing with conversations that cover multiple distinct subjects
"""

from aiagentaz.src.core.graph.node import BaseNode
from enum import Enum
from typing import Callable, Any, Optional


class EnumSummarizer(Enum):
    """
    The summarizer to use.
    """
    GENSIM = "Gensim"
    SUMY = "Sumy"

class TokensOptimizer(BaseNode):
    """
    This operator is used to optimize the prompt for the LLM.
    """

    def __init__(self, task_id: str, task: Callable, summarizer: Optional[str]):
        super().__init__()
        self.task_id = task_id # Set the task id
        self.task = task # Set the task
        self.summarizer = self._get_summarizer(summarizer) # Set the summarizer

    @property
    def node_id(self) -> str:
        return self.task_id # Return the task id

    def _get_summarizer(self, summarizer: str = EnumSummarizer.GENSIM) -> str:
        """Get the summarizer"""
        return EnumSummarizer(summarizer) # Return the summarizer

    def _summarize_chat_history(self) -> str:
        """Summarize the chat history"""
        summarizer = self.summarizer # Get the summarizer
    
    def execute_task(self) -> Any:
        """Execute the task"""
        if callable(self.task):
            if 'input_from_upstream_node' in self.task.__code__.co_varnames:
                return self.task(input_from_upstream_node=self.input_from_upstream_node)