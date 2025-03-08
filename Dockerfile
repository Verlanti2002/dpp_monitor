# Usa un'immagine Python aggiornata e più leggera
FROM python:3.12-slim

# Imposta la directory di lavoro nel container
WORKDIR /usr/local/app

# Installa le dipendenze di sistema (incluse curl e apt-utils)
RUN apt update && apt install -y curl && rm -rf /var/lib/apt/lists/*

# Copia solo il file delle dipendenze (per ottimizzare la cache)
COPY requirements.txt .

# Installa le dipendenze senza cache
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto del progetto
COPY . .

# Esponi la porta di Django (8000)
EXPOSE 8000

# Crea un utente non root per sicurezza
RUN useradd -m appuser
USER appuser

# Comando per avviare il server Django con Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "dpp_monitor.wsgi:application"]