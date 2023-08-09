import os
import random
import discord

""""

qui vanno le funzioni esterne senza riempire il main é come se fosse un oggetto statico in java o una libreria .h in c
va importata nel main con

import utils
se vuoi importare tutto e richiamare le funzioni con utils.metodo()

from utils import *
importi tutto e richiami come funzione(), sconsigliato perché da problemi di leak

from utils import funzione1, funzione2, funzione3
puoi farlo ma é scomodo consigliato anche questo se vuoi rendere elegante il codice ma un pó merda le librerie

"""

def prendiFoto():
    dir = os.path.join('static', 'photo', 'gatti')

    foto = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]

    randFoto = random.choice(foto)
    fotoPath = os.path.join(dir, randFoto)
    ffoto = discord.File(fotoPath)

    return ffoto
