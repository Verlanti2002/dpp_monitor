#!/bin/bash

URL="http://192.168.49.2:30080/api/events/"
DATA='{"event_type": "test", "payload": {"product_id": 123, "name": "Test Product"}}'

n_request=10

for i in $(seq 1 $n_request); do
  curl -X POST "$URL" \
       -H "Content-Type: application/json" \
       -d "$DATA" > /dev/null 2>&1 &
done

wait  # Attende il completamento di tutti i processi in background
echo "Test completato: $n_request richieste inviate"