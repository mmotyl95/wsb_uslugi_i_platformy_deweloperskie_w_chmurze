from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return ("Witam na stronie projektu")

@app.route("/hello")
def who():
    return "Kim jesteś?"

@app.route("/hello/<name>")
def greetingName(name):
    return("Witam, {name}, jak się masz?")
