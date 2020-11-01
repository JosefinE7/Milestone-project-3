import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/store")
def store():
    return render_template("store.html")


@app.route("/prior_work")
def prior_work():
    return render_template("prior_work.html")


@app.route("/contact_me")
def contact_me():
    return render_template("contact_me.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(
        os.environ.get("PORT")), debug=True)
