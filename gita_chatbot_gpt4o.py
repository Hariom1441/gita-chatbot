import os
import openai
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# Load Gita content
with open("data/gita.txt", "r", encoding="utf-8") as f:
    gita_context = f.read()

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question", "")
    
    # Properly formatted multi-line f-string
    prompt = f"""You are a compassionate teacher answering using the Bhagavad Gita.

Context:
{gita_context}

User: {question}
GitaBot:"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200
        )
        return jsonify({"response": response["choices"][0]["message"]["content"].strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
