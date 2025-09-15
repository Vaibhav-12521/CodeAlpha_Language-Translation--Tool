from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate_text():
    text = request.form["text"]
    src = request.form["src"]
    dest = request.form["dest"]
    translated = translator.translate(text, src=src, dest=dest).text
    return jsonify({"translated": translated})

if __name__ == "__main__":
    app.run(debug=True)
