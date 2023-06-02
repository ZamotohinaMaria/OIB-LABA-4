import functions as f
import logging
import sys
from PyQt5.QtWidgets import (QApplication)
from window import Window


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename='logs.log', filemode='w')

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
