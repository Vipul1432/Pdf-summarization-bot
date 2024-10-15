import os
from utils.pdf_reader import PDFReader
from utils.api_client import GroqClient
from prompt import Prompt

class PDFSummarizer:
    """
    A class for summarizing text from PDF files in a specified folder.
    """

    def __init__(self):
        """
        Initializes the PDFSummarizer with required utilities.
        """
        self.pdf_reader = PDFReader()
        self.groq_client = GroqClient()
        self.prompt = Prompt()

    def summarize_pdfs(self, folder_path: str):
        """
        Reads and summarizes all PDF files in the specified folder.

        :param folder_path: Path to the folder containing PDF files.
        :return: A dictionary where keys are PDF file names and values are summaries.
        """
        summaries = {}

        if not os.path.isdir(folder_path):
            print("The provided path is not a valid directory.")
            return summaries

        for file_name in os.listdir(folder_path):
            if file_name.endswith(".pdf"):
                file_path = os.path.join(folder_path, file_name)
                pdf_text = self.pdf_reader.read_pdf(file_path)
                prompt = self.prompt.create_prompt(pdf_text)
                summary = self.groq_client.summarize(prompt)
                summaries[file_name] = summary

        return summaries

    def answer_question(self, pdf_text: str, question: str) -> str:
        """
        Uses the full text of a PDF to answer a user's question.

        :param pdf_text: The full text of the PDF content.
        :param question: The user's question related to the PDF.
        :return: An AI-generated answer to the question.
        """
        prompt = f"Based on the following PDF text, answer the question.\n\nPDF Text:\n{pdf_text}\n\nQuestion: {question}"
        return self.groq_client.summarize(prompt)
