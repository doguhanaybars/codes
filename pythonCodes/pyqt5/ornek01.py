import sys
from PyQt5 import QtWidgets

uygulama = QtWidgets.QApplication(sys.argv)

pencere = QtWidgets.QWidget()

pencere.setWindowTitle("merhaba title")


pencere.show()

sys.exit(uygulama.exec_())