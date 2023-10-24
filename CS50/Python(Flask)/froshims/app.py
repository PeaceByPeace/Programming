import os
from flask_mail import Mail, Message
from flask import Flask, render_template, request, redirect
from cs50 import SQL

app = Flask(__name__)


os.environ.setdefault("MAIL_DEFAULT_SENDER", 'ilja.123732@gmail.com')
os.environ.setdefault("MAIL_PASSWORD", "yvpb fumw ogur nrjq")
os.environ.setdefault("MAIL_USERNAME", 'ilja.123732@gmail.com')

app.config["MAIL_DEFAULT_SENDER"] = os.environ["MAIL_DEFAULT_SENDER"]
app.config["MAIL_PASSWORD"] = os.environ["MAIL_PASSWORD"]
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.environ["MAIL_USERNAME"]

mail = Mail(app)
db = SQL("sqlite:///froshims.db")


SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee",
    "Football"
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/deregister", methods=["POST"])
def deregister():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM registrants WHERE id = ?", id)
    return redirect("/registrants")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")

    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")

    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")

    e_mail = request.form.get("e-mail")
    if not e_mail:
        return render_template("error.html", message="No e-mail was provided")

    db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport)
    message = Message("You are registered", recipients=[e_mail], body=f'Your name is {name} and your favorite sport is {sport}')
    mail.send(message)
    return redirect("/registrants")


@app.route('/registrants')
def registrants():
    registrants = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=registrants)