#!/bin/bash

if [ $# -gt 0 ]; then
    source 07_usuarioConectado.sh "$@"
else
    echo "Se requiere al menos un parámetro."
    echo "Uso: $0 <nombre> <lugar>"
fi
