import sys
from OpenGL.GL import *
from PyQt5.QtWidgets import QOpenGLWidget, QApplication


class PyQtOpenGL(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.paint_0 = False        
        self.paint_1 = False
        self.paint_2 = False


    def initializeGL(self):         
        glClearColor(1.0, 1.0, 0.0, 0.0) 
        glClear(GL_COLOR_BUFFER_BIT)     

    def resizeGL(self, w, h):            
        glMatrixMode(GL_PROJECTION)      
        glLoadIdentity()                 
        glOrtho(-50, 50, -50, 50, -50.0, 50.0)  
                                                
        glViewport(0, 0, w, h)                  
        
    def paintGL(self):                  
        if self.paint_0:       
            glColor3f(1.0, 0.0, 0.0)    
            glRectf(-5, -5, 5, 5)       
 
        if self.paint_1: 
            glColor3f(0.0, 1.0, 0.0)    
            x=10
            y=10
            self.draw_loop(x, y)
        
        if self.paint_2: 
            glColor3f(0.0, 0.0, 0.0)
            x=5
            y=5
            self.draw_loop(x, y)
                            
    def draw_loop(self, x, y, incr=10):
        for _ in range(5):
            self.draw_square_lines(x, y)
            x += incr
            y += incr

    def draw_square_lines(self, x=10, y=10, z=0):
        glBegin(GL_LINES)         
        glVertex3f(x, y, z)       
        glVertex3f(x, -y, z)      
         
        glVertex3f(x, -y, z)
        glVertex3f(-x, -y, z)
         
        glVertex3f(-x, -y, z)
        glVertex3f(-x, y, z)
         
        glVertex3f(-x, y, z)
        glVertex3f(x, y, z)
        glEnd()      



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = PyQtOpenGL()
    widget.show()
    app.exec_()
