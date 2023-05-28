from PyQt5.QtWidgets import (
    QPushButton,
    QMainWindow,
    QLabel,
    QDesktopWidget,
    QProgressBar)
from PyQt5.QtGui import (QIcon, QFont, QPixmap)
from PyQt5.QtCore import QBasicTimer
from PyQt5 import QtCore
import functions as f
import cv2

flag = 0

class Window(QMainWindow):
    def __init__(self) -> None:
        """функция инициализации
        """
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        """функция работы окна
        """    
        self.info_message = QLabel(self)
        self.info_card_num = QLabel(f'Информация о карте: ******-******-{f.data["last_num"]}', self)
        self.image_bar = QLabel(self)
        self.btn_create_bar = QPushButton('Построить график', self)
        self.btn_card_num = QPushButton('Найти номер карты', self)
        self.pbar = QProgressBar(self)
        self.timer = QBasicTimer()
        self.step = 0

        self.settings()
        
        self.setFixedWidth(self.w)
        self.setFixedHeight(self.h)
        self.center()
        self.setWindowTitle('OIB laba 4')
        self.setWindowIcon(QIcon('icon.png'))
        self.setStyleSheet('background-color: #dbdcff;')
        self.show()

    def settings(self) -> None:
        """функция настройки элементов графического интерфейса
        """
        self.w = 900
        self.h = 500
        self.info_message.setGeometry(0, 200, self.w, 300)
        self.info_message.setFont(QFont('Arial', 12))
        self.info_message.setAlignment(QtCore.Qt.AlignCenter)
        
        self.info_card_num.setGeometry(0, 50, self.w, 50)
        self.info_card_num.setFont(QFont('Arial', 12))
        self.info_card_num.setAlignment(QtCore.Qt.AlignLeft)
        
        self.pbar.setGeometry(self.w/2, self.h/2, 200, 25)
        self.pbar.close()

        self.btn_x_size = 300
        self.btn_y_size = 40
        self.luft = 0
        self.btn_font_main = QFont('Arial', 11)
        self.btn_StyleSheet_main = 'background-color: #171982; color: #dbdcff; border :1px solid;'

        self.btn_card_num.setGeometry(
            self.luft, 0, self.btn_x_size, self.btn_y_size)
        self.btn_card_num.setFont(self.btn_font_main)
        self.btn_card_num.setStyleSheet(self.btn_StyleSheet_main)
        self.btn_card_num.clicked.connect(self.card_num)

        self.btn_create_bar.setGeometry(self.btn_x_size + self.luft + 5, 0,
                                     self.btn_x_size, self.btn_y_size)
        self.btn_create_bar.setFont(self.btn_font_main)
        self.btn_create_bar.setStyleSheet(self.btn_StyleSheet_main)
        self.btn_create_bar.clicked.connect(self.create_bar)

    def center(self) -> None:
        """функция централизации окна на экране
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def print_info_message(self, text: str) -> None:
        """функция вывода информации об этапах работы программы
        и ошибках

        Args:
            text (str): выводимое сообщение
        """
        self.info_message.clear()
        self.info_message.setText(text)
        self.info_message.show()
    
    def card_num(self) -> None:
        self.info_card_num.setText(f'Информация о карте: {f.find_card_num()}')
        
    def create_bar(self) -> None:
        #f.create_bar(f.time_research())
        im = cv2.imread("researches.png", cv2.IMREAD_ANYCOLOR)
        cv2.imshow("researches", im)
        # im = QPixmap('researches.png')
        # self.image_bar.clear()
        # self.image_bar.setPixmap(im)
        # self.image_bar.adjustSize()
        # self.image_bar.move(0, 200)
        # self.image_bar.show()