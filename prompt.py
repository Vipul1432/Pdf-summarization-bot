class Prompt:
    """
    A class responsible for creating prompts for summarizing PDF text.
    """

    def create_prompt(self, text: str) -> str:
        """
        Generates a prompt tailored for summarizing the given text.

        :param text: The text content extracted from the PDF.
        :return: A well-crafted prompt for the AI model.
        """
        return (
            f"Summarize the following content concisely, focusing on key points:\n\n{text}\n\n"
            "Summary:"
        )