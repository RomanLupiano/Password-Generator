from crypt import methods
from random import choice
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/generate", methods=["GET", "POST"])
def generate():
    if request.method == "GET" or request.form.get('lenght') == '':
        return render_template("home.html")

    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    lenght = int(request.form.get('lenght'))
    
    if request.form.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
    if request.form.get('special'):
        characters.extend(list('/*-+=!?@#$%&*()'))
    if request.form.get('numbers'):
        characters.extend(list('0123456789'))

    for i in range(lenght):
        generated_password += choice(characters)

    return render_template("home.html", password=generated_password)

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, port=4000)

