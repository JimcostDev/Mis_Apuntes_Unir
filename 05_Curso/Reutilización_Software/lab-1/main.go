package main

import (
	"fmt"
	"strings"
)

// ------------------ INTERFACES PRINCIPALES -------------------
// Interfaz común para todos los informes
type Report interface {
	Procesar() // Todos los informes deben implementar este método
}

// Interfaz abstracta de la fábrica
type ReportFactory interface {
	CrearFactura() Report
	CrearCompra() Report
	CrearPedido() Report // Nuevo tipo añadido en la evolución
}

// ------------------ INFORMES ENTRADA -------------------
type EntradaFactura struct{}

func (e EntradaFactura) Procesar() {
	fmt.Println("[ENTRADA] Procesando factura...")
}

type EntradaCompra struct{}

func (e EntradaCompra) Procesar() {
	fmt.Println("[ENTRADA] Procesando compra...")
}

type EntradaPedido struct{} // Nuevo tipo

func (e EntradaPedido) Procesar() {
	fmt.Println("[ENTRADA] Procesando pedido...")
}

// ------------------ INFORMES SALIDA -------------------
type SalidaFactura struct{}

func (s SalidaFactura) Procesar() {
	fmt.Println("[SALIDA] Procesando factura...")
}

type SalidaCompra struct{}

func (s SalidaCompra) Procesar() {
	fmt.Println("[SALIDA] Procesando compra...")
}

// ------------------ INFORMES MIXTOS (Nueva categoría) -------------------
type MixtaFactura struct{}

func (m MixtaFactura) Procesar() {
	fmt.Println("[MIXTA] Procesando factura...")
}

type MixtaCompra struct{}

func (m MixtaCompra) Procesar() {
	fmt.Println("[MIXTA] Procesando compra...")
}

// ------------------ FÁBRICAS CONCRETAS -------------------
// Fábrica para informes de ENTRADA
type FabricaEntrada struct{}

func (f FabricaEntrada) CrearFactura() Report { return EntradaFactura{} }
func (f FabricaEntrada) CrearCompra() Report  { return EntradaCompra{} }
func (f FabricaEntrada) CrearPedido() Report  { return EntradaPedido{} }

// Fábrica para informes de SALIDA
type FabricaSalida struct{}

func (f FabricaSalida) CrearFactura() Report { return SalidaFactura{} }
func (f FabricaSalida) CrearCompra() Report  { return SalidaCompra{} }
func (f FabricaSalida) CrearPedido() Report {
	panic("Operación no soportada: SALIDA no tiene pedidos")
}

// Fábrica para informes MIXTOS (Nueva fábrica)
type FabricaMixta struct{}

func (f FabricaMixta) CrearFactura() Report { return MixtaFactura{} }
func (f FabricaMixta) CrearCompra() Report  { return MixtaCompra{} }
func (f FabricaMixta) CrearPedido() Report {
	panic("Operación no soportada: MIXTA no tiene pedidos")
}

// ------------------ CLIENTE/FACTORY SELECTOR -------------------
func obtenerFabrica(prefijo string) ReportFactory {
	switch prefijo {
	case "ENT":
		return FabricaEntrada{}
	case "SAL":
		return FabricaSalida{}
	case "MIX": // Nueva categoría añadida
		return FabricaMixta{}
	default:
		panic("Categoría de informe desconocida: " + prefijo)
	}
}

// ------------------ MAIN -------------------
func main() {
	archivos := []string{
		"ENT_FAC_001.txt",
		"ENT_COM_002.txt",
		"ENT_PED_003.txt",
		"SAL_FAC_004.txt",
		"SAL_COM_005.txt",
		"MIX_FAC_006.txt",
		"MIX_COM_007.txt",
	}

	for _, archivo := range archivos {
		// Extraer componentes del nombre
		partes := strings.Split(archivo, "_")
		if len(partes) < 3 {
			fmt.Printf("Nombre inválido: %s\n", archivo)
			continue
		}

		categoria := partes[0]
		tipo := partes[1]

		// Obtener fábrica correspondiente
		fabrica := obtenerFabrica(categoria)

		// Crear informe según el tipo
		var informe Report
		switch tipo {
		case "FAC":
			informe = fabrica.CrearFactura()
		case "COM":
			informe = fabrica.CrearCompra()
		case "PED": // Manejo del nuevo tipo
			informe = fabrica.CrearPedido()
		default:
			fmt.Printf("Tipo de informe no reconocido: %s\n", tipo)
			continue
		}

		// Procesar informe
		fmt.Printf("Procesando %s\n", archivo)
		informe.Procesar()
		fmt.Println("------------------")
	}
}
