from flask import Flask,render_template,request,jsonify
from rag_pipeline import get_answer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/ask",methods = ["Post"])
def ask():
    question = request.json.get("question")

    answer = get_answer(question)

    return jsonify({
        "answer":answer
    })

if __name__ == "__main__":
    app.run(debug = True)