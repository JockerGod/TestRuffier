# напиши здесь код основного приложения и первого экрана
from instr import *
from second_win import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        self.setStyleSheet('background-color: #190c29;')

    def initUI(self):
        self.hello_text = QLabel(text = txt_hello)
        self.hello_text.setStyleSheet(
            "color: #17e817;"
            "font-size: 25px;"
        )
        self.instruction = QLabel(text = txt_instruction)
        self.instruction.setStyleSheet(
            "color: white;"
            "font-size: 15px;"
        )
        self.button = QPushButton(text = txt_next)
        self.button.setStyleSheet(
            "color: #ffd500;"
            "font-size: 15px;"
        )
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.instruction, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.button, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

    def connects(self):
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = SecondWin()

app = QApplication([])
m_v = MainWin()
app.exec_()


