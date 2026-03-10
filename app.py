from flask import Flask, render_template, request, redirect, url_for
from db import get_db

app = Flask(__name__)
app.secret_key = "temp"

@app.route("/")
def forside():
    return render_template("forside.html")

@app.route("/innlegg")
def inlegg():
    return "<h1>hello world<h1/>"

@app.route("/signup", methods=["GET", "POST"])
def singup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        print(username, password, email)
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, password))
        db.commit()
        cursor.close()
        db.close()
        
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/profile")
def profil():
    return "<h1>profilen<h1/>"

if __name__ == "__main__":
    app.run(debug=True)