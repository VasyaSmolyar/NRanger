import sys
import os
import main
import dialog
import engine
from errors import NError
from PyQt5 import QtWidgets

class MainApp(QtWidgets.QMainWindow, main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.action.triggered.connect(self.load)
        self.engine = None

    def load(self):
        fd = FileApp()
        fd.show()
        fd.exec()
        if fd.engine:
            self.engine = fd.engine
            self.label.setText(os.path.split(self.engine.fname)[1])

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
