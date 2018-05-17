import OpenGL.GL as GL
import OpenGL.GLU as GLU
import OpenGL.GLUT as GLUT
import sys

x1, x2, y1, y2 = 0, 0, 0, 0

def dda():
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) > abs(dy):
        step = abs(dx)
    else:
        step = abs(dy)
    
    x_in = dx / step
    y_in = dy / step
    x, y = x1, y1
    GL.glBegin(GL_POINTS)
    GL.glVertex2i(x, y)
    GL.glEnd()

    for k in xrange(step):
        x += x_in
        y += y_in

        GL.glBegin(GL_POINTS)
        GL.glVertex2i(x, y)
        GL.glEnd()
    
    GL.glFlush()

def initialize():
    GL.glClearColor(0.7, 0.7, 0.7, 0.7)
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()
    GLU.gluOrtho2D(-100, 100, -100, 100)

GLUT.glutInit()
GLU.gluInitDisplayMode(GLUT.GLUT_SINGLE | GLUT.GLUT_RGB)
GLUT.glutInitWIndowSize(500, 500)
GLUT.glutInitWIndowPosition(100, 100)
GLUT.glutCreateWindow("DDA Sistemas Graficos")
initialize()
GLUT.glutDisplayFunc(dda)
GLUT.glutMainLoop()
