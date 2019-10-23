import sys
from PyQt5 import QtCore, QtWidgets
from Main import Ui_MainWindow
from PyQt5 import QtSql
import sqlite3
from pprint import pprint

class MainWindow_EXEC():
   
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)    
        
        self.create_DB()

        self.ui.pushButton.clicked.connect(self.print_data)
        self.model = None
        self.ui.pushButton.clicked.connect(self.sql_tableview_model)
        self.ui.pushButton_2.clicked.connect(self.sql_add_row)
        self.ui.pushButton_3.clicked.connect(self.sql_delete_row)
       
        self.MainWindow.show()
        sys.exit(app.exec_()) 
  
    def sql_delete_row(self):
        if self.model:
          
            self.model.removeRow(self.ui.tableView.currentIndex().row())
            
        else:
            self.sql_tableview_model()
              
    def sql_add_row(self):
        if self.model:
            self.model.insertRows(self.model.rowCount(), 1)
          
        else:
            self.sql_tableview_model()

    def sql_tableview_model(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('DATE.db')
        
        tableview = self.ui.tableView
        
        self.model = QtSql.QSqlTableModel()
        tableview.setModel(self.model)
        tableview.setModel(self.model)
        
        self.model.setTable('PRODUCT')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)   
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "productLine")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "textDesciption")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "htmlDescription")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "image")
        
    def print_data(self):
        sqlite_file = 'DATE.db'
        conn = sqlite3.connect(sqlite_file)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM 'PRODUCT' ORDER BY ID")
        all_rows = cursor.fetchall()
        pprint(all_rows)
        
        conn.commit()       
        conn.close()        

    def create_DB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('DATE.db')
        db.open()
    
        query = QtSql.QSqlQuery()
        
        query.exec_("create table PRODUCT (ID int(15) primary key,"
                    "productLine varchar(50), textDescription varchar(400), htmlDescription varchar(100),"
                    "image varchar(50))")
      
        query.exec_("insert into PRODUCT values(1, 'Refresco', 'Area de Bebidas', 'html\\:refrescos.com', 'none1')")
        query.exec_("insert into PRODUCT values(2, 'Pastas', 'Area de pastas', 'html\\:pastas.com', 'none2')")
        query.exec_("insert into PRODUCT values(3, 'Salud', 'Area de salud', 'html\\:salud.com', 'none3')")
        query.exec_("insert into PRODUCT values(4, 'Carnes Frias', 'Area de carnes frias', 'html\\:images.com', 'none4')")
        

if __name__ == "__main__":
    MainWindow_EXEC()
