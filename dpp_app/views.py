import sys
import json
import uuid
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def receive_event(request):
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

        return Response(event_info, status=201)
    except json.JSONDecodeError as e:
        # Gestione errori specifici di parsing JSON
        error_message = f"Errore nel parsing JSON: {str(e)}"
        print(error_message, flush=True, file=sys.stderr)
        return Response({"error": "Formato JSON non valido"}, status=400)
    except Exception as e:
        # Gestione di altri errori imprevisti
        error_message = f"Errore interno del server: {str(e)}"
        print(error_message, flush=True, file=sys.stderr)
        return Response({"error": "Errore interno del server"}, status=500)