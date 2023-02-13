from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout, QPushButton

class Calculator(QWidget):
    def init(self):
        super().init()
        self.initUI()

    def initUI(self):
        self.display = QLineEdit(self)
        self.display.setReadOnly(True)
        self.grid = QGridLayout()

        buttons = ["7", "8", "9", "+",
                   "4", "5", "6", "-",
                   "1", "2", "3", "*",
                   "0", ".", "=", "/", "C"]

        row = 1
        col = 0
        for button in buttons:
            if col > 3:
                col = 0
                row += 1

            btn = QPushButton(button, self)
            btn.clicked.connect(lambda _, b=button: self.append_display(b))
            self.grid.addWidget(btn, row, col)
            col += 1

        self.grid.addWidget(self.display, 0, 0, 1, 4)
        self.setLayout(self.grid)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Calculator")
        self.show()

    def append_display(self, b):
        if b == "=":
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except:
                self.display.setText("Error")
        elif b == "C":
            self.display.clear()
        else:
            self.display.insert(b)

if __name__ == "__main__":
    app = QApplication([])
    calculator = Calculator()
    app.exec()
