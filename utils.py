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