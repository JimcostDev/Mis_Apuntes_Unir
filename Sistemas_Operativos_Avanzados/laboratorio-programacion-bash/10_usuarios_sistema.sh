#!/bin/bash

# Obtener la lista de usuarios activos
usuarios_conectados=$(who | awk '{print $1}')

# Verificar si el primer parámetro coincide con algún usuario conectado
usuario="$1"
if [[ " ${usuarios_conectados[@]} " =~ " ${usuario} " ]]; then
    echo "SI"
else
    echo "NO"
fi
