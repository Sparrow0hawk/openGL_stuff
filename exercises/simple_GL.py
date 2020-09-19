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

def showScreen():
    """ 
    Initial function for creating a window in which graphics can be shown
    """
     # clear screen, returns while screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

if __name__ == '__main__':
    main()