@echo off
:: Este script añade todos los archivos, pide un comentario y hace push

:: Navegar al directorio del repositorio, si es necesario
:: cd C:\ruta\de\tu\repositorio

:: Hacer git add .
git add .

:: Pedir el comentario del commit al usuario
set /p commitMsg="Introduce el mensaje del commit: "

:: Hacer git commit con el mensaje proporcionado
git commit -m "%commitMsg%"

:: Hacer git push
git push

pause
