import tkinter as tk
from OpenGL.GL import *
from OpenGL.GLU import *
from pyopengltk import OpenGLFrame

class CubeViewer(OpenGLFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.animate = 1
        self.init = False
        
    def initgl(self):
        """Método de inicialización del contexto OpenGL"""
        if not self.init:
            glClearColor(0.0, 0.0, 0.0, 0.0)
            glEnable(GL_DEPTH_TEST)
            glShadeModel(GL_SMOOTH)
            self.init = True
        
    def draw_cube(self):
        """Método para dibujar el cubo"""
        vertices = [
            [-0.5, -0.5,  0.5], [ 0.5, -0.5,  0.5],
            [ 0.5,  0.5,  0.5], [-0.5,  0.5,  0.5],
            [-0.5, -0.5, -0.5], [ 0.5, -0.5, -0.5],
            [ 0.5,  0.5, -0.5], [-0.5,  0.5, -0.5],
        ]
        
        edges = [
            [0, 1], [1, 2], [2, 3], [3, 0],
            [4, 5], [5, 6], [6, 7], [7, 4],
            [0, 4], [1, 5], [2, 6], [3, 7]
        ]
        
        glBegin(GL_LINES)
        glColor3f(1.0, 1.0, 1.0)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()

    def redraw(self, *args, **kwargs):
        """Método principal de renderizado"""
        if not self.init:
            self.initgl()
            
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        viewport_width = self.width // 2
        viewport_height = self.height // 2
        
        # 1. Proyección Ortogonal
        glViewport(0, viewport_height, viewport_width, viewport_height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-2, 2, -2, 2, -10, 10)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glRotatef(30, 1, 1, 0)
        self.draw_cube()
        
        # 2. Proyección Gabinete
        glViewport(viewport_width, viewport_height, viewport_width, viewport_height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-2, 2, -2, 2, -10, 10)
        cabinet = [
            1.0, 0.0, -0.3536, 0.0,
            0.0, 1.0, -0.3536, 0.0,
            0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0
        ]
        glMultMatrixf(cabinet)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glRotatef(30, 1, 1, 0)
        self.draw_cube()
        
        # 3. Proyección Perspectiva Simétrica
        glViewport(0, 0, viewport_width, viewport_height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, viewport_width/viewport_height, 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, 0, -3)
        glRotatef(30, 1, 1, 0)
        self.draw_cube()
        
        # 4. Proyección Perspectiva Oblicua
        glViewport(viewport_width, 0, viewport_width, viewport_height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-1, 1, -1, 1, 2, 10)
        oblique = [
            1.0, 0.0, 0.3, 0.0,
            0.0, 1.0, 0.3, 0.0,
            0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0
        ]
        glMultMatrixf(oblique)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, 0, -5)
        glRotatef(30, 1, 1, 0)
        self.draw_cube()
        
        if self.animate:
            self.after(10, self.redraw)

def main():
    root = tk.Tk()
    root.title("Proyecciones 3D - Cubo")
    
    viewer = CubeViewer(root, width=800, height=600)
    viewer.pack(fill=tk.BOTH, expand=tk.YES)
    
    viewer.animate = 1
    viewer.after(100, viewer.redraw)
    
    root.mainloop()

if __name__ == "__main__":
    main()