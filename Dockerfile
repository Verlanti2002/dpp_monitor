# Usa un'immagine Python aggiornata e più leggera
FROM python:3.12-slim

# Imposta la directory di lavoro nel container
WORKDIR /usr/local/app

# Installa le dipendenze di sistema, curl ed elimina i file temporanei generati durante l'installazione
RUN apt update && apt install -y curl && rm -rf /var/lib/apt/lists/*

# Copia il file delle dipendenze
COPY requirements.txt .

# Installa le dipendenze, impedendo a pip di salvare nella cache i pacchetti
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto del progetto
COPY . .

# Crea un utente non root per sicurezza
RUN useradd -m appuser
USER appuser

# Espone la porta 8000 di Django (il container ascolterà su tale porta)
EXPOSE 8000

# Comando per avviare il server Django con Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "dpp_monitor.wsgi:application"]