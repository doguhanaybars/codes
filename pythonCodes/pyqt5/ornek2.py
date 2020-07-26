import sys
from Pyqt5 import QtWidgets
from Pyqt5 import QtGui

class p_sinifi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.show()

if __name__ == '__main__':
    uygulama = QtWidgets.QApplication(sys.argv)
    pencere = p_sinifi()
    sys.exit(uygulama.exec_())

