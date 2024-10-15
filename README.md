# PDF Summarization Bot

## Overview

The PDF Summarization Bot is a Python application that reads PDF files from a specified folder, summarizes their content using AI, and allows users to ask questions based on the PDF text. This project utilizes the Groq AI model for summarization, making it an efficient tool for quickly extracting key information from large documents.

## Features

- Read PDF files from a user-specified directory.
- Summarize the text content of each PDF using the Groq AI model.
- Interactive question-and-answer feature, allowing users to inquire about specific details from the PDFs.
- Export the bot as a standalone executable.

## Requirements

- Python 3.12 or higher
- Required Python packages:
  - `groq`
  - `PyPDF2` (or any PDF reading library you choose)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Vipul2432/pdf-summarization-bot.git
   cd pdf-summarization-bot
   ```

2. Install the required packages:

   ````bash
   pip install -r requirements.txt```

   ````

3. Set up your environment variable for the Groq API key:

   ```bash
   set GROQ_API_KEY=your_api_key_here
   ```

## Executable File

An executable version of the bot is included in this repository. You can simply download the PDFSummarizer.exe file from the repository and run it without needing to install Python or any dependencies.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Vipul1432/pdf-summarization-bot/blob/main/LICENSE.txt) file for details.

