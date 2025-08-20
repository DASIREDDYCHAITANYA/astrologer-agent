from flask import Flask, render_template, request, jsonify
from llm import response_

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        name = request.form.get("name")
        dob = request.form.get("dob")
        time = request.form.get("time")
        place = request.form.get("place")
        question = request.form.get("question")

        # Call your LLM function
        result = response_(name, dob, time, place, question)

        return jsonify({"status": "success", "response": result})
    except Exception as e:
        return jsonify({"status": "error", "response": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
