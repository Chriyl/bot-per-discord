# Usa l'immagine di Ubuntu 16.04 come base
FROM ubuntu:16.04

# Aggiorna il sistema e installa le dipendenze
RUN apt-get update && \
    apt-get install -y python3.6 python3.6-dev python3-pip

# Imposta Python 3.6 come l'interprete di default
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1

# Copia il codice sorgente o gli script all'interno del contenitore
# Puoi usare il comando COPY per copiare i tuoi file nel contenitore
COPY main.py
COPY utils.py
COPY requirements.txt


# Imposta la directory di lavoro all'interno del contenitore
# WORKDIR /path/to/your/code
RUN pip install requirements
# Esegui il tuo comando principale o avvia l'interprete Python
CMD ["python3", "main.py"]
