import random
import os # MODULO OS
from flask import Flask, render_template
app = Flask(__name__)


# LIST COMPREHNSION
frutti = [
  [nome_file, nome_file.split(".")[0], "Guarda che bel frutto", i]
  for i, nome_file in enumerate(os.listdir("static/images"))
]
def carica_descrizioni():
   for f in frutti:
      nome = f[1][:-1]
      try:
        with open(f"descrizioni/{nome}.txt","r") as finn:
          descrizione = finn.read()
          f[2] = descrizione
      except FileNotFoundError:
         continue
carica_descrizioni()
   
articoli = ["il", "lo", "la", "l'", "i", "gli", "le" ]
@app.route('/')
def index():
    i = random.randint(0, len(frutti) - 1)
    nome_file, frutto_random, _, _ = frutti[i]

    try:
      j = int(frutto_random[-1])
    except:
      j = 0
    articolo = articoli[j]
    frutto_random = frutto_random[:-1]
    
    return render_template('index.html', 
                           nome_file = nome_file,
                           frutto_random=frutto_random,
                             frutti=frutti,
                             articolo = articolo,
                             random = random
                            )

@app.route("/descrizioni")
def descrizioni():
   return render_template("descrizioni.html")
 # descr =  

@app.route("/descrizione/<int:frutto_idx>")
def descrizione(frutto_idx):
    nome_file, frutto, descr, _ = frutti[frutto_idx]

    try:
      j = int(frutto[-1])
    except:
      j = 0
    articolo = articoli[j]
    frutto = frutto[:-1]
    return render_template('descrizioni.html', 
                           nome_file = nome_file,
                           frutto_random=frutto,
                             descrizione=descr,
                             articolo = articolo,
                            )

app.run(debug=True)

