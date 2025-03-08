import sys
import json # Libreria per manipolare dati JSON
import logging
import uuid
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Configurazione del logger
logger = logging.getLogger(__name__)

# Create your views here.
@api_view(['POST'])
def receive_event(request):
    # API che riceve eventi in JSON, li interpreta e li stampa in console

    try:
        # Estrae i dati JSON dalla richiesta
        data = request.data

        # Generazione di un ID univoco per il log dell'evento
        event_id = str(uuid.uuid4())

        event_info = {
            "message": "Evento ricevuto con successo",
            "event_id": event_id,
            "data": data
        }

        # Formattazione JSON in modo leggibile
        formatted_json = json.dumps(event_info, indent=4)

        # Stampa in console e registra nei log
        print(formatted_json, flush=True, file=sys.stdout)
        logger.info(formatted_json)

        # Restituisce la risposta direttamente con l'oggetto event_info (senza dump manuale)
        return Response(event_info, status=201)
    except json.JSONDecodeError as e:
        # Gestione errori specifici di parsing JSON
        error_message = f"Errore nel parsing JSON: {str(e)}"
        print(error_message, flush=True, file=sys.stderr)
        logger.error(error_message)
        return Response({"error": "Formato JSON non valido"}, status=400)
    except Exception:
        # Gestione di altri errori imprevisti
        logger.exception("Errore durante l'elaborazione dell'evento") # Stack trace dettagliato
        return Response({"error": "Errore interno del server"}, status=500)