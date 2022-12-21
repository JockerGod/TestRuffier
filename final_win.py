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
            pass
        elif exp.age <= 12 and >= 11:
            pass
        elif exp.age <= 10 and >= 9:
            if self.index >= 19.5:
                self.result = txt_res1
            elif self.index <=19.4 and >=15.5:
                self.result = txt_res2
            elif self.index <=15.4 and >=10.5:
                self.result = txt_res3
            elif self.index <=10.4 and >=5:
                self.result = txt_res4
            elif self.index <= 6.4:
                self.result = txt_res5
        elif exp.age <= 8 and >= 7:
            if self.index >= 21:
                self.result = txt_res1
            elif self.index <=20 and >=17:
                self.result = txt_res2
            elif self.index <=16.9 and >=12:
                self.result = txt_res3
            elif self.index <=11.9 and >=6.5:
                self.result = txt_res4
            elif self.index <= 6.4:
                self.result = txt_res5

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
