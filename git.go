package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"strings"
)

func main() {
	// Ejecutar git add .
	addCmd := exec.Command("git", "add", ".")
	if err := addCmd.Run(); err != nil {
		fmt.Println("Error al ejecutar git add:", err)
		return
	}

	// Obtener mensaje del commit del usuario
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Introduce el mensaje del commit: ")
	mensajeCommit, err := reader.ReadString('\n')
	if err != nil {
		fmt.Println("Error al leer el mensaje del commit:", err)
		return
	}

	// Eliminar el carácter de nueva línea del mensaje
	mensajeCommit = strings.TrimSpace(mensajeCommit)

	// Ejecutar git commit
	commitCmd := exec.Command("git", "commit", "-m", mensajeCommit)
	if err := commitCmd.Run(); err != nil {
		fmt.Println("Error al ejecutar git commit:", err)
		return
	}

	// Ejecutar git push
	pushCmd := exec.Command("git", "push")
	if err := pushCmd.Run(); err != nil {
		fmt.Println("Error al ejecutar git push:", err)
		return
	}

	fmt.Println("\n¡Operaciones de git completadas exitosamente!")
	fmt.Println("Presiona Enter para salir...")
	bufio.NewReader(os.Stdin).ReadBytes('\n')
}
