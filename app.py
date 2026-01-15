from flask import Flask, render_template, request
from utils.summarizer import generate_notes

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    notes = ""
    if request.method == "POST":
        text = request.form["text"]
        notes = generate_notes(text)
    return render_template("index.html", notes=notes)

if __name__ == "__main__":
    app.run(debug=True)
