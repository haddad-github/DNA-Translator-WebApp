from flask import Flask, render_template, request, flash

#Initialiser l'application; creer classe pour notre application
app = Flask(__name__)
app.secret_key = "bruh"

#Represente la derniere partie du URL (ex: /page1 , /stats, /store3, etc.)
#Doit associer cette route avec une fonction
@app.route("/translate")
def index():
    #Flash un message; liee aux % message % de index.html
    flash("RNA seq")
    return render_template("index.html")

##CODE PYTHON##
@app.route("/translate", methods=["POST", "GET"])
def translate():

    dict = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}

    dnaSequence = str(request.form['dnaSeq']).upper()

    rnaSequence = "".upper()
    
    for letter in dnaSequence:
        if letter not in dict:
            pass
        else:
            rnaSequence += dict[letter]

    #flash = print
    flash(rnaSequence)

    #Faut toujours return le template pareil au index
    return render_template("index.html")