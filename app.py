from flask import Flask, render_template, request, flash

#Initialiser l'application; creer classe pour notre application
app = Flask(__name__)
app.secret_key = "###"

#Represente la derniere partie du URL (ex: /page1 , /stats, /store3, etc.)
#Doit associer cette route avec une fonction
@app.route("/translate")
def index():
    #Flash un message; liee aux % message % de index.html
    flash("RNA seq")
    return render_template("index.html")

def getProtein(seq):

    proteinDict = {
            'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
            'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
            'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
            'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
            'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
            'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
            'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
            'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
            'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
            'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
            'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
            'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
            'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
            'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
            'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
        }

    protein = []

    try:
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]

            if len(codon) == 3:
                protein += proteinDict[codon]
    except:
        pass

    final_protein = "".join(protein)

    return final_protein

###CODE PYTHON###
#@app.route("/translate", methods=["POST", "GET"])
#def dropdown():
 #   orfs = [1,2,3]
    
  #  return render_template('index.html', orfs=orfs)

##CODE PYTHON##
@app.route("/translate", methods=["POST", "GET"])
def translate():

    dict = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}

    dnaSequence = str(request.form['dnaSeq']).upper()

    rnaSequence = "".upper()
    
    for letter in dnaSequence:
        if letter not in dict:
            rnaSequence = "ATGC-Only."
            break
        else:
            rnaSequence += dict[letter]

    #flash = print
    #flash(rnaSequence)

    protSeq = getProtein(dnaSequence)

    #Faut toujours return le template pareil au index
    return render_template("index.html", rna = rnaSequence, prot = protSeq)
