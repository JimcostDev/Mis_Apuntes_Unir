#!/bin/bash
#Programa para validar procesos, memoria, recursos, variables.

echo ""
echo "----------- PROGRAMA VALIDACIÓN RECURSOS -----------"
echo ""
opcion=0

while :
do
        #Limpiar Pantalla
        clear
        echo " ----- Menú Principal ------ "
        echo ""
        echo "1)Proceso Actuales "
        echo "2)Memoria Disponible "
        echo "3)Espacio en disco "
        echo "4)Informacion Red"
        echo "5)Variables de entorno configuradas "
        echo "6)Información Programa "
        echo "7)Comprimir Arcivos SH"
        echo "8)Salir "
        echo ""
        #Leer datos de usuario
        read -n1 -p "Ingrese la opción a seleccionar (1 - 8): " opcion
        #Validar opción ingresada
        case $opcion in
                1)
                        echo -e "\n..Procesos Actuales.."
                        ps axu
                        sleep 3
                        ;;
                2)
                        echo -e "\n..Memoria Disponible.."
                        free
                        sleep 3
                        ;;
                3)
                        echo -e "\n..Espacion en disco.."
                        df -h
                        sleep 3
                        ;;
                4)
                        echo -e "\n..Información Red.."
                        ifconfig -a
                        sleep 3
                        ;;
                5)
                        echo -e "\n..Variables de Entorno Configuradas.."
                        #printenv
                        env -u VAR
                        sleep 3
                        ;;
                6)
                        echo -e "\n..Información Programa.."
                        dpkg -l | more
                        sleep 3
                        ;;
                7)
                        echo -e "\n..Comprimiedo Archivos.."
                        tar -czvf archivosCompresos.tar.gz *
                        echo -e "\n SUCESS!!"
                        sleep 3
                        ;;
                8)
                        echo -e "\n..Bye!!"
                        exit 0
                        ;;
        esac
done