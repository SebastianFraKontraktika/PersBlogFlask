from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv, dotenv_values 
from db import get_db
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("secret_key")

@app.route("/")
def forside():
    return render_template("forside.html")

@app.route("/innlegg")
def inlegg():
    return "<h1>hello world<h1/>"

@app.route("/signup", methods=["GET", "POST"])
def signup():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT username, email FROM users")
        Brukere = cursor.fetchall()
        
        if Brukere:
            for bruker in Brukere:
                if bruker["email"] == email:
                    email = None
                    flash("email already in use, proceed to login")
                    return redirect(url_for("login"))
                
                elif bruker["username"] == username:
                    username = None
                    print("Username already in use")
                    error = "username already exits"

            if email and username:    
                cursor.execute(
                    "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                    (username, email, password))
                db.commit()
                cursor.close()
                db.close()
                return redirect(url_for("login"))
        else:
            cursor.execute(
                "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                (username, email, password))
            db.commit()
            cursor.close()
            db.close()
            return redirect(url_for("login"))

    return render_template("signup.html", error=error)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = {"username": username, "password": password}

        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT username, password FROM users")
        Brukere = cursor.fetchall()

        for bruker in Brukere:
            if bruker == user:
                flash("Congratulations, you are now logged in")
                # noe som lagrer sessions
                return redirect(url_for("profil"))
            
        error = "Invalid username or password please try again"
    return render_template("login.html", error=error)

@app.route("/profile")
def profil():
    return "<h1>profilen<h1/>"

if __name__ == "__main__":
    app.run(debug=True)