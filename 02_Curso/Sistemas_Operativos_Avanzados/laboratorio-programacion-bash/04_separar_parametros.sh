#!/bin/bash

# Verificar si se han proporcionado argumentos
if [ $# -eq 0 ]; then
  echo "No se han proporcionado argumentos."
  exit 1
fi

# Concatenar los argumentos separados por comas
args=$(IFS=','; echo "$*")

# Imprimir los argumentos separados por comas
echo "Los argumentos separados por comas son: $args"