import os
import random
import discord
from dotenv import load_dotenv

load_dotenv(r'C:\Users\chris\OneDrive\Desktop\cred\credentials.env')

"""
qui vanno le funzioni esterne senza riempire il main é come se fosse un oggetto statico in java o una libreria .h in c
va importata nel main con

import utils
se vuoi importare tutto e richiamare le funzioni con utils.metodo()

from utils import *
importi tutto e richiami come funzione(), sconsigliato perché da problemi di leak

from utils import funzione1, funzione2, funzione3
puoi farlo ma é scomodo consigliato anche questo se vuoi rendere elegante il codice ma un pó merda le librerie
"""



def prendiFoto() -> discord.File or str:
    try:

        PATH_CAT = os.environ.get("PATH_CAT_FILE")

        foto = [f for f in os.listdir(PATH_CAT) if os.path.isfile(os.path.join(PATH_CAT, f))]

        randFoto = random.choice(foto)
        fotoPath = os.path.join(PATH_CAT, randFoto)
        ffoto = discord.File(fotoPath)

        return ffoto
    except Exception as e:
        return f"c'é stato il seguente errore {e}"

def  prendiFrase(path: str) -> str:
    frasi: list[str]  = []
    try:
        with open(path) as f:
            for line in f:
                frasi.append(line)

        return random.choice(frasi)
    except Exception as e:
        return f"c'é stato il seguente errore: {e}"

def formattaInsulto(frase: str, arg: str) -> str:
    frase = frase.replace("{PLACEHOLDER}", arg)
    return frase



