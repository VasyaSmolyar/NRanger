import sys
import os
import main
import dialog
import engine
from errors import NError
from PyQt5 import QtWidgets, QtCore, QtGui

class MainApp(QtWidgets.QMainWindow, main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.action.triggered.connect(self.load)
        self.engine = None
        self.scene = QtWidgets.QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)
        self.gw = 700
        self.gh = 400
        self.graphicsView.setSceneRect(0,0,self.gw,self.gh)

    def load(self):
        fd = FileApp()
        fd.show()
        fd.exec()
        if fd.engine:
            self.engine = fd.engine
            self.label.setText(os.path.split(self.engine.fname)[1])
            self.engine.prepare()
            rects, norms = self.engine.getRects(self.gw,self.gh)
            self.scene.clear()
            for n in norms:
                self.scene.addRect(n[0],n[1],n[2],n[3],QtGui.QPen(QtCore.Qt.blue))
            for r in rects:
                self.scene.addRect(r[0],r[1],r[2],r[3],QtGui.QPen(QtCore.Qt.red))
            sw = self.gw / len(self.engine.data)
            w = 0
            for name in self.engine.data:
                text = self.scene.addText(name,QtGui.QFont("Times", 14))
                text.setX(w)
                w += sw
class FileApp(QtWidgets.QDialog, dialog.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.read)
        self.fname = ""
        self.engine = None

    def accept(self):
        try:
            down = float(self.lineEdit.text())
            count = self.spinBox.value()
            up = float(self.lineEdit_2.text())
            assert(self.fname != "")
            self.engine = engine.NEngine(self.fname,down,up,count)
            self.close()
        except ValueError:
            raise NError("Неверный формат вводимых данных")
        except AssertionError:
            raise NError("Не выбран файл")

    def read(self):
        self.fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбрать файл', os.getcwd())[0]
        self.label.setText(os.path.split(self.fname)[1])

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
