import tkinter as tk
import math
import time

# Constantes
WINDOW_SIZE = 400
CLOCK_RADIUS = 150
HOUR_HAND_LENGTH = 80
MINUTE_HAND_LENGTH = 110
SECOND_HAND_LENGTH = 130

class AnalogClock(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master, width=WINDOW_SIZE, height=WINDOW_SIZE, bg='white')
        self.pack()
        self.center = WINDOW_SIZE // 2
        self.update_clock()

    def draw_hand(self, length, angle, width, color):
        x = self.center + length * math.sin(angle)
        y = self.center - length * math.cos(angle)
        self.create_line(self.center, self.center, x, y, width=width, fill=color)

    def draw_clock_face(self):
        # Dibujar el círculo del reloj
        self.create_oval(self.center - CLOCK_RADIUS, self.center - CLOCK_RADIUS,
                         self.center + CLOCK_RADIUS, self.center + CLOCK_RADIUS,
                         outline='black', width=4)

        # Dibujar los números del reloj
        for i in range(1, 13):
            angle = math.pi / 2 - 2 * math.pi * i / 12
            x = self.center + 0.75 * CLOCK_RADIUS * math.cos(angle)
            y = self.center - 0.75 * CLOCK_RADIUS * math.sin(angle)
            self.create_text(x, y, text=str(i), font=('Arial', 14))

        # Dibujar marcas de las horas y minutos
        for i in range(60):
            angle = 2 * math.pi * i / 60
            inner_radius = 0.9 * CLOCK_RADIUS if i % 5 == 0 else 0.95 * CLOCK_RADIUS
            outer_radius = CLOCK_RADIUS
            x1 = self.center + inner_radius * math.sin(angle)
            y1 = self.center - inner_radius * math.cos(angle)
            x2 = self.center + outer_radius * math.sin(angle)
            y2 = self.center - outer_radius * math.cos(angle)
            width = 2 if i % 5 == 0 else 1
            self.create_line(x1, y1, x2, y2, width=width)

    def update_clock(self):
        self.delete('all')  # Limpiar la pantalla
        self.draw_clock_face()

        # Obtener la hora actual
        current_time = time.localtime()
        hour, minute, second = current_time.tm_hour % 12, current_time.tm_min, current_time.tm_sec

        # Calcular ángulos para cada manecilla
        hour_angle = 2 * math.pi * (hour + minute / 60) / 12
        minute_angle = 2 * math.pi * minute / 60
        second_angle = 2 * math.pi * second / 60

        # Dibujar manecillas
        self.draw_hand(HOUR_HAND_LENGTH, hour_angle, 6, 'black')
        self.draw_hand(MINUTE_HAND_LENGTH, minute_angle, 4, 'blue')
        self.draw_hand(SECOND_HAND_LENGTH, second_angle, 2, 'red')

        # Actualizar cada 1000 milisegundos (1 segundo)
        self.after(1000, self.update_clock)

def main():
    root = tk.Tk()
    root.title("Reloj Analógico")
    clock = AnalogClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()
