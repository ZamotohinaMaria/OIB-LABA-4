import functions as f
import logging
import sys
from PyQt5.QtWidgets import (QApplication)
from window import Window
import json

SETTINGS = {
    'hash': '4006234246b4fd2b2833d740927ab20465afad862c74b1a88ec0869bde5c836c',
    'bins': ('510126', '519778', '521178', '522828', '523701',
        '530331', '530827', '548673', '548674', '552175',
        '555928', '555933', '555949', '555957', '555921'
        ),
    'last_numbers': '0254',
}

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename='logs.log', filemode='w')
    with open('settings.json', 'w') as fp:
        json.dump(SETTINGS, fp)

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
