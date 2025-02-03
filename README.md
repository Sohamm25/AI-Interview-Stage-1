# AI Interviewer

This project is a basic command-line tool that simulates an interview session. It asks a series of interview questions, gathers your responses, and then provides some feedback based on word count, sentence structure, and sentiment analysis.

## Features

- **Interactive Interview:** The tool asks you interview questions one by one.
- **Response Analysis:** After you answer, it analyzes your response and offers feedback.
- **Simple Feedback:** Feedback includes suggestions on how to add more detail, adjust tone, and improve sentence structure.

## Setup

1. **Clone the repository.**
2. **Install the required packages:**

   ```bash
   pip install nltk
   ```

3. **Run the script:**

   ```bash
   python ai_interviewer.py
   ```

The script will download the necessary NLTK resources on the first run.

## Usage

Simply run the tool and answer the questions as they appear. After the interview, you'll receive a summary with detailed feedback to help you improve your interview responses.