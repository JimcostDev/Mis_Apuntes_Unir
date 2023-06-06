#!/bin/bash

if [ $# -gt 0 ]; then
    echo "Hola $1, bienvenido a: $2"
else
    echo "Se requiere al menos un parámetro."
    echo "Uso: $0 <nombre> <lugar>"
fi
