import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QSizePolicy, QPushButton

class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora')
        self.setFixedSize(400,400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5) #add caixa de texto
        self.display.setDisabled(True) #desablita digitação na caixa de texto
        self.setStyleSheet('*{background: white; color: #000; font-size:25px}')

        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.create_btn(QPushButton('7'), 1, 0, 1 ,1)
        self.create_btn(QPushButton('8'), 1, 1, 1, 1)
        self.create_btn(QPushButton('9'), 1, 2, 1, 1)
        self.create_btn(QPushButton('+'), 1, 3, 1, 1)
        self.create_btn(
            QPushButton('C'), 1, 4, 1, 1,
            lambda : self.display.setText(''),
            'background:#FF0000; color: #FFF; font-weight:900'
        )

        self.create_btn(QPushButton('4'), 2, 0, 1, 1)
        self.create_btn(QPushButton('5'), 2, 1, 1, 1)
        self.create_btn(QPushButton('6'), 2, 2, 1, 1)
        self.create_btn(QPushButton('-'), 2, 3, 1, 1)
        self.create_btn(
            QPushButton('<-'), 2, 4, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1]
            ),
        'background:#FF0000; color: #FFF; font-weight:900'
        )

        self.create_btn(QPushButton('1'), 3, 0, 1, 1)
        self.create_btn(QPushButton('2'), 3, 1, 1, 1)
        self.create_btn(QPushButton('3'), 3, 2, 1, 1)
        self.create_btn(QPushButton('/'), 3, 3, 1, 1)
        self.create_btn(QPushButton(''), 3, 4, 1, 1)

        self.create_btn(QPushButton('.'), 4, 0, 1, 1)
        self.create_btn(QPushButton('0'), 4, 1, 1, 1)
        self.create_btn(QPushButton(''), 4, 2, 1, 1)
        self.create_btn(QPushButton('*'), 4, 3, 1, 1)
        self.create_btn(
            QPushButton('='), 4, 4, 1, 1,
            self.eval_equal
        )


        self.setCentralWidget(self.cw)

    def create_btn(self, btn, row, col, rowspan, colspan, funcao=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_equal(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('Conta inválida')
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
