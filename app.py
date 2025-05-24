from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os

app = Flask(__name__)

# Set your Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_advice", methods=["POST"])
def get_advice():
    data = request.get_json()
    user_input = data["message"]
    prompt = f"You are a relationship advisor. Give short, clear, and practical advice in 2-3 sentences. Also don't you to much vocublary, you ear vocublary\nUser: {user_input}\nBot:"
    
    response = model.generate_content(prompt)
    return jsonify({"reply": response.text.strip()})

if __name__ == "__main__":
    app.run(debug=True)
