import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    texto = QLabel('Teste Power Calc') # type: ignore
    texto.setStyleSheet('font-size: 50px;')
    window.vertical_layout.addWidget(texto) # type: ignore

    window.show()

    app.exec()