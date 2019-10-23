"""
Video de rotacion del contenedor
"""

import sys
from OpenGL.GL import *
from PyQt5.QtWidgets import QOpenGLWidget, QApplication
from PyQt5.QtCore import pyqtSignal, QPoint, Qt


class PyQtOpenGL(QOpenGLWidget):
    
    x_rotation_changed = pyqtSignal(int)
    y_rotation_changed = pyqtSignal(int)
    z_rotation_changed = pyqtSignal(int)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.paint_0 = True
        self.paint_1 = True
        self.paint_2 = True
        self.resize_lines = True
        self.resize_lines = False
        
        self.paint_rotation = True
        self.paint_rotation = False
        self.x_rotation = 0        
        self.y_rotation = 0
        self.z_rotation = 0

        self.last_pos = QPoint()

    def normalize_angle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle
    
    
    def set_x_rotation(self, angle):
        angle = self.normalize_angle(angle)
        if angle != self.x_rotation:
            self.x_rotation = angle
            self.x_rotation_changed.emit(angle)
            self.update()

    def set_y_rotation(self, angle):
        angle = self.normalize_angle(angle)
        if angle != self.y_rotation:
            self.y_rotation = angle
            self.y_rotation_changed.emit(angle)
            self.update()

    def set_z_rotation(self, angle):
        angle = self.normalize_angle(angle)
        if angle != self.z_rotation:
            self.z_rotation = angle
            self.z_rotation_changed.emit(angle)
            self.update()
            
    def initializeGL(self):
    
        glClearColor(0.0, 0.0, 1.0, 0.0)
        
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)  
        
        lightPosition = [0, 0, 10, 1.0]  
        glLightfv(GL_LIGHT0, GL_POSITION, lightPosition) 

    def paintGL(self):
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -10.0)
        glRotatef(self.x_rotation / 16.0, 1.0, 0.0, 0.0)
        glRotatef(self.y_rotation / 16.0, 0.0, 1.0, 0.0)
        glRotatef(self.z_rotation / 16.0, 0.0, 0.0, 1.0)
        self.draw()      
   
    def draw(self):
        if self.paint_rotation:
            glColor3f(1.0, 0.0, 0.0)    
            glBegin(GL_QUADS)
            glNormal3f(0, 0, -1)
            glVertex3f(-1 ,-1, 0)
            glVertex3f(-1 ,1, 0)
            glVertex3f(1, 1, 0)
            glVertex3f(1, -1, 0)
            glEnd()
            
            glColor3f(0.0, 0.0, 0.0)
            glBegin(GL_TRIANGLES)   
            glNormal3f(0, -1, 0.707)
            glVertex3f(-1, -1, 0)
            glVertex3f(1, -1, 0)
            glVertex3f(0, 0, 1.2)
            glEnd()

            glBegin(GL_TRIANGLES)
            glNormal3f(1,0, 0.707)
            glVertex3f(1,-1,0)
            glVertex3f(1,1,0)
            glVertex3f(0,0,1.2)
            glEnd()
            
            glBegin(GL_TRIANGLES)
            glNormal3f(0,1,0.707)
            glVertex3f(1,1,0)
            glVertex3f(-1,1,0)
            glVertex3f(0,0,1.2)
            glEnd()
     
            glBegin(GL_TRIANGLES)
            glNormal3f(-1,0,0.707)
            glVertex3f(-1,1,0)
            glVertex3f(-1,-1,0)
            glVertex3f(0,0,1.2)
            glEnd()   

        
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
        
         
    def resizeGL(self, width, height):
  
        side = min(width, height)
        if side < 0:
            return
  
        glViewport((width - side) // 2, (height - side) // 2, side, side)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        
        if self.resize_lines:
            glOrtho(-50, 50, -50, 50, -50.0, 50.0)  
        else:
            glOrtho(-2, +2, -2, +2, 1.0, 15.0)      
            
        glMatrixMode(GL_MODELVIEW)            
                
                
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


    def mousePressEvent(self, event):
        # reimplemented
        self.last_pos = event.pos()

    def mouseMoveEvent(self, event):
        # reimplemented
        move_x = event.x() - self.last_pos.x()
        move_y = event.y() - self.last_pos.y()

        if event.buttons() & Qt.LeftButton:                     
            self.set_x_rotation(self.x_rotation + 8 * move_y)
            self.set_y_rotation(self.y_rotation + 8 * move_x)
            
        elif event.buttons() & Qt.RightButton:                  
            self.set_x_rotation(self.x_rotation + 8 * move_y)
            self.set_z_rotation(self.z_rotation + 8 * move_x)   

        self.last_pos = event.pos()     
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = PyQtOpenGL()
    widget.show()
    app.exec_()
