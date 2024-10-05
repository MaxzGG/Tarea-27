#!/bin/bash

# Verifica si el comando netstat está disponible
if ! command -v netstat &> /dev/null
then
    echo "Error: netstat no está instalado."
    exit 1
fi

# Mostrar las conexiones en estado ESTABLISHED
netstat -tn 2>/dev/null | grep ESTABLISHED