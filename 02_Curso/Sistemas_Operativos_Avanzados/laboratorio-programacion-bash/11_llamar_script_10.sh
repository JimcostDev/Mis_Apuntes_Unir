#!/bin/bash

if [ $# -gt 0 ]; then
    usuario_conectado=$(./10_usuarios_sistema "$1")
    
    if [ "$usuario_conectado" = "SI" ]; then
        echo "Hola $1, bienvenido a: $2"
    else
        echo "El usuario proporcionado no está conectado al sistema."
    fi
else
    echo "Se requiere al menos un parámetro."
    echo "Uso: $0 <nombre> <lugar>"
fi
