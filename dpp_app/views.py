import sys
import json
import uuid
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import api_view


"""
Oracle Function
Funzione che permette di stabilire la validità di un determinato evento
param: data Informazioni relative ad un evento
return: True se l'evento è riconosciuto come valido, false altrimenti   
"""
def oracle_function(data):
    return True

# Create your views here.
"""
Check Event
Funzione che estrae i dati dalla HTTP Request, applica l'oracle function all'evento e restituisce l'esito
param: request HTTP Request
return: HTTP Response
"""
@api_view(['POST'])
def check_event(request):
    try:
        # Estrae i dati JSON dalla richiesta
        data = request.data

        # Generazione di un ID univoco per identificare l'evento
        event_id = str(uuid.uuid4())

        status = oracle_function(data)

        event_info = {
            "event_id": event_id,
            "data": data,
            "status": "valid" if status else "invalid"
        }

        # Formattazione JSON in modo leggibile
        formatted_json = json.dumps(event_info, indent=4)

        # Stampa in console
        print(formatted_json, flush=True, file=sys.stdout)

        if status:
            return Response(event_info, status=200) # Dati validi, HTTP 200 OK
        else:
            return Response(event_info, status=400) # Dati non validi, HTTP 400 Bad Request
    except json.JSONDecodeError as e:
        # Gestione errori specifici di parsing JSON
        error_message = f"Errore nel parsing JSON: {str(e)}"
        print(error_message, flush=True, file=sys.stderr)
        return Response({"error": "Formato JSON non valido"}, status=400)
    except ValidationError as e:
        # Gestione errori di validazione
        error_message = f"Errore di validazione: {str(e)}"
        print(error_message, flush=True, file=sys.stderr)
        return Response({"error": "Errore di validazione dei dati"}, status=400)
    except Exception as e:
        # Gestione di altri errori imprevisti
        error_message = f"Errore interno del server: {str(e)}"
        print(error_message, flush=True, file=sys.stderr)
        return Response({"error": "Errore interno del server"}, status=500)
