from Exercice1 import *
from PySide2.QtWidgets import *

class Test (QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        layout = QVBoxLayout()
        self.setWindowTitle("IHM")
        grille = QGridLayout()

        label = QLabel("Laissez un commentaire ")
        texte = QTextEdit()
        button1 = QPushButton(" SUCCESS ")
        button2 = QPushButton(" CANCEL ")
        layout.addWidget(label)
        layout.addWidget(texte)
        layout.addLayout(grille)
        grille.addWidget(button1,0,0)
        grille.addWidget(button2,0,1)

        self.setLayout(layout)


if __name__ == "__main__":
   #app = QApplication([])
   test = Test()
   test.show()
   app.exec_()


