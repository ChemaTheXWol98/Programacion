from PyQt5 import QtCore, QtWidgets
from third_part_2 import Ui_MainWindow

class DragDropButton(QtWidgets.QPushButton):
    def __init__(self, text, parent):
        super().__init__(text, parent)
        self.setAcceptDrops(True)
        print("it's already ok")

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.setText(event.mimeData().text())



class DragDropCombo(QtWidgets.QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)
        print("it's already ok")

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()

            

    
class MainWindow_EXEC():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)

        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        


                                           
