from crypt import methods
from random import choice
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def redir(): 
    return render_template("home.html", lang="en")

@app.route("/<string:lang>")
def home(lang): 
    return render_template("home.html", lang=lang)

@app.route("/generate", methods=["GET", "POST"])
def generate():
    if request.form.get('lenght') == '':
        error_message = "Select a lenght for your password"
        return render_template("home.html", message=error_message)

    if request.method == "GET":
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

    return render_template("home.html", password=generated_password, lenght=lenght)

@app.route("/about/<string:lang>")
def about(lang):
    return render_template("about.html", lang=lang)


if __name__ == "__main__":
    app.run(debug=True, port=4000)

