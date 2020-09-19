import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
print('Imports successful!')

def main():

    glutInit() # create a glut instance
    glutInitDisplayMode(GLUT_RGBA) # colour display mode
    glutInitWindowSize(500, 500) # height and width of window
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("OpenGL Coding practise")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)

    glutMainLoop()

    return None

def square():

    glBegin(GL_QUADS)
    glVertex2f(100, 100)
    glVertex2f(200, 100)
    glVertex2f(200, 200)
    glVertex2f(100, 200)
    glEnd()

def iterate():
    glViewport(0,0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    """ 
    Initial function for creating a window in which graphics can be shown
    """
     # clear screen, returns while screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    square()
    glutSwapBuffers()


if __name__ == '__main__':
    main()