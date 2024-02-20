from typing import Any
from langchain.prompts import PromptTemplate

class CustomPromptTemplate(PromptTemplate):
    def format(self, **kwargs: Any) -> str:
        """Format the prompt with the inputs.

        Args:
            kwargs: Any arguments to be passed to the prompt template.

        Returns:
            A formatted string. If formatting fails, return an empty string.

        Example:

            .. code-block:: python

                prompt.format(variable1="foo")
        """
        try:
            return super().format(**kwargs)
        except Exception as e:
            print(f"Prompt format missing: {e}, drop this prompt.")
            return ""