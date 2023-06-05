import functions as f
import logging
import sys
from PyQt5.QtWidgets import (QApplication)
from window import Window
import json

SETTINGS = {
    'hash_file': 'files/hash.txt',
    'bins_file': 'files/bins.txt',
    'last_numbers_file': 'files/last_numbers.txt',
}

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename='logs.log', filemode='w')
    with open('files/settings.json', 'w') as fp:
        json.dump(SETTINGS, fp)

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
