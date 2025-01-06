from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    lang = request.args.get("lang", "per")  # Default to Persian
    return render_template("index.html", lang=lang)
