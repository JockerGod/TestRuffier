# напиши здесь код для второго экрана приложения
from instr import *
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit


class Export(self):
        def __init__(self, age, t1, t2, t3):
                super().__init__()
                self.age = age
                self.t1 = t1
                self.t2 = t2
                self.t3 = t3


#Создание окна
class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connect()
        self.show()

# настройка окна
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        self.setStyleSheet('background-color: #190c29;')
 
 # создание виджетов
    def initUI(self):
        self.text1 = QLabel(txt_name)
        self.text1.setStyleSheet(
                'color: white;'
                'font-size: 15px'
        )
        self.text2 = QLabel(txt_age)
        self.text2.setStyleSheet(
                'color: white;'
                'font-size: 15px'
        )
        self.text3 = QLabel(txt_test1)
        self.text3.setStyleSheet(
                'color: white;'
                'font-size: 15px'
        )
        self.text4 = QLabel(txt_test2)
        self.text4.setStyleSheet(
                'color: white;'
                'font-size: 15px'
        )
        self.text5 = QLabel(txt_test3)
        self.text5.setStyleSheet(
                'color: white;'
                'font-size: 15px'
        )

        self.text_time = QLabel("00:00:15")
        self.text_time.setStyleSheet(
                'color: white;'
                'font-size: 30px'
        )

        self.line1 = QLineEdit(text = txt_hintname)
        self.line1.setStyleSheet(
                'color: white;'
                'font-size: 15px'
        )
        self.line2 = QLineEdit(text = txt_hintage)
        self.line2.setStyleSheet(
                'color: white;'
                'font-size: 15px'
        )
        self.line3 = QLineEdit(text = txt_hinttest1)
        self.line3.setStyleSheet(
                'color: white;'
                'font-size: 15px'
        )
        self.line4 = QLineEdit(text = txt_hinttest2)
        self.line4.setStyleSheet(
                'color: white;'
                'font-size: 15px'
        )
        self.line5 = QLineEdit(text = txt_hinttest3)
        self.line5.setStyleSheet(
                'color: white;'
                'font-size: 15px'
        )

        self.btn1 = QPushButton(text = txt_starttest1)
        self.btn1.setStyleSheet(
                'color: #ffd500;'
                'font-size: 15px'
        )
        self.btn2 = QPushButton(text = txt_starttest2)
        self.btn2.setStyleSheet(
                'color: #ffd500;'
                'font-size: 15px'
        )

        self.btn2_1 = QPushButton('Прибавить приседание')
        self.btn2_1.setStyleSheet(
                'color: #ffd500;'
                'font-size: 15px'
        )

        self.btn3 = QPushButton(text = txt_starttest3)
        self.btn3.setStyleSheet(
                'color: #ffd500;'
                'font-size: 15px'
        )
        self.btn4 = QPushButton(text = txt_sendresults)
        self.btn4.setStyleSheet(
                'color: #ffd500;'
                'font-size: 15px'
        )
        


# установка на левую направляющую
        self.L1 = QVBoxLayout()
        self.L1.addWidget(self.text1, alignment = Qt.AlignLeft)
        self.L1.addWidget(self.line1, alignment = Qt.AlignLeft)
        self.L1.addWidget(self.text2, alignment = Qt.AlignLeft)
        self.L1.addWidget(self.line2, alignment = Qt.AlignLeft)
        self.L1.addWidget(self.text3, alignment = Qt.AlignLeft)
        self.L1.addWidget(self.btn1, alignment = Qt.AlignLeft)
        self.L1.addWidget(self.line3, alignment = Qt.AlignLeft)
        self.L1.addWidget(self.text4, alignment = Qt.AlignLeft)
        self.L1.addWidget(self.btn2, alignment = Qt.AlignLeft)
        self.L1.addWidget(self.btn2_1, alignment = Qt.AlignLeft)
        self.L1.addWidget(self.text5, alignment = Qt.AlignLeft)
        self.L1.addWidget(self.btn3, alignment = Qt.AlignLeft)
        self.L1.addWidget(self.line4, alignment = Qt.AlignLeft)
        self.L1.addWidget(self.line5, alignment = Qt.AlignLeft)
        self.L1.addWidget(self.btn4, alignment = Qt.AlignCenter)

# уствновка на правую направляющую
        self.L2 = QVBoxLayout()
        self.L2.addWidget(self.text_time, alignment = Qt.AlignRight)

# уствновка на центральную направляющую
        self.Main_line = QHBoxLayout()
        self.Main_line.addLayout(self.L1)
        self.Main_line.addLayout(self.L2)
        self.setLayout(self.Main_line)


    def time_start(self):
            global time
            time = QTime(0, 0, 15)
            self.timer = QTimer()
            self.timer.timeout.connect(self.time1Event)
            self.timer.start(1000)
        

    def time1Event(self):
            global time
            time = time.addSecs(-1)
            self.text_time.setText(time.toString("hh:mm:ss"))
            if time.toString("hh:mm:ss") == "00:00:00":
                self.text_time.setStyleSheet(
                        "color: red;"
                        'font-size: 30px'
                        )
                self.timer.stop()

    def time_contin(self):
            global time
            time = QTime(0, 0, 30)
            self.timer = QTimer()
            self.timer.timeout.connect(self.time2Event)
            self.timer.start(1000)

    def time2Event(self):
            global time
            time = time.addSecs(-1)
            self.text_time.setText(time.toString("hh:mm:ss")[6:8])
            if time.toString("hh:mm:ss") == "00:00:00":
                self.timer.stop()

    def time_final(self):
            global time
            time = QTime(0, 1, 0)
            self.timer = QTimer()
            self.timer.timeout.connect(self.time3Event)
            self.timer.start(1500)

    def time3Event(self):
            global time
            time = time.addSecs(-1)
            self.text_time.setText(time.toString("hh:mm:ss")[6:8])
            if int(time.toString("hh:mm:ss")[6:8]) >= 45:
                    self.text_time.setStyleSheet(
                            'color: #2aeb2a;'
                            'font-size: 45px'
                            )
            elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
                    self.text_time.setStyleSheet(
                            'color: #2aeb2a;'
                            'font-size: 45px'
                            )
            else:
                    self.text_time.setStyleSheet(
                            'color: white;'
                            'font-size: 45px'
                            )



#
    def connect(self):
        self.btn1.clicked.connect(self.time_start)
        self.btn2.clicked.connect(self.time_contin)
        self.btn3.clicked.connect(self.time_final)
        self.btn4.clicked.connect(self.next_win)

#
    def next_win(self):
        self.hide()
        self.tw = FinalWin(Export(self.line2, self.line3, self.line4, self.line5))