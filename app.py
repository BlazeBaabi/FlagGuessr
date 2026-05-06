from flask import Flask, render_template, request, session, redirect, url_for
import requests
import random

app = Flask(__name__)
app.secret_key = "secret123"


COUNTRIES = []

def random_cat():
    try:
        url = "https://api.thecatapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit=1"
        response = requests.get(url)
        data = response.json()
        session["Cat"] = data[0]["url"]
    except:
        session["Cat"] = "https://media.tenor.com/DtD4LZbctTIAAAAM/tamm-cat.gif"

def load_countries():
    global COUNTRIES
    url = "https://restcountries.com/v3.1/all?fields=name,flags"
    response = requests.get(url)
    data = response.json()

    COUNTRIES = [
        (c.get("name", {}).get("common"), c.get("flags", {}).get("png"))
        for c in data
        if c.get("name", {}).get("common") and c.get("flags", {}).get("png")
    ]

load_countries()


def new_round():
    name, flag = random.choice(COUNTRIES)

    session["country"] = name
    session["flag"] = flag

    random_cat()

    if session.get("mode") == "easy":
        options = random.sample([c[0] for c in COUNTRIES], 3)
        options.append(name)
        random.shuffle(options)

        session["BTN1"] = options[0]
        session["BTN2"] = options[1]
        session["BTN3"] = options[2]
        session["BTN4"] = options[3]


@app.route("/set_mode/<mode>")
def set_mode(mode):
    if mode in ["easy", "hard"]:
        session["mode"] = mode

    session["Points"] = 0
    session["Streak"] = 0

    new_round()
    return redirect(url_for("home"))


@app.route("/", methods=["GET"])
def home():
    if "Points" not in session:
        session["Points"] = 0
    if "Streak" not in session:
        session["Streak"] = 0
    if "mode" not in session:
        session["mode"] = "easy"

    
    if "country" not in session:
        new_round()

    mode = session["mode"]

    return render_template(
        "index.html",
        mode=mode,
        flag=session["flag"],
        points=session["Points"],
        streak=session["Streak"],
        BTN1=session.get("BTN1"),
        BTN2=session.get("BTN2"),
        BTN3=session.get("BTN3"),
        BTN4=session.get("BTN4"),
        cat=session.get("Cat")
    )


@app.route("/guess", methods=["POST"])
def guess():
    guess = request.form.get("guess", "")
    correct = session.get("country")

    if guess.lower() == correct.lower():
        session["Points"] += 1
        session["Streak"] += 1
    else:
        session["Streak"] = 0
        if session["Points"] > 0:
            session["Points"] -= 1

    new_round()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)