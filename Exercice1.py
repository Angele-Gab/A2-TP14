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

    def __init__(self,n):
        QWidget.__init__(self)
        self.__n = n

        box = QVBoxLayout()
        widget = []
        for i in  range (0,n) :
            widget.append(QLabel("Label"))
            for i in widget :
                box.addWidget(i)
            self.setLayout(box)




mainWidget.setLayout(layout)

mainWidget.show()
app.exec_()

if __name__ == "__main__":
   #app = QApplication([])
   win = Window(3)
   win.show()
   app.exec_()
