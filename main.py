import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import untitled

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = untitled.Ui_Dialog()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())