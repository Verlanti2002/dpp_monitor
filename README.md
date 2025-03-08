# Digital Product Passport - Monitor

## 📌 Descrizione
Il **DPP Monitor** (“Digital Product Passport Monitor”) è un microservizio che riceve, interpreta e manipola eventi JSON inviati dal **DPP Browser**. Questo sistema è containerizzato con **Docker** e scalabile con **Kubernetes** per garantire l'affidabilità e la gestione del carico in caso di elevato numero di richieste.

## 📌 Tecnologie Utilizzate
- **Python 3.10+** - Linguaggio di programmazione
- **Django REST Framework** - API REST per la gestione degli eventi
- **Docker Engine** - Containerizzazione del microservizio
- **Kubernetes** - Orchestrazione e scalabilità dei container (minikube e kubectl)


## 📌 Setup dell'Ambiente di Sviluppo
### 1️⃣ Clonare il Repository
```bash
git clone https://github.com/Verlanti2002/dpp-monitor.git
cd dpp-monitor
