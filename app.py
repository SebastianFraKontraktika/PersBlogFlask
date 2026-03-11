from flask import Flask, render_template, request, redirect, url_for, flash
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
def signup():
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
                    return redirect(url_for("login"))
                elif bruker["username"] == username:
                    username = None
                    print("Username already in use")
                    # make it so that something popsup to tell that username is already in use
                    # flash('username already exists', 'error')
                    # return redirect(url_for("signup"))

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

    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
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
                # noe som poper opp og sier du er logget på
                # noe som lagrer sessions
                return redirect(url_for("profil"))
        # noe som sier at brukernavn eller passord er feil.
        print("FAEN")

    return render_template("login.html")

@app.route("/profile")
def profil():
    return "<h1>profilen<h1/>"

if __name__ == "__main__":
    app.run(debug=True)