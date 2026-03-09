from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def forside():
    return render_template("forside.html")

@app.route("/om")
def om():
    return "<h1>hello world<h1/>"

@app.route("/signup")
def singup():
    return "<h1>kommer snart!<h1/>"

@app.route("/login")
def login():
    return "<h1>kommer snart!<h1/>"

if __name__ == "__main__":
    app.run(debug=True)