import PyPDF2

class PDFReader:
    """
    A utility class for reading text from PDF files.
    """

    def read_pdf(self, file_path: str) -> str:
        """
        Reads text content from a PDF file.

        :param file_path: Path to the PDF file.
        :return: Extracted text from the PDF.
        """
        text = ""
        with open(file_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text