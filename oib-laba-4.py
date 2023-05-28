# |5|4006234246b4fd2b2833d740927ab20465afad862c74b1a88ec0869bde5c836c|Mastercard|Дебетовая|Альфа-банк|0254|sha256|
import sys
from PyQt5.QtWidgets import (QApplication)
from window import Window

if __name__ == '__main__':
    #logging.basicConfig(level=logging.INFO, filename='logs.log', filemode='w')
    #f.find_card_num()
    # cores = mp.cpu_count()
    # research_times = f.time_research()
    # f.create_bar(research_times, cores)
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())