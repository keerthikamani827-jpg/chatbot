# AI Chat Assistant

## Overview

AI Chat Assistant is a simple conversational AI application built using Python, Streamlit, and Hugging Face Inference API.

The application allows users to ask questions and receive AI-generated responses through an interactive chat interface. Chat history is maintained during the current session.

## Features

* Interactive chat interface
* AI-generated responses
* Chat history management
* Hugging Face API integration
* GPT-OSS-120B model support
* Simple and responsive Streamlit UI
* Secure API token handling using environment variables

## Technologies Used

* Python
* Streamlit
* Hugging Face Hub
* Hugging Face Inference API
* GPT-OSS-120B

## Project Structure

```text
AI-Chat-Assistant/
│
├── app.py
├── requirements.txt
└── README.md
```

## Requirements

Make sure Python is installed on your system.

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

## Hugging Face API Token

This project requires a Hugging Face API token.

Set the token as an environment variable.

### Windows PowerShell

```powershell
$env:HF_TOKEN="your_hugging_face_token"
```

Do not directly add the API token to the Python source code or upload it to GitHub.

## Running the Application

Open the project folder in VS Code and run:

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## How It Works

1. The user enters a question in the Streamlit chat interface.
2. The question is stored in the session chat history.
3. Python sends the conversation to the Hugging Face Inference API.
4. The GPT-OSS-120B model processes the request.
5. The generated response is displayed in the chat interface.
6. The response is stored in the session history for continued conversation.

## Environment Variable

The application uses the following environment variable:

```text
HF_TOKEN
```

This keeps the Hugging Face API token separate from the application source code.

## Future Improvements

* Add user authentication
* Add conversation export
* Add multiple AI model selection
* Add voice input and output
* Add database support for permanent chat history
* Add file upload and document question answering

## License

This project is created for educational and development purposes.
