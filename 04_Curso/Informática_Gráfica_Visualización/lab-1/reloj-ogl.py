import glfw
from OpenGL.GL import *
import math
import time

# Constantes
WINDOW_SIZE = 800
CLOCK_RADIUS = 0.8
HOUR_HAND_LENGTH = 0.5
MINUTE_HAND_LENGTH = 0.7
SECOND_HAND_LENGTH = 0.8

def draw_circle(radius, segments, color, filled=False):
    glColor3f(*color)
    if filled:
        glBegin(GL_TRIANGLE_FAN)
    else:
        glBegin(GL_LINE_LOOP)
    
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

def draw_hand(length, angle, width, color):
    glColor3f(*color)
    glLineWidth(width)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    x = length * math.sin(angle)
    y = length * math.cos(angle)
    glVertex2f(x, y)
    glEnd()

def draw_number(number, x, y, scale):
    glColor3f(0, 0, 0)  # Color negro para los números
    glLineWidth(2)  # Grosor de las líneas para los números

    # Definiciones de los números usando líneas
    numbers = {
        0: [(0,1,1,1), (1,1,1,0), (1,0,1,-1), (1,-1,0,-1), (0,-1,0,1)],
        1: [(0,1,1,1), (1,1,1,-1)],
        2: [(0,1,1,1), (1,1,1,0), (1,0,0,0), (0,0,0,-1), (0,-1,1,-1)],
        3: [(0,1,1,1), (1,1,1,-1), (0,0,1,0)],
        4: [(0,1,0,0), (0,0,1,0), (1,1,1,-1)],
        5: [(1,1,0,1), (0,1,0,0), (0,0,1,0), (1,0,1,-1), (1,-1,0,-1)],
        6: [(1,1,0,1), (0,1,0,-1), (0,-1,1,-1), (1,-1,1,0), (1,0,0,0)],
        7: [(0,1,1,1), (1,1,1,-1)],
        8: [(0,1,1,1), (1,1,1,-1), (0,-1,1,-1), (0,1,0,-1), (0,0,1,0)],
        9: [(1,-1,1,1), (1,1,0,1), (0,1,0,0), (0,0,1,0)]
    }

    glPushMatrix()
    glTranslatef(x, y, 0)
    glScalef(scale, scale, scale)

    if number < 10:
        for line in numbers[number]:
            glBegin(GL_LINES)
            glVertex2f(line[0], line[1])
            glVertex2f(line[2], line[3])
            glEnd()
    else:
        # Dibujar las decenas
        for line in numbers[1]:
            glBegin(GL_LINES)
            glVertex2f(line[0] - 1.5, line[1])
            glVertex2f(line[2] - 1.5, line[3])
            glEnd()
        # Dibujar las unidades
        for line in numbers[number - 10]:
            glBegin(GL_LINES)
            glVertex2f(line[0] + 0.5, line[1])
            glVertex2f(line[2] + 0.5, line[3])
            glEnd()

    glPopMatrix()

def draw_numbers():
    for i in range(1, 13):
        angle = math.pi / 2 - 2 * math.pi * i / 12
        x = 0.78 * CLOCK_RADIUS * math.cos(angle)
        y = 0.78 * CLOCK_RADIUS * math.sin(angle)
        draw_number(i, x, y, 0.06)  # Redujimos la escala de 0.1 a 0.06

def draw_clock(hour, minute, second):
    # Fondo del reloj
    draw_circle(CLOCK_RADIUS, 100, (0.95, 0.95, 0.95), filled=True)
    
    # Borde del reloj
    draw_circle(CLOCK_RADIUS, 100, (0.1, 0.1, 0.1))
    
    # Marcas de las horas y minutos
    for i in range(60):
        angle = 2 * math.pi * i / 60
        inner_radius = 0.9 * CLOCK_RADIUS if i % 5 == 0 else 0.95 * CLOCK_RADIUS
        outer_radius = 0.98 * CLOCK_RADIUS
        inner_x = inner_radius * math.sin(angle)
        inner_y = inner_radius * math.cos(angle)
        outer_x = outer_radius * math.sin(angle)
        outer_y = outer_radius * math.cos(angle)
        glLineWidth(2 if i % 5 == 0 else 1)
        glBegin(GL_LINES)
        glVertex2f(inner_x, inner_y)
        glVertex2f(outer_x, outer_y)
        glEnd()
    
    draw_numbers()
    
    # Centro del reloj
    draw_circle(0.02, 20, (0, 0, 0), filled=True)
    
    # Manecillas
    hour_angle = 2 * math.pi * ((hour % 12 + minute / 60) / 12)
    minute_angle = 2 * math.pi * (minute / 60)
    second_angle = 2 * math.pi * (second / 60)
    
    draw_hand(HOUR_HAND_LENGTH, hour_angle, 6, (0.2, 0.2, 0.2))
    draw_hand(MINUTE_HAND_LENGTH, minute_angle, 4, (0.3, 0.3, 0.3))
    draw_hand(SECOND_HAND_LENGTH, second_angle, 2, (0.7, 0.2, 0.2))

def main():
    if not glfw.init():
        raise Exception("GLFW no inicializado correctamente!")
    
    window = glfw.create_window(WINDOW_SIZE, WINDOW_SIZE, "Reloj Analógico", None, None)
    if not window:
        glfw.terminate()
        raise Exception("GLFW ventana no creada!")
    
    glfw.make_context_current(window)
    
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        glOrtho(-1, 1, -1, 1, -1, 1)
        
        current_time = time.localtime()
        hour, minute, second = current_time.tm_hour, current_time.tm_min, current_time.tm_sec
        
        draw_clock(hour, minute, second)
        
        glfw.swap_buffers(window)
        glfw.poll_events()
    
    glfw.terminate()

if __name__ == "__main__":
    main()