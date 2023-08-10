  GNU nano 6.2                                            Dockerfile
# Usa l'immagine di Python 3.6 come base
FROM python:3.6

# Copia il codice sorgente o gli script all'interno del contenitore
COPY main.py /app/
COPY utils.py /app/
COPY credentials.env  /app/
COPY static /app/stat

# Imposta la directory di lavoro all'interno del contenitore
WORKDIR /app

# Installa le dipendenze Python
RUN pip install discord.py
RUN pip install python-dotenv

# Esegui il tuo comando principale o avvia l'interprete Python
CMD ["python", "main.py"]


















