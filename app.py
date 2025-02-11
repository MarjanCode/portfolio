from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    lang = request.args.get("lang", "fa")  # Default to Farsi
    return render_template("index.html", lang=lang)


if __name__ == "__main__":
    app.run(debug=True)

