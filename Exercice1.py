from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QVBoxLayout
app = QApplication([])
mainWidget = QWidget()


layout = QVBoxLayout()

label1 = QLabel("EXERCICE 1 - TP14")
label2 = QLabel("Ceci est un QLabel")
button1 = QPushButton("Ceci est un QPushButton")
button2 = QPushButton("Ceci est un deuxième QPushButton")

layout.addWidget(label1)
layout.addWidget(label2)
layout.addWidget(button1)
layout.addWidget(button2)




class Window (QWidget) :

    def __init__(self):
        QWidget.__init__(self)

        self.layout = QVBoxLayout()

        self.label = QLabel("Premier exercice du TP14")
        self.button = QPushButton("   1   ")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)





mainWidget.setLayout(layout)

mainWidget.show()
app.exec_()

if __name__ == "__main__":
   #app = QApplication([])
   win = Window()
   win.show()
   app.exec_()
