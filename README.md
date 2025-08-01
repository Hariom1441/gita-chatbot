# Gita Chatbot 🕉️

A chatbot using OpenAI GPT-4o API to answer questions inspired by teachings from the Bhagavad Gita.

## Features
- GPT-4o LLM
- Flask API endpoint: `/ask`
- Secure key via `.env`

## Setup
```bash
pip install -r requirements.txt
python -m dotenv set OPENAI_API_KEY your_api_key
```

## Run
```bash
python gita_chatbot.py
```

## Example Usage
```bash
curl -X POST http://127.0.0.1:5000/ask -H "Content-Type: application/json" -d '{"question": "What is the nature of the soul?"}'
```
