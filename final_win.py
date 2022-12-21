# напиши здесь код третьего экрана приложения
from instr import *
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit

class FinalWin(QWidget):
    def __init__(self,exp):
        super().__init__()
        self.exp = exp
        self.result()
        self.set_appear()
        self.initUI()
        self.show()

# Подсчёт индекса и результата
    def result(self):
        self.index = (4*(int(self.exp.t1.text()) + int(self.exp.t2.text()) + int(self.exp.t3.text()))-200)/10

        if int(self.exp.age.text()) >= 15:
            if self.index >= 15:
                self.result = txt_res1
            elif self.index <=14.9 and self.index >=11:
                self.result = txt_res2
            elif self.index <=10.9 and self.index >=6:
                self.result = txt_res3
            elif self.index <=5.9 and self.index >=0.5:
                self.result = txt_res4
            elif self.index <= 0.4:
                self.result = txt_res5
        elif int(self.exp.age.text()) <= 14 and int(self.exp.age.text()) >= 13:
            if self.index >= 16.5:
                self.result = txt_res1
            elif self.index <=16.4 and self.index >=12.5:
                self.result = txt_res2
            elif self.index <=12.4 and self.index >=7.5:
                self.result = txt_res3
            elif self.index <=7.4 and self.index >=2:
                self.result = txt_res4
            elif self.index <= 1.9:
                self.result = txt_res5
        elif int(self.exp.age.text()) <= 12 and int(self.exp.age.text()) >= 11:
            if self.index >= 18:
                self.result = txt_res1
            elif self.index <=17.9 and self.index >=14:
                self.result = txt_res2
            elif self.index <=13.9 and self.index >=9:
                self.result = txt_res3
            elif self.index <=8.9 and self.index >=3.5:
                self.result = txt_res4
            elif self.index <= 3.4:
                self.result = txt_res5
        elif int(self.exp.age.text()) <= 10 and int(self.exp.age.text()) >= 9:
            if self.index >= 19.5:
                self.result = txt_res1
            elif self.index <=19.4 and self.index >=15.5:
                self.result = txt_res2
            elif self.index <=15.4 and self.index >=10.5:
                self.result = txt_res3
            elif self.index <=10.4 and self.index >=5:
                self.result = txt_res4
            elif self.index <= 6.4:
                self.result = txt_res5
        elif int(self.exp.age.text()) <= 8 and int(self.exp.age.text()) >= 7:
            if self.index >= 21:
                self.result = txt_res1
            elif self.index <=20 and self.index >=17:
                self.result = txt_res2
            elif self.index <=16.9 and self.index >=12:
                self.result = txt_res3
            elif self.index <=11.9 and self.index >=6.5:
                self.result = txt_res4
            elif self.index <= 6.4:
                self.result = txt_res5

            else:
                self.result = "К сожелению такой возраст не обрабатывается..."
                
# настройка окна
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        self.setStyleSheet('background-color: #190c29;')
        
# Виджеты и направляющии
    def initUI(self):
        self.text_work = QLabel(txt_workheart + str(self.result))
        self.text_work.setStyleSheet(
                'color: white;'
                'font-size: 15px'
        )

        self.text_index = QLabel(txt_index + str(self.index))
        self.text_index.setStyleSheet(
                'color: white;'
                'font-size: 15px'
        )

    # установка на левую направляющую
        self.L1 = QVBoxLayout()
        self.L1.addWidget(self.text_work, alignment = Qt.AlignCenter)
        self.L1.addWidget(self.text_index, alignment = Qt.AlignCenter)
        self.setLayout(self.L1)
