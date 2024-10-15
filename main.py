from pdf_summarizer import PDFSummarizer
import os

def get_folder_path() -> str:
    """
    Prompts user for folder path.
    
    :return: Folder path entered by the user.
    """
    return input("Please enter the path to the folder containing PDF files (or type 'exit' to quit): ")

def display_summaries(summaries: dict):
    """
    Displays summaries for each PDF file.
    
    :param summaries: Dictionary with file names as keys and summaries as values.
    """
    for file_name, summary in summaries.items():
        print(f"\nSummary for {file_name}:\n{summary}\n")

def ask_questions_for_pdf(summarizer: PDFSummarizer, pdf_text: str, file_name: str):
    """
    Prompts the user to ask questions based on the provided PDF text.

    :param summarizer: PDFSummarizer instance.
    :param pdf_text: Text content of the PDF.
    :param file_name: Name of the file for context in the prompt.
    """
    while True:
        user_question = input(f"Ask a question about {file_name} (or type 'back' to select another file): ")
        if user_question.lower() == "back":
            break
        answer = summarizer.answer_question(pdf_text, user_question)
        print(f"Answer: {answer}\n")

def question_answer_mode(summarizer: PDFSummarizer, folder_path: str, summaries: dict):
    """
    Allows the user to select a PDF file by name and ask questions.

    :param summarizer: PDFSummarizer instance.
    :param folder_path: Path to the folder containing PDFs.
    :param summaries: Dictionary with file names as keys and summaries as values.
    """
    print("You can now ask questions based on any PDF by its file name. Type 'back' to go for asking questions from another pdf.")
    while True:
        file_name = input("Enter the PDF file name to ask a question about (or type 'back' to finish): ")
        if file_name.lower() == "back":
            break
        if file_name not in summaries:
            print(f"File {file_name} not found. Please enter a valid file name.")
            continue

        # Load the full PDF text and enter question mode
        pdf_path = os.path.join(folder_path, file_name)
        pdf_text = summarizer.pdf_reader.read_pdf(pdf_path)
        ask_questions_for_pdf(summarizer, pdf_text, file_name)

def main():
    summarizer = PDFSummarizer()

    while True:
        folder_path = get_folder_path()
        if folder_path.lower() == "exit":
            print("Exiting the program.")
            break

        summaries = summarizer.summarize_pdfs(folder_path)
        display_summaries(summaries)
        question_answer_mode(summarizer, folder_path, summaries)

if __name__ == "__main__":
    main()
