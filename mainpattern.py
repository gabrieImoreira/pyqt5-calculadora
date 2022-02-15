import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.QtWidgets import QGridLayout, QPushButton
class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Botão')
        self.btn.setStyleSheet('font-size:25px')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)

        self.btn.clicked.connect(self.acao)
        self.setCentralWidget(self.cw)

    def acao(self):
        print('Botão acionado')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()

