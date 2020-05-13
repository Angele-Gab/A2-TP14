from Exercice1 import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *


class Curseur (QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        QWidget.setFixedSize(400,300)
        layout = QVBoxLayout()

        self.setWindowTitle("IHM")
        self.myicon = QIcon("fr-flag.png")
        self.setWindowIcon(self.myicon)
        layout = QVBoxLayout()
        label = QLabel("Hello World")
        label.setAlignment(Qt.AlignCenter)
        progressbar = QProgressBar()
        progressbar.setValue(50)
        lineedit = QLineEdit()
        clickme = QPushButton("Click me !")
        clickme.setToolTip("PLEASE")
        layout.addWidget(label)
        layout.addWidget(progressbar)
        layout.addWidget(lineedit)
        layout.addWidget(clickme)
        self.setLayout(layout)



if __name__ == "__main__":
   win = Curseur()
   win.show()
   app.exec_()

