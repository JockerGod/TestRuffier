# напиши здесь код для второго экрана приложения
from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit

#Создание окна
class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connect()
        self.show()
#
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
 #       
    def initUI(self):
        self.text1 = QLabel()
        self.text2 = QLabel()
        self.text3 = QLabel()
        self.text4 = QLabel()

        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.line3 = QLineEdit()
        self.line4 = QLineEdit()
        self.line5 = QLineEdit()

        self.btn1 = QPushButton()
        self.btn2 = QPushButton()
        self.btn3 = QPushButton()
        self.btn4 = QPushButton()
#
        self.L1 = QHBoxLayout()
        self.L1.addWidget(btn1, alignment = Qt.AlignLeft)
        self.L1.addWidget(btn2, alignment = Qt.AlignLeft)
        self.L1.addWidget(btn3, alignment = Qt.AlignLeft)
        self.L1.addWidget(btn4, alignment = Qt.AlignLeft)

        self.L1.addWidget(text1, alignment = Qt.AlignLeft)
        self.L1.addWidget(text2, alignment = Qt.AlignLeft)
        self.L1.addWidget(text3, alignment = Qt.AlignLeft)
        self.L1.addWidget(text4, alignment = Qt.AlignLeft)
        self.L1.addWidget(text5, alignment = Qt.AlignLeft)

        self.L1.addWidget(line1, alignment = Qt.AlignLeft)
        self.L1.addWidget(line2, alignment = Qt.AlignLeft)
        self.L1.addWidget(line3, alignment = Qt.AlignLeft)
        self.L1.addWidget(line4, alignment = Qt.AlignLeft)
        self.L1.addWidget(line5, alignment = Qt.AlignLeft)



#
    def connect(self):
        pass
#
    def next_win(self):
        self.hide()

app = QApplication([])
Main_win = SecondWin()
app.exec_()