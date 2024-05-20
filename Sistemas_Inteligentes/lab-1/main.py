class JugadorFutbol:
    def __init__(self, nombre, posicion, energia):
        self.nombre = nombre
        self.posicion = posicion
        self.energia = energia

    def pasar_pelota(self, companero):
        if self.energia > 20:
            print(f"{self.nombre} pasa la pelota a {companero.nombre}.")
            self.energia -= 10
        else:
            print(f"{self.nombre} está demasiado cansado para pasar la pelota.")

    def disparar_a_gol(self):
        if self.energia > 30:
            print(f"{self.nombre} dispara a gol.")
            self.energia -= 20
        else:
            print(f"{self.nombre} está demasiado cansado para disparar a gol.")

    def defender(self):
        if self.energia > 15:
            print(f"{self.nombre} defiende.")
            self.energia -= 5
        else:
            print(f"{self.nombre} está demasiado cansado para defender.")

# Crear jugadores
jugador1 = JugadorFutbol("Ronaldo", "Delantero", 40)
jugador2 = JugadorFutbol("Kevin", "Centrocampista", 60)
jugador3 = JugadorFutbol("Cris", "Centrocampista", 10)

# Simular acciones
jugador2.pasar_pelota(jugador1)
jugador1.disparar_a_gol()
jugador3.defender()
