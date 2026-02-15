from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["message"]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI Copilot assistant helping with coding and productivity."},
            {"role": "user", "content": user_input}
        ]
    )

    answer = response.choices[0].message.content

    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(debug=True)
