from Exercice1 import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *


class Curseur (QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        QWidget.setFixedSize(400,300)
        layout = QVBoxLayout()

        self.setWindowTitle("IHM")




if __name__ == "__main__":
   win = Curseur()
   win.show()
   app.exec_()

