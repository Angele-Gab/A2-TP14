from Exercice1 import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *


class Curseur (QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(400,300)
        layout = QVBoxLayout()

        self.setWindowTitle("IHM")

        self.myicon = QIcon("fr-flag(1).png")
        self.setWindowIcon(self.myicon)

        label = QLabel("Hello World ! ")
        label.setAlignment(Qt.AlignCenter)

        barre = QProgressBar()
        barre.setValue(50)

        texte = QLineEdit()
        bouton = QPushButton("Clicke me ! ")
        bouton.setToolTip("PLEASE")

        layout.addWidget(label)
        layout.addWidget(barre)
        layout.addWidget(bouton)

        self.setLayout(layout)




if __name__ == "__main__":
   win = Curseur()
   win.show()
   app.exec_()

