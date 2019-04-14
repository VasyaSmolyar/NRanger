from PyQt5 import QtWidgets

class NError(Exception):
    def __init__(self, msg):
        werr = QtWidgets.QErrorMessage()
        werr.showMessage(msg)
        werr.exec_()
