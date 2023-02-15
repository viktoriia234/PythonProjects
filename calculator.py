import sys
from PyQt5.QtCore import QSignalMapper
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        grid = QGridLayout(self)
        mapper = QSignalMapper(self)
        btns = (('1', '2', '3', '+'),
                ('4', '5', '6', '-'),
                ('7', '8', '9', '*'),
                ('0', '.', '=', '/'),
                )
        self.line = QLineEdit()
        self.flag = False
        grid.addWidget(self.line, 0, 0, 1, 4)
        for row in range(4):
            for col in range(4):
                button = QPushButton(btns[row][col])
                grid.addWidget(button, row + 1, col)
                button.clicked.connect(mapper.map)
                mapper.setMapping(button, button.text())
        mapper.mapped[str].connect(self.on_mapped)

    def on_mapped(self, val):
        if val == '=':
            self.flag = True
            txt = self.line.text()
            if '+' in txt:
                arr = [float(i) for i in txt.split('+')]
                self.line.setText(str(arr[0] + arr[-1]))
            elif '-' in txt:
                arr = [float(i) for i in txt.split('-')]
                self.line.setText(str(arr[0] - arr[-1]))
            elif '*' in txt:
                arr = [float(i) for i in txt.split('*')]
                self.line.setText(str(arr[0] * arr[-1]))
            elif '/' in txt:
                arr = [float(i) for i in txt.split('/')]
                self.line.setText(str(arr[0] / arr[-1]))
        else:
            if self.flag:
                self.line.clear()
                self.flag = False
            self.line.setText(self.line.text() + val)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
