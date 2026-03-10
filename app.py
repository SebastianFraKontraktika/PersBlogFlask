from flask import Flask, render_template
from db import get_db

app = Flask(__name__)
app.secret_key = "temp"

@app.route("/")
def forside():
    return render_template("forside.html")

@app.route("/innlegg")
def inlegg():
    return "<h1>hello world<h1/>"

@app.route("/signup")
def singup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/profile")
def profil():
    return "<h1>profilen<h1/>"

if __name__ == "__main__":
    app.run(debug=True)