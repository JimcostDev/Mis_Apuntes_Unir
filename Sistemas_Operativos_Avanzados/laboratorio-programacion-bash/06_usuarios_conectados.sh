#!/bin/bash

if [ $# -gt 0 ]; then
    # Obtener la lista de usuarios activos
    usuarios_conectados=$(who | awk '{print $1}')
    
    # Verificar si al menos uno de los parámetros es un usuario conectado
    usuario_valido=false
    for parametro in "$@"; do
        if [[ " ${usuarios_conectados[@]} " =~ " ${parametro} " ]]; then
            usuario_valido=true
            break
        fi
    done

    if $usuario_valido; then
        echo "Hola $1, bienvenido a: $2"
    else
        echo "Los usuarios proporcionados no están conectados al sistema."
        echo "Usuarios conectados: ${usuarios_conectados[*]}"
    fi
else
    echo "Se requiere al menos un parámetro."
    echo "Uso: $0 <nombre> <lugar>"
fi
