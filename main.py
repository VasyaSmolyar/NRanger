# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 527)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        #self.menu_2 = QtWidgets.QMenu(self.menubar)
        #self.menu_2.setObjectName("menu_2")
        #self.menu_3 = QtWidgets.QMenu(self.menubar)
        #self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        #self.action_2 = QtWidgets.QAction(MainWindow)
        #self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action)
        #self.menu_2.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())
        #self.menubar.addAction(self.menu_2.menuAction())
        #self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NRanger"))
        self.label.setText(_translate("MainWindow", "*Пустой файл"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        #self.menu_2.setTitle(_translate("MainWindow", "Вид"))
        #self.menu_3.setTitle(_translate("MainWindow", "О программе"))
        self.action.setText(_translate("MainWindow", "Загрузить новые данные"))
        #self.action_2.setText(_translate("MainWindow", "Параметры отрисовки"))


