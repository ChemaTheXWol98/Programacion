# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\third_part_2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 427)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-1, 1, 471, 411))
        self.tabWidget.setAcceptDrops(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_drag_drop = QtWidgets.QWidget()
        self.tab_drag_drop.setObjectName("tab_drag_drop")
        self.comboBox = QtWidgets.QComboBox(self.tab_drag_drop)
        self.comboBox.setGeometry(QtCore.QRect(130, 20, 111, 22))
        self.comboBox.setMinimumSize(QtCore.QSize(111, 22))
        self.comboBox.setAcceptDrops(True)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_drag_drop)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 113, 21))
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab_drag_drop)
        self.pushButton.setGeometry(QtCore.QRect(250, 20, 161, 23))
        self.pushButton.setAcceptDrops(True)
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.tab_drag_drop)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 211, 331))
        self.listWidget.setDragEnabled(True)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_drag_drop)
        self.listWidget_2.setGeometry(QtCore.QRect(230, 50, 221, 331))
        self.listWidget_2.setDragEnabled(True)
        self.listWidget_2.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.listWidget_2.setObjectName("listWidget_2")
        self.tabWidget.addTab(self.tab_drag_drop, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Widget 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Widget 2"))
        self.pushButton.setText(_translate("MainWindow", "DragButton"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Item 1"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Item2"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Item 3"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Item 4"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_drag_drop), _translate("MainWindow", "Drag & Drop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
