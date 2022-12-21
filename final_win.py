from instr import *
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit

class FinalWin(QWidget):
    def __init__(self,exp):
        super().__init__()
        self.exp = exp
        self.resualt()
        self.set_appear()
        self.initUI()
        self.show()

# 
    def result(self, exp):
        self.index = (4*(int(exp.t1) + int(exp.t1) + int(exp.t1))-200)/10

        if exp.age >= 15:
            if self.index >= 15:
                self.result = txt_res1
            elif self.index <=14.9 and >=11:
                self.result = txt_res2
            elif self.index <=10.9 and >=6:
                self.result = txt_res3
            elif self.index <=5.9 and >=0.5:
                self.result = txt_res4
            elif self.index <= 0.4:
                self.result = txt_res5
        elif exp.age <= 14 and >= 13:
            if self.index >= 16.5:
                self.result = txt_res1
            elif self.index <=16.4 and >=12.5:
                self.result = txt_res2
            elif self.index <=12.4 and >=7.5:
                self.result = txt_res3
            elif self.index <=7.4 and >=2:
                self.result = txt_res4
            elif self.index <= 1.9:
                self.result = txt_res5
        elif exp.age <= 12 and >= 11:
            if self.index >= 18:
                self.result = txt_res1
            elif self.index <=17.9 and >=14:
                self.result = txt_res2
            elif self.index <=13.9 and >=9:
                self.result = txt_res3
            elif self.index <=8.9 and >=3.5:
                self.result = txt_res4
            elif self.index <= 3.4:
                self.result = txt_res5
        elif exp.age <= 10 and >= 9:
            pass
        elif exp.age <= 8 and >= 7:
            pass

# настройка окна
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        self.setStyleSheet('background-color: #190c29;')

    def initUI(self):
        self.text_work = QLabel(txt_workheart + self.result)
        self.text_work.setStyleSheet(
                'color: white;'
                'font-size: 15px'
        )

        self.text_index = QLabel(txt_index + self.index)
        self.text_index.setStyleSheet(
                'color: white;'
                'font-size: 15px'
        )