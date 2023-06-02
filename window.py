import cv2
import functions as f
import numpy as np
from PyQt5.QtWidgets import (
    QPushButton,
    QMainWindow,
    QLabel,
    QDesktopWidget,
    QProgressBar)
from PyQt5.QtGui import (QIcon, QFont)
from PyQt5.QtCore import QBasicTimer
from PyQt5 import QtCore


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
        self.info_card_num = QLabel(
            f'Информация о карте: ************{f.data["last_num"]}', self)
        self.image_bar = QLabel(self)
        self.btn_create_bar = QPushButton('Построить график', self)
        self.btn_card_num = QPushButton('Найти номер карты', self)
        self.btn_luna = QPushButton('Алгоритм Луна', self)
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
        self.info_message.setGeometry(0, 0, self.w, self.h)
        self.info_message.setFont(QFont('Arial', 12))
        self.info_message.setAlignment(QtCore.Qt.AlignCenter)

        self.info_card_num.setGeometry(0, 50, self.w, 50)
        self.info_card_num.setFont(QFont('Arial', 12))
        self.info_card_num.setAlignment(QtCore.Qt.AlignLeft)

        self.pbar.setGeometry(310, 125, 310, 40)
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

        self.btn_luna.setGeometry(2 * self.btn_x_size + self.luft + 10, 0,
                                  self.btn_x_size, self.btn_y_size)
        self.btn_luna.setFont(self.btn_font_main)
        self.btn_luna.setStyleSheet(self.btn_StyleSheet_main)
        self.btn_luna.clicked.connect(self.alg_luna)

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
        """функция поиска номера карты и вывода его на экран
        """
        self.print_info_message('Идет поиск')
        self.info_card_num.setText(f'Информация о карте: {f.find_card_num()}')
        self.info_message.close()

    def alg_luna(self) -> None:
        """функция проверка номера карты на валидность с помощью алгоритма Луна
        """
        card_num = f.find_card_num()
        self.info_card_num.setText(f'Информация о карте: {card_num}')
        if f.algorithm_luna(card_num):
            self.print_info_message('Номер карты валидный')
        else:
            self.print_info_message(
                'Номер карты не прошел проверку алгоритмом Луна')

    def create_bar(self) -> None:
        """функция создания и вывода на экран графика зависимости 
        времени исследования от количества использованных ядер
        """
        self.pbar.show()
        self.print_info_message('Идут исследования')
        if not self.timer.isActive():
            self.timer.start(100, self)
        research_times = np.zeros(shape=0)
        for c in range(1, 21):
            research_times = np.append(research_times, f.time_research(c))
            self.update_pbar

        f.create_bar(research_times)

        im = cv2.imread("researches.png", cv2.IMREAD_ANYCOLOR)
        cv2.imshow("researches", im)
        self.card_num
        self.info_message.close()

    def update_pbar(self) -> None:
        """функция для обновления прогресс бара
        """
        if self.step >= 100:
            self.timer.stop()
            return
        self.step += 5
        self.pbar.setValue(self.step)
